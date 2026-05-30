#!/usr/bin/env python3
"""Update specific YAML-frontmatter fields in a briefing file, atomically.

Usage:
  update-frontmatter.py <file> --set key=value [--set key=value ...]

Value parsing:
  - "null", "~", "" → None
  - "true" / "false" → bool
  - anything else    → string (quoted in the written YAML to stay a string)

Limited to flat key:value frontmatter — the shape `template.md` produces. No
nested structures, no flow style. The frontmatter block must be the first
thing in the file and end on the second `---` line.
"""
import argparse
import sys
from pathlib import Path


def parse_value(raw: str):
    low = raw.lower()
    if low in ("", "null", "~"):
        return None
    if low == "true":
        return True
    if low == "false":
        return False
    return raw


def yaml_dump_value(v) -> str:
    if v is None:
        return "null"
    if isinstance(v, bool):
        return "true" if v else "false"
    s = str(v)
    needs_quote = (
        s == ""
        or s in ("null", "~", "true", "false")
        or s[:1] in "\"'-[{|>!&*"
        or any(c in s for c in "\n#:")
    )
    if needs_quote:
        return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'
    return s


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("file", type=Path)
    ap.add_argument("--set", action="append", default=[], metavar="KEY=VALUE")
    args = ap.parse_args()

    text = args.file.read_text(encoding="utf-8")
    if not text.startswith("---\n") and not text.startswith("---\r\n"):
        print(f"{args.file}: missing YAML frontmatter", file=sys.stderr)
        return 2
    end = text.find("\n---", 4)
    if end < 0:
        print(f"{args.file}: unterminated frontmatter", file=sys.stderr)
        return 2

    fm_lines = text[4:end].splitlines()
    body = text[end + 4 :]  # starts at "\n..." after closing ---

    updates: dict[str, object] = {}
    for assignment in args.set:
        if "=" not in assignment:
            print(f"--set expects key=value (got {assignment!r})", file=sys.stderr)
            return 2
        k, _, v = assignment.partition("=")
        updates[k.strip()] = parse_value(v)

    seen: set[str] = set()
    new_lines: list[str] = []
    for line in fm_lines:
        stripped = line.lstrip()
        if not stripped or stripped.startswith("#") or ":" not in stripped:
            new_lines.append(line)
            continue
        key = stripped.split(":", 1)[0].strip()
        if key in updates:
            new_lines.append(f"{key}: {yaml_dump_value(updates[key])}")
            seen.add(key)
        else:
            new_lines.append(line)

    for key, val in updates.items():
        if key not in seen:
            new_lines.append(f"{key}: {yaml_dump_value(val)}")

    new_fm = "\n".join(new_lines)
    new_text = "---\n" + new_fm + ("\n" if not new_fm.endswith("\n") else "") + "---" + body

    tmp = args.file.with_suffix(args.file.suffix + ".tmp")
    tmp.write_text(new_text, encoding="utf-8")
    tmp.replace(args.file)
    return 0


if __name__ == "__main__":
    sys.exit(main())
