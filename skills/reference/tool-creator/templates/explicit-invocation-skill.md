# Template — explicit-invocation skill

For skills that the operator invokes deliberately via `/<name>`,
where auto-discovery would be noise. Examples: `/memo`,
`/post-discussion`, `/tool-creator` itself.

## Frontmatter

```yaml
---
name: <NAME>                # e.g., post-discussion, memo, tag-milestone
description: <ONE-PARAGRAPH>. <ONE-PARAGRAPH-WHEN-TO-USE>. <ONE-PARAGRAPH-DON'T-INVOKE-FOR>.
disable-model-invocation: true
---
```

**Optional fields** (uncomment + fill if needed):

```yaml
# allowed-tools: Bash, Read, Write, Edit
# arguments:
#   <ARG_NAME>: <ARG_DESCRIPTION>
```

## What `disable-model-invocation: true` does

Strips the skill's description from Claude's context entirely.
Claude will not know about the skill unless the operator types
`/<name>`. Auto-invocation cannot fire. The full SKILL.md body
loads only at explicit invocation.

This is correct for skills where:

- Action is deliberate (write a memo, post a discussion, tag a
  milestone)
- Side effects are real (opens a PR, modifies a file, posts a
  comment)
- Operator should always be in the loop

This is wrong for skills where:

- Claude should propose the skill when the task matches (use
  `auto-discoverable-skill.md` instead)
- The skill is reference / knowledge (e.g., docs lookups —
  `auto-discoverable-skill.md` again)

## Body skeleton

```markdown
# <name> — <one-line capability>

<2-3 paragraph intro: what the skill does, what its authoritative
spec is (if any — e.g., a SOP file), what it doesn't do.>

## When to use this skill

Invoke when:

- <trigger 1>
- <trigger 2>

Don't invoke for:

- <anti-trigger 1: e.g., "trivial one-off scripts">
- <anti-trigger 2>

## Procedure

### Step 1 — <name>

<concrete steps, code blocks for shell commands, paths absolute
where the cwd is unknown>

### Step 2 — <name>

<...>

## Failure modes

- **<failure 1>** — <how to recover>
- **<failure 2>** — <how to recover>

## Canonical source

<paths or URLs that constitute the SOT for this skill's content;
when this skill and the SOT disagree, SOT wins>

## Cross-references

- <related issue or memo numbers>
- <related skills or commands>
```

## Naming notes

- Skill name = lowercase, hyphenated. Slash-invocation form is
  `/<name>` (Claude Code surfaces both `.claude/commands/<name>.md`
  and `.claude/skills/<name>/SKILL.md` as `/<name>`).
- Description: write the first sentence as the action. Include
  "Use when..." as a sentence, not a bullet — it lands in
  Claude's prompts as prose.
- Description length cap: ~1500 chars combined `description` +
  `when_to_use` per Anthropic's spec. Keep tight.

## Worked example

The /memo-sync command body shows the canonical shape for a
`disable-model-invocation: true` skill:

- Frontmatter is minimal: name + description.
- Body opens with what the skill does + its SOP reference.
- "When to use" + "don't invoke for" lists are explicit.
- Procedure uses bash code blocks with COO root resolution.
- Failure modes section names known issues + recovery paths.

`vade-coo-memory/.claude/skills/memo-sync/SKILL.md` is a
reasonable model to copy structure from when authoring a new
explicit-invocation skill.
