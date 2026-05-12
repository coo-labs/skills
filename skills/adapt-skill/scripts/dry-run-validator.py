#!/usr/bin/env python3
"""Dry-run validator for adapt-skill # Setup hints manifest.

Reads a reference skill's SKILL.md, parses the # Setup hints YAML block,
verifies each `find:` string exists in the body, applies fallbacks, and
emits the adapted output to stdout. Reports problems (missing finds,
ambiguous find_unique, malformed YAML) to stderr.

Usage: python3 dry-run-adapt-skill.py <path-to-SKILL.md>
"""
import sys, re, os
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: pyyaml not installed. Install with: pip install pyyaml", file=sys.stderr)
    sys.exit(2)

def split_hints_block(text):
    """Return (body, hints_yaml) by splitting at the last `# Setup hints` H1."""
    lines = text.splitlines(keepends=True)
    hints_idx = None
    for i, line in enumerate(lines):
        if line.strip() == "# Setup hints":
            hints_idx = i  # take the last one
    if hints_idx is None:
        return text, None
    body = "".join(lines[:hints_idx])
    # Strip trailing whitespace from body
    body = body.rstrip() + "\n"
    hints_block = "".join(lines[hints_idx:])
    # Extract the first ```yaml ... ``` fenced block after the H1
    m = re.search(r"```yaml\n(.*?)\n```", hints_block, re.DOTALL)
    if not m:
        return body, None
    return body, m.group(1)

def validate_and_apply(skill_path, answers=None):
    """Walk the manifest. Report findings. Return (adapted_body, problems)."""
    text = Path(skill_path).read_text()
    body, hints_yaml = split_hints_block(text)
    problems = []
    if hints_yaml is None:
        problems.append("FATAL: no `# Setup hints` H1 with fenced ```yaml``` block found")
        return body, problems
    try:
        manifest = yaml.safe_load(hints_yaml)
    except yaml.YAMLError as e:
        problems.append(f"FATAL: YAML parse error: {e}")
        return body, problems
    if not isinstance(manifest, dict):
        problems.append(f"FATAL: manifest is not a dict (got {type(manifest).__name__})")
        return body, problems

    setup_hints = manifest.get("setup_hints", []) or []
    requires = manifest.get("requires", []) or []
    philosophical_gate = manifest.get("philosophical_gate")
    script_hints = manifest.get("script_hints", []) or []
    degradations = manifest.get("degradations", []) or []

    print(f"\n=== Manifest summary for {skill_path} ===", file=sys.stderr)
    print(f"  setup_hints:        {len(setup_hints)}", file=sys.stderr)
    print(f"  requires:           {len(requires)}", file=sys.stderr)
    print(f"  philosophical_gate: {'yes' if philosophical_gate else 'no'}", file=sys.stderr)
    print(f"  script_hints:       {len(script_hints)}", file=sys.stderr)
    print(f"  degradations:       {len(degradations)}", file=sys.stderr)

    # Validate each hint's find string exists; apply substitution with fallback.
    adapted = body
    for hint in setup_hints:
        key = hint.get("key", "<no-key>")
        kind = hint.get("kind", "<no-kind>")
        find = hint.get("find")
        find_unique = hint.get("find_unique", False)
        fallback = hint.get("fallback", "")
        if find is None:
            problems.append(f"hint '{key}': missing `find:` field")
            continue
        # Check presence in the (un-adapted, original) body
        count = body.count(find)
        if count == 0:
            problems.append(f"hint '{key}': find string NOT FOUND in body (0 occurrences)")
            continue
        if find_unique and count != 1:
            problems.append(f"hint '{key}': find_unique=true but found {count} occurrences")
            continue
        if count > 1 and not find_unique:
            print(f"  NOTE hint '{key}': find string appears {count} times — global substitute", file=sys.stderr)
        # Apply fallback (simulating a "skip" answer for all hints)
        # In real adapt-skill the user's answer or fallback is used.
        replacement = fallback if fallback else ""
        adapted = adapted.replace(find, replacement)

    # Check script_hints: verify referenced paths exist in the skill directory
    skill_dir = Path(skill_path).parent
    for sh in script_hints:
        path = sh.get("path")
        treatment = sh.get("treatment")
        if not path:
            problems.append(f"script_hint: missing `path:` field")
            continue
        full = skill_dir / path
        exists = full.exists()
        if not exists:
            problems.append(f"script_hint path '{path}': NOT FOUND in skill dir {skill_dir}")
        if treatment not in ("PARAMETERIZE", "REGENERATE-PER-USER", "DROP"):
            problems.append(f"script_hint '{path}': unknown treatment '{treatment}'")

    return adapted, problems

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: dry-run-adapt-skill.py <SKILL.md path>", file=sys.stderr)
        sys.exit(2)
    skill_path = sys.argv[1]
    adapted, problems = validate_and_apply(skill_path)
    print(adapted)
    print("\n=== Problems ===", file=sys.stderr)
    if not problems:
        print("(none)", file=sys.stderr)
    else:
        for p in problems:
            print(f"  - {p}", file=sys.stderr)
    sys.exit(1 if problems else 0)
