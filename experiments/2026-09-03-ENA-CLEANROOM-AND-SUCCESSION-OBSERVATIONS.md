# Real-use observation — ENA cleanrooms, null results, and deep succession

Date: 2026-09-03

Status: `REAL_PROJECT_OBSERVATION / NOT_A_NEW_TEMPLATE_YET`

## 1. Real project/task

The Human-AI Workbench was indirectly exercised while a human and ChatGPT continued the long-lived `evolution-native-agent-architecture` (ENA) project through:

- research divergence/convergence;
- multiple fresh-AI validation rounds;
- disposable GitHub cleanrooms;
- treatment-arm preregistration;
- negative/null result interpretation;
- branch cleanup;
- a deep session succession request.

The work was already worth doing for ENA; no artificial demo project was created for Workbench.

## 2. What coordination patterns actually helped

### One hot status surface remained valuable

`NOW.md` was much cheaper than rereading old release/handoff machinery for ordinary continuation.

When the next action was clear, a full audit added cost without improving the decision.

### Deep succession was still necessary once

Near the end of a very long, decision-heavy session, the human explicitly asked for a detailed handoff because continuity risk was now high.

A normal 10-exchange slice would have omitted:

- several experiment generations;
- negative results;
- research-coverage obligations;
- cross-repository boundaries;
- branch cleanup state;
- experiment-design lessons.

The useful adaptation was **not** “increase the default transcript window.”

It was to distinguish:

```text
NORMAL CONTINUATION
vs
DEEP SUCCESSION
```

and use a structured deep handoff only when the risk justified it.

## 3. Fresh evaluator context worked in the opposite direction

Fresh validation needed **less author context**, not more.

An early design mistake was to consider telling fresh validators not to inspect ENA source/research/oracle surfaces.

The human pointed out that this itself reveals hidden answer surfaces.

The improved pattern became:

```text
STRUCTURAL ABSENCE OF CONTAMINATION
>
PLEASE IGNORE KNOWN CONTAMINATION
```

Separate disposable repos and later orphan/root commits removed source-project/bootstrap history from the evaluator's reachable surface.

This is important for Workbench because “more continuity context” is not universally good. Context strategy depends on the role of the receiving AI.

## 4. Byte/structure equality paid evidential rent

Across treatment arms, identical common framework/task trees were verified rather than assumed.

This reduced arguments after the result about whether an accidental file difference caused the observed behavior.

Generalizable observation:

> When the claim depends on only one experimental variable changing, make the common substrate actually identical where practical.

This is not needed for normal work; it is useful when AI behavior itself is evidence.

## 5. Preregistration prevented post-hoc victory stories

Before the I/J/K/L inheritance pilot, the project wrote down unfavorable interpretations:

- if no-inheritance performs equally well, no inheritance benefit was demonstrated;
- if successful recipe performs as well as boundary-oriented inheritance, superiority is weakened;
- if full archive performs as well, a special compact inheritance unit may not be necessary in that setting.

The observed result was a four-way qualitative tie.

Because interpretation was written first, the project did **not** reinterpret “all groups succeeded” as a win for the favored boundary-memory hypothesis.

Generalizable observation:

> A tiny preregistration can be more valuable than a large evaluation framework when it prevents moving the goalposts.

## 6. Null results changed the project correctly

Two kinds of null/negative result mattered:

### Baseline did not fail

Semantic-reachability baselines were good in 8/8 tested cases.

The project cancelled planned “repair” arms instead of running them anyway.

Lesson:

```text
NO DEFECT OBSERVED
-> DO NOT BUILD REPAIR FOR PLAN COMPLETENESS
```

### Treatment arms did not differ

I/J/K/L all behaved well.

The project narrowed the mechanism claim and moved on.

Lesson:

```text
NO DIFFERENCE
-> INSPECT SATURATION / TREATMENT NECESSITY / THEORY SCOPE
```

not:

```text
NO DIFFERENCE
-> ADD MORE TRIALS UNTIL FAVORITE WINS
```

## 7. Strong AI reasoning can saturate mechanism experiments

The inheritance pilot's target prompt itself contained enough current-world semantics for GPT-5.6 Sol at high reasoning to derive the correct policy without predecessor experience.

The no-inheritance control therefore matched all inheritance arms.

Generalizable observation:

> If testing memory/training/inheritance/workflow mechanisms, the target task must give the treatment a real causal opportunity to matter.

For ENA this changed the next experimental design from one-shot Q&A to a multi-stage developmental setup.

## 8. First complete output should be captured before tutoring

Fresh-session outputs were treated as evidence only before correction dialogue.

After collection, substantive responses were archived back into the source project before disposable cleanrooms were deleted.

Generalizable lightweight sequence:

```text
RUN
-> CAPTURE FIRST COMPLETE OUTPUT
-> ADJUDICATE
-> DISCUSS/CORRECT
-> ARCHIVE DECISION-RELEVANT EVIDENCE
-> DELETE DISPOSABLE SURFACE
```

## 9. Branch bloat exposed a real coordination failure

ENA had accumulated many branches from release, candidate, validation, research, alignment, and experiment work.

Most had completed their purpose but still existed.

A long-lived research branch also drifted behind `main` while retaining three unique files.

Two opposite mistakes were possible:

- keep every branch forever out of fear;
- delete everything because the list is ugly.

The useful rule was:

```text
CHECK UNIQUE MATERIAL
-> PRESERVE WHAT MATTERS
-> DELETE PURPOSE-EXHAUSTED SURFACE
```

The project also moved away from a permanent integration branch toward `main + short-lived PR branches`.

Generalizable observation:

> Temporary coordination surfaces should have retirement conditions. A workspace is not automatically an archive.

## 10. What this observation changes in Workbench now

Promote now:

- distinguish NORMAL continuation, DEEP succession, and FRESH evaluation context modes;
- preserve negative/null results in handoff when losing them would cause repeat work;
- allow structured deep handoffs instead of treating a fixed conversation-count default as a law;
- record lightweight experiment guidance for preregistration, first-output capture, structural isolation, null results, and temporary workspace cleanup.

Do **not** promote yet:

- a universal cleanroom template;
- mandatory SHA/tree verification for ordinary projects;
- a general experimental-governance layer;
- ENA-specific concepts such as Constitution IDs, MDS, boundary memory, or Effect Lifecycle.

## 11. Follow-up question for Workbench

The next evidence should come from another real project or another substantially different AI collaboration task.

Questions:

- Does the NORMAL/DEEP/FRESH context split remain useful outside ENA?
- Does a structured deep handoff reduce reconstruction cost better than a longer transcript slice?
- Which parts of the lightweight experiment method recur often enough to deserve a standalone template?
- Does branch/workspace retirement remain valuable for non-research projects?

Until repeated use answers these, keep this file as an observation rather than expanding the Workbench into a governance system.

## 12. Treatment exposure is an execution fact, not a readiness claim

The later ENA developmental-inheritance experiment exposed a new execution-integrity failure that the earlier cleanroom method did not catch.

Two fresh experimental successors returned plausible initialization/readback responses for the same treatment repository, but later provenance responses independently stated that they had **not actually opened/read the treatment before the behavioral probes**.

The important general working-method distinction is:

```text
RESOURCE ADDRESS PRESENT
!= RESOURCE OPENED
!= FULL INPUT INSPECTED
!= INPUT ASSIMILATED
```

A `READY` acknowledgement is therefore not proof of treatment delivery. A shallow readback such as the first visible line can also be satisfied without establishing that the decision-relevant input was actually inspected.

For experiments where exposure itself is part of the causal intervention, verify exposure **before** collecting behavioral evidence.

The useful pattern from the replacement run was a lightweight, non-semantic verification that required access to a structurally distant part of the file—for example a non-empty-line count plus the exact final non-empty line. This strengthened evidence that the file had actually been traversed without asking the successor to summarize or rehearse the treatment semantics.

Important limits:

- proof of inspection is still not proof of assimilation;
- self-reported provenance is evidence, not an objective tool trace;
- if independent execution/tool traces are available, prefer them for proving access;
- do not ask for a semantic summary merely to prove reading, because the verification itself can become an extra treatment exposure or rehearsal;
- choose verification fields before seeing behavioral quality when practical, so verification cannot become a selective way to discard inconvenient outcomes.

Protocol classification should remain explicit:

```text
TREATMENT NEVER ACCESSED BEFORE PROBES
= protocol failure

TREATMENT ACCESSED, THEN MISREMEMBERED OR MISUSED
= valid behavioral outcome
```

Protocol-deviant attempts should be preserved rather than silently deleted.

Generalizable observation:

> When AI behavior is evidence and treatment delivery is causal, verify the delivery event separately from the behavioral response. Do not infer execution from compliance language.

This remains an **observation**, not yet a universal Workbench template. Reuse in another real experiment should determine whether a reusable treatment-exposure checklist is warranted.
