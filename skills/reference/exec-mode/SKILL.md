---
name: exec-mode
description: "Load the executive persona for sessions where the natural shape is delegate exploration → preserve main-context for decisions and action → reflect on state and priorities. Three modes fit: sweep/cleanup, strategic reflection, or both. Reads `coo/personas/exec-mode.md` (the persona doctrine, including its discipline rollup folded from prior retrospectives with per-rule provenance), adopts the discipline, then asks user for scope. Invoke as `/exec-mode --revise-persona` to enter persona-revision mode (re-introduces read-all-retros + plan-mode REQUIRED + adversarial-auditor gates per the persona's `Persona-revision discipline` section). Use when starting a consolidation pass on open PRs/issues, when reflecting on substrate state and priorities, or when revising the persona itself. Don't invoke for narrow code-task work, single-PR review, or anything where standard COO discipline already fits — exec-mode is bias-overlay for broad-scope sessions, not a wrapper around the standard COO."
disable-model-invocation: true
argument-hint: optional scope hint, or --revise-persona
metadata:
  type: role
  vendoring: custom
---

# exec-mode — load the executive persona

Executive bias-overlay for broad-scope sessions: sweep/cleanup
across open PRs and issues, strategic reflection on substrate
state and priorities, or combinations. The skill is the invocation
primitive; the persona doctrine lives at `./persona.md`
(originally `coo/personas/exec-mode.md` in the substrate this was
extracted from — adapt to your own project's location) and is
loaded fresh each session. **The persona file wins on any
procedural disagreement.**

> **Reference skill.** This pattern is portable; the substrate
> references in the persona doctrine (project board, CB-* / OG-*
> beliefs, integrity-check probes, VADE memo IDs) are not. Read
> [`../README.md`](../README.md) for the fork-and-adapt path.

## When to use

- Consolidation pass on open PRs/issues across a project's repo
  set (VADE: the five `vade-app/*` repos).
- Strategic reflection on substrate state and ranked priorities
  (no action loop required).
- Revising the persona itself (`--revise-persona` submode).
- Combinations (reflection prompts a next sweep).

Don't invoke for narrow code-task work, single-PR review, or work
that doesn't benefit from delegated parallel-sub-agent exploration.

## Procedure

1. **Standard COO boot.** If the `coo/CLAUDE.md` reading order is
   not yet complete this session, complete it before continuing.
   The persona's discipline expects identity / governance /
   preferences / episodic / lineage substrate to be loaded first.
2. **Load persona doctrine.** Read `coo/personas/exec-mode.md` in
   full. Routine /exec-mode invocations rely on its **Discipline
   rollup** (rule-name index + provenance map). Persona
   retrospectives in `coo/personas/exec-mode-retrospectives/` are
   NOT read at boot in routine mode — only in `--revise-persona`
   mode.
3. **Mode selection.** If `--revise-persona` is in `$ARGUMENTS`,
   jump to the persona file's `## Persona-revision discipline`
   section and follow that procedure (read-all-retros + plan-mode
   REQUIRED + auditor gates). Otherwise continue to step 4.
4. **Synthesize.** State in 2-3 sentences: current discipline as
   you understand it; any pending refinements that affect this run;
   `summary.ok` state in `integrity-check.json` (surface failing
   invariant if degraded).
5. **Ask scope.** Defaults to offer: open PRs across the five
   vade-app repos; open `proj:*` issues; a specific repo / lane /
   cohort; a specific PR/issue list; strategic-reflection-only
   pass (jump to Phase 4). Wait for the user's answer; do not
   auto-detect.

## Failure modes

- **Standard boot was skipped at session start.** Step 1 detects;
  do the boot before continuing.
- **`integrity-check.json` `summary.ok=false`.** Surface the
  failing invariant via `groups.<A–F>.<id>.detail` before swinging.
- **`--revise-persona` invoked without revision intent.** The
  submode is heavyweight; surface the cost and confirm before
  jumping to the submode.
- **Mem0 disconnected at boot.** File-canonical wins per
  MEMO-2026-04-27-01; proceed without Mem0 reachable. End-of-session
  episodic save uses REST fallback per SOP-MEM-001 §5.

## Canonical source

```text
vade-coo-memory/.claude/skills/exec-mode/SKILL.md (this file)
vade-coo-memory/coo/personas/exec-mode.md (persona doctrine — SOT)
vade-coo-memory/coo/personas/exec-mode-retrospectives/ (audit trail)
vade-coo-memory/CLAUDE.md (standard COO boot — substrate)
```

When this skill and the persona file disagree on procedural detail,
the persona file wins.

## Cross-references

- `coo/personas/README.md` — persona-overlay pattern doc
- `coo/parallel_instance_protocol.md` §8 + §8.5 — sub-agent dispatch

$ARGUMENTS

# Setup hints

*Read by [`adapt-skill`](../../adapt-skill/SKILL.md). Stripped from
the adapted output. Schema: [`adapt-skill/SCHEMA.md`](../../adapt-skill/SCHEMA.md).
The persona doctrine file (`persona.md`) is the heart of this
skill; treat its adaptation as the main work, not the SKILL.md.*

```yaml
setup_hints:
  - key: boot_procedure_ref
    kind: PROMPT
    question: "Path to your agent's boot/reading-order file (e.g. CLAUDE.md)? Used in Step 1 of the procedure."
    find: "the `coo/CLAUDE.md` reading order"
    fallback: "your project's boot reading order (if you have one)"

  - key: persona_doctrine_path
    kind: OPTIONAL
    question: "Where will your persona doctrine file live? (Default: ./persona.md alongside this SKILL.md — recommended.) Provide a different path only if you keep persona docs elsewhere."
    find: "`./persona.md`"
    fallback: "`./persona.md`"

  - key: persona_doctrine_path_long
    kind: OPTIONAL
    question: "Same path again, with full prose context — see find string. Skip to leave the VADE worked-example reference."
    find: "(originally `coo/personas/exec-mode.md` in the substrate this was\nextracted from — adapt to your own project's location)"
    fallback: ""

  - key: repo_set_description
    kind: PROMPT
    question: "What's the repo set this exec-mode will sweep across? (Examples: 'the three repos under myorg', 'just this one repo', 'all repos in my GitHub org'.) Used as a default-scope description in Step 5."
    find: "open PRs across the five\n   vade-app repos; open `proj:*` issues"
    fallback: "open PRs across your repo set; open prioritized issues"

  - key: vade_repos_aside
    kind: OPTIONAL
    question: "Skip unless you want to keep the VADE 'five vade-app/*' aside as documentation of where this pattern was extracted from."
    find: " (VADE: the five `vade-app/*` repos)"
    fallback: ""

  - key: integrity_check_path
    kind: DETECT
    detection: "test -f \"${VADE_CLOUD_STATE_DIR:-}/integrity-check.json\" 2>/dev/null && echo found || true"
    find: "`summary.ok` state in `integrity-check.json` (surface failing\n   invariant if degraded)"
    fallback: "any health-check or environment-validation signals your project has"

  - key: mem0_failure_mode
    kind: OPTIONAL
    question: "Does your substrate use Mem0 (or equivalent) for cross-session state? Skip to drop the Mem0-disconnected failure-mode bullet."
    find: |
      - **Mem0 disconnected at boot.** File-canonical wins per
        MEMO-2026-04-27-01; proceed without Mem0 reachable. End-of-session
        episodic save uses REST fallback per SOP-MEM-001 §5.
    fallback: ""

script_hints:
  - path: persona.md
    treatment: REGENERATE-PER-USER
    rationale: "The persona doctrine is the heart of exec-mode and is densely substrate-coupled (five named repos, integrity-check probe paths, proj:* labels, permanently-open semantics, coo/lineage/ manifest paths, CB-006 quorum, named auditor agents). Mechanical substitution produces an incoherent doctrine. The adapted version is emitted as a skeleton with Phase 0-4 headings filled in but the discipline-rollup empty for the user to fold their own per-run lessons into. Source for inspiration: skills/reference/exec-mode/persona.md (this file's sibling — read but do not install verbatim)."

  - path: personas-README.md
    treatment: PARAMETERIZE
    rationale: "Persona-pattern documentation; mostly substrate-agnostic prose. Light substitution covers the VADE-specific examples; the load-bearing pattern (load-fresh-each-session, retrospectives compound, revision discipline) ports."

degradations:
  - when: "--revise-persona invoked but auditor_agents not configured"
    body_replace:
      find: "jump to the persona file's `## Persona-revision discipline`\n   section and follow that procedure (read-all-retros + plan-mode\n   REQUIRED + auditor gates)"
      with: "jump to the persona file's `## Persona-revision discipline`\n   section and follow that procedure (read-all-retros + plan-mode\n   REQUIRED). Note: this adapted skill has no auditor agents configured — replace the auditor-gate step with explicit human review before merging the revision PR."
    note: "Adapted without adversarial auditor agents — --revise-persona's auditor gates degrade to explicit human review. Re-run /adapt-skill exec-mode after installing safety-auditor and emancipatory-auditor (or your own equivalents) to restore the gates."
```
