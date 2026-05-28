# Skill & agent inventory

Two scripts that walk a list of repos, discover every Claude Code skill
(`SKILL.md`) and agent (`.md` under `agents/`), and produce a structured
inventory + a human-readable report.

- `inventory.py` — walk the repos, emit JSON, validate against `schema.json`
- `render.py` — read the JSON, validate, render as Markdown, JSON, or CSV
- `schema.json` — JSON Schema (draft 2020-12) the JSON output validates against

The schema is the contract between the two scripts. Both validate against it
on every run, so a drift between producer and consumer fails loudly.

## Why

We have skills and agents living in `.claude/skills/` and `.claude/agents/`
across at least four repos (`coo-memory`, `coo-harness`, `skills`,
`vade-canvas`). Each repo has its own vendoring marker convention, its own
bundle layout, and no shared registry. Before this script there was no
single answer to: *which skills do we actually have, where do they live,
which are vendored, how big are they, and when were they added?*

## Usage

```
# Discover and write inventory.json
python3 tools/inventory.py \
    /path/to/coo-memory \
    /path/to/coo-harness \
    /path/to/vade-canvas \
    /path/to/skills \
    --transcripts /root/.claude/projects \
    --out tools/example/inventory.json

# Render markdown
python3 tools/render.py tools/example/inventory.json --out tools/example/inventory.md

# Render CSV (one row per entry; spreadsheet-friendly)
python3 tools/render.py tools/example/inventory.json --format csv --out tools/example/inventory.csv

# Re-validate an existing inventory file
python3 tools/inventory.py --validate-only --out tools/example/inventory.json
```

No repo paths are hard-coded — pass any set of paths. Each path is treated
as an independent repo root; `.claude/skills/*/SKILL.md`,
`.claude/agents/**/*.md`, `skills/*/SKILL.md`, and `agents/**/*.md` are all
discovered automatically.

## What it discovers per entry

| Field | Source |
|---|---|
| `kind` | `skill` or `agent` |
| `name` | Frontmatter `name:` (fallback: directory or filename) |
| `repo` | `git remote get-url origin` → `owner/repo` slug |
| `repo_dir`, `entry_path` | Paths relative to the repo root |
| `frontmatter` | `name`, `description`, `argument-hint`, `allowed-tools`, `tools`, `model`, `license`, `compatibility`, plus the full `metadata` block |
| `description_chars`, `body_chars`, `total_bytes`, `total_lines` | File-size metrics |
| `vendoring` | `custom` / `vendored` / `vendored-customized` / `unknown` — declared (frontmatter `metadata.vendoring`) if present, otherwise parsed from `UPSTREAM.md` / `VENDORED.md` markers at the repo root, `.claude/skills/`, `.claude/agents/`, and per-skill directories |
| `vendoring_source` | `declared` or `heuristic` — tells you which path produced the value |
| `vendor_source` | `upstream` URL, `commit` SHA, `snapshot_date`, `local_edits` text, and the path of the marker file (or `frontmatter.metadata` if declared) |
| `type` | `procedural`, `role`, `documentation`, `reference`, `api-service`, `meta`, `review`, `agent-auditor`, `agent-reviewer`, `agent-researcher`, `agent-orchestrator`, `agent-specialist`, `agent-general`, `unknown` — declared (frontmatter `metadata.type`) if present, otherwise classified by overrideable regex rules |
| `type_source` | `declared` or `heuristic` |
| `type_signals` | Human-readable reasons supporting the type label |
| `bundle` | Subdirs found inside a skill bundle: `scripts`, `references`, `assets`, `agents`, `evals`, `templates`, `eval-viewer`, plus `LICENSE`, vendor markers, and any unrecognized files/dirs |
| `git.first_commit_iso`, `last_commit_iso`, `commits_count` | `git log --follow` against the entry path |
| `usage.invocations`, `unique_sessions`, `last_iso` | If `--transcripts DIR` is passed: counted from `<command-name>NAME</command-name>` tokens and `Skill` tool-use blocks in any `*.jsonl` under that directory |

## Declared metadata (agentskills.io `metadata:` block)

The script reads declared metadata from the SKILL.md `metadata:` block per the
[agentskills.io open standard](https://agentskills.io/specification), which
Claude Code's docs explicitly defer to. The standard describes `metadata` as
"a map from string keys to string values" intended for "additional properties
not defined by the Agent Skills spec." Declared values **override** the
heuristic ones; the script records which path produced each value
(`type_source`, `vendoring_source`).

Recognized `metadata.*` keys:

| Key | Effect on inventory |
|---|---|
| `type` | Sets `entry.type` directly; `type_source = "declared"` |
| `vendoring` | Sets `entry.vendoring` directly; `vendoring_source = "declared"` |
| `upstream`, `commit`, `snapshot_date`, `local_edits` | When `vendoring` is declared, these populate `vendor_source` (replacing the parsed-marker route) |
| `version`, `author`, `deprecated`, `supersedes`, anything else | Passed through verbatim in `frontmatter.metadata` for the renderer to surface |

The two **top-level** standard fields are also captured:

| Field | Source |
|---|---|
| `license` | agentskills.io spec — name or bundled file reference |
| `compatibility` | agentskills.io spec — environment requirements (max 500 chars per spec) |

The inventory does not write to any SKILL.md — declaring metadata is a
deliberate per-skill act by whoever maintains it. The renderer marks
declared values with ★ in the per-repo tables and reports
`Declared metadata coverage: type X/N (P%), vendoring Y/N (P%)` in the
summary so the migration arc is visible.

### Example SKILL.md frontmatter with declared metadata

```yaml
---
name: cf-wrangler
description: Cloudflare Workers CLI ...
metadata:
  type: api-service
  vendoring: vendored
  upstream: https://github.com/cloudflare/skills
  commit: 7c449def4e0c63daa27212d853094e4c8e37bbe8
  snapshot_date: "2026-04-28"
  version: "1.0"
  author: cloudflare
license: Apache-2.0
---
```

With the above, the inventory needs neither the `UPSTREAM.md` marker file
nor the regex name-heuristic to land on `type=api-service, vendoring=vendored`
with full provenance. The script reports `type_source: declared`,
`vendoring_source: declared`, and the renderer marks both with ★.

## Vendoring detection

The script reads vendoring markers from these locations (in order):

- `<repo>/UPSTREAM.md`, `<repo>/VENDORED.md`
- `<repo>/.claude/UPSTREAM.md`, `<repo>/.claude/VENDORED.md`
- `<repo>/.claude/skills/UPSTREAM.md`, `<repo>/.claude/skills/VENDORED.md`
- `<repo>/.claude/agents/UPSTREAM.md`, `<repo>/.claude/agents/VENDORED.md`
- `<repo>/skills/UPSTREAM.md`, `<repo>/skills/VENDORED.md`
- `<repo>/agents/UPSTREAM.md`, `<repo>/agents/VENDORED.md`
- `<repo>/.claude/skills/<skill>/{UPSTREAM,VENDORED}.md`
- `<repo>/skills/<skill>/{UPSTREAM,VENDORED}.md`

It parses each as Markdown, splits on `##` section headings, and treats
each section name as a skill or agent identifier (comma-separated lists
and path-style names like `agents/foo.md` are handled). It extracts
`Source repo` / `Upstream`, `Source commit`, `Snapshot date`, and
`Local edits`. If the `Local edits` text reads as a `name:`-only rename
(matched loosely), the entry is `vendored`; otherwise `vendored-customized`.

Sections such as `## Relocation history`, `## Bump procedure`,
`## Skills not vendored (yet)`, `## Conceptual provenance` are skipped.

## Type classification

Heuristic rules live in the `DEFAULT_TYPE_RULES` dict at the top of
`inventory.py`. Override or extend them by passing `--type-rules FILE.json`
with a JSON object using the same `skill_rules` / `agent_rules` shape.
Rules are tried in order; the first match wins. Each rule supports any
combination of:

- `if_name_regex`: regex matched against the entry name
- `if_name_in`: explicit allowlist
- `if_has_subdir`: requires that subdir in the skill bundle (`scripts`, etc.)
- `if_desc_regex`: regex matched against frontmatter description
- `type`: label to apply
- `signal`: human-readable reason recorded in `type_signals`

This keeps the classifier transparent and tweakable without code changes.

## Usage metrics

Pass `--transcripts DIR` to scan every `*.jsonl` under that directory for
skill invocations. The scanner looks for two markers:

1. `<command-name>NAME</command-name>` tokens in text content (the harness
   inserts these for slash-command and skill invocations).
2. `tool_use` blocks with `name == "Skill"` and `input.skill == NAME`.

Counts are per-skill across the whole transcript corpus the script is
pointed at. The default container only holds the current session's
transcripts, so most counts will be near zero unless you point at an
archive. The report explicitly notes the scan directory and file count so
the consumer can interpret.

## Validation

The schema is JSON Schema 2020-12. Both scripts validate against it with a
minimal in-tree validator (no `jsonschema` PyPI dependency) covering the
subset we use: `type`, `enum`, `required`, `properties`,
`additionalProperties`, `items`, `minimum`, and local `$ref` to `$defs/*`.

To replace the validator with the standard library, install `jsonschema`
and substitute `Draft202012Validator(schema).validate(data)` — the schema
itself is unchanged.

## Output samples

See `example/inventory.json`, `example/inventory.md`, and
`example/inventory.csv` in this directory for current outputs across the
four-repo set.
