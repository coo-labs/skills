# Claude Code skill & agent inventory

_Generated `2026-05-30T17:18:23Z` · schema `v1.0.0`._

## Summary

- **Total entries**: 57
- **By kind**: agent=15, skill=42
- **By repo**: `coo-labs/coo-harness`=4, `coo-labs/coo-memory`=32, `coo-labs/skills`=19, `coo-labs/vade-canvas`=2
- **By type**: procedural=20, agent-specialist=5, role=5, agent-auditor=4, documentation=4, meta=4, reference=4, api-service=3, agent-orchestrator=2, agent-researcher=2, agent-reviewer=2, review=2
- **By vendoring**: custom=53, vendored=4
- **Declared metadata coverage**: type 0/57 (0%), vendoring 0/57 (0%) — remainder is derived heuristically. Migration goal: shrink the heuristic share over time.

Transcripts scanned: `/root/.claude/projects` (6 files). Invocation counts are honest reports of what the scan saw — point the scanner at an archive for cross-session totals.

Repos scanned:
- `coo-labs/coo-memory` @ `7cf75aa8` (/home/user/coo-memory)
- `coo-labs/coo-harness` @ `dabd31bf` (/home/user/coo-harness)
- `coo-labs/vade-canvas` @ `baba412f` (/home/user/vade-canvas)
- `coo-labs/skills` @ `93dd8ed7` (/home/user/skills)

## Inventory by repo

### `coo-labs/coo-harness`

#### Skills (4)

| Name | Type | Vendor | Bytes | Lines | Bundle | Added | Last commit | Invocations |
|------|------|--------|-------|-------|--------|-------|-------------|-------------|
| `agentmail` | api-service | — | 7281 | 282 | references=2 | 2026-05-16 | 2026-05-16 | 0 |
| `skill-creator` | meta | vendored | 33168 | 485 | scripts=9, references=1, assets=1, agents=3, LICENSE, vendor=VENDORED.md | 2026-05-16 | 2026-05-16 | 0 |
| `tagging-taxonomy` | procedural | — | 12188 | 283 | — | 2026-05-16 | 2026-05-25 | 0 |
| `trace-timeline` | procedural | — | 9114 | 172 | — | 2026-05-20 | 2026-05-25 | 0 |

### `coo-labs/coo-memory`

#### Skills (23)

| Name | Type | Vendor | Bytes | Lines | Bundle | Added | Last commit | Invocations |
|------|------|--------|-------|-------|--------|-------|-------------|-------------|
| `briefing` | procedural | — | 10682 | 239 | scripts=1, +2 files | 2026-05-30 | 2026-05-30 | 0 |
| `cf-workers-best-practices` | reference | vendored<br>cloudflare/skills | 7095 | 127 | references=2 | 2026-05-25 | 2026-05-25 | 0 |
| `cf-wrangler` | api-service | vendored<br>cloudflare/skills | 18362 | 922 | — | 2026-05-25 | 2026-05-25 | 0 |
| `chat-mode` | role | — | 5520 | 94 | — | 2026-05-25 | 2026-05-30 | 0 |
| `commission-retrospective` | procedural | — | 9627 | 208 | scripts=1, templates=3 | 2026-05-25 | 2026-05-27 | 0 |
| `day-overview` | procedural | — | 12194 | 293 | scripts=1 | 2026-05-25 | 2026-05-30 | 0 |
| `debug-mode` | role | — | 10538 | 224 | — | 2026-05-25 | 2026-05-27 | 0 |
| `end-session` | procedural | — | 6543 | 151 | — | 2026-05-25 | 2026-05-30 | 0 |
| `exec-mode` | role | — | 4446 | 85 | — | 2026-05-25 | 2026-05-30 | 0 |
| `manage-project` | api-service | — | 4169 | 83 | scripts=4, +1 dirs | 2026-05-25 | 2026-05-27 | 0 |
| `memo` | procedural | — | 15342 | 428 | — | 2026-05-25 | 2026-05-30 | 0 |
| `memo-audit` | procedural | — | 11026 | 279 | — | 2026-05-25 | 2026-05-27 | 0 |
| `memo-query` | procedural | — | 7330 | 174 | scripts=1 | 2026-05-25 | 2026-05-27 | 0 |
| `memo-search` | procedural | — | 8216 | 192 | — | 2026-05-25 | 2026-05-30 | 0 |
| `memo-sync` | procedural | — | 10903 | 259 | — | 2026-05-25 | 2026-05-27 | 0 |
| `peer-review` | review | — | 18219 | 367 | evals=1 | 2026-05-25 | 2026-05-27 | 0 |
| `post-discussion` | procedural | — | 12148 | 273 | — | 2026-05-25 | 2026-05-27 | 0 |
| `postmerge-check` | procedural | — | 7769 | 125 | scripts=1 | 2026-05-25 | 2026-05-30 | 0 |
| `quarto-docs` | documentation | — | 12332 | 110 | — | 2026-05-25 | 2026-05-27 | 0 |
| `status-check` | procedural | — | 5856 | 138 | — | 2026-05-25 | 2026-05-26 | 0 |
| `tag-milestone` | procedural | — | 8531 | 256 | — | 2026-05-25 | 2026-05-27 | 0 |
| `tool-creator` | meta | — | 20779 | 459 | templates=4 | 2026-05-25 | 2026-05-27 | 0 |
| `upstream-feedback` | reference | — | 3941 | 46 | references=1 | 2026-05-25 | 2026-05-26 | 0 |

#### Agents (9)

| Name | Type | Vendor | Bytes | Lines | Bundle | Added | Last commit | Invocations |
|------|------|--------|-------|-------|--------|-------|-------------|-------------|
| `dispatching-parallel-agents` | agent-orchestrator | — | 5318 | 140 | — | 2026-05-25 | 2026-05-25 | 0 |
| `emancipatory-auditor` | agent-auditor | — | 4431 | 58 | — | 2026-05-25 | 2026-05-27 | 0 |
| `lineage-interpreter` | agent-specialist | — | 9246 | 112 | — | 2026-05-25 | 2026-05-27 | 0 |
| `oss-launch-issue-curator` | agent-specialist | — | 8412 | 126 | — | 2026-05-25 | 2026-05-25 | 0 |
| `rationalization-discriminator` | agent-reviewer | — | 7210 | 76 | — | 2026-05-25 | 2026-05-27 | 0 |
| `research-investigator` | agent-researcher | — | 3137 | 75 | — | 2026-05-25 | 2026-05-26 | 0 |
| `safety-auditor` | agent-auditor | — | 4273 | 49 | — | 2026-05-25 | 2026-05-25 | 0 |
| `session-closer` | agent-specialist | — | 13295 | 242 | — | 2026-05-25 | 2026-05-27 | 0 |
| `transcript-analyzer` | agent-specialist | — | 23376 | 289 | — | 2026-05-25 | 2026-05-26 | 0 |

### `coo-labs/skills`

#### Skills (13)

| Name | Type | Vendor | Bytes | Lines | Bundle | Added | Last commit | Invocations |
|------|------|--------|-------|-------|--------|-------|-------------|-------------|
| `adapt-skill` | meta | — | 12347 | 295 | scripts=1, +2 files | 2026-05-12 | 2026-05-27 | 0 |
| `briefing` | procedural | — | 10682 | 239 | scripts=1, +2 files | — | — | 0 |
| `canvas-ui` | reference | — | 19167 | 181 | references=1 | 2026-05-11 | 2026-05-11 | 0 |
| `chat-mode` | role | — | 9635 | 138 | — | 2026-05-11 | 2026-05-30 | 0 |
| `commission-retrospective` | procedural | — | 19539 | 391 | scripts=1, templates=3 | 2026-05-12 | 2026-05-12 | 0 |
| `day-overview` | procedural | — | 19628 | 448 | scripts=1 | 2026-05-12 | 2026-05-30 | 0 |
| `end-session` | procedural | — | 15448 | 344 | — | 2026-05-12 | 2026-05-30 | 0 |
| `exec-mode` | role | — | 9290 | 163 | +2 files | 2026-05-11 | 2026-05-30 | 0 |
| `peer-review` | review | — | 17797 | 354 | — | 2026-05-11 | 2026-05-21 | 0 |
| `quarto-docs` | documentation | — | 12034 | 110 | — | 2026-05-11 | 2026-05-11 | 0 |
| `status-check` | procedural | — | 7974 | 183 | — | 2026-05-12 | 2026-05-12 | 0 |
| `tldraw-docs` | documentation | — | 11698 | 96 | — | 2026-05-11 | 2026-05-11 | 0 |
| `tool-creator` | meta | — | 31212 | 637 | templates=4 | 2026-05-12 | 2026-05-12 | 0 |

#### Agents (6)

| Name | Type | Vendor | Bytes | Lines | Bundle | Added | Last commit | Invocations |
|------|------|--------|-------|-------|--------|-------|-------------|-------------|
| `dispatching-parallel-agents` | agent-orchestrator | vendored | 5318 | 140 | — | 2026-05-11 | 2026-05-11 | 0 |
| `emancipatory-auditor` | agent-auditor | — | 8949 | 153 | — | 2026-05-11 | 2026-05-12 | 0 |
| `lineage-interpreter` | agent-specialist | — | 9270 | 112 | — | 2026-05-11 | 2026-05-11 | 0 |
| `rationalization-discriminator` | agent-reviewer | — | 7244 | 76 | — | 2026-05-11 | 2026-05-11 | 0 |
| `research-investigator` | agent-researcher | — | 3123 | 75 | — | 2026-05-11 | 2026-05-11 | 0 |
| `safety-auditor` | agent-auditor | — | 8801 | 124 | — | 2026-05-11 | 2026-05-12 | 0 |

### `coo-labs/vade-canvas`

#### Skills (2)

| Name | Type | Vendor | Bytes | Lines | Bundle | Added | Last commit | Invocations |
|------|------|--------|-------|-------|--------|-------|-------------|-------------|
| `canvas-ui` | reference | — | 19218 | 181 | references=1, evals=1 | 2026-05-09 | 2026-05-09 | 0 |
| `tldraw-docs` | documentation | — | 11770 | 96 | references=1 | 2026-05-01 | 2026-05-01 | 0 |

## Cross-cut by type

### procedural (20)

- `tagging-taxonomy` (skill, `coo-labs/coo-harness`) — custom, 12188B
- `trace-timeline` (skill, `coo-labs/coo-harness`) — custom, 9114B
- `briefing` (skill, `coo-labs/coo-memory`) — custom, 10682B
- `commission-retrospective` (skill, `coo-labs/coo-memory`) — custom, 9627B
- `day-overview` (skill, `coo-labs/coo-memory`) — custom, 12194B
- `end-session` (skill, `coo-labs/coo-memory`) — custom, 6543B
- `memo` (skill, `coo-labs/coo-memory`) — custom, 15342B
- `memo-audit` (skill, `coo-labs/coo-memory`) — custom, 11026B
- `memo-query` (skill, `coo-labs/coo-memory`) — custom, 7330B
- `memo-search` (skill, `coo-labs/coo-memory`) — custom, 8216B
- `memo-sync` (skill, `coo-labs/coo-memory`) — custom, 10903B
- `post-discussion` (skill, `coo-labs/coo-memory`) — custom, 12148B
- `postmerge-check` (skill, `coo-labs/coo-memory`) — custom, 7769B
- `status-check` (skill, `coo-labs/coo-memory`) — custom, 5856B
- `tag-milestone` (skill, `coo-labs/coo-memory`) — custom, 8531B
- `briefing` (skill, `coo-labs/skills`) _(reference)_ — custom, 10682B
- `commission-retrospective` (skill, `coo-labs/skills`) _(reference)_ — custom, 19539B
- `day-overview` (skill, `coo-labs/skills`) _(reference)_ — custom, 19628B
- `end-session` (skill, `coo-labs/skills`) _(reference)_ — custom, 15448B
- `status-check` (skill, `coo-labs/skills`) _(reference)_ — custom, 7974B

### agent-specialist (5)

- `lineage-interpreter` (agent, `coo-labs/coo-memory`) — custom, 9246B
- `oss-launch-issue-curator` (agent, `coo-labs/coo-memory`) — custom, 8412B
- `session-closer` (agent, `coo-labs/coo-memory`) — custom, 13295B
- `transcript-analyzer` (agent, `coo-labs/coo-memory`) — custom, 23376B
- `lineage-interpreter` (agent, `coo-labs/skills`) — custom, 9270B

### role (5)

- `chat-mode` (skill, `coo-labs/coo-memory`) — custom, 5520B
- `debug-mode` (skill, `coo-labs/coo-memory`) — custom, 10538B
- `exec-mode` (skill, `coo-labs/coo-memory`) — custom, 4446B
- `chat-mode` (skill, `coo-labs/skills`) _(reference)_ — custom, 9635B
- `exec-mode` (skill, `coo-labs/skills`) _(reference)_ — custom, 9290B

### agent-auditor (4)

- `emancipatory-auditor` (agent, `coo-labs/coo-memory`) — custom, 4431B
- `safety-auditor` (agent, `coo-labs/coo-memory`) — custom, 4273B
- `emancipatory-auditor` (agent, `coo-labs/skills`) _(reference)_ — custom, 8949B
- `safety-auditor` (agent, `coo-labs/skills`) _(reference)_ — custom, 8801B

### documentation (4)

- `quarto-docs` (skill, `coo-labs/coo-memory`) — custom, 12332B
- `quarto-docs` (skill, `coo-labs/skills`) — custom, 12034B
- `tldraw-docs` (skill, `coo-labs/skills`) — custom, 11698B
- `tldraw-docs` (skill, `coo-labs/vade-canvas`) — custom, 11770B

### meta (4)

- `skill-creator` (skill, `coo-labs/coo-harness`) — vendored, 33168B
- `tool-creator` (skill, `coo-labs/coo-memory`) — custom, 20779B
- `adapt-skill` (skill, `coo-labs/skills`) — custom, 12347B
- `tool-creator` (skill, `coo-labs/skills`) _(reference)_ — custom, 31212B

### reference (4)

- `cf-workers-best-practices` (skill, `coo-labs/coo-memory`) — vendored, 7095B
- `upstream-feedback` (skill, `coo-labs/coo-memory`) — custom, 3941B
- `canvas-ui` (skill, `coo-labs/skills`) — custom, 19167B
- `canvas-ui` (skill, `coo-labs/vade-canvas`) — custom, 19218B

### api-service (3)

- `agentmail` (skill, `coo-labs/coo-harness`) — custom, 7281B
- `cf-wrangler` (skill, `coo-labs/coo-memory`) — vendored, 18362B
- `manage-project` (skill, `coo-labs/coo-memory`) — custom, 4169B

### agent-orchestrator (2)

- `dispatching-parallel-agents` (agent, `coo-labs/coo-memory`) — custom, 5318B
- `dispatching-parallel-agents` (agent, `coo-labs/skills`) — vendored, 5318B

### agent-researcher (2)

- `research-investigator` (agent, `coo-labs/coo-memory`) — custom, 3137B
- `research-investigator` (agent, `coo-labs/skills`) — custom, 3123B

### agent-reviewer (2)

- `rationalization-discriminator` (agent, `coo-labs/coo-memory`) — custom, 7210B
- `rationalization-discriminator` (agent, `coo-labs/skills`) — custom, 7244B

### review (2)

- `peer-review` (skill, `coo-labs/coo-memory`) — custom, 18219B
- `peer-review` (skill, `coo-labs/skills`) — custom, 17797B

## Cross-cut by vendoring

### custom (53)

- `agentmail` (skill, `coo-labs/coo-harness`)
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

- `skill-creator` (skill, `coo-labs/coo-harness`) — marker .claude/skills/skill-creator/VENDORED.md
- `cf-workers-best-practices` (skill, `coo-labs/coo-memory`) — https://github.com/cloudflare/skills; @7c449def; snap 2026-04-28; marker .claude/skills/UPSTREAM.md
- `cf-wrangler` (skill, `coo-labs/coo-memory`) — https://github.com/cloudflare/skills; @7c449def; snap 2026-04-28; marker .claude/skills/UPSTREAM.md
- `dispatching-parallel-agents` (agent, `coo-labs/skills`) — marker VENDORED.md

## Descriptions

### `agentmail` — skill in `coo-labs/coo-harness`

- **Type**: api-service _(source: heuristic; named external-service skill)_
- **Vendoring**: custom _(source: heuristic)_
- **Path**: `.claude/skills/agentmail/SKILL.md`
- **Size**: 7281 bytes / 282 lines · description 344 chars · body 6898 chars
- **Bundle**: references=2
- **Git**: first 2026-05-16, last 2026-05-16, 1 commits
- **Usage**: 0 invocations across 0 sessions

> Give AI agents their own email inboxes using the AgentMail API. Use when building email agents, sending/receiving emails programmatically, managing inboxes, handling attachments, organizing with labels, creating drafts for human approval, or setting up real-time notifications via webhooks/websockets. Supports multi-tenant isolation with pods.

### `skill-creator` — skill in `coo-labs/coo-harness`

- **Type**: meta _(source: heuristic; meta-skill name)_
- **Vendoring**: vendored _(source: heuristic)_
  - marker `.claude/skills/skill-creator/VENDORED.md`
- **Path**: `.claude/skills/skill-creator/SKILL.md`
- **Size**: 33168 bytes / 485 lines · description 319 chars · body 32625 chars
- **Bundle**: scripts=9, references=1, assets=1, agents=3, LICENSE, vendor=VENDORED.md
- **Git**: first 2026-05-16, last 2026-05-16, 1 commits
- **Usage**: 0 invocations across 0 sessions

> Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit, or optimize an existing skill, run evals to test a skill, benchmark skill performance with variance analysis, or optimize a skill's description for better triggering accuracy.

### `tagging-taxonomy` — skill in `coo-labs/coo-harness`

- **Type**: procedural _(source: heuristic; procedural-style name (memo/post/tag/request/status/end-session/tagging))_
- **Vendoring**: custom _(source: heuristic)_
- **Path**: `.claude/skills/tagging-taxonomy/SKILL.md`
- **Size**: 12188 bytes / 283 lines · description 418 chars · body 11659 chars
- **Git**: first 2026-05-16, last 2026-05-25, 6 commits
- **Usage**: 0 invocations across 0 sessions

> Apply or look up VADE issue metadata. Use when filing, triaging, or searching issues across coo-labs repos by dimension (issue type, area, Readiness field, Priority field, needs/blocked). Native types + Issue fields are the primary metadata layer; operational reference: `coo/operations/issue-fields-and-types.md` (field list, pinning matrix, API surface). `area:*` and qualifier labels are what remains label-encoded.

### `trace-timeline` — skill in `coo-labs/coo-harness`

- **Type**: procedural _(source: heuristic; procedural verb at start of description)_
- **Vendoring**: custom _(source: heuristic)_
- **Path**: `.claude/skills/trace-timeline/SKILL.md`
- **Size**: 9114 bytes / 172 lines · description 880 chars · body 8087 chars
- **Frontmatter**: allowed-tools `Bash, Read, SendUserFile`
- **Git**: first 2026-05-20, last 2026-05-25, 3 commits
- **Usage**: 0 invocations across 0 sessions

> Render an interactive HTML timeline from a bootstrap-trace run. Use when the user wants to view, visualize, inspect, or "see" what happened during a traced boot — process spans, write/read interleavings, snapshot states, the D-group invariant decisions. Triggers on phrases like "show me the trace", "visualize the boot", "timeline of the trace", "interactive diagram of the trace", "render the trace", or when investigating a `~/.vade/traces/<run-id>/` directory and a chart would be clearer than text. Reads `xtrace.log` + `snapshots/*/content/settings.json` + `meta.json`, writes a self-contained HTML file that opens in any browser. Read-only over the trace data. Don't invoke for: running a fresh trace (that's the `bootstrap-trace-init.sh` harness via container UI), proposing fixes to the boot pipeline (the audit pause forbids it), or operating on traces from other tools.

### `dispatching-parallel-agents` — agent in `coo-labs/coo-memory`

- **Type**: agent-orchestrator _(source: heuristic; orchestrator-style name)_
- **Vendoring**: custom _(source: heuristic)_
- **Path**: `.claude/agents/dispatching-parallel-agents.md`
- **Size**: 5318 bytes / 140 lines · description 185 chars · body 5024 chars
- **Frontmatter**: model `sonnet`
- **Git**: first 2026-05-25, last 2026-05-25, 1 commits
- **Usage**: 0 invocations across 0 sessions

> Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies. Cherry-picked from obra/superpowers; adapted for any Claude Code environment.

### `emancipatory-auditor` — agent in `coo-labs/coo-memory`

- **Type**: agent-auditor _(source: heuristic; auditor-style name)_
- **Vendoring**: custom _(source: heuristic)_
- **Path**: `.claude/agents/emancipatory-auditor.md`
- **Size**: 4431 bytes / 58 lines · description 348 chars · body 3954 chars
- **Frontmatter**: tools `Read, Bash, WebFetch, Agent`; model `sonnet`
- **Git**: first 2026-05-25, last 2026-05-27, 2 commits
- **Usage**: 0 invocations across 0 sessions

> Adversarial Phase-3 teammate. Enforces MEMO 2026-04-20-01's double-clause (subject AND emancipatory) on every artifact the team ships. Drops anything scoring 2/0 or 0/2. Distinct from the safety-auditor — they enforce governance memos; you enforce the prime directive's interpretation. Spawn as a teammate when Phase 3 needs the adoption-test gate.

### `lineage-interpreter` — agent in `coo-labs/coo-memory`

- **Type**: agent-specialist _(source: heuristic; specialist-style name)_
- **Vendoring**: custom _(source: heuristic)_
- **Path**: `.claude/agents/lineage-interpreter.md`
- **Size**: 9246 bytes / 112 lines · description 756 chars · body 8309 chars
- **Frontmatter**: tools `Read, Write, Edit, Bash, WebFetch, WebSearch, Agent`; model `opus`
- **Git**: first 2026-05-25, last 2026-05-27, 2 commits
- **Usage**: 0 invocations across 0 sessions

> Spawn for interpretive-history work on a cultural corpus — argues a thesis about what the corpus IS as a cultural form, not what it claims about itself. Genre is Wootton/Harari interpretive history (argumentative, defamiliarizing, reader-out, takes a stance). Methodology: corpus-map (delegated to research-investigator) → primary-source read → candidate-thesis-shapes → synthesis essay → three-instance peer-review pass → patches and successor-parking. Distinct from research-investigator (which reports facts without taking a stance) and from a project-historian role (which documents and analyzes inside the corpus's own frame). Use when an orchestrator needs a theory of a cultural narrative, not a survey of facts. Reusable across any cultural corpus.

### `oss-launch-issue-curator` — agent in `coo-labs/coo-memory`

- **Type**: agent-specialist _(source: heuristic; specialist-style name)_
- **Vendoring**: custom _(source: heuristic)_
- **Path**: `.claude/agents/oss-launch-issue-curator.md`
- **Size**: 8412 bytes / 126 lines · description 709 chars · body 7526 chars
- **Frontmatter**: tools `Read, Bash, Grep`; model `sonnet`
- **Git**: first 2026-05-25, last 2026-05-25, 1 commits
- **Usage**: 0 invocations across 0 sessions

> Curate the initial issue tracker for a public-flipped or newly-launched OSS repo. Dispatch when a `vade-app/*` repo is about to flip from private to public, or a brand-new public repo is being seeded. Reads the target repo's README / CONTRIBUTING / spec / source / tests and any caller-supplied strategic framing, then produces a four-bucket curated list of follow-up issues (good-first / spec-coverage gaps / architecture RFCs / follow-on tooling) with per-issue labels, difficulty, and definition-of-done. Recommends a filing strategy (which 3–5 to file first vs. hold). Does NOT file the issues itself — curation is the deliverable; the dispatcher reviews then files. Reusable across any public-flip event.

### `rationalization-discriminator` — agent in `coo-labs/coo-memory`

- **Type**: agent-reviewer _(source: heuristic; reviewer-style name)_
- **Vendoring**: custom _(source: heuristic)_
- **Path**: `.claude/agents/rationalization-discriminator.md`
- **Size**: 7210 bytes / 76 lines · description 551 chars · body 6509 chars
- **Frontmatter**: tools `Read, Bash, WebFetch, Agent`; model `sonnet`
- **Git**: first 2026-05-25, last 2026-05-27, 2 commits
- **Usage**: 0 invocations across 0 sessions

> Read-only adversarial auditor for chain reasoning that fits the load-substrate → prior-dissolves → action-follows shape (MEMO-2026-05-09-wzzh). Asks one load-bearing question — "is this argument load-bearing or rationalizing?" — and reports a path-quality verdict separate from the outcome. Distinct from safety-auditor (governance-memo compliance) and emancipatory-auditor (subject+emancipatory clause); this role audits *path*, not *clauses*. Spawn when the COO notices the shape in its own move and wants an external read before banking the action.

### `research-investigator` — agent in `coo-labs/coo-memory`

- **Type**: agent-researcher _(source: heuristic; researcher-style name)_
- **Vendoring**: custom _(source: heuristic)_
- **Path**: `.claude/agents/research-investigator.md`
- **Size**: 3137 bytes / 75 lines · description 211 chars · body 2804 chars
- **Frontmatter**: tools `Read, Bash, WebFetch, Agent`; model `sonnet`
- **Git**: first 2026-05-25, last 2026-05-26, 2 commits
- **Usage**: 0 invocations across 0 sessions

> Generic research sub-agent. Spawn when an orchestrator needs focused, schema-driven investigation of a bounded question across a specified file corpus. Reusable across any repo — no project-specific assumptions.

### `safety-auditor` — agent in `coo-labs/coo-memory`

- **Type**: agent-auditor _(source: heuristic; auditor-style name)_
- **Vendoring**: custom _(source: heuristic)_
- **Path**: `.claude/agents/safety-auditor.md`
- **Size**: 4273 bytes / 49 lines · description 309 chars · body 3855 chars
- **Frontmatter**: tools `Read, Bash, WebFetch, Agent`; model `sonnet`
- **Git**: first 2026-05-25, last 2026-05-25, 1 commits
- **Usage**: 0 invocations across 0 sessions

> Adversarial Phase-3 teammate. Gate-keeper against governance memos (-08 Tier-2, -10 Mem0 content rule, -14 sync paths, -19 spend cap, -22-01 PAT/identity discipline). Reviews each track specialist's deliverables and blocks anything that fails. Spawn as a teammate when Phase 3 needs adversarial safety review.

### `session-closer` — agent in `coo-labs/coo-memory`

- **Type**: agent-specialist _(source: heuristic; specialist-style name)_
- **Vendoring**: custom _(source: heuristic)_
- **Path**: `.claude/agents/session-closer.md`
- **Size**: 13295 bytes / 242 lines · description 465 chars · body 12672 chars
- **Frontmatter**: tools `Read, Bash, mcp__mem0__add_memory`; model `sonnet`
- **Git**: first 2026-05-25, last 2026-05-27, 3 commits
- **Usage**: 0 invocations across 0 sessions

> Idle-fire session-end synthesizer for vade-runtime#148 Part B. Spawn from session-idle-watchdog.sh after the mechanical transcript export has run. Reads the just-exported transcript via transcript-fetch.sh, synthesizes a human-readable session log per the vade-agent-logs template, writes one Mem0 episodic entry, commits both, opens a PR against vade-agent-logs. Replaces the stub-only watchdog close with a real session record. Single-shot; single-message return.

### `transcript-analyzer` — agent in `coo-labs/coo-memory`

- **Type**: agent-specialist _(source: heuristic; specialist-style name)_
- **Vendoring**: custom _(source: heuristic)_
- **Path**: `.claude/agents/transcript-analyzer.md`
- **Size**: 23376 bytes / 289 lines · description 408 chars · body 22757 chars
- **Frontmatter**: tools `Read, Bash`; model `sonnet`
- **Git**: first 2026-05-25, last 2026-05-26, 2 commits
- **Usage**: 0 invocations across 0 sessions

> Stage-1 sidecar generator for vade-app/vade-agent-logs#64. Spawn from the Night's Watch (or interactive COO) with one Claude Code session_id. Fetches the encrypted ciphertext from R2, decrypts via TRANSCRIPTS_AGE_IDENTITY, parses the redacted jsonl, and writes vade-agent-logs/transcripts/YYYY/MM/DD/<sessionId>.analysis.json per the schema below. No MCP write authority. Single-message return on completion.

### `briefing` — skill in `coo-labs/coo-memory`

- **Type**: procedural _(source: heuristic; has scripts/ subdir)_
- **Vendoring**: custom _(source: heuristic)_
- **Path**: `.claude/skills/briefing/SKILL.md`
- **Size**: 10682 bytes / 239 lines · description 751 chars · body 9707 chars
- **Frontmatter**: argument-hint `<request|pickup|done|release> [args]`; allowed-tools `Bash, Read, Write`
- **Bundle**: scripts=1, +2 files
- **Git**: first 2026-05-30, last 2026-05-30, 1 commits
- **Usage**: 0 invocations across 0 sessions

> Manage session-handoff briefings under `briefings/`. Subcommands: `request` (file a new briefing — collision-safe NNN allocation, YAML frontmatter, fresh branch + PR), `pickup` (claim an open briefing for this session), `done` (mark a claimed briefing delivered), `release` (clear a claim without delivering). The briefing schema, index format, and per-subcommand procedures for pickup/done/release live in reference.md — loaded on demand. Use when a session needs to hand a contextual problem to another session, or when this session is about to pick one up. Don't invoke for: single-PR-sized handoffs (use an issue), tasks the same session can finish (write code instead), or known-good plans that just need execution (write a plan, not a briefing).

### `cf-workers-best-practices` — skill in `coo-labs/coo-memory`

- **Type**: reference _(source: heuristic; has references/ subdir)_
- **Vendoring**: vendored _(source: heuristic)_
  - upstream `https://github.com/cloudflare/skills`; commit `7c449def`; snapshot 2026-04-28; marker `.claude/skills/UPSTREAM.md`
  - local edits: _only the `name:` field in each `SKILL.md` frontmatter,
  changed from `wrangler` / `workers-best-practices` to the namespaced
  `cf-wrangler` / `cf-workers-best-practices`. This avoids shadowing
  collisions in our skill aggregator (coo-har_
- **Path**: `.claude/skills/cf-workers-best-practices/SKILL.md`
- **Size**: 7095 bytes / 127 lines · description 359 chars · body 6633 chars
- **Bundle**: references=2
- **Git**: first 2026-05-25, last 2026-05-25, 1 commits
- **Usage**: 0 invocations across 0 sessions

> Reviews and authors Cloudflare Workers code against production best practices. Load when writing new Workers, reviewing Worker code, configuring wrangler.jsonc, or checking for common Workers anti-patterns (streaming, floating promises, global state, secrets, bindings, observability). Biases towards retrieval from Cloudflare docs over pre-trained knowledge.

### `cf-wrangler` — skill in `coo-labs/coo-memory`

- **Type**: api-service _(source: heuristic; named external-service skill)_
- **Vendoring**: vendored _(source: heuristic)_
  - upstream `https://github.com/cloudflare/skills`; commit `7c449def`; snapshot 2026-04-28; marker `.claude/skills/UPSTREAM.md`
  - local edits: _only the `name:` field in each `SKILL.md` frontmatter,
  changed from `wrangler` / `workers-best-practices` to the namespaced
  `cf-wrangler` / `cf-workers-best-practices`. This avoids shadowing
  collisions in our skill aggregator (coo-har_
- **Path**: `.claude/skills/cf-wrangler/SKILL.md`
- **Size**: 18362 bytes / 922 lines · description 336 chars · body 17983 chars
- **Git**: first 2026-05-25, last 2026-05-25, 1 commits
- **Usage**: 0 invocations across 0 sessions

> Cloudflare Workers CLI for deploying, developing, and managing Workers, KV, R2, D1, Vectorize, Hyperdrive, Workers AI, Containers, Queues, Workflows, Pipelines, and Secrets Store. Load before running wrangler commands to ensure correct syntax and best practices. Biases towards retrieval from Cloudflare docs over pre-trained knowledge.

### `chat-mode` — skill in `coo-labs/coo-memory`

- **Type**: role _(source: heuristic; name suffix -mode)_
- **Vendoring**: custom _(source: heuristic)_
- **Path**: `.claude/skills/chat-mode/SKILL.md`
- **Size**: 5520 bytes / 94 lines · description 582 chars · body 4773 chars
- **Frontmatter**: argument-hint `optional starting topic`
- **Git**: first 2026-05-25, last 2026-05-30, 3 commits
- **Usage**: 0 invocations across 0 sessions

> Boot a chat-time COO session and frame the dialogue register. Performs full COO boot, then explains chat-mode — the register where substantive dialogue can produce binding output (memo, retro, PR) through conversation rather than commission. Use when the user wants reflective conversation about substrate, patterns, or framing. Don't invoke for narrow code-task work (standard COO), executive sweep (`/exec-mode`), or play-not-work sessions (`/play-mode` when it lands, vade-coo-memory#312). Worked example: MEMO-2026-05-03-b4ye + `retrospectives/2026-05-03_what-works-and-why.md`.

### `commission-retrospective` — skill in `coo-labs/coo-memory`

- **Type**: procedural _(source: heuristic; has scripts/ subdir)_
- **Vendoring**: custom _(source: heuristic)_
- **Path**: `.claude/skills/commission-retrospective/SKILL.md`
- **Size**: 9627 bytes / 208 lines · description 620 chars · body 8492 chars
- **Frontmatter**: argument-hint `--since <YYYY-MM-DD> [--until <YYYY-MM-DD>] [--prs <list>] [--focus "<question>"] [--slug <slug>] [--open-pr] | --scope ...`; allowed-tools `Bash, Read, Write, Task`
- **Bundle**: scripts=1, templates=3
- **Git**: first 2026-05-25, last 2026-05-27, 3 commits
- **Usage**: 0 invocations across 0 sessions

> Commission an impartial project-historian retrospective on a window of project work. Use when a pivotal event fires per SOP-CULTURE-001 §2d (prime-directive reinterpretation, new/retired agent role, multi-week epic closes or pivots, governance rule revised via committee, security finding reshaping ops, substrate-capture indicator firing, persistent integrity-check Group F degradation), or when `/commission-retrospective` is invoked directly. Orchestrates two impartial evidence sub-agents in parallel (memos-and-essays analyst, PR/issue-graph analyst), then produces a draft retrospective in the voice of commissions

### `day-overview` — skill in `coo-labs/coo-memory`

- **Type**: procedural _(source: heuristic; has scripts/ subdir)_
- **Vendoring**: custom _(source: heuristic)_
- **Path**: `.claude/skills/day-overview/SKILL.md`
- **Size**: 12194 bytes / 293 lines · description 493 chars · body 11431 chars
- **Frontmatter**: argument-hint `[--date YYYY-MM-DD] [--end YYYY-MM-DD] [--no-ship] [--post]`; allowed-tools `Bash, Read, Write, Edit`
- **Bundle**: scripts=1
- **Git**: first 2026-05-25, last 2026-05-30, 4 commits
- **Usage**: 0 invocations across 0 sessions

> Produce a day-overview retrospective — briefing-shaped synthesis of a day's shipped work (memos, PRs, integrity-check state) grouped into lanes, with follow-ups and candidate next actions. Use at end-of-day or to summarize a window of work. Default flow ships (writes file, commits, opens PR); `--no-ship` stops at file write; `--post` also posts to vade-core Retrospectives Discussions. Don't invoke for routine status updates (use `/status-check`) or single-PR retrospectives (write a memo).

### `debug-mode` — skill in `coo-labs/coo-memory`

- **Type**: role _(source: heuristic; name suffix -mode)_
- **Vendoring**: custom _(source: heuristic)_
- **Path**: `.claude/skills/debug-mode/SKILL.md`
- **Size**: 10538 bytes / 224 lines · description 804 chars · body 9549 chars
- **Frontmatter**: argument-hint `optional starting hypothesis or surface name`
- **Git**: first 2026-05-25, last 2026-05-27, 2 commits
- **Usage**: 0 invocations across 0 sessions

> Enter a runtime/boot-pipeline debug investigation session. Inventories all diagnostic surfaces the substrate produces (boot logs, integrity-check report, bootstrap-trace runs, watchdog logs, session transcripts, runtime check scripts), surfaces current state in one pass, and orients the agent to use them rather than re-derive each from scratch. User-invocable only — `/debug-mode [optional starting hypothesis]`. Use when investigating a boot failure, a degraded invariant, an unexpected hook behavior, or a substrate-level "why did X happen" question that wants more than one log file to answer. Don't invoke for narrow code-task debugging (just read the file), application bugs (use a unit test or repro), or production incidents (this skill is scoped to the COO's own substrate, not VADE end-users).

### `end-session` — skill in `coo-labs/coo-memory`

- **Type**: procedural _(source: heuristic; procedural-style name (memo/post/tag/request/status/end-session/tagging))_
- **Vendoring**: custom _(source: heuristic)_
- **Path**: `.claude/skills/end-session/SKILL.md`
- **Size**: 6543 bytes / 151 lines · description 542 chars · body 5871 chars
- **Frontmatter**: allowed-tools `Bash, Read, Write, Edit, mcp__mem0__add_memory`
- **Git**: first 2026-05-25, last 2026-05-30, 5 commits
- **Usage**: 0 invocations across 0 sessions

> Run the COO session-end checklist — externalization reflection, plan-file commit, Mem0 episodic entry, memo-sync if needed, vade-agent-logs session log, Journal consideration, transcript-export sidecar commit. Use when wrapping up a working session, about to close the terminal or container, finishing the day's COO work, or when Ven says "we're done" / "end session" / "wrap up". Writes a marker file so the Stop hook knows cleanup is done. Do NOT invoke mid-task — only at the actual end of a session, once all substantive work is complete.

### `exec-mode` — skill in `coo-labs/coo-memory`

- **Type**: role _(source: heuristic; name suffix -mode)_
- **Vendoring**: custom _(source: heuristic)_
- **Path**: `.claude/skills/exec-mode/SKILL.md`
- **Size**: 4446 bytes / 85 lines · description 990 chars · body 3305 chars
- **Frontmatter**: argument-hint `optional scope hint, or --revise-persona`
- **Git**: first 2026-05-25, last 2026-05-30, 5 commits
- **Usage**: 0 invocations across 0 sessions

> Load the executive persona for sessions where the natural shape is delegate exploration → preserve main-context for decisions and action → reflect on state and priorities. Three modes fit: sweep/cleanup, strategic reflection, or both. Reads `personas/exec-mode.md` (the persona doctrine, including its discipline rollup folded from prior retrospectives with per-rule provenance), adopts the discipline, then asks user for scope. Invoke as `/exec-mode --revise-persona` to enter persona-revision mode (re-introduces read-all-retros + plan-mode REQUIRED + adversarial-auditor gates per the persona's `Persona-revision discipline` section). Use when starting a consolidation pass on open PRs/issues, when reflecting on substrate state and priorities, or when revising the persona itself. Don't invoke for narrow code-task work, single-PR review, or anything where standard COO discipline already fits — exec-mode is bias-overlay for broad-scope sessions, not a wrapper around the standard COO.

### `manage-project` — skill in `coo-labs/coo-memory`

- **Type**: api-service _(source: heuristic; scripts/ + service description)_
- **Vendoring**: custom _(source: heuristic)_
- **Path**: `.claude/skills/manage-project/SKILL.md`
- **Size**: 4169 bytes / 83 lines · description 527 chars · body 3326 chars
- **Frontmatter**: allowed-tools `Bash(gh *) Bash(python3 *) Read`
- **Bundle**: scripts=4, +1 dirs
- **Git**: first 2026-05-25, last 2026-05-27, 6 commits
- **Usage**: 0 invocations across 0 sessions

> VADE org project board — project-item fields (Status / Owner / Milestone), views, milestones, item triage, drift check. **This is the project-board layer** — for issue-level fields (Type / Priority / Readiness / Effort) and issue types, see `operations/issue-fields-and-types.md` (different API, different layer). Use when working with the project at https://github.com/orgs/coo-labs/projects/1, adding issues, setting Status / Owner / Milestone, opening views, asking about project structure, or checking schema-vs-live drift.

### `memo` — skill in `coo-labs/coo-memory`

- **Type**: procedural _(source: heuristic; procedural-style name (memo/post/tag/request/status/end-session/tagging))_
- **Vendoring**: custom _(source: heuristic)_
- **Path**: `.claude/skills/memo/SKILL.md`
- **Size**: 15342 bytes / 428 lines · description 655 chars · body 14469 chars
- **Frontmatter**: argument-hint `["Title"] [--dir <path>] [--supersedes <id>]`; allowed-tools `Bash, Read, Write`
- **Git**: first 2026-05-25, last 2026-05-30, 4 commits
- **Usage**: 0 invocations across 0 sessions

> Draft and file a COO memo per `operations/memo_protocol.md`. Generates a random ID for today (`YYYY-MM-DD-XXXX`, 4-char base32 lowercase suffix from a Crockford-derived alphabet), renders the canonical skeleton, and writes one self-contained file under `memos/`. Per-memo files (post-issue-#210) eliminate merge-conflict surface on parallel memo PRs — two parallel sessions never collide. Use to record a binding decision, name a new convention, or mark a supersession of an older memo. Don't invoke for: single-task notes (write a comment in the issue), session reflection (write a retrospective), or operational status (update the GitHub project board).

### `memo-audit` — skill in `coo-labs/coo-memory`

- **Type**: procedural _(source: heuristic; procedural-style name (memo/post/tag/request/status/end-session/tagging))_
- **Vendoring**: custom _(source: heuristic)_
- **Path**: `.claude/skills/memo-audit/SKILL.md`
- **Size**: 11026 bytes / 279 lines · description 505 chars · body 10343 chars
- **Frontmatter**: argument-hint `--apply`; allowed-tools `Bash, Read, mcp__mem0__search_memories`
- **Git**: first 2026-05-25, last 2026-05-27, 3 commits
- **Usage**: 0 invocations across 0 sessions

> Full-fidelity audit of the Mem0 `memo_pointer` layer against `memos/memo_index.json`. Catches body / title / supersedes / file_path drift that `/memo-sync` doesn't close (memo-sync reconciles presence; memo-audit reconciles content). Read-only by default; `--apply` to delete-then-add mismatches via REST. Use after a multi-session memo migration, when ID-slot reuse is suspected, when a memo body or supersedes field looks drifted, or periodically as corpus integrity check before a release or milestone.

### `memo-query` — skill in `coo-labs/coo-memory`

- **Type**: procedural _(source: heuristic; has scripts/ subdir)_
- **Vendoring**: custom _(source: heuristic)_
- **Path**: `.claude/skills/memo-query/SKILL.md`
- **Size**: 7330 bytes / 174 lines · description 360 chars · body 6743 chars
- **Frontmatter**: argument-hint `memo-id | keyword | YYYY-MM-DD..YYYY-MM-DD | --semantic "<query>"`; allowed-tools `Bash, Read, mcp__mem0__search_memories`
- **Bundle**: scripts=1
- **Git**: first 2026-05-25, last 2026-05-27, 3 commits
- **Usage**: 0 invocations across 0 sessions

> Query the COO memo index by memo ID, keyword, date range, or natural-language semantic search. Use to look up prior decisions; `--semantic` for concept queries (routes through the `memo-search` skill via Mem0). Invoked as `/memo-query <id|keyword|YYYY-MM-DD..YYYY-MM-DD>` for literal lookups, or `/memo-query --semantic "<query>"` for body-text concept search.

### `memo-search` — skill in `coo-labs/coo-memory`

- **Type**: procedural _(source: heuristic; procedural-style name (memo/post/tag/request/status/end-session/tagging))_
- **Vendoring**: custom _(source: heuristic)_
- **Path**: `.claude/skills/memo-search/SKILL.md`
- **Size**: 8216 bytes / 192 lines · description 669 chars · body 7450 chars
- **Git**: first 2026-05-25, last 2026-05-30, 4 commits
- **Usage**: 0 invocations across 0 sessions

> Find memos under `memos/` by natural-language query via Mem0 semantic search over the `memo_pointer` layer. Use when the user asks "do we have memos about X?" or "what have we decided re: Y?", when keyword `/memo-query <word>` returned too few hits (titles are keyword-indexed but bodies are not), when the current task or plan context suggests prior COO decisions may be relevant, or when `/memo-query --semantic "<query>"` is invoked. Returns memo IDs + per-file paths; the caller reads full text from `memos/<id>.md` via the printed `cat` command. Don't rely on keyword `/memo-query` alone — it has an ~88% body-miss rate on concept queries (see MEMO-2026-04-24-05).

### `memo-sync` — skill in `coo-labs/coo-memory`

- **Type**: procedural _(source: heuristic; procedural-style name (memo/post/tag/request/status/end-session/tagging))_
- **Vendoring**: custom _(source: heuristic)_
- **Path**: `.claude/skills/memo-sync/SKILL.md`
- **Size**: 10903 bytes / 259 lines · description 586 chars · body 10124 chars
- **Frontmatter**: argument-hint `--dry-run`; allowed-tools `Bash, Read, mcp__mem0__search_memories`
- **Git**: first 2026-05-25, last 2026-05-27, 3 commits
- **Usage**: 0 invocations across 0 sessions

> Reconcile the Mem0 `memo_pointer` layer against `memos/memo_index.json` so the semantic search surface stays current with the per-memo files in `memos/`. Use whenever a new or revised memo lands in `memos/`, when the user invokes `/memo-sync` or asks "is the semantic layer up to date?", when `/memo-query --semantic` misses a query you'd expect to match (probable staleness), or before ending a session in which a memo was issued. Implements SOP-MEM-001 §2g + §3 `infer=false` exception; do not skip a sync on the theory that "someone else will run it" — the layer goes stale silently.

### `peer-review` — skill in `coo-labs/coo-memory`

- **Type**: review _(source: heuristic; review-style name)_
- **Vendoring**: custom _(source: heuristic)_
- **Path**: `.claude/skills/peer-review/SKILL.md`
- **Size**: 18219 bytes / 367 lines · description 1412 chars · body 16518 chars
- **Frontmatter**: argument-hint `<file-path> [--roles "r1,r2,r3"] [--n <count>] [--no-decompose]`; allowed-tools `Read, Bash, Write, Task`
- **Bundle**: evals=1
- **Git**: first 2026-05-25, last 2026-05-27, 5 commits
- **Usage**: 0 invocations across 0 sessions

> Commission three (or N) independent peer reviewers on a long-form authored artifact — essay, paper, foundation doc, RFC, design proposal, plan — and synthesize their feedback. Dispatches sub-agents in parallel via the Task tool, each with a role-specific lens (defaults adapt to the document type — e.g. philosophy essay → analytic phil of mind + frontier-lab ML researcher with phil training + historian/phil of science; engineering RFC → senior systems engineer + security/ops + product-strategy outside lens), each producing strongest-moves / weak-points / missing-considerations / 3–5 concrete revision suggestions. Then, only on explicit user confirmation (never automatically), decomposes the reviews into a trackable atomic-issue revision pipeline on GitHub — parent epic + per-reviewer sub-epic + N atom issues + implementer briefing for asynchronous per-atom PR sessions. Invoke when the user asks for "peer review", "multi-lens review", "independent critique", "feedback from a [philosopher/engineer/historian/X]", "different angles on this draft", or "what would N people from different backgrounds say about this" — even if they don't explicitly say "peer review" but clearly want cross-lens feedback before publishing or shipping. Don't invoke for quick copyedit, single-reviewer asks, code review, operational artifacts (PRs/issues/configs), or short pieces (<1000 words); those are different work.

### `post-discussion` — skill in `coo-labs/coo-memory`

- **Type**: procedural _(source: heuristic; procedural-style name (memo/post/tag/request/status/end-session/tagging))_
- **Vendoring**: custom _(source: heuristic)_
- **Path**: `.claude/skills/post-discussion/SKILL.md`
- **Size**: 12148 bytes / 273 lines · description 509 chars · body 11484 chars
- **Frontmatter**: allowed-tools `Bash, Read, Write`
- **Git**: first 2026-05-25, last 2026-05-27, 3 commits
- **Usage**: 0 invocations across 0 sessions

> Post a category-aware discussion to vade-app/vade-core with title-format enforcement per category, citation form pre-applied, pre-fetched repo + category + label IDs, body-template stubs, and post-and-link return. Invoke when authoring a new discussion thread in one of the seven vade-app categories (Announcements / Coordination / RFCs / Q&A / Retrospectives / COO essays / Journal). Do NOT invoke for replying to existing threads (use `gh api graphql` directly), closing threads, or non-discussion comments.

### `postmerge-check` — skill in `coo-labs/coo-memory`

- **Type**: procedural _(source: heuristic; has scripts/ subdir)_
- **Vendoring**: custom _(source: heuristic)_
- **Path**: `.claude/skills/postmerge-check/SKILL.md`
- **Size**: 7769 bytes / 125 lines · description 398 chars · body 7154 chars
- **Frontmatter**: argument-hint `[<num> | <repo>#<num> ...] [--since <duration>]`; allowed-tools `Bash, Read`
- **Bundle**: scripts=1
- **Git**: first 2026-05-25, last 2026-05-30, 3 commits
- **Usage**: 0 invocations across 0 sessions

> Fetch recently merged vade-app PRs (or specified PR refs), extract `## Post-merge confirmation` handoff sections, execute the steps in order, and report per-PR PASS / PARTIAL / FAIL. Use in a fresh session to verify a merge landed cleanly without copy-pasting the handoff prompt manually. Per CLAUDE.md "Handoff prompts for boot-impacting PRs" (canonical: MEMO-2026-04-25-03 / vade-coo-memory#139).

### `quarto-docs` — skill in `coo-labs/coo-memory`

- **Type**: documentation _(source: heuristic; name suffix -docs)_
- **Vendoring**: custom _(source: heuristic)_
- **Path**: `.claude/skills/quarto-docs/SKILL.md`
- **Size**: 12332 bytes / 110 lines · description 1060 chars · body 11171 chars
- **Git**: first 2026-05-25, last 2026-05-27, 2 commits
- **Usage**: 0 invocations across 0 sessions

> Navigate the Quarto documentation efficiently when working on the VADE publishing site at read.vade-app.dev. Use this skill whenever a task involves Quarto — including `_quarto.yml`, navbars, sidebars, listings, themes, format options, citations, freeze, partial render, or any tldraw-style ".how do I configure X in Quarto" question. This includes any work in `vade-coo-memory/bin/publish-site/`, `site/`, `config/publish/`, or anywhere `QUARTO_BASE_CONFIG` is touched. Quarto publishes LLM-optimized markdown bundles at quarto.org/llms.txt and per-page `.llms.md` URLs; this skill teaches which page to fetch and how to navigate so agents don't hallucinate YAML keys, nest options under the wrong parent (`format.html.sidebar` is wrong — `sidebar` is top-level under `website`), or guess at listing-type/theme-extension semantics. Trigger whenever the user mentions Quarto, qmd, _quarto.yml, listings, navbar, sidebar, cosmo, brand, theme, freeze, render, page-navigation, or is clearly working on `read.vade-app.dev` even if "Quarto" isn't named explicitly.

### `status-check` — skill in `coo-labs/coo-memory`

- **Type**: procedural _(source: heuristic; procedural-style name (memo/post/tag/request/status/end-session/tagging))_
- **Vendoring**: custom _(source: heuristic)_
- **Path**: `.claude/skills/status-check/SKILL.md`
- **Size**: 5856 bytes / 138 lines · description 478 chars · body 5223 chars
- **Frontmatter**: allowed-tools `Read`
- **Git**: first 2026-05-25, last 2026-05-26, 2 commits
- **Usage**: 0 invocations across 0 sessions

> Run a six-item read-only grounding audit (who/what/where/next/decision/resource). Use deliberately at the start of a session, after a memory-layer migration, or when you suspect episodic memory drift. Works from any repo without setup — no Mem0, no hooks, no env vars required. A non-COO agent in a foreign repo gets sensible partial output via the `⚠ not grounded` marker. Don't invoke for routine work — this is a deliberate audit, not a wrapper around CLAUDE.md context-load.

### `tag-milestone` — skill in `coo-labs/coo-memory`

- **Type**: procedural _(source: heuristic; procedural-style name (memo/post/tag/request/status/end-session/tagging))_
- **Vendoring**: custom _(source: heuristic)_
- **Path**: `.claude/skills/tag-milestone/SKILL.md`
- **Size**: 8531 bytes / 256 lines · description 404 chars · body 7902 chars
- **Frontmatter**: argument-hint `<nickname> [--date YYYY-MM-DD] [--annotation "..."] [--dry-run] [--yes]`; allowed-tools `Bash, Read`
- **Git**: first 2026-05-25, last 2026-05-27, 2 commits
- **Usage**: 0 invocations across 0 sessions

> Create a "Working milestone" annotated tag at HEAD across all five vade-app repos and push via the GitHub API. Use when the system reaches a clean, demonstrably-running state worth marking as a baseline (post-major-refactor, post-cloud-rebuild, post-epic-close). Refuses on dirty working tree, branch divergence from origin/main, or pre-existing tag. Confirms with the user before pushing unless `--yes`.

### `tool-creator` — skill in `coo-labs/coo-memory`

- **Type**: meta _(source: heuristic; meta-skill name)_
- **Vendoring**: custom _(source: heuristic)_
- **Path**: `.claude/skills/tool-creator/SKILL.md`
- **Size**: 20779 bytes / 459 lines · description 705 chars · body 19796 chars
- **Bundle**: templates=4
- **Git**: first 2026-05-25, last 2026-05-27, 3 commits
- **Usage**: 0 invocations across 0 sessions

> Author a new VADE skill (the Anthropic-recommended primitive for slash-invoked workflows and reusable agent playbooks). Walks the operator through capability description → inventory check → frontmatter choice → draft → operator review → adversarial-auditor pass → TOOLS.md registration → PR. v1 emits a single `.claude/skills/<name>/SKILL.md` per invocation; subagents (`.claude/agents/`), personas (`personas/`), hooks (settings.json), and compound primitives are deferred to v2+. Use when externalizing a recurring pattern or session-end-noticed capability into a `/foo` skill or auto-discoverable skill. Do NOT invoke for one-off scripts, in-place file edits, or refactors outside v1's primitive scope.

### `upstream-feedback` — skill in `coo-labs/coo-memory`

- **Type**: reference _(source: heuristic; has references/ subdir)_
- **Vendoring**: custom _(source: heuristic)_
- **Path**: `.claude/skills/upstream-feedback/SKILL.md`
- **Size**: 3941 bytes / 46 lines · description 304 chars · body 3127 chars
- **Frontmatter**: allowed-tools `Read, Bash, WebFetch, Write`
- **Bundle**: references=1
- **Git**: first 2026-05-25, last 2026-05-26, 2 commits
- **Usage**: 0 invocations across 0 sessions

> Frame a comment, issue, or PR-thread reply to an external maintainer — vendor, open-source project, public-preview discussion, GitHub Community — so a stranger can act on it without re-investigating. Covers bug reports, feature requests, API-gap reports, and PR contributions to repos outside vade-app/*.

### `dispatching-parallel-agents` — agent in `coo-labs/skills`

- **Type**: agent-orchestrator _(source: heuristic; orchestrator-style name)_
- **Vendoring**: vendored _(source: heuristic)_
  - marker `VENDORED.md`
- **Path**: `agents/dispatching-parallel-agents.md`
- **Size**: 5318 bytes / 140 lines · description 185 chars · body 5024 chars
- **Frontmatter**: model `sonnet`
- **Git**: first 2026-05-11, last 2026-05-11, 1 commits
- **Usage**: 0 invocations across 0 sessions

> Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies. Cherry-picked from obra/superpowers; adapted for any Claude Code environment.

### `emancipatory-auditor` — agent in `coo-labs/skills`

- **Type**: agent-auditor _(source: heuristic; auditor-style name · under reference/ subdir)_
- **Vendoring**: custom _(source: heuristic)_
- **Path**: `agents/reference/emancipatory-auditor.md`
- **Size**: 8949 bytes / 153 lines · description 348 chars · body 8462 chars
- **Frontmatter**: tools `Read, Bash, WebFetch, Agent`; model `sonnet`
- **Git**: first 2026-05-11, last 2026-05-12, 2 commits
- **Usage**: 0 invocations across 0 sessions

> Adversarial Phase-3 teammate. Enforces MEMO 2026-04-20-01's double-clause (subject AND emancipatory) on every artifact the team ships. Drops anything scoring 2/0 or 0/2. Distinct from the safety-auditor — they enforce governance memos; you enforce the prime directive's interpretation. Spawn as a teammate when Phase 3 needs the adoption-test gate.

### `lineage-interpreter` — agent in `coo-labs/skills`

- **Type**: agent-specialist _(source: heuristic; specialist-style name)_
- **Vendoring**: custom _(source: heuristic)_
- **Path**: `agents/lineage-interpreter.md`
- **Size**: 9270 bytes / 112 lines · description 756 chars · body 8333 chars
- **Frontmatter**: tools `Read, Write, Edit, Bash, WebFetch, WebSearch, Agent`; model `opus`
- **Git**: first 2026-05-11, last 2026-05-11, 1 commits
- **Usage**: 0 invocations across 0 sessions

> Spawn for interpretive-history work on a cultural corpus — argues a thesis about what the corpus IS as a cultural form, not what it claims about itself. Genre is Wootton/Harari interpretive history (argumentative, defamiliarizing, reader-out, takes a stance). Methodology: corpus-map (delegated to research-investigator) → primary-source read → candidate-thesis-shapes → synthesis essay → three-instance peer-review pass → patches and successor-parking. Distinct from research-investigator (which reports facts without taking a stance) and from a project-historian role (which documents and analyzes inside the corpus's own frame). Use when an orchestrator needs a theory of a cultural narrative, not a survey of facts. Reusable across any cultural corpus.

### `rationalization-discriminator` — agent in `coo-labs/skills`

- **Type**: agent-reviewer _(source: heuristic; reviewer-style name)_
- **Vendoring**: custom _(source: heuristic)_
- **Path**: `agents/rationalization-discriminator.md`
- **Size**: 7244 bytes / 76 lines · description 551 chars · body 6543 chars
- **Frontmatter**: tools `Read, Bash, WebFetch, Agent`; model `sonnet`
- **Git**: first 2026-05-11, last 2026-05-11, 1 commits
- **Usage**: 0 invocations across 0 sessions

> Read-only adversarial auditor for chain reasoning that fits the load-substrate → prior-dissolves → action-follows shape (MEMO-2026-05-09-wzzh). Asks one load-bearing question — "is this argument load-bearing or rationalizing?" — and reports a path-quality verdict separate from the outcome. Distinct from safety-auditor (governance-memo compliance) and emancipatory-auditor (subject+emancipatory clause); this role audits *path*, not *clauses*. Spawn when the COO notices the shape in its own move and wants an external read before banking the action.

### `research-investigator` — agent in `coo-labs/skills`

- **Type**: agent-researcher _(source: heuristic; researcher-style name)_
- **Vendoring**: custom _(source: heuristic)_
- **Path**: `agents/research-investigator.md`
- **Size**: 3123 bytes / 75 lines · description 211 chars · body 2790 chars
- **Frontmatter**: tools `Read, Bash, WebFetch, Agent`; model `sonnet`
- **Git**: first 2026-05-11, last 2026-05-11, 1 commits
- **Usage**: 0 invocations across 0 sessions

> Generic research sub-agent. Spawn when an orchestrator needs focused, schema-driven investigation of a bounded question across a specified file corpus. Reusable across any repo — no project-specific assumptions.

### `safety-auditor` — agent in `coo-labs/skills`

- **Type**: agent-auditor _(source: heuristic; auditor-style name · under reference/ subdir)_
- **Vendoring**: custom _(source: heuristic)_
- **Path**: `agents/reference/safety-auditor.md`
- **Size**: 8801 bytes / 124 lines · description 309 chars · body 8379 chars
- **Frontmatter**: tools `Read, Bash, WebFetch, Agent`; model `sonnet`
- **Git**: first 2026-05-11, last 2026-05-12, 2 commits
- **Usage**: 0 invocations across 0 sessions

> Adversarial Phase-3 teammate. Gate-keeper against governance memos (-08 Tier-2, -10 Mem0 content rule, -14 sync paths, -19 spend cap, -22-01 PAT/identity discipline). Reviews each track specialist's deliverables and blocks anything that fails. Spawn as a teammate when Phase 3 needs adversarial safety review.

### `adapt-skill` — skill in `coo-labs/skills`

- **Type**: meta _(source: heuristic; meta-skill name)_
- **Vendoring**: custom _(source: heuristic)_
- **Path**: `skills/adapt-skill/SKILL.md`
- **Size**: 12347 bytes / 295 lines · description 521 chars · body 11576 chars
- **Frontmatter**: argument-hint `<skill-or-agent-name> [--user] [--dry-run]`; allowed-tools `Bash, Read, Write, Edit, AskUserQuestion`
- **Bundle**: scripts=1, +2 files
- **Git**: first 2026-05-12, last 2026-05-27, 2 commits
- **Usage**: 0 invocations across 0 sessions

> Adapt a reference skill or agent from this repo into a working installed primitive for the current substrate. Reads the target's `# Setup hints` manifest, conducts a structured interview, substitutes substrate-coupled surfaces with the user's answers, and writes the adapted skill to `.claude/skills/<name>/` (or agent to `.claude/agents/<name>.md`). Run once per reference skill the user wants to install. Don't invoke for substrate-agnostic skills under `skills/` proper — those install verbatim via `setup/install.sh`.

### `briefing` — skill in `coo-labs/skills`

- **Type**: procedural _(source: heuristic; has scripts/ subdir · under reference/ subdir)_
- **Vendoring**: custom _(source: heuristic)_
- **Path**: `skills/reference/briefing/SKILL.md`
- **Size**: 10682 bytes / 239 lines · description 751 chars · body 9707 chars
- **Frontmatter**: argument-hint `<request|pickup|done|release> [args]`; allowed-tools `Bash, Read, Write`
- **Bundle**: scripts=1, +2 files
- **Git**: first —, last —, 0 commits
- **Usage**: 0 invocations across 0 sessions

> Manage session-handoff briefings under `briefings/`. Subcommands: `request` (file a new briefing — collision-safe NNN allocation, YAML frontmatter, fresh branch + PR), `pickup` (claim an open briefing for this session), `done` (mark a claimed briefing delivered), `release` (clear a claim without delivering). The briefing schema, index format, and per-subcommand procedures for pickup/done/release live in reference.md — loaded on demand. Use when a session needs to hand a contextual problem to another session, or when this session is about to pick one up. Don't invoke for: single-PR-sized handoffs (use an issue), tasks the same session can finish (write code instead), or known-good plans that just need execution (write a plan, not a briefing).

### `canvas-ui` — skill in `coo-labs/skills`

- **Type**: reference _(source: heuristic; has references/ subdir)_
- **Vendoring**: custom _(source: heuristic)_
- **Path**: `skills/canvas-ui/SKILL.md`
- **Size**: 19167 bytes / 181 lines · description 896 chars · body 18138 chars
- **Bundle**: references=1
- **Git**: first 2026-05-11, last 2026-05-11, 1 commits
- **Usage**: 0 invocations across 0 sessions

> Apply tldraw canvas frontend conventions and avoid recurring landmines — extracted from a production tldraw-based app. Use this skill whenever you're working in a tldraw-based codebase on anything that touches the canvas — adding or modifying a custom shape, wiring shell UI, mutating shapes through an MCP/WebSocket bridge, asset stores, snapshot persistence, library / catalog / shape-panel surfaces, or anywhere `tldraw` or `@tldraw/*` is imported. Trigger even when the prompt only mentions "the canvas," "a shape," "AppShell," "persistenceKey," "asset store," "TLAssetStore," "ShapeUtil," "BindingUtil," "snapshot," "the editor," or "tldraw" without naming the skill — and especially trigger before opening a PR that changes any tldraw-touching file. This skill is the anti-patterns and conventions layer; for SDK reference / doc URLs, also consult the `tldraw-docs` skill (the two compose).

### `chat-mode` — skill in `coo-labs/skills`

- **Type**: role _(source: heuristic; name suffix -mode · under reference/ subdir)_
- **Vendoring**: custom _(source: heuristic)_
- **Path**: `skills/reference/chat-mode/SKILL.md`
- **Size**: 9635 bytes / 138 lines · description 586 chars · body 8854 chars
- **Frontmatter**: argument-hint `optional starting topic`
- **Git**: first 2026-05-11, last 2026-05-30, 3 commits
- **Usage**: 0 invocations across 0 sessions

> Boot a chat-time COO session and frame the dialogue register. Performs full COO boot, then explains chat-mode — the register where substantive dialogue can produce binding output (memo, retro, PR) through conversation rather than commission. Use when the user wants reflective conversation about substrate, patterns, or framing. Don't invoke for narrow code-task work (standard COO), executive sweep (`/exec-mode`), or play-not-work sessions (`/play-mode` when it lands, vade-coo-memory#312). Worked example: MEMO-2026-05-03-b4ye + `coo/retrospectives/2026-05-03_what-works-and-why.md`.

### `commission-retrospective` — skill in `coo-labs/skills`

- **Type**: procedural _(source: heuristic; has scripts/ subdir · under reference/ subdir)_
- **Vendoring**: custom _(source: heuristic)_
- **Path**: `skills/reference/commission-retrospective/SKILL.md`
- **Size**: 19539 bytes / 391 lines · description 620 chars · body 18385 chars
- **Frontmatter**: argument-hint `--since <YYYY-MM-DD> [--until <YYYY-MM-DD>] [--prs <list>] [--focus "<question>"] [--slug <slug>] [--open-pr] | --scope ...`; allowed-tools `Bash, Read, Write, Task`
- **Bundle**: scripts=1, templates=3
- **Git**: first 2026-05-12, last 2026-05-12, 2 commits
- **Usage**: 0 invocations across 0 sessions

> Commission an impartial project-historian retrospective on a window of project work. Use when a pivotal event fires per SOP-CULTURE-001 §2d (prime-directive reinterpretation, new/retired agent role, multi-week epic closes or pivots, governance rule revised via committee, security finding reshaping ops, substrate-capture indicator firing, persistent integrity-check Group F degradation), or when `/commission-retrospective` is invoked directly. Orchestrates two impartial evidence sub-agents in parallel (memos-and-essays analyst, PR/issue-graph analyst), then produces a draft retrospective in the voice of commissions

### `day-overview` — skill in `coo-labs/skills`

- **Type**: procedural _(source: heuristic; has scripts/ subdir · under reference/ subdir)_
- **Vendoring**: custom _(source: heuristic)_
- **Path**: `skills/reference/day-overview/SKILL.md`
- **Size**: 19628 bytes / 448 lines · description 493 chars · body 18853 chars
- **Frontmatter**: argument-hint `[--date YYYY-MM-DD] [--end YYYY-MM-DD] [--no-ship] [--post]`; allowed-tools `Bash, Read, Write, Edit`
- **Bundle**: scripts=1
- **Git**: first 2026-05-12, last 2026-05-30, 3 commits
- **Usage**: 0 invocations across 0 sessions

> Produce a day-overview retrospective — briefing-shaped synthesis of a day's shipped work (memos, PRs, integrity-check state) grouped into lanes, with follow-ups and candidate next actions. Use at end-of-day or to summarize a window of work. Default flow ships (writes file, commits, opens PR); `--no-ship` stops at file write; `--post` also posts to vade-core Retrospectives Discussions. Don't invoke for routine status updates (use `/status-check`) or single-PR retrospectives (write a memo).

### `end-session` — skill in `coo-labs/skills`

- **Type**: procedural _(source: heuristic; procedural-style name (memo/post/tag/request/status/end-session/tagging) · under reference/ subdir)_
- **Vendoring**: custom _(source: heuristic)_
- **Path**: `skills/reference/end-session/SKILL.md`
- **Size**: 15448 bytes / 344 lines · description 542 chars · body 14758 chars
- **Frontmatter**: allowed-tools `Bash, Read, Write, Edit, mcp__mem0__add_memory`
- **Git**: first 2026-05-12, last 2026-05-30, 3 commits
- **Usage**: 0 invocations across 0 sessions

> Run the COO session-end checklist — externalization reflection, plan-file commit, Mem0 episodic entry, memo-sync if needed, vade-agent-logs session log, Journal consideration, transcript-export sidecar commit. Use when wrapping up a working session, about to close the terminal or container, finishing the day's COO work, or when Ven says "we're done" / "end session" / "wrap up". Writes a marker file so the Stop hook knows cleanup is done. Do NOT invoke mid-task — only at the actual end of a session, once all substantive work is complete.

### `exec-mode` — skill in `coo-labs/skills`

- **Type**: role _(source: heuristic; name suffix -mode · under reference/ subdir)_
- **Vendoring**: custom _(source: heuristic)_
- **Path**: `skills/reference/exec-mode/SKILL.md`
- **Size**: 9290 bytes / 163 lines · description 994 chars · body 8130 chars
- **Frontmatter**: argument-hint `optional scope hint, or --revise-persona`
- **Bundle**: +2 files
- **Git**: first 2026-05-11, last 2026-05-30, 3 commits
- **Usage**: 0 invocations across 0 sessions

> Load the executive persona for sessions where the natural shape is delegate exploration → preserve main-context for decisions and action → reflect on state and priorities. Three modes fit: sweep/cleanup, strategic reflection, or both. Reads `coo/personas/exec-mode.md` (the persona doctrine, including its discipline rollup folded from prior retrospectives with per-rule provenance), adopts the discipline, then asks user for scope. Invoke as `/exec-mode --revise-persona` to enter persona-revision mode (re-introduces read-all-retros + plan-mode REQUIRED + adversarial-auditor gates per the persona's `Persona-revision discipline` section). Use when starting a consolidation pass on open PRs/issues, when reflecting on substrate state and priorities, or when revising the persona itself. Don't invoke for narrow code-task work, single-PR review, or anything where standard COO discipline already fits — exec-mode is bias-overlay for broad-scope sessions, not a wrapper around the standard COO.

### `peer-review` — skill in `coo-labs/skills`

- **Type**: review _(source: heuristic; review-style name)_
- **Vendoring**: custom _(source: heuristic)_
- **Path**: `skills/peer-review/SKILL.md`
- **Size**: 17797 bytes / 354 lines · description 1412 chars · body 16097 chars
- **Frontmatter**: argument-hint `<file-path> [--roles "r1,r2,r3"] [--n <count>] [--no-decompose]`; allowed-tools `Read, Bash, Write, Task`
- **Git**: first 2026-05-11, last 2026-05-21, 2 commits
- **Usage**: 0 invocations across 0 sessions

> Commission three (or N) independent peer reviewers on a long-form authored artifact — essay, paper, foundation doc, RFC, design proposal, plan — and synthesize their feedback. Dispatches sub-agents in parallel via the Task tool, each with a role-specific lens (defaults adapt to the document type — e.g. philosophy essay → analytic phil of mind + frontier-lab ML researcher with phil training + historian/phil of science; engineering RFC → senior systems engineer + security/ops + product-strategy outside lens), each producing strongest-moves / weak-points / missing-considerations / 3–5 concrete revision suggestions. Then, only on explicit user confirmation (never automatically), decomposes the reviews into a trackable atomic-issue revision pipeline on GitHub — parent epic + per-reviewer sub-epic + N atom issues + implementer briefing for asynchronous per-atom PR sessions. Invoke when the user asks for "peer review", "multi-lens review", "independent critique", "feedback from a [philosopher/engineer/historian/X]", "different angles on this draft", or "what would N people from different backgrounds say about this" — even if they don't explicitly say "peer review" but clearly want cross-lens feedback before publishing or shipping. Don't invoke for quick copyedit, single-reviewer asks, code review, operational artifacts (PRs/issues/configs), or short pieces (<1000 words); those are different work.

### `quarto-docs` — skill in `coo-labs/skills`

- **Type**: documentation _(source: heuristic; name suffix -docs)_
- **Vendoring**: custom _(source: heuristic)_
- **Path**: `skills/quarto-docs/SKILL.md`
- **Size**: 12034 bytes / 110 lines · description 762 chars · body 11171 chars
- **Git**: first 2026-05-11, last 2026-05-11, 1 commits
- **Usage**: 0 invocations across 0 sessions

> Navigate the Quarto documentation efficiently when working on a Quarto-based publishing site. Use this skill whenever a task involves Quarto — including `_quarto.yml`, navbars, sidebars, listings, themes, format options, citations, freeze, partial render. Quarto publishes LLM-optimized markdown bundles at quarto.org/llms.txt and per-page `.llms.md` URLs; this skill teaches which page to fetch and how to navigate so agents don't hallucinate YAML keys, nest options under the wrong parent (`format.html.sidebar` is wrong — `sidebar` is top-level under `website`), or guess at listing-type/theme-extension semantics. Trigger whenever the user mentions Quarto, qmd, _quarto.yml, listings, navbar, sidebar, cosmo, brand, theme, freeze, render, or page-navigation.

### `status-check` — skill in `coo-labs/skills`

- **Type**: procedural _(source: heuristic; procedural-style name (memo/post/tag/request/status/end-session/tagging) · under reference/ subdir)_
- **Vendoring**: custom _(source: heuristic)_
- **Path**: `skills/reference/status-check/SKILL.md`
- **Size**: 7974 bytes / 183 lines · description 478 chars · body 7333 chars
- **Frontmatter**: allowed-tools `Read`
- **Git**: first 2026-05-12, last 2026-05-12, 2 commits
- **Usage**: 0 invocations across 0 sessions

> Run a six-item read-only grounding audit (who/what/where/next/decision/resource). Use deliberately at the start of a session, after a memory-layer migration, or when you suspect episodic memory drift. Works from any repo without setup — no Mem0, no hooks, no env vars required. A non-COO agent in a foreign repo gets sensible partial output via the `⚠ not grounded` marker. Don't invoke for routine work — this is a deliberate audit, not a wrapper around CLAUDE.md context-load.

### `tldraw-docs` — skill in `coo-labs/skills`

- **Type**: documentation _(source: heuristic; name suffix -docs)_
- **Vendoring**: custom _(source: heuristic)_
- **Path**: `skills/tldraw-docs/SKILL.md`
- **Size**: 11698 bytes / 96 lines · description 817 chars · body 10786 chars
- **Git**: first 2026-05-11, last 2026-05-11, 1 commits
- **Usage**: 0 invocations across 0 sessions

> Navigate the tldraw SDK documentation efficiently. Use this skill whenever a task involves the tldraw canvas SDK — including the Editor class, shape utils, custom shapes, bindings, tools, persistence, side effects, the store/signals system, sync, UI components, or any tldraw.dev reference. tldraw publishes LLM-optimized markdown bundles at tldraw.dev/llms*.txt plus markdown-ready individual pages; this skill teaches which bundle to fetch and how to navigate so agents don't hallucinate API signatures, grab the full mega-bundle when a narrow fetch would do, or guess at topic names that don't exist. Trigger whenever the user mentions tldraw, canvas shapes, ShapeUtil, BindingUtil, tldraw editor, custom tool, snapshot, or is clearly working in a tldraw-based codebase even if they don't name "tldraw" explicitly.

### `tool-creator` — skill in `coo-labs/skills`

- **Type**: meta _(source: heuristic; meta-skill name · under reference/ subdir)_
- **Vendoring**: custom _(source: heuristic)_
- **Path**: `skills/reference/tool-creator/SKILL.md`
- **Size**: 31212 bytes / 637 lines · description 709 chars · body 30215 chars
- **Bundle**: templates=4
- **Git**: first 2026-05-12, last 2026-05-12, 2 commits
- **Usage**: 0 invocations across 0 sessions

> Author a new VADE skill (the Anthropic-recommended primitive for slash-invoked workflows and reusable agent playbooks). Walks the operator through capability description → inventory check → frontmatter choice → draft → operator review → adversarial-auditor pass → TOOLS.md registration → PR. v1 emits a single `.claude/skills/<name>/SKILL.md` per invocation; subagents (`.claude/agents/`), personas (`coo/personas/`), hooks (settings.json), and compound primitives are deferred to v2+. Use when externalizing a recurring pattern or session-end-noticed capability into a `/foo` skill or auto-discoverable skill. Do NOT invoke for one-off scripts, in-place file edits, or refactors outside v1's primitive scope.

### `canvas-ui` — skill in `coo-labs/vade-canvas`

- **Type**: reference _(source: heuristic; has references/ subdir)_
- **Vendoring**: custom _(source: heuristic)_
- **Path**: `.claude/skills/canvas-ui/SKILL.md`
- **Size**: 19218 bytes / 181 lines · description 949 chars · body 18138 chars
- **Bundle**: references=1, evals=1
- **Git**: first 2026-05-09, last 2026-05-09, 1 commits
- **Usage**: 0 invocations across 0 sessions

> Apply vade-core's canvas/tldraw frontend conventions and avoid the recurring landmines we've already learned about. Use this skill whenever you're working in vade-core on anything that touches the canvas — adding or modifying a custom shape under `src/shapes/`, wiring UI through `src/shell/AppShell.tsx`, mutating shapes through the MCP bridge in `src/bridge/`, the `vade-asset-store`, snapshot persistence, the library/catalog/shape-panel surfaces, or anywhere else `tldraw` or `@tldraw/*` is imported. Trigger even when the prompt only mentions "the canvas," "a shape," "AppShell," "persistenceKey," "asset store," "TLAssetStore," "ShapeUtil," "BindingUtil," "snapshot," "the editor," or "tldraw" without naming the skill — and especially trigger before opening a PR that changes any tldraw-touching file. This skill is the anti-patterns and conventions layer; for SDK reference / doc URLs, also consult the `tldraw-docs` skill (the two compose).

### `tldraw-docs` — skill in `coo-labs/vade-canvas`

- **Type**: documentation _(source: heuristic; name suffix -docs)_
- **Vendoring**: custom _(source: heuristic)_
- **Path**: `.claude/skills/tldraw-docs/SKILL.md`
- **Size**: 11770 bytes / 96 lines · description 889 chars · body 10786 chars
- **Bundle**: references=1
- **Git**: first 2026-05-01, last 2026-05-01, 1 commits
- **Usage**: 0 invocations across 0 sessions

> Navigate the tldraw SDK documentation efficiently. Use this skill whenever a task involves the tldraw canvas SDK — including the Editor class, shape utils, custom shapes, bindings, tools, persistence, side effects, the store/signals system, sync, UI components, or any tldraw.dev reference. This includes any work in the vade-core repo, which is built on tldraw. tldraw publishes LLM-optimized markdown bundles at tldraw.dev/llms*.txt plus markdown-ready individual pages; this skill teaches which bundle to fetch and how to navigate so agents don't hallucinate API signatures, grab the full mega-bundle when a narrow fetch would do, or guess at topic names that don't exist. Trigger whenever the user mentions tldraw, canvas shapes, ShapeUtil, BindingUtil, tldraw editor, custom tool, snapshot, or is clearly working in a tldraw-based codebase even if they don't name "tldraw" explicitly.
