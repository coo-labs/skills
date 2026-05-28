#!/usr/bin/env python3
"""
render.py - read an inventory JSON produced by tools/inventory.py, validate
it against tools/schema.json, and render a human-readable markdown document.

Usage:
  render.py INVENTORY.json [--schema schema.json] [--out PATH]
            [--format md|json|csv] [--no-validate]
"""

import argparse
import csv
import io
import json
import sys
from pathlib import Path

# Reuse the validator + schema loader from the inventory module
sys.path.insert(0, str(Path(__file__).resolve().parent))
from inventory import validate, load_schema, SchemaError  # noqa: E402


# ---------------------------------------------------------------------------
# Markdown renderer
# ---------------------------------------------------------------------------

def _bundle_summary(bundle):
    parts = []
    for k in ("scripts", "references", "assets", "agents", "evals", "templates"):
        if k in bundle and bundle[k].get("count", 0):
            parts.append(f"{k}={bundle[k]['count']}")
    if "license" in bundle:
        parts.append("LICENSE")
    if "vendor_file" in bundle:
        parts.append(f"vendor={bundle['vendor_file']}")
    if "other" in bundle:
        parts.append(f"+{len(bundle['other'])} files")
    if "other_dirs" in bundle:
        parts.append(f"+{len(bundle['other_dirs'])} dirs")
    return ", ".join(parts) or "—"


def _short_iso(s):
    return (s or "")[:10] or "—"


def _vendor_cell(e):
    v = e["vendoring"]
    if v == "custom":
        return "—"
    src = e.get("vendor_source") or {}
    upstream = src.get("upstream")
    if upstream:
        # collapse https://github.com/owner/repo → owner/repo
        slug = upstream.rstrip("/").rsplit("/", 2)
        short = "/".join(slug[-2:]) if len(slug) >= 2 else upstream
        return f"{v}<br>{short}"
    return v


def render_md(data):
    out = []
    s = data["summary"]
    scan = data["scan"]

    out += [
        "# Claude Code skill & agent inventory",
        "",
        f"_Generated `{data['generated_at']}` · schema `v{data['schema_version']}`._",
        "",
    ]

    out += ["## Summary", ""]
    out += [f"- **Total entries**: {s['count_total']}"]
    out += ["- **By kind**: " + ", ".join(f"{k}={v}" for k, v in sorted(s["by_kind"].items()))]
    out += ["- **By repo**: " + ", ".join(f"`{k}`={v}" for k, v in sorted(s["by_repo"].items()))]
    out += ["- **By type**: " + ", ".join(f"{k}={v}" for k, v in sorted(s["by_type"].items(), key=lambda x: (-x[1], x[0])))]
    out += ["- **By vendoring**: " + ", ".join(f"{k}={v}" for k, v in sorted(s["by_vendoring"].items()))]
    out += [""]

    tx = scan.get("transcripts")
    if tx:
        out += [f"Transcripts scanned: `{tx.get('dir')}` ({tx.get('files_scanned', 0)} files). "
                "Invocation counts are honest reports of what the scan saw — point the "
                "scanner at an archive for cross-session totals.",
                ""]
    out += ["Repos scanned:"]
    for r in scan["repos"]:
        sha = (r.get("head_sha") or "")[:8] or "?"
        out += [f"- `{r['remote']}` @ `{sha}` ({r['path']})"]
    out += [""]

    # ---- Per-repo tables ----
    by_repo = {}
    for e in data["entries"]:
        by_repo.setdefault(e["repo"], []).append(e)

    out += ["## Inventory by repo", ""]
    for repo in sorted(by_repo):
        out += [f"### `{repo}`", ""]
        for kind in ("skill", "agent"):
            kentries = sorted([e for e in by_repo[repo] if e["kind"] == kind],
                              key=lambda e: e["name"])
            if not kentries:
                continue
            out += [f"#### {kind.title()}s ({len(kentries)})", ""]
            out += ["| Name | Type | Vendor | Bytes | Lines | Bundle | Added | Last commit | Invocations |"]
            out += ["|------|------|--------|-------|-------|--------|-------|-------------|-------------|"]
            for e in kentries:
                inv = (e.get("usage") or {}).get("invocations")
                inv_s = "—" if inv is None else str(inv)
                bundle_s = _bundle_summary(e["bundle"])
                out += [
                    f"| `{e['name']}` | {e['type']} | {_vendor_cell(e)} | "
                    f"{e['total_bytes']} | {e['total_lines']} | {bundle_s} | "
                    f"{_short_iso(e['git'].get('first_commit_iso'))} | "
                    f"{_short_iso(e['git'].get('last_commit_iso'))} | {inv_s} |"
                ]
            out += [""]

    # ---- Type cross-cut ----
    out += ["## Cross-cut by type", ""]
    by_type = {}
    for e in data["entries"]:
        by_type.setdefault(e["type"], []).append(e)
    for t in sorted(by_type, key=lambda k: (-len(by_type[k]), k)):
        out += [f"### {t} ({len(by_type[t])})", ""]
        for e in sorted(by_type[t], key=lambda e: (e["repo"], e["name"])):
            ref = " _(reference)_" if e.get("is_reference") else ""
            out += [f"- `{e['name']}` ({e['kind']}, `{e['repo']}`){ref} — "
                    f"{e['vendoring']}, {e['total_bytes']}B"]
        out += [""]

    # ---- Vendoring cross-cut ----
    out += ["## Cross-cut by vendoring", ""]
    by_vendor = {}
    for e in data["entries"]:
        by_vendor.setdefault(e["vendoring"], []).append(e)
    for v in ("custom", "vendored", "vendored-customized", "unknown"):
        if v not in by_vendor:
            continue
        out += [f"### {v} ({len(by_vendor[v])})", ""]
        for e in sorted(by_vendor[v], key=lambda e: (e["repo"], e["kind"], e["name"])):
            src = e.get("vendor_source") or {}
            extra = ""
            if v != "custom":
                bits = []
                if src.get("upstream"): bits.append(src["upstream"])
                if src.get("commit"):   bits.append(f"@{src['commit'][:8]}")
                if src.get("snapshot_date"): bits.append(f"snap {src['snapshot_date']}")
                if src.get("vendor_file"):   bits.append(f"marker {src['vendor_file']}")
                extra = " — " + "; ".join(bits) if bits else ""
            out += [f"- `{e['name']}` ({e['kind']}, `{e['repo']}`){extra}"]
        out += [""]

    # ---- Descriptions detail ----
    out += ["## Descriptions", ""]
    for e in sorted(data["entries"], key=lambda x: (x["repo"], x["kind"], x["name"])):
        out += [f"### `{e['name']}` — {e['kind']} in `{e['repo']}`"]
        out += [""]
        out += [f"- **Type**: {e['type']} _( {' · '.join(e.get('type_signals', []) or ['—'])} )_"]
        out += [f"- **Vendoring**: {e['vendoring']}"]
        if e.get("vendor_source"):
            src = e["vendor_source"]
            line = []
            if src.get("upstream"): line.append(f"upstream `{src['upstream']}`")
            if src.get("commit"):   line.append(f"commit `{src['commit'][:8]}`")
            if src.get("snapshot_date"): line.append(f"snapshot {src['snapshot_date']}")
            if src.get("vendor_file"):   line.append(f"marker `{src['vendor_file']}`")
            if line:
                out += ["  - " + "; ".join(line)]
            if src.get("local_edits"):
                out += [f"  - local edits: _{src['local_edits'][:240]}_"]
        out += [f"- **Path**: `{e['entry_path']}`"]
        out += [f"- **Size**: {e['total_bytes']} bytes / {e['total_lines']} lines · "
                f"description {e['description_chars']} chars · body {e['body_chars']} chars"]
        fm = e["frontmatter"]
        meta_bits = []
        if fm.get("argument_hint"): meta_bits.append(f"argument-hint `{fm['argument_hint']}`")
        if fm.get("allowed_tools"): meta_bits.append(f"allowed-tools `{fm['allowed_tools']}`")
        if fm.get("tools"):         meta_bits.append(f"tools `{fm['tools']}`")
        if fm.get("model"):         meta_bits.append(f"model `{fm['model']}`")
        if meta_bits:
            out += ["- **Frontmatter**: " + "; ".join(meta_bits)]
        if e["bundle"]:
            out += [f"- **Bundle**: {_bundle_summary(e['bundle'])}"]
        g = e["git"]
        out += [f"- **Git**: first {_short_iso(g.get('first_commit_iso'))}, "
                f"last {_short_iso(g.get('last_commit_iso'))}, {g.get('commits_count', 0)} commits"]
        u = e.get("usage")
        if u:
            out += [f"- **Usage**: {u['invocations']} invocations across "
                    f"{u['unique_sessions']} sessions"
                    + (f", last {u['last_iso'][:19]}" if u.get('last_iso') else "")]
        desc = (e["frontmatter"].get("description") or "").replace("\n", " ").strip()
        if desc:
            out += [""]
            # quote-fold long descriptions
            out += ["> " + desc]
        out += [""]

    return "\n".join(out).rstrip() + "\n"


# ---------------------------------------------------------------------------
# CSV renderer (one row per entry; flat columns)
# ---------------------------------------------------------------------------

CSV_COLUMNS = [
    "repo", "kind", "name", "type", "vendoring",
    "total_bytes", "total_lines", "description_chars",
    "first_commit_iso", "last_commit_iso", "commits_count",
    "invocations", "unique_sessions", "last_invocation_iso",
    "entry_path", "upstream", "commit", "is_reference",
]


def render_csv(data):
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(CSV_COLUMNS)
    for e in sorted(data["entries"], key=lambda x: (x["repo"], x["kind"], x["name"])):
        src = e.get("vendor_source") or {}
        u = e.get("usage") or {}
        g = e["git"]
        w.writerow([
            e["repo"], e["kind"], e["name"], e["type"], e["vendoring"],
            e["total_bytes"], e["total_lines"], e["description_chars"],
            g.get("first_commit_iso") or "", g.get("last_commit_iso") or "",
            g.get("commits_count", 0),
            u.get("invocations", ""), u.get("unique_sessions", ""),
            u.get("last_iso") or "",
            e["entry_path"], src.get("upstream") or "", src.get("commit") or "",
            "true" if e.get("is_reference") else "false",
        ])
    return buf.getvalue()


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------

def main(argv=None):
    ap = argparse.ArgumentParser(description="Render a skill inventory JSON file.")
    ap.add_argument("inventory", help="Path to inventory JSON")
    ap.add_argument("--schema", default=None, help="Path to schema.json")
    ap.add_argument("--out", default="-", help='Output path; "-" = stdout')
    ap.add_argument("--format", default="md", choices=["md", "json", "csv"])
    ap.add_argument("--no-validate", action="store_true",
                    help="Skip schema validation (not recommended)")
    args = ap.parse_args(argv)

    data = json.loads(Path(args.inventory).read_text())

    if not args.no_validate:
        schema = load_schema(args.schema)
        try:
            validate(data, schema)
        except SchemaError as e:
            print(f"Schema validation failed: {e}", file=sys.stderr)
            return 2

    if args.format == "md":
        out = render_md(data)
    elif args.format == "csv":
        out = render_csv(data)
    else:
        out = json.dumps(data, indent=2) + "\n"

    if args.out == "-":
        sys.stdout.write(out)
    else:
        Path(args.out).write_text(out)
        print(f"Wrote {args.out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
