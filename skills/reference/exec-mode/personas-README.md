# coo/personas/

*Loaded-on-demand COO personas. A persona is a bias-overlay invoked
by an explicit slash command — distinct from the standard COO
discipline (CLAUDE.md, the always-on substrate) and from sub-agent
templates (`.claude/agents/`, dispatched via the `Agent` tool). The
standard COO does the boot reading and the day-to-day work; a
persona narrows the discipline for a specific kind of work.*

---

## Pattern

Each persona lives in a single file (`<name>.md`) under this
directory. Per-run retrospectives live alongside in
`<name>-retrospectives/`, one file per run, dated.

Loaded by an explicit-invocation skill at
`vade-coo-memory/.claude/skills/<name>/SKILL.md`
(`disable-model-invocation: true`). Per Anthropic skill-primitive
guidance + vade-coo-memory#321, the skill is the canonical surface
for new tool authoring; the persona migrated from a `.claude/commands/`
slash command to a skill in v3 (2026-04-30).

The skill reads the persona file at boot. Routine invocations rely
on the persona file's **discipline rollup** (folded prior runs'
standing lessons with per-rule `(vN-from-<retro-slug>)` provenance
citations) — the retrospectives themselves are NOT loaded at
routine boot. A `--revise-persona` submode re-introduces read-all-
retros + plan-mode REQUIRED + adversarial-auditor gates for
revision sessions; recency-bias is a named failure mode of
recursive self-modification, and the principled stop is the
revision gate, not boot-time re-read.

A persona overlay does not change governance. CB-006 quorum gates
revisions to a persona's *constraints* (delegation rules,
cohort-respect defaults, governance restraints). Surface refinements
(Phase-0 survey, sub-agent prompt template tweaks, output schemas,
discipline-rollup additions) land on normal PR review.

## Current personas

| Name | File | Slash command | Inaugural retrospective |
|---|---|---|---|
| Exec-mode | [`exec-mode.md`](exec-mode.md) | `/exec-mode` | [`exec-mode-retrospectives/2026-04-30_spring-cleaning.md`](exec-mode-retrospectives/2026-04-30_spring-cleaning.md) |

## Adding a persona

1. Author `coo/personas/<name>.md` following the structure of an
   existing persona — clear `What this is` / `When this applies` /
   phase shape / **discipline rollup** (folded from any pre-existing
   retrospectives, with `(vN-from-<retro-slug>)` provenance) /
   constraints / `--revise-persona` submode / recursive-self-
   modification discipline.
2. Author `vade-coo-memory/.claude/skills/<name>/SKILL.md`
   explicit-invocation skill (`disable-model-invocation: true`) per
   `/tool-creator`'s `templates/explicit-invocation-skill.md`. The
   skill body holds the boot procedure (Step 0 standard COO boot,
   Step 1 load persona file, Step 2 mode selection from `$ARGUMENTS`,
   Step 3 synthesize, Step 4 ask for scope) and reads the persona
   file at runtime; the persona file is the source of truth for
   doctrine.
3. Add a row to `TOOLS.md` §11 (Personas) and a row to §3 for
   the skill primitive. Update the cross-cutting summary count.
4. Adversarial-auditor review on the introducing PR
   (`safety-auditor` + `emancipatory-auditor`); audit-then-PR
   pattern (run on the working tree before PR opens; fold PASS-
   WITH-NOTES inline).
5. BDFL ratifies the initial creation. Future *constraint* changes
   go through CB-006 quorum; future surface refinements land on
   normal PR review with auditor reports.

## Why personas, not just CLAUDE.md sections

CLAUDE.md is the always-on substrate; bloating it with mode-specific
disciplines makes boot reading more expensive and dilutes the
always-on rules. A persona is loaded-on-demand: the cost is paid by
the session that needs it, not by every session.

A persona is also distinct from a sub-agent. Sub-agents under
`.claude/agents/` are dispatched via the `Agent` tool with custom
prompts; they have their own context window and tool subset. A
persona shapes the *main* COO's behavior for a session — the COO
itself loads the persona and follows it; the persona may then
dispatch sub-agents per its own discipline.
