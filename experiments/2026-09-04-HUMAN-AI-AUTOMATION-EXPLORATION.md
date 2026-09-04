# Human-AI Collaboration Automation Exploration

Date: `2026-09-04`

Status: `REAL_WORKFLOW_PROBLEM / ACTIVE_EXPLORATION / NOT_A_UNIVERSAL_TEMPLATE`

## 1. Why this exploration exists

A real ENA mechanism experiment required the human project owner to open fresh ChatGPT sessions and repeatedly copy prompts and outputs between the project-manager session and independent successor sessions.

That preserved experimental independence, but the human was doing low-value transport work:

```text
manager AI
-> human copy/paste
-> fresh AI
-> human copy/paste
-> manager AI
```

The human correctly identified this as poor Human-AI collaboration design.

The problem is not merely inconvenience. Manual relay:

- consumes human attention without using human judgment;
- creates transcription / prompt-drift risk;
- limits experiment scale;
- makes long-running multi-Agent work tiring;
- turns the human into infrastructure instead of a decision-maker;
- can contaminate experiments when exact frozen prompts are relayed manually.

The Workbench should therefore treat **removing low-value human message-bus work** as an important automation target.

## 2. Desired collaboration shape

Human attention should concentrate on:

- purpose and priorities;
- consequential choices;
- ambiguity that requires human judgment;
- acceptance/rejection of important changes;
- reality contact and values;
- escalation when automation cannot safely decide.

Mechanical coordination should move toward:

```text
human intent / approval
        ↓
manager AI / orchestrator
        ↓
automated task packaging + routing
        ↓
fresh/isolated AI workers where required
        ↓
automated evidence capture + provenance
        ↓
manager synthesis / adjudication
        ↓
human only where judgment matters
```

Candidate principle:

```text
HUMAN IN THE LOOP
!=
HUMAN AS THE LOOP
```

This is a Workbench hypothesis/principle candidate, not yet a universal rule.

## 3. Current verified execution capability

In the current ChatGPT task environment on 2026-09-04:

- ordinary OS child processes can be spawned successfully;
- multiple child processes can run independently at the operating-system level;
- no directly callable local executable was found for `codex`, `hermes`, `openclaw`, `claude`, `gemini`, or `aider`.

Therefore:

```text
OS SUBPROCESS AVAILABLE
!=
FRESH INDEPENDENT AI WORKER AVAILABLE
```

OS subprocesses can automate computation, packaging, validation, hashing, scoring, file operations and local orchestration, but they do not by themselves create an independent model session.

## 4. Primary exploration question

> What is the cheapest reliable way for a Human-AI project manager to spawn or invoke isolated AI workers, exchange staged messages with them, capture first outputs and provenance, and return results without requiring the human to manually relay messages?

The answer may differ by environment. The goal is not one universal Agent framework; it is a reusable decision model for choosing the lightest automation surface that preserves the required independence and control.

## 5. Capability ladder to investigate

Investigate from the least infrastructural burden upward.

### Level 0 — manual relay

Human opens sessions and copies messages.

Use only when no automation surface exists or when human review itself is the intended gate.

This is the current baseline and should not be normalized as the desired workflow.

### Level 1 — local mechanical orchestration

Use OS subprocesses/scripts to automate:

- exact prompt retrieval from frozen files;
- prompt hashing / fixture verification;
- sequencing rules;
- output parsing;
- evidence archival;
- scoring/adjudication support;
- Git branch/PR packaging.

This reduces errors but still needs an external AI execution surface.

### Level 2 — API-backed fresh model sessions

Investigate whether a model API can provide:

- independently initialized conversations;
- explicit model/reasoning configuration where needed;
- deterministic treatment delivery boundaries;
- multi-turn session continuity;
- raw response capture;
- no hidden exposure to manager context;
- acceptable cost and rate limits.

This is likely the simplest path when API access is available and experimental comparability to the desired model surface is acceptable.

### Level 3 — external Agent runner / CLI

Investigate available runners such as Codex, Hermes, OpenClaw or equivalent when installed/authorized.

Important distinction:

```text
AGENT RUNNER AVAILABLE
!=
INDEPENDENT VALIDATOR GUARANTEED
```

The runner must support actual context isolation and must not silently inherit manager state, workspace contamination or answer surfaces.

### Level 4 — CI / GitHub Actions execution

For reproducible experiments or repo-native work, investigate Actions/external runners that can:

- instantiate isolated workspaces;
- inject only treatment-specific material;
- invoke external model APIs/agents;
- archive outputs as artifacts or commits;
- verify hashes and frozen fixtures;
- parallelize replicates.

This adds infrastructure and secrets-management cost, so it should be used only when the reproducibility/scale benefit pays for itself.

### Level 5 — persistent multi-Agent orchestration

Only if repeated real work justifies it, consider a persistent router/orchestrator with:

- role isolation;
- worker lifecycle management;
- message routing;
- evidence/provenance logging;
- permission boundaries;
- retry/timeout semantics;
- human escalation points.

Do not build this layer merely because it is architecturally attractive.

## 6. Requirements for a useful automation surface

A candidate surface should be evaluated on at least these dimensions:

### Independence

Can a worker genuinely start without unintended manager/project context?

### Exact treatment delivery

Can the orchestrator prove which bytes/messages the worker was intended to receive?

### Exposure verification

Can actual resource/treatment inspection be evidenced without semantically rehearsing the treatment?

### Multi-turn continuity

Can one worker remain the same successor across developmental stages without mixing with another run?

### First-output preservation

Can the first complete answer be frozen before correction/tutoring?

### Provenance

Can outputs be linked to run identity, treatment identity, model/configuration and sequence?

### Human intervention cost

How many human actions are required per run, and do those actions require judgment or merely transport?

### Mechanical reliability

Can prompt drift, wrong-order delivery, missed steps and transcription errors be prevented by machine checks?

### Cost / availability

Does automation cost more money/infrastructure than the human effort it removes?

### Security and secrets

What credentials, APIs, repository permissions and external data exposure are required?

## 7. Immediate ENA use case

ENA's next planned mechanism experiment is temporal assimilation / developmental order.

Unlike the prior static-carrier experiment, it may require several staged developmental interactions per fresh successor before a transfer battery. A manual design could easily require dozens of human copy/paste operations.

Therefore this is a good real-work pressure test for Workbench automation.

Target outcome before ENA launches the next large replicated experiment:

> Find a workflow that materially reduces human relay operations while preserving fresh-successor isolation, staged interaction, first-output capture and experiment integrity.

This exploration must not dictate ENA's scientific result. It only improves the execution apparatus.

## 8. Automation opportunities even before fresh-agent spawning is solved

The following should be automated independently of the final worker surface:

- frozen prompt retrieval from repo artifacts instead of retyping;
- prompt/order/hash validation before delivery;
- per-run state machine (`INIT -> STAGE_1 -> ... -> FROZEN`);
- response-format validation;
- exact raw-output preservation;
- protocol-deviation classification;
- run ledger generation;
- primary score calculation from frozen oracle after unblinding;
- branch/PR preparation;
- cleanup/retirement checks for temporary surfaces.

This separates two problems:

```text
AI EXECUTION AUTOMATION
and
EXPERIMENT / WORKFLOW ORCHESTRATION AUTOMATION
```

The second can advance even when the first is constrained.

## 9. Failure modes to prevent

Automation is not automatically better. Specifically guard against:

- hidden shared context between supposedly fresh workers;
- accidental oracle exposure;
- automatic retries that erase first-output evidence;
- orchestrator paraphrasing frozen prompts;
- silent prompt/order drift;
- worker reuse across independent replicates;
- API/provider behavior that changes model identity or configuration unexpectedly;
- a complex orchestration framework whose maintenance costs exceed the saved human work;
- replacing meaningful human judgment with automation merely to maximize autonomy.

## 10. Success criterion

This exploration succeeds when real work demonstrates a workflow where:

```text
human transport actions -> near zero
human judgment remains available where consequential
fresh-worker boundaries remain credible
machine-verifiable sequencing/evidence improves
coordination cost decreases rather than moves elsewhere
```

A useful metric is not "number of Agents". It is **human judgment leverage per unit of coordination effort**.

## 11. Near-term investigation sequence

1. inventory execution surfaces actually callable from ChatGPT/connected tools and from the user's own infrastructure;
2. investigate API-backed fresh-session feasibility and cost;
3. investigate whether GitHub Actions or another runner can securely invoke those sessions;
4. investigate Codex/Hermes/OpenClaw only where they are actually available rather than assumed;
5. prototype the smallest end-to-end relay-free run with one manager, one isolated worker and frozen evidence capture;
6. only then test multi-worker replication/parallelism;
7. feed observed friction back into Workbench before creating a reusable template.

## 12. Repository boundary

This file belongs in Human-AI Workbench because the problem is general collaboration method:

> how humans and AI should divide coordination, execution and judgment work.

ENA should record only that its next experiment is temporarily waiting at the execution-design boundary and link back to this exploration. ENA natural-law research should not absorb the orchestration framework itself.

## 13. Current stance

Do not assume full autonomous multi-Agent orchestration is the goal.

The goal is narrower and more practical:

> remove mechanical human relay wherever doing so preserves or improves control, evidence quality and project progress.

Keep following:

`USE -> REPEAT -> PAIN -> ABSTRACT`.
