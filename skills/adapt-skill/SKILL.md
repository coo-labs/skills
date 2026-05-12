---
name: adapt-skill
description: Adapt a reference skill or agent from this repo into a working installed primitive for the current substrate. Reads the target's `# Setup hints` manifest, conducts a structured interview, substitutes substrate-coupled surfaces with the user's answers, and writes the adapted skill to `.claude/skills/<name>/` (or agent to `.claude/agents/<name>.md`). Run once per reference skill the user wants to install. Don't invoke for substrate-agnostic skills under `skills/` proper — those install verbatim via `setup/cloud-setup.sh`.
argument-hint: <skill-or-agent-name> [--user] [--dry-run]
disable-model-invocation: true
allowed-tools: Bash, Read, Write, Edit, AskUserQuestion
---

# adapt-skill — port a reference skill to your substrate

The reference skills and agents under `skills/reference/` and
`agents/reference/` carry substrate-coupled paths, helpers, and
governance memos from the originating project (VADE). Installing
them verbatim leaves a user's agent looking for files that don't
exist. This meta-skill is the adaptation primitive: it reads the
target's structured `# Setup hints` manifest, runs the interview,
and produces a working installed skill in the user's substrate.

> **Pattern.** Each reference skill carries a `# Setup hints`
> section at the bottom of its `SKILL.md` declaring its
> substrate-coupled surfaces — file paths, named concepts, repo
> sets, helper scripts, governance rules. The hints follow the
> schema in [`SCHEMA.md`](SCHEMA.md). This skill reads them,
> conducts a structured interview, and substitutes. The reference
> skill body stays as the worked example; the adapted skill is the
> rewritten version that lands in the user's `.claude/skills/`.

## When to use

Invoke when:

- A user wants to install one of the reference skills (`chat-mode`,
  `exec-mode`, `day-overview`, `request-briefing`,
  `commission-retrospective`, `end-session`, `status-check`,
  `tool-creator`) or reference agents (`safety-auditor`,
  `emancipatory-auditor`) into their own project.
- The user types `/adapt-skill <name>` directly.
- `/adapt-skill --list` to see what's available with portability
  tiers.

Don't invoke for:

- Substrate-agnostic skills under `skills/` proper (`quarto-docs`,
  `tldraw-docs`, `canvas-ui`, `peer-review`) — these install
  verbatim via `setup/cloud-setup.sh`.
- Re-adaptation of an already-installed skill. The interview
  baked answers into the skill body; to change them, edit the
  installed file directly or re-run `--dry-run` to see what would
  change.
- Authoring a brand-new skill — use `tool-creator` once you've
  adapted it.

## Procedure

### Step 0 — Resolve target and pre-flight

Parse `$ARGUMENTS`. If `--list`, print the table of available
reference targets with their portability tiers and exit:

```text
chat-mode                   config-only       (skills/reference/)
exec-mode                   agent-rewrite     (skills/reference/)
status-check                drop-in           (skills/reference/)
day-overview                agent-rewrite     (skills/reference/)
request-briefing            config-only       (skills/reference/)
commission-retrospective    agent-rewrite     (skills/reference/)
end-session                 agent-rewrite     (skills/reference/)
tool-creator                drop-and-redesign (skills/reference/)
safety-auditor              agent-rewrite     (agents/reference/)
emancipatory-auditor        agent-rewrite     (agents/reference/)
```

Otherwise, the first positional argument is the target name.
Locate the source file:

```bash
NAME="$1"
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")/../../.." && pwd)"
if [ -f "$REPO_ROOT/skills/reference/$NAME/SKILL.md" ]; then
  KIND="skill"
  SRC="$REPO_ROOT/skills/reference/$NAME/SKILL.md"
  SRC_DIR="$REPO_ROOT/skills/reference/$NAME"
elif [ -f "$REPO_ROOT/agents/reference/$NAME.md" ]; then
  KIND="agent"
  SRC="$REPO_ROOT/agents/reference/$NAME.md"
  SRC_DIR="$REPO_ROOT/agents/reference"
else
  echo "adapt-skill: $NAME not found under skills/reference/ or agents/reference/"
  exit 2
fi
```

Decide install target:

- `--user`: install to `$HOME/.claude/skills/$NAME/` (or
  `$HOME/.claude/agents/$NAME.md`).
- Default: install to `$PWD/.claude/skills/$NAME/` (or
  `$PWD/.claude/agents/$NAME.md`).

If the target already exists, ask the user before overwriting. The
existing file may carry their prior adaptations.

### Step 1 — Read the source and parse `# Setup hints`

Read the source file. Locate the `# Setup hints` H1 section
(must be the last H1 in the file). Parse the YAML inside the
fenced code block per [`SCHEMA.md`](SCHEMA.md).

If no `# Setup hints` section exists, the target is not adaptable
via this skill. Tell the user and stop.

The parsed manifest carries up to five blocks:

- `requires:` — `DEPENDS_ON` entries: helpers, other skills, or
  external files the target needs in addition to substitution.
  Check each: if absent, surface to the user as a pre-install gate
  before continuing.
- `philosophical_gate:` — single optional block: asks the user a
  buy-in question about the values the target encodes. If the
  user answers "no", abort with a recommendation to author from
  pattern (read `agents/reference/README.md` or
  `skills/reference/README.md`).
- `setup_hints:` — the interview rubric. Each hint has `key`,
  `kind`, `question` or `detection`, `find` or `find_unique`,
  `fallback`. See SCHEMA.md.
- `script_hints:` — per-bundled-asset treatment (`PARAMETERIZE`,
  `REGENERATE-PER-USER`, `DROP`).
- `degradations:` — declared fallback patterns when an optional
  capability is missing (e.g. "no auditor agents → manual
  review").

### Step 2 — Pre-flight: dependencies and philosophical gate

For each entry in `requires:`, check presence. Probe via the
`detect:` field (file existence, env var, etc.). If absent and
`severity: blocking`, stop and tell the user what to install
first. If `severity: warning`, note and continue.

If `philosophical_gate:` is set, surface the question to the user
via `AskUserQuestion`. The user's answer determines the path:

- "Yes, this lines up with how my project works" → continue to Step 3.
- "No, this doesn't fit my project's values" → abort and point
  to the pattern README. Do not produce a half-adapted file.

### Step 3 — Run the interview

Batch the `PROMPT` hints into `AskUserQuestion` groups of ≤3
questions per batch (the tool's limit) per
MEMO-2026-04-28-4umz-style "≥3 decisions queue → structured form"
discipline. Run `DETECT` hints automatically. Ask `OPTIONAL`
hints with an explicit "skip" option.

For each hint, record either the user's answer or the `fallback`
string. Build the substitution map.

Some hints declare `min_count` or `cold_start` directives:

- `min_count: N` — for hints that take a list (e.g. governance
  rules). If the user supplies fewer than N entries, route to the
  hint's `fallback` (which may be "abort and recommend authoring
  rules first").
- `cold_start: skip` — for hints referencing prior-art that doesn't
  exist on first install. Detect absence and apply the fallback
  without prompting.

### Step 4 — Substitute

For each substitution, find the `find` string in the source body
and replace with the user's answer. If `find_unique: true` is set,
assert the string appears exactly once before replacing; abort
with a diagnostic if it appears 0 or 2+ times (the skill author
gave imprecise `find` text).

The `# Setup hints` H1 section itself is **stripped** from the
output — it is meta about the source, not part of the installed
skill.

### Step 5 — Handle bundled scripts and templates

For each entry in `script_hints`:

- `PARAMETERIZE`: copy the file from `$SRC_DIR/<path>` to the
  target install path, then apply the same substitution map to it.
- `REGENERATE-PER-USER`: do NOT copy. Emit a skeleton at the
  target path with TODO comments naming what needs to be authored
  per-substrate. The script's `rationale:` field becomes the
  skeleton's header comment.
- `DROP`: do not copy or generate. Remove any references to the
  asset from the adapted SKILL.md body.

### Step 6 — Write the adapted skill

Write the substituted body to the target path:

- `skill` kind: `$INSTALL_DIR/.claude/skills/$NAME/SKILL.md`
  (plus any `PARAMETERIZE` assets in the same directory).
- `agent` kind: `$INSTALL_DIR/.claude/agents/$NAME.md`.

In `--dry-run` mode, do not write; instead, print a diff-style
summary of what would change.

### Step 7 — Emit the setup report

Tell the user:

1. What was installed and where.
2. Which hints were answered vs which used fallbacks.
3. Any `REGENERATE-PER-USER` assets that need follow-up
   authoring.
4. Any declared `degradations` that were applied (e.g. "Phase 2
   auditor pair collapsed to single self-review checklist; the
   adapted skill notes this in its body").
5. Next-action hints — e.g. "now run `/<name>` to test the
   adapted skill," or "you'll want to install
   `<dependency>` next."

## Critical constraints

- **Find-and-replace is literal.** The `find` field is a verbatim
  substring match. Skill authors should make these unambiguous;
  `find_unique: true` is the escape hatch when a string would
  otherwise collide.
- **Never partially adapt.** If pre-flight, philosophical gate, or
  any hint with `severity: blocking` fails, do not write the
  adapted file. Half-adapted skills produce hollow verdicts
  silently — worse than no skill.
- **Never overwrite without consent.** If the target install path
  exists, ask the user. The existing file may carry their prior
  edits.
- **The `# Setup hints` section is meta, not body.** Strip it
  from the adapted output; do not propagate it into the installed
  skill.
- **Don't invent substitutions.** If the source body references
  something the hints don't cover, leave it as-is and surface to
  the user in the setup report. The skill author is responsible
  for declaring complete hints; the meta-skill is not a
  general-purpose substrate rewriter.

## Failure modes

- **Source has no `# Setup hints` section.** The target isn't
  adaptable via this skill. Tell the user and stop.
- **Source has malformed YAML.** Surface the parse error verbatim
  and point at the line. Skill authors fix at source.
- **Philosophical gate rejected.** Abort cleanly; recommend the
  pattern README path. No partial file.
- **`min_count` not met.** Apply the fallback (which is usually
  "abort and recommend authoring rules first"). Don't emit a
  vacuous auditor.
- **`find` string not present in body.** Skill author error.
  Surface the missing string; do not silently skip.
- **Install target exists.** Ask before overwrite.

## Worked example: adapting status-check

See [`WORKED-EXAMPLE.md`](WORKED-EXAMPLE.md) for a walked-through
adaptation of `status-check` (the simplest reference skill) into
a foreign substrate. The example shows the interview transcript,
the substitution map, and the final installed SKILL.md.

## Canonical source

```text
skills/adapt-skill/SKILL.md (this file)
skills/adapt-skill/SCHEMA.md (the # Setup hints manifest schema)
skills/adapt-skill/WORKED-EXAMPLE.md (status-check adaptation walkthrough)
skills/adapt-skill/scripts/dry-run-validator.py (QA tool: parses a hints manifest, verifies every find: string is in the body, reports problems)
skills/reference/<name>/SKILL.md (each reference skill carries its own hints)
agents/reference/<name>.md (each reference agent carries its own hints)
```

## Validating a reference skill's hints manifest

Before adapting (or when authoring a new reference skill), run the
validator against the source SKILL.md:

```sh
python3 skills/adapt-skill/scripts/dry-run-validator.py \
  skills/reference/<name>/SKILL.md
```

Exit 0 means every declared `find:` string is present in the body
and every `script_hints` path resolves. Exit 1 means the manifest
has gaps the adapter can't paper over. Stderr lists each problem
with the offending hint key.

## Cross-references

- `skills/reference/README.md` — the fork-and-adapt path (manual
  alternative to this skill)
- `agents/reference/README.md` — same for reference agents
- `setup/cloud-setup.sh` — installs substrate-agnostic
  `skills/*` and `agents/*` verbatim; reference targets are
  deliberately excluded and routed through this meta-skill
