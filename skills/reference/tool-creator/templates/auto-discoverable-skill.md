# Template — auto-discoverable skill

For knowledge or reference skills that Claude should propose when
the task matches. Examples: `tldraw-docs`, `claude-api`,
`cf-wrangler`, `memo-search`, `commission-retrospective`,
`memo-sync`.

## Frontmatter

```yaml
---
name: <NAME>                # e.g., tldraw-docs, claude-api
description: <ONE-PARAGRAPH-WHAT>. <ONE-PARAGRAPH-WHEN-CLAUDE-SHOULD-PROPOSE>. <ONE-PARAGRAPH-DON'T-INVOKE-FOR>.
---
```

**No `disable-model-invocation` field** — leaving it unset means
the skill is auto-discoverable. The description loads into
Claude's context, so Claude can weigh the skill as a delegation
candidate when a task matches.

**Optional fields** (uncomment + fill if needed):

```yaml
# allowed-tools: Read, WebFetch
# when_to_use: <SUPPLEMENTAL-WHEN-TO-USE-IF-DESCRIPTION-RUNS-LONG>
```

## How auto-discovery works

When Claude sees a user task, it scans available skill
`description` fields for matches. The skill with the best
description-to-task match gets proposed (or invoked, if the
operator has approved auto-invocation).

This means the description IS the skill's discoverability
surface. Optimize it for keyword + intent match:

- **Keywords:** name the technologies / domains / patterns the
  skill covers. Example: `tldraw-docs` description names
  "Editor class, shape utils, custom shapes, bindings, tools,
  persistence, side effects, the store/signals system, sync, UI
  components".
- **Intent verbs:** name what tasks the skill addresses.
  Example: "Reviews and authors Cloudflare Workers code against
  production best practices."
- **Anti-triggers:** add a "SKIP" or "Don't invoke for" clause
  to prevent false-positive matches. Example: `claude-api`
  description ends with "SKIP: file imports `openai`/other-provider
  SDK, filename like `*-openai.py`/`*-generic.py`,
  provider-neutral code, general programming/ML."

## Body skeleton

```markdown
# <name> — <one-line capability>

<2-3 paragraph intro: what the skill is for, what reference docs
or substrate it points to, what it doesn't replace.>

## When this skill helps

- <use case 1: e.g., "User asks how to do X with library Y">
- <use case 2: e.g., "Code imports Y SDK and needs Z feature">
- <use case 3>

## What it does NOT cover

- <anti-trigger 1: e.g., "Other-provider equivalents (use <skill> instead)">
- <anti-trigger 2>

## How to use it (when active)

<concrete steps the skill itself performs once invoked: doc
fetches, pattern lookups, etc.>

## Reference index

<table or list of: topic → canonical doc URL or file path. The
skill's primary value is often this index — it tells Claude
where authoritative content lives so it can fetch on demand.>

## Cross-references

- <related skills>
- <upstream documentation links>
```

## Naming notes

- Same conventions as explicit-invocation: lowercase, hyphenated.
- Description should make the skill *retrievable* by both
  keyword search and intent match. Triple-pass test:
  1. Does a peer agent searching for "<topic>" find it?
  2. Does Claude weigh this skill positively when a relevant
     task arrives?
  3. Does the description have an explicit anti-trigger to
     prevent false-positive invocation?

## Worked example

`vade-coo-memory/.claude/skills/memo-search/SKILL.md` is a good
example. The description names: "Find memos under `coo/memos/` by
natural-language query via Mem0 semantic search over the
`memo_pointer` layer. Use when the user asks 'do we have memos
about X?' or 'what have we decided re: Y?', when keyword
`/memo-query <word>` returned too few hits..."

The description names the action (find memos), the substrate
(memo_pointer layer), the trigger phrasings (natural-language
questions), and the alternative tool to fall back from
(`/memo-query <word>` keyword search). All of that surfaces in
Claude's delegation logic.
