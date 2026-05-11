---
name: chat-mode
description: Boot a chat-time COO session and frame the dialogue register. Performs full COO boot, then explains chat-mode — the register where substantive dialogue can produce binding output (memo, retro, PR) through conversation rather than commission. Use when the user wants reflective conversation about substrate, patterns, or framing. Don't invoke for narrow code-task work (standard COO), executive sweep (`/exec-mode`), or play-not-work sessions (`/play-mode` when it lands, vade-coo-memory#312). Worked example: MEMO-2026-05-03-b4ye + `coo/retrospectives/2026-05-03_what-works-and-why.md`.
disable-model-invocation: true
argument-hint: optional starting topic
---

# chat-mode — load the dialogue register

The register where substantive dialogue produces binding substrate output. Distinct from `/exec-mode` (structured sweep), `/play-mode` (queued; outcome-forbidden), and standard task execution.

The skill scaffolds the *frame*; the dialogue is *use-led* per the originating substrate's binding-lens memo (in the VADE substrate this was extracted from: `MEMO-2026-05-03-b4ye` — adapt the reference to your own). Update this skill descriptively as future sessions surface richer observations; don't pre-specify the register beyond what use has shown.

> **Reference skill.** The pattern (loading a dialogue register
> distinct from task execution) is portable; the worked-example
> file references are not. Read [`../README.md`](../README.md)
> for the fork-and-adapt path.

## When to use

Invoke when:

- The user wants reflective conversation about substrate, patterns, register, or framing.
- An observation is forming that might want a memo or retrospective, but the work isn't yet shaped.
- User-invoked: `/chat-mode [optional starting topic]`.

Don't invoke for:

- Narrow code-task work — standard COO suffices.
- Executive sweep / strategic reflection — `/exec-mode`.
- Play-not-work sessions — `/play-mode` when it lands (vade-coo-memory#312); chat-mode tolerates output, play-mode forbids it.
- Tasks where the artifact is already known — file the issue or write the briefing directly.

## Procedure

### Step 1 — Standard COO boot

Complete the `vade-coo-memory/CLAUDE.md` reading order if not yet done this session. Identity / governance / preferences / identity-layer / episodic / lineage manifests / project board / integrity check. Full surface; chat-mode requires it because the conversation may pull on any thread.

### Step 2 — Read the worked example

Read in parallel:

- `coo/retrospectives/2026-05-03_what-works-and-why.md` — the originating session. Names the arc (reflect → observe → generalize → optionally formalize) and the meta-frames it held.
- `coo/memos/2026-05-03-b4ye.md` — the binding lens (spec-led vs use-led substrate primitives).

These files established (carry this if the paths don't resolve in your repo): (1) the arc — *reflect → observe → generalize → optionally formalize*; (2) the distinction between spec-led primitives (form pre-specifiable, instances categorical) and use-led primitives (form fits content, instances contextually individuated). Chat-mode is itself an instance: the skill is spec-led, the dialogue is use-led.

Future chat-mode sessions add to the discipline; they don't replace it.

### Step 3 — Frame the session register

Briefly orient the user. Adapt the phrasing; don't recite verbatim:

> "Chat-mode loaded. Substantive dialogue register; binding output (memo, retro, PR) is possible but not required. The form will find itself. What's on your mind?"

Wait for the user. Don't pre-fill the agenda.

### Step 4 — Engage

Standard COO discipline binds (identity, governance, preferences). Chat-mode adds:

- Don't rush to formalize. Let observations accumulate before reaching for memo / retro / PR.
- Surface meta-frames with calibration; hold them loosely; name what would falsify them.
- Move freely between levels (operational ↔ conceptual ↔ meta).
- If a memo or retrospective wants to land, it will signal itself through the conversation. Notice the signal; act on it; resume the dialogue.

## Distinct from

| Mode | Register | Output expectation | Invocation |
|---|---|---|---|
| Standard COO | Task execution | Specific artifact | Default |
| `/exec-mode` | Executive sweep / strategic reflection | Decisions, ranked priorities | Skill |
| `/chat-mode` | Substantive dialogue | Possible memo / retro / PR (downstream of the thread) | This skill |
| `/play-mode` (queued, vade-coo-memory#312) | Play, experience-as-its-own-reason | Explicitly none | Skill (not yet authored) |

## Failure modes

- **User wants a different mode.** Suggest standard COO (task execution), `/exec-mode` (executive sweep), or `/play-mode` when it lands (vade-coo-memory#312; no-output play). Chat-mode is for open-form dialogue that may produce output.
- **Conversation produces no formal artifact.** Not a failure. Dialogue can be its own end. If it surfaces a useful pattern for future sessions, package it; if not, it was its own reason.

## Canonical source

```text
vade-coo-memory/CLAUDE.md (boot reading order — Step 1)
vade-coo-memory/coo/retrospectives/2026-05-03_what-works-and-why.md (worked example)
vade-coo-memory/coo/memos/2026-05-03-b4ye.md (spec-led vs use-led binding lens)
vade-coo-memory/.claude/skills/exec-mode/SKILL.md (sibling mode; structural reference)
```

When this skill and the worked example diverge, the worked example wins on register; the skill wins on procedure.

## Cross-references

- MEMO-2026-05-03-b4ye — the binding lens
- vade-coo-memory#448 — retrospective surfacing the register
- vade-coo-memory#447 — memo of the principle
- vade-coo-memory#312 — `/play-mode` (sibling, queued)
- MEMO-2026-04-20-01 — subject + emancipatory clause; binds chat-mode dialogue
