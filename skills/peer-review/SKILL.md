---
name: peer-review
description: Commission three (or N) independent peer reviewers on a long-form authored artifact — essay, paper, foundation doc, RFC, design proposal, plan — and synthesize their feedback. Dispatches sub-agents in parallel via the Task tool, each with a role-specific lens (defaults adapt to the document type — e.g. philosophy essay → analytic phil of mind + frontier-lab ML researcher with phil training + historian/phil of science; engineering RFC → senior systems engineer + security/ops + product-strategy outside lens), each producing strongest-moves / weak-points / missing-considerations / 3–5 concrete revision suggestions. Then, only on explicit user confirmation (never automatically), decomposes the reviews into a trackable atomic-issue revision pipeline on GitHub — parent epic + per-reviewer sub-epic + N atom issues + implementer briefing for asynchronous per-atom PR sessions. Invoke when the user asks for "peer review", "multi-lens review", "independent critique", "feedback from a [philosopher/engineer/historian/X]", "different angles on this draft", or "what would N people from different backgrounds say about this" — even if they don't explicitly say "peer review" but clearly want cross-lens feedback before publishing or shipping. Don't invoke for quick copyedit, single-reviewer asks, code review, operational artifacts (PRs/issues/configs), or short pieces (<1000 words); those are different work.
argument-hint: <file-path> [--roles "r1,r2,r3"] [--n <count>] [--no-decompose]
allowed-tools: Read, Bash, Write, Task
---

# peer-review — multi-lens independent critique on long-form artifacts

Packages the pattern used to review *De-centering Mind* (May 2026):
three independent reviewers dispatched in parallel, strong-convergence
synthesis, optional atomic-issue tracker for asynchronous per-atom
revision via a re-runnable implementer briefing.

Canonical reference artifacts — read these to ground in the shape.
The originating substrate (`vade-coo-memory`) is private, so the
issue links below aren't directly fetchable; treat them as
shape-templates for the kind of decomposition this skill produces,
not as docs a reader can open:

- `vade-coo-memory#635` — parent epic with cross-cutting findings
- `vade-coo-memory#636`, `#637`, `#638` — sub-epic shape (TL;DR +
  paired-file reference + atom checklist)
- `vade-coo-memory#639`–`#673` — atomic issue shape (quote + section
  + suggested edit + scope/cluster/cross-cut labels)
- `vade-coo-memory/coo/briefings/029-decentering-mind-revision-implementer.md`
  — re-runnable per-atom PR session briefing (the template to adapt)

A consumer adapting this skill into their own repository should
substitute their own equivalent paths and tracker conventions.

## When to use this skill

Invoke when:

- The user asks for peer review, multi-lens critique, or independent
  feedback on a long-form authored artifact.
- The user says variants like "get me 3 reviewers", "what would a
  [philosopher / engineer / historian / X] say", "different angles
  on this draft", "let me feedback this", "review from independent
  perspectives".
- A draft is at the polish-before-publish stage and would benefit
  from cross-lens feedback before final revision.

Don't invoke for:

- Quick copyedit / spell-check / proofread — different work; do
  inline or use a simpler editor.
- Single-reviewer requests ("just one person", "your take") — call
  one Agent directly.
- Code review / PR review / config review — operational artifacts
  are reviewed by line-by-line tools and a single domain expert,
  not by lens-driven prose review.
- Short pieces (<~1000 words) — three lenses + synthesis has
  overhead that doesn't pay back at that length.

## Cost note

Phase 1 on a 3–5K-word artifact typically uses ~80–100K Opus tokens
(reviewers plus synthesis) and 5–10 minutes wall-clock when the
reviewers run in parallel; closer to 10–15 minutes when fallback to
sequential authorship is needed (see *Task-tool fallback* below).
Phase 2 (atomic decomposition) adds another ~40 GitHub artifacts and
~30 minutes of session time. This is not free; plan accordingly,
and don't invoke speculatively on borderline-eligible artifacts —
the *Don't invoke for* list above is meant to keep cost honest.

## Phases

The skill has two phases. **Phase 1 always runs; Phase 2 is opt-in.**
Never decompose into atoms without explicit user confirmation —
atomic decomposition is a real commitment (the May 2026 essay
produced 35 atomic issues + 3 sub-epics + 1 parent epic + 1 PR + 1
implementer briefing; that's ~40 GitHub artifacts).

### Phase 1 — dispatch and synthesize

1. **Read the artifact.** Confirm scope, document type, and rough
   length. If the user hasn't named a role set, propose a default
   based on document type (see *Role-set defaults* below) and offer
   to adjust. If the type is ambiguous, *ask* — the role-set choice
   frames the entire review and a wrong frame produces wrong-shaped
   feedback.

2. **Dispatch the reviewers in parallel.** Single message, multiple
   Task tool calls. Each prompt contains:

   - **A vivid role description.** Tenure-track, named tradition,
     named opinions. Not "a philosopher" but "a tenured analytic
     philosopher of mind in the post-Dennett naturalist tradition
     who has engaged closely with Clark/Chalmers and has taught the
     Adams & Aizawa internalist critique many times." Vividness
     matters because subagents have to *become* the role, and
     generic role names produce generic feedback.

   - **The artifact inlined.** Subagents don't share parent context.
     Include the full text between explicit `---ARTIFACT---` /
     `---END ARTIFACT---` delimiters so they don't confuse it with
     instructions.

   - **The framing line.** Constant across reviewers: *"Give a
     constructive peer review… Be rigorous and direct. Charitable
     interpretation first, then your actual critique — but don't be
     deferential. The author wants real feedback. Work from the
     artifact text alone; do not web-search."* Without this line,
     reviewers default to politeness; with it, they engage.

   - **3–7 attend-to prompts.** Role-tuned questions sharpening what
     this reviewer should probe. For the phil-of-mind reviewer on
     *De-centering Mind*: *"Does the 'patterns' invocation do real
     philosophical work? Is the consciousness-bracketing too quick?
     How does it sit relative to Adams & Aizawa internalist
     critiques?"* These prompts make the lens specific to the
     artifact, not just to the role.

   - **Output structure.** Strongest moves / weak points / missing
     considerations / 3–5 concrete actionable revision suggestions.
     Markdown. ~1000 words cap.

   - **Notable-absences hint.** A short list of likely-missing
     citations specific to that reviewer's literature, framed as
     *"you may flag if relevant."* This affordance materially
     improves reviews; reviewers calibrate well from a curated
     absence list.

   - **Length cap + no-web-search.** Both as explicit constraints.
     Both are honored reliably.

   - **Model override.** Specify `model: "opus"` (or equivalent) so
     the reviewer runs on a high-capability model — substantive
     critique work shouldn't default to a cheaper tier.

   **Task-tool fallback.** Some invocation contexts (notably,
   subagent recursion locks in the test harness and some Cowork
   setups) make the Task tool unavailable — the dispatch will fail
   with *"No such tool available: Task. Task is not available
   inside subagents."* If this happens, **don't bail.** Author the
   reviews sequentially in your own context, one role-lens at a
   time. Between reviewers, do a clean break: restate the new role
   description at the top of the new review and re-anchor on the
   artifact text fresh, so each reviewer's framing isn't
   contaminated by the previous one's vocabulary. Flag the fallback
   in the transcript so the user knows which structural guarantees
   were preserved (independent framing, vivid roles, length cap, no
   web-search) and which were approximated (wall-clock parallelism,
   context-isolation between reviewers). The deliverable shape is
   the same; only the dispatch mechanism differs. Empirically (see
   `peer-review-workspace/iteration-1/`), the sequential fallback
   still hits 100% on the structural assertions; it's just slower.

3. **Synthesize convergence.** After all reviewers return:

   - Identify atoms that appear in ≥2 reviews → flag as
     cross-cutting findings.
   - Identify sections all reviewers praised → flag as load-bearing
     strengths to preserve.
   - Identify sections all reviewers flagged → strongest revision
     signal; lead with these.
   - Produce a TL;DR per reviewer (strongest / weakest / theme).
   - Order the cross-cutting findings by leverage — resolving one
     should incidentally resolve overlap elsewhere.

4. **Deliver to the user.** Cross-cutting synthesis up top, then the
   full reviews verbatim. End with the phase-boundary question:

   > Want me to break these into a trackable issue tree (Phase 2)?

   Don't proceed without affirmative confirmation.

### Phase 2 — atomic decomposition (opt-in)

Run only on explicit user request. The decomposition produces a
trackable issue tree plus a re-runnable implementer briefing so the
per-atom PR work can happen asynchronously across multiple sessions.

1. **Land the artifact + reviews to `coo/_drafts/<topic>/`:**

   - `<topic>.md` (the artifact itself, working file for PRs)
   - `review_<role>.md` per reviewer (paired files; long-form review
     text doesn't belong in issue bodies — issue-shape-lint per
     `coo/operations/issue-pr-hygiene.md`)

2. **Create labels** (reuse existing if present; create otherwise):

   - `<topic-marker>` — project marker, e.g., `essay:decentering-mind`
   - `reviewer:<r1>` / `reviewer:<r2>` / `reviewer:<r3>` — lineage
   - `cluster:<theme>` — strategic groupings discovered in synthesis
     (e.g., `cluster:literature`, `cluster:calibration`,
     `cluster:we-problem`)
   - `cross-cut` — atoms flagged by ≥2 reviewers
   - `scope:line` / `scope:paragraph` / `scope:section` — work-size
     triage

3. **Create the issue tree in this order** (later references earlier
   IDs):

   a. **Parent epic** — workflow summary, cross-cutting findings,
      sub-epic placeholders, label taxonomy, out-of-scope notes.
   b. **Three (or N) sub-epics** — one per reviewer. TL;DR (strongest
      / weak / theme) + paired-file reference + atom checklist
      placeholder. Don't paste the full review into the issue body
      (lint will warn at ~600 words; the paired file is the
      canonical artifact).
   c. **N atomic issues** — one per concrete critique. Each carries:
      - Section reference (e.g., "§3 — Mind beyond the skull")
      - Verbatim reviewer quote
      - Suggested edit (if the reviewer offered one; otherwise mark
        "suggested edit deferred to author")
      - Cross-cut signal pointing at overlapping atoms in other
        reviewers' rosters when applicable
      - Scope + cluster + cross-cut labels as appropriate

   Atom-creation scales well by batched shell script — write one
   script per reviewer that loops `gh issue create` with heredoc
   bodies. The May 2026 work created 35 atoms in ~3 minutes this
   way; doing them by individual Bash calls would have been slow
   and error-prone.

4. **Update sub-epic bodies with atom checklists**, and update the
   parent epic body with sub-epic links + atom ranges, after all
   atoms are filed and IDs are known.

5. **Write the implementer briefing** under
   `coo/briefings/NNN-<topic>-revision-implementer.md`. Use
   `coo/briefings/TEMPLATE.md` as the shape; use briefing 029 as the
   worked example. The briefing must:

   - Use the existing `readiness:ready` label as the trigger
     marker (per cross-repo taxonomy MEMO-2026-04-22-09; don't
     invent a new label).
   - Name the exact query filter:
     ```
     gh issue list --label "<topic-marker>" \
       --label "readiness:ready" --state open
     ```
     plus `-label type:epic` to filter out parents/sub-epics.
   - Call out natural cluster bundles based on `cluster:*` labels —
     e.g., several `cluster:literature` atoms may bundle into one
     PR that adds a citations paragraph + bibliography entries.
   - State that comments override the suggested edit in the body
     (Ven's per-atom decisions are authoritative).
   - Be **re-runnable**: each commissioning queries the current
     ready set fresh. Don't bake in a specific batch.
   - Cap output per session at one atom or one coherent cluster
     bundle (per the harness branch model — one branch per session).

6. **Open one PR** to land artifact + reviews + briefing to the
   working branch. Use `bin/gh-pr-create.sh` for the closing-keyword
   lint. Use `Closes: n/a` since this PR is the on-ramp, not a
   resolution. Subscribe per PR-watch discipline.

7. **Summarize the tree** to the user: parent epic number, sub-epic
   numbers, atom range, PR number. Explain the readiness convention:

   > Apply `readiness:ready` to atoms you want implemented (with
   > optional comment-modifications to the suggested edit).
   > Commission a fresh session against briefing NNN; it picks up
   > the ready set, drafts focused PRs, hands back.

## Role-set defaults

The skill *proposes* role sets rather than hard-coding. The pattern
is: pick role-lenses that *are the literature* the artifact engages
with, plus one outside lens that knows the genre's failure modes.

| Artifact type | Default roles |
|---|---|
| Philosophical essay on mind / AI / cognition | analytic phil of mind · frontier-lab ML researcher with phil training · historian / phil of science |
| Engineering RFC or architecture doc | senior systems engineer (or domain specialist) · security / ops · product-strategy outside lens |
| Product proposal / customer pitch | user-empathy / customer-zero · business-strategy · technical-feasibility |
| Empirical research paper | methodologist for the specific design · domain expert · cross-domain reader-out |
| Cultural / lineage essay / retrospective | relevant domain scholar · comparable-corpus reader · reader-out outside lens |
| Plan / strategy doc | execution-oriented PM · skeptic / red-team · stakeholder-empathy |

If the document type is ambiguous, *ask* — don't guess between two
plausible role-sets without confirmation.

## Anti-patterns

- **Don't auto-decompose into atoms.** The decomposition is a real
  cost commitment. Always make Phase 2 opt-in.
- **Don't use generic role descriptions.** "An expert" or "a
  philosopher" produces generic feedback. Vividness (named
  tradition, named opinions, specific literatures) is load-bearing.
- **Don't share context between reviewers.** They're meant to be
  independent. Don't include other reviewers' prompts or hints in
  any one's brief. Convergence emerges from independent dispatch;
  coordination contaminates it.
- **Don't web-search.** Reviewers should engage with the artifact,
  not Google around. The constraint matters; reviewers honor it.
- **Don't pad with deference.** "Charitable interpretation first,
  then real critique — no deference" is the constant framing line.
  Reviewers default to politeness without it.
- **Don't run the skill on short pieces.** Three lenses + synthesis
  on a <1000-word piece is overkill; the lenses have nothing to
  differentiate.
- **Don't dispatch sequentially.** Single message, multiple Task
  calls = parallel execution. Sequential dispatch wastes wall-clock
  and risks one reviewer's response biasing the next's framing if
  they somehow share state (they shouldn't, but the parallel form
  is structurally cleaner).

## Examples

### Phase 1 invocation (philosophy essay)

```
/peer-review /path/to/essay.md
```

The skill reads the essay, identifies it as philosophical, proposes
the phil-of-mind / ML / historian role set, asks for confirmation,
dispatches three Task agents in parallel, synthesizes, delivers, and
asks about Phase 2.

### Phase 1 invocation with custom roles

```
/peer-review /path/to/engineering-rfc.md --roles "kernel-engineer,security-architect,product-pm"
```

Skill uses the named roles instead of defaults. Confirms before
dispatching.

### Phase 2 follow-on

User confirms Phase 2 after reviewing Phase 1 output. Skill files
the issue tree (~40 artifacts for a 5K-word essay), writes the
implementer briefing, opens the landing PR. Subscribes.

## Out of scope

- Choosing whether to publish the artifact (author's call after
  revision).
- Drafting the per-atom PRs (separate implementer session per
  briefing NNN; see briefing 029 for the canonical template).
- Cross-posting, SEO, venue selection.
- Final copyedit / proofread.

---

*v1.1 — iteration-1 eval fixes (vade-coo-memory#675; iter-1 in
`peer-review-workspace/iteration-1/`). Added: cost note + Task-tool
fallback paragraph. Eval surfaced that subagent contexts can't
recurse Task; the skill now instructs sequential authorship as a
documented fallback rather than letting the agent improvise.*

*v1.0 — initial packaging from the May 2026 De-centering Mind
workflow (vade-coo-memory#635 / #674 / briefing 029).*
