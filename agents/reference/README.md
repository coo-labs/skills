# Reference agents

The two agents here — `safety-auditor` and `emancipatory-auditor` —
encode discipline patterns that have been useful inside the VADE
substrate. They are NOT meant to be installed verbatim into another
project.

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
