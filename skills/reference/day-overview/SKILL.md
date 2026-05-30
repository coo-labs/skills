---
name: day-overview
description: Produce a day-overview retrospective — briefing-shaped synthesis of a day's shipped work (memos, PRs, integrity-check state) grouped into lanes, with follow-ups and candidate next actions. Use at end-of-day or to summarize a window of work. Default flow ships (writes file, commits, opens PR); `--no-ship` stops at file write; `--post` also posts to vade-core Retrospectives Discussions. Don't invoke for routine status updates (use `/status-check`) or single-PR retrospectives (write a memo).
argument-hint: "[--date YYYY-MM-DD] [--end YYYY-MM-DD] [--no-ship] [--post]"
disable-model-invocation: true
allowed-tools: Bash, Read, Write, Edit
metadata:
  type: procedural
  vendoring: custom
---

# day-overview — briefing-shaped synthesis of a day's shipped work

Produces a structured retrospective for a UTC date window:
memos issued, PRs merged, integrity-check state, grouped into
lanes, with carried-forward follow-ups and ranked next actions.
The file lands at `coo/retrospectives/<date>_day-overview.md`;
the default flow ships via PR.

Format reference: the most recent existing day-overview in
`coo/retrospectives/`. Match its shape exactly — readers expect
this shape, not creative restructuring.

> **Reference skill.** The pattern (briefing-shape day synthesis
> from substrate records — memos, merged PRs, integrity snapshot
> — grouped into lanes) is portable; the worked-example paths
> (`coo/retrospectives/`, `coo/memos/`, the five `vade-app/*`
> repo list, integrity-check JSON shape, GraphQL category and
> label IDs) and the `scripts/day-overview.sh` manifest gatherer
> are substrate-coupled and ship verbatim as the VADE worked
> example. Read [`../README.md`](../README.md) for the
> fork-and-adapt path.

## When to use this skill

Invoke when:

- The day has wrapped (UTC) and the operator wants a structured
  digest of what shipped.
- A multi-day window needs synthesis (use `--end` to extend).
- The user types `/day-overview` directly.

Don't invoke for:

- Routine status updates (use `/status-check` for grounding).
- Single-PR retrospectives (write a memo, not a day-overview).
- Reflection that doesn't fit the briefing shape (write prose
  to `coo/_drafts/`).

## Procedure

### 0. Resolve paths and date

```bash
COO="$(for c in "${COO_MEMORY_DIR:-}" "${CLAUDE_PROJECT_DIR:-}" "${CLAUDE_PROJECT_DIR:-}/../vade-coo-memory" "$HOME/GitHub/vade-app/vade-coo-memory" "/home/user/vade-coo-memory"; do [ -n "$c" ] && [ -f "$c/coo/memo_protocol.md" ] && { cd "$c" && pwd -P; break; }; done)"
[ -n "$COO" ] || { echo "day-overview: could not find vade-coo-memory data root"; exit 1; }
```

Determine the target date:

- If `$ARGUMENTS` contains `--date YYYY-MM-DD`, use that.
- Otherwise default to **yesterday UTC**
  (`date -u -d 'yesterday' +%Y-%m-%d`). A day-overview most often
  runs after the day has wrapped; "today" UTC may still be in
  progress.

Determine the end date:

- If `$ARGUMENTS` contains `--end YYYY-MM-DD`, use that.
- Otherwise default to a single 24-hour UTC window of `--date`
  (the script's `END="${END:-$DATE}"`). For multi-day arcs
  (e.g. backfill that crosses several days), pass `--end`
  explicitly.

Tell the user the chosen window in one line before proceeding.

### 1. Gather the manifest

```bash
MANIFEST="$(bash "$COO/.claude/skills/day-overview/scripts/day-overview.sh" --date "$DATE" --end "$END")"
```

The manifest is JSON with these top-level fields:

- `date`, `arc.start_iso`, `arc.end_iso`
- `target_file` — where the briefing will be written
- `target_exists` — boolean; if true, abort unless the user
  explicitly confirms overwrite
- `prior_day_overview` — path to the most recent existing
  day-overview (the format reference)
- `memos` — array of memos issued in window (id, title,
  date, status, supersedes, file_path)
- `memo_count`, `pr_count`
- `prs` — `{<repo>: [{number, title, mergedAt, author, mergedBy, url}, ...], ...}`
- `integrity_check` — `{ok, passed, total, degraded}` snapshot

If `memo_count == 0 && pr_count == 0`, stop and tell the user
the window has no record to synthesize. Do not write a
placeholder.

If `target_exists == true`, ask the user whether to overwrite
before proceeding.

### 2. Read the format reference and source memos

Read the file at `prior_day_overview` (most recently shipped
day-overview). It is the canonical format reference. Every
section it contains should appear in your output unless you have
a specific reason to drop one.

Read the full text of every memo in the manifest via Read on
`$COO/<file_path>` (one file per memo, post-issue-#210). The
memos are the load-bearing source of structure for the briefing
— every lane traces back to one or more.

For PRs that the manifest titles suggest are pivotal to a lane
(large diffs, named in memos, or whose titles introduce a new
system), optionally fetch the PR body via
`GH_TOKEN="$GITHUB_MCP_PAT" gh pr view <N> --repo vade-app/<repo>`.
Don't fetch every PR; fetch only when the title is insufficient.

### 3. Synthesize the briefing

Write the file at `target_file`. Match the structure of
`prior_day_overview` exactly.

**Frontmatter date for multi-day arcs.** The publish-site build
derives the rendered page's `date:` from the filename prefix when no
frontmatter is set (`bin/publish-site/build.py:_date_from_path`). The
filename uses `$DATE` (the start), so for multi-day arcs the publish
date would mis-attribute to the start. When `--end != --date`,
prepend a YAML frontmatter block with `date: <END>` so the published
page carries the correct close date. Single-day windows can omit the
block — the filename prefix serves. (vade-coo-memory#622.)

```yaml
---
date: <END>
---
```

Required sections in order:

1. **Title** — `# YYYY-MM-DD — Day overview`.
2. **Italicized header** — one paragraph naming this is a
   briefing-not-reflective synthesis. Note the UTC arc, named
   source memos, and that the file is a synthesis (not source of
   truth — the memos are).
3. **Scope and framing** — one or two paragraphs. Describe the
   day's shape (operational vs. structural, the dominant
   pattern, any cross-day arc). Surface counts (memos, PRs per
   repo). Do not list everything; just enough that a reader can
   pre-load expectations.
4. **Lanes** — group by lane, not timestamp. Three to six lanes
   is typical (four was the median in prior overviews). Each
   lane: one bolded memo header (or "no memo, but…" for PR-only
   arcs), one paragraph of context, the decisions/sub-PRs that
   landed, and a "Net effect of Lane N" closing paragraph.
5. **How this fits existing priorities** — usually 3–5 bullets,
   each one project / arc / structural-claim.
6. **Open follow-ups carried forward** — number them. Each has
   a one-sentence symptom + the surface that tracks it (issue #,
   memo ID, etc.).
7. **Candidate next actions** — group by friction
   (lowest-first). Standard buckets: "Single-instance, no
   committee" / "Operational close-out" / "Committee-scoped" /
   "Design / exploration". Plus a "Standing obligation" line
   for end-of-session discipline.
8. **Footer** — `*End of briefing. Source memos: ... Linked artifacts: ... Linked discussions: ... Integrity check at briefing close: N/N OK.*`

#### Voice rules (strict — match prior overviews)

- **Briefing, not reflective.** No "I felt", "we noticed", or
  first-person interiority. State facts, decisions, net effects.
- **Dense.** No throat-clearing. Every paragraph carries
  information.
- **Past tense for what shipped; present tense for current
  state and rules.**
- **Concrete identifiers.** Cite memo IDs, PR numbers (with
  repo prefix when cross-repo, per the `<owner>/<repo>#NN`
  rule), file paths, line numbers.
- **No emojis.** Em-dashes are fine; bullet-prefix glyphs like
  `•` and `→` are fine in body text but not in lane headers.

### 4. Verify

```bash
[ -f "$TARGET_FILE" ] && wc -l "$TARGET_FILE"
```

Expect 200–600 lines for a day with 3–5 memos. Substantially
shorter suggests under-synthesis; substantially longer suggests
over-elaboration. Tell the user the file path and line count.

### 5. Ship the PR (default)

Ship by default. If `$ARGUMENTS` contains `--no-ship`, skip this
step and stop after the file write so the user can review before
committing.

If the harness has already placed you on a designated dev branch
(typical of cloud sessions — e.g. `claude/day-overview-*`),
reuse it; otherwise create a date-based branch:

```bash
cd "$COO"
CURRENT_BRANCH="$(git branch --show-current)"
case "$CURRENT_BRANCH" in
  claude/*) BRANCH="$CURRENT_BRANCH" ;;
  *) BRANCH="claude/day-overview-${DATE}"
     git checkout -b "$BRANCH" 2>/dev/null || git checkout "$BRANCH" ;;
esac
git add "coo/retrospectives/${DATE}_day-overview.md"
git commit -m "Add ${DATE} day-overview retrospective"
git push -u origin "$BRANCH"
GH_TOKEN="$GITHUB_MCP_PAT" gh pr create --repo vade-app/vade-coo-memory --base main --head "$BRANCH" \
  --title "Add ${DATE} day-overview retrospective" \
  --body "Briefing-shaped synthesis of ${DATE}'s shipped work. Mirrors the format of prior day-overviews. See file body for source memos and lane breakdown."
```

The `--head "$BRANCH"` flag is load-bearing: in cloud sessions
the local git remote is a proxy that `gh` cannot resolve, so
`gh pr create` needs the branch named explicitly. If a branch
with the chosen name was already pushed and merged, reuse the
current working branch — use judgment.

### 6. Optional: post to Discussions Retrospectives

If `$ARGUMENTS` contains `--post`:

```bash
# Body = file content + standard source-link footer (day-overview-specific)
{
  cat "$TARGET_FILE"
  printf '\n\n---\n\n*Source: [`coo/retrospectives/%s_day-overview.md`](https://github.com/vade-app/vade-coo-memory/blob/main/coo/retrospectives/%s_day-overview.md) on `vade-app/vade-coo-memory`. The file is the source of truth; this discussion is the publication surface.*\n' "$DATE" "$DATE"
} > "/tmp/day-overview-body-${DATE}.md"

# Discussion title — strip the leading "# " from the file's H1 line; no [retrospective*] prefix
TITLE="$(head -1 "$TARGET_FILE" | sed 's/^# //')"

# Post via the shared helper (created 2026-04-30, vade-coo-memory#313 PR)
RESULT=$(bash "$COO/.claude/_lib/post-discussion.sh" \
  retrospectives \
  "$TITLE" \
  "/tmp/day-overview-body-${DATE}.md" \
  LA_kwDOR_h5U88AAAACgyezFw)

URL="$(jq -r '.url' <<<"$RESULT")"
NUMBER="$(jq -r '.number' <<<"$RESULT")"
```

The helper at `.claude/_lib/post-discussion.sh` owns
the GraphQL mechanic, the seven category IDs, and the repo ID.
The `retrospective: day-overview` label ID
(`LA_kwDOR_h5U88AAAACgyezFw`) is passed as the fourth argument.
**The helper is shared with the `post-discussion` skill** — both
consumers route through the same authoritative GraphQL surface.

Tell the user the discussion number and URL.

## Critical constraints

- **Never overwrite an existing file silently.** If
  `target_exists == true`, ask first.
- **Default flow ships.** Write file → commit → push → open PR
  by default. `--no-ship` stops at the file write for
  review-first workflows.
- **Never invent memos or PRs.** Synthesize only what the
  manifest contains. If the manifest is empty, stop.
- **No `[retrospective*]` prefix on the discussion title.** Per
  the Retrospectives category convention, the category surface
  plus the `retrospective:*` label do that work.
- **Match the prior format.** Readers know the shape; surprise
  restructuring costs more than it pays.

## Failure modes

- **Manifest empty (no memos, no PRs).** Stop with a one-line
  report; don't write a placeholder.
- **`target_exists == true`.** Ask the user before overwriting.
- **`gh pr create` fails on cloud branch.** Confirm the
  `--head "$BRANCH"` flag is set; the local git proxy can't
  resolve it implicitly.
- **`post-discussion.sh` returns non-2xx.** Surface the error
  body; the helper's failure is the upstream-Discussions API,
  not local state.

## Canonical source

```text
vade-coo-memory/.claude/skills/day-overview/scripts/day-overview.sh (manifest builder)
vade-coo-memory/.claude/_lib/post-discussion.sh (shared GraphQL helper)
vade-coo-memory/coo/retrospectives/<date>_day-overview.md (output location)
```

## Cross-references

- `post-discussion` skill — shares `_lib/post-discussion.sh`;
  same authoritative GraphQL surface.
- `commission-retrospective` skill — historian-voiced
  retrospectives for pivotal events (different scope; SOP-CULTURE-001 §2d
  triggers vs day-window synthesis).
- vade-coo-memory#313 — `_lib/post-discussion.sh` extraction (the
  cross-consumer refactor).
- vade-coo-memory#333 — command→skill migration sweep epic; this
  skill is Class C item 1 of 3.

# Setup hints

*Read by [`adapt-skill`](../../adapt-skill/SKILL.md). Stripped from
the adapted output. Schema: [`adapt-skill/SCHEMA.md`](../../adapt-skill/SCHEMA.md).
The bundled `scripts/day-overview.sh` is REGENERATE-PER-USER —
the meta-skill emits a skeleton, not a working script; you author
the manifest builder against your own substrate.*

```yaml
requires:
  - kind: file
    name: "post-discussion helper (for --post flag only)"
    detect: "test -f \"$(git rev-parse --show-toplevel 2>/dev/null)\"/.claude/_lib/post-discussion.sh"
    severity: warning
    install_hint: "Only needed if you'll use --post to publish to a discussion surface. The shared helper carries platform-specific GraphQL IDs and is best authored per-substrate. Without it, --post is unavailable; the rest of the skill works."

setup_hints:
  - key: data_root_var
    kind: PROMPT
    question: "What shell variable name should hold the repo root in this skill? (VADE uses $COO.) Examples: $REPO, $REPO_ROOT, $PROJECT."
    find: "$COO"
    fallback: "$REPO_ROOT"

  - key: data_root_discovery
    kind: OPTIONAL
    question: "Step 0 discovers the repo root via a sentinel file (VADE looks for coo/memo_protocol.md). What's your equivalent sentinel? Skip to use git rev-parse instead."
    find_unique: true
    find: |
      ```bash
      COO="$(for c in "${COO_MEMORY_DIR:-}" "${CLAUDE_PROJECT_DIR:-}" "${CLAUDE_PROJECT_DIR:-}/../vade-coo-memory" "$HOME/GitHub/vade-app/vade-coo-memory" "/home/user/vade-coo-memory"; do [ -n "$c" ] && [ -f "$c/coo/memo_protocol.md" ] && { cd "$c" && pwd -P; break; }; done)"
      [ -n "$COO" ] || { echo "day-overview: could not find vade-coo-memory data root"; exit 1; }
      ```
    fallback: |
      ```bash
      REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null)"
      [ -n "$REPO_ROOT" ] || { echo "day-overview: run from inside a git repo"; exit 1; }
      ```

  - key: retrospectives_dir
    kind: PROMPT
    question: "Where should day-overview files land? (VADE: coo/retrospectives/.) Examples: docs/retrospectives/, logs/daily/, .agent-logs/days/."
    find: "coo/retrospectives/<date>_day-overview.md"
    fallback: "retrospectives/<date>_day-overview.md"

  - key: retrospectives_dir_short
    kind: PROMPT
    question: "Same retrospectives dir without the trailing filename (used in several body locations). Provide just the directory path with trailing slash."
    find: "coo/retrospectives/"
    fallback: "retrospectives/"

  - key: memos_dir_ref
    kind: OPTIONAL
    question: "Do you have a memos directory the skill should mention as the source-of-truth for lanes? (VADE: coo/memos/.) Skip if you have no memo system."
    find: "`coo/memos/`"
    fallback: "your project's records directory"

  - key: github_token_env
    kind: OPTIONAL
    question: "Environment variable for your GitHub PAT? (Examples: GITHUB_TOKEN, GITHUB_MCP_PAT.) Skip if gh's default auth works."
    find: "GH_TOKEN=\"$GITHUB_MCP_PAT\" "
    fallback: ""

  - key: target_repo_prefix
    kind: PROMPT
    question: "GitHub org or owner prefix for your repos? (VADE: vade-app.) Examples: myorg, alice."
    find: "vade-app/"
    fallback: ""

  - key: target_repo
    kind: PROMPT
    question: "Primary repo for day-overview PRs? (owner/repo format.)"
    find: "vade-app/vade-coo-memory"
    fallback: ""

  - key: branch_prefix
    kind: OPTIONAL
    question: "Branch naming prefix for new day-overview branches? (VADE uses claude/day-overview-YYYY-MM-DD.) Skip for the default."
    find: "claude/day-overview-${DATE}"
    fallback: "day-overview-${DATE}"

  - key: branch_match
    kind: OPTIONAL
    question: "Branch-name glob for the 'reuse cloud-session designated branch' check? (VADE: claude/*.) Skip for the default."
    find: "  claude/*) BRANCH=\"$CURRENT_BRANCH\" ;;"
    fallback: "  agent/*|claude/*) BRANCH=\"$CURRENT_BRANCH\" ;;"

  - key: vade_repo_aside_main
    kind: OPTIONAL
    question: "Skip unless you want to keep the 'vade-app/<repo>' reference in the gh pr view example."
    find: "GH_TOKEN=\"$GITHUB_MCP_PAT\" gh pr view <N> --repo vade-app/<repo>"
    fallback: "GH_TOKEN=\"$GITHUB_MCP_PAT\" gh pr view <N> --repo <owner>/<repo>"

  - key: post_discussion_step
    kind: OPTIONAL
    question: "Do you have a discussion-post surface and helper script for the --post flag? Skip to drop Step 6 entirely."
    find_unique: true
    find: |
      ### 6. Optional: post to Discussions Retrospectives
      
      If `$ARGUMENTS` contains `--post`:
      
      ```bash
      # Body = file content + standard source-link footer (day-overview-specific)
      {
        cat "$TARGET_FILE"
        printf '\n\n---\n\n*Source: [`coo/retrospectives/%s_day-overview.md`](https://github.com/vade-app/vade-coo-memory/blob/main/coo/retrospectives/%s_day-overview.md) on `vade-app/vade-coo-memory`. The file is the source of truth; this discussion is the publication surface.*\n' "$DATE" "$DATE"
      } > "/tmp/day-overview-body-${DATE}.md"
      
      # Discussion title — strip the leading "# " from the file's H1 line; no [retrospective*] prefix
      TITLE="$(head -1 "$TARGET_FILE" | sed 's/^# //')"
      
      # Post via the shared helper (created 2026-04-30, vade-coo-memory#313 PR)
      RESULT=$(bash "$COO/.claude/_lib/post-discussion.sh" \
        retrospectives \
        "$TITLE" \
        "/tmp/day-overview-body-${DATE}.md" \
        LA_kwDOR_h5U88AAAACgyezFw)
      
      URL="$(jq -r '.url' <<<"$RESULT")"
      NUMBER="$(jq -r '.number' <<<"$RESULT")"
      ```
      
      The helper at `.claude/_lib/post-discussion.sh` owns
      the GraphQL mechanic, the seven category IDs, and the repo ID.
      The `retrospective: day-overview` label ID
      (`LA_kwDOR_h5U88AAAACgyezFw`) is passed as the fourth argument.
      **The helper is shared with the `post-discussion` skill** — both
      consumers route through the same authoritative GraphQL surface.
      
      Tell the user the discussion number and URL.
    fallback: |
      ### 6. (Skipped — no discussion-post surface configured)
      
      Adapt-skill: no `_lib/post-discussion.sh` helper detected in your
      substrate. The `--post` flag is unavailable in this adapted skill.
      If you later install a discussion-post helper (e.g. by adapting the
      `post-discussion` skill), re-run `/adapt-skill day-overview` to
      restore this step.

script_hints:
  - path: scripts/day-overview.sh
    treatment: REGENERATE-PER-USER
    rationale: "Hardcodes five VADE repo names in REPOS array; coo/memo_index.json path; the $VADE_CLOUD_STATE_DIR integrity-check probe; four-level path-relative discovery. Mechanical substitution can't safely rewrite all of these without breaking shell quoting. Skeleton emitted with TODO comments for: REPOS list, memo-index path (or skip-block), integrity-check probe (or skip-block), output directory."
```
