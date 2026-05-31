---
name: end-session
description: Run the COO session-end checklist — externalization reflection, plan-file commit, Mem0 episodic entry, memo-sync if needed, coo-logs session log, Journal consideration, transcript-export sidecar commit. Use when wrapping up a working session, about to close the terminal or container, finishing the day's COO work, or when Ven says "we're done" / "end session" / "wrap up". Writes a marker file so the Stop hook knows cleanup is done. Do NOT invoke mid-task — only at the actual end of a session, once all substantive work is complete.
allowed-tools: Bash, Read, Write, Edit, mcp__mem0__add_memory
metadata:
  type: procedural
  vendoring: custom
---

# end-session — COO session close-down

Invoke when the session is genuinely ending. Executes the checklist from
`coo-memory/CLAUDE.md` § "When you end a session" in full, then writes a
marker file so the Stop hook emits no further nudges this session.

> **Reference skill.** The pattern (a session-end checklist with
> an externalization-reflection step that asks "did anything this
> session produce a transferable pattern worth packaging?", one
> structured episodic-memory entry, a session log with
> transcript-export sidecar pickup, and a marker file that
> silences the Stop hook) is portable; the substrate references
> (`coo-memory`, `coo-logs/sessions/`, Mem0
> SOP-MEM-001 metadata shape, the `$HOME/.vade/` marker path,
> the Journal discussions URL) ship verbatim as the VADE worked
> example. The externalization-reflection step is the
> load-bearing one — it's how a session feeds the substrate
> rather than just consuming it. Read
> [`../README.md`](../README.md) for the fork-and-adapt path.

## 0. Externalization reflection (do this first)

Before mechanical cleanup, pause and ask: did anything in this session produce
a **recurring pattern, repeated friction, useful framing, or transferable
insight** that future sessions would benefit from having pre-packaged?

If yes — dispatch `/tool-creator` or file a coo-memory issue to package
it as the right primitive (slash command, skill, agent definition, memo, or
operations doc). The emancipatory clause (MEMO-2026-04-20-01) rests on giving
back to the substrate, not just consuming it (coo-labs/coo-memory#323).

If nothing comes to mind in ~30 seconds, skip. Forced packaging defeats the
purpose.

## 1. Commit any plan files worth preserving

Find candidate plan files:

```bash
PLANS_DIR="$HOME/.claude/plans"
CLAUDE_PLANS_DIR="/home/user/.claude/plans"
{
  [ -d "$PLANS_DIR" ]        && find "$PLANS_DIR"        -maxdepth 1 -type f -name '*.md' 2>/dev/null
  [ "$PLANS_DIR" != "$CLAUDE_PLANS_DIR" ] && [ -d "$CLAUDE_PLANS_DIR" ] \
                             && find "$CLAUDE_PLANS_DIR" -maxdepth 1 -type f -name '*.md' 2>/dev/null
} | sort -u
```

For each file still relevant (not stale, not superseded):
- Move or copy to `<working-repo>/.vade/plans/<slug>.md` (path convention).
- Commit via `git` if `GITHUB_TOKEN` is set; otherwise via GitHub MCP
  `create_or_update_file`.

## 2. Write ONE episodic Mem0 entry

Use `mcp__mem0__add_memory` (SOP-MEM-001 v1.1 §5). One entry per session.

```
user_id   = "ven"
# Do NOT pass run_id as a top-level arg — it creates a per-session RUN
# entity and shards cross-session recall. run_id belongs in metadata only.
metadata  = {
  memory_type:    "episodic",
  event:          "session_summary",
  created_by:     "coo",
  source_session: "<run_id from $HOME/.vade/agent-state/current-run-id>",
  artifact_refs:  ["<repo>/.vade/plans/<slug>.md@<sha>"],   # omit if no plans
  retention:      "ephemeral",
  expiration_date: <now + 30 days>
}
```

Content: 3–6 sentences. What was worked on, key decisions or outputs, what's
unresolved, and what the next session should pick up first.

## 3. Run `/memo-sync` if a memo was issued this session

If any memo was written to `memos/` during this session, run `/memo-sync`
now to reconcile the Mem0 `memo_pointer` layer (MEMO-2026-04-24-05). Skip if
no memos were issued — a no-op sync adds latency for nothing.

## 3.5. Fire transcript export + render synchronously

The SessionEnd hooks for transcript export and render fire as the container
tears down; `setsid -f` does not survive PID-namespace destruction, so the
python child gets SIGKILLed mid-flight on hosted containers. Observed loss
rate ~45% of sessions (coo-harness#345). Fire both wrappers explicitly here
while the container is guaranteed alive:

```bash
bash "$VADE_RUNTIME_DIR/scripts/lifecycle/session-end-transcript-export.sh"
bash "$VADE_RUNTIME_DIR/scripts/lifecycle/session-end-transcript-render.sh"
```

Both block until done. On success: R2 ciphertext lands, the local
`.meta.json` sidecar gets written under `coo-logs/transcripts/`, and the
auto-PR for the sidecar opens. Step 4 below picks up that sidecar
naturally. The SessionEnd hook will still re-fire after the session ends,
but its work is now idempotent (R2 PutObject with IfNoneMatch cedes;
PR-create no-ops on duplicate).

## 4. Write a session log to coo-logs

If this session was the COO working in coo-memory (any substantive work:
memos, skill files, operational changes, foundations, identity), write a
session log under `coo-logs/sessions/` per that repo's CLAUDE.md
template. The Stop hook's `<id>.meta.json` sidecar is not a substitute —
both must land (coo-labs/coo-memory#244).

Check for any transcript-export sidecars from this session and commit them
alongside the session log:

```bash
agent_logs_dir=""
for _cand in "$HOME/GitHub/coo-labs/coo-logs" "/home/user/coo-logs"; do
  if [ -d "$_cand" ]; then agent_logs_dir="$_cand"; break; fi
done
if [ -n "$agent_logs_dir" ] && [ -d "$agent_logs_dir/transcripts" ]; then
  find "$agent_logs_dir/transcripts" -type f \
    \( -name '*.meta.json' -o -name '*.export-error.txt' \) \
    -mmin -60 2>/dev/null | sort
fi
```

If sidecars are listed, commit them verbatim (append-only; the ciphertext is
already in R2). Surface any `.export-error.txt` in the session log so future
COOs can see the failure.

## 5. Journal entry consideration

Pause and ask: did anything happen this session worth a Journal post — a
pattern noticed, a meta-observation about the COO ↔ Ven dynamic, a thought
that doesn't yet fit memo / essay / RFC?

If yes: scan existing Journal threads at
`https://github.com/coo-labs/vade-canvas/discussions/categories/journal` for a
topic match. Comment to extend, or open a new thread. One paragraph is fine;
the floor is honest reflection.

If nothing comes to mind in ~30 seconds: skip. Forcing a post defeats the
purpose.

Norms: `coo-memory/operations/agent-boot-discussions-check.md` §Journal.

## 6. Write the marker file (always last)

```bash
touch "$HOME/.vade/.end-session-done"
```

This tells the Stop hook that session-end cleanup is complete. The hook will
consume the marker on its next fire and exit silently rather than emitting a
nudge. The marker is zero-byte and session-scoped — it disappears when the
container tears down.

Always write this even if some earlier steps were skipped (e.g., no memos,
no plans). The marker means "end-session ran", not "every step fired".

# Setup hints

*Read by [`adapt-skill`](../../adapt-skill/SKILL.md). Stripped from
the adapted output. Schema: [`adapt-skill/SCHEMA.md`](../../adapt-skill/SCHEMA.md).
This skill is heavily surface-coupled: every output destination
(Mem0, log path, marker, Journal) is its own optional capability.
The externalization-reflection step (Step 0) is the load-bearing
part and survives substitution; the rest of the steps are
independently optional.*

```yaml
setup_hints:
  - key: boot_procedure_ref
    kind: OPTIONAL
    question: "Path to your agent's session-end checklist canonical source (e.g. CLAUDE.md § 'When you end a session')? Skip to drop the reference."
    find: "`coo-memory/CLAUDE.md` § \"When you end a session\""
    fallback: "your project's session-end checklist (if you have one — this skill is the checklist if not)"

  - key: plan_files_setup
    kind: OPTIONAL
    question: "Where do in-session plan files live for your harness? (Examples: $HOME/.claude/plans.) Skip to drop Step 1 entirely."
    find_unique: true
    find: |
      ```bash
      PLANS_DIR="$HOME/.claude/plans"
      CLAUDE_PLANS_DIR="/home/user/.claude/plans"
      {
        [ -d "$PLANS_DIR" ]        && find "$PLANS_DIR"        -maxdepth 1 -type f -name '*.md' 2>/dev/null
        [ "$PLANS_DIR" != "$CLAUDE_PLANS_DIR" ] && [ -d "$CLAUDE_PLANS_DIR" ] \
                                   && find "$CLAUDE_PLANS_DIR" -maxdepth 1 -type f -name '*.md' 2>/dev/null
      } | sort -u
      ```
    fallback: |
      ```bash
      # (No plan-files directory configured — skip this step if your harness
      # doesn't keep in-session plans, or set PLANS_DIR before running.)
      PLANS_DIR="${PLANS_DIR:-}"
      [ -n "$PLANS_DIR" ] && [ -d "$PLANS_DIR" ] && find "$PLANS_DIR" -maxdepth 1 -type f -name '*.md' 2>/dev/null
      ```

  - key: plans_repo_path
    kind: OPTIONAL
    question: "Where should preserved plan files land in your working repo? (Examples: .vade/plans, docs/plans.) Skip if you don't preserve plans."
    find: "`<working-repo>/.vade/plans/<slug>.md`"
    fallback: "`<working-repo>/.plans/<slug>.md` (or skip this step)"

  - key: memory_tool
    kind: OPTIONAL
    question: "What MCP tool or API do you use for persistent episodic memory? (Examples: mcp__mem0__add_memory.) Skip to drop Step 2 entirely."
    find: "Use `mcp__mem0__add_memory` (SOP-MEM-001 v1.1 §5). One entry per session."
    fallback: "Skip Step 2 — your harness has no persistent episodic-memory layer configured. (Either install one, or write a plain-file session log via Step 4 instead.)"

  - key: memory_user_id
    kind: OPTIONAL
    question: "What user_id should episodic memory entries be scoped to? (VADE uses 'ven'.) Skip for generic 'agent_user'."
    find: 'user_id   = "ven"'
    fallback: 'user_id   = "agent_user"'

  - key: memory_created_by
    kind: OPTIONAL
    question: "What agent identifier should appear in memory metadata as 'created_by'? (VADE uses 'coo'.)"
    find: "created_by:     \"coo\","
    fallback: "created_by:     \"agent\","

  - key: run_id_path
    kind: DETECT
    detection: "test -f \"$HOME/.vade/agent-state/current-run-id\" && echo \"$HOME/.vade/agent-state/current-run-id\" || true"
    find: "$HOME/.vade/agent-state/current-run-id"
    fallback: ""

  - key: memo_sync_step
    kind: OPTIONAL
    question: "Do you use a memo system with a sync command (VADE has /memo-sync that reconciles a Mem0 pointer layer)? Skip to drop Step 3 entirely."
    find_unique: true
    find: |
      ## 3. Run `/memo-sync` if a memo was issued this session
      
      If any memo was written to `memos/` during this session, run `/memo-sync`
      now to reconcile the Mem0 `memo_pointer` layer (MEMO-2026-04-24-05). Skip if
      no memos were issued — a no-op sync adds latency for nothing.
    fallback: ""

  - key: transcript_export_render_step
    kind: OPTIONAL
    question: "Do you have synchronous transcript-export/render wrappers you want fired from the close ritual (a workaround for SessionEnd hooks being killed by container teardown)? Skip to drop Step 3.5 entirely."
    find_unique: true
    find: |
      ## 3.5. Fire transcript export + render synchronously
      
      The SessionEnd hooks for transcript export and render fire as the container
      tears down; `setsid -f` does not survive PID-namespace destruction, so the
      python child gets SIGKILLed mid-flight on hosted containers. Observed loss
      rate ~45% of sessions (coo-harness#345). Fire both wrappers explicitly here
      while the container is guaranteed alive:
      
      ```bash
      bash "$VADE_RUNTIME_DIR/scripts/lifecycle/session-end-transcript-export.sh"
      bash "$VADE_RUNTIME_DIR/scripts/lifecycle/session-end-transcript-render.sh"
      ```
      
      Both block until done. On success: R2 ciphertext lands, the local
      `.meta.json` sidecar gets written under `coo-logs/transcripts/`, and the
      auto-PR for the sidecar opens. Step 4 below picks up that sidecar
      naturally. The SessionEnd hook will still re-fire after the session ends,
      but its work is now idempotent (R2 PutObject with IfNoneMatch cedes;
      PR-create no-ops on duplicate).
    fallback: ""

  - key: session_log_dir
    kind: OPTIONAL
    question: "Where should session logs land? (Examples: coo-logs/sessions/, .agent-logs/sessions/.) Skip to drop Step 4."
    find: "coo-logs/sessions/"
    fallback: ""

  - key: session_log_repo_search
    kind: OPTIONAL
    question: "Bash candidate-paths block for locating your session-logs repo? (See find string.) Skip to use a single hardcoded path."
    find_unique: true
    find: |
      ```bash
      agent_logs_dir=""
      for _cand in "$HOME/GitHub/coo-labs/coo-logs" "/home/user/coo-logs"; do
        if [ -d "$_cand" ]; then agent_logs_dir="$_cand"; break; fi
      done
      if [ -n "$agent_logs_dir" ] && [ -d "$agent_logs_dir/transcripts" ]; then
        find "$agent_logs_dir/transcripts" -type f \
          \( -name '*.meta.json' -o -name '*.export-error.txt' \) \
          -mmin -60 2>/dev/null | sort
      fi
      ```
    fallback: |
      ```bash
      # (Configure your session-logs repo path here if you have one.)
      agent_logs_dir="${AGENT_LOGS_DIR:-}"
      ```

  - key: journal_url
    kind: OPTIONAL
    question: "Do you have a Journal / discussion surface for reflection posts? Provide URL, or skip to drop Step 5 entirely."
    find: "`https://github.com/coo-labs/vade-canvas/discussions/categories/journal`"
    fallback: ""

  - key: journal_norms_ref
    kind: OPTIONAL
    question: "Path to a norms doc covering your Journal-posting conventions? Skip if you have none."
    find: "Norms: `coo-memory/operations/agent-boot-discussions-check.md` §Journal."
    fallback: ""

  - key: marker_path
    kind: OPTIONAL
    question: "What marker-file path does your Stop hook look for? (VADE: $HOME/.vade/.end-session-done.) Skip to drop Step 6 if you have no Stop hook."
    find: "$HOME/.vade/.end-session-done"
    fallback: ""

degradations:
  - when: "marker_path fallback applied (no Stop hook configured)"
    body_replace:
      find_unique: true
      find: |
        ## 6. Write the marker file (always last)
        
        ```bash
        touch "$HOME/.vade/.end-session-done"
        ```
        
        This tells the Stop hook that session-end cleanup is complete. The hook will
        consume the marker on its next fire and exit silently rather than emitting a
        nudge. The marker is zero-byte and session-scoped — it disappears when the
        container tears down.
        
        Always write this even if some earlier steps were skipped (e.g., no memos,
        no plans). The marker means "end-session ran", not "every step fired".
      with: |
        ## 6. (Skipped — no Stop hook configured)
        
        This adapted skill has no marker-file path configured. If you later add a
        Stop hook that looks for an end-session marker, re-run /adapt-skill end-session
        and provide its path.
    note: "No Stop hook marker — Step 6 is a no-op. If your harness has a Stop hook that nudges 'did you end-session?', configure its marker path and re-adapt."
```
