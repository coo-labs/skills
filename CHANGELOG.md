# Changelog

All notable changes to this repository are documented in this file.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning follows [Semantic Versioning](https://semver.org/).

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
