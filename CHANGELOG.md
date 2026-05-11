# Changelog

All notable changes to this repository are documented in this file.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning follows [Semantic Versioning](https://semver.org/).

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
