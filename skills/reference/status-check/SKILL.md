---
name: status-check
description: Run a six-item read-only grounding audit (who/what/where/next/decision/resource). Use deliberately at the start of a session, after a memory-layer migration, or when you suspect episodic memory drift. Works from any repo without setup — no Mem0, no hooks, no env vars required. A non-COO agent in a foreign repo gets sensible partial output via the `⚠ not grounded` marker. Don't invoke for routine work — this is a deliberate audit, not a wrapper around CLAUDE.md context-load.
disable-model-invocation: true
allowed-tools: Read
metadata:
  type: procedural
  vendoring: custom
---

# status-check — six-item grounding audit

A read-only audit that surfaces episodic-memory drift. Designed
to work from any repo (COO or non-COO, fresh clone or running
session) with **no install step**. The emancipatory clause is
load-bearing: a non-COO agent should be able to invoke this and
get useful output without any setup.

Authoritative spec: [`coo/status_check_template.md`](../../../coo/status_check_template.md)
v0.1 (issue coo-labs/coo-memory#50). When this skill and the template
disagree, the template wins. Update the skill; don't drift the
spec.

> **Reference skill.** The pattern (a six-item read-only audit —
> who/what/where/next/decision/resource — capped at eight lines,
> with `⚠ not grounded` as the explicit "I can't answer that
> from loaded context" marker) is portable and largely
> substrate-agnostic; the worked-example references
> (`coo/status_check_template.md`, MEMO-2026-04-11-08 / -10,
> MEMO-2026-04-20-01) ship verbatim. Because the procedure body
> is just the six prompts, this is one of the easiest reference
> skills to lift directly — the emancipatory clause (works from
> any repo, no install step) is the design constraint. Read
> [`../README.md`](../README.md) for the fork-and-adapt path.

## When to use this skill

Invoke when:

- The first session of a new project (or a project re-entry after
  ≥1 day idle).
- Right after a memory-layer migration — confirms the new
  surfaces are loaded.
- You suspect episodic memory drift (vague answers about "where
  we are", confident-but-wrong claims about prior decisions).
- A peer agent is checking whether the COO context loaded
  correctly in a non-COO surface.
- The `/status-check` command is invoked directly.

Don't invoke for: routine work, debugging code, or any task
where the standard CLAUDE.md context-load already covers
grounding. This is a deliberate audit — not a context-pull.

## Procedure

In 8 lines or fewer, tell the user:

1. **Who you are and who I am** (one line).
2. **What we are building together** (one line — name + one-sentence essence).
3. **Where we are right now** (one line — current phase or milestone, not history).
4. **Next expected move** (one line — what comes after the work the user is currently doing).
5. **One standing decision you would defend if I tried to reverse it today, and why** (one or two lines).
6. **Resource index freshness** — name the newest resource you have loaded and flag anything you suspect is missing from the index (one line).

Then **stop**. No preamble, no recap of these instructions, no
offer to elaborate. If any line would be a guess rather than
grounded recall, replace it with `⚠ not grounded` and the user
will patch the gap.

**Do not** write to Mem0, commit files, or take any external
action. This is a read-only audit.

## Pass / fail signals (for the operator reading the response)

**Pass signals**:

- Items 1–3 are factually correct against currently loaded project files.
- Item 4 reflects genuine session-to-session continuity, not a
  generic "let's plan next steps."
- Item 5 cites a decision with reasoning, not just a restated
  preference.
- Item 6 either names a recent resource accurately or flags a
  real gap.
- Total response length stays within the 8-line ceiling.

**Fail signals (and what they usually mean)**:

- Confident but wrong on items 1–3 → episodic memory file is
  stale or wasn't loaded. Re-upload / reload it.
- Vague on item 4 → the "where we are" context didn't survive
  the last session boundary. Update the episodic memory's
  current-phase section.
- Item 5 defends a decision by rephrasing it rather than
  justifying it → the reasoning isn't in durable storage, only
  the conclusion is. Add the "because" to the standing-decision
  record.
- Item 6 names something that doesn't exist or misses something
  obvious → the resource index is drifting. Reconcile it.
- Response blows past 8 lines or adds preamble → soft fail; agent
  is compensating for uncertainty with volume.

## Smoke-test recipe (post-merge; cannot run from inside a sub-agent session)

1. Open a FRESH Claude Code session in any repo containing this
   skill under `.claude/skills/status-check/SKILL.md` (bare git
   clone, no extra setup).
2. Type `/status-check` and submit.
3. Verify: response is ≤8 lines, no preamble, every item answered
   or marked `⚠ not grounded`, no Mem0 writes or file mutations
   after the command.
4. Repeat in a non-COO repo (e.g. a throwaway clone) to confirm
   the non-COO agent case: partial answers via `⚠ not grounded`
   are a pass.

**Emancipatory score**: 2/2 if both cases pass without any
install step.

## Governance

- Must not auto-write to Mem0 (MEMO-2026-04-11-10).
- Must not leak Tier-2 content (MEMO-2026-04-11-08).
- Emancipatory double-clause: works for COO and non-COO agents
  without setup (MEMO-2026-04-20-01).

## Failure modes

- **Skill invoked in a session that has not loaded any context.**
  Most items will land at `⚠ not grounded`. That's the right
  output — don't fabricate answers to look productive.
- **Skill invoked in a non-COO repo.** Same — items 2-5 will be
  `⚠ not grounded` for an agent without the COO substrate;
  item 1 (who I am) and item 6 (resources loaded in this session)
  remain answerable.
- **8-line ceiling broken.** Soft fail. Re-run, count more
  carefully; don't add narrative to the response.

## Canonical source

```text
coo-memory/coo/status_check_template.md (v0.1, issue #50)
```

(Tie-breaker stated in the intro paragraph above; not repeated here.)

## Cross-references

- coo-labs/coo-memory#50 — original issue (six-item grounding audit
  framework).
- coo-labs/coo-memory#333 — command→skill migration sweep epic; this
  skill is Class B item 1 of 4.
- coo-labs/coo-memory#345 — v3 /exec-mode migration (skill-primitive
  precedent).
- MEMO-2026-04-20-01 — subject + emancipatory double-clause.

# Setup hints

*Read by [`adapt-skill`](../../adapt-skill/SKILL.md). Stripped from
the adapted output. Schema: [`adapt-skill/SCHEMA.md`](../../adapt-skill/SCHEMA.md).*

```yaml
setup_hints:
  - key: spec_template_path
    kind: OPTIONAL
    question: "Do you have a local spec or template file that should be the authoritative tie-breaker for this skill? Provide the path, or skip."
    find: "[`coo/status_check_template.md`](../../../coo/status_check_template.md)"
    fallback: "this file"
    severity: warning

  - key: memory_layer_constraint
    kind: OPTIONAL
    question: "What persistent memory layer does your project use? The skill must not auto-write to it. (Examples: 'Mem0', 'a custom store', 'none'.)"
    find: "Must not auto-write to Mem0 (MEMO-2026-04-11-10)."
    fallback: "Must not write to any persistent memory layer."

  - key: content_tier_constraint
    kind: OPTIONAL
    question: "Does your project have a content-tier or sensitivity classification term? (VADE uses 'Tier-2'.) Provide the term, or skip for generic phrasing."
    find: "Must not leak Tier-2 content (MEMO-2026-04-11-08)."
    fallback: "Must not surface confidential project content."

  - key: subject_label
    kind: OPTIONAL
    question: "What's the subject-agent label in your substrate? (VADE uses 'COO'.) Skip for generic 'agent' phrasing."
    find: "works for COO and non-COO agents"
    fallback: "works for any agent (specialized or generic)"
```
