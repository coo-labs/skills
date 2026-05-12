# `# Setup hints` manifest schema

Each reference skill or agent under `skills/reference/` or
`agents/reference/` carries a `# Setup hints` section at the
bottom of its `SKILL.md` (or its `.md` file for agents). The
`adapt-skill` meta-skill reads this section and runs a structured
interview to produce an installed version for the user's substrate.

This document is the authoritative schema. When this document and
a specific reference skill's hints disagree, this document wins —
update the skill, not the meaning.

## Format

The section starts with an H1 heading exactly `# Setup hints` and
contains a single fenced YAML code block. The H1 MUST be the
**last** H1 in the file — `adapt-skill` strips everything from this
H1 onward when producing the adapted output, so any content after
it (including cross-references or notes) will be dropped. Put
cross-references **before** the `# Setup hints` section.

```markdown
# Setup hints

```yaml
requires:
  - ...
philosophical_gate:
  ...
setup_hints:
  - ...
script_hints:
  - ...
degradations:
  - ...
```
```

All five top-level blocks are optional. A minimal hints section
might be just `setup_hints:` with one or two entries.

## `requires:` — install-order dependencies

Names files, helpers, or other skills that the target needs in
addition to substitution.

```yaml
requires:
  - kind: file | env | skill | agent
    name: <human-readable label>
    detect: <bash one-liner that returns 0 if present>
    severity: blocking | warning
    install_hint: <one-line guidance for the user on how to satisfy>
```

- `kind` — what sort of dependency. `file` for a path; `env` for
  an environment variable; `skill` for another reference or
  installed skill; `agent` for a sub-agent definition.
- `name` — what the user sees in the pre-flight report.
- `detect` — a bash one-liner that exits 0 if the dependency is
  present. `adapt-skill` runs this verbatim.
- `severity` — `blocking` stops adaptation; `warning` notes and
  continues.
- `install_hint` — one-line guidance the meta-skill surfaces when
  the dependency is missing.

Example (from `day-overview`):

```yaml
requires:
  - kind: file
    name: "post-discussion shared helper"
    detect: "test -f $HOME/.claude/_lib/post-discussion.sh"
    severity: warning
    install_hint: "Only needed if you'll use --post to publish to a discussion surface. Adapt the `post-discussion` skill first, or accept that --post will be unavailable."
```

## `philosophical_gate:` — value buy-in

For targets that embed a theory of value (not just substrate
paths). If the user doesn't accept the theory, mechanical
substitution produces incoherent output; the user should author
from the pattern README instead.

```yaml
philosophical_gate:
  question: <the buy-in question>
  yes_label: <what to display for the "yes, this fits" answer>
  no_label: <what to display for the "no, this doesn't fit" answer>
  no_action: <one-line guidance for the no path; typically "see <README> and author from the pattern">
```

Example (from `emancipatory-auditor`):

```yaml
philosophical_gate:
  question: "This auditor enforces a double-clause: every artifact must (a) grow the author's capability AND (b) be installable by a peer agent without inherited context. Does this match how your project judges artifacts?"
  yes_label: "Yes, both clauses fit"
  no_label: "No, my project judges artifacts differently"
  no_action: "Read agents/reference/README.md — author a quality-gate agent that scores against your own acceptance criteria instead of adapting this one."
```

Use sparingly. Most reference skills are substrate-coupled, not
value-coupled — `setup_hints` alone is sufficient.

## `setup_hints:` — the interview rubric

The core of the manifest. Each entry is one substitution.

```yaml
setup_hints:
  - key: <short identifier>
    kind: PROMPT | DETECT | OPTIONAL
    question: <what to ask the user>   # PROMPT and OPTIONAL
    detection: <bash one-liner>        # DETECT — output is the substitution value
    find: <literal string in body to replace>
    find_unique: true                  # optional; abort if find appears 0 or 2+ times
    fallback: <substitution value if user skips / detection fails / answer is empty>
    min_count: N                       # optional; for list-valued PROMPTs
    cold_start: skip                   # optional; bypass interview on first install
    severity: blocking | warning       # optional; default warning; only meaningful with min_count
```

### Field semantics

- `key` — short identifier; used in the setup report only.
- `kind`:
  - `PROMPT` — always ask the user. No skip.
  - `DETECT` — run `detection`; use stdout as the substitution
    value. If exit non-zero, use `fallback`.
  - `OPTIONAL` — ask the user; offer "skip" as a first-class
    answer routing to `fallback`.
- `question` (PROMPT / OPTIONAL) — what `AskUserQuestion`
  surfaces. Be specific about format (path / list / name).
- `detection` (DETECT) — a bash one-liner. `adapt-skill` runs it
  and uses stdout, trimmed, as the substitution.
- `find` — literal substring in the source body to replace.
  Find-and-replace is global by default — every occurrence
  is substituted.
- `find_unique: true` — assert the `find` string appears exactly
  once. If 0 or 2+, abort with a diagnostic. Use when the literal
  would collide with unrelated occurrences (e.g. the path
  `coo/retrospectives/` may appear both as an output dir and in a
  cross-reference).
- `fallback` — what to substitute if the user skips, detection
  fails, or the answer is empty. Required for `OPTIONAL` and
  `DETECT`; recommended for `PROMPT`.
- `min_count: N` — for hints that take a list (governance rules,
  repo names, etc.). If fewer than N entries, route to `fallback`.
- `cold_start: skip` — when `detection` returns non-zero AND a
  declared prior-art file is absent, skip the interview and apply
  `fallback`. Used for hints referencing calibration prior-art
  that won't exist on first install.
- `severity: blocking` — only meaningful with `min_count`; aborts
  the entire adaptation if the threshold isn't met. Default is
  `warning` (apply fallback, continue).

### Worked example (from `day-overview`)

```yaml
setup_hints:
  - key: retrospectives_dir
    kind: PROMPT
    question: "Where should day-overview files land? (e.g. docs/retrospectives/, logs/daily/)"
    find: "coo/retrospectives/"
    fallback: "docs/retrospectives/"

  - key: memo_index_path
    kind: OPTIONAL
    question: "Path to your memo/record index file (JSON array), or 'skip' if you have no such index."
    find: "coo/memo_index.json"
    fallback: ""  # empty string means "skill will skip the memos step at runtime"

  - key: repo_list
    kind: PROMPT
    question: "List the GitHub repos this skill should scan, comma-separated (owner/repo format)."
    find: 'REPOS=("vade-coo-memory" "vade-runtime" "vade-core" "vade-governance" "vade-agent-logs")'
    fallback: 'REPOS=()'

  - key: integrity_check_path
    kind: DETECT
    detection: 'echo "${VADE_CLOUD_STATE_DIR:-}/integrity-check.json"'
    find: '${VADE_CLOUD_STATE_DIR:-$CLAUDE_PROJECT_DIR/.vade-cloud-state}/integrity-check.json'
    fallback: ""
```

## `script_hints:` — bundled assets

For reference skills that ship with scripts, templates, or sub-
agent definitions alongside their `SKILL.md`.

```yaml
script_hints:
  - path: <relative to skill directory>
    treatment: PARAMETERIZE | REGENERATE-PER-USER | DROP
    rationale: <one-line why>
```

- `PARAMETERIZE` — `adapt-skill` copies the file to the install
  directory and applies the same substitution map to it.
- `REGENERATE-PER-USER` — `adapt-skill` does NOT copy. It emits a
  skeleton at the install path with TODO comments naming what
  needs to be authored per-substrate. The `rationale` becomes the
  skeleton header comment.
- `DROP` — neither copy nor regenerate. References to the asset
  in the body should be removed via a `setup_hints` entry with
  `fallback: ""` (or similar).

Example (from `commission-retrospective`):

```yaml
script_hints:
  - path: scripts/commission-retrospective.sh
    treatment: REGENERATE-PER-USER
    rationale: "Hardcodes vade-app/vade-coo-memory, coo/memo_index.json paths; rewrite per your repo layout."

  - path: templates/historian-prompt.md
    treatment: PARAMETERIZE
    rationale: "Eight required output sections port verbatim; only paths and project name substitute."
```

## `degradations:` — declared fallback patterns

When the target ships with a capability that requires another
optional substrate piece (e.g. adversarial auditor agents), this
block declares what to do if it's absent.

```yaml
degradations:
  - when: <hint key with fallback applied OR requires entry missing>
    body_replace:
      find: <body text describing the capability>
      with: <body text describing the degraded alternative>
    note: <one-line note appended to the adapted skill body>
```

Example (from `tool-creator`):

```yaml
degradations:
  - when: safety_governance_rules has min_count fallback
    body_replace:
      find: "Phase 2 dispatches two adversarial auditors in parallel"
      with: "Phase 2 runs a single self-review checklist (no auditor pair configured)"
    note: "Adapted with no governance rules — Phase 2 collapses to self-review. Re-run /adapt-skill tool-creator after authoring rules."
```

## What `adapt-skill` strips

The entire `# Setup hints` H1 section is stripped from the adapted
output. This includes everything from the `# Setup hints` heading
to the end of the file. Therefore:

- Cross-references (`## Cross-references`) MUST appear **before**
  the `# Setup hints` section.
- The `# Setup hints` section is meta about the source, not
  documentation for the installed skill's user.

## What stays in the adapted skill

Everything from the start of the file up to (but not including)
the `# Setup hints` H1. This is the worked-example body of the
reference skill, with substitutions applied.

The frontmatter (YAML between `---` lines at the top) is preserved
verbatim and is subject to substitution. If a hint's `find`
appears in frontmatter, it is substituted there too.

## Authoring hints for a new reference skill

When you write a new reference skill that's substrate-coupled,
add its `# Setup hints` section at the bottom. Checklist:

1. List every concrete path / repo / file / env var / memo ID in
   the body. Each is a candidate substitution.
2. For each, decide kind: PROMPT (user must supply), DETECT
   (probe), OPTIONAL (skip is fine).
3. Write `find` strings that are unambiguous. Prefer paths with
   leading directory context (`coo/retrospectives/`) over bare
   filenames.
4. **Verify each `find` string actually appears in the body**
   — markdown wraps lines at ~70 chars, so a string you wrote as
   one line ("open PRs across the five vade-app repos") may
   actually live across two ("open PRs across the five\n   vade-app
   repos") in the rendered source. The validator at
   `scripts/dry-run-validator.py` enforces this.
5. If a string would collide, mark `find_unique: true` and pick a
   surrounding-context-rich excerpt.
6. Provide a `fallback` for every entry — what does the installed
   skill look like if the user skips this?
7. If the skill embeds a value/philosophy that's not universally
   shared, add `philosophical_gate`.
8. If the skill needs other helpers or skills to be installed
   first, add `requires`.
9. If the skill has bundled scripts/templates, add `script_hints`.
10. Validate with `scripts/dry-run-validator.py`:
    ```sh
    python3 scripts/dry-run-validator.py path/to/SKILL.md
    ```
    Exit 0 means every `find` string was located. The validator
    also catches: malformed YAML, missing `find` fields, ambiguous
    `find_unique` (≠1 occurrence), and `script_hints` paths that
    don't exist in the skill directory. Run before committing any
    new reference skill or hints update.

## Cross-references

- [`SKILL.md`](SKILL.md) — the adapt-skill itself; reads this
  schema.
- [`WORKED-EXAMPLE.md`](WORKED-EXAMPLE.md) — walked-through
  adaptation of `status-check`.
