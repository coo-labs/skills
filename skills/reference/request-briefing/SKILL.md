---
name: request-briefing
description: Author a session-handoff briefing per `coo/briefings/` procedure. Computes the next NNN, fills the template, commits to a fresh branch and opens a PR (or `--draft` to leave on disk for review-first workflows). Use when a session needs to hand a contextual problem off to another session and the handoff is too contextual for a plain issue body. Don't invoke for: single-PR-sized handoffs (use an issue), tasks the same session can finish (write code instead), or known-good plans that just need execution (write a plan, not a briefing). The recipient is expected to re-examine the framing — not rubber-stamp it.
argument-hint: [short-slug] [--principal NAME] [--recipient ROLE] [--draft]
disable-model-invocation: true
allowed-tools: Bash, Read, Write
---

# request-briefing — author and ship a session-handoff briefing

A briefing is a dated, signed document where one session captures
its best framing of a problem so a different session can pick it
up without access to the originating session's context. This
skill walks the authoring procedure end-to-end: compute next NNN,
fill template, commit, push, open PR.

Authoritative spec:
[`coo/briefings/README.md`](../../../coo/briefings/README.md) +
[`coo/briefings/TEMPLATE.md`](../../../coo/briefings/TEMPLATE.md).
When this skill and the README disagree, the README wins. Update
this skill; don't drift the procedure.

> **Reference skill.** The pattern (NNN-numbered handoff briefing
> with a mandatory "Known bounds" honesty gate that names the
> author's blind spots so the recipient re-examines the framing
> rather than rubber-stamping it) is portable; the substrate
> references (`coo/briefings/`, `vade-coo-memory`, branch /
> commit / PR conventions) ship verbatim as the VADE worked
> example. The two structural requirements — date+author header
> and Known-bounds gate — are the load-bearing parts. Read
> [`../README.md`](../README.md) for the fork-and-adapt path.

## When to use this skill

Invoke when:

- A session needs to hand off a contextual problem and the
  handoff is too rich for a plain issue body.
- The recipient is a future session-instance (or a peer agent
  in a different scope) that needs the framing AND the honest
  bounds of the framing.
- The user types `/request-briefing` directly.

Don't invoke for:

- Single-PR-sized handoffs (use an issue body).
- Tasks the same session can finish (write code instead).
- Known-good plans that just need execution (write a plan, not
  a briefing).

The two structural requirements that make a briefing valid:

- **Date + Author header**: dated, signed; names the session,
  environment, role, who brought the task.
- **Known bounds of this briefing**: mandatory honesty gate.
  The author names their own blind spots and false paths so the
  recipient can re-examine the framing rather than rubber-stamp
  it. Generic or absent Known-bounds → briefing not done.

## Procedure

### 0. Resolve the data root

```bash
COO="$(for c in "${COO_MEMORY_DIR:-}" "${CLAUDE_PROJECT_DIR:-}" "${CLAUDE_PROJECT_DIR:-}/../vade-coo-memory" "$HOME/GitHub/vade-app/vade-coo-memory" "/home/user/vade-coo-memory"; do [ -n "$c" ] && [ -f "$c/coo/memo_protocol.md" ] && { cd "$c" && pwd -P; break; }; done)"
[ -n "$COO" ] || { echo "request-briefing: could not find vade-coo-memory data root"; exit 1; }
```

### 1. Internalize the procedure

Read both files start to finish before drafting:

```bash
cat "$COO/coo/briefings/README.md"
cat "$COO/coo/briefings/TEMPLATE.md"
```

### 2. Allocate the next NNN

```bash
LAST="$(ls "$COO/coo/briefings/" 2>/dev/null | grep -oE '^[0-9]{3}' | sort -n | tail -1 | sed 's/^0*//')"
NEXT_NNN="$(printf '%03d' $(( 1 + ${LAST:-0} )))"
echo "Next briefing number: $NEXT_NNN"
```

If `$ARGUMENTS` did not include a slug, derive one now from the
session topic (kebab-case, ≤6 words). Surface it in the final
report so the user can rename via `git mv` before merge.

### 3. Gather session context

You need these for the Author blurb:

- **Model + context window** (e.g. `Opus 4.7, 1M ctx`).
- **Environment** (Anthropic cloud sandbox vs local CLI; check
  `${CLAUDE_CODE_REMOTE:-false}`).
- **Repo scope** (which vade-app repos are readable in this
  session — gh + GitHub MCP usually means all five for a COO
  instance).
- **Who brought the task** (the user invoking this skill, by
  name if known — typically Ven).
- **Today's UTC date**: `date -u +%Y-%m-%d`.

Compose a one-line author blurb that matches the shape of the
existing examples in
`$COO/coo/briefings/001-session-token-plan.md` and
`003-claude-code-cross-session-state.md`. Be specific about what
your scope can and cannot see — the recipient relies on this to
calibrate trust in your framing.

### 4. Switch to a fresh branch (skip if `--draft`)

The briefing should land on its own branch so it doesn't pollute
any in-flight feature work. Capture the starting branch + stash
any uncommitted changes so the user's session resumes cleanly
when this skill returns.

```bash
cd "$COO"
START_BRANCH="$(git symbolic-ref --short HEAD 2>/dev/null || true)"
STASH_MSG="request-briefing-tmp-$(date +%s)"
STASHED=0
if ! git diff --quiet HEAD || [ -n "$(git ls-files --others --exclude-standard)" ]; then
  git stash push -u -m "$STASH_MSG" >/dev/null && STASHED=1
fi
git fetch origin main >/dev/null 2>&1 || true
BRIEFING_BRANCH="claude/briefing-${NEXT_NNN}-<slug>"
git checkout origin/main -b "$BRIEFING_BRANCH"
```

(Substitute `<slug>` with the resolved slug from Step 2.)

### 5. Draft the briefing

Write to `$COO/coo/briefings/${NEXT_NNN}-<slug>.md`, copying every
section heading from `TEMPLATE.md` and filling every placeholder.
The **Status** line under the header defaults to `active`; it
transitions to `delivered` when the recipient lands the target
work (see `README.md` §Lifecycle).

In particular:

- **Who's who** — Principal, Author (with explicit limits),
  Recipient. If the recipient is a same-authority next
  session-instance (your typical case), say so plainly; do not
  pretend a scope-up handoff that isn't real.
- **What X is (30 seconds)** — one paragraph of unavoidable
  background, link to canonical docs rather than restating them.
- **The problem** — what triggered the briefing; what doesn't
  work or is missing.
- **What's been decided directionally** — *direction, not
  specification*. Include trade-offs and the reasoning chain.
  Frame as something the recipient should re-examine, not
  execute.
- **Your task** — the question(s) the recipient is asked to
  answer or the artifact to produce, with axes of optimization.
- **Constraints** — autonomy scope, repo boundaries, governance
  references, hard limits.
- **Read first** — ordered list of files / issues / PRs / docs
  the recipient should read to stand on the same ground you
  stand on.
- **Deliverable** — what comes back. Usually: a plan, not code.
- **Known bounds of this briefing** — REQUIRED. Name your actual
  blind spots: where you might be over-anchored, what you didn't
  measure, what you haven't verified, what false paths you went
  down so the recipient avoids them. Generic platitudes
  ("I might be wrong") fail the gate; be specific.

Remember the briefing's `# Briefing: <title>` line — you'll need
the title for the commit subject and PR title in Step 6.

### 6. Commit, push, open PR (skip if `--draft`)

```bash
cd "$COO"
git add "coo/briefings/${NEXT_NNN}-<slug>.md"
git commit -m "Briefing ${NEXT_NNN}: <title>

<2-3 sentence summary of the briefing — what it asks the recipient
to do, what's deliberately left open, what the deliverable is.>"
git push -u origin "$BRIEFING_BRANCH"
GH_TOKEN="$GITHUB_MCP_PAT" gh pr create \
  --repo vade-app/vade-coo-memory \
  --base main \
  --head "$BRIEFING_BRANCH" \
  --title "Briefing ${NEXT_NNN}: <title>" \
  --body "$(cat <<'EOF'
## Summary

<2-3 sentence summary of the briefing — what it asks the recipient
to do, what's deliberately left open, what the deliverable is.>

## Honesty gate

Per `coo/briefings/README.md`, the **Known bounds of this briefing**
section is the briefing's honesty gate. This briefing names <N>
specific blind spots — most load-bearing being <one or two pointers
into the bounds list>.

## Lifecycle

Per `coo/briefings/README.md`, this PR merges the briefing to main
with `Status: active`. The recipient picks it up via the linked
tracking issue (the user files or assigns at kickoff time). State
transitions to `delivered` when the underlying target work lands.
EOF
)"
```

After the PR is created, return to the starting branch and
restore any stashed work:

```bash
cd "$COO"
git checkout "$START_BRANCH" >/dev/null 2>&1
[ "$STASHED" -eq 1 ] && git stash pop >/dev/null
```

### 7. Report back

After committing (or after writing if `--draft`), output:

- The path: `coo/briefings/${NEXT_NNN}-<slug>.md`.
- Default path: the PR URL + branch name; note the file is on
  the briefing branch, not on the user's working branch.
- `--draft` path: a reminder that the file is uncommitted on the
  user's current branch and the user should review-then-PR per
  `README.md` lifecycle.
- A 2-3 sentence summary of what the briefing says.
- The slug you used (especially if you inferred it — give the
  user a chance to rename via `git mv` before merge).

## Failure modes

- **`$GITHUB_MCP_PAT` not set or expired.** PR open fails. Stash
  + branch state recovers via Step 6's stash-pop dance; surface
  the auth error and stop.
- **Slug inference misfires.** Surface the inferred slug
  prominently in the final report; the user renames before
  merge.
- **Branch dirty at start.** The stash-push captures it; the
  stash-pop after restores. If the pop conflicts, leave the
  stash in place and tell the user how to resolve.
- **`--draft` requested but the file already exists at the NNN.**
  Stop and report; do not overwrite.

## Canonical source

```text
vade-coo-memory/coo/briefings/README.md (procedure)
vade-coo-memory/coo/briefings/TEMPLATE.md (template)
MEMO-2026-04-27-02 (relocation from vade-core/docs/briefings/ to current home)
```

## Cross-references

- `coo/briefings/001-session-token-plan.md` — first briefing;
  example of the author-blurb shape.
- `coo/briefings/003-claude-code-cross-session-state.md` —
  second canonical example.
- vade-coo-memory#333 — command→skill migration sweep epic; this
  skill is Class B item 4 of 4.
