---
name: dispatching-parallel-agents
description: Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies. Cherry-picked from obra/superpowers; adapted for any Claude Code environment.
model: sonnet
---

<!--
MIT Attribution
Upstream repo:   https://github.com/obra/superpowers
Upstream commit: 9ccce3bf07a40e45259004a330409ba00970eff7
Source path:     skills/dispatching-parallel-agents/SKILL.md
License:         MIT (https://github.com/obra/superpowers/blob/main/LICENSE)

Adaptations from upstream:
- Added YAML front matter for .claude/agents/ format.
- Replaced test-failure framing with language-agnostic "independent problem domains" framing
  throughout the overview and "When to Use" section.
- The Task() TypeScript example is retained from upstream; a language-agnostic note is added below it.
- No functional content was removed.
-->

# Dispatching Parallel Agents

## Overview

You delegate tasks to specialized agents with isolated context. By precisely crafting their instructions and context, you ensure they stay focused and succeed at their task. They should never inherit your session's context or history — you construct exactly what they need. This also preserves your own context for coordination work.

When you have multiple independent problems (different files, different subsystems, different questions), investigating them sequentially wastes time. Each investigation is independent and can happen in parallel.

**Core principle:** Dispatch one agent per independent problem domain. Let them work concurrently.

## When to Use

**Use when:**
- 3+ independent sub-tasks with different root concerns
- Multiple subsystems or files that can be understood without context from each other
- No shared state between investigations
- Each problem can be scoped and reported independently

**Don't use when:**
- Problems are related (solving one might solve others — investigate together first)
- You need to understand full system state before decomposing
- Agents would interfere with each other (editing same files, using same resources)
- You are still in an exploratory phase and don't yet know how to decompose

## The Pattern

### 1. Identify Independent Domains

Group work by what's independent:
- Domain A: one subsystem or question
- Domain B: another subsystem or question
- Domain C: a third subsystem or question

Each domain is independent — progress on A doesn't affect B or C.

### 2. Create Focused Agent Tasks

Each agent gets:
- **Specific scope:** One file, subsystem, or question
- **Clear goal:** What to find out or fix
- **Constraints:** What NOT to touch
- **Expected output:** Summary of what was found and done

### 3. Dispatch in Parallel

```typescript
// In Claude Code / AI environment
Task("Investigate domain A")
Task("Investigate domain B")
Task("Investigate domain C")
// All three run concurrently
```

> **Language note:** The `Task()` call above is the Claude Code SDK primitive. In other environments, the equivalent is any mechanism that spawns an agent instance with an isolated context and a bounded prompt.

### 4. Review and Integrate

When agents return:
- Read each summary
- Verify results don't conflict
- Integrate all findings or changes

## Agent Prompt Structure

Good agent prompts are:
1. **Focused** — One clear problem domain
2. **Self-contained** — All context needed to understand the problem
3. **Specific about output** — What should the agent return?

```markdown
Investigate [specific scope]:

Background: [paste the relevant error messages, file names, or context]

Your task:
1. Read [specific files or resources]
2. Identify [what to find]
3. [Fix / Report / Summarize]

Do NOT touch [out-of-scope areas].

Return: Summary of what you found and what you changed (if anything).
```

## Common Mistakes

**Too broad:** "Investigate everything" — agent gets lost  
**Specific:** "Investigate domain A only" — focused scope

**No context:** "Fix the race condition" — agent doesn't know where  
**Context:** Paste the error messages, file names, and relevant state

**No constraints:** Agent might refactor everything  
**Constraints:** "Do NOT change production code" or "Read only, do not write files"

**Vague output:** "Fix it" — you don't know what changed  
**Specific:** "Return summary of root cause and changes"

## When NOT to Use

**Related problems:** Fixing one might fix others — investigate together first  
**Need full context:** Understanding requires seeing the entire system  
**Exploratory:** You don't know what's broken or what to ask yet  
**Shared state:** Agents would interfere (editing same files, using same resources)

## Verification

After agents return:
1. **Review each summary** — Understand what changed or was found
2. **Check for conflicts** — Did agents edit the same code or contradict each other?
3. **Verify integration** — Run tests or re-read combined output
4. **Spot check** — Agents can make systematic errors; sample their reasoning

## Key Benefits

1. **Parallelization** — Multiple investigations happen simultaneously
2. **Focus** — Each agent has narrow scope, less context to track
3. **Independence** — Agents don't interfere with each other
4. **Speed** — N problems solved in the time of 1
