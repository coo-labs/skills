# Reference skills

The skills under this directory encode session-shape patterns —
**register loaders** and **persona overlays** — that have been
useful inside the VADE substrate. They are NOT meant to be
installed verbatim into another project.

Same shape as `agents/reference/`: the *pattern* ports cleanly;
the *substrate references* don't.

## What's here

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

## Why "reference"

These skills cite VADE-internal artifacts as worked examples:
- `chat-mode` references a specific memo and retrospective as the
  binding-lens and originating session.
- `exec-mode` references VADE's project board structure, the
  `coo/CLAUDE.md` boot order, and the integrity-check probe.

Those references won't resolve in your project. The patterns —
loading a register; layering a persona doctrine with
discipline-rollup folded from per-run retrospectives;
distinguishing routine-mode from revise-persona-mode — DO port.

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
4. Per-run retrospectives in
   `coo/personas/exec-mode-retrospectives/` (or your equivalent)
   compound discipline over time; the persona file's
   "Discipline rollup" section is where you fold standing
   lessons with provenance citations.

## Why not install verbatim

The SKILL.md files reference doctrine files and worked-example
substrate by path. Installing them unchanged leaves the consumer's
agent looking for files that don't exist (`coo/personas/exec-mode.md`,
`coo/retrospectives/2026-05-03_what-works-and-why.md`,
`coo/CLAUDE.md`). The substrate-agnostic skills under
`skills/` proper (`quarto-docs`, `tldraw-docs`, `canvas-ui`,
`peer-review`) install cleanly; these don't.
