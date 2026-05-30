---
name: briefing
description: "Manage session-handoff briefings under `briefings/`. Subcommands: `request` (file a new briefing — collision-safe NNN allocation, YAML frontmatter, fresh branch + PR), `pickup` (claim an open briefing for this session), `done` (mark a claimed briefing delivered), `release` (clear a claim without delivering). The briefing schema, index format, and per-subcommand procedures for pickup/done/release live in reference.md — loaded on demand. Use when a session needs to hand a contextual problem to another session, or when this session is about to pick one up. Don't invoke for: single-PR-sized handoffs (use an issue), tasks the same session can finish (write code instead), or known-good plans that just need execution (write a plan, not a briefing)."
argument-hint: "<request|pickup|done|release> [args]"
disable-model-invocation: true
allowed-tools: Bash, Read, Write
metadata:
  type: procedural
  vendoring: custom
---

# briefing — manage session-handoff briefings

## What a briefing is

A briefing is a dated, signed document where one session captures its best
framing of a problem so a different session can pick it up without access to
the originating session's context. It is orientation, not specification — the
recipient is expected to **re-examine** the framing, not rubber-stamp it.

Briefings live under `briefings/<NNN>-<slug>.md`. The COO is the typical
recipient (broadest scope across `coo-labs/*`); the typical author is a
session-scoped agent that hit the edge of what its own scope can decide.

## Briefing vs memo vs issue

Three handoff forms exist in the substrate; they are not interchangeable.

- **Memo** — when the artifact is a *binding decision* future sessions read as
  case-law. Memos crystallize conclusions in the present tense.
- **Issue** — when the artifact is a *well-scoped task*. The next session
  needs the target, not the framing.
- **Briefing** — when the *framing itself* is the work product. The author has
  accumulated context and judgment that doesn't fit in an issue body and
  isn't yet a binding decision; the recipient needs the framing-not-just-the-
  target to act well.

Heuristic: if collapsing the handoff into a one-paragraph issue body would
lose real signal — why the problem is shaped the way it is, what false paths
are already known, what the author *can't see* — write a briefing.

## The honesty gate

A briefing reflects the author's best framing within their session-scope, no
more. To make that explicit, every briefing carries a mandatory **Known
bounds of this briefing** section where the author names their actual blind
spots: where they may be over-anchored, what they didn't measure, what false
paths they went down so the recipient avoids them. Generic platitudes ("I
might be wrong") fail the gate.

## Subcommands

- `/briefing request` (or `/briefing` with no arg) — author a new briefing.
- `/briefing pickup` — list open briefings; choose one to claim for this session.
- `/briefing done <NNN>` — the target work for briefing NNN has landed.
- `/briefing release <NNN>` — abandon a claim without marking delivered.

Don't invoke for: single-PR handoffs (use an issue), tasks this session can
finish (write code), or known-good plans that just need execution.

## Dispatch

Resolve the data root and pull the subcommand off `$ARGUMENTS`:

```bash
COO="$(for c in "${COO_MEMORY_DIR:-}" "${CLAUDE_PROJECT_DIR:-}" "/home/user/coo-memory"; do
  [ -n "$c" ] && [ -f "$c/operations/memo_protocol.md" ] && { cd "$c" && pwd -P; break; }; done)"
[ -n "$COO" ] || { echo "briefing: could not find coo-memory data root"; exit 1; }
SUB="${ARGUMENTS%% *}"
REST="${ARGUMENTS#"$SUB"}"; REST="${REST# }"
```

Then route:

- **`request` or empty `$SUB`** → follow the procedure inline below (most-common path; kept in SKILL.md so it loads with the skill).
- **`pickup`, `done`, `release`** → Read [`reference.md`](reference.md) (colocated) and follow the matching section. The detailed procedures live there because they only run when their subcommand fires.
- **anything else** → print `Usage: /briefing <request|pickup|done|release> [args]` and stop.

## /briefing request — author and ship

The two structural requirements that make a briefing valid:

- **YAML frontmatter** (date, author, status, claim fields) — dated, signed,
  machine-readable. Field-by-field semantics in `reference.md`.
- **Known bounds of this briefing** — mandatory honesty gate. The author names
  their own blind spots and false paths so the recipient can re-examine the
  framing rather than rubber-stamp it. Generic or absent Known-bounds →
  briefing not done.

### 1. Read the template

```bash
cat "${CLAUDE_SKILL_DIR:-.claude/skills/briefing}/template.md"
```

That's the body shape and the frontmatter you need to fill.

### 2. Allocate the next NNN (collision-safe)

Fold open briefing PRs into the max so a PR claiming NNN that hasn't merged
yet doesn't collide (resolves [#1092](https://github.com/coo-labs/coo-memory/issues/1092)):

```bash
FS_MAX="$(ls "$COO/briefings/" 2>/dev/null | grep -oE '^[0-9]{3}' | sort -n | tail -1 | sed 's/^0*//')"
PR_MAX="$(gh pr list --repo coo-labs/coo-memory --state open \
  --json title,headRefName --jq '
    [.[] | (.title, .headRefName) |
     capture("(?:[Bb]riefing[ -])(?P<n>[0-9]{3})")? | .n | tonumber] | max // 0' 2>/dev/null || echo 0)"
NEXT_NNN="$(printf '%03d' $(( 1 + ( FS_MAX > PR_MAX ? FS_MAX : PR_MAX ) )))"
echo "Next briefing number: $NEXT_NNN"
```

A TOCTOU race remains (two concurrent authors both query and both pick the
same NNN); the collision-tolerance rule under Failure modes below is the backstop.

If `$REST` did not include a slug, derive one from the session topic
(kebab-case, ≤6 words). Surface it in the final report so the user can rename
via `git mv` before merge.

### 3. Gather session context for the author blurb

- Model + context window (e.g. `Opus 4.7, 1M ctx`).
- Environment (Anthropic cloud sandbox vs local CLI; `${CLAUDE_CODE_REMOTE:-false}`).
- Repo scope (which coo-labs repos are readable — gh + GitHub MCP usually means
  all of them for a COO instance).
- Who brought the task (typically Ven, by name).
- Today's UTC date: `date -u +%Y-%m-%d`.

Compose a one-line author blurb matching existing examples
(`$COO/briefings/001-session-token-plan.md`, `003-claude-code-cross-session-state.md`).
Be specific about what your scope can and cannot see — the recipient relies on
this to calibrate trust in your framing.

### 4. Switch to a fresh branch (skip if `--draft`)

The briefing lands on its own branch so it doesn't pollute any in-flight
feature work. Capture starting branch + stash uncommitted changes for clean
return.

```bash
cd "$COO"
START_BRANCH="$(git symbolic-ref --short HEAD 2>/dev/null || true)"
STASH_MSG="briefing-tmp-$(date +%s)"
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

Copy `template.md` to `$COO/briefings/${NEXT_NNN}-<slug>.md` and fill every
placeholder. The template carries the canonical frontmatter shape and the
required body sections; `reference.md` documents each frontmatter field. The
**Known bounds of this briefing** section is the honesty gate — generic
platitudes fail it.

### 6. Commit, push, open PR (skip if `--draft`)

Regenerate both the anchor TOC and the JSON index before staging:

```bash
cd "$COO"
python3 bin/briefings-index.py --write
git add "briefings/${NEXT_NNN}-<slug>.md" briefings/README.md briefings/briefing_index.json
git commit -m "Briefing ${NEXT_NNN}: <title>

<2-3 sentence summary>"
git push -u origin "$BRIEFING_BRANCH"
bash "${VADE_RUNTIME_DIR:-/home/user/coo-harness}/scripts/gh-pr-create.sh" \
  --repo coo-labs/coo-memory \
  --base main \
  --head "$BRIEFING_BRANCH" \
  --title "Briefing ${NEXT_NNN}: <title>" \
  --body "## Summary

<2-3 sentence summary>

## Honesty gate

Per \`briefings/README.md\`, the **Known bounds of this briefing** section is
the briefing's honesty gate. This briefing names <N> specific blind spots —
most load-bearing being <one or two pointers>.

## Lifecycle

Lands with \`status: open\`. The recipient picks it up via \`/briefing pickup\`,
which sets \`claimed_by_session\` + \`claimed_at\`. State transitions to
\`delivered\` via \`/briefing done\` when the target work lands."
```

Bare `gh` is required (not `GH_TOKEN=$GITHUB_MCP_PAT gh …` — that defeats the
`gh-coo-wrap.sh` shim). `gh-pr-create.sh` adds the closing-keyword lint.

Return to the starting branch and restore the stash:

```bash
cd "$COO"
git checkout "$START_BRANCH" >/dev/null 2>&1
[ "$STASHED" -eq 1 ] && git stash pop >/dev/null
```

### 7. Report back

After committing (or after writing if `--draft`):

- The path: `briefings/${NEXT_NNN}-<slug>.md`.
- Default path: PR URL + branch name; note the file is on the briefing
  branch, not the user's working branch.
- `--draft` path: reminder the file is uncommitted on the user's current
  branch.
- 2-3 sentence summary of what the briefing says.
- The slug used (especially if inferred — give the user a chance to `git mv`
  before merge).

## Failure modes

- **Stale `$GITHUB_MCP_PAT`** (exit 1, zero-byte stdout/stderr from `gh`):
  run `bash coo-harness/scripts/check-pat-freshness.sh`. On STALE, re-export
  via `op read op://COO/vade-coo-self-2026-04/token` or boot a fresh session.
- **Slug inference misfires.** Surface the inferred slug prominently in the
  final report; user renames before merge.
- **Branch dirty at start.** Stash-push captures; stash-pop after restores.
  If pop conflicts, leave the stash and tell the user how to resolve.
- **`--draft` requested but the file already exists at the NNN.** Stop and
  report; do not overwrite.
- **Concurrent author race** (two sessions both pick the same NNN after the
  gh-PR-fold). Collision is tolerated by the anchor index — both files retain
  their numbers; the index renders both under one heading. Do not renumber;
  inbound references the earlier briefing has accumulated would break.

## Related

- `template.md` (colocated) — the body shape, copied per `/briefing request`.
- `reference.md` (colocated) — schema, index format, `pickup`/`done`/`release` procedures.
- MEMO-2026-04-27-02 — original relocation from `vade-core/docs/briefings/`.
- [#1092](https://github.com/coo-labs/coo-memory/issues/1092) — collision-fix origin.
