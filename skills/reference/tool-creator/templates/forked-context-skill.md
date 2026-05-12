# Template — forked-context skill

For skills that should run in isolated subagent context, not the
main conversation. Use when the skill's intermediate work would
flood the main context window — long research tasks, multi-step
investigations, parallel evaluations.

## Frontmatter

```yaml
---
name: <NAME>
description: <ONE-PARAGRAPH-WHAT>. <ONE-PARAGRAPH-WHEN-TO-USE>. <ONE-PARAGRAPH-DON'T-INVOKE-FOR>.
context: fork
---
```

**Optional fields:**

```yaml
# disable-model-invocation: true   # if explicit-only
# allowed-tools: Read, Bash, WebFetch
# arguments:
#   <ARG_NAME>: <ARG_DESCRIPTION>
```

## What `context: fork` does

The skill runs in a subagent context (separate transcript, own
context window), inheriting the parent's conversation history at
fork time. Results return to the parent; intermediate work
(searches, file reads, log parses) stays in the subagent
transcript.

This is correct for skills where:

- Intermediate work would crowd main context (e.g., reading 20
  files to extract one fact)
- Parallel investigation would benefit from isolation (e.g.,
  evaluating two competing approaches independently)
- The skill spawns its own sub-tasks and synthesizes their output

This is wrong for skills where:

- The operator wants to see intermediate steps (use a regular
  skill in main context — the iteration IS the point)
- The skill modifies the working tree as it runs (subagent
  isolation can't share the tree cleanly with the parent's
  uncommitted changes)
- Tool authoring or any flow where the operator iterates
  draft-by-draft (use `explicit-invocation-skill.md` instead)

## Body skeleton

```markdown
# <name> — <one-line capability>

<intro: what the skill does, why it runs in forked context, what
it returns to the parent>

## When to use this skill

- <trigger 1>
- <trigger 2>

Don't invoke for:

- <anti-trigger 1: e.g., "tasks where intermediate output is the
  point — use <other skill> in main context instead">

## Inputs

- **`<ARG_NAME>`** — <description>
- **`<ARG_NAME>`** — <description>

## Procedure (runs in subagent context)

<steps the subagent performs; can include further sub-agent
dispatches — though Anthropic's spec says subagents cannot nest,
so any further dispatch must come from the parent>

## Output to parent

<structured shape of what the subagent returns. Schema enforces
small surface area:>

```
{
  "summary": "<2-3 sentence summary>",
  "findings": ["<finding 1>", "<finding 2>", ...],
  "recommendations": ["<rec 1>", ...],
  "needs_parent_decision": ["<flag 1>", ...]   // optional
}
```

## Cross-references

- <related skills>
- <related sub-agent definitions in `.claude/agents/`>
```

## Naming notes

- `context: fork` skills are best named for the *output* they
  produce, not the *internal work*. Operator cares about what
  comes back to the main context.
- Document the output schema in the body. The subagent should
  return a small, structured payload; verbose intermediate
  output stays in the subagent transcript.

## Caveat — vade has zero forked-context skills today

As of 2026-04-30, no vade skill uses `context: fork`. The pattern
is documented here for completeness; the first vade use case will
need to validate that:

1. The fork actually preserves the relevant parent context
2. The output schema reaches the parent intact
3. Working-tree changes from a forked skill are appropriately
   isolated (or that the skill is read-only)

If you're authoring the first forked-context vade skill, treat it
as a research spike — drop a paired issue to capture findings
back into this template. **File findings as a follow-up to
vade-coo-memory#322 (or a successor issue)** so this template
can be updated with the validated assumptions; otherwise the
caveat bitrots.

## Adjacent pattern — Agent tool dispatch

If the skill's natural shape is "spawn a subagent and synthesize
its output," consider whether it should be a sub-agent
definition (`.claude/agents/<name>.md`) instead of a forked-context
skill. Sub-agent definitions are dispatched via the Agent tool
with a custom prompt, and may fit "single-purpose investigator"
shapes better than `context: fork` skills.

The decision: sub-agent definitions are *templates the
orchestrator instantiates per call*; forked-context skills are
*reusable workflows that always run forked*. For one-off
investigations, sub-agent template wins. For a recurring "always
run isolated" workflow, forked-context skill wins.
