#!/usr/bin/env python3
"""
backfill-metadata.py — patch a `metadata:` block into each SKILL.md /
agent .md frontmatter, sourcing the declarations from an inventory.json
produced by `inventory.py`.

Per the agentskills.io spec, `metadata` is a string-keyed map intended
as the host-tool extension surface. This script writes:
  - `metadata.type`     ← inventory.entry.type
  - `metadata.vendoring` ← inventory.entry.vendoring
  - `metadata.upstream` / `commit` / `snapshot_date` / `local_edits` /
    `license` — for vendored entries, from VENDOR_OVERRIDES below

Existing frontmatter content is preserved exactly; the new block is
inserted before the closing `---`. Files already carrying a top-level
`metadata:` key are skipped (idempotent — safe to re-run).

Usage:
  backfill-metadata.py INVENTORY.json --repo OWNER/REPO [--dry-run]
"""

import argparse
import json
import re
import sys
from pathlib import Path


FRONTMATTER_RE = re.compile(r"\A(---\s*\n)(.*?)(\n---\s*\n)", re.DOTALL)


# Hand-curated provenance for vendored entries that the inventory parser
# couldn't extract cleanly (the bold-style `**Upstream:**` and Anthropic's
# unlinked "search the public skill-creator repository" cases).
VENDOR_OVERRIDES = {
    ("coo-labs/coo-memory", "cf-wrangler"): {
        "upstream":      "https://github.com/cloudflare/skills",
        "commit":        "7c449def4e0c63daa27212d853094e4c8e37bbe8",
        "snapshot_date": "2026-04-28",
        "local_edits":   "name-only (renamed for namespacing in our aggregator)",
        "license":       "Apache-2.0",
    },
    ("coo-labs/coo-memory", "cf-workers-best-practices"): {
        "upstream":      "https://github.com/cloudflare/skills",
        "commit":        "7c449def4e0c63daa27212d853094e4c8e37bbe8",
        "snapshot_date": "2026-04-28",
        "local_edits":   "name-only (renamed for namespacing in our aggregator)",
        "license":       "Apache-2.0",
    },
    ("coo-labs/coo-harness", "skill-creator"): {
        # Upstream URL is not pinned in VENDORED.md; left undeclared
        # rather than speculating
        "local_edits":   "none (verbatim per VENDORED.md maintenance rule)",
        "license":       "Apache-2.0",
    },
    ("coo-labs/skills", "dispatching-parallel-agents"): {
        "upstream":      "https://github.com/obra/superpowers",
        "local_edits":   "generalized project-specific paths for portability across substrates",
        # marker says "check upstream for current terms" — license undeclared
    },
    # Vendored entries with no marker file — provenance only in the import
    # commit message. Force vendoring: vendored via the override (the
    # inventory's marker-based detection returns 'custom' for these).
    ("coo-labs/coo-harness", "agentmail"): {
        "vendoring":     "vendored",
        "upstream":      "https://github.com/agentmail-to/agentmail-skills",
        "snapshot_date": "2026-04-22",
        "local_edits":   "none (verbatim per import commit 0ca5b61)",
    },
}


def _yaml_scalar(v):
    """Emit v as a valid inline YAML scalar.

    Quote anything that could be misparsed (contains `:`, `#`, leading
    digit, special YAML keywords, etc). Plain identifiers and bare
    URLs without a `#` go unquoted.
    """
    s = str(v)
    needs_quote = (
        not s
        or s[0] in "!&*-?,[]{}|>%@`#" + " \t"
        or s[-1] in " \t"
        or "#" in s
        or ": " in s
        or s.lower() in ("true", "false", "null", "yes", "no", "on", "off", "~")
        or re.match(r"^[+-]?[0-9]", s)  # numeric-looking
    )
    if needs_quote:
        return json.dumps(s)  # valid JSON-style YAML string
    return s


def build_metadata_block(entry, override=None):
    """Return the YAML lines for an entry's metadata block (no trailing newline).

    Overrides win over inventory-derived values — useful when a skill was
    vendored without a marker file (the inventory sees `custom`; the
    override forces the truth).
    """
    override = override or {}
    vendoring = override.get("vendoring") or entry["vendoring"]
    lines = ["metadata:"]
    lines.append(f"  type: {_yaml_scalar(entry['type'])}")
    lines.append(f"  vendoring: {_yaml_scalar(vendoring)}")
    if vendoring in ("vendored", "vendored-customized"):
        src = entry.get("vendor_source") or {}
        for key in ("upstream", "commit", "snapshot_date", "local_edits"):
            v = override.get(key) or src.get(key)
            if v:
                lines.append(f"  {key}: {_yaml_scalar(v)}")
    if override.get("license"):
        lines.append(f"  license: {_yaml_scalar(override['license'])}")
    return "\n".join(lines)


def has_existing_metadata(fm_body):
    """True if the frontmatter body has a top-level `metadata:` key."""
    return bool(re.search(r"^metadata\s*:", fm_body, re.MULTILINE))


def patch_file(path, metadata_block):
    """Insert metadata_block before closing `---` of frontmatter.

    Returns one of: "patched", "no-frontmatter", "already-has-metadata".
    """
    text = Path(path).read_text(encoding="utf-8")
    m = FRONTMATTER_RE.match(text)
    if not m:
        return "no-frontmatter"
    fm_body = m.group(2)
    if has_existing_metadata(fm_body):
        return "already-has-metadata"
    # Insert the block just before the closing `---`. Ensure exactly one
    # newline between the last existing key and the block.
    sep = "\n" if not fm_body.endswith("\n") else ""
    new_fm = fm_body + sep + metadata_block
    new_text = m.group(1) + new_fm + m.group(3) + text[m.end():]
    Path(path).write_text(new_text, encoding="utf-8")
    return "patched"


def main(argv=None):
    ap = argparse.ArgumentParser(description="Backfill metadata blocks across one repo.")
    ap.add_argument("inventory", help="Path to inventory JSON")
    ap.add_argument("--repo", required=True, help="Repo slug (e.g. coo-labs/coo-memory)")
    ap.add_argument("--dry-run", action="store_true", help="Show the blocks but don't write")
    args = ap.parse_args(argv)

    data = json.loads(Path(args.inventory).read_text())
    repo_path = next(
        (r["path"] for r in data["scan"]["repos"] if r["remote"] == args.repo),
        None,
    )
    if not repo_path:
        sys.exit(f"repo {args.repo!r} not in inventory.scan.repos")

    entries = [e for e in data["entries"] if e["repo"] == args.repo]
    if not entries:
        print(f"no entries found for {args.repo}", file=sys.stderr)
        return 0

    patched, skipped_meta, skipped_no_fm = [], [], []
    for entry in entries:
        override = VENDOR_OVERRIDES.get((entry["repo"], entry["name"]), {})
        block = build_metadata_block(entry, override)
        full_path = Path(repo_path) / entry["entry_path"]

        if args.dry_run:
            print(f"--- {entry['entry_path']} ({entry['kind']} '{entry['name']}') ---")
            print(block)
            print()
            continue

        if not full_path.is_file():
            print(f"MISS: {full_path}", file=sys.stderr)
            continue

        status = patch_file(full_path, block)
        if status == "patched":
            patched.append(entry["entry_path"])
        elif status == "already-has-metadata":
            skipped_meta.append(entry["entry_path"])
        else:
            skipped_no_fm.append(entry["entry_path"])

    if args.dry_run:
        print(f"Would process {len(entries)} entries in {args.repo}", file=sys.stderr)
    else:
        print(f"Patched: {len(patched)} files", file=sys.stderr)
        if skipped_meta:
            print(f"Skipped (already has metadata): {len(skipped_meta)}", file=sys.stderr)
        if skipped_no_fm:
            print(f"Skipped (no frontmatter): {len(skipped_no_fm)}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
