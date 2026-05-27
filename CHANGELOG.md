# Changelog

All notable changes to this repository are documented in this file.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning follows [Semantic Versioning](https://semver.org/).

## Unreleased

### Changed

- Repo org renamed `vade-app/skills` → `coo-labs/skills`. README install
  commands updated; existing clones continue to work via GitHub's
  automatic redirect on the old org/repo path.
- `setup/cloud-setup.sh` renamed to `setup/install.sh`. The name
  `cloud-setup` was a misleading artifact — the script installs skills
  into any Claude Code project, not specifically a cloud one. Callers
  must update their invocation paths. Internal references in
  `README.md`, `setup/README.md`, and `skills/adapt-skill/SKILL.md`
  updated.

## v0.4.0 — 2026-05-12

Extends the `skills/reference/` tier with six substrate-discipline
skills from the VADE corpus — patterns that were live in the
private substrate but had not yet been ported to the public corpus.
Same fork-and-adapt model as v0.3.0: pattern ports cleanly,
substrate references in the discipline files don't.

### Reference skills

- `skills/reference/day-overview` — briefing-shape synthesis of a
  day's shipped work (memos, merged PRs, integrity snapshot)
  grouped into lanes, with carried-forward follow-ups and ranked
  next actions. Ships with `scripts/day-overview.sh` as the
  worked manifest-gatherer.
- `skills/reference/request-briefing` — author an NNN-numbered
  session-handoff briefing. Load-bearing structural requirement:
  a mandatory "Known bounds" section where the author names
  their blind spots so the recipient re-examines the framing
  rather than rubber-stamping it.
- `skills/reference/commission-retrospective` — impartial
  project-historian retrospective on a window of project work.
  Two evidence sub-agents in parallel (memos-and-essays analyst,
  PR/issue-graph analyst), then a third-person draft that
  refuses recycled defended positions. Ships with shell
  pre-flight and three sub-agent templates.
- `skills/reference/end-session` — session close-down checklist.
  Begins with an externalization-reflection step (did anything
  this session produce a transferable pattern worth packaging?),
  followed by one episodic-memory entry, a session log,
  transcript-export sidecar pickup, and a marker file that
  silences a Stop hook.
- `skills/reference/status-check` — six-item read-only grounding
  audit (who/what/where/next/decision/resource) capped at eight
  lines, with `⚠ not grounded` as the explicit "I can't answer
  that from loaded context" marker. The most substrate-agnostic
  of the reference skills.
- `skills/reference/tool-creator` — staged-checkpoint skill
  authoring. Phase 1 draft (inventory check, frontmatter
  decision-tree, deliberate stop). Phase 2 finalize (two
  adversarial auditors in parallel, tools-registry row, PR).
  Four canonical refactor patterns documented. Ships with four
  templates.

## v0.3.0 — 2026-05-11

Adds `skills/reference/` tier — session-register and persona-overlay
patterns extracted from VADE that need adaptation before they
install cleanly.

### Reference skills

- `skills/reference/chat-mode` — Loads the dialogue register
  (distinct from execution-shaped sessions): substantive
  conversation that can produce binding output (memo, retro, PR).
- `skills/reference/exec-mode` — Loads an executive-persona overlay
  (Phase 0 survey → optional Plan-mode → Phase 2 sub-agent dispatch
  → Phase 3 act → Phase 4 reflection) for broad-scope sweep /
  cleanup / strategic-reflection sessions. Ships with the persona
  doctrine (`persona.md`) and the persona-pattern README
  (`personas-README.md`).

Same shape as `agents/reference/`: pattern ports cleanly; substrate
references in the discipline files don't.

## v0.2.0 — 2026-05-11

Adds the `peer-review` skill — commission N independent reviewers in
parallel on a long-form authored artifact and synthesize findings
into a trackable revision pipeline.

### Skills

- `peer-review` — Multi-lens independent critique on long-form
  artifacts (essays, papers, foundation docs, RFCs, plans).
  Dispatches sub-agents in parallel via the Task tool; produces
  strongest-moves / weak-points / missing-considerations /
  concrete-revision-suggestions per reviewer, then synthesizes.
  Optional Phase-2 decomposition into a GitHub issue tree +
  re-runnable implementer briefing for asynchronous per-atom
  revision PRs.

## v0.1.0 — 2026-05-11

Initial public release.

### Skills

- `quarto-docs` — Navigate Quarto SDK documentation
- `tldraw-docs` — Navigate the tldraw canvas SDK
- `canvas-ui` — Canvas / tldraw frontend conventions

### Agents

- `research-investigator`
- `rationalization-discriminator`
- `lineage-interpreter`
- `dispatching-parallel-agents` (vendored from
  [obra/superpowers](https://github.com/obra/superpowers))

### Reference agents

- `agents/reference/safety-auditor` — VADE-shaped; fork and adapt
- `agents/reference/emancipatory-auditor` — VADE-shaped; fork and adapt

### Setup

- `setup/cloud-setup.sh` — installer
- `setup/mcp.json.template` — MCP server template (1Password +
  env-var fallback)

### Release cadence

Event-driven: a new release is cut when new skills land or
substantive revisions ship. No fixed monthly cadence; the source
substrate is the cadence input.
