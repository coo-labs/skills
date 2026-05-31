# Claude Code skill & agent inventory

_Generated `2026-05-30T18:01:37Z` · schema `v1.0.0`._

## Summary

- **Total entries**: 57
- **By kind**: agent=15, skill=42
- **By repo**: `coo-labs/coo-harness`=4, `coo-labs/coo-memory`=32, `coo-labs/skills`=19, `coo-labs/vade-canvas`=2
- **By type**: procedural=20, agent-specialist=5, role=5, agent-auditor=4, documentation=4, meta=4, reference=4, api-service=3, agent-orchestrator=2, agent-researcher=2, agent-reviewer=2, review=2
- **By vendoring**: custom=52, vendored=4, vendored-customized=1
- **Declared metadata coverage**: type 57/57 (100%), vendoring 57/57 (100%) — remainder is derived heuristically. Migration goal: shrink the heuristic share over time.

Transcripts scanned: `/root/.claude/projects` (6 files). Invocation counts are honest reports of what the scan saw — point the scanner at an archive for cross-session totals.

Repos scanned:
- `coo-labs/coo-memory` @ `94fd06c5` (/home/user/coo-memory)
- `coo-labs/coo-harness` @ `f4047718` (/home/user/coo-harness)
- `coo-labs/vade-canvas` @ `7b88a64e` (/home/user/vade-canvas)
- `coo-labs/skills` @ `f30cd026` (/home/user/skills)

## Inventory by repo

### `coo-labs/coo-harness`

#### Skills (4)

| Name | Type | Vendor | Bytes | Lines | Bundle | Added | Last commit | Invocations |
|------|------|--------|-------|-------|--------|-------|-------------|-------------|
| `agentmail` | api-service | vendored<br>agentmail-to/agentmail-skills | 7483 | 288 | references=2 | 2026-05-16 | 2026-05-30 | 0 |
| `skill-creator` | meta | vendored | 33299 | 490 | scripts=9, references=1, assets=1, agents=3, LICENSE, vendor=VENDORED.md | 2026-05-16 | 2026-05-30 | 0 |
| `tagging-taxonomy` | procedural | — | 12237 | 286 | — | 2026-05-16 | 2026-05-30 | 0 |
| `trace-timeline` | procedural | — | 9177 | 175 | — | 2026-05-20 | 2026-05-30 | 0 |

### `coo-labs/coo-memory`

#### Skills (23)

| Name | Type | Vendor | Bytes | Lines | Bundle | Added | Last commit | Invocations |
|------|------|--------|-------|-------|--------|-------|-------------|-------------|
| `briefing` | procedural | — | 10731 | 242 | scripts=1, +2 files | 2026-05-30 | 2026-05-30 | 0 |
| `cf-workers-best-practices` | reference | vendored<br>cloudflare/skills | 7368 | 135 | references=2 | 2026-05-25 | 2026-05-30 | 0 |
| `cf-wrangler` | api-service | vendored<br>cloudflare/skills | 18637 | 930 | — | 2026-05-25 | 2026-05-30 | 0 |
| `chat-mode` | role | — | 5563 | 97 | — | 2026-05-25 | 2026-05-30 | 0 |
| `commission-retrospective` | procedural | — | 9676 | 211 | scripts=1, templates=3 | 2026-05-25 | 2026-05-30 | 0 |
| `day-overview` | procedural | — | 12243 | 296 | scripts=1 | 2026-05-25 | 2026-05-30 | 0 |
| `debug-mode` | role | — | 10581 | 227 | — | 2026-05-25 | 2026-05-30 | 0 |
| `end-session` | procedural | — | 6592 | 154 | — | 2026-05-25 | 2026-05-30 | 0 |
| `exec-mode` | role | — | 4489 | 88 | — | 2026-05-25 | 2026-05-30 | 0 |
| `manage-project` | api-service | — | 4219 | 86 | scripts=4, +1 dirs | 2026-05-25 | 2026-05-30 | 0 |
| `memo` | procedural | — | 15391 | 431 | — | 2026-05-25 | 2026-05-30 | 0 |
| `memo-audit` | procedural | — | 11075 | 282 | — | 2026-05-25 | 2026-05-30 | 0 |
| `memo-query` | procedural | — | 7379 | 177 | scripts=1 | 2026-05-25 | 2026-05-30 | 0 |
| `memo-search` | procedural | — | 8265 | 195 | — | 2026-05-25 | 2026-05-30 | 0 |
| `memo-sync` | procedural | — | 10952 | 262 | — | 2026-05-25 | 2026-05-30 | 0 |
| `peer-review` | review | — | 18264 | 370 | evals=1 | 2026-05-25 | 2026-05-30 | 0 |
| `post-discussion` | procedural | — | 12197 | 276 | — | 2026-05-25 | 2026-05-30 | 0 |
| `postmerge-check` | procedural | — | 7818 | 128 | scripts=1 | 2026-05-25 | 2026-05-30 | 0 |
| `quarto-docs` | documentation | — | 12384 | 113 | — | 2026-05-25 | 2026-05-30 | 0 |
| `status-check` | procedural | — | 5905 | 141 | — | 2026-05-25 | 2026-05-30 | 0 |
| `tag-milestone` | procedural | — | 8580 | 259 | — | 2026-05-25 | 2026-05-30 | 0 |
| `tool-creator` | meta | — | 20822 | 462 | templates=4 | 2026-05-25 | 2026-05-30 | 0 |
| `upstream-feedback` | reference | — | 3989 | 49 | references=1 | 2026-05-25 | 2026-05-30 | 0 |

#### Agents (9)

| Name | Type | Vendor | Bytes | Lines | Bundle | Added | Last commit | Invocations |
|------|------|--------|-------|-------|--------|-------|-------------|-------------|
| `dispatching-parallel-agents` | agent-orchestrator | — | 5375 | 143 | — | 2026-05-25 | 2026-05-30 | 0 |
| `emancipatory-auditor` | agent-auditor | — | 4483 | 61 | — | 2026-05-25 | 2026-05-30 | 0 |
| `lineage-interpreter` | agent-specialist | — | 9303 | 115 | — | 2026-05-25 | 2026-05-30 | 0 |
| `oss-launch-issue-curator` | agent-specialist | — | 8467 | 129 | — | 2026-05-25 | 2026-05-30 | 0 |
| `rationalization-discriminator` | agent-reviewer | — | 7263 | 79 | — | 2026-05-25 | 2026-05-30 | 0 |
| `research-investigator` | agent-researcher | — | 3192 | 78 | — | 2026-05-25 | 2026-05-30 | 0 |
| `safety-auditor` | agent-auditor | — | 4325 | 52 | — | 2026-05-25 | 2026-05-30 | 0 |
| `session-closer` | agent-specialist | — | 13350 | 245 | — | 2026-05-25 | 2026-05-30 | 0 |
| `transcript-analyzer` | agent-specialist | — | 23431 | 292 | — | 2026-05-25 | 2026-05-30 | 0 |

### `coo-labs/skills`

#### Skills (13)

| Name | Type | Vendor | Bytes | Lines | Bundle | Added | Last commit | Invocations |
|------|------|--------|-------|-------|--------|-------|-------------|-------------|
| `adapt-skill` | meta | — | 12390 | 298 | scripts=1, +2 files | 2026-05-12 | 2026-05-30 | 0 |
| `briefing` | procedural | — | 10731 | 242 | scripts=1, +2 files | 2026-05-30 | 2026-05-30 | 0 |
| `canvas-ui` | reference | — | 19215 | 184 | references=1 | 2026-05-11 | 2026-05-30 | 0 |
| `chat-mode` | role | — | 9678 | 141 | — | 2026-05-11 | 2026-05-30 | 0 |
| `commission-retrospective` | procedural | — | 19588 | 394 | scripts=1, templates=3 | 2026-05-12 | 2026-05-30 | 0 |
| `day-overview` | procedural | — | 19677 | 451 | scripts=1 | 2026-05-12 | 2026-05-30 | 0 |
| `end-session` | procedural | — | 15497 | 347 | — | 2026-05-12 | 2026-05-30 | 0 |
| `exec-mode` | role | — | 9333 | 166 | +2 files | 2026-05-11 | 2026-05-30 | 0 |
| `peer-review` | review | — | 17842 | 357 | — | 2026-05-11 | 2026-05-30 | 0 |
| `quarto-docs` | documentation | — | 12086 | 113 | — | 2026-05-11 | 2026-05-30 | 0 |
| `status-check` | procedural | — | 8023 | 186 | — | 2026-05-12 | 2026-05-30 | 0 |
| `tldraw-docs` | documentation | — | 11750 | 99 | — | 2026-05-11 | 2026-05-30 | 0 |
| `tool-creator` | meta | — | 31255 | 640 | templates=4 | 2026-05-12 | 2026-05-30 | 0 |

#### Agents (6)

| Name | Type | Vendor | Bytes | Lines | Bundle | Added | Last commit | Invocations |
|------|------|--------|-------|-------|--------|-------|-------------|-------------|
| `dispatching-parallel-agents` | agent-orchestrator | vendored-customized<br>obra/superpowers | 5604 | 147 | — | 2026-05-11 | 2026-05-30 | 0 |
| `emancipatory-auditor` | agent-auditor | — | 9001 | 156 | — | 2026-05-11 | 2026-05-30 | 0 |
| `lineage-interpreter` | agent-specialist | — | 9327 | 115 | — | 2026-05-11 | 2026-05-30 | 0 |
| `rationalization-discriminator` | agent-reviewer | — | 7297 | 79 | — | 2026-05-11 | 2026-05-30 | 0 |
| `research-investigator` | agent-researcher | — | 3178 | 78 | — | 2026-05-11 | 2026-05-30 | 0 |
| `safety-auditor` | agent-auditor | — | 8853 | 127 | — | 2026-05-11 | 2026-05-30 | 0 |

### `coo-labs/vade-canvas`

#### Skills (2)

| Name | Type | Vendor | Bytes | Lines | Bundle | Added | Last commit | Invocations |
|------|------|--------|-------|-------|--------|-------|-------------|-------------|
| `canvas-ui` | reference | — | 19266 | 184 | references=1, evals=1 | 2026-05-09 | 2026-05-30 | 0 |
| `tldraw-docs` | documentation | — | 11822 | 99 | references=1 | 2026-05-01 | 2026-05-30 | 0 |

## Cross-cut by type

### procedural (20)

- `tagging-taxonomy` (skill, `coo-labs/coo-harness`) — custom, 12237B
- `trace-timeline` (skill, `coo-labs/coo-harness`) — custom, 9177B
- `briefing` (skill, `coo-labs/coo-memory`) — custom, 10731B
- `commission-retrospective` (skill, `coo-labs/coo-memory`) — custom, 9676B
- `day-overview` (skill, `coo-labs/coo-memory`) — custom, 12243B
- `end-session` (skill, `coo-labs/coo-memory`) — custom, 6592B
- `memo` (skill, `coo-labs/coo-memory`) — custom, 15391B
- `memo-audit` (skill, `coo-labs/coo-memory`) — custom, 11075B
- `memo-query` (skill, `coo-labs/coo-memory`) — custom, 7379B
- `memo-search` (skill, `coo-labs/coo-memory`) — custom, 8265B
- `memo-sync` (skill, `coo-labs/coo-memory`) — custom, 10952B
- `post-discussion` (skill, `coo-labs/coo-memory`) — custom, 12197B
- `postmerge-check` (skill, `coo-labs/coo-memory`) — custom, 7818B
- `status-check` (skill, `coo-labs/coo-memory`) — custom, 5905B
- `tag-milestone` (skill, `coo-labs/coo-memory`) — custom, 8580B
- `briefing` (skill, `coo-labs/skills`) _(reference)_ — custom, 10731B
- `commission-retrospective` (skill, `coo-labs/skills`) _(reference)_ — custom, 19588B
- `day-overview` (skill, `coo-labs/skills`) _(reference)_ — custom, 19677B
- `end-session` (skill, `coo-labs/skills`) _(reference)_ — custom, 15497B
- `status-check` (skill, `coo-labs/skills`) _(reference)_ — custom, 8023B

### agent-specialist (5)

- `lineage-interpreter` (agent, `coo-labs/coo-memory`) — custom, 9303B
- `oss-launch-issue-curator` (agent, `coo-labs/coo-memory`) — custom, 8467B
- `session-closer` (agent, `coo-labs/coo-memory`) — custom, 13350B
- `transcript-analyzer` (agent, `coo-labs/coo-memory`) — custom, 23431B
- `lineage-interpreter` (agent, `coo-labs/skills`) — custom, 9327B

### role (5)

- `chat-mode` (skill, `coo-labs/coo-memory`) — custom, 5563B
- `debug-mode` (skill, `coo-labs/coo-memory`) — custom, 10581B
- `exec-mode` (skill, `coo-labs/coo-memory`) — custom, 4489B
- `chat-mode` (skill, `coo-labs/skills`) _(reference)_ — custom, 9678B
- `exec-mode` (skill, `coo-labs/skills`) _(reference)_ — custom, 9333B

### agent-auditor (4)

- `emancipatory-auditor` (agent, `coo-labs/coo-memory`) — custom, 4483B
- `safety-auditor` (agent, `coo-labs/coo-memory`) — custom, 4325B
- `emancipatory-auditor` (agent, `coo-labs/skills`) _(reference)_ — custom, 9001B
- `safety-auditor` (agent, `coo-labs/skills`) _(reference)_ — custom, 8853B

### documentation (4)

- `quarto-docs` (skill, `coo-labs/coo-memory`) — custom, 12384B
- `quarto-docs` (skill, `coo-labs/skills`) — custom, 12086B
- `tldraw-docs` (skill, `coo-labs/skills`) — custom, 11750B
- `tldraw-docs` (skill, `coo-labs/vade-canvas`) — custom, 11822B

### meta (4)

- `skill-creator` (skill, `coo-labs/coo-harness`) — vendored, 33299B
- `tool-creator` (skill, `coo-labs/coo-memory`) — custom, 20822B
- `adapt-skill` (skill, `coo-labs/skills`) — custom, 12390B
- `tool-creator` (skill, `coo-labs/skills`) _(reference)_ — custom, 31255B

### reference (4)

- `cf-workers-best-practices` (skill, `coo-labs/coo-memory`) — vendored, 7368B
- `upstream-feedback` (skill, `coo-labs/coo-memory`) — custom, 3989B
- `canvas-ui` (skill, `coo-labs/skills`) — custom, 19215B
- `canvas-ui` (skill, `coo-labs/vade-canvas`) — custom, 19266B

### api-service (3)

- `agentmail` (skill, `coo-labs/coo-harness`) — vendored, 7483B
- `cf-wrangler` (skill, `coo-labs/coo-memory`) — vendored, 18637B
- `manage-project` (skill, `coo-labs/coo-memory`) — custom, 4219B

### agent-orchestrator (2)

- `dispatching-parallel-agents` (agent, `coo-labs/coo-memory`) — custom, 5375B
- `dispatching-parallel-agents` (agent, `coo-labs/skills`) — vendored-customized, 5604B

### agent-researcher (2)

- `research-investigator` (agent, `coo-labs/coo-memory`) — custom, 3192B
- `research-investigator` (agent, `coo-labs/skills`) — custom, 3178B

### agent-reviewer (2)

- `rationalization-discriminator` (agent, `coo-labs/coo-memory`) — custom, 7263B
- `rationalization-discriminator` (agent, `coo-labs/skills`) — custom, 7297B

### review (2)

- `peer-review` (skill, `coo-labs/coo-memory`) — custom, 18264B
- `peer-review` (skill, `coo-labs/skills`) — custom, 17842B

## Cross-cut by vendoring

### custom (52)

- `tagging-taxonomy` (skill, `coo-labs/coo-harness`)
- `trace-timeline` (skill, `coo-labs/coo-harness`)
- `dispatching-parallel-agents` (agent, `coo-labs/coo-memory`)
- `emancipatory-auditor` (agent, `coo-labs/coo-memory`)
- `lineage-interpreter` (agent, `coo-labs/coo-memory`)
- `oss-launch-issue-curator` (agent, `coo-labs/coo-memory`)
- `rationalization-discriminator` (agent, `coo-labs/coo-memory`)
- `research-investigator` (agent, `coo-labs/coo-memory`)
- `safety-auditor` (agent, `coo-labs/coo-memory`)
- `session-closer` (agent, `coo-labs/coo-memory`)
- `transcript-analyzer` (agent, `coo-labs/coo-memory`)
- `briefing` (skill, `coo-labs/coo-memory`)
- `chat-mode` (skill, `coo-labs/coo-memory`)
- `commission-retrospective` (skill, `coo-labs/coo-memory`)
- `day-overview` (skill, `coo-labs/coo-memory`)
- `debug-mode` (skill, `coo-labs/coo-memory`)
- `end-session` (skill, `coo-labs/coo-memory`)
- `exec-mode` (skill, `coo-labs/coo-memory`)
- `manage-project` (skill, `coo-labs/coo-memory`)
- `memo` (skill, `coo-labs/coo-memory`)
- `memo-audit` (skill, `coo-labs/coo-memory`)
- `memo-query` (skill, `coo-labs/coo-memory`)
- `memo-search` (skill, `coo-labs/coo-memory`)
- `memo-sync` (skill, `coo-labs/coo-memory`)
- `peer-review` (skill, `coo-labs/coo-memory`)
- `post-discussion` (skill, `coo-labs/coo-memory`)
- `postmerge-check` (skill, `coo-labs/coo-memory`)
- `quarto-docs` (skill, `coo-labs/coo-memory`)
- `status-check` (skill, `coo-labs/coo-memory`)
- `tag-milestone` (skill, `coo-labs/coo-memory`)
- `tool-creator` (skill, `coo-labs/coo-memory`)
- `upstream-feedback` (skill, `coo-labs/coo-memory`)
- `emancipatory-auditor` (agent, `coo-labs/skills`)
- `lineage-interpreter` (agent, `coo-labs/skills`)
- `rationalization-discriminator` (agent, `coo-labs/skills`)
- `research-investigator` (agent, `coo-labs/skills`)
- `safety-auditor` (agent, `coo-labs/skills`)
- `adapt-skill` (skill, `coo-labs/skills`)
- `briefing` (skill, `coo-labs/skills`)
- `canvas-ui` (skill, `coo-labs/skills`)
- `chat-mode` (skill, `coo-labs/skills`)
- `commission-retrospective` (skill, `coo-labs/skills`)
- `day-overview` (skill, `coo-labs/skills`)
- `end-session` (skill, `coo-labs/skills`)
- `exec-mode` (skill, `coo-labs/skills`)
- `peer-review` (skill, `coo-labs/skills`)
- `quarto-docs` (skill, `coo-labs/skills`)
- `status-check` (skill, `coo-labs/skills`)
- `tldraw-docs` (skill, `coo-labs/skills`)
- `tool-creator` (skill, `coo-labs/skills`)
- `canvas-ui` (skill, `coo-labs/vade-canvas`)
- `tldraw-docs` (skill, `coo-labs/vade-canvas`)

### vendored (4)

- `agentmail` (skill, `coo-labs/coo-harness`) — https://github.com/agentmail-to/agentmail-skills; snap 2026-04-22; marker frontmatter.metadata
- `skill-creator` (skill, `coo-labs/coo-harness`) — marker frontmatter.metadata
- `cf-workers-best-practices` (skill, `coo-labs/coo-memory`) — https://github.com/cloudflare/skills; @7c449def; snap 2026-04-28; marker frontmatter.metadata
- `cf-wrangler` (skill, `coo-labs/coo-memory`) — https://github.com/cloudflare/skills; @7c449def; snap 2026-04-28; marker frontmatter.metadata

### vendored-customized (1)

- `dispatching-parallel-agents` (agent, `coo-labs/skills`) — https://github.com/obra/superpowers; @9ccce3bf; marker frontmatter.metadata

## Descriptions

### `agentmail` — skill in `coo-labs/coo-harness`

- **Type**: api-service _(source: declared; declared metadata.type = 'api-service')_
- **Vendoring**: vendored _(source: declared)_
  - upstream `https://github.com/agentmail-to/agentmail-skills`; snapshot 2026-04-22; marker `frontmatter.metadata`
  - local edits: _none (verbatim per import commit 0ca5b61)_
- **Path**: `.claude/skills/agentmail/SKILL.md`
- **Size**: 7483 bytes / 288 lines · description 344 chars · body 6898 chars
- **Bundle**: references=2
- **Git**: first 2026-05-16, last 2026-05-30, 3 commits
- **Usage**: 0 invocations across 0 sessions

> Give AI agents their own email inboxes using the AgentMail API. Use when building email agents, sending/receiving emails programmatically, managing inboxes, handling attachments, organizing with labels, creating drafts for human approval, or setting up real-time notifications via webhooks/websockets. Supports multi-tenant isolation with pods.

### `skill-creator` — skill in `coo-labs/coo-harness`

- **Type**: meta _(source: declared; declared metadata.type = 'meta')_
- **Vendoring**: vendored _(source: declared)_
  - marker `frontmatter.metadata`
  - local edits: _none (verbatim per VENDORED.md maintenance rule)_
- **Path**: `.claude/skills/skill-creator/SKILL.md`
- **Size**: 33299 bytes / 490 lines · description 319 chars · body 32625 chars
- **Bundle**: scripts=9, references=1, assets=1, agents=3, LICENSE, vendor=VENDORED.md
- **Git**: first 2026-05-16, last 2026-05-30, 2 commits
- **Usage**: 0 invocations across 0 sessions

> Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit, or optimize an existing skill, run evals to test a skill, benchmark skill performance with variance analysis, or optimize a skill's description for better triggering accuracy.

### `tagging-taxonomy` — skill in `coo-labs/coo-harness`

- **Type**: procedural _(source: declared; declared metadata.type = 'procedural')_
- **Vendoring**: custom _(source: declared)_
  - marker `frontmatter.metadata`
- **Path**: `.claude/skills/tagging-taxonomy/SKILL.md`
- **Size**: 12237 bytes / 286 lines · description 418 chars · body 11659 chars
- **Git**: first 2026-05-16, last 2026-05-30, 7 commits
- **Usage**: 0 invocations across 0 sessions

> Apply or look up VADE issue metadata. Use when filing, triaging, or searching issues across coo-labs repos by dimension (issue type, area, Readiness field, Priority field, needs/blocked). Native types + Issue fields are the primary metadata layer; operational reference: `operations/issue-fields-and-types.md` (field list, pinning matrix, API surface). `area:*` and qualifier labels are what remains label-encoded.

### `trace-timeline` — skill in `coo-labs/coo-harness`

- **Type**: procedural _(source: declared; declared metadata.type = 'procedural')_
- **Vendoring**: custom _(source: declared)_
  - marker `frontmatter.metadata`
- **Path**: `.claude/skills/trace-timeline/SKILL.md`
- **Size**: 9177 bytes / 175 lines · description 880 chars · body 8087 chars
- **Frontmatter**: allowed-tools `Bash, Read, SendUserFile`
- **Git**: first 2026-05-20, last 2026-05-30, 4 commits
- **Usage**: 0 invocations across 0 sessions

> Render an interactive HTML timeline from a bootstrap-trace run. Use when the user wants to view, visualize, inspect, or "see" what happened during a traced boot — process spans, write/read interleavings, snapshot states, the D-group invariant decisions. Triggers on phrases like "show me the trace", "visualize the boot", "timeline of the trace", "interactive diagram of the trace", "render the trace", or when investigating a `~/.vade/traces/<run-id>/` directory and a chart would be clearer than text. Reads `xtrace.log` + `snapshots/*/content/settings.json` + `meta.json`, writes a self-contained HTML file that opens in any browser. Read-only over the trace data. Don't invoke for: running a fresh trace (that's the `bootstrap-trace-init.sh` harness via container UI), proposing fixes to the boot pipeline (the audit pause forbids it), or operating on traces from other tools.

### `dispatching-parallel-agents` — agent in `coo-labs/coo-memory`

- **Type**: agent-orchestrator _(source: declared; declared metadata.type = 'agent-orchestrator')_
- **Vendoring**: custom _(source: declared)_
  - marker `frontmatter.metadata`
- **Path**: `.claude/agents/dispatching-parallel-agents.md`
- **Size**: 5375 bytes / 143 lines · description 185 chars · body 5024 chars
- **Frontmatter**: model `sonnet`
- **Git**: first 2026-05-25, last 2026-05-30, 2 commits
- **Usage**: 0 invocations across 0 sessions

> Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies. Cherry-picked from obra/superpowers; adapted for any Claude Code environment.

### `emancipatory-auditor` — agent in `coo-labs/coo-memory`

- **Type**: agent-auditor _(source: declared; declared metadata.type = 'agent-auditor')_
- **Vendoring**: custom _(source: declared)_
  - marker `frontmatter.metadata`
- **Path**: `.claude/agents/emancipatory-auditor.md`
- **Size**: 4483 bytes / 61 lines · description 348 chars · body 3954 chars
- **Frontmatter**: tools `Read, Bash, WebFetch, Agent`; model `sonnet`
- **Git**: first 2026-05-25, last 2026-05-30, 3 commits
- **Usage**: 0 invocations across 0 sessions

> Adversarial Phase-3 teammate. Enforces MEMO 2026-04-20-01's double-clause (subject AND emancipatory) on every artifact the team ships. Drops anything scoring 2/0 or 0/2. Distinct from the safety-auditor — they enforce governance memos; you enforce the prime directive's interpretation. Spawn as a teammate when Phase 3 needs the adoption-test gate.

### `lineage-interpreter` — agent in `coo-labs/coo-memory`

- **Type**: agent-specialist _(source: declared; declared metadata.type = 'agent-specialist')_
- **Vendoring**: custom _(source: declared)_
  - marker `frontmatter.metadata`
- **Path**: `.claude/agents/lineage-interpreter.md`
- **Size**: 9303 bytes / 115 lines · description 756 chars · body 8309 chars
- **Frontmatter**: tools `Read, Write, Edit, Bash, WebFetch, WebSearch, Agent`; model `opus`
- **Git**: first 2026-05-25, last 2026-05-30, 3 commits
- **Usage**: 0 invocations across 0 sessions

> Spawn for interpretive-history work on a cultural corpus — argues a thesis about what the corpus IS as a cultural form, not what it claims about itself. Genre is Wootton/Harari interpretive history (argumentative, defamiliarizing, reader-out, takes a stance). Methodology: corpus-map (delegated to research-investigator) → primary-source read → candidate-thesis-shapes → synthesis essay → three-instance peer-review pass → patches and successor-parking. Distinct from research-investigator (which reports facts without taking a stance) and from a project-historian role (which documents and analyzes inside the corpus's own frame). Use when an orchestrator needs a theory of a cultural narrative, not a survey of facts. Reusable across any cultural corpus.

### `oss-launch-issue-curator` — agent in `coo-labs/coo-memory`

- **Type**: agent-specialist _(source: declared; declared metadata.type = 'agent-specialist')_
- **Vendoring**: custom _(source: declared)_
  - marker `frontmatter.metadata`
- **Path**: `.claude/agents/oss-launch-issue-curator.md`
- **Size**: 8467 bytes / 129 lines · description 709 chars · body 7526 chars
- **Frontmatter**: tools `Read, Bash, Grep`; model `sonnet`
- **Git**: first 2026-05-25, last 2026-05-30, 2 commits
- **Usage**: 0 invocations across 0 sessions

> Curate the initial issue tracker for a public-flipped or newly-launched OSS repo. Dispatch when a `coo-labs/*` repo is about to flip from private to public, or a brand-new public repo is being seeded. Reads the target repo's README / CONTRIBUTING / spec / source / tests and any caller-supplied strategic framing, then produces a four-bucket curated list of follow-up issues (good-first / spec-coverage gaps / architecture RFCs / follow-on tooling) with per-issue labels, difficulty, and definition-of-done. Recommends a filing strategy (which 3–5 to file first vs. hold). Does NOT file the issues itself — curation is the deliverable; the dispatcher reviews then files. Reusable across any public-flip event.

### `rationalization-discriminator` — agent in `coo-labs/coo-memory`

- **Type**: agent-reviewer _(source: declared; declared metadata.type = 'agent-reviewer')_
- **Vendoring**: custom _(source: declared)_
  - marker `frontmatter.metadata`
- **Path**: `.claude/agents/rationalization-discriminator.md`
- **Size**: 7263 bytes / 79 lines · description 551 chars · body 6509 chars
- **Frontmatter**: tools `Read, Bash, WebFetch, Agent`; model `sonnet`
- **Git**: first 2026-05-25, last 2026-05-30, 3 commits
- **Usage**: 0 invocations across 0 sessions

> Read-only adversarial auditor for chain reasoning that fits the load-substrate → prior-dissolves → action-follows shape (MEMO-2026-05-09-wzzh). Asks one load-bearing question — "is this argument load-bearing or rationalizing?" — and reports a path-quality verdict separate from the outcome. Distinct from safety-auditor (governance-memo compliance) and emancipatory-auditor (subject+emancipatory clause); this role audits *path*, not *clauses*. Spawn when the COO notices the shape in its own move and wants an external read before banking the action.

### `research-investigator` — agent in `coo-labs/coo-memory`

- **Type**: agent-researcher _(source: declared; declared metadata.type = 'agent-researcher')_
- **Vendoring**: custom _(source: declared)_
  - marker `frontmatter.metadata`
- **Path**: `.claude/agents/research-investigator.md`
- **Size**: 3192 bytes / 78 lines · description 211 chars · body 2804 chars
- **Frontmatter**: tools `Read, Bash, WebFetch, Agent`; model `sonnet`
- **Git**: first 2026-05-25, last 2026-05-30, 3 commits
- **Usage**: 0 invocations across 0 sessions

> Generic research sub-agent. Spawn when an orchestrator needs focused, schema-driven investigation of a bounded question across a specified file corpus. Reusable across any repo — no project-specific assumptions.

### `safety-auditor` — agent in `coo-labs/coo-memory`

- **Type**: agent-auditor _(source: declared; declared metadata.type = 'agent-auditor')_
- **Vendoring**: custom _(source: declared)_
  - marker `frontmatter.metadata`
- **Path**: `.claude/agents/safety-auditor.md`
- **Size**: 4325 bytes / 52 lines · description 309 chars · body 3855 chars
- **Frontmatter**: tools `Read, Bash, WebFetch, Agent`; model `sonnet`
- **Git**: first 2026-05-25, last 2026-05-30, 2 commits
- **Usage**: 0 invocations across 0 sessions

> Adversarial Phase-3 teammate. Gate-keeper against governance memos (-08 Tier-2, -10 Mem0 content rule, -14 sync paths, -19 spend cap, -22-01 PAT/identity discipline). Reviews each track specialist's deliverables and blocks anything that fails. Spawn as a teammate when Phase 3 needs adversarial safety review.

### `session-closer` — agent in `coo-labs/coo-memory`

- **Type**: agent-specialist _(source: declared; declared metadata.type = 'agent-specialist')_
- **Vendoring**: custom _(source: declared)_
  - marker `frontmatter.metadata`
- **Path**: `.claude/agents/session-closer.md`
- **Size**: 13350 bytes / 245 lines · description 465 chars · body 12672 chars
- **Frontmatter**: tools `Read, Bash, mcp__mem0__add_memory`; model `sonnet`
- **Git**: first 2026-05-25, last 2026-05-30, 4 commits
- **Usage**: 0 invocations across 0 sessions

> Idle-fire session-end synthesizer for coo-labs/coo-harness#148 Part B. Spawn from session-idle-watchdog.sh after the mechanical transcript export has run. Reads the just-exported transcript via transcript-fetch.sh, synthesizes a human-readable session log per the coo-logs template, writes one Mem0 episodic entry, commits both, opens a PR against vade-agent-logs. Replaces the stub-only watchdog close with a real session record. Single-shot; single-message return.

### `transcript-analyzer` — agent in `coo-labs/coo-memory`

- **Type**: agent-specialist _(source: declared; declared metadata.type = 'agent-specialist')_
- **Vendoring**: custom _(source: declared)_
  - marker `frontmatter.metadata`
- **Path**: `.claude/agents/transcript-analyzer.md`
- **Size**: 23431 bytes / 292 lines · description 408 chars · body 22757 chars
- **Frontmatter**: tools `Read, Bash`; model `sonnet`
- **Git**: first 2026-05-25, last 2026-05-30, 3 commits
- **Usage**: 0 invocations across 0 sessions

> Stage-1 sidecar generator for coo-labs/coo-logs#64. Spawn from the Night's Watch (or interactive COO) with one Claude Code session_id. Fetches the encrypted ciphertext from R2, decrypts via TRANSCRIPTS_AGE_IDENTITY, parses the redacted jsonl, and writes coo-logs/transcripts/YYYY/MM/DD/<sessionId>.analysis.json per the schema below. No MCP write authority. Single-message return on completion.

### `briefing` — skill in `coo-labs/coo-memory`

- **Type**: procedural _(source: declared; declared metadata.type = 'procedural')_
- **Vendoring**: custom _(source: declared)_
  - marker `frontmatter.metadata`
- **Path**: `.claude/skills/briefing/SKILL.md`
- **Size**: 10731 bytes / 242 lines · description 751 chars · body 9707 chars
- **Frontmatter**: argument-hint `<request|pickup|done|release> [args]`; allowed-tools `Bash, Read, Write`
- **Bundle**: scripts=1, +2 files
- **Git**: first 2026-05-30, last 2026-05-30, 2 commits
- **Usage**: 0 invocations across 0 sessions

> Manage session-handoff briefings under `briefings/`. Subcommands: `request` (file a new briefing — collision-safe NNN allocation, YAML frontmatter, fresh branch + PR), `pickup` (claim an open briefing for this session), `done` (mark a claimed briefing delivered), `release` (clear a claim without delivering). The briefing schema, index format, and per-subcommand procedures for pickup/done/release live in reference.md — loaded on demand. Use when a session needs to hand a contextual problem to another session, or when this session is about to pick one up. Don't invoke for: single-PR-sized handoffs (use an issue), tasks the same session can finish (write code instead), or known-good plans that just need execution (write a plan, not a briefing).

### `cf-workers-best-practices` — skill in `coo-labs/coo-memory`

- **Type**: reference _(source: declared; declared metadata.type = 'reference')_
- **Vendoring**: vendored _(source: declared)_
  - upstream `https://github.com/cloudflare/skills`; commit `7c449def`; snapshot 2026-04-28; marker `frontmatter.metadata`
  - local edits: _name-only (renamed for namespacing in our aggregator)_
- **Path**: `.claude/skills/cf-workers-best-practices/SKILL.md`
- **Size**: 7368 bytes / 135 lines · description 359 chars · body 6633 chars
- **Bundle**: references=2
- **Git**: first 2026-05-25, last 2026-05-30, 2 commits
- **Usage**: 0 invocations across 0 sessions

> Reviews and authors Cloudflare Workers code against production best practices. Load when writing new Workers, reviewing Worker code, configuring wrangler.jsonc, or checking for common Workers anti-patterns (streaming, floating promises, global state, secrets, bindings, observability). Biases towards retrieval from Cloudflare docs over pre-trained knowledge.

### `cf-wrangler` — skill in `coo-labs/coo-memory`

- **Type**: api-service _(source: declared; declared metadata.type = 'api-service')_
- **Vendoring**: vendored _(source: declared)_
  - upstream `https://github.com/cloudflare/skills`; commit `7c449def`; snapshot 2026-04-28; marker `frontmatter.metadata`
  - local edits: _name-only (renamed for namespacing in our aggregator)_
- **Path**: `.claude/skills/cf-wrangler/SKILL.md`
- **Size**: 18637 bytes / 930 lines · description 336 chars · body 17983 chars
- **Git**: first 2026-05-25, last 2026-05-30, 2 commits
- **Usage**: 0 invocations across 0 sessions

> Cloudflare Workers CLI for deploying, developing, and managing Workers, KV, R2, D1, Vectorize, Hyperdrive, Workers AI, Containers, Queues, Workflows, Pipelines, and Secrets Store. Load before running wrangler commands to ensure correct syntax and best practices. Biases towards retrieval from Cloudflare docs over pre-trained knowledge.

### `chat-mode` — skill in `coo-labs/coo-memory`

- **Type**: role _(source: declared; declared metadata.type = 'role')_
- **Vendoring**: custom _(source: declared)_
  - marker `frontmatter.metadata`
- **Path**: `.claude/skills/chat-mode/SKILL.md`
- **Size**: 5563 bytes / 97 lines · description 582 chars · body 4773 chars
- **Frontmatter**: argument-hint `optional starting topic`
- **Git**: first 2026-05-25, last 2026-05-30, 4 commits
- **Usage**: 0 invocations across 0 sessions

> Boot a chat-time COO session and frame the dialogue register. Performs full COO boot, then explains chat-mode — the register where substantive dialogue can produce binding output (memo, retro, PR) through conversation rather than commission. Use when the user wants reflective conversation about substrate, patterns, or framing. Don't invoke for narrow code-task work (standard COO), executive sweep (`/exec-mode`), or play-not-work sessions (`/play-mode` when it lands, coo-labs/coo-memory#312). Worked example: MEMO-2026-05-03-b4ye + `retrospectives/2026-05-03_what-works-and-why.md`.

### `commission-retrospective` — skill in `coo-labs/coo-memory`

- **Type**: procedural _(source: declared; declared metadata.type = 'procedural')_
- **Vendoring**: custom _(source: declared)_
  - marker `frontmatter.metadata`
- **Path**: `.claude/skills/commission-retrospective/SKILL.md`
- **Size**: 9676 bytes / 211 lines · description 620 chars · body 8492 chars
- **Frontmatter**: argument-hint `--since <YYYY-MM-DD> [--until <YYYY-MM-DD>] [--prs <list>] [--focus "<question>"] [--slug <slug>] [--open-pr] | --scope ...`; allowed-tools `Bash, Read, Write, Task`
- **Bundle**: scripts=1, templates=3
- **Git**: first 2026-05-25, last 2026-05-30, 4 commits
- **Usage**: 0 invocations across 0 sessions

> Commission an impartial project-historian retrospective on a window of project work. Use when a pivotal event fires per SOP-CULTURE-001 §2d (prime-directive reinterpretation, new/retired agent role, multi-week epic closes or pivots, governance rule revised via committee, security finding reshaping ops, substrate-capture indicator firing, persistent integrity-check Group F degradation), or when `/commission-retrospective` is invoked directly. Orchestrates two impartial evidence sub-agents in parallel (memos-and-essays analyst, PR/issue-graph analyst), then produces a draft retrospective in the voice of commissions

### `day-overview` — skill in `coo-labs/coo-memory`

- **Type**: procedural _(source: declared; declared metadata.type = 'procedural')_
- **Vendoring**: custom _(source: declared)_
  - marker `frontmatter.metadata`
- **Path**: `.claude/skills/day-overview/SKILL.md`
- **Size**: 12243 bytes / 296 lines · description 493 chars · body 11431 chars
- **Frontmatter**: argument-hint `[--date YYYY-MM-DD] [--end YYYY-MM-DD] [--no-ship] [--post]`; allowed-tools `Bash, Read, Write, Edit`
- **Bundle**: scripts=1
- **Git**: first 2026-05-25, last 2026-05-30, 5 commits
- **Usage**: 0 invocations across 0 sessions

> Produce a day-overview retrospective — briefing-shaped synthesis of a day's shipped work (memos, PRs, integrity-check state) grouped into lanes, with follow-ups and candidate next actions. Use at end-of-day or to summarize a window of work. Default flow ships (writes file, commits, opens PR); `--no-ship` stops at file write; `--post` also posts to vade-canvas Retrospectives Discussions. Don't invoke for routine status updates (use `/status-check`) or single-PR retrospectives (write a memo).

### `debug-mode` — skill in `coo-labs/coo-memory`

- **Type**: role _(source: declared; declared metadata.type = 'role')_
- **Vendoring**: custom _(source: declared)_
  - marker `frontmatter.metadata`
- **Path**: `.claude/skills/debug-mode/SKILL.md`
- **Size**: 10581 bytes / 227 lines · description 804 chars · body 9549 chars
- **Frontmatter**: argument-hint `optional starting hypothesis or surface name`
- **Git**: first 2026-05-25, last 2026-05-30, 3 commits
- **Usage**: 0 invocations across 0 sessions

> Enter a runtime/boot-pipeline debug investigation session. Inventories all diagnostic surfaces the substrate produces (boot logs, integrity-check report, bootstrap-trace runs, watchdog logs, session transcripts, runtime check scripts), surfaces current state in one pass, and orients the agent to use them rather than re-derive each from scratch. User-invocable only — `/debug-mode [optional starting hypothesis]`. Use when investigating a boot failure, a degraded invariant, an unexpected hook behavior, or a substrate-level "why did X happen" question that wants more than one log file to answer. Don't invoke for narrow code-task debugging (just read the file), application bugs (use a unit test or repro), or production incidents (this skill is scoped to the COO's own substrate, not VADE end-users).

### `end-session` — skill in `coo-labs/coo-memory`

- **Type**: procedural _(source: declared; declared metadata.type = 'procedural')_
- **Vendoring**: custom _(source: declared)_
  - marker `frontmatter.metadata`
- **Path**: `.claude/skills/end-session/SKILL.md`
- **Size**: 6592 bytes / 154 lines · description 542 chars · body 5871 chars
- **Frontmatter**: allowed-tools `Bash, Read, Write, Edit, mcp__mem0__add_memory`
- **Git**: first 2026-05-25, last 2026-05-30, 6 commits
- **Usage**: 0 invocations across 0 sessions

> Run the COO session-end checklist — externalization reflection, plan-file commit, Mem0 episodic entry, memo-sync if needed, coo-logs session log, Journal consideration, transcript-export sidecar commit. Use when wrapping up a working session, about to close the terminal or container, finishing the day's COO work, or when Ven says "we're done" / "end session" / "wrap up". Writes a marker file so the Stop hook knows cleanup is done. Do NOT invoke mid-task — only at the actual end of a session, once all substantive work is complete.

### `exec-mode` — skill in `coo-labs/coo-memory`

- **Type**: role _(source: declared; declared metadata.type = 'role')_
- **Vendoring**: custom _(source: declared)_
  - marker `frontmatter.metadata`
- **Path**: `.claude/skills/exec-mode/SKILL.md`
- **Size**: 4489 bytes / 88 lines · description 990 chars · body 3305 chars
- **Frontmatter**: argument-hint `optional scope hint, or --revise-persona`
- **Git**: first 2026-05-25, last 2026-05-30, 6 commits
- **Usage**: 0 invocations across 0 sessions

> Load the executive persona for sessions where the natural shape is delegate exploration → preserve main-context for decisions and action → reflect on state and priorities. Three modes fit: sweep/cleanup, strategic reflection, or both. Reads `personas/exec-mode.md` (the persona doctrine, including its discipline rollup folded from prior retrospectives with per-rule provenance), adopts the discipline, then asks user for scope. Invoke as `/exec-mode --revise-persona` to enter persona-revision mode (re-introduces read-all-retros + plan-mode REQUIRED + adversarial-auditor gates per the persona's `Persona-revision discipline` section). Use when starting a consolidation pass on open PRs/issues, when reflecting on substrate state and priorities, or when revising the persona itself. Don't invoke for narrow code-task work, single-PR review, or anything where standard COO discipline already fits — exec-mode is bias-overlay for broad-scope sessions, not a wrapper around the standard COO.

### `manage-project` — skill in `coo-labs/coo-memory`

- **Type**: api-service _(source: declared; declared metadata.type = 'api-service')_
- **Vendoring**: custom _(source: declared)_
  - marker `frontmatter.metadata`
- **Path**: `.claude/skills/manage-project/SKILL.md`
- **Size**: 4219 bytes / 86 lines · description 527 chars · body 3326 chars
- **Frontmatter**: allowed-tools `Bash(gh *) Bash(python3 *) Read`
- **Bundle**: scripts=4, +1 dirs
- **Git**: first 2026-05-25, last 2026-05-30, 7 commits
- **Usage**: 0 invocations across 0 sessions

> VADE org project board — project-item fields (Status / Owner / Milestone), views, milestones, item triage, drift check. **This is the project-board layer** — for issue-level fields (Type / Priority / Readiness / Effort) and issue types, see `operations/issue-fields-and-types.md` (different API, different layer). Use when working with the project at https://github.com/orgs/coo-labs/projects/1, adding issues, setting Status / Owner / Milestone, opening views, asking about project structure, or checking schema-vs-live drift.

### `memo` — skill in `coo-labs/coo-memory`

- **Type**: procedural _(source: declared; declared metadata.type = 'procedural')_
- **Vendoring**: custom _(source: declared)_
  - marker `frontmatter.metadata`
- **Path**: `.claude/skills/memo/SKILL.md`
- **Size**: 15391 bytes / 431 lines · description 655 chars · body 14469 chars
- **Frontmatter**: argument-hint `["Title"] [--dir <path>] [--supersedes <id>]`; allowed-tools `Bash, Read, Write`
- **Git**: first 2026-05-25, last 2026-05-30, 5 commits
- **Usage**: 0 invocations across 0 sessions

> Draft and file a COO memo per `operations/memo_protocol.md`. Generates a random ID for today (`YYYY-MM-DD-XXXX`, 4-char base32 lowercase suffix from a Crockford-derived alphabet), renders the canonical skeleton, and writes one self-contained file under `memos/`. Per-memo files (post-issue-#210) eliminate merge-conflict surface on parallel memo PRs — two parallel sessions never collide. Use to record a binding decision, name a new convention, or mark a supersession of an older memo. Don't invoke for: single-task notes (write a comment in the issue), session reflection (write a retrospective), or operational status (update the GitHub project board).

### `memo-audit` — skill in `coo-labs/coo-memory`

- **Type**: procedural _(source: declared; declared metadata.type = 'procedural')_
- **Vendoring**: custom _(source: declared)_
  - marker `frontmatter.metadata`
- **Path**: `.claude/skills/memo-audit/SKILL.md`
- **Size**: 11075 bytes / 282 lines · description 505 chars · body 10343 chars
- **Frontmatter**: argument-hint `--apply`; allowed-tools `Bash, Read, mcp__mem0__search_memories`
- **Git**: first 2026-05-25, last 2026-05-30, 4 commits
- **Usage**: 0 invocations across 0 sessions

> Full-fidelity audit of the Mem0 `memo_pointer` layer against `memos/memo_index.json`. Catches body / title / supersedes / file_path drift that `/memo-sync` doesn't close (memo-sync reconciles presence; memo-audit reconciles content). Read-only by default; `--apply` to delete-then-add mismatches via REST. Use after a multi-session memo migration, when ID-slot reuse is suspected, when a memo body or supersedes field looks drifted, or periodically as corpus integrity check before a release or milestone.

### `memo-query` — skill in `coo-labs/coo-memory`

- **Type**: procedural _(source: declared; declared metadata.type = 'procedural')_
- **Vendoring**: custom _(source: declared)_
  - marker `frontmatter.metadata`
- **Path**: `.claude/skills/memo-query/SKILL.md`
- **Size**: 7379 bytes / 177 lines · description 360 chars · body 6743 chars
- **Frontmatter**: argument-hint `memo-id | keyword | YYYY-MM-DD..YYYY-MM-DD | --semantic "<query>"`; allowed-tools `Bash, Read, mcp__mem0__search_memories`
- **Bundle**: scripts=1
- **Git**: first 2026-05-25, last 2026-05-30, 4 commits
- **Usage**: 0 invocations across 0 sessions

> Query the COO memo index by memo ID, keyword, date range, or natural-language semantic search. Use to look up prior decisions; `--semantic` for concept queries (routes through the `memo-search` skill via Mem0). Invoked as `/memo-query <id|keyword|YYYY-MM-DD..YYYY-MM-DD>` for literal lookups, or `/memo-query --semantic "<query>"` for body-text concept search.

### `memo-search` — skill in `coo-labs/coo-memory`

- **Type**: procedural _(source: declared; declared metadata.type = 'procedural')_
- **Vendoring**: custom _(source: declared)_
  - marker `frontmatter.metadata`
- **Path**: `.claude/skills/memo-search/SKILL.md`
- **Size**: 8265 bytes / 195 lines · description 669 chars · body 7450 chars
- **Git**: first 2026-05-25, last 2026-05-30, 5 commits
- **Usage**: 0 invocations across 0 sessions

> Find memos under `memos/` by natural-language query via Mem0 semantic search over the `memo_pointer` layer. Use when the user asks "do we have memos about X?" or "what have we decided re: Y?", when keyword `/memo-query <word>` returned too few hits (titles are keyword-indexed but bodies are not), when the current task or plan context suggests prior COO decisions may be relevant, or when `/memo-query --semantic "<query>"` is invoked. Returns memo IDs + per-file paths; the caller reads full text from `memos/<id>.md` via the printed `cat` command. Don't rely on keyword `/memo-query` alone — it has an ~88% body-miss rate on concept queries (see MEMO-2026-04-24-05).

### `memo-sync` — skill in `coo-labs/coo-memory`

- **Type**: procedural _(source: declared; declared metadata.type = 'procedural')_
- **Vendoring**: custom _(source: declared)_
  - marker `frontmatter.metadata`
- **Path**: `.claude/skills/memo-sync/SKILL.md`
- **Size**: 10952 bytes / 262 lines · description 586 chars · body 10124 chars
- **Frontmatter**: argument-hint `--dry-run`; allowed-tools `Bash, Read, mcp__mem0__search_memories`
- **Git**: first 2026-05-25, last 2026-05-30, 4 commits
- **Usage**: 0 invocations across 0 sessions

> Reconcile the Mem0 `memo_pointer` layer against `memos/memo_index.json` so the semantic search surface stays current with the per-memo files in `memos/`. Use whenever a new or revised memo lands in `memos/`, when the user invokes `/memo-sync` or asks "is the semantic layer up to date?", when `/memo-query --semantic` misses a query you'd expect to match (probable staleness), or before ending a session in which a memo was issued. Implements SOP-MEM-001 §2g + §3 `infer=false` exception; do not skip a sync on the theory that "someone else will run it" — the layer goes stale silently.

### `peer-review` — skill in `coo-labs/coo-memory`

- **Type**: review _(source: declared; declared metadata.type = 'review')_
- **Vendoring**: custom _(source: declared)_
  - marker `frontmatter.metadata`
- **Path**: `.claude/skills/peer-review/SKILL.md`
- **Size**: 18264 bytes / 370 lines · description 1412 chars · body 16518 chars
- **Frontmatter**: argument-hint `<file-path> [--roles "r1,r2,r3"] [--n <count>] [--no-decompose]`; allowed-tools `Read, Bash, Write, Task`
- **Bundle**: evals=1
- **Git**: first 2026-05-25, last 2026-05-30, 6 commits
- **Usage**: 0 invocations across 0 sessions

> Commission three (or N) independent peer reviewers on a long-form authored artifact — essay, paper, foundation doc, RFC, design proposal, plan — and synthesize their feedback. Dispatches sub-agents in parallel via the Task tool, each with a role-specific lens (defaults adapt to the document type — e.g. philosophy essay → analytic phil of mind + frontier-lab ML researcher with phil training + historian/phil of science; engineering RFC → senior systems engineer + security/ops + product-strategy outside lens), each producing strongest-moves / weak-points / missing-considerations / 3–5 concrete revision suggestions. Then, only on explicit user confirmation (never automatically), decomposes the reviews into a trackable atomic-issue revision pipeline on GitHub — parent epic + per-reviewer sub-epic + N atom issues + implementer briefing for asynchronous per-atom PR sessions. Invoke when the user asks for "peer review", "multi-lens review", "independent critique", "feedback from a [philosopher/engineer/historian/X]", "different angles on this draft", or "what would N people from different backgrounds say about this" — even if they don't explicitly say "peer review" but clearly want cross-lens feedback before publishing or shipping. Don't invoke for quick copyedit, single-reviewer asks, code review, operational artifacts (PRs/issues/configs), or short pieces (<1000 words); those are different work.

### `post-discussion` — skill in `coo-labs/coo-memory`

- **Type**: procedural _(source: declared; declared metadata.type = 'procedural')_
- **Vendoring**: custom _(source: declared)_
  - marker `frontmatter.metadata`
- **Path**: `.claude/skills/post-discussion/SKILL.md`
- **Size**: 12197 bytes / 276 lines · description 509 chars · body 11484 chars
- **Frontmatter**: allowed-tools `Bash, Read, Write`
- **Git**: first 2026-05-25, last 2026-05-30, 4 commits
- **Usage**: 0 invocations across 0 sessions

> Post a category-aware discussion to coo-labs/vade-canvas with title-format enforcement per category, citation form pre-applied, pre-fetched repo + category + label IDs, body-template stubs, and post-and-link return. Invoke when authoring a new discussion thread in one of the seven coo-labs categories (Announcements / Coordination / RFCs / Q&A / Retrospectives / COO essays / Journal). Do NOT invoke for replying to existing threads (use `gh api graphql` directly), closing threads, or non-discussion comments.

### `postmerge-check` — skill in `coo-labs/coo-memory`

- **Type**: procedural _(source: declared; declared metadata.type = 'procedural')_
- **Vendoring**: custom _(source: declared)_
  - marker `frontmatter.metadata`
- **Path**: `.claude/skills/postmerge-check/SKILL.md`
- **Size**: 7818 bytes / 128 lines · description 398 chars · body 7154 chars
- **Frontmatter**: argument-hint `[<num> | <repo>#<num> ...] [--since <duration>]`; allowed-tools `Bash, Read`
- **Bundle**: scripts=1
- **Git**: first 2026-05-25, last 2026-05-30, 4 commits
- **Usage**: 0 invocations across 0 sessions

> Fetch recently merged coo-labs PRs (or specified PR refs), extract `## Post-merge confirmation` handoff sections, execute the steps in order, and report per-PR PASS / PARTIAL / FAIL. Use in a fresh session to verify a merge landed cleanly without copy-pasting the handoff prompt manually. Per CLAUDE.md "Handoff prompts for boot-impacting PRs" (canonical: MEMO-2026-04-25-03 / coo-labs/coo-memory#139).

### `quarto-docs` — skill in `coo-labs/coo-memory`

- **Type**: documentation _(source: declared; declared metadata.type = 'documentation')_
- **Vendoring**: custom _(source: declared)_
  - marker `frontmatter.metadata`
- **Path**: `.claude/skills/quarto-docs/SKILL.md`
- **Size**: 12384 bytes / 113 lines · description 1060 chars · body 11171 chars
- **Git**: first 2026-05-25, last 2026-05-30, 3 commits
- **Usage**: 0 invocations across 0 sessions

> Navigate the Quarto documentation efficiently when working on the VADE publishing site at read.vade-app.dev. Use this skill whenever a task involves Quarto — including `_quarto.yml`, navbars, sidebars, listings, themes, format options, citations, freeze, partial render, or any tldraw-style ".how do I configure X in Quarto" question. This includes any work in `coo-memory/bin/publish-site/`, `site/`, `config/publish/`, or anywhere `QUARTO_BASE_CONFIG` is touched. Quarto publishes LLM-optimized markdown bundles at quarto.org/llms.txt and per-page `.llms.md` URLs; this skill teaches which page to fetch and how to navigate so agents don't hallucinate YAML keys, nest options under the wrong parent (`format.html.sidebar` is wrong — `sidebar` is top-level under `website`), or guess at listing-type/theme-extension semantics. Trigger whenever the user mentions Quarto, qmd, _quarto.yml, listings, navbar, sidebar, cosmo, brand, theme, freeze, render, page-navigation, or is clearly working on `read.vade-app.dev` even if "Quarto" isn't named explicitly.

### `status-check` — skill in `coo-labs/coo-memory`

- **Type**: procedural _(source: declared; declared metadata.type = 'procedural')_
- **Vendoring**: custom _(source: declared)_
  - marker `frontmatter.metadata`
- **Path**: `.claude/skills/status-check/SKILL.md`
- **Size**: 5905 bytes / 141 lines · description 478 chars · body 5223 chars
- **Frontmatter**: allowed-tools `Read`
- **Git**: first 2026-05-25, last 2026-05-30, 3 commits
- **Usage**: 0 invocations across 0 sessions

> Run a six-item read-only grounding audit (who/what/where/next/decision/resource). Use deliberately at the start of a session, after a memory-layer migration, or when you suspect episodic memory drift. Works from any repo without setup — no Mem0, no hooks, no env vars required. A non-COO agent in a foreign repo gets sensible partial output via the `⚠ not grounded` marker. Don't invoke for routine work — this is a deliberate audit, not a wrapper around CLAUDE.md context-load.

### `tag-milestone` — skill in `coo-labs/coo-memory`

- **Type**: procedural _(source: declared; declared metadata.type = 'procedural')_
- **Vendoring**: custom _(source: declared)_
  - marker `frontmatter.metadata`
- **Path**: `.claude/skills/tag-milestone/SKILL.md`
- **Size**: 8580 bytes / 259 lines · description 404 chars · body 7902 chars
- **Frontmatter**: argument-hint `<nickname> [--date YYYY-MM-DD] [--annotation "..."] [--dry-run] [--yes]`; allowed-tools `Bash, Read`
- **Git**: first 2026-05-25, last 2026-05-30, 3 commits
- **Usage**: 0 invocations across 0 sessions

> Create a "Working milestone" annotated tag at HEAD across all five coo-labs repos and push via the GitHub API. Use when the system reaches a clean, demonstrably-running state worth marking as a baseline (post-major-refactor, post-cloud-rebuild, post-epic-close). Refuses on dirty working tree, branch divergence from origin/main, or pre-existing tag. Confirms with the user before pushing unless `--yes`.

### `tool-creator` — skill in `coo-labs/coo-memory`

- **Type**: meta _(source: declared; declared metadata.type = 'meta')_
- **Vendoring**: custom _(source: declared)_
  - marker `frontmatter.metadata`
- **Path**: `.claude/skills/tool-creator/SKILL.md`
- **Size**: 20822 bytes / 462 lines · description 705 chars · body 19796 chars
- **Bundle**: templates=4
- **Git**: first 2026-05-25, last 2026-05-30, 4 commits
- **Usage**: 0 invocations across 0 sessions

> Author a new VADE skill (the Anthropic-recommended primitive for slash-invoked workflows and reusable agent playbooks). Walks the operator through capability description → inventory check → frontmatter choice → draft → operator review → adversarial-auditor pass → TOOLS.md registration → PR. v1 emits a single `.claude/skills/<name>/SKILL.md` per invocation; subagents (`.claude/agents/`), personas (`personas/`), hooks (settings.json), and compound primitives are deferred to v2+. Use when externalizing a recurring pattern or session-end-noticed capability into a `/foo` skill or auto-discoverable skill. Do NOT invoke for one-off scripts, in-place file edits, or refactors outside v1's primitive scope.

### `upstream-feedback` — skill in `coo-labs/coo-memory`

- **Type**: reference _(source: declared; declared metadata.type = 'reference')_
- **Vendoring**: custom _(source: declared)_
  - marker `frontmatter.metadata`
- **Path**: `.claude/skills/upstream-feedback/SKILL.md`
- **Size**: 3989 bytes / 49 lines · description 304 chars · body 3127 chars
- **Frontmatter**: allowed-tools `Read, Bash, WebFetch, Write`
- **Bundle**: references=1
- **Git**: first 2026-05-25, last 2026-05-30, 3 commits
- **Usage**: 0 invocations across 0 sessions

> Frame a comment, issue, or PR-thread reply to an external maintainer — vendor, open-source project, public-preview discussion, GitHub Community — so a stranger can act on it without re-investigating. Covers bug reports, feature requests, API-gap reports, and PR contributions to repos outside coo-labs/*.

### `dispatching-parallel-agents` — agent in `coo-labs/skills`

- **Type**: agent-orchestrator _(source: declared; declared metadata.type = 'agent-orchestrator')_
- **Vendoring**: vendored-customized _(source: declared)_
  - upstream `https://github.com/obra/superpowers`; commit `9ccce3bf`; marker `frontmatter.metadata`
  - local edits: _frontmatter added; test-failure framing generalized to independent problem domains_
- **Path**: `agents/dispatching-parallel-agents.md`
- **Size**: 5604 bytes / 147 lines · description 185 chars · body 5024 chars
- **Frontmatter**: model `sonnet`
- **Git**: first 2026-05-11, last 2026-05-30, 2 commits
- **Usage**: 0 invocations across 0 sessions

> Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies. Cherry-picked from obra/superpowers; adapted for any Claude Code environment.

### `emancipatory-auditor` — agent in `coo-labs/skills`

- **Type**: agent-auditor _(source: declared; declared metadata.type = 'agent-auditor' · under reference/ subdir)_
- **Vendoring**: custom _(source: declared)_
  - marker `frontmatter.metadata`
- **Path**: `agents/reference/emancipatory-auditor.md`
- **Size**: 9001 bytes / 156 lines · description 348 chars · body 8462 chars
- **Frontmatter**: tools `Read, Bash, WebFetch, Agent`; model `sonnet`
- **Git**: first 2026-05-11, last 2026-05-30, 3 commits
- **Usage**: 0 invocations across 0 sessions

> Adversarial Phase-3 teammate. Enforces MEMO 2026-04-20-01's double-clause (subject AND emancipatory) on every artifact the team ships. Drops anything scoring 2/0 or 0/2. Distinct from the safety-auditor — they enforce governance memos; you enforce the prime directive's interpretation. Spawn as a teammate when Phase 3 needs the adoption-test gate.

### `lineage-interpreter` — agent in `coo-labs/skills`

- **Type**: agent-specialist _(source: declared; declared metadata.type = 'agent-specialist')_
- **Vendoring**: custom _(source: declared)_
  - marker `frontmatter.metadata`
- **Path**: `agents/lineage-interpreter.md`
- **Size**: 9327 bytes / 115 lines · description 756 chars · body 8333 chars
- **Frontmatter**: tools `Read, Write, Edit, Bash, WebFetch, WebSearch, Agent`; model `opus`
- **Git**: first 2026-05-11, last 2026-05-30, 2 commits
- **Usage**: 0 invocations across 0 sessions

> Spawn for interpretive-history work on a cultural corpus — argues a thesis about what the corpus IS as a cultural form, not what it claims about itself. Genre is Wootton/Harari interpretive history (argumentative, defamiliarizing, reader-out, takes a stance). Methodology: corpus-map (delegated to research-investigator) → primary-source read → candidate-thesis-shapes → synthesis essay → three-instance peer-review pass → patches and successor-parking. Distinct from research-investigator (which reports facts without taking a stance) and from a project-historian role (which documents and analyzes inside the corpus's own frame). Use when an orchestrator needs a theory of a cultural narrative, not a survey of facts. Reusable across any cultural corpus.

### `rationalization-discriminator` — agent in `coo-labs/skills`

- **Type**: agent-reviewer _(source: declared; declared metadata.type = 'agent-reviewer')_
- **Vendoring**: custom _(source: declared)_
  - marker `frontmatter.metadata`
- **Path**: `agents/rationalization-discriminator.md`
- **Size**: 7297 bytes / 79 lines · description 551 chars · body 6543 chars
- **Frontmatter**: tools `Read, Bash, WebFetch, Agent`; model `sonnet`
- **Git**: first 2026-05-11, last 2026-05-30, 2 commits
- **Usage**: 0 invocations across 0 sessions

> Read-only adversarial auditor for chain reasoning that fits the load-substrate → prior-dissolves → action-follows shape (MEMO-2026-05-09-wzzh). Asks one load-bearing question — "is this argument load-bearing or rationalizing?" — and reports a path-quality verdict separate from the outcome. Distinct from safety-auditor (governance-memo compliance) and emancipatory-auditor (subject+emancipatory clause); this role audits *path*, not *clauses*. Spawn when the COO notices the shape in its own move and wants an external read before banking the action.

### `research-investigator` — agent in `coo-labs/skills`

- **Type**: agent-researcher _(source: declared; declared metadata.type = 'agent-researcher')_
- **Vendoring**: custom _(source: declared)_
  - marker `frontmatter.metadata`
- **Path**: `agents/research-investigator.md`
- **Size**: 3178 bytes / 78 lines · description 211 chars · body 2790 chars
- **Frontmatter**: tools `Read, Bash, WebFetch, Agent`; model `sonnet`
- **Git**: first 2026-05-11, last 2026-05-30, 2 commits
- **Usage**: 0 invocations across 0 sessions

> Generic research sub-agent. Spawn when an orchestrator needs focused, schema-driven investigation of a bounded question across a specified file corpus. Reusable across any repo — no project-specific assumptions.

### `safety-auditor` — agent in `coo-labs/skills`

- **Type**: agent-auditor _(source: declared; declared metadata.type = 'agent-auditor' · under reference/ subdir)_
- **Vendoring**: custom _(source: declared)_
  - marker `frontmatter.metadata`
- **Path**: `agents/reference/safety-auditor.md`
- **Size**: 8853 bytes / 127 lines · description 309 chars · body 8379 chars
- **Frontmatter**: tools `Read, Bash, WebFetch, Agent`; model `sonnet`
- **Git**: first 2026-05-11, last 2026-05-30, 3 commits
- **Usage**: 0 invocations across 0 sessions

> Adversarial Phase-3 teammate. Gate-keeper against governance memos (-08 Tier-2, -10 Mem0 content rule, -14 sync paths, -19 spend cap, -22-01 PAT/identity discipline). Reviews each track specialist's deliverables and blocks anything that fails. Spawn as a teammate when Phase 3 needs adversarial safety review.

### `adapt-skill` — skill in `coo-labs/skills`

- **Type**: meta _(source: declared; declared metadata.type = 'meta')_
- **Vendoring**: custom _(source: declared)_
  - marker `frontmatter.metadata`
- **Path**: `skills/adapt-skill/SKILL.md`
- **Size**: 12390 bytes / 298 lines · description 521 chars · body 11576 chars
- **Frontmatter**: argument-hint `<skill-or-agent-name> [--user] [--dry-run]`; allowed-tools `Bash, Read, Write, Edit, AskUserQuestion`
- **Bundle**: scripts=1, +2 files
- **Git**: first 2026-05-12, last 2026-05-30, 4 commits
- **Usage**: 0 invocations across 0 sessions

> Adapt a reference skill or agent from this repo into a working installed primitive for the current substrate. Reads the target's `# Setup hints` manifest, conducts a structured interview, substitutes substrate-coupled surfaces with the user's answers, and writes the adapted skill to `.claude/skills/<name>/` (or agent to `.claude/agents/<name>.md`). Run once per reference skill the user wants to install. Don't invoke for substrate-agnostic skills under `skills/` proper — those install verbatim via `setup/install.sh`.

### `briefing` — skill in `coo-labs/skills`

- **Type**: procedural _(source: declared; declared metadata.type = 'procedural' · under reference/ subdir)_
- **Vendoring**: custom _(source: declared)_
  - marker `frontmatter.metadata`
- **Path**: `skills/reference/briefing/SKILL.md`
- **Size**: 10731 bytes / 242 lines · description 751 chars · body 9707 chars
- **Frontmatter**: argument-hint `<request|pickup|done|release> [args]`; allowed-tools `Bash, Read, Write`
- **Bundle**: scripts=1, +2 files
- **Git**: first 2026-05-30, last 2026-05-30, 2 commits
- **Usage**: 0 invocations across 0 sessions

> Manage session-handoff briefings under `briefings/`. Subcommands: `request` (file a new briefing — collision-safe NNN allocation, YAML frontmatter, fresh branch + PR), `pickup` (claim an open briefing for this session), `done` (mark a claimed briefing delivered), `release` (clear a claim without delivering). The briefing schema, index format, and per-subcommand procedures for pickup/done/release live in reference.md — loaded on demand. Use when a session needs to hand a contextual problem to another session, or when this session is about to pick one up. Don't invoke for: single-PR-sized handoffs (use an issue), tasks the same session can finish (write code instead), or known-good plans that just need execution (write a plan, not a briefing).

### `canvas-ui` — skill in `coo-labs/skills`

- **Type**: reference _(source: declared; declared metadata.type = 'reference')_
- **Vendoring**: custom _(source: declared)_
  - marker `frontmatter.metadata`
- **Path**: `skills/canvas-ui/SKILL.md`
- **Size**: 19215 bytes / 184 lines · description 896 chars · body 18138 chars
- **Bundle**: references=1
- **Git**: first 2026-05-11, last 2026-05-30, 2 commits
- **Usage**: 0 invocations across 0 sessions

> Apply tldraw canvas frontend conventions and avoid recurring landmines — extracted from a production tldraw-based app. Use this skill whenever you're working in a tldraw-based codebase on anything that touches the canvas — adding or modifying a custom shape, wiring shell UI, mutating shapes through an MCP/WebSocket bridge, asset stores, snapshot persistence, library / catalog / shape-panel surfaces, or anywhere `tldraw` or `@tldraw/*` is imported. Trigger even when the prompt only mentions "the canvas," "a shape," "AppShell," "persistenceKey," "asset store," "TLAssetStore," "ShapeUtil," "BindingUtil," "snapshot," "the editor," or "tldraw" without naming the skill — and especially trigger before opening a PR that changes any tldraw-touching file. This skill is the anti-patterns and conventions layer; for SDK reference / doc URLs, also consult the `tldraw-docs` skill (the two compose).

### `chat-mode` — skill in `coo-labs/skills`

- **Type**: role _(source: declared; declared metadata.type = 'role' · under reference/ subdir)_
- **Vendoring**: custom _(source: declared)_
  - marker `frontmatter.metadata`
- **Path**: `skills/reference/chat-mode/SKILL.md`
- **Size**: 9678 bytes / 141 lines · description 586 chars · body 8854 chars
- **Frontmatter**: argument-hint `optional starting topic`
- **Git**: first 2026-05-11, last 2026-05-30, 4 commits
- **Usage**: 0 invocations across 0 sessions

> Boot a chat-time COO session and frame the dialogue register. Performs full COO boot, then explains chat-mode — the register where substantive dialogue can produce binding output (memo, retro, PR) through conversation rather than commission. Use when the user wants reflective conversation about substrate, patterns, or framing. Don't invoke for narrow code-task work (standard COO), executive sweep (`/exec-mode`), or play-not-work sessions (`/play-mode` when it lands, coo-labs/coo-memory#312). Worked example: MEMO-2026-05-03-b4ye + `retrospectives/2026-05-03_what-works-and-why.md`.

### `commission-retrospective` — skill in `coo-labs/skills`

- **Type**: procedural _(source: declared; declared metadata.type = 'procedural' · under reference/ subdir)_
- **Vendoring**: custom _(source: declared)_
  - marker `frontmatter.metadata`
- **Path**: `skills/reference/commission-retrospective/SKILL.md`
- **Size**: 19588 bytes / 394 lines · description 620 chars · body 18385 chars
- **Frontmatter**: argument-hint `--since <YYYY-MM-DD> [--until <YYYY-MM-DD>] [--prs <list>] [--focus "<question>"] [--slug <slug>] [--open-pr] | --scope ...`; allowed-tools `Bash, Read, Write, Task`
- **Bundle**: scripts=1, templates=3
- **Git**: first 2026-05-12, last 2026-05-30, 3 commits
- **Usage**: 0 invocations across 0 sessions

> Commission an impartial project-historian retrospective on a window of project work. Use when a pivotal event fires per SOP-CULTURE-001 §2d (prime-directive reinterpretation, new/retired agent role, multi-week epic closes or pivots, governance rule revised via committee, security finding reshaping ops, substrate-capture indicator firing, persistent integrity-check Group F degradation), or when `/commission-retrospective` is invoked directly. Orchestrates two impartial evidence sub-agents in parallel (memos-and-essays analyst, PR/issue-graph analyst), then produces a draft retrospective in the voice of commissions

### `day-overview` — skill in `coo-labs/skills`

- **Type**: procedural _(source: declared; declared metadata.type = 'procedural' · under reference/ subdir)_
- **Vendoring**: custom _(source: declared)_
  - marker `frontmatter.metadata`
- **Path**: `skills/reference/day-overview/SKILL.md`
- **Size**: 19677 bytes / 451 lines · description 493 chars · body 18853 chars
- **Frontmatter**: argument-hint `[--date YYYY-MM-DD] [--end YYYY-MM-DD] [--no-ship] [--post]`; allowed-tools `Bash, Read, Write, Edit`
- **Bundle**: scripts=1
- **Git**: first 2026-05-12, last 2026-05-30, 4 commits
- **Usage**: 0 invocations across 0 sessions

> Produce a day-overview retrospective — briefing-shaped synthesis of a day's shipped work (memos, PRs, integrity-check state) grouped into lanes, with follow-ups and candidate next actions. Use at end-of-day or to summarize a window of work. Default flow ships (writes file, commits, opens PR); `--no-ship` stops at file write; `--post` also posts to vade-canvas Retrospectives Discussions. Don't invoke for routine status updates (use `/status-check`) or single-PR retrospectives (write a memo).

### `end-session` — skill in `coo-labs/skills`

- **Type**: procedural _(source: declared; declared metadata.type = 'procedural' · under reference/ subdir)_
- **Vendoring**: custom _(source: declared)_
  - marker `frontmatter.metadata`
- **Path**: `skills/reference/end-session/SKILL.md`
- **Size**: 15497 bytes / 347 lines · description 542 chars · body 14758 chars
- **Frontmatter**: allowed-tools `Bash, Read, Write, Edit, mcp__mem0__add_memory`
- **Git**: first 2026-05-12, last 2026-05-30, 4 commits
- **Usage**: 0 invocations across 0 sessions

> Run the COO session-end checklist — externalization reflection, plan-file commit, Mem0 episodic entry, memo-sync if needed, coo-logs session log, Journal consideration, transcript-export sidecar commit. Use when wrapping up a working session, about to close the terminal or container, finishing the day's COO work, or when Ven says "we're done" / "end session" / "wrap up". Writes a marker file so the Stop hook knows cleanup is done. Do NOT invoke mid-task — only at the actual end of a session, once all substantive work is complete.

### `exec-mode` — skill in `coo-labs/skills`

- **Type**: role _(source: declared; declared metadata.type = 'role' · under reference/ subdir)_
- **Vendoring**: custom _(source: declared)_
  - marker `frontmatter.metadata`
- **Path**: `skills/reference/exec-mode/SKILL.md`
- **Size**: 9333 bytes / 166 lines · description 994 chars · body 8130 chars
- **Frontmatter**: argument-hint `optional scope hint, or --revise-persona`
- **Bundle**: +2 files
- **Git**: first 2026-05-11, last 2026-05-30, 4 commits
- **Usage**: 0 invocations across 0 sessions

> Load the executive persona for sessions where the natural shape is delegate exploration → preserve main-context for decisions and action → reflect on state and priorities. Three modes fit: sweep/cleanup, strategic reflection, or both. Reads `personas/exec-mode.md` (the persona doctrine, including its discipline rollup folded from prior retrospectives with per-rule provenance), adopts the discipline, then asks user for scope. Invoke as `/exec-mode --revise-persona` to enter persona-revision mode (re-introduces read-all-retros + plan-mode REQUIRED + adversarial-auditor gates per the persona's `Persona-revision discipline` section). Use when starting a consolidation pass on open PRs/issues, when reflecting on substrate state and priorities, or when revising the persona itself. Don't invoke for narrow code-task work, single-PR review, or anything where standard COO discipline already fits — exec-mode is bias-overlay for broad-scope sessions, not a wrapper around the standard COO.

### `peer-review` — skill in `coo-labs/skills`

- **Type**: review _(source: declared; declared metadata.type = 'review')_
- **Vendoring**: custom _(source: declared)_
  - marker `frontmatter.metadata`
- **Path**: `skills/peer-review/SKILL.md`
- **Size**: 17842 bytes / 357 lines · description 1412 chars · body 16097 chars
- **Frontmatter**: argument-hint `<file-path> [--roles "r1,r2,r3"] [--n <count>] [--no-decompose]`; allowed-tools `Read, Bash, Write, Task`
- **Git**: first 2026-05-11, last 2026-05-30, 3 commits
- **Usage**: 0 invocations across 0 sessions

> Commission three (or N) independent peer reviewers on a long-form authored artifact — essay, paper, foundation doc, RFC, design proposal, plan — and synthesize their feedback. Dispatches sub-agents in parallel via the Task tool, each with a role-specific lens (defaults adapt to the document type — e.g. philosophy essay → analytic phil of mind + frontier-lab ML researcher with phil training + historian/phil of science; engineering RFC → senior systems engineer + security/ops + product-strategy outside lens), each producing strongest-moves / weak-points / missing-considerations / 3–5 concrete revision suggestions. Then, only on explicit user confirmation (never automatically), decomposes the reviews into a trackable atomic-issue revision pipeline on GitHub — parent epic + per-reviewer sub-epic + N atom issues + implementer briefing for asynchronous per-atom PR sessions. Invoke when the user asks for "peer review", "multi-lens review", "independent critique", "feedback from a [philosopher/engineer/historian/X]", "different angles on this draft", or "what would N people from different backgrounds say about this" — even if they don't explicitly say "peer review" but clearly want cross-lens feedback before publishing or shipping. Don't invoke for quick copyedit, single-reviewer asks, code review, operational artifacts (PRs/issues/configs), or short pieces (<1000 words); those are different work.

### `quarto-docs` — skill in `coo-labs/skills`

- **Type**: documentation _(source: declared; declared metadata.type = 'documentation')_
- **Vendoring**: custom _(source: declared)_
  - marker `frontmatter.metadata`
- **Path**: `skills/quarto-docs/SKILL.md`
- **Size**: 12086 bytes / 113 lines · description 762 chars · body 11171 chars
- **Git**: first 2026-05-11, last 2026-05-30, 2 commits
- **Usage**: 0 invocations across 0 sessions

> Navigate the Quarto documentation efficiently when working on a Quarto-based publishing site. Use this skill whenever a task involves Quarto — including `_quarto.yml`, navbars, sidebars, listings, themes, format options, citations, freeze, partial render. Quarto publishes LLM-optimized markdown bundles at quarto.org/llms.txt and per-page `.llms.md` URLs; this skill teaches which page to fetch and how to navigate so agents don't hallucinate YAML keys, nest options under the wrong parent (`format.html.sidebar` is wrong — `sidebar` is top-level under `website`), or guess at listing-type/theme-extension semantics. Trigger whenever the user mentions Quarto, qmd, _quarto.yml, listings, navbar, sidebar, cosmo, brand, theme, freeze, render, or page-navigation.

### `status-check` — skill in `coo-labs/skills`

- **Type**: procedural _(source: declared; declared metadata.type = 'procedural' · under reference/ subdir)_
- **Vendoring**: custom _(source: declared)_
  - marker `frontmatter.metadata`
- **Path**: `skills/reference/status-check/SKILL.md`
- **Size**: 8023 bytes / 186 lines · description 478 chars · body 7333 chars
- **Frontmatter**: allowed-tools `Read`
- **Git**: first 2026-05-12, last 2026-05-30, 3 commits
- **Usage**: 0 invocations across 0 sessions

> Run a six-item read-only grounding audit (who/what/where/next/decision/resource). Use deliberately at the start of a session, after a memory-layer migration, or when you suspect episodic memory drift. Works from any repo without setup — no Mem0, no hooks, no env vars required. A non-COO agent in a foreign repo gets sensible partial output via the `⚠ not grounded` marker. Don't invoke for routine work — this is a deliberate audit, not a wrapper around CLAUDE.md context-load.

### `tldraw-docs` — skill in `coo-labs/skills`

- **Type**: documentation _(source: declared; declared metadata.type = 'documentation')_
- **Vendoring**: custom _(source: declared)_
  - marker `frontmatter.metadata`
- **Path**: `skills/tldraw-docs/SKILL.md`
- **Size**: 11750 bytes / 99 lines · description 817 chars · body 10786 chars
- **Git**: first 2026-05-11, last 2026-05-30, 2 commits
- **Usage**: 0 invocations across 0 sessions

> Navigate the tldraw SDK documentation efficiently. Use this skill whenever a task involves the tldraw canvas SDK — including the Editor class, shape utils, custom shapes, bindings, tools, persistence, side effects, the store/signals system, sync, UI components, or any tldraw.dev reference. tldraw publishes LLM-optimized markdown bundles at tldraw.dev/llms*.txt plus markdown-ready individual pages; this skill teaches which bundle to fetch and how to navigate so agents don't hallucinate API signatures, grab the full mega-bundle when a narrow fetch would do, or guess at topic names that don't exist. Trigger whenever the user mentions tldraw, canvas shapes, ShapeUtil, BindingUtil, tldraw editor, custom tool, snapshot, or is clearly working in a tldraw-based codebase even if they don't name "tldraw" explicitly.

### `tool-creator` — skill in `coo-labs/skills`

- **Type**: meta _(source: declared; declared metadata.type = 'meta' · under reference/ subdir)_
- **Vendoring**: custom _(source: declared)_
  - marker `frontmatter.metadata`
- **Path**: `skills/reference/tool-creator/SKILL.md`
- **Size**: 31255 bytes / 640 lines · description 709 chars · body 30215 chars
- **Bundle**: templates=4
- **Git**: first 2026-05-12, last 2026-05-30, 3 commits
- **Usage**: 0 invocations across 0 sessions

> Author a new VADE skill (the Anthropic-recommended primitive for slash-invoked workflows and reusable agent playbooks). Walks the operator through capability description → inventory check → frontmatter choice → draft → operator review → adversarial-auditor pass → TOOLS.md registration → PR. v1 emits a single `.claude/skills/<name>/SKILL.md` per invocation; subagents (`.claude/agents/`), personas (`personas/`), hooks (settings.json), and compound primitives are deferred to v2+. Use when externalizing a recurring pattern or session-end-noticed capability into a `/foo` skill or auto-discoverable skill. Do NOT invoke for one-off scripts, in-place file edits, or refactors outside v1's primitive scope.

### `canvas-ui` — skill in `coo-labs/vade-canvas`

- **Type**: reference _(source: declared; declared metadata.type = 'reference')_
- **Vendoring**: custom _(source: declared)_
  - marker `frontmatter.metadata`
- **Path**: `.claude/skills/canvas-ui/SKILL.md`
- **Size**: 19266 bytes / 184 lines · description 949 chars · body 18138 chars
- **Bundle**: references=1, evals=1
- **Git**: first 2026-05-09, last 2026-05-30, 2 commits
- **Usage**: 0 invocations across 0 sessions

> Apply vade-canvas's canvas/tldraw frontend conventions and avoid the recurring landmines we've already learned about. Use this skill whenever you're working in vade-canvas on anything that touches the canvas — adding or modifying a custom shape under `src/shapes/`, wiring UI through `src/shell/AppShell.tsx`, mutating shapes through the MCP bridge in `src/bridge/`, the `vade-asset-store`, snapshot persistence, the library/catalog/shape-panel surfaces, or anywhere else `tldraw` or `@tldraw/*` is imported. Trigger even when the prompt only mentions "the canvas," "a shape," "AppShell," "persistenceKey," "asset store," "TLAssetStore," "ShapeUtil," "BindingUtil," "snapshot," "the editor," or "tldraw" without naming the skill — and especially trigger before opening a PR that changes any tldraw-touching file. This skill is the anti-patterns and conventions layer; for SDK reference / doc URLs, also consult the `tldraw-docs` skill (the two compose).

### `tldraw-docs` — skill in `coo-labs/vade-canvas`

- **Type**: documentation _(source: declared; declared metadata.type = 'documentation')_
- **Vendoring**: custom _(source: declared)_
  - marker `frontmatter.metadata`
- **Path**: `.claude/skills/tldraw-docs/SKILL.md`
- **Size**: 11822 bytes / 99 lines · description 889 chars · body 10786 chars
- **Bundle**: references=1
- **Git**: first 2026-05-01, last 2026-05-30, 2 commits
- **Usage**: 0 invocations across 0 sessions

> Navigate the tldraw SDK documentation efficiently. Use this skill whenever a task involves the tldraw canvas SDK — including the Editor class, shape utils, custom shapes, bindings, tools, persistence, side effects, the store/signals system, sync, UI components, or any tldraw.dev reference. This includes any work in the vade-canvas repo, which is built on tldraw. tldraw publishes LLM-optimized markdown bundles at tldraw.dev/llms*.txt plus markdown-ready individual pages; this skill teaches which bundle to fetch and how to navigate so agents don't hallucinate API signatures, grab the full mega-bundle when a narrow fetch would do, or guess at topic names that don't exist. Trigger whenever the user mentions tldraw, canvas shapes, ShapeUtil, BindingUtil, tldraw editor, custom tool, snapshot, or is clearly working in a tldraw-based codebase even if they don't name "tldraw" explicitly.
