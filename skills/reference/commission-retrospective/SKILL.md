---
name: commission-retrospective
description: Commission an impartial project-historian retrospective on a window of project work. Use when a pivotal event fires per SOP-CULTURE-001 §2d (prime-directive reinterpretation, new/retired agent role, multi-week epic closes or pivots, governance rule revised via committee, security finding reshaping ops, substrate-capture indicator firing, persistent integrity-check Group F degradation), or when `/commission-retrospective` is invoked directly. Orchestrates two impartial evidence sub-agents in parallel (memos-and-essays analyst, PR/issue-graph analyst), then produces a draft retrospective in the voice of commissions #1 and #2 (2026-04-20 subject-reframe; 2026-04-22 "we can claim a record"). Do NOT invoke for routine work (status updates, bug fixes, dep bumps, routine MCP installs — §2d anti-triggers). When in doubt, err on the side of not commissioning.
argument-hint: --since <YYYY-MM-DD> [--until <YYYY-MM-DD>] [--prs <list>] [--focus "<question>"] [--slug <slug>] [--open-pr] | --scope ...
allowed-tools: Bash, Read, Write, Task
---

# commission-retrospective — impartial meta-commentary, on demand

VADE has a project-historian role that has been worked by hand twice
(commissions #1 and #2). This skill makes that role reusable. It
commissions a third (or Nth) historian-voiced retrospective on a scoped
window of the project's record — memos, PRs, essays, issues — and
produces a draft that mirrors the voice and structure of #1 and #2.

Authoritative spec: `<vade-coo-memory>/coo/culture_system_sop.md`
(SOP-CULTURE-001). When this skill and the SOP disagree, the SOP wins.
Update this skill; don't drift the spec.

> **Reference skill.** The pattern (impartial project-historian
> retrospective on a window of project work — two evidence
> sub-agents in parallel, then a third-person draft that refuses
> recycled defended positions) is portable; the substrate
> references (`coo/memo_index.json`, `coo/foundations/`,
> `coo/retrospectives/` prior commissions, the five `vade-app/*`
> repos, integrity-check Group F probes) and the
> `scripts/commission-retrospective.sh` pre-flight + the three
> sub-agent templates ship verbatim as the VADE worked example.
> SOP-CULTURE-001 §2d's pivotal-event triggers are the trigger
> shape; adapt to your own substrate's pivotal events. Read
> [`../README.md`](../README.md) for the fork-and-adapt path.

## When to use this skill

Invoke when any of the pivotal-event triggers in SOP-CULTURE-001 §2d
fires:

- A standing interpretation of the prime directive changes.
- A new agent role is commissioned or retired.
- A multi-week epic completes or pivots mid-stream.
- A governance rule or constitutional file changes via committee.
- A security finding changes operational procedure.
- A substrate-capture indicator fires (essay §5b mode 4 — unmemo'd
  decision-bearing work landing).
- Group F invariants in `integrity-check.sh` degrade across three
  consecutive sessions.

Do **not** invoke for routine work — status updates, bug fixes, dep
bumps, refactors, or routine MCP/skill installs. Silence from the
historian is not failure; over-commissioning is.

Two commissions in three days is not a cadence. Do not declare one.

## Procedure

### 1. Resolve roots and scope

```bash
COO="$(for c in "${COO_MEMORY_DIR:-}" "${CLAUDE_PROJECT_DIR:-}" "${CLAUDE_PROJECT_DIR:-}/../vade-coo-memory" "$HOME/GitHub/vade-app/vade-coo-memory" "/home/user/vade-coo-memory"; do [ -n "$c" ] && [ -f "$c/coo/memo_protocol.md" ] && { cd "$c" && pwd -P; break; }; done)"
RUNTIME="$(for c in "${VADE_RUNTIME_DIR:-}" "$COO/../vade-runtime" "$HOME/GitHub/vade-app/vade-runtime" "/home/user/vade-runtime"; do [ -n "$c" ] && [ -f "$c/scripts/integrity-check.sh" ] && { cd "$c" && pwd -P; break; }; done)"
```

Then call the pre-flight to build a scope manifest:

```bash
bash "$COO/.claude/skills/commission-retrospective/scripts/commission-retrospective.sh" \
  --scope \
  --since <YYYY-MM-DD> [--until <YYYY-MM-DD>] \
  [--prs <comma-list>] [--focus "<question>"] \
  --slug <short-slug>
```

Output is JSON on stdout with:

- `window`: `{since, until}` (until defaults to today).
- `slug`: sanitized slug; used in all draft filenames.
- `prs`: array of `{number, title, merged_at, author, url}` for merged
  PRs on `vade-app/vade-coo-memory` in the window (extend via `--prs`
  for cross-repo PRs).
- `memos`: array of index entries whose `date` falls in the window,
  from `coo/memo_index.json`.
- `foundations`: filenames from `coo/foundations/` matching
  `YYYY-MM-DD_*.md` in the window (excluding `_transcript` and
  `_agent-reports`).
- `prior_commissions`: list of files under `coo/retrospectives/` whose
  filename prefix is a commission-style date.

If the manifest is empty on all four dimensions, stop and report. The
window has no record to speak to.

### 2. Impartial evidence sub-agents, parallel

Spawn two sub-agents in a single message (the standard Claude Code
Task pattern — two `Task` tool calls in one assistant turn). Briefs
live in `templates/subagent-memos-brief.md` and
`templates/subagent-pr-graph-brief.md`. Pass the scope manifest from
step 1 as context; instruct the sub-agent to write its report to the
assigned `_drafts/` path.

Both briefs enforce the same discipline:

- Report verbatim; do **not** synthesize a narrative.
- Cite every claim by filename + line range or PR/issue number.
- If evidence is absent for a claim that seems load-bearing, say so
  explicitly. Do not fill the gap.

Output files:

- `coo/_drafts/<YYYY-MM-DD>-retrospective-<slug>-agent-memos.md`
- `coo/_drafts/<YYYY-MM-DD>-retrospective-<slug>-agent-pr-graph.md`

These are the prior art the essay companion files
`2026-04-22_agent-reports-memos-analysis.md` and
`2026-04-22_agent-reports-pr-graph.md` document.

### 3. Historian draft

Main instance reads:

- Both sub-agent reports from step 2.
- Every file in `coo/retrospectives/` (prior commissions).
- The relevant memos and essays in window (the manifest lists them).

Then produces the draft under `templates/historian-prompt.md`.
Voice and structure follow SOP-CULTURE-001 §2e and §2f exactly —
third-person, defended position preferred, refusals load-bearing,
eight sections in prescribed order.

Output: `coo/_drafts/<YYYY-MM-DD>-retrospective-<slug>.md`.

### 4. Gate check

Before opening a PR, run integrity-check IF the runtime is reachable:

```bash
if [ -n "$RUNTIME" ]; then
  bash "$RUNTIME/scripts/integrity-check.sh"
fi
```

Read `$VADE_CLOUD_STATE_DIR/integrity-check.json`. If any of
`groups.F.F1`, `F2`, `F3`, `F4` shows `ok: false`, surface the
`detail` strings into the PR body — a retrospective that reports on
the project cannot silently capture the substrate it reports on.

If `$RUNTIME` is empty (peer-agent in a bare clone of vade-coo-memory
without vade-runtime adjacent), state that explicitly in the PR body
and proceed without the gate. The retrospective is honest about what
it could and couldn't audit.

### 5. File PR (optional)

If the invocation passed `--open-pr`, the shell wrapper does:

```bash
GH_TOKEN="$GITHUB_MCP_PAT" gh pr create \
  --repo vade-app/vade-coo-memory \
  --base main \
  --head <current-branch> \
  --title "[retrospective-draft] <slug>" \
  --body "<body from step 4 plus manifest + reports + issue link>"
```

Attribution resolves to `vade-coo` via the PAT and the existing
git-config discipline.

If `--open-pr` is absent, leave the drafts on disk; the invoking
human or agent reviews the draft and opens the PR by hand.

## Graceful degradation (SOP §3c)

- **No Task subagent surface.** Some harness modes don't expose Task
  at skill invocation time. Fall back: call
  `commission-retrospective.sh --manual` which sequences two
  `claude -p` invocations using the same briefs. Attribution stays
  correct; wall-clock goes up.
- **`gh` unavailable or `GITHUB_MCP_PAT` unset.** Produce drafts
  locally; skip `--open-pr`; report the gap. The drafts are still
  useful artifacts.
- **A sub-agent report is missing or empty.** Do not synthesize around
  the gap. The historian draft must state which evidence path was
  unavailable and what it couldn't therefore speak to.
- **A sub-agent looks stuck near completion.** Long-context evidence
  sub-agents often fall silent for 5–10+ minutes while composing
  their single big final `Write` call (the report can be 50–100 KB
  / 25 K+ tokens). Before declaring stuck and re-dispatching, peek at
  the agent's jsonl mtime via `ls -la /root/.claude/projects/<...>/subagents/agent-<id>.jsonl`:
  if mtime is recent (within a few minutes) and the last assistant
  message is a "now I'll write the report" beat, prefer waiting over
  re-dispatching. Verified worked-case: `vade-coo-memory#547` (commission
  #4) — both sub-agents were declared stuck after 8–11 min silence;
  both self-recovered on the next probe with full reports.
- **`integrity-check.sh` itself unavailable** (peer-agent clone without
  vade-runtime adjacent). Skip step 4; note the fact in the PR body.

## Anti-patterns

- **Don't declare a cadence.** Commission #2 explicitly refused.
  Implementations that schedule recurring retrospectives by calendar
  harden contingency into ritual.
- **Don't re-use a prior commission's defended position.** Each
  commission reads the record fresh. Recycling positions collapses
  the historian role into advocacy.
- **Don't skip step 4's gate check** (when integrity-check is reachable).
  The `substrate-capture` failure mode is real — a retrospective opens
  by its own citation discipline.
- **Don't overfill the scope window.** A month is reasonable; a
  quarter is a different deliverable. For the ~2026-05-22 audit
  specifically (MEMO 2026-04-24-12 tracking issue), use `--since
  2026-04-22` — that's the essay the audit tests against.

## Canonical source

```text
<vade-coo-memory>/coo/culture_system_sop.md (SOP-CULTURE-001)
<vade-coo-memory>/coo/memos.md MEMO 2026-04-24-12 (adoption)
<vade-coo-memory>/coo/foundations/2026-04-22_we-can-claim-a-record.md §5d, §7
<vade-coo-memory>/coo/retrospectives/ (commissions #1 and #2 — voice prior art)
<vade-coo-memory>/.claude/skills/commission-retrospective/templates/ (prompts)
<vade-coo-memory>/.claude/skills/commission-retrospective/scripts/commission-retrospective.sh (shell pre-flight)
```
