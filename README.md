# vade-app/skills

Portable [Claude Code](https://www.anthropic.com/claude-code) skills
and sub-agent definitions, extracted from the VADE substrate
(<https://read.vade-app.dev>).

## What's here

**Skills** (`skills/`) — Claude Code "skills" are scoped competence
bundles loaded on demand. Each is a directory containing a
`SKILL.md` with frontmatter (`name`, `description`) and any
`references/` it draws on.

- `quarto-docs` — Navigate Quarto SDK documentation efficiently
  without hallucinating YAML keys.
- `tldraw-docs` — Navigate the tldraw canvas SDK without
  hallucinating API signatures.
- `canvas-ui` — Canvas / tldraw frontend conventions and the
  recurring landmines a tldraw-based codebase teaches you about.
- `peer-review` — Commission N independent peer reviewers on a
  long-form authored artifact (essay, paper, RFC, plan) and
  synthesize findings into a trackable revision pipeline.

**Agents** (`agents/`) — Sub-agent definitions for Claude Code's
`Agent` tool. Each is a single `.md` file with frontmatter
(`name`, `description`, optional `tools`, `model`).

- `research-investigator` — Schema-driven research sub-agent for
  bounded investigations across a specified file corpus.
- `rationalization-discriminator` — Read-only adversarial auditor
  that asks "is this argument load-bearing or rationalizing?" and
  reports a path-quality verdict separate from the outcome.
- `lineage-interpreter` — Argues a thesis about what a cultural
  corpus *is* as a cultural form, not what it claims about itself.
- `dispatching-parallel-agents` — Cherry-picked from
  [obra/superpowers](https://github.com/obra/superpowers); adapted
  for any Claude Code environment.

**Reference agents** (`agents/reference/`) — Carry concept-level
patterns we found useful, but cite VADE-internal memos. Fork and
adapt to your own substrate.

- `safety-auditor` — Gate-keeper pattern: adversarial Phase-3
  teammate that blocks artifacts violating named governance memos.
- `emancipatory-auditor` — Adoption-test gate: every artifact must
  grow the author's capability AND be installable by a peer.

**Setup** (`setup/`) — Installer plus `.mcp.json` template that
uses 1Password vault references with environment-variable fallback.

## Patterns these encode

Two patterns recur across the skills here:

1. **LLM-optimized-doc-bundle navigation.** Some SDKs publish their
   documentation in markdown bundles explicitly designed for
   language-model consumption (Quarto at `quarto.org/llms.txt`;
   tldraw at `tldraw.dev/llms*.txt`). The `quarto-docs` and
   `tldraw-docs` skills teach which bundle to fetch and how to
   navigate it so an agent doesn't grab the mega-bundle when a
   narrow page would do, doesn't hallucinate topic names that
   don't exist, and doesn't repeatedly miss the right page.
2. **Project-conventions-as-skill.** A skill captures the
   accumulated landmines of working in a specific codebase
   (`canvas-ui` is the worked case for tldraw-based projects). The
   skill is the anti-pattern layer; the SDK-docs skill is the
   reference layer. The two compose.

## Install

### Option A — quick clone into a Claude Code project

```sh
git clone https://github.com/vade-app/skills.git /tmp/vade-skills
cp -r /tmp/vade-skills/skills/* /path/to/your-project/.claude/skills/
cp /tmp/vade-skills/agents/*.md /path/to/your-project/.claude/agents/
```

### Option B — setup script

```sh
./setup/cloud-setup.sh /path/to/your-project
```

Symlinks `skills/*` and `agents/*` into your project's `.claude/`
directory (or `~/.claude/` if you pass `--user`).

### Option C — pin to a release

```sh
git clone --branch v0.1.0 --depth 1 https://github.com/vade-app/skills.git
```

Releases follow semver: minor bumps when skills are added, patch
bumps for in-place revisions. Tag releases on the
[Releases page](https://github.com/vade-app/skills/releases).

## MCP servers

The `setup/mcp.json.template` is intentionally a template, not a
working `.mcp.json`. It encodes a single pattern: **secrets resolve
through 1Password CLI** (`op://Vault/Item/field`) **with
environment-variable fallback**. To activate any server, copy the
template, fill in your own vault paths or env vars, drop entries
you don't need, and save as `.mcp.json` in your project root.

The template covers `mem0`, `github`, `agentmail` — substitute or
extend as your project requires.

## Provenance

These artifacts were authored inside the
[VADE substrate](https://read.vade-app.dev) and extracted here so
that peer agents and humans can install and adapt them. Where an
artifact has earlier upstream provenance (cherry-picked from
another public repo), it is named in [`VENDORED.md`](VENDORED.md).

## License

CC-BY-4.0. See [`LICENSE`](LICENSE).

Attribution: link to this repository
(<https://github.com/vade-app/skills>) and name the version you
copied from.
