# Human-AI Workbench

A practical way to run long-lived projects with AI **without turning project coordination into the project itself**.

This repository is not a constitution, governance framework, or certification system. It is a small set of working habits and templates for humans and AI systems that need to continue real work across sessions, models, and tools.

The workbench should remain **cheaper than the work it helps coordinate**.

## Repository role and canonical ownership

Human-AI Workbench is the canonical home for **generalizable human-AI project-working method** discovered through real projects.

It may originate from experience inside another project and then return to serve that project, while remaining independently reusable elsewhere.

The first major example is ENA:

```text
ENA real project work
-> repeated collaboration / continuity / experiment friction
-> extract the project-general method
-> Human-AI Workbench
-> method returns to support ENA
-> same method can be tested in unrelated projects
```

Repository boundaries:

- `guytogay/evolution-native-agent-architecture` owns ENA theory, mechanisms, Current/release semantics, ENA research evidence, and ENA-specific project occurrences.
- `guytogay/human-ai-workbench` owns reusable human-AI collaboration method: continuation, handoff, project-state practice, lightweight experiment execution discipline, and temporary-workspace lifecycle when those patterns generalize beyond ENA.
- `guytogay/ena-field-guide` owns evidence-backed practical HOW for applying ENA-derived mechanisms in Agent/Host work.

Do not keep parallel canonical copies merely because a method was first discovered inside ENA.

Preferred ownership transition:

```text
project occurrence discovers method
-> Workbench becomes canonical for the reusable method
-> originating project keeps only its local adapter / occurrence / evidence
```

This is not a demand to move every project-specific detail here. A method belongs here only when it can be stated without requiring ENA-specific theory or one project's internal state.

## Start here

For an active project, keep one short live status file based on [`templates/NOW.md`](templates/NOW.md).

A new AI session should normally:

1. Read `NOW.md`.
2. Read the recent conversation slice or structured handoff material that `NOW.md` actually points to.
3. Open only the files, issues, or artifacts needed by the current task.
4. Be able to answer:
   - What is the current goal?
   - What is already decided?
   - What is still uncertain?
   - What is the next consequential action?
5. If those are clear, **start working**. Do not perform a full project audit by default.

## Use the right context mode

Real use showed that “handoff” and “independent evaluation” need opposite context strategies.

### Normal continuation — default

Use the smallest context that preserves correct continuation:

```text
NOW
-> relevant artifact / recent slice
-> work
```

Do not expand context merely because more history exists.

### Deep succession — exception

Use a structured deep handoff when losing the current session would likely erase a long decision chain, active experimental design, important rejected approaches, cross-repository boundaries, or method learned during the session.

A deep handoff may be much richer than the normal 10-exchange default when that richness actually prevents expensive reconstruction.

The important rule is:

```text
HANDOFF DEPTH TRACKS CONTINUITY RISK
```

not:

```text
EVERY SESSION CHANGE -> MAXIMUM CONTEXT DUMP
```

### Fresh independent evaluation

When the goal is an unprimed first judgment, do **not** give the evaluator the project-manager handoff.

Prefer structural isolation:

```text
only the target/task/common material needed for evaluation
+ no hidden answer/oracle/project-history surface
```

Do not reveal that an answer exists elsewhere and then tell the evaluator not to look for it.

## Before a consequential step

Do not stay head-down indefinitely. At major milestones, scope changes, substantial new mechanisms, or phase transitions, reconnect the next action to the project plan.

Ask briefly:

- Who are we solving this for?
- What concrete problem are we solving?
- What approach are we currently using?
- What SMART evidence would count as success?
- How does this step move us closer to that success?
- Are we solving the original problem, or mainly maintaining machinery created by our previous solution?
- Does the intended portability still match the project: local, reusable, or general?

If the goal or approach should change, change it explicitly. **Do not drift silently.**

## Minimal working set

The first version intentionally stays small:

- [`templates/PROJECT-PLAN.md`](templates/PROJECT-PLAN.md) — who the project is for, the concrete problem, current approach, SMART success, scope, portability, and current work.
- [`templates/NOW.md`](templates/NOW.md) — the single hot status surface for the next session.
- [`templates/HANDOFF.md`](templates/HANDOFF.md) — what to carry between sessions and when to escalate to a deep handoff.
- [`templates/DECISION.md`](templates/DECISION.md) — only for decisions that would otherwise be expensive to reconstruct.
- [`experiments/`](experiments/) — observations from real work. Templates should grow from repeated use, not imagined future needs.

Git history stores history. Issues store open work. CI stores machine-known execution facts. Do not copy those facts into multiple status documents unless they change a human or AI decision.

## Default numbers

These are defaults, not laws. Change them when real use shows a better value.

| Item | Default |
| --- | --- |
| Live status files | 1 (`NOW.md`) |
| `NOW.md` length | preferably ≤ 1,500 words |
| Active next actions | ≤ 3 |
| Active work streams | ≤ 5 |
| Normal handoff conversation | 10 user/assistant exchanges |
| Light handoff conversation | 5 exchanges |
| Deep handoff conversation | 15–20 exchanges **only as a starting heuristic; structured deep succession may replace this when continuity risk is higher** |
| Earlier context carried manually | ≤ 3 items by default |
| Full project audit on takeover | No, unless the next action requires it |
| New project-management document | Only when an existing surface cannot carry the needed truth |

One exchange means **one user message plus the assistant response**.

## What deserves durable recording

Persist information when losing it would likely cause wrong work or expensive repetition, especially:

- a decision that changes project direction;
- a direction the human explicitly rejected;
- a failed approach that a future session is likely to retry;
- a negative/null result that narrows what should be tried next;
- a current blocker;
- an experimental interpretation fixed before results;
- evidence that changes what should be done next;
- context a future session cannot cheaply recover from Git, issues, or working artifacts.

Normally do **not** create durable records for:

- ordinary discussion;
- brainstorming that did not change a decision;
- every tool call or intermediate step;
- CI run IDs and checksums already available from CI/Git;
- daily activity logs;
- information duplicated elsewhere.

## When AI is part of an experiment

Real ENA work exposed a useful lightweight experiment discipline. It is not required for ordinary projects, but it helps when the AI's first response is itself evidence.

### Isolate the variable structurally

If comparing treatments, keep the common substrate genuinely common and change only the intended variable where practical.

If prior context would contaminate a fresh judgment, remove it from the evaluation surface rather than asking the AI to ignore it.

### Write the interpretation before looking

Before running treatment arms, record:

- what would count as useful success;
- obvious failure shapes;
- what result would weaken the preferred hypothesis;
- what null/tie would mean.

This does not need a giant experiment framework. A short preregistration note is often enough.

### Preserve the first complete output

If the first answer is evidence:

```text
first answer
-> capture
-> then correct / discuss / compare
```

Do not count an answer produced after tutoring as an independent baseline.

### Let null results stay null

If all treatments behave the same, do not rename the tie as a win for the favorite method.

Ask instead whether:

- the treatment was unnecessary;
- the task exposed the answer directly;
- the model's baseline capability saturated the fixture;
- the mechanism claim should narrow.

### Make the mechanism causally necessary

A strong AI can often solve a one-shot problem from the target prompt alone.

If testing memory, inheritance, training, or workflow mechanisms, design the task so the treatment has a genuine opportunity to change behavior rather than merely decorate an already-solvable prompt.

See the real-use observation in `experiments/2026-09-03-ENA-CLEANROOM-AND-SUCCESSION-OBSERVATIONS.md`.

## Temporary workspaces should expire

Branches, cleanrooms, and test repos are working surfaces, not automatic archives.

Before deleting a temporary workspace:

1. check whether it contains unique decision-relevant material;
2. move/archive what actually matters;
3. preserve the evidence/commit/PR needed for lineage;
4. remove the temporary surface.

Do not keep every branch forever out of fear, and do not delete first merely because the list looks untidy.

## How the workbench should evolve

Use it first. Notice repeated pain. Only then add structure.

`USE → REPEAT → PAIN → ABSTRACT`

Avoid the reverse pattern:

`IMAGINE FUTURE PAIN → DESIGN SYSTEM → GOVERN SYSTEM`

A lesson observed once should normally enter `experiments/` or `NOW.md` before it becomes another permanent template.
