#!/usr/bin/env bash
# day-overview: manifest gatherer for the `/day-overview` slash command.
#
# Lives at <coo-memory>/.claude/skills/day-overview/scripts/day-overview.sh; resolves
# its data root via SCRIPT_DIR. Travels with the data.
#
# Emits a single JSON manifest covering:
#   - the UTC arc (start_iso, end_iso)
#   - memos issued in the arc (id, title, date, status, supersedes, file_path)
#   - merged PRs in the arc across the five coo-labs repos
#   - integrity-check summary snapshot (if available)
#   - whether the target retrospective file already exists
#
# Output is pure JSON on stdout; diagnostics go to stderr.
#
# Usage:
#   day-overview.sh --date YYYY-MM-DD [--end YYYY-MM-DD]
#
# `--end` extends the arc through end-of-day UTC of the named date (inclusive).
# Default arc is exactly the 24-hour UTC window of `--date`.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd -P)"
COO_REPO="$(cd "$SCRIPT_DIR/../../../.." && pwd -P)"

DATE=""
END=""
REPOS=(coo-memory coo-harness coo-logs coo-console tjsonl skills coo4one vade-canvas site)

usage() {
  cat >&2 <<EOF
Usage: day-overview.sh --date YYYY-MM-DD [--end YYYY-MM-DD]
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --date) DATE="$2"; shift 2 ;;
    --end)  END="$2"; shift 2 ;;
    -h|--help) usage; exit 0 ;;
    *) echo "unknown arg: $1" >&2; usage; exit 2 ;;
  esac
done

[[ -n "$DATE" ]] || { usage; exit 2; }
[[ "$DATE" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}$ ]] || { echo "bad --date: $DATE" >&2; exit 2; }
END="${END:-$DATE}"
[[ "$END" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}$ ]] || { echo "bad --end: $END" >&2; exit 2; }

command -v jq >/dev/null 2>&1 || { echo "day-overview: jq required" >&2; exit 3; }

START_ISO="${DATE}T00:00:00Z"
END_ISO="${END}T23:59:59Z"

INDEX="$COO_REPO/memos/memo_index.json"
[[ -f "$INDEX" ]] || { echo "day-overview: $INDEX not found" >&2; exit 4; }

MEMOS_JSON="$(jq --arg d "$DATE" --arg e "$END" '[.[] | select(.date >= $d and .date <= $e) | {id, title, date, status, supersedes, file_path}]' "$INDEX")"

TMPDIR_JSON="$(mktemp -d)"
trap 'rm -rf "$TMPDIR_JSON"' EXIT
PRS_FILE="$TMPDIR_JSON/prs.json"
echo '{}' > "$PRS_FILE"
if command -v gh >/dev/null 2>&1 && [[ -n "${GITHUB_MCP_PAT:-${GITHUB_TOKEN:-${GH_TOKEN:-}}}" ]]; then
  for repo in "${REPOS[@]}"; do
    list_file="$TMPDIR_JSON/${repo}.json"
    GH_TOKEN="${GITHUB_MCP_PAT:-${GITHUB_TOKEN:-${GH_TOKEN:-}}}" gh pr list --repo "coo-labs/$repo" --state merged \
      --search "merged:>=${DATE} merged:<=${END}T23:59:59Z" \
      --json number,title,mergedAt,author,mergedBy,url \
      --limit 50 > "$list_file" 2>/dev/null || echo '[]' > "$list_file"
    jq --arg r "$repo" --slurpfile l "$list_file" '. + {($r): $l[0]}' "$PRS_FILE" > "$PRS_FILE.tmp" && mv "$PRS_FILE.tmp" "$PRS_FILE"
  done
fi

INTEGRITY_JSON='null'
INTEGRITY_PATH="${VADE_CLOUD_STATE_DIR:-${CLAUDE_PROJECT_DIR:-$HOME}/.vade-cloud-state}/integrity-check.json"
if [[ -f "$INTEGRITY_PATH" ]]; then
  INTEGRITY_JSON="$(jq '{ok: .summary.ok, passed: .summary.passed, total: .summary.total, degraded: .summary.degraded}' "$INTEGRITY_PATH")"
fi

TARGET_FILE="$COO_REPO/retrospectives/${DATE}_day-overview.md"
EXISTS=false
[[ -f "$TARGET_FILE" ]] && EXISTS=true

PRIOR_FILE=""
if [[ -d "$COO_REPO/retrospectives" ]]; then
  PRIOR_FILE="$(ls -1 "$COO_REPO/retrospectives"/*_day-overview.md 2>/dev/null | grep -v "${DATE}_day-overview.md" | sort | tail -1 || true)"
fi

MEMOS_FILE="$TMPDIR_JSON/memos.json"
INTEGRITY_FILE="$TMPDIR_JSON/integrity.json"
printf '%s' "$MEMOS_JSON" > "$MEMOS_FILE"
printf '%s' "$INTEGRITY_JSON" > "$INTEGRITY_FILE"

jq -n \
  --arg date "$DATE" \
  --arg start_iso "$START_ISO" \
  --arg end_iso "$END_ISO" \
  --arg coo_repo "$COO_REPO" \
  --arg target_file "$TARGET_FILE" \
  --arg prior_file "$PRIOR_FILE" \
  --argjson exists "$EXISTS" \
  --slurpfile memos "$MEMOS_FILE" \
  --slurpfile prs "$PRS_FILE" \
  --slurpfile integrity "$INTEGRITY_FILE" \
  '{
    date: $date,
    arc: {start_iso: $start_iso, end_iso: $end_iso},
    coo_repo: $coo_repo,
    target_file: $target_file,
    target_exists: $exists,
    prior_day_overview: (if $prior_file == "" then null else $prior_file end),
    memos: $memos[0],
    memo_count: ($memos[0] | length),
    prs: $prs[0],
    pr_count: ([$prs[0][] | length] | add // 0),
    integrity_check: $integrity[0]
  }'
