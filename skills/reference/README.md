# Reference skills

The skills under this directory encode session-shape patterns —
**register loaders**, **persona overlays**, and **substrate
discipline** — that have been useful inside the VADE substrate.
They are NOT meant to be installed verbatim into another project.

**Canonical install path:** run `/adapt-skill <name>` (from
[`../adapt-skill/`](../adapt-skill/)) per reference target you
want to install. The meta-skill reads each target's
`# Setup hints` manifest at the bottom of its `SKILL.md`,
conducts a structured interview about your substrate, and writes
the adapted version to `.claude/skills/<name>/SKILL.md`. The
fork-and-adapt path documented below remains an option for users
who want to inspect and rewrite by hand.

Same shape as `agents/reference/`: the *pattern* ports cleanly;
the *substrate references* don't.

## What's here

### Register and persona

- `chat-mode/` — a session-register loader. Names the dialogue
  register where substantive conversation can produce binding
  output (memo, retrospective, PR) rather than only task
  execution. Distinct from execution-shaped sessions.
- `exec-mode/` — an executive-persona overlay. Loads a discipline
  doctrine (Phase 0 survey → optional Plan-mode → Phase 2
  sub-agent dispatch → Phase 3 act → Phase 4 reflection) for
  broad-scope sessions: sweep/cleanup across open PRs and issues,
  strategic reflection on substrate state and priorities, or
  combinations. Includes the persona doctrine file
  (`persona.md`) and the persona-pattern README
  (`personas-README.md`).

### Substrate discipline

- `day-overview/` — briefing-shape synthesis of a day's shipped
  work. Gathers memos, merged PRs, and an integrity snapshot
  from a substrate, groups into lanes, lists carried-forward
  follow-ups, and ranks next actions. Ships with the
  `scripts/day-overview.sh` manifest-gatherer as the worked
  reference implementation.
- `briefing/` — manage NNN-numbered session-handoff briefings as a
  lifecycle: `request` (file a new briefing — collision-safe NNN
  allocation, YAML frontmatter, fresh branch + PR), `pickup`
  (claim an open briefing for the current session), `done` (mark
  delivered), `release` (clear a claim without delivering). The
  load-bearing structural requirement is a mandatory "Known
  bounds of this briefing" section where the author names their
  own blind spots so the recipient re-examines the framing rather
  than rubber-stamps it. Ships with `reference.md` (schema,
  index format, per-subcommand procedures), `template.md`, and
  `scripts/update-frontmatter.py`. **Setup hints are not yet
  rewritten for the lifecycle shape — the canonical bundle is
  mirrored verbatim from the originating substrate as a worked
  example; install via fork-and-adapt until a `# Setup hints`
  block lands (tracked in #28).**
- `commission-retrospective/` — commission an impartial
  project-historian retrospective on a window of project work.
  Two evidence sub-agents in parallel (memos-and-essays analyst,
  PR/issue-graph analyst), then a third-person draft that
  refuses recycled defended positions. Ships with a shell
  pre-flight and three sub-agent templates.
- `end-session/` — a session close-down checklist. Begins with
  an **externalization reflection** step — *did anything this
  session produce a recurring pattern, repeated friction, or
  transferable insight that future sessions would benefit from
  having pre-packaged?* — followed by one structured episodic
  memory entry, a session log, transcript-export sidecar
  pickup, and a marker file that silences a Stop hook.
- `status-check/` — six-item read-only grounding audit
  (who/what/where/next/decision/resource) capped at eight
  lines, with `⚠ not grounded` as the explicit "I can't answer
  that from loaded context" marker. The most substrate-agnostic
  of the reference skills — the procedure is just the six
  prompts.
- `tool-creator/` — staged-checkpoint skill authoring. Phase 1
  draft: inventory check across existing skills, frontmatter
  decision-tree, deliberate stop for operator review. Phase 2
  finalize: two adversarial auditors in parallel
  (`safety-auditor`, `emancipatory-auditor`), tools-registry
  row, PR. Four canonical refactor patterns documented
  (rename / extract+delegate / refactor in place / abort).
  Ships with four templates.

## Why "reference"

These skills cite VADE-internal artifacts as worked examples:
- `chat-mode` references a specific memo and retrospective as the
  binding-lens and originating session.
- `exec-mode` references VADE's project board structure, the
  `coo/CLAUDE.md` boot order, and the integrity-check probe.
- `day-overview` and `commission-retrospective` walk the five
  `coo-labs/*` repos, read `coo/memo_index.json`, and snapshot
  the VADE integrity-check JSON shape.
- `briefing` writes into `briefings/` and follows a
  `coo-memory`-specific branch / PR convention; the
  lifecycle subcommands (`pickup` / `done` / `release`) maintain
  a JSON index whose schema lives in the substrate's
  `briefings/_index.json`.
- `end-session` writes a session log under
  `coo-logs/sessions/` and an episodic Mem0 entry per
  VADE's SOP-MEM-001 metadata schema.
- `tool-creator` registers new skills in VADE's `TOOLS.md`,
  invokes named governance memos as auditor inputs, and routes
  through the `safety-auditor` / `emancipatory-auditor` sub-agent
  definitions.

Those references won't resolve in your project. The patterns —
loading a register; layering a persona doctrine with
discipline-rollup folded from per-run retrospectives;
distinguishing routine-mode from revise-persona-mode; briefing-
shape day synthesis; impartial-historian commission of a record
window; handoff briefings with an honesty gate; six-item grounding
audits; staged-checkpoint skill authoring — DO port.

## How to adapt

1. Copy the relevant directory into your `.claude/skills/`.
2. For `exec-mode`: write your own persona doctrine. The
   structure (Phase 0 / Plan-mode / Phase 2 dispatch / Phase 3
   act / Phase 4 reflection) is the bone; the discipline
   particulars are yours to fill. Update `SKILL.md`'s
   `personas/<name>.md` reference to point at where you keep
   the doctrine.
3. For `chat-mode`: write your own register-framing for the
   dialogue mode. Drop the VADE worked-example references; add
   your own as your first session in the register produces them.
4. For `day-overview` and `commission-retrospective`: edit the
   bundled scripts (`scripts/day-overview.sh`,
   `scripts/commission-retrospective.sh`) so they walk your own
   repo set and read your own memo/record index. Drop the
   VADE-specific integrity-check probe or replace with your
   project's equivalent. Adjust the discussion-post step
   (category IDs, label IDs) for your platform — or drop it.
5. For `briefing`: decide where briefings live in your substrate
   (default in VADE: `briefings/`), author your own `README.md`
   + `TEMPLATE.md` there, and update the skill's path references
   and the `reference.md` schema doc. Decide whether your project
   needs the full lifecycle (`request` / `pickup` / `done` /
   `release` with a JSON index) or just the `request` half;
   strip the lifecycle bits from `SKILL.md` and `reference.md`
   if not. Keep the **Known bounds** gate as the load-bearing
   structural requirement — that's the
   honesty-gate pattern.
6. For `end-session`: replace the VADE-specific surfaces (Mem0
   episodic metadata schema, `coo-logs/sessions/` log
   path, the Journal Discussions URL, the `$HOME/.vade/` marker
   path) with your own. Keep the externalization-reflection
   step — that's how a session feeds the substrate rather than
   just consuming it.
7. For `status-check`: largely lifts directly. Trim the
   worked-example memo references; the six prompts and the
   `⚠ not grounded` marker are the load-bearing parts.
8. For `tool-creator`: replace the VADE-specific governance
   memos (PAT discipline, Mem0 content rule, path scope, spend
   cap, attribution, subject+emancipatory clause) with your
   own auditor gates, and update the `TOOLS.md` row schema to
   your own tools registry. Keep the staged-checkpoint shape and
   the four refactor patterns (rename / extract+delegate /
   refactor in place / abort) — those are the load-bearing
   parts.
9. Per-run retrospectives in
   `coo/personas/exec-mode-retrospectives/` (or your equivalent)
   compound discipline over time; the persona file's
   "Discipline rollup" section is where you fold standing
   lessons with provenance citations.

## Why not install verbatim

The SKILL.md files reference doctrine files and worked-example
substrate by path. Installing them unchanged leaves the consumer's
agent looking for files that don't exist (`coo/personas/exec-mode.md`,
`coo/retrospectives/2026-05-03_what-works-and-why.md`,
`coo/CLAUDE.md`, `coo/briefings/README.md`, `coo/memo_index.json`,
`coo/status_check_template.md`, `coo/culture_system_sop.md`,
`TOOLS.md`, `coo-logs/sessions/`). The substrate-agnostic
skills under `skills/` proper (`quarto-docs`, `tldraw-docs`,
`canvas-ui`, `peer-review`) install cleanly; these don't.
