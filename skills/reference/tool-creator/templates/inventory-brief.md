# Inventory sub-agent brief

Used by `/tool-creator` Phase 1 Step 1.2. The orchestrator
inlines this brief plus the new skill's `$capability_description`
and `$invocation_surface` into an Explore sub-agent prompt.

The agent's job: find exact-name collisions, near-duplicates, or
overlapping authority across all `.claude/skills/` and
`.claude/commands/` directories in the three vade-app repos.

## Brief template (substitute fields in <ANGLE-BRACKETS>)

```
You are an Explore sub-agent inventorying existing VADE tools to
detect collisions or near-duplicates with a proposed new skill.

## Pre-fetched context (do not re-derive)

A new skill is being authored. Its key parameters:

- Proposed name: <NAME>
- One-line capability: <CAPABILITY_DESCRIPTION>
- Invocation surface: <EXPLICIT|AUTO-DISCOVERABLE|FORKED-CONTEXT>
- Refactor target (if any): <REFACTOR_TARGET_PATH or "none">

VADE has skills + commands in (paths resolved from the same
COO root-resolution block in `/tool-creator` SKILL.md Step 1.1):
- <VADE_COO_MEMORY_DIR>/.claude/skills/
- <VADE_COO_MEMORY_DIR>/.claude/commands/
- <VADE_RUNTIME_DIR>/.claude/skills/
- <VADE_CORE_DIR>/.claude/skills/

Default container layout:
- <VADE_COO_MEMORY_DIR> = /home/user/vade-coo-memory
- <VADE_RUNTIME_DIR>    = /home/user/vade-runtime
- <VADE_CORE_DIR>       = /home/user/vade-core

Peer agents in a different project layout substitute their own
roots before the sub-agent fires. The orchestrator resolves
these from the COO root block (`$COO/../vade-runtime`,
`$COO/../vade-core` by convention) and inlines the resolved
paths into the brief.

Existing inventory at TOOLS.md §3 Skills + §2 Slash commands.

## Your task

1. **List** all skills + commands in the four directories above
   (use `ls`).
2. **Check** for an exact-name collision with `<NAME>`. If found,
   STOP — flag it as a hard collision.
3. **Read frontmatter (or first ~30 lines)** of every skill or
   command whose name overlaps lexically OR whose category seems
   adjacent (e.g., a new `/post-discussion` should check existing
   `/discussion-*`, `/post-*`, anything in `commission-retrospective`
   or `briefing` lineage).
4. **For each candidate**: does its description overlap
   substantively with `<CAPABILITY_DESCRIPTION>`? Score the
   overlap as: NONE / WEAK / SUBSTANTIAL.
5. **Report**.

## Forbidden

Do NOT re-Read CLAUDE.md, identity files, episodic_memory.md,
parallel_instance_protocol.md, this brief, or
`coo/briefings/010-tool-creator-design.md`. The substrate is
already loaded in main context.

## Output schema (≤300 words)

```
## Exact-name collision
<YES with path | NO>

## Near-duplicates (SUBSTANTIAL overlap)
- <path1>: <one-line description>; reason for overlap
- <path2>: ...
(or: NONE)

## Adjacent skills (WEAK overlap, worth knowing)
- <path>: <one-line>
- ...

## Recommendation
<PROCEED | REFACTOR <path> | MERGE-INTO <path> | RENAME-AND-PROCEED>

## Reasoning (3-5 sentences)
```

Be terse. Cite paths.
```

## How the orchestrator consumes this

After the agent returns:

- **Exact-name collision: YES** → STOP Phase 1. Surface to
  operator. Default resolution: set `$refactor_target` to the
  collision path and re-invoke.
- **Near-duplicates SUBSTANTIAL** → SURFACE to operator with the
  agent's reasoning + paths. Operator decides: proceed (the new
  skill is genuinely distinct), refactor existing, or merge.
- **Adjacent skills WEAK** → log for operator awareness; don't
  block.
- **Recommendation `PROCEED`** → continue to Step 1.3 (decide
  frontmatter).

## Why this is a sub-agent, not main-context work

The inventory pass reads ~10-30 frontmatter blocks across three
repos. That's main-context-flooding territory if done in main
context — and the orchestrator only needs the structured report.
Sub-agent isolation keeps the orchestrator's working memory
focused on the operator's design choices.
