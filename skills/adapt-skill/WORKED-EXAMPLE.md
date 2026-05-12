# Worked example: adapting `status-check`

This walks through `/adapt-skill status-check` for a hypothetical
user whose project is a research group's shared notebook repo.

`status-check` is the simplest reference skill (portability tier:
drop-in), so the example focuses on the meta-skill's mechanics
rather than on heavy rewrite work. For a harder example (heavy
substitution, bundled scripts, philosophical gate), read the
hints in `skills/reference/day-overview/` or
`agents/reference/emancipatory-auditor.md`.

## The source

`skills/reference/status-check/SKILL.md` references three things
that won't resolve in a foreign repo:

- The authoritative spec at `coo/status_check_template.md` v0.1
  (used as a tie-breaker reference).
- Mem0 by name, in the governance section ("Must not auto-write
  to Mem0").
- A "Tier-2 content" governance concept.

Its `# Setup hints` section (added in this same PR — see
`skills/reference/status-check/SKILL.md` after this PR lands) is
small:

```yaml
setup_hints:
  - key: spec_template_path
    kind: OPTIONAL
    question: "Do you have a local spec or template file that should be the authoritative tie-breaker for this skill? Provide the path, or skip."
    find: "coo/status_check_template.md"
    fallback: ""

  - key: memory_layer_name
    kind: OPTIONAL
    question: "What persistent memory layer does your project use? (e.g. Mem0, custom store, 'none'.)"
    find: "Must not auto-write to Mem0"
    fallback: "Must not write to any persistent memory layer"

  - key: content_tier_term
    kind: OPTIONAL
    question: "Does your project have a content-tier or sensitivity classification term? (VADE uses 'Tier-2'.) Provide the term or skip."
    find: "Must not leak Tier-2 content"
    fallback: "Must not surface confidential project content"
```

(There are also a few cross-reference lines — `MEMO-2026-04-11-08`,
etc. — but the `# Setup hints` stripping handles those because
they live in the cross-references section AFTER the hints H1.
Wait — that's the opposite order. See the schema's "What
`adapt-skill` strips" section. The cross-references for
`status-check` are deliberately placed **before** the hints
section, so they survive. The hints stripping only removes the
hints block itself, not all trailing content.)

## The interview

The user runs:

```sh
/adapt-skill status-check
```

`adapt-skill` reads the source, parses the hints, and asks (one
`AskUserQuestion` batch, three questions):

1. **spec_template_path** — User answers: "skip" (no local spec
   file).
2. **memory_layer_name** — User answers: "We use Obsidian and
   plain markdown notes; no programmatic memory layer."
3. **content_tier_term** — User answers: "skip" (no formal
   classification).

The substitution map is built:

| key | find | replace |
|---|---|---|
| spec_template_path | `coo/status_check_template.md` | `""` (fallback) |
| memory_layer_name | `Must not auto-write to Mem0` | `Must not write to any persistent memory layer` (fallback — user skipped) |
| content_tier_term | `Must not leak Tier-2 content` | `Must not surface confidential project content` (fallback) |

(The skip on `spec_template_path` leaves the surrounding paragraph
referencing an empty string; the meta-skill flags this in the
setup report as a candidate for body-level cleanup the user may
want to do post-install.)

## The output

`adapt-skill` writes to `./.claude/skills/status-check/SKILL.md`:

- Frontmatter preserved verbatim.
- Body lines about the authoritative spec at
  `coo/status_check_template.md` now reference `""` (an obvious
  marker for the user to clean up).
- The Governance section's three rules now read:
  - "Must not write to any persistent memory layer" (was: Mem0)
  - "Must not surface confidential project content" (was:
    Tier-2)
  - "Emancipatory double-clause: works for COO and non-COO agents
    without setup" — **unchanged** because no hint covers this
    line, and the meta-skill doesn't invent substitutions. The
    setup report surfaces "COO" / "non-COO" as a candidate
    follow-up.
- The `# Setup hints` section is stripped.
- The `## Cross-references` section before the hints block is
  preserved (with `vade-coo-memory#NNN` references intact — a
  setup-report candidate cleanup item).

## The setup report

```
Installed: ./.claude/skills/status-check/SKILL.md (was: skills/reference/status-check/SKILL.md)

Substitutions applied:
  spec_template_path     fallback (user skipped) — body contains an empty string at the prior path location; consider cleanup
  memory_layer_name      fallback (user skipped) — generic phrasing applied
  content_tier_term      fallback (user skipped) — generic phrasing applied

Not covered by hints (candidate follow-up):
  - "COO" and "non-COO" agent references in body
  - vade-coo-memory#NNN cross-references in `## Cross-references`
  - The emancipatory-clause memo citation in the Governance section

Next: run /status-check to test. Edit the installed SKILL.md directly to clean up the candidate-follow-up items.
```

## What this example demonstrates

- The meta-skill is **conservative**: it substitutes only what the
  hints declare. It does not try to be clever about other VADE-
  specific bits.
- The setup report surfaces candidate cleanups the user may want
  to do — but the meta-skill doesn't gate on them. The adapted
  skill is functional even with VADE cross-refs left intact;
  those refs are inert in a foreign substrate.
- Skip is a first-class answer. The fallback handles it.
- The `# Setup hints` section is stripped — the installed skill
  doesn't carry meta about how it was adapted.

## What a harder example would add

For `day-overview` (next-hardest port):

- A `requires:` block flagging the `post-discussion` helper.
- A `script_hints:` block marking `scripts/day-overview.sh` as
  `REGENERATE-PER-USER` — the meta-skill emits a skeleton with
  TODO comments rather than a working script.
- Many more substitutions (five repo names, integrity-check path,
  memo index path, etc.).
- A larger setup report flagging the regenerated script as
  needing per-user authoring.

For `emancipatory-auditor` (hardest port):

- A `philosophical_gate:` that asks the buy-in question first.
- On "no", abort with a recommendation to author from the pattern
  README. No partial file.

Both are documented in the schema. The mechanics are the same;
the surface area is larger.
