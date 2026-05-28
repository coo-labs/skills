#!/usr/bin/env python3
"""
inventory.py - walk one or more repos for Claude Code skills/agents and emit
a structured inventory that validates against ./schema.json.

The script is path-agnostic: pass repo paths positionally. It discovers
SKILL.md files under <repo>/.claude/skills/ and <repo>/skills/, and agent
.md files under <repo>/.claude/agents/ and <repo>/agents/ (including
reference/ subdirs). Vendoring is detected from UPSTREAM.md / VENDORED.md
markers at multiple levels.

Usage:
  inventory.py REPO [REPO ...] [--out PATH] [--schema schema.json]
               [--transcripts DIR] [--type-rules FILE]
  inventory.py --validate-only --out inventory.json --schema schema.json
"""

import argparse
import json
import os
import re
import subprocess
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False


SCHEMA_VERSION = "1.0.0"

# ---------------------------------------------------------------------------
# Frontmatter parsing
# ---------------------------------------------------------------------------

FRONTMATTER_RE = re.compile(r'\A---\s*\n(.*?\n)---\s*\n', re.DOTALL)


def parse_frontmatter(text):
    """Return (frontmatter_dict, body, frontmatter_text)."""
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, text, ""
    fm_text = m.group(1)
    body = text[m.end():]
    if HAS_YAML:
        try:
            data = yaml.safe_load(fm_text) or {}
            if not isinstance(data, dict):
                data = _fallback_parse(fm_text)
        except Exception:
            data = _fallback_parse(fm_text)
    else:
        data = _fallback_parse(fm_text)
    return data, body, fm_text


def _fallback_parse(text):
    """Minimal `key: value` parser for simple frontmatter."""
    result = {}
    for line in text.splitlines():
        if not line.strip() or line.strip().startswith('#'):
            continue
        m = re.match(r'^([A-Za-z_][\w-]*)\s*:\s*(.*)$', line)
        if m:
            k, v = m.group(1), m.group(2).strip()
            if (v.startswith('"') and v.endswith('"')) or \
               (v.startswith("'") and v.endswith("'")):
                v = v[1:-1]
            result[k] = v
    return result


def _stringify(v):
    """Frontmatter values may be str, list, dict; render as a single string for the entry."""
    if v is None:
        return None
    if isinstance(v, list):
        return ", ".join(str(x) for x in v)
    if isinstance(v, dict):
        return json.dumps(v, sort_keys=True)
    return str(v)


# ---------------------------------------------------------------------------
# Declared metadata (agentskills.io spec: metadata is a free-form map at the
# top level of frontmatter, intended as the extension surface for host tools)
# ---------------------------------------------------------------------------

# Keys inside `metadata:` the inventory recognizes. Any other keys are passed
# through verbatim in the `metadata` block but don't override anything.
METADATA_KEYS_OVERRIDE_TYPE      = ("type",)
METADATA_KEYS_OVERRIDE_VENDORING = ("vendoring",)
METADATA_VENDOR_SOURCE_KEYS      = ("upstream", "commit", "snapshot_date", "local_edits")


def _extract_metadata(fm):
    """Pull the metadata block out of frontmatter, coercing to JSON-safe scalars.

    The agentskills.io spec calls for a map of string keys to string values.
    PyYAML autotypes some scalars (dates, timestamps) into Python objects
    that aren't JSON-serializable, so we stringify anything that isn't a
    primitive scalar.
    """
    md = fm.get("metadata")
    if not isinstance(md, dict):
        return {}
    out = {}
    for k, v in md.items():
        if v is None or isinstance(v, (str, int, float, bool)):
            out[k] = v
        else:
            out[k] = str(v)
    return out


# ---------------------------------------------------------------------------
# Vendoring detection
# ---------------------------------------------------------------------------

VENDOR_MARKER_NAMES = ("UPSTREAM.md", "VENDORED.md")


def find_vendor_markers(repo_path):
    """Return list of (path, content) for vendor-marker files in the repo."""
    repo_path = Path(repo_path)
    out = []
    search_dirs = [
        repo_path,
        repo_path / ".claude",
        repo_path / ".claude" / "skills",
        repo_path / ".claude" / "agents",
        repo_path / "skills",
        repo_path / "agents",
    ]
    for d in search_dirs:
        if not d.is_dir():
            continue
        for name in VENDOR_MARKER_NAMES:
            f = d / name
            if f.is_file():
                try:
                    out.append((f, f.read_text(encoding="utf-8", errors="replace")))
                except Exception:
                    pass
    # Per-skill markers (one level deeper)
    for sk_root in (repo_path / ".claude" / "skills", repo_path / "skills"):
        if not sk_root.is_dir():
            continue
        for child in sk_root.iterdir():
            if child.is_dir():
                for name in VENDOR_MARKER_NAMES:
                    f = child / name
                    if f.is_file():
                        try:
                            out.append((f, f.read_text(encoding="utf-8", errors="replace")))
                        except Exception:
                            pass
    return out


def parse_vendor_marker(content):
    """Parse a marker file into {section_name: info_dict}.

    Sections are `## ...` headings; a single section may list multiple
    comma-separated names. Path-like names (e.g. `agents/foo.md`) are
    reduced to the basename without extension.
    """
    out = {}
    sections = re.split(r"^##\s+", content, flags=re.MULTILINE)
    for sec in sections[1:]:
        lines = sec.splitlines()
        if not lines:
            continue
        header = lines[0].strip()
        if header.lower().startswith(("skills not ", "relocation", "bump procedure",
                                       "conceptual provenance", "why we did")):
            continue
        raw = [s.strip().rstrip("/") for s in header.split(",")]
        names = []
        for rn in raw:
            if "/" in rn:
                rn = rn.rsplit("/", 1)[-1]
            if rn.endswith(".md"):
                rn = rn[:-3]
            if rn:
                names.append(rn)
        body = "\n".join(lines[1:])
        info = {}
        for field, pat in (
            ("upstream", r"\*\*(?:Source repo|Upstream)\*\*:\s*<?([^\s>]+)>?"),
            ("commit", r"\*\*Source commit\*\*:\s*`?([0-9a-f]{7,40})`?"),
            ("snapshot_date", r"\*\*Snapshot date\*\*:\s*([0-9-]+)"),
        ):
            m = re.search(pat, body, re.IGNORECASE)
            if m:
                info[field] = m.group(1)
        if re.search(r"local\s*edits", body, re.IGNORECASE):
            le = re.search(
                r"\*\*Local edits\*\*:\s*(.+?)(?:\n\n|\n\*\*|\Z)",
                body, re.DOTALL | re.IGNORECASE,
            )
            edits_text = (le.group(1).strip() if le else "")
            info["local_edits"] = edits_text[:500]
            # "only the `name:` field" / "only ... name ... field" / "name: rename only"
            only_name_edit = bool(re.search(
                r"only.{0,40}name.{0,40}field|name.{0,20}field.{0,20}only|name.{0,10}rename",
                edits_text, re.IGNORECASE,
            ))
            info["local_edits_significant"] = bool(edits_text) and not only_name_edit
        for name in names:
            out[name] = info
    return out


def build_vendor_index(repo_path):
    """Aggregate marker info into {entry_name: info} for the repo."""
    repo_path = Path(repo_path)
    markers = find_vendor_markers(repo_path)
    index = {}
    for path, content in markers:
        parsed = parse_vendor_marker(content)
        for name, info in parsed.items():
            info_copy = dict(info)
            info_copy.setdefault("vendor_file", str(path.relative_to(repo_path)))
            existing = index.get(name, {})
            index[name] = {**existing, **info_copy}
        # Per-skill marker (lives inside the skill dir): mark the parent dir
        parent = path.parent
        parent_is_skill_dir = (
            parent.parent.name in ("skills",) or
            (parent.parent.name == "skills" and parent.parent.parent.name == ".claude")
        )
        if parent_is_skill_dir and parent.name not in ("skills", "agents", ".claude"):
            agg = {}
            for info in parsed.values():
                agg.update({k: v for k, v in info.items() if v})
            agg.setdefault("vendor_file", str(path.relative_to(repo_path)))
            existing = index.get(parent.name, {})
            index[parent.name] = {**existing, **agg}
    return index


def classify_vendoring(name, vendor_index):
    """Return ('custom'|'vendored'|'vendored-customized'|'unknown', info)."""
    info = vendor_index.get(name)
    if not info:
        return "custom", None
    if info.get("local_edits_significant"):
        return "vendored-customized", info
    return "vendored", info


# ---------------------------------------------------------------------------
# Type classification (heuristic, override-able)
# ---------------------------------------------------------------------------

DEFAULT_TYPE_RULES = {
    "skill_rules": [
        {"if_name_regex": r"-docs$|^docs-",       "type": "documentation", "signal": "name suffix -docs"},
        {"if_name_regex": r"-mode$",               "type": "role",          "signal": "name suffix -mode"},
        {"if_name_in": ["skill-creator", "tool-creator", "adapt-skill"],
         "type": "meta", "signal": "meta-skill name"},
        {"if_name_regex": r"^code-review|^simplify$|review$",
         "type": "review", "signal": "review-style name"},
        {"if_name_in": ["agentmail", "cf-wrangler"],
         "type": "api-service", "signal": "named external-service skill"},
        {"if_has_subdir": "scripts", "if_desc_regex": r"\b(cli|wrangler|api|service|cloudflare)\b",
         "type": "api-service", "signal": "scripts/ + service description"},
        {"if_has_subdir": "scripts", "type": "procedural", "signal": "has scripts/ subdir"},
        {"if_has_subdir": "references", "type": "reference", "signal": "has references/ subdir"},
        {"if_name_regex": r"^memo(-|$)|^post-|^tag-|^request-|^status-|^end-session$|^tagging-",
         "type": "procedural", "signal": "procedural-style name (memo/post/tag/request/status/end-session/tagging)"},
        {"if_desc_regex": r"^\s*(Run|Apply|Find|Post|Author|Create|Audit|Search|Draft|File|Reconcile|Render|Navigate|Configure|Generate|Launch|Deploy|Compute|Build|Look up|Initialize|Verify|Review)\b",
         "type": "procedural", "signal": "procedural verb at start of description"},
        {"if_desc_regex": r"\b(draft and file|reconcile|render|navigate|configure|generate|run the|executes? a|walks? the|writes? a)\b",
         "type": "procedural", "signal": "procedural verb in description"},
    ],
    "agent_rules": [
        {"if_name_regex": r"auditor$|^safety-|^emancipatory-", "type": "agent-auditor",     "signal": "auditor-style name"},
        {"if_name_regex": r"review|discriminator",             "type": "agent-reviewer",    "signal": "reviewer-style name"},
        {"if_name_regex": r"research|investigator|explore",    "type": "agent-researcher",  "signal": "researcher-style name"},
        {"if_name_regex": r"dispatch|parallel",                "type": "agent-orchestrator","signal": "orchestrator-style name"},
        {"if_name_regex": r"curator|closer|analyzer|interpreter",
         "type": "agent-specialist", "signal": "specialist-style name"},
    ],
}


def classify_type(name, kind, fm, bundle, rules):
    desc = (fm.get("description") or "").lower()
    rule_set = rules["agent_rules" if kind == "agent" else "skill_rules"]
    for rule in rule_set:
        if "if_name_regex" in rule and not re.search(rule["if_name_regex"], name):
            continue
        if "if_name_in" in rule and name not in rule["if_name_in"]:
            continue
        if "if_has_subdir" in rule:
            sub = rule["if_has_subdir"]
            if sub not in bundle or bundle[sub].get("count", 0) <= 0:
                continue
        if "if_desc_regex" in rule and not re.search(rule["if_desc_regex"], desc, re.IGNORECASE):
            continue
        return rule["type"], [rule["signal"]]
    fallback = "agent-general" if kind == "agent" else "unknown"
    return fallback, ["no heuristic matched"]


# ---------------------------------------------------------------------------
# Bundle inspection
# ---------------------------------------------------------------------------

KNOWN_BUNDLE_SUBDIRS = {"scripts", "references", "assets", "agents",
                        "evals", "eval-viewer", "templates"}


def inspect_bundle(skill_dir):
    out = {}
    if not skill_dir.is_dir():
        return out
    other_files = []
    other_dirs = {}
    for child in sorted(skill_dir.iterdir()):
        name = child.name
        if child.is_dir():
            files = sorted(p.name for p in child.rglob("*") if p.is_file())
            entry = {"count": len(files), "files": files[:50]}
            if name in KNOWN_BUNDLE_SUBDIRS:
                out[name] = entry
            else:
                other_dirs[name] = {"count": len(files)}
        else:
            if name == "SKILL.md":
                continue
            if name in VENDOR_MARKER_NAMES:
                out["vendor_file"] = name
            elif name.startswith("LICENSE"):
                out["license"] = name
            else:
                other_files.append(name)
    if other_files:
        out["other"] = other_files
    if other_dirs:
        out["other_dirs"] = other_dirs
    return out


# ---------------------------------------------------------------------------
# Git metadata
# ---------------------------------------------------------------------------

def _git(repo_path, *args, timeout=10):
    try:
        r = subprocess.run(
            ["git", "-C", str(repo_path), *args],
            capture_output=True, text=True, timeout=timeout,
        )
        if r.returncode != 0:
            return None
        return r.stdout
    except Exception:
        return None


def git_first_commit(repo_path, relpath):
    out = _git(repo_path, "log", "--follow", "--format=%aI", "--", relpath)
    if not out:
        return None
    lines = [ln for ln in out.strip().splitlines() if ln]
    return lines[-1] if lines else None


def git_last_commit(repo_path, relpath):
    out = _git(repo_path, "log", "-1", "--format=%aI", "--", relpath)
    return (out.strip() or None) if out is not None else None


def git_commits_count(repo_path, relpath):
    out = _git(repo_path, "log", "--follow", "--format=%H", "--", relpath)
    if out is None:
        return 0
    return len([ln for ln in out.strip().splitlines() if ln])


def git_remote_slug(repo_path):
    out = _git(repo_path, "remote", "get-url", "origin", timeout=5)
    if out:
        m = re.search(r"[:/]([^/:]+/[^/:]+?)(?:\.git)?/?$", out.strip())
        if m:
            return m.group(1)
    return Path(repo_path).name


def git_head_sha(repo_path):
    out = _git(repo_path, "rev-parse", "HEAD", timeout=5)
    return (out.strip() or None) if out is not None else None


# ---------------------------------------------------------------------------
# Transcript usage scan
# ---------------------------------------------------------------------------

COMMAND_TAG_RE = re.compile(r"<command-name>([^<\n]+)</command-name>")


def scan_transcripts(transcripts_dir, names):
    """Walk all .jsonl files under transcripts_dir; count skill invocations.

    A skill is "invoked" when:
      - a <command-name>NAME</command-name> token appears in any text content
        (the harness inserts this for slash commands and skill invocations), or
      - a tool_use block has name=='Skill' with input.skill==NAME.
    Returns (usage_map, files_scanned).
    """
    usage = {n: {"invocations": 0, "sessions": set(), "last_iso": None}
             for n in names}
    files_scanned = 0
    if not transcripts_dir or not transcripts_dir.is_dir():
        return _finalize_usage(usage), 0

    for f in sorted(transcripts_dir.rglob("*.jsonl")):
        files_scanned += 1
        try:
            with f.open("r", encoding="utf-8", errors="replace") as fh:
                for line in fh:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        rec = json.loads(line)
                    except Exception:
                        continue
                    _scan_record(rec, usage)
        except Exception:
            continue
    return _finalize_usage(usage), files_scanned


def _scan_record(rec, usage):
    sid = rec.get("sessionId") or rec.get("session_id") or "unknown"
    ts = rec.get("timestamp") or ""

    def hit(nm):
        if nm not in usage:
            return
        usage[nm]["invocations"] += 1
        usage[nm]["sessions"].add(sid)
        if ts and (usage[nm]["last_iso"] is None or ts > usage[nm]["last_iso"]):
            usage[nm]["last_iso"] = ts

    msg = rec.get("message")
    content = msg.get("content") if isinstance(msg, dict) else rec.get("content")

    if isinstance(content, str):
        for m in COMMAND_TAG_RE.findall(content):
            hit(m.split()[0].lstrip("/"))
    elif isinstance(content, list):
        for blk in content:
            if not isinstance(blk, dict):
                continue
            if blk.get("type") == "text":
                for m in COMMAND_TAG_RE.findall(blk.get("text") or ""):
                    hit(m.split()[0].lstrip("/"))
            elif blk.get("type") == "tool_use":
                if blk.get("name") in ("Skill", "skill"):
                    nm = (blk.get("input") or {}).get("skill")
                    if nm:
                        hit(nm)


def _finalize_usage(usage):
    return {
        n: {
            "invocations": v["invocations"],
            "unique_sessions": len(v["sessions"]),
            "last_iso": v["last_iso"],
        }
        for n, v in usage.items()
    }


# ---------------------------------------------------------------------------
# Discovery
# ---------------------------------------------------------------------------

def discover_skills(repo_path):
    repo_path = Path(repo_path)
    for skills_root in (repo_path / ".claude" / "skills", repo_path / "skills"):
        if not skills_root.is_dir():
            continue
        for child in sorted(skills_root.iterdir()):
            if not child.is_dir():
                continue
            skill_md = child / "SKILL.md"
            if skill_md.is_file():
                yield child, skill_md


def discover_agents(repo_path):
    repo_path = Path(repo_path)
    for agents_root in (repo_path / ".claude" / "agents", repo_path / "agents"):
        if not agents_root.is_dir():
            continue
        for entry in sorted(agents_root.iterdir()):
            if entry.is_file() and entry.suffix == ".md":
                yield agents_root, entry
            elif entry.is_dir():
                for sub in sorted(entry.iterdir()):
                    if sub.is_file() and sub.suffix == ".md":
                        yield agents_root, sub


# ---------------------------------------------------------------------------
# Entry assembly
# ---------------------------------------------------------------------------

def _apply_declared_metadata(declared, heur_type, heur_signals, heur_vendoring, heur_vinfo):
    """Apply declared metadata overrides; return resolved (type, type_source,
    type_signals, vendoring, vendoring_source, vendor_source)."""
    type_label, type_source, signals = heur_type, "heuristic", heur_signals
    if declared.get("type"):
        type_label = str(declared["type"])
        type_source = "declared"
        signals = [f"declared metadata.type = {type_label!r}"]

    vendoring, vendoring_source = heur_vendoring, "heuristic"
    vendor_source = heur_vinfo
    if declared.get("vendoring"):
        vendoring = str(declared["vendoring"])
        vendoring_source = "declared"
        # When vendoring is declared, build vendor_source from declared keys
        declared_vendor = {k: declared[k] for k in METADATA_VENDOR_SOURCE_KEYS if k in declared}
        if declared_vendor:
            vendor_source = {**(heur_vinfo or {}), **declared_vendor, "vendor_file": "frontmatter.metadata"}
        elif heur_vinfo is None:
            vendor_source = {"vendor_file": "frontmatter.metadata"}
    return type_label, type_source, signals, vendoring, vendoring_source, vendor_source


def process_skill(skill_dir, skill_md, repo_path, repo_slug, vendor_index, type_rules):
    text = skill_md.read_text(encoding="utf-8", errors="replace")
    fm, body, _ = parse_frontmatter(text)
    name = fm.get("name") or skill_dir.name
    bundle = inspect_bundle(skill_dir)
    heur_vendoring, heur_vinfo = classify_vendoring(name, vendor_index)
    heur_type, heur_signals = classify_type(name, "skill", fm, bundle, type_rules)
    declared = _extract_metadata(fm)
    type_label, type_source, type_signals, vendoring, vendoring_source, vendor_source = \
        _apply_declared_metadata(declared, heur_type, heur_signals, heur_vendoring, heur_vinfo)
    rel = skill_md.relative_to(repo_path).as_posix()
    rel_dir = skill_dir.relative_to(repo_path).as_posix()
    return {
        "kind": "skill",
        "name": name,
        "repo": repo_slug,
        "repo_dir": rel_dir,
        "entry_path": rel,
        "frontmatter": {
            "name":          _stringify(fm.get("name")),
            "description":   _stringify(fm.get("description")),
            "argument_hint": _stringify(fm.get("argument-hint") or fm.get("argument_hint")),
            "allowed_tools": _stringify(fm.get("allowed-tools") or fm.get("allowed_tools")),
            "tools":         _stringify(fm.get("tools")),
            "model":         _stringify(fm.get("model")),
            "license":       _stringify(fm.get("license")),
            "compatibility": _stringify(fm.get("compatibility")),
            "metadata":      declared or None,
        },
        "description_chars": len(fm.get("description") or ""),
        "body_chars":        len(body),
        "total_bytes":       skill_md.stat().st_size,
        "total_lines":       text.count("\n") + (0 if text.endswith("\n") else 1),
        "vendoring":         vendoring,
        "vendoring_source":  vendoring_source,
        "vendor_source":     vendor_source,
        "type":              type_label,
        "type_source":       type_source,
        "type_signals":      type_signals,
        "is_reference":      False,
        "bundle":            bundle,
        "git": {
            "first_commit_iso": git_first_commit(repo_path, rel),
            "last_commit_iso":  git_last_commit(repo_path, rel),
            "commits_count":    git_commits_count(repo_path, rel),
        },
    }


def process_agent(agents_root, agent_md, repo_path, repo_slug, vendor_index, type_rules):
    text = agent_md.read_text(encoding="utf-8", errors="replace")
    fm, body, _ = parse_frontmatter(text)
    name = fm.get("name") or agent_md.stem
    heur_vendoring, heur_vinfo = classify_vendoring(name, vendor_index)
    heur_type, heur_signals = classify_type(name, "agent", fm, {}, type_rules)
    declared = _extract_metadata(fm)
    type_label, type_source, type_signals, vendoring, vendoring_source, vendor_source = \
        _apply_declared_metadata(declared, heur_type, heur_signals, heur_vendoring, heur_vinfo)
    rel = agent_md.relative_to(repo_path).as_posix()
    parts = agent_md.relative_to(agents_root).parts
    is_reference = len(parts) > 1 and parts[0] == "reference"
    if is_reference:
        type_signals = list(type_signals) + ["under reference/ subdir"]
    return {
        "kind": "agent",
        "name": name,
        "repo": repo_slug,
        "repo_dir": agent_md.parent.relative_to(repo_path).as_posix(),
        "entry_path": rel,
        "frontmatter": {
            "name":          _stringify(fm.get("name")),
            "description":   _stringify(fm.get("description")),
            "argument_hint": _stringify(fm.get("argument-hint") or fm.get("argument_hint")),
            "allowed_tools": _stringify(fm.get("allowed-tools") or fm.get("allowed_tools")),
            "tools":         _stringify(fm.get("tools")),
            "model":         _stringify(fm.get("model")),
            "license":       _stringify(fm.get("license")),
            "compatibility": _stringify(fm.get("compatibility")),
            "metadata":      declared or None,
        },
        "description_chars": len(fm.get("description") or ""),
        "body_chars":        len(body),
        "total_bytes":       agent_md.stat().st_size,
        "total_lines":       text.count("\n") + (0 if text.endswith("\n") else 1),
        "vendoring":         vendoring,
        "vendoring_source":  vendoring_source,
        "vendor_source":     vendor_source,
        "type":              type_label,
        "type_source":       type_source,
        "type_signals":      type_signals,
        "is_reference":      is_reference,
        "bundle":            {},
        "git": {
            "first_commit_iso": git_first_commit(repo_path, rel),
            "last_commit_iso":  git_last_commit(repo_path, rel),
            "commits_count":    git_commits_count(repo_path, rel),
        },
    }


# ---------------------------------------------------------------------------
# Minimal JSON Schema validator (subset: type, required, properties,
# additionalProperties, items, enum, minimum, $ref to #/$defs, oneOf via list types)
# ---------------------------------------------------------------------------

class SchemaError(Exception):
    pass


def validate(data, schema, root=None, path="$"):
    if root is None:
        root = schema
    if "$ref" in schema:
        ref = schema["$ref"]
        if not ref.startswith("#/"):
            raise SchemaError(f"{path}: only local $ref supported ({ref})")
        target = root
        for part in ref[2:].split("/"):
            target = target[part]
        return validate(data, target, root, path)
    if "type" in schema:
        types = schema["type"] if isinstance(schema["type"], list) else [schema["type"]]
        if not any(_typecheck(data, t) for t in types):
            raise SchemaError(
                f"{path}: expected type {types}, got "
                f"{'null' if data is None else type(data).__name__}"
            )
        if data is None:
            return
    if "enum" in schema and data not in schema["enum"]:
        raise SchemaError(f"{path}: {data!r} not in enum {schema['enum']}")
    if isinstance(data, dict):
        for req in schema.get("required", []):
            if req not in data:
                raise SchemaError(f"{path}: missing required {req!r}")
        props = schema.get("properties", {})
        add_props = schema.get("additionalProperties", True)
        for k, v in data.items():
            if k in props:
                validate(v, props[k], root, f"{path}.{k}")
            else:
                if add_props is False:
                    raise SchemaError(f"{path}.{k}: additional property not allowed")
                if isinstance(add_props, dict):
                    validate(v, add_props, root, f"{path}.{k}")
    if isinstance(data, list) and "items" in schema:
        for i, item in enumerate(data):
            validate(item, schema["items"], root, f"{path}[{i}]")
    if isinstance(data, (int, float)) and not isinstance(data, bool):
        if "minimum" in schema and data < schema["minimum"]:
            raise SchemaError(f"{path}: {data} below minimum {schema['minimum']}")


def _typecheck(data, t):
    return {
        "object":  isinstance(data, dict),
        "array":   isinstance(data, list),
        "string":  isinstance(data, str),
        "integer": isinstance(data, int) and not isinstance(data, bool),
        "number":  isinstance(data, (int, float)) and not isinstance(data, bool),
        "boolean": isinstance(data, bool),
        "null":    data is None,
    }.get(t, False)


# ---------------------------------------------------------------------------
# Summary + driver
# ---------------------------------------------------------------------------

def _summarize(entries):
    by_repo, by_kind, by_type, by_vendoring = (defaultdict(int) for _ in range(4))
    declared_type = declared_vendoring = 0
    for e in entries:
        by_repo[e["repo"]] += 1
        by_kind[e["kind"]] += 1
        by_type[e["type"]] += 1
        by_vendoring[e["vendoring"]] += 1
        if e.get("type_source") == "declared":
            declared_type += 1
        if e.get("vendoring_source") == "declared":
            declared_vendoring += 1
    return {
        "count_total": len(entries),
        "by_repo": dict(by_repo),
        "by_kind": dict(by_kind),
        "by_type": dict(by_type),
        "by_vendoring": dict(by_vendoring),
        "declared_share": {
            "type":      declared_type,
            "vendoring": declared_vendoring,
        },
    }


def load_schema(schema_path):
    if schema_path and Path(schema_path).is_file():
        return json.loads(Path(schema_path).read_text())
    default = Path(__file__).resolve().parent / "schema.json"
    if default.is_file():
        return json.loads(default.read_text())
    raise SystemExit(f"schema file not found ({schema_path or default})")


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="Walk one or more repos for Claude Code skills/agents."
    )
    ap.add_argument("repos", nargs="*", help="Paths to repos to scan")
    ap.add_argument("--out", default="-", help='Output JSON path; "-" = stdout')
    ap.add_argument("--schema", default=None,
                    help="Path to schema.json (default: alongside this script)")
    ap.add_argument("--transcripts", default=None,
                    help="Directory to recursively scan for *.jsonl transcripts")
    ap.add_argument("--type-rules", default=None,
                    help="Optional JSON file of type-classification rules to merge over defaults")
    ap.add_argument("--validate-only", action="store_true",
                    help="Validate --out against --schema and exit (no rescan)")
    args = ap.parse_args(argv)

    schema = load_schema(args.schema)

    if args.validate_only:
        if args.out == "-":
            ap.error("--validate-only requires --out FILE")
        data = json.loads(Path(args.out).read_text())
        validate(data, schema)
        print(f"OK: {args.out} validates against schema", file=sys.stderr)
        return 0

    if not args.repos:
        ap.error("one or more repo paths required")

    type_rules = DEFAULT_TYPE_RULES
    if args.type_rules:
        override = json.loads(Path(args.type_rules).read_text())
        type_rules = {**DEFAULT_TYPE_RULES, **override}

    repo_meta, entries, names = [], [], set()
    for r in args.repos:
        rp = Path(r).resolve()
        if not rp.is_dir():
            print(f"WARN: {rp} is not a directory; skipping", file=sys.stderr)
            continue
        slug = git_remote_slug(rp)
        repo_meta.append({"path": str(rp), "remote": slug, "head_sha": git_head_sha(rp)})
        vindex = build_vendor_index(rp)
        for skill_dir, skill_md in discover_skills(rp):
            e = process_skill(skill_dir, skill_md, rp, slug, vindex, type_rules)
            entries.append(e); names.add(e["name"])
        for agents_root, agent_md in discover_agents(rp):
            e = process_agent(agents_root, agent_md, rp, slug, vindex, type_rules)
            entries.append(e); names.add(e["name"])

    transcripts_meta = None
    if args.transcripts:
        usage, n = scan_transcripts(Path(args.transcripts), names)
        transcripts_meta = {"dir": str(Path(args.transcripts).resolve()),
                            "files_scanned": n}
        for e in entries:
            e["usage"] = usage.get(e["name"],
                                   {"invocations": 0, "unique_sessions": 0, "last_iso": None})

    entries.sort(key=lambda e: (e["repo"], e["kind"], e["name"]))
    output = {
        "schema_version": SCHEMA_VERSION,
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "scan": {"repos": repo_meta, "transcripts": transcripts_meta},
        "entries": entries,
        "summary": _summarize(entries),
    }

    validate(output, schema)

    txt = json.dumps(output, indent=2)
    if args.out == "-":
        print(txt)
    else:
        Path(args.out).write_text(txt + "\n")
        print(f"Wrote {len(entries)} entries to {args.out} "
              f"(validated against schema)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
