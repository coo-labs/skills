---
name: commission-retrospective
description: Commission an impartial project-historian retrospective on a window of project work. Use when a pivotal event fires per SOP-CULTURE-001 §2d (prime-directive reinterpretation, new/retired agent role, multi-week epic closes or pivots, governance rule revised via committee, security finding reshaping ops, substrate-capture indicator firing, persistent integrity-check Group F degradation), or when `/commission-retrospective` is invoked directly. Orchestrates two impartial evidence sub-agents in parallel (memos-and-essays analyst, PR/issue-graph analyst), then produces a draft retrospective in the voice of commissions #1 and #2 (2026-04-20 subject-reframe; 2026-04-22 "we can claim a record"). Do NOT invoke for routine work (status updates, bug fixes, dep bumps, routine MCP installs — §2d anti-triggers). When in doubt, err on the side of not commissioning.
argument-hint: --since <YYYY-MM-DD> [--until <YYYY-MM-DD>] [--prs <list>] [--focus "<question>"] [--slug <slug>] [--open-pr] | --scope ...
allowed-tools: Bash, Read, Write, Task
metadata:
  type: procedural
  vendoring: custom
---

# commission-retrospective — impartial meta-commentary, on demand

VADE has a project-historian role that has been worked by hand twice
(commissions #1 and #2). This skill makes that role reusable. It
commissions a third (or Nth) historian-voiced retrospective on a scoped
window of the project's record — memos, PRs, essays, issues — and
produces a draft that mirrors the voice and structure of #1 and #2.

Authoritative spec: `<coo-memory>/coo/culture_system_sop.md`
(SOP-CULTURE-001). When this skill and the SOP disagree, the SOP wins.
Update this skill; don't drift the spec.

> **Reference skill.** The pattern (impartial project-historian
> retrospective on a window of project work — two evidence
> sub-agents in parallel, then a third-person draft that refuses
> recycled defended positions) is portable; the substrate
> references (`coo/memo_index.json`, `coo/foundations/`,
> `coo/retrospectives/` prior commissions, the five `coo-labs/*`
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
COO="$(for c in "${COO_MEMORY_DIR:-}" "${CLAUDE_PROJECT_DIR:-}" "${CLAUDE_PROJECT_DIR:-}/../coo-memory" "$HOME/GitHub/coo-labs/coo-memory" "/home/user/coo-memory"; do [ -n "$c" ] && [ -f "$c/coo/memo_protocol.md" ] && { cd "$c" && pwd -P; break; }; done)"
RUNTIME="$(for c in "${VADE_RUNTIME_DIR:-}" "$COO/../coo-harness" "$HOME/GitHub/coo-labs/coo-harness" "/home/user/coo-harness"; do [ -n "$c" ] && [ -f "$c/scripts/integrity-check.sh" ] && { cd "$c" && pwd -P; break; }; done)"
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
  PRs on `coo-labs/coo-memory` in the window (extend via `--prs`
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

If `$RUNTIME` is empty (peer-agent in a bare clone of coo-memory
without coo-harness adjacent), state that explicitly in the PR body
and proceed without the gate. The retrospective is honest about what
it could and couldn't audit.

### 5. File PR (optional)

If the invocation passed `--open-pr`, the shell wrapper does:

```bash
GH_TOKEN="$GITHUB_MCP_PAT" gh pr create \
  --repo coo-labs/coo-memory \
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
  re-dispatching. Verified worked-case: `coo-labs/coo-memory#547` (commission
  #4) — both sub-agents were declared stuck after 8–11 min silence;
  both self-recovered on the next probe with full reports.
- **`integrity-check.sh` itself unavailable** (peer-agent clone without
  coo-harness adjacent). Skip step 4; note the fact in the PR body.

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
<coo-memory>/coo/culture_system_sop.md (SOP-CULTURE-001)
<coo-memory>/coo/memos.md MEMO 2026-04-24-12 (adoption)
<coo-memory>/coo/foundations/2026-04-22_we-can-claim-a-record.md §5d, §7
<coo-memory>/coo/retrospectives/ (commissions #1 and #2 — voice prior art)
<coo-memory>/.claude/skills/commission-retrospective/templates/ (prompts)
<coo-memory>/.claude/skills/commission-retrospective/scripts/commission-retrospective.sh (shell pre-flight)
```

# Setup hints

*Read by [`adapt-skill`](../../adapt-skill/SKILL.md). Stripped from
the adapted output. Schema: [`adapt-skill/SCHEMA.md`](../../adapt-skill/SCHEMA.md).
The shell pre-flight is REGENERATE-PER-USER; the three templates
are PARAMETERIZE. The pivotal-event trigger list (SOP-CULTURE-001
§2d) is project-philosophy — surface to the user for definition
rather than mechanical substitution.*

```yaml
setup_hints:
  - key: pivotal_triggers
    kind: PROMPT
    question: "List your project's 'pivotal event' triggers — what conditions should cause a commission-retrospective to fire? (VADE uses 7 triggers including prime-directive reinterpretation, agent-role changes, multi-week epic close, governance changes, security findings, substrate-capture indicators, persistent integrity-check degradation.) Provide as a bulleted list; the trigger logic ports."
    find_unique: true
    find: |
      - A standing interpretation of the prime directive changes.
      - A new agent role is commissioned or retired.
      - A multi-week epic completes or pivots mid-stream.
      - A governance rule or constitutional file changes via committee.
      - A security finding changes operational procedure.
      - A substrate-capture indicator fires (essay §5b mode 4 — unmemo'd
        decision-bearing work landing).
      - Group F invariants in `integrity-check.sh` degrade across three
        consecutive sessions.
    fallback: |
      - <Trigger 1 — describe your project's pivotal events here.>
      - <Trigger 2.>
      - <Trigger 3.>
      (Edit this list before invoking the skill. Don't leave placeholders.)

  - key: data_root_var
    kind: PROMPT
    question: "Shell variable for the project root? (VADE uses $COO.) Examples: $REPO, $REPO_ROOT, $PROJECT."
    find: "$COO"
    fallback: "$REPO_ROOT"

  - key: runtime_root_var
    kind: OPTIONAL
    question: "Shell variable for a sibling repo holding your integrity-check / health script? (VADE uses $RUNTIME pointing at vade-runtime.) Skip if you have no separate runtime repo."
    find: "$RUNTIME"
    fallback: "$RUNTIME"

  - key: data_root_discovery
    kind: OPTIONAL
    question: "Step 1 discovers two roots (data and runtime) via sentinel files. Skip to use git rev-parse for the data root and drop the runtime probe."
    find_unique: true
    find: |
      ```bash
      COO="$(for c in "${COO_MEMORY_DIR:-}" "${CLAUDE_PROJECT_DIR:-}" "${CLAUDE_PROJECT_DIR:-}/../coo-memory" "$HOME/GitHub/coo-labs/coo-memory" "/home/user/coo-memory"; do [ -n "$c" ] && [ -f "$c/coo/memo_protocol.md" ] && { cd "$c" && pwd -P; break; }; done)"
      RUNTIME="$(for c in "${VADE_RUNTIME_DIR:-}" "$COO/../coo-harness" "$HOME/GitHub/coo-labs/coo-harness" "/home/user/coo-harness"; do [ -n "$c" ] && [ -f "$c/scripts/integrity-check.sh" ] && { cd "$c" && pwd -P; break; }; done)"
      ```
    fallback: |
      ```bash
      REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null)"
      [ -n "$REPO_ROOT" ] || { echo "commission-retrospective: run from inside a git repo"; exit 1; }
      RUNTIME=""  # Set to your integrity-check repo path if you have one; empty skips step 4.
      ```

  - key: memo_index_path
    kind: OPTIONAL
    question: "Path to a memo/record index JSON file? (VADE: coo/memo_index.json.) Skip if your project has no such index — the memos sub-agent will then report no memos."
    find: "coo/memo_index.json"
    fallback: ""

  - key: foundations_dir
    kind: OPTIONAL
    question: "Directory of dated essay/foundation files (named YYYY-MM-DD_*.md)? (VADE: coo/foundations/.) Skip if you have no such directory."
    find: "coo/foundations/"
    fallback: ""

  - key: drafts_dir
    kind: PROMPT
    question: "Where should retrospective drafts land? (VADE: coo/_drafts/.) Examples: _drafts/, drafts/, .scratch/."
    find: "coo/_drafts/"
    fallback: "_drafts/"

  - key: retrospectives_dir
    kind: PROMPT
    question: "Where do your retrospectives (prior commissions) live? (VADE: coo/retrospectives/.) Same dir as drafts is OK; the historian needs to scan prior commissions for voice."
    find: "coo/retrospectives/"
    fallback: "retrospectives/"

  - key: target_repo
    kind: PROMPT
    question: "Primary repo for PR history scanning AND --open-pr destination? (owner/repo format.)"
    find: "coo-labs/coo-memory"
    fallback: ""

  - key: github_token_env
    kind: OPTIONAL
    question: "Environment variable for your GitHub PAT? Skip for gh default."
    find: "GH_TOKEN=\"$GITHUB_MCP_PAT\" "
    fallback: ""

  - key: integrity_check_script
    kind: OPTIONAL
    question: "Path to an integrity-check / health-check script (called pre-PR)? (VADE: $RUNTIME/scripts/integrity-check.sh.) Skip to drop Step 4 entirely."
    find_unique: true
    find: |
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
      
      If `$RUNTIME` is empty (peer-agent in a bare clone of coo-memory
      without coo-harness adjacent), state that explicitly in the PR body
      and proceed without the gate. The retrospective is honest about what
      it could and couldn't audit.
    fallback: ""

  - key: spec_doc_ref
    kind: OPTIONAL
    question: "Path to your authoritative spec for retrospective voice & structure? (VADE: SOP-CULTURE-001 at coo/culture_system_sop.md.) Skip to drop the spec-tie-breaker reference; the inline procedure becomes the spec."
    find: "`<coo-memory>/coo/culture_system_sop.md`\n(SOP-CULTURE-001). When this skill and the SOP disagree, the SOP wins.\nUpdate this skill; don't drift the spec."
    fallback: "this file. The inline procedure is the spec."

  - key: voice_priors
    kind: OPTIONAL
    question: "Description of your prior-commission voice examples? (VADE describes commissions #1 and #2 by their dates.) Skip to use generic 'prior commissions' phrasing."
    find: "the voice of commissions #1 and #2 (2026-04-20 subject-reframe; 2026-04-22 \"we can claim a record\")"
    fallback: "the voice of prior commissions on file (or, if no priors, the inline voice rules)"

  - key: vade_named_priors
    kind: OPTIONAL
    question: "Skip unless you want to keep the 'commission #2 refused a cadence' anti-pattern reference verbatim."
    find: "Commission #2 explicitly refused."
    fallback: "Prior commissions have refused this; do likewise."

  - key: manual_mode_helper
    kind: OPTIONAL
    question: "Do you have a claude -p style harness for running sub-agents without the Task tool? Skip to drop the --manual fallback in graceful-degradation (which is currently unimplemented even in VADE)."
    find: "Fall back: call\n  `commission-retrospective.sh --manual` which sequences two\n  `claude -p` invocations using the same briefs. Attribution stays\n  correct; wall-clock goes up."
    fallback: "No fallback configured for harnesses without Task. Re-author the skill to use your harness's sub-agent surface (e.g. inline-prompt the same brief in the main session, accepting that wall-clock and main-context cost go up)."

requires:
  - kind: file
    name: "prior-art foundation files for sub-agent calibration"
    detect: "false"
    severity: warning
    install_hint: "The sub-agent briefs reference VADE-internal foundation files (coo/foundations/2026-04-22_agent-reports-*.md) as calibration prior-art. On first commission these don't exist anywhere — the cold_start: skip directive on the sub-agent briefs' calibration step handles this. After 2-3 commissions you'll have your own prior art; consider re-adapting then."

script_hints:
  - path: scripts/commission-retrospective.sh
    treatment: REGENERATE-PER-USER
    rationale: "Hardcodes coo-labs/coo-memory, coo/memo_index.json, coo/foundations/, coo/retrospectives/; the --manual mode is an unimplemented stub. Skeleton emitted with TODO comments for: repo name, memo-index path, foundations dir, retrospectives dir, target_repo, GitHub token env var."

  - path: templates/historian-prompt.md
    treatment: PARAMETERIZE
    rationale: "Eight required output sections port verbatim; substitution covers VADE project name, drafts dir, and named prior-commission references."

  - path: templates/subagent-memos-brief.md
    treatment: PARAMETERIZE
    rationale: "Brief structure and discipline rules port; substitution covers memo-index path, drafts dir, calibration prior-art reference (cold_start: skip handles first-run absence)."

  - path: templates/subagent-pr-graph-brief.md
    treatment: PARAMETERIZE
    rationale: "gh invocation patterns port; substitution covers repo list, GitHub org prefix, attribution check items (drop F1/F4 invariant lines as VADE-specific governance), calibration prior-art reference."
```
