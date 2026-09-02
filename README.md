# Human-AI Workbench

A practical way to run long-lived projects with AI **without turning project coordination into the project itself**.

This repository is not a constitution, governance framework, or certification system. It is a small set of working habits and templates for humans and AI systems that need to continue real work across sessions, models, and tools.

The workbench should remain **cheaper than the work it helps coordinate**.

## Start here

For an active project, keep one short live status file based on [`templates/NOW.md`](templates/NOW.md).

A new AI session should normally:

1. Read `NOW.md`.
2. Read the recent conversation slice included in the handoff, normally 10 user/assistant exchanges.
3. Open only the files, issues, or artifacts explicitly linked from `NOW.md` or the current task.
4. Be able to answer:
   - What is the current goal?
   - What is already decided?
   - What is still uncertain?
   - What is the next consequential action?
5. If those are clear, **start working**. Do not perform a full project audit by default.

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
- [`templates/HANDOFF.md`](templates/HANDOFF.md) — what to carry between sessions, including concrete conversation defaults.
- [`templates/DECISION.md`](templates/DECISION.md) — only for decisions that would otherwise be expensive to reconstruct.
- [`experiments/`](experiments/) — real tests of the working method. Templates should grow from repeated use, not imagined future needs.

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
| Deep handoff conversation | 15–20 exchanges maximum by default |
| Earlier context carried manually | ≤ 3 items |
| Full project audit on takeover | No, unless the next action requires it |
| New project-management document | Only when an existing surface cannot carry the needed truth |

One exchange means **one user message plus the assistant response**.

## What deserves durable recording

Persist information when losing it would likely cause wrong work or expensive repetition, especially:

- a decision that changes project direction;
- a direction the human explicitly rejected;
- a failed approach that a future session is likely to retry;
- a current blocker;
- evidence that changes what should be done next;
- context a future session cannot cheaply recover from Git, issues, or the working artifacts.

Normally do **not** create durable records for:

- ordinary discussion;
- brainstorming that did not change a decision;
- every tool call or intermediate step;
- CI run IDs and checksums already available from CI/Git;
- daily activity logs;
- information duplicated elsewhere.

## How the workbench should evolve

Use it first. Notice repeated pain. Only then add structure.

`USE → REPEAT → PAIN → ABSTRACT`

Avoid the reverse pattern:

`IMAGINE FUTURE PAIN → DESIGN SYSTEM → GOVERN SYSTEM`
