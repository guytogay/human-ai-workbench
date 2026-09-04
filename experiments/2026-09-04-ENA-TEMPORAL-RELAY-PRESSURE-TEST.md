# ENA Temporal Relay Pressure Test

Date: `2026-09-04`

Status: `REAL-USE OBSERVATION / CANDIDATE WORKBENCH METHOD / NOT_YET_UNIVERSAL_TEMPLATE`

## What happened

ENA's Temporal Assimilation / Developmental Order experiment supplied the first real pressure test for the relay problem recorded in `2026-09-04-HUMAN-AI-AUTOMATION-EXPLORATION.md`.

The scientific requirement was legitimate: each primary run needed a fresh ChatGPT Temporary Chat, treatment isolation, staged interaction and verbatim first-output capture.

A local Codex helper reduced some mechanical browser/clipboard handling, but the overall workflow still depended on a human-visible relay between the manager session and fresh experimental sessions.

The experiment completed successfully, but the coordination cost was real enough that it should affect the design of later work.

## Main lesson

The first response to coordination friction should not automatically be to automate the existing workflow.

Ask first whether the workflow can be redesigned so the coordination step disappears.

```text
REDUCE COORDINATION BY DESIGN
BEFORE
AUTOMATING COORDINATION
```

or, more operationally:

```text
REMOVE THE RELAY STEP IF POSSIBLE
-> AUTOMATE ONLY THE RELAY THAT REMAINS NECESSARY
```

This is different from merely adding an orchestrator.

## Why this matters

Suppose an experiment requires ten staged exchanges per fresh worker.

One response is:

```text
build machinery to relay ten stages automatically
```

A cheaper response may be:

```text
redesign the experiment so the same discriminating evidence can be obtained from one frozen treatment delivery
```

If scientific validity is preserved, the second approach removes:

- human copy/paste burden;
- transport failure modes;
- stage-order drift;
- state-machine complexity;
- orchestration infrastructure;
- extra surfaces that themselves require governance.

Automation should not preserve accidental complexity merely because the complexity already exists.

## Immediate follow-on evidence

The next ENA mechanism design, Metamemory Update Policy v1, applied this lesson before primary collection.

Instead of copying the Temporal staged pattern, it was redesigned around:

```text
one fresh worker
+ one complete treatment payload
+ one first-output capture
= one run
```

The experiment still preserves:

- fresh-worker isolation;
- exact treatment delivery;
- first-output evidence;
- cross-arm comparability;
- frozen validity and stop rules.

But it removes developmental stage-by-stage relay because that staging is not causally required for the metamemory question being tested.

This is a concrete example of project method improving experimental design rather than merely wrapping it in more tooling.

## Boundary

This lesson does **not** mean every multi-turn workflow should be flattened.

Keep staging when the causal question itself depends on:

- intermediate commitment;
- feedback after each action;
- temporal ordering;
- state accumulated through interaction;
- human judgment at a real decision boundary.

The test is:

> If the intermediate relay vanished, would the phenomenon under study or the decision quality materially change?

If yes, preserve the stage and automate transport where useful.

If no, remove the stage before building automation around it.

## Relationship to HUMAN IN THE LOOP != HUMAN AS THE LOOP

The earlier candidate principle remains useful:

```text
HUMAN IN THE LOOP
!=
HUMAN AS THE LOOP
```

This occurrence adds a second dimension:

```text
AUTOMATED LOOP
!=
NECESSARY LOOP
```

The objective is not maximum autonomous machinery. It is maximum useful human judgment with minimum unnecessary coordination.

## What to test next

Use the Metamemory one-shot primary round as the next real measurement point.

Record:

- human transport actions per run;
- whether any action requires judgment rather than transport;
- treatment-delivery errors;
- output-capture errors;
- whether remaining relay burden is large enough to justify API/Agent-runner automation.

Do not build a persistent multi-Agent orchestrator unless the reduced workflow still produces repeated material pain.

## Promotion rule

Do not add a permanent Workbench template solely from this one occurrence.

Promote this into a stronger reusable method only if additional unrelated work confirms the same pattern:

```text
existing workflow has coordination pain
-> removing unnecessary stages preserves outcome quality
-> coordination cost drops
-> the lesson transfers beyond ENA
```

Until then, retain it as a strong real-use observation.
