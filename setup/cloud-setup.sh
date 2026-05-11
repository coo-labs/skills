#!/usr/bin/env bash
# cloud-setup.sh — install vade-app/skills into a Claude Code project.
#
# Usage:
#   ./setup/cloud-setup.sh <project-path>
#   ./setup/cloud-setup.sh --user             # install into ~/.claude/
#   ./setup/cloud-setup.sh --copy <path>      # copy instead of symlink
#   ./setup/cloud-setup.sh --include-reference <path>  # also install agents/reference/

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

mode="symlink"
include_reference=0
target=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --user)
      target="${HOME}/.claude"
      shift
      ;;
    --copy)
      mode="copy"
      shift
      ;;
    --include-reference)
      include_reference=1
      shift
      ;;
    --help|-h)
      sed -n '2,9p' "${BASH_SOURCE[0]}"
      exit 0
      ;;
    -*)
      echo "unknown flag: $1" >&2
      exit 2
      ;;
    *)
      target="$1/.claude"
      shift
      ;;
  esac
done

if [[ -z "$target" ]]; then
  echo "usage: $0 <project-path> | --user" >&2
  exit 2
fi

mkdir -p "$target/skills" "$target/agents"

install_one() {
  local src="$1"
  local dst="$2"
  if [[ "$mode" == "symlink" ]]; then
    ln -sfn "$src" "$dst"
  else
    rm -rf "$dst"
    cp -r "$src" "$dst"
  fi
  echo "  $dst"
}

echo "Installing skills into $target/skills/ (mode: $mode):"
for d in "$REPO_ROOT"/skills/*/; do
  name="$(basename "$d")"
  install_one "$d" "$target/skills/$name"
done

echo "Installing agents into $target/agents/ (mode: $mode):"
for f in "$REPO_ROOT"/agents/*.md; do
  name="$(basename "$f")"
  install_one "$f" "$target/agents/$name"
done

if [[ "$include_reference" -eq 1 && -d "$REPO_ROOT/agents/reference" ]]; then
  echo "Installing reference agents (VADE-coupled; review before use):"
  for f in "$REPO_ROOT"/agents/reference/*.md; do
    [[ -f "$f" ]] || continue
    name="$(basename "$f")"
    install_one "$f" "$target/agents/$name"
  done
fi

echo
echo "Done. Optional next step:"
echo "  cp $REPO_ROOT/setup/mcp.json.template $(dirname "$target")/.mcp.json"
echo "  # then edit to fill in your op:// vault paths or env vars"
