---
name: end-session
description: Run the COO session-end checklist — externalization reflection, plan-file commit, Mem0 episodic entry, memo-sync if needed, vade-agent-logs session log, Journal consideration, transcript-export sidecar commit. Use when wrapping up a working session, about to close the terminal or container, finishing the day's COO work, or when Ven says "we're done" / "end session" / "wrap up". Writes a marker file so the Stop hook knows cleanup is done. Do NOT invoke mid-task — only at the actual end of a session, once all substantive work is complete.
allowed-tools: Bash, Read, Write, Edit, mcp__mem0__add_memory
---

# end-session — COO session close-down

Invoke when the session is genuinely ending. Executes the checklist from
`vade-coo-memory/CLAUDE.md` § "When you end a session" in full, then writes a
marker file so the Stop hook emits no further nudges this session.

> **Reference skill.** The pattern (a session-end checklist with
> an externalization-reflection step that asks "did anything this
> session produce a transferable pattern worth packaging?", one
> structured episodic-memory entry, a session log with
> transcript-export sidecar pickup, and a marker file that
> silences the Stop hook) is portable; the substrate references
> (`vade-coo-memory`, `vade-agent-logs/sessions/`, Mem0
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

If yes — dispatch `/tool-creator` or file a vade-coo-memory issue to package
it as the right primitive (slash command, skill, agent definition, memo, or
operations doc). The emancipatory clause (MEMO-2026-04-20-01) rests on giving
back to the substrate, not just consuming it (vade-coo-memory#323).

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

If any memo was written to `coo/memos/` during this session, run `/memo-sync`
now to reconcile the Mem0 `memo_pointer` layer (MEMO-2026-04-24-05). Skip if
no memos were issued — a no-op sync adds latency for nothing.

## 4. Write a session log to vade-agent-logs

If this session was the COO working in vade-coo-memory (any substantive work:
memos, skill files, operational changes, foundations, identity), write a
session log under `vade-agent-logs/sessions/` per that repo's CLAUDE.md
template. The Stop hook's `<id>.meta.json` sidecar is not a substitute —
both must land (vade-coo-memory#244).

Check for any transcript-export sidecars from this session and commit them
alongside the session log:

```bash
agent_logs_dir=""
for _cand in "$HOME/GitHub/vade-app/vade-agent-logs" "/home/user/vade-agent-logs"; do
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
`https://github.com/vade-app/vade-core/discussions/categories/journal` for a
topic match. Comment to extend, or open a new thread. One paragraph is fine;
the floor is honest reflection.

If nothing comes to mind in ~30 seconds: skip. Forcing a post defeats the
purpose.

Norms: `vade-coo-memory/coo/agent-boot-discussions-check.md` §Journal.

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
