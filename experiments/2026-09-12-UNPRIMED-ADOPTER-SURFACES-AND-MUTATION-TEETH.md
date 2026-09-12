# Unprimed adopter surfaces, mutation teeth, and parser-checked documentation

Date: 2026-09-12
Status: `METHOD_RECORD` — transferable practice, stated without relying on any product-specific
concept, contract, or internal state name. (Provenance: the ENA coordination work of 2026-09-12;
the occurrences are cited only as evidence, not as the definition.)

## 1. The evaluation a system cannot run on itself

Reviewers inside a project inherit its assumptions. Self-tests confirm what the authors already
believe; they are structurally unable to surface "a newcomer cannot get started". The gap is not
test *coverage*, it is **information state**.

**Practice — the unprimed adopter surface.**

1. Publish a **separate, disposable surface** containing only: the artifact under evaluation, a
   neutral task statement, and the rules of the exercise. No design notes, no oracle, no known
   defect list, no conversation history.
2. Make the surface **structurally** clean, not merely declared clean. A repository whose history
   contains prior experiment context is not a fresh surface even if the working tree is replaced;
   use a single orphan commit or a throwaway repository. *Do not tell an evaluator that hidden
   context exists and then ask it not to look — remove the contamination instead.*
3. Give the evaluator a role that makes confusion reportable: **nobody will help you**, and the
   three most valuable outputs are (a) where you had to stop and think, (b) what the documentation
   told you versus what you had to discover, (c) the raw commands, exit codes and output.
4. Explicitly require it to attempt **three things the documentation does not bless** — the
   plausible mistakes a newcomer makes — and to classify each response as caught / ignored /
   confusing.
5. Require the evaluator to **declare its own evidence boundary**: what it could not execute, what
   it did not verify, and which conclusions are reading-only. In the observed run the evaluator
   volunteered that its shell could not reach the network, that it executed copied code paths
   rather than a byte-verified checkout, and listed seven capabilities it had *not* exercised.
   That paragraph is what makes the rest of the report usable.
6. **Replay after the fix.** Run the same class of evaluator against the revised artifact and ask
   the same questions. Comparing two reports measures whether the friction actually went away;
   a second evaluator of a different model family is worth spending only if structural problems
   remain.

Cost note: the surface is a snapshot and a task file; the evaluation runs on an ordinary chat
session. The information gain per unit of effort is far higher than another author-written test.

## 2. Passing is not evidence until the check can fail

Two relations that look alike and are not:

```text
the check passes                 -> the artifact may still be broken
the check passes AND fails when the artifact is broken -> evidence
```

**Practice — mutate the real artifact, not a strawman.** Writing a deliberately wrong stand-in
proves the harness can fail *in principle*. The stronger step, done last, is to take the **actual
verified revision**, patch one behaviour out of it in a scratch copy, and require the harness to
report a failure that names that behaviour. Mutations worth using:

- neuter an input validator so it accepts everything (must break the rejection check, while the
  accept-valid check still passes — this distinguishes "rejects correctly" from "rejects
  everything");
- delete a required user-facing notice;
- delete a required sentence from documentation;
- make a fail-closed path succeed by inventing a plausible value.

Also demand **satisfiability** of every clause check: install the required sentence/behaviour in a
scratch copy and require the check to go green. A check that can never pass is as worthless as one
that can never fail, and it is harder to notice.

Corollary for the harness itself: when a check fails, **read the artifact's own message before
believing the failure**. In the observed work, five apparent product failures were all defects of
the measurement: a fixture invalidated by the probe's own edit (a duplicate key the strict reader
correctly refused), a tool invoked with the wrong interface, a value the tool was right to reject,
a scalar parsed as a string rather than a boolean, and an exit code read through a shell pipeline
instead of directly. **Measure the raw result; do not read it through a wrapper.**

## 3. Documentation that the product cannot execute

A document that instructs a user to write something the product's own reader rejects is a defect
with a specific shape: it is invisible to unit tests, invisible to code review of the code, and
fatal to the person who follows it.

**Practice — parse the documentation with the real parser.**

1. Extract every fenced example that claims to be configuration (not prose lists) from every
   user-facing document.
2. Run each through **the actual reader** the product uses, not a general-purpose parser. A
   deliberately narrow parser is legitimate; documentation that contradicts it is not.
3. Classify failures: syntax the reader refuses by design (a violation) versus fragments that
   legitimately need surrounding context (a note).
4. Seek the **smallest differentiating cases** rather than a verdict: here, flow-empty, flow-item
   and nested-mapping forms parsed while block sequences did not — a matrix that turns "the docs
   are wrong" into "change the example to a nested mapping", which is a one-line fix.
5. Check whether the restriction is discoverable: in the observed case the limitation existed only
   in a source comment. A limitation a user cannot find is a limitation they will hit.

The durable fix is a regression test in the product repository that feeds its own documentation to
its own reader — made in the same change, and registered in CI, otherwise the guard never runs.

## 4. Routing closure and refusal are product features

From the same evaluation: the most valuable thing the artifact did was **refuse**. A cold,
unassisted evaluator could not complete setup, and the correct outcome was a machine-decidable
"not ready" with reasons — not a guess, not a silently borrowed default, not a manufactured
initialized state. Two design lessons generalize:

- **A "not ready" verdict must be executable and bounded**, and it must be able to say *why*. An
  artifact that can only answer "ready" or "broken" forces users to fabricate the missing inputs.
- **One readiness definition.** If two entry points can disagree about readiness, the weaker one
  becomes the effective contract. Verify explicitly that the definitions agree, including on the
  failure side, and that an unusable user-supplied justification is rejected rather than counted.
- **Do not make every operation depend on a global gate.** Setup, repair and diagnostic actions
  are legitimately useful while the artifact is not ready; blanket gating creates a circular
  bootstrap. State the boundary instead: one tool decides readiness for ordinary work; success of
  a setup action does not imply readiness is complete.
