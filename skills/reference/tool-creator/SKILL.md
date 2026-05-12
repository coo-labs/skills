---
name: tool-creator
description: Author a new VADE skill (the Anthropic-recommended primitive for slash-invoked workflows and reusable agent playbooks). Walks the operator through capability description → inventory check → frontmatter choice → draft → operator review → adversarial-auditor pass → TOOLS.md registration → PR. v1 emits a single `.claude/skills/<name>/SKILL.md` per invocation; subagents (`.claude/agents/`), personas (`coo/personas/`), hooks (settings.json), and compound primitives are deferred to v2+. Use when externalizing a recurring pattern or session-end-noticed capability into a `/foo` skill or auto-discoverable skill. Do NOT invoke for one-off scripts, in-place file edits, or refactors outside v1's primitive scope.
disable-model-invocation: true
---

# tool-creator — author a new VADE skill

VADE's primitive for capability authoring. Replaces the ad-hoc
"write a SKILL.md, hope the frontmatter is right, remember to update
TOOLS.md, run auditors, open PR" sequence with a staged-checkpoint
flow that captures intent, inventories duplicates, decides
frontmatter from a documented decision tree, and registers the new
skill consistently.

Authoritative spec for the underlying primitives is Anthropic's
docs (https://code.claude.com/docs/en/skills). This skill encodes
VADE-specific authoring discipline on top: TOOLS.md row format,
adversarial-auditor convention, and the staged-checkpoint workflow.
When this skill and Anthropic's docs disagree on primitive shape,
the docs win — open an issue and update this skill.

> **Reference skill.** The pattern (staged-checkpoint skill
> authoring — Phase 1 draft with inventory check, frontmatter
> decision-tree, and a deliberate stop; Phase 2 finalize with
> two adversarial auditors in parallel, a tools-registry row,
> and a PR) is portable; the substrate references (the five
> `vade-app/*` repos, `coo/parallel_instance_protocol.md` §8 for
> sub-agent dispatch discipline, `coo/personas/`, governance
> memos MEMO-2026-04-22-01 / -11-10 / -11-14 / -28-3ca3 /
> -22-04, MEMO-2026-04-20-01's subject+emancipatory double
> clause, the `TOOLS.md` row schema, the `safety-auditor` /
> `emancipatory-auditor` agent definitions) ship verbatim as the
> VADE worked example. The four refactor patterns (rename / extract
> + delegate / refactor in place / abort) and the staged-checkpoint
> discipline are the load-bearing parts; the specific governance
> memos are local. Read [`../README.md`](../README.md) for the
> fork-and-adapt path.

## When to use this skill

Invoke when:

- Operator wants to externalize a recurring session pattern as a
  reusable `/foo` slash-skill (the briefing 010 use case).
- A queued issue names a new skill to author (e.g.,
  vade-coo-memory#312 `/play-mode`, #313 `/post-discussion`).
- An existing tool is being refactored — pass the existing path as
  `$refactor_target` so the inventory step reads it for context.
- End-of-session reflection (vade-coo-memory#323 follow-up surface)
  identifies a pattern worth packaging.

Don't invoke for:

- One-off scripts that won't be reused (just write the script).
- Edits to existing skills that don't change frontmatter shape
  (use Edit on the SKILL.md directly).
- Authoring sub-agents (`.claude/agents/<name>.md` — v2 scope),
  personas (`coo/personas/<name>.md` — v3 scope), or hooks
  (settings.json — v4 scope). v1 is **skill-only**.

## Inputs

The skill expects (operator-supplied, prompted if absent):

- **`capability_description`** — One-line of what the new tool
  does. Required.
- **`invocation_surface`** — One of:
  - `explicit` — operator types `/foo` to invoke
    (`disable-model-invocation: true` in frontmatter)
  - `auto-discoverable` — Claude weighs the skill against a task
    via its `description` (`disable-model-invocation` unset)
  - `forked-context` — runs in isolated subagent context
    (`context: fork`)
- **`refactor_target`** — Optional path to an existing
  command/skill being refactored. If non-empty, inventory step
  reads existing files for context and the draft step proposes a
  refactor diff rather than a fresh file.
- **`first_test_case`** — Concrete invocation that should work
  after the skill ships. Used in the falsifier section of the PR
  body.

## Procedure

### Phase 1 — Draft (default invocation)

#### Step 1.1 — Resolve roots and capture intent

```bash
COO="$(for c in "${COO_MEMORY_DIR:-}" "${CLAUDE_PROJECT_DIR:-}" "${CLAUDE_PROJECT_DIR:-}/../vade-coo-memory" "$HOME/GitHub/vade-app/vade-coo-memory" "/home/user/vade-coo-memory"; do [ -n "$c" ] && [ -f "$c/coo/memo_protocol.md" ] && { cd "$c" && pwd -P; break; }; done)"
[ -n "$COO" ] || { echo "tool-creator: could not find vade-coo-memory data root"; exit 1; }
```

Read or prompt for the four inputs above. If `$refactor_target`
is non-empty, also Read the existing file(s) and capture the
existing frontmatter shape.

#### Step 1.2 — Inventory (parallel sub-agent)

Spawn one Explore sub-agent in a single message. Brief is in
`templates/inventory-brief.md`. The agent inspects all
`.claude/skills/` directories across the three vade-app repos
(vade-coo-memory, vade-runtime, vade-core) plus `.claude/commands/`
in vade-coo-memory (legacy, but still in use). It reports:

- **Exact-name collision** — a skill or command with the same
  name already exists. STOP and surface to operator. Default
  resolution: refactor the existing tool (set
  `$refactor_target`).
- **Near-duplicate** — a skill whose description overlaps
  significantly. SURFACE to operator with
  "duplicate?" branching question. Operator chooses: proceed,
  refactor existing, or merge.
- **No collision** — proceed.

Forbidden in the agent prompt: re-Reading CLAUDE.md, identity
files, `coo/episodic_memory.md`, this SKILL.md. Inline pre-fetched
context in the prompt per `coo/parallel_instance_protocol.md` §8.
Cap output ≤300 words.

#### Step 1.2.5 — Refactor patterns (canonical inventory resolutions)

When the inventory step surfaces a collision or near-duplicate, four
canonical resolutions are available. Pick the one that fits before
proceeding to Step 1.3; surface the choice to the operator with the
inventory finding.

- **Path A — Rename and proceed.** The new skill's capability is
  genuinely distinct; rename to disambiguate (`/foo-explorer` vs
  the colliding `/foo`). Inventory becomes a no-op for the renamed
  draft.
- **Path B — Extract → delegate (the "shared helper" pattern).**
  Two consumers do overlapping work via copy-paste or near-paste.
  Extract the overlap into a single helper script (cross-consumer
  helpers live at `.claude/_lib/<name>.sh`; single-consumer helpers
  live in the skill's own `scripts/<name>.sh`); both consumers
  delegate to it. The new skill ships the helper alongside its
  SKILL.md; the existing consumer is refactored to delegate. **This
  is the pattern the `/post-discussion` skill set as precedent on
  2026-04-30** (vade-coo-memory#313): inventory found
  `day-overview --post` doing the same GraphQL mutation; the
  resolution was to extract `post-discussion.sh`, point both
  consumers at it, and ship the new skill as the canonical
  invocation surface. Set `$refactor_target` on the existing
  consumer so the inventory step's output captures the
  cross-consumer scope; populate `$secondary_targets` (when v1.1
  lands) with the additional files this run will edit.
- **Path C — Refactor in place (no extraction).** The collision is
  exact and the new "skill" is actually a revision of the existing
  one (e.g., a v2 of `/foo` with a new procedure). Set
  `$refactor_target` to the existing skill's path; produce a diff
  rather than a fresh write. No helper extraction; one consumer.
- **Path D — Abort.** The capability already exists in a form the
  operator hadn't realized. Don't ship; close the inventory finding
  with a note pointing to the existing skill.

The operator decides which path applies based on the inventory
report; the skill's job is to surface the choice clearly, not to
auto-pick. Path B is the load-bearing one to remember — extracting
shared helpers prevents the drift class where two consumers diverge
in their copy-paste of the same logic. Cross-references:
vade-coo-memory#313 (precedent), vade-coo-memory#322 (this v1.1
candidate, surfaced 2026-04-30T22:08), and `coo/personas/exec-mode
-retrospectives/2026-04-30_post-discussion-prototype.md` (the
prototype run that named the pattern).

#### Step 1.3 — Decide frontmatter

Walk the decision tree in §"Decision tree" below using the
operator's `$invocation_surface` and capability characteristics.
Output the chosen frontmatter YAML. Confirm with operator before
writing.

The three primary frontmatter variants live as templates under
`templates/`:

- `templates/explicit-invocation-skill.md` —
  `disable-model-invocation: true`, manual `/foo` invocation.
- `templates/auto-discoverable-skill.md` — rich `description` for
  Claude's delegation logic; Claude can propose the skill when
  the task matches.
- `templates/forked-context-skill.md` — `context: fork` for
  skills that should run in isolated subagent context (e.g.,
  long-running research tasks that would flood main context).

Read the template that matches `$invocation_surface`. Substitute
the operator's `name`, `description`, and any tool-access
constraints.

#### Step 1.4 — Draft

Create the directory `vade-coo-memory/.claude/skills/<name>/`
and write `SKILL.md` from the chosen template. If supporting
files are needed (templates, helper scripts, prompt files),
write them under the same directory.

If `$refactor_target` is non-empty: instead of a fresh write,
produce a diff against the existing file(s). The operator
applies the diff after review.

#### Step 1.5 — Stop

Return to operator with a summary:

- Files drafted / diff produced (paths + line counts)
- Frontmatter chosen (one-line)
- Inventory results (collisions, near-duplicates, none)
- Next step: review the draft, adjust naming / frontmatter /
  body as needed, then run `/tool-creator --finalize <name>`.

**Do NOT** run auditors, write to TOOLS.md, or open a PR in
Phase 1. Tool authoring is iterative; the operator may adjust
naming, predicate clarity, or tool-access constraints before
finalizing.

### Phase 2 — Finalize (`/tool-creator --finalize <name>`)

Phase 2 runs only after the operator has reviewed and adjusted
the Phase 1 draft. Re-runs are fine; the operator can finalize
multiple times if auditor findings require iteration.

**Spend hygiene:** each `--finalize` run spawns two adversarial
auditor sub-agents in parallel. Address all BLOCK findings before
re-running rather than iterating freely — repeated cycles
multiply token cost against the $500/mo cap (MEMO-2026-04-28-3ca3).

#### Step 2.1 — Adversarial auditors (parallel)

Spawn two sub-agents in a single message: `safety-auditor`
and `emancipatory-auditor` per VADE convention. Each reads the
current `SKILL.md` (post-operator-review) and supporting files;
each returns a structured report.

Each auditor prompt MUST follow `coo/parallel_instance_protocol.md`
§8 inline: pre-fetched context paragraph (the new skill's
purpose, files in scope), explicit `Do NOT re-Read` list (e.g.,
`CLAUDE.md`, `identity/*`, `coo/episodic_memory.md`,
`parallel_instance_protocol.md`), and output cap ≤500 words.
The agent definitions in `.claude/agents/` carry their own
discipline; the orchestrating skill asserts the §8 constraints
inline so they bind regardless of agent-definition drift.

- **safety-auditor** checks against governance memos
  (MEMO-2026-04-22-01 PAT discipline, MEMO-2026-04-11-10 Mem0
  content rule, MEMO-2026-04-11-14 path scope, MEMO-2026-04-28-3ca3
  spend cap, MEMO-2026-04-22-04 attribution). PASS / PASS-WITH-NOTES /
  BLOCK.
- **emancipatory-auditor** checks against MEMO-2026-04-20-01
  subject+emancipatory double-clause. Scores Subject:0–2,
  Emancipatory:0–2. Anything 2/0 or 0/2 BLOCKS.

Fold findings inline if PASS-WITH-NOTES. If either BLOCKs, stop
and surface to operator; iterate the draft and re-finalize.

#### Step 2.2 — Register in TOOLS.md

Append a row to the §3 Skills section of `TOOLS.md` (current
location; if Ven moves it to repo root, update this skill).
Default values for a fresh row:

- `wiring_tier`: `skill`
- `decisions_to_invoke`: `2` (recognize trigger + select skill)
- `rule_class`: `mechanical` (most skills) or
  `design-time-structural` (skills that fire during epic phases,
  not per session — e.g., `skill-creator`)
- `predicate_clarity`: `predicate` (clear trigger) or
  `always-do-implicit-bound` / `always-do-false-positive-class`
- `rediscovery_cost`: `0` (just added)
- `evidence_of_use`: `0` (no log-grep history yet)
- `last_updated`: today's UTC date
- `flags`: empty (nightly review will populate)

Bump the per-category count in §"Cross-cutting summary".

#### Step 2.3 — Cross-references

Update CLAUDE.md cross-reference ONLY if the new skill is in
the boot reading order (rare; most skills don't qualify). Most
skills are discoverable via TOOLS.md and Anthropic's skill
discovery — explicit boot-reading-order placement is reserved
for skills that bind every session.

#### Step 2.4 — Open PR

```bash
GH_TOKEN="$GITHUB_MCP_PAT" gh pr create \
  --repo vade-app/vade-coo-memory \
  --base main \
  --head <current-branch> \
  --title "skill: /<name> — <one-line capability>" \
  --body-file /tmp/tool-creator-pr-body.md
```

Use `--body-file` (not `--body`) when the body mentions any
literal env-var name like `$GITHUB_MCP_PAT` or `$MEM0_API_KEY` —
the bash-token-guard pattern-matches the literal token names
even with backslash escapes (exec-mode v2 retro lesson).

PR body sections:

- **Summary** — what the skill does (3-5 lines)
- **Files changed** — paths + line counts
- **Frontmatter chosen** — and reasoning
- **Adversarial-auditor reports** — both findings, folded or
  acknowledged
- **First test case** — operator-supplied; what should work on
  invocation
- **Verification plan** — how to confirm the skill works after
  merge
- **Out of scope** — what this PR explicitly does NOT do
  (especially relevant for refactor PRs)

## Decision tree — frontmatter branches

When the operator says... | Choose this template | Why
:---|:---|:---
"User types `/foo`" — explicit deliberate authoring action | `explicit-invocation-skill.md` (`disable-model-invocation: true`) | Auto-invocation would surprise; description out of context keeps Claude focused
"Claude should propose this when the task matches" — discoverable knowledge skill | `auto-discoverable-skill.md` (no `disable-model-invocation`) | Description in context lets Claude weigh the skill as a delegation candidate
"Long-running research / task that would flood main context" | `forked-context-skill.md` (`context: fork`) | Subagent isolation preserves main-context for decisions
"Skill that mostly references vendored docs" — like `cf-wrangler`, `tldraw-docs` | `auto-discoverable-skill.md` with rich `description` + `when_to_use` | Claude weighs against task; operator doesn't usually need to remember the skill name

Tool-access decisions (`allowed-tools` field — optional):

- **Minimal tools** — list only what the body actually invokes;
  honors least-privilege. Use this default.
- **Broad tools** — omit `allowed-tools` entirely; skill inherits
  parent context's tool access. Use only when the skill's tool
  needs are dynamic / not knowable in advance.

Argument decisions (`arguments` field — optional, named-positional):

- **No arguments** — skill body is fully self-contained. Most
  skills.
- **Positional** — `$ARGUMENTS` substituted into body at runtime.
  Use for simple parameter passes.
- **Named** — `arguments: {name1: ..., name2: ...}` for explicit
  multi-input skills.

## Templates

The three frontmatter templates live alongside this SKILL.md:

- `templates/explicit-invocation-skill.md` — for `/foo` deliberate
  authoring actions (e.g., `/post-discussion`, `/memo`).
- `templates/auto-discoverable-skill.md` — for knowledge skills
  Claude should propose (e.g., `tldraw-docs`, `claude-api`).
- `templates/forked-context-skill.md` — for isolated-context
  research / long-task skills.
- `templates/inventory-brief.md` — sub-agent prompt for Step 1.2.

Each template includes commented frontmatter, an example body
skeleton, and notes on what to substitute.

## TOOLS.md row format (reference)

The full schema is in `TOOLS.md` §"Rubric reference". A
newly-added skill row has these defaults; fill them per your
skill's actual shape:

```
| <name> | `vade-coo-memory/.claude/skills/<name>/SKILL.md` | <one-line purpose> | skill | 2 | mechanical | predicate | 0 | 0 | <YYYY-MM-DD> | |
```

Place it in §3 Skills, in alphabetical-ish order with the other
skills. Bump §"Cross-cutting summary" count.

## Failure modes

- **Inventory finds an exact-name collision.** STOP at Step 1.2.
  Operator decides: rename, refactor existing (set
  `$refactor_target`), or abort.
- **Inventory finds a near-duplicate.** SURFACE to operator with
  the duplicate's path + description. Operator decides whether
  the new skill is genuinely distinct or whether to merge /
  refactor.
- **safety-auditor BLOCKs in Phase 2.** Stop. Surface BLOCK
  reasoning to operator. Iterate the draft (revise the offending
  body section) and re-run `--finalize`.
- **emancipatory-auditor BLOCKs (2/0 or 0/2 score).** Stop. The
  skill fails the subject-AND-emancipatory double-clause
  (MEMO-2026-04-20-01). Iterate; re-finalize.
- **`gh pr create` rejects body for env-var token.** Switch to
  `--body-file /tmp/...` (exec-mode v2 retro lesson; this should
  be the default in this skill — surface as a blocker if it
  happens).
- **Operator wants to skip Phase 2 finalization.** That's fine —
  Phase 1 produces a usable draft. The operator can manually
  open a PR or hold the draft for review. Phase 2 is an
  affordance, not a gate.

## Out of scope for v1

These are deferred to later versions:

- **Subagents** (`.claude/agents/<name>.md`) — different file
  shape; v2 work.
- **Personas** (`coo/personas/<name>.md`) — vade-specific mode
  overlay; v3 work. The persona-vs-skill question is real for
  refactors like vade-coo-memory#321 (exec-mode skill refactor)
  but v1 doesn't yet handle it.
- **Hooks** (settings.json) and compound primitives like
  triple-wired skill+command+hook (e.g., memo-sync) — v4 work.
- **Migrating existing command+skill pairs to skill-only.**
  Anthropic's docs say `.claude/commands/<name>.md` is now legacy
  (skills are the recommended primitive), but vade has 11
  commands across the three repos. Migration is its own sweep,
  out of /tool-creator v1's job. File a follow-up issue once v1
  ships.
- **Auto-invocation from session signals.** End-of-session
  externalization (#323) is the natural home for that; once
  /tool-creator v1 binds, #323 can dispatch it.

## Canonical source

```text
vade-coo-memory/.claude/skills/tool-creator/SKILL.md (this file)
vade-coo-memory/.claude/skills/tool-creator/templates/ (templates)
vade-coo-memory/TOOLS.md (registration target)
vade-coo-memory/.claude/agents/safety-auditor.md (Phase 2 auditor)
vade-coo-memory/.claude/agents/emancipatory-auditor.md (Phase 2 auditor)
vade-coo-memory/coo/parallel_instance_protocol.md §8 (sub-agent dispatch)
https://code.claude.com/docs/en/skills (Anthropic spec — SOT for primitive shape)
```

When this skill and Anthropic's docs disagree on primitive
shape, the docs win — open an issue and update this skill;
don't drift the spec.

## Cross-references

- vade-coo-memory#322 (proposal)
- vade-coo-memory#326 (briefing 010 — design substrate)
- vade-coo-memory#321 (exec-mode skill refactor; v3 candidate)
- vade-coo-memory#323 (end-of-session externalization; downstream
  consumer once v1 binds)
- vade-coo-memory#312 (`/play-mode`) and #313 (`/post-discussion`)
  — queued use cases
- MEMO-2026-04-20-01 (subject+emancipatory double-clause; gates
  emancipatory-auditor)
- MEMO-2026-04-22-01 (PAT discipline; gates safety-auditor)
- MEMO-2026-04-26-07 (adoption discipline; informs the
  TOOLS.md-row registration step)
- MEMO-2026-04-28-4umz (issue/PR ruling-shape; informs PR-body
  shape in Step 2.4)

# Setup hints

*Read by [`adapt-skill`](../../adapt-skill/SKILL.md). Stripped from
the adapted output. Schema: [`adapt-skill/SCHEMA.md`](../../adapt-skill/SCHEMA.md).
The auditor pair (safety-auditor, emancipatory-auditor) is the
hardest part to adapt — without configured governance rules, the
auditors produce vacuous PASS verdicts. The graceful degradation
collapses Phase 2 to a self-review checklist when no rules are
supplied.*

```yaml
setup_hints:
  - key: skills_root
    kind: PROMPT
    question: "Where do new skills get written in your project? (Examples: .claude/skills/, vade-coo-memory/.claude/skills/.) Provide the directory path that will be the parent of <skill-name>/SKILL.md."
    find: "vade-coo-memory/.claude/skills/<name>/"
    fallback: ".claude/skills/<name>/"

  - key: skills_root_short
    kind: PROMPT
    question: "Same skills root without the placeholder (used in other body locations). Provide just the directory path."
    find: "vade-coo-memory/.claude/skills/"
    fallback: ".claude/skills/"

  - key: repo_roots_for_inventory
    kind: PROMPT
    question: "List the repo paths the inventory sub-agent should scan for existing skills (comma-separated absolute paths or repo names). VADE scans three: vade-coo-memory, vade-runtime, vade-core."
    find: "vade-coo-memory, vade-runtime, vade-core"
    fallback: "<your primary repo>"

  - key: legacy_commands_scan
    kind: OPTIONAL
    question: "Do you have legacy .claude/commands/ files the inventory should also scan? Skip if you're skill-only."
    find: " plus `.claude/commands/`\nin vade-coo-memory (legacy, but still in use)"
    fallback: ""

  - key: data_root_resolution
    kind: OPTIONAL
    question: "Step 1.1 has a COO data-root resolution block (sentinel-file discovery). Skip to replace with a generic 'cd to repo root' instruction."
    find_unique: true
    find: |-
      COO="$(for c in "${COO_MEMORY_DIR:-}" "${CLAUDE_PROJECT_DIR:-}" "${CLAUDE_PROJECT_DIR:-}/../vade-coo-memory" "$HOME/GitHub/vade-app/vade-coo-memory" "/home/user/vade-coo-memory"; do [ -n "$c" ] && [ -f "$c/coo/memo_protocol.md" ] && { cd "$c" && pwd -P; break; }; done)"
      [ -n "$COO" ] || { echo "tool-creator: could not find vade-coo-memory data root"; exit 1; }
    fallback: |-
      COO="$(git rev-parse --show-toplevel 2>/dev/null)"
      [ -n "$COO" ] || { echo "tool-creator: run from inside a git repo"; exit 1; }

  - key: tools_registry_path
    kind: OPTIONAL
    question: "Path to your tools registry file (like VADE's TOOLS.md)? Provide the path. Skip to drop the registration step entirely — Phase 2.2 becomes a no-op."
    find: "TOOLS.md"
    fallback: "<no-tools-registry>"

  - key: tools_registry_schema_block
    kind: OPTIONAL
    question: "VADE's tools registry has a 7-field row schema (wiring_tier, decisions_to_invoke, rule_class, predicate_clarity, rediscovery_cost, evidence_of_use, last_updated). Skip to keep this default schema in the adapted skill; replace by editing the body after install if your registry differs."
    find_unique: true
    find: |-
      - `wiring_tier`: `skill`
      - `decisions_to_invoke`: `2` (recognize trigger + select skill)
      - `rule_class`: `mechanical` (most skills) or
        `design-time-structural` (skills that fire during epic phases,
        not per session — e.g., `skill-creator`)
      - `predicate_clarity`: `predicate` (clear trigger) or
        `always-do-implicit-bound` / `always-do-false-positive-class`
      - `rediscovery_cost`: `0` (just added)
      - `evidence_of_use`: `0` (no log-grep history yet)
      - `last_updated`: today's UTC date
      - `flags`: empty (nightly review will populate)
    fallback: |-
      - <field 1>: <your registry's first column>
      - <field 2>: <your registry's second column>
      - ... (edit this block to match your tools registry's row schema)

  - key: safety_governance_rules
    kind: PROMPT
    min_count: 2
    severity: warning
    question: "List your project's governance rules the safety-auditor should enforce. Provide as 'rule-id | source | what-it-forbids' triples, one per line. Minimum 2; below that, the adapted skill drops the safety-auditor (degradation path)."
    find: "(MEMO-2026-04-22-01 PAT discipline, MEMO-2026-04-11-10 Mem0\n  content rule, MEMO-2026-04-11-14 path scope, MEMO-2026-04-28-3ca3\n  spend cap, MEMO-2026-04-22-04 attribution)"
    fallback: "(your governance rule sources — author at least 2 and re-adapt)"

  - key: emancipatory_principle
    kind: OPTIONAL
    question: "Do you want the emancipatory-auditor (adoption-test gate)? It enforces: artifacts must (a) grow author capability AND (b) be installable by a peer without inherited context. Skip if your project doesn't share this double-clause."
    find: "MEMO-2026-04-20-01\n  subject+emancipatory double-clause"
    fallback: "your project's quality-gate criterion"

  - key: spend_cap
    kind: OPTIONAL
    question: "Token/spend cap that governs Phase 2 iteration count? (VADE: $500/mo per MEMO-2026-04-28-3ca3.) Skip to drop the spend-hygiene note."
    find: "$500/mo cap (MEMO-2026-04-28-3ca3)"
    fallback: "your project's spend cap"

  - key: target_repo
    kind: PROMPT
    question: "GitHub repo for skill PRs? (owner/repo format.)"
    find: "vade-app/vade-coo-memory"
    fallback: "<owner>/<repo>"

  - key: github_token_env
    kind: OPTIONAL
    question: "Environment variable for GitHub PAT? Skip for gh default."
    find: "GH_TOKEN=\"$GITHUB_MCP_PAT\" "
    fallback: ""

  - key: parallel_protocol_ref
    kind: OPTIONAL
    question: "Path to your sub-agent dispatch discipline doc (VADE: coo/parallel_instance_protocol.md §8)? Skip to inline the rule."
    find: "`coo/parallel_instance_protocol.md` §8"
    fallback: "your project's sub-agent dispatch discipline (or inline the rule: pre-fetch context, forbid re-reading enumerated files, cap output, structured schema)"

  - key: precedent_retrospective
    kind: OPTIONAL
    question: "Path to a retrospective documenting a pattern-precedent for this skill? (VADE: coo/personas/exec-mode-retrospectives/2026-04-30_post-discussion-prototype.md.) Skip if you have no such precedent."
    find: "`coo/personas/exec-mode\n-retrospectives/2026-04-30_post-discussion-prototype.md`"
    fallback: "(no precedent retrospective)"

  - key: boot_order_cross_ref
    kind: OPTIONAL
    question: "If your project has a boot-order/reading-list file (VADE: CLAUDE.md), Step 2.3 may need to update it. Skip if you have no such file — Step 2.3 becomes a no-op."
    find: "Update CLAUDE.md cross-reference"
    fallback: "(No boot-order file configured — Step 2.3 is a no-op.) Update CLAUDE.md cross-reference"

  - key: out_of_scope_section
    kind: OPTIONAL
    question: "Skip unless you want to keep the VADE-specific 'Out of scope for v1' references (vade-coo-memory#321, #312, #313, named legacy commands)."
    find_unique: true
    find: |
      - **Personas** (`coo/personas/<name>.md`) — vade-specific mode
        overlay; v3 work. The persona-vs-skill question is real for
        refactors like vade-coo-memory#321 (exec-mode skill refactor)
        but v1 doesn't yet handle it.
      - **Hooks** (settings.json) and compound primitives like
        triple-wired skill+command+hook (e.g., memo-sync) — v4 work.
      - **Migrating existing command+skill pairs to skill-only.**
        Anthropic's docs say `.claude/commands/<name>.md` is now legacy
        (skills are the recommended primitive), but vade has 11
        commands across the three repos. Migration is its own sweep,
        out of /tool-creator v1's job. File a follow-up issue once v1
        ships.
      - **Auto-invocation from session signals.** End-of-session
        externalization (#323) is the natural home for that; once
        /tool-creator v1 binds, #323 can dispatch it.
    fallback: |
      - **Hooks and compound primitives** — different shape; deferred.
      - **Migrating legacy commands to skills** — its own sweep; deferred.
      - **Auto-invocation from session signals** — deferred.

requires:
  - kind: agent
    name: "safety-auditor (Phase 2 adversarial)"
    detect: "test -f \"$(git rev-parse --show-toplevel 2>/dev/null)\"/.claude/agents/safety-auditor.md || test -f \"$HOME/.claude/agents/safety-auditor.md\""
    severity: warning
    install_hint: "Phase 2 dispatches safety-auditor as one of two parallel auditors. Adapt via /adapt-skill safety-auditor before invoking /tool-creator. If absent, Phase 2 collapses to self-review per the degradation."

  - kind: agent
    name: "emancipatory-auditor (Phase 2 adversarial)"
    detect: "test -f \"$(git rev-parse --show-toplevel 2>/dev/null)\"/.claude/agents/emancipatory-auditor.md || test -f \"$HOME/.claude/agents/emancipatory-auditor.md\""
    severity: warning
    install_hint: "Phase 2 dispatches emancipatory-auditor alongside safety-auditor. The emancipatory clause is philosophically coupled — adapt via /adapt-skill emancipatory-auditor only if your project shares the double-clause."

script_hints:
  - path: templates/inventory-brief.md
    treatment: REGENERATE-PER-USER
    rationale: "Hardcodes three vade-app repo paths and the .claude/commands/ legacy scan. Skeleton emitted with TODO comments for the repo-roots list and the registry-file path (or registry-absent flag)."

  - path: templates/explicit-invocation-skill.md
    treatment: PARAMETERIZE
    rationale: "Frontmatter structure ports verbatim; substitution covers worked-example references and any VADE-specific cross-refs."

  - path: templates/auto-discoverable-skill.md
    treatment: PARAMETERIZE
    rationale: "Same as explicit-invocation; replace memo-search worked example with a user-supplied example or leave as VADE-historical context."

  - path: templates/forked-context-skill.md
    treatment: PARAMETERIZE
    rationale: "Drop the vade-coo-memory#322 follow-up reference; the rest of the caveat documentation is substrate-agnostic."

degradations:
  - when: "safety_governance_rules below min_count"
    body_replace:
      find: "the auditor pair runs in parallel via the Task tool"
      with: "Phase 2 runs a single self-review checklist (no auditor pair configured — safety_governance_rules was below min_count at adapt-skill time)"
    note: "Adapted with insufficient governance rules — Phase 2 collapsed to self-review. Author your safety rules (minimum 2) and re-run /adapt-skill tool-creator to restore the auditor pair."

  - when: "emancipatory_principle fallback applied"
    body_replace:
      find: "emancipatory-auditor"
      with: "(emancipatory-auditor not configured — your project opted out of the double-clause)"
    note: "Adapted without the emancipatory-auditor — Phase 2 runs safety-auditor only (or self-review if safety rules are also empty)."
```
