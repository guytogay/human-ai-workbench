# NOW

## Project

Human-AI Workbench

## Current goal

Reduce low-value human coordination work while preserving human judgment, fresh-AI isolation, evidence quality and project control.

The immediate real-work pressure is ENA: the human should not have to act as a manual copy/paste message bus between a manager AI and fresh successor/validator sessions.

Candidate relation under exploration:

```text
HUMAN IN THE LOOP
!=
HUMAN AS THE LOOP
```

## Where we are

- The repository still uses a deliberately small working set: README + PROJECT-PLAN + NOW + HANDOFF + optional DECISION + experiments.
- ENA provided the first substantial real-project stress test of the working method.
- Human-AI Workbench is the canonical home for project-general human-AI working method; ENA retains only local occurrences and scientific evidence.
- Three context modes remain explicit: `NORMAL continuation`, `DEEP succession`, and `FRESH independent evaluation`.
- Treatment-exposure integrity is now recorded: `READY` or shallow readback does not prove actual resource inspection.
- A new real workflow problem is active: reduce or eliminate manual human relay between AIs.

## Active automation exploration

Observation / exploration:

`experiments/2026-09-04-HUMAN-AI-AUTOMATION-EXPLORATION.md`

The current ChatGPT task environment was verified to support ordinary OS child processes, but no directly callable local `codex`, `hermes`, `openclaw`, `claude`, `gemini`, or `aider` executable was found.

Therefore:

```text
OS SUBPROCESS AVAILABLE
!=
FRESH INDEPENDENT AI WORKER AVAILABLE
```

The active question is how to obtain the lightest reliable execution surface that can invoke isolated AI workers and exchange staged messages without human transport work.

Candidate surfaces to investigate, in increasing infrastructure cost:

1. local mechanical orchestration for prompts, hashes, sequencing, capture and scoring;
2. API-backed fresh model sessions;
3. installed external Agent runners / CLIs when actually available;
4. GitHub Actions or other isolated runners invoking external models;
5. persistent multi-Agent orchestration only after repeated real use justifies it.

## What should be automated regardless of worker surface

- frozen prompt retrieval rather than retyping;
- prompt/order/hash validation;
- per-run state machines;
- response-format checks;
- first-output capture;
- provenance/run ledgers;
- protocol-deviation classification;
- post-freeze scoring support;
- Git branch/PR packaging;
- temporary workspace cleanup checks.

This keeps separate:

```text
AI EXECUTION AUTOMATION
and
WORKFLOW / EXPERIMENT ORCHESTRATION AUTOMATION
```

## Human role target

Human attention should be spent on:

- purpose and priority;
- consequential choices;
- ambiguity requiring judgment;
- acceptance/rejection of important changes;
- reality contact and values;
- escalation when automation cannot safely decide.

Human attention should not be spent on mechanically relaying already-decided bytes between AIs when a reliable transport can do it.

## Current unknowns

- Which fresh-agent execution surfaces are actually callable from ChatGPT, GitHub or the user's infrastructure?
- Can API-backed sessions provide enough isolation and multi-turn continuity for fresh-successor experiments?
- Can GitHub Actions or another runner invoke them securely and reproducibly?
- What is the cheapest reliable evidence of actual treatment/resource inspection when objective tool traces are unavailable?
- How much infrastructure is justified before automation costs more than the relay work it removes?
- Which parts recur across unrelated projects strongly enough to deserve a reusable template?

## Next consequential action

Inventory and test the actually available execution surfaces, starting with the lowest-infrastructure option that can support one complete manager -> isolated worker -> evidence-capture loop without human copy/paste.

Use the upcoming ENA temporal-assimilation/developmental-order experiment as a real pressure test, but do not let the automation apparatus determine ENA's scientific outcome.

Do not build a persistent multi-Agent framework until a smaller solution has been tried and found insufficient.

## Do not redo / do not overgrow

- Do not turn this repository into ENA.
- Do not absorb ENA theory, Current semantics, or Field Guide HOW.
- Do not equate more Agents with better collaboration.
- Do not automate consequential human judgment merely to maximize autonomy.
- Do not treat OS subprocesses as independent AI workers.
- Do not treat an Agent runner as an independent validator unless context isolation is demonstrated.
- Do not add a universal orchestration template before repeated real use.
- Do not treat `READY` or a shallow readback as proof of treatment exposure.
- Keep following `USE -> REPEAT -> PAIN -> ABSTRACT`.
