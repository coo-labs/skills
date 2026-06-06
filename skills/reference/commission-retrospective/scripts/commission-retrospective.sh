#!/usr/bin/env bash
# commission-retrospective: pre-flight and optional PR opener for the
# `/commission-retrospective` slash command.
#
# Lives at <coo-memory>/.claude/skills/commission-retrospective/scripts/commission-retrospective.sh;
# resolves its data root via SCRIPT_DIR. Travels with the data.
#
# Modes:
#   --scope      Emit a JSON scope manifest on stdout (no side effects).
#   --open-pr    Open a PR on coo-memory for a completed draft.
#   --manual     Fallback orchestrator when in-session Task is unavailable;
#                sequences two `claude -p` invocations using the briefs.
#
# See <coo-memory>/operations/culture_system_sop.md (SOP-CULTURE-001) for spec.
# See <coo-memory>/.claude/skills/commission-retrospective/SKILL.md for procedure.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd -P)"
COO_REPO="$(cd "$SCRIPT_DIR/../../../.." && pwd -P)"

MODE=""
SINCE=""
UNTIL=""
PRS=""
FOCUS=""
SLUG=""

usage() {
  cat >&2 <<EOF
Usage:
  commission-retrospective.sh --scope   --since YYYY-MM-DD [--until YYYY-MM-DD] [--prs N,M] [--focus "Q"] --slug <slug>
  commission-retrospective.sh --open-pr --slug <slug> [--body-file PATH]
  commission-retrospective.sh --manual  --since YYYY-MM-DD [--until YYYY-MM-DD] --slug <slug>

The skill at <coo-memory>/.claude/skills/commission-retrospective/
drives the historian flow; this shell helper handles only the plumbing.
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --scope)    MODE="scope"; shift ;;
    --open-pr)  MODE="open-pr"; shift ;;
    --manual)   MODE="manual"; shift ;;
    --since)    SINCE="$2"; shift 2 ;;
    --until)    UNTIL="$2"; shift 2 ;;
    --prs)      PRS="$2"; shift 2 ;;
    --focus)    FOCUS="$2"; shift 2 ;;
    --slug)     SLUG="$2"; shift 2 ;;
    --body-file) BODY_FILE="$2"; shift 2 ;;
    -h|--help)  usage; exit 0 ;;
    *) echo "unknown arg: $1" >&2; usage; exit 2 ;;
  esac
done

[ -n "$MODE" ] || { usage; exit 2; }

sanitize_slug() {
  printf '%s' "$1" \
    | tr '[:upper:]' '[:lower:]' \
    | tr -c 'a-z0-9-' '-' \
    | tr -s '-' \
    | sed 's/^-//;s/-$//'
}

today_utc() { date -u +%Y-%m-%d; }

ensure_jq() {
  if ! command -v jq >/dev/null 2>&1; then
    echo "commission-retrospective: jq required" >&2
    exit 3
  fi
}

ensure_gh() {
  if ! command -v gh >/dev/null 2>&1; then
    return 1
  fi
  if [ -z "${GITHUB_MCP_PAT:-}" ] && command -v op >/dev/null 2>&1; then
    # Post-Phase-2 (coo-memory#873) the PAT is not in tool-subshell env;
    # this script passes GH_TOKEN=$GITHUB_MCP_PAT into gh calls, so the
    # gh-coo-wrap.sh own op-read doesn't fire. Single-shot fallback,
    # same pattern as coo-harness#456.
    GITHUB_MCP_PAT="$(op read op://COO/github-pat-vade-coo/token 2>/dev/null || true)"
    export GITHUB_MCP_PAT
  fi
  [ -n "${GITHUB_MCP_PAT:-}" ] || return 1
  return 0
}

emit_scope() {
  ensure_jq
  [ -n "$SINCE" ] || { echo "--since required" >&2; exit 2; }
  [ -n "$SLUG"  ] || { echo "--slug required" >&2; exit 2; }
  local until_resolved="${UNTIL:-$(today_utc)}"
  local safe_slug; safe_slug=$(sanitize_slug "$SLUG")

  local prs_json='[]'
  if ensure_gh; then
    prs_json=$(GH_TOKEN="$GITHUB_MCP_PAT" gh pr list \
      --repo coo-labs/coo-memory \
      --state merged \
      --search "merged:$SINCE..$until_resolved" \
      --json number,title,author,mergedAt,url \
      --limit 100 2>/dev/null || echo '[]')
  fi

  local memos_json='[]'
  local index_path="$COO_REPO/memos/memo_index.json"
  if [ -f "$index_path" ]; then
    memos_json=$(jq --arg s "$SINCE" --arg u "$until_resolved" \
      '[.[] | select(.date >= $s and .date <= $u)]' "$index_path" 2>/dev/null || echo '[]')
  fi

  local foundations_json='[]'
  if [ -d "$COO_REPO/foundations" ]; then
    foundations_json=$(cd "$COO_REPO/foundations" 2>/dev/null \
      && ls -1 2>/dev/null \
      | grep -E '^[0-9]{4}-[0-9]{2}-[0-9]{2}_' \
      | grep -vE '_transcript\.md$|_agent-reports' \
      | awk -v s="$SINCE" -v u="$until_resolved" '
          { d = substr($0, 1, 10); if (d >= s && d <= u) print $0 }
        ' \
      | jq -R -s 'split("\n") | map(select(length > 0))' 2>/dev/null \
      || echo '[]')
  fi

  local prior_json='[]'
  if [ -d "$COO_REPO/retrospectives" ]; then
    prior_json=$(cd "$COO_REPO/retrospectives" 2>/dev/null \
      && ls -1 2>/dev/null \
      | grep -E '^[0-9]{4}-[0-9]{2}-[0-9]{2}[_-]' \
      | jq -R -s 'split("\n") | map(select(length > 0))' 2>/dev/null \
      || echo '[]')
  fi

  local extra_prs_json='[]'
  if [ -n "$PRS" ]; then
    extra_prs_json=$(printf '%s' "$PRS" \
      | tr ',' '\n' \
      | awk 'NF > 0 {print}' \
      | jq -R -s 'split("\n") | map(select(length > 0))' 2>/dev/null || echo '[]')
  fi

  jq -n \
    --arg since "$SINCE" \
    --arg until "$until_resolved" \
    --arg slug "$safe_slug" \
    --arg focus "$FOCUS" \
    --argjson prs "$prs_json" \
    --argjson extra_prs "$extra_prs_json" \
    --argjson memos "$memos_json" \
    --argjson foundations "$foundations_json" \
    --argjson prior "$prior_json" \
    '{
      window: {since: $since, until: $until},
      slug: $slug,
      focus: (if $focus == "" then null else $focus end),
      prs: $prs,
      extra_prs: $extra_prs,
      memos: $memos,
      foundations: $foundations,
      prior_commissions: $prior
    }'
}

open_pr() {
  ensure_gh || { echo "gh not available or GITHUB_MCP_PAT unset; skipping PR open" >&2; exit 4; }
  [ -n "$SLUG" ] || { echo "--slug required" >&2; exit 2; }
  local safe_slug; safe_slug=$(sanitize_slug "$SLUG")
  local body_arg
  if [ -n "${BODY_FILE:-}" ] && [ -f "${BODY_FILE}" ]; then
    body_arg="--body-file ${BODY_FILE}"
  else
    body_arg="--body 'Draft retrospective; see _drafts/ for the artifact and sub-agent reports.'"
  fi
  local branch
  branch=$(git -C "$COO_REPO" branch --show-current 2>/dev/null || echo "")
  [ -n "$branch" ] || { echo "no current branch in $COO_REPO" >&2; exit 5; }

  # shellcheck disable=SC2086
  GH_TOKEN="$GITHUB_MCP_PAT" gh pr create \
    --repo coo-labs/coo-memory \
    --base main \
    --head "$branch" \
    --title "[retrospective-draft] $safe_slug" \
    $body_arg
}

manual_run() {
  cat >&2 <<'EOF'
commission-retrospective: --manual fallback is documented but not yet
implemented. Expected shape:

  claude -p --brief templates/subagent-memos-brief.md ...
  claude -p --brief templates/subagent-pr-graph-brief.md ...
  claude -p --brief templates/historian-prompt.md ...

Each invocation writes to a _drafts/ path matching the slug. Ship
this when the in-session Task-subagent surface is proven unavailable on
a supported harness — until then, manual orchestration is the workaround.
See <coo-memory>/operations/culture_system_sop.md §3c.
EOF
  exit 6
}

case "$MODE" in
  scope)   emit_scope ;;
  open-pr) open_pr ;;
  manual)  manual_run ;;
  *)       usage; exit 2 ;;
esac
