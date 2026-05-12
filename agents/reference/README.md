# Reference agents

The two agents here — `safety-auditor` and `emancipatory-auditor` —
encode discipline patterns that have been useful inside the VADE
substrate. They are NOT meant to be installed verbatim into another
project.

**Canonical install path:** run `/adapt-skill <name>` (from
[`../../skills/adapt-skill/`](../../skills/adapt-skill/)) per
agent you want to install. The meta-skill reads each agent's
`# Setup hints` manifest at the bottom of its `.md` file,
conducts a structured interview, and writes the adapted version
to `.claude/agents/<name>.md`. The fork-and-adapt path below
remains an option for users who want to rewrite by hand.

- `safety-auditor` carries a `min_count: 2` directive on its
  governance-rules hint — without ≥2 real rules, the adapted
  agent isn't emitted (a rule-less auditor PASSes everything,
  which is worse than no auditor).
- `emancipatory-auditor` carries a `philosophical_gate:` —
  the double-clause is a theory of value, not just a path set.
  Users who don't share the theory are routed to author from
  the pattern instead of mechanical adaptation.

## Why "reference"

Both auditors cite VADE-internal governance memos
(`MEMO-YYYY-MM-DD-<suffix>`) that name specific disciplines we hold
ourselves to: the Tier-2 disposition rule, the Mem0 content rule,
the spend cap, the subject + emancipatory double-clause. Those memo
references won't resolve in your project — and the disciplines they
encode may not be ones you want to enforce.

The value here is the **shape**: an adversarial Phase-3 teammate
that gates artifacts against a named, written set of rules. Lift
that shape, swap the rules for your own, and the auditor pattern
ports cleanly.

## How to adapt

1. Copy the relevant `.md` file into your own `.claude/agents/`.
2. Edit the description to name *your* rule set (your governance
   memos, your style guide, your acceptance criteria).
3. Rewrite the rubric inside the agent's body to score artifacts
   against your rules, not VADE's.
4. Wire your team's review or merge flow to spawn the agent at the
   gate point you care about.

## Why not install verbatim

If a peer agent installs `safety-auditor` unchanged and dispatches
it, the auditor will fail to find the memos it references and will
either produce hollow verdicts (everything passes for the wrong
reason) or noisy verdicts (everything fails because the rule-source
is missing). Neither is useful. The `agents/` siblings
(`research-investigator`, `lineage-interpreter`, etc.) are
substrate-agnostic and install cleanly; these two are not.
