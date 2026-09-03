# Handoff

A handoff is not automatically a project archive. Its job is to carry enough context for the next AI to continue correctly at lower cost than reconstructing the project.

## First choose the mode

### NORMAL — default

Use when current `NOW.md`, a relevant conversation slice, and a few linked artifacts are enough.

### LIGHT

Use for simple continuation with little ambiguity.

### DEEP SUCCESSION — exception

Use when losing the current session is likely to erase a long decision chain, experimental oracle/design, important rejected approaches, cross-repository boundaries, or reusable method that cannot be recovered cheaply.

A deep succession may use a structured summary/package instead of blindly pasting a very long chat window.

### FRESH EVALUATION — not a handoff

If the next AI is supposed to make an independent/unprimed judgment, **do not use this project handoff as its input**. Create an isolated evaluation surface containing only the material legitimately available to the evaluator.

## 1. Current state

Attach or link the project's current `NOW.md`.

Do not rewrite the same state into another long summary unless deep succession genuinely needs a richer projection.

## 2. Recent conversation slice

Default for NORMAL: **10 relevant user/assistant exchanges**.

One exchange = one user message + the assistant response.

Heuristics:

- **LIGHT — 5 exchanges**
- **NORMAL — 10 exchanges**
- **DEEP — 15–20 exchanges** when a contiguous recent argument carries the needed state

But real use showed that a complex deep succession can be better served by a structured decision-bearing summary than by simply increasing the transcript count.

The question is:

> What representation lets the next AI reconstruct the correct decision state with the least distortion and unnecessary context?

## 3. Earlier context worth carrying

For NORMAL, add at most 3 earlier items by default when recency alone would hide something decision-relevant.

For each:

- **What:** quote, decision, artifact, or link.
- **Why it still matters:** one sentence.

For DEEP SUCCESSION, add more only when each item protects against a concrete continuity failure.

## 4. Current artifacts

Link what the next action needs.

- Working file / branch / PR:
- Active issue:
- Test/evidence artifact:
- Current result/oracle, if relevant:

Machine-known facts such as CI run IDs and checksums should normally be retrieved from Git/CI rather than copied unless exact identity is itself decision-critical.

## 5. Explicit human direction

Carry instructions whose loss would materially change the work, especially:

- rejected approaches;
- scope boundaries;
- desired output/work style;
- decisions that should not be silently reopened;
- what the human considers a meaningful vs pointless experiment;
- cross-repository ownership/boundary decisions.

## 6. Negative and null results

When relevant, explicitly record:

- what failed;
- what tied/no-differenced;
- what hypothesis was narrowed;
- what should not be rerun just to obtain a preferred result.

Negative evidence is easy for summaries to erase and expensive for future sessions to rediscover.

## 7. “Do not redo” list

Include only likely expensive repetitions, for example:

- a branch already superseded;
- an experiment whose baseline passed and therefore needs no repair arm;
- a hypothesis already narrowed by a preregistered null result;
- a temporary workspace whose unique material has already been archived.

## 8. Next consequential action

Write one concrete next action.

If the next AI can understand the goal, decisions, unknowns, constraints, and this next action, the handoff is sufficient.

## 9. Deep-succession extras — only when justified

A DEEP handoff may add:

- project/repository ecosystem map;
- recent decision-bearing rounds;
- method/lessons learned;
- experimental design constraints;
- cleanup/migration state;
- file read-order catalog;
- explicit fidelity limits of archived evidence.

Do not promote these extras into mandatory templates for every project unless repeated use proves their value.

## Receiver behavior

For NORMAL continuation:

1. Read `NOW.md`.
2. Read the recent slice/linked artifact.
3. Resolve current goal, decided facts, unknowns, next action.
4. Start work.

For DEEP succession:

1. Read `NOW.md`.
2. Follow the structured handoff entrypoint.
3. Reverify mutable live facts before writes.
4. Retrieve only deeper history needed by the next action.
5. Continue without asking the human to repeat persisted project background.

Do **not** perform a full repository/project audit unless the current action genuinely depends on it.

If the handoff is insufficient, retrieve the smallest missing piece rather than rebuilding the entire project history.
