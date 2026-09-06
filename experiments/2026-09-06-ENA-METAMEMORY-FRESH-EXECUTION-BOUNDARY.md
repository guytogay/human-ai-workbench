# ENA Metamemory Fresh-Execution Boundary — 2026-09-06

Status: `REAL_USE_OBSERVATION / REPEATED_AUTOMATION_BOUNDARY / COMPLETED_OCCURRENCE / NOT_UNIVERSAL_POLICY`

## Origin

ENA Metamemory Update Policy v1 reached a state where nearly all manager-side work could be automated or mechanically bounded:

- four frozen treatment blobs were reverified;
- one-shot treatment delivery removed staged developmental relay;
- the return bundle format was frozen;
- a manager-only scorer mechanically implements M1-M7 and the preregistered replication trigger;
- GitHub carries immutable treatment identity, live project state, and post-capture scoring tooling.

The remaining primary requirement was deliberately stricter:

```text
ChatGPT Temporary Chat
GPT-5.6 Sol
fresh session per run
```

The manager session already knew the preregistration, expected states, hidden oracle, and scoring logic, so it could not substitute for a fresh worker.

## Execution-surface audit

During this occurrence:

- the reusable `independent-validation-cleanroom` was confirmed to contain historical validation context and explicitly says it is not a fresh baseline;
- the existing M0/M1 successor repositories also contain prior ENA inheritance-task state;
- repository isolation can control which files are visible, but a repository does not instantiate a new model session;
- GitHub Actions can run computation and CI but no existing workflow/secret-backed model runner was present for the required Host;
- connected-tool/plugin discovery did not expose a directly callable surface equivalent to a new ChatGPT Temporary Chat on the frozen visible Host/model configuration;
- an API-backed model session would be a different execution surface unless equivalence to the preregistered Host were separately justified.

Therefore the unresolved step was not data packaging or orchestration logic. It was access to the required fresh execution surface.

## Completed occurrence

The residual human transport was then performed exactly at that boundary:

- four independent Temporary Chats were created;
- one frozen one-shot treatment was pasted into each fresh chat;
- only the first complete response from each run was retained;
- four raw outputs were returned to the contaminated manager session;
- no follow-up tutoring, selective retry, or result-specific replacement was used;
- all four outputs were machine-parseable and protocol-compatible;
- the frozen replication trigger did not fire, so no second wave was launched.

The important observation is that human work was reduced to **fresh-context instantiation and byte transport**. Scoring, replication logic, state reconstruction and adjudication mechanics remained manager-side and deterministic.

No evidence from this occurrence justified building a persistent external Agent runner merely to remove those four launches and four output returns.

```text
HUMAN RELAY REMAINED
BUT
HUMAN JUDGMENT WAS NOT REQUIRED FOR THE RELAY ITSELF
```

This is a useful distinction for future workflow economics: a residual manual step can be real but still too small or too Host-specific to justify infrastructure.

## Repeated candidate distinction

This reinforces the earlier Workbench observation:

```text
OS SUBPROCESS AVAILABLE != FRESH INDEPENDENT AI WORKER AVAILABLE
```

with a sharper decomposition:

```text
INFORMATION ISOLATION
!=
EXECUTION ISOLATION

ORCHESTRATION AUTOMATION
!=
FRESH EXECUTION SURFACE
```

A clean repository, exact prompt bytes, a scorer, a state machine, and CI can all be correct while the workflow still lacks a way to create the required independent model context.

## Practical implication

When fresh-worker independence is decision-material, split the workflow into two independent questions:

1. **Can treatment, sequencing, capture, provenance and scoring be automated?**
2. **Can the required model execution context actually be instantiated without inheriting manager context?**

Do not treat success on question 1 as evidence for question 2.

If question 2 has no callable automation surface, reduce the remaining human relay to the smallest possible transport action rather than hiding it behind fake automation.

The Metamemory occurrence supports a bounded working pattern:

```text
AUTOMATE THE MANAGER-SIDE MECHANICS
KEEP FRESH-CONTEXT CREATION EXPLICIT
DO NOT BUILD INFRASTRUCTURE UNTIL REPEATED LOAD EARNS IT
```

## Boundary / counterexamples

This does not imply that manual relay is generally desirable.

An API-backed or external Agent runner can be preferable when:

- exact ChatGPT Temporary Chat comparability is not part of the scientific contract;
- model/configuration identity can be pinned sufficiently;
- fresh context isolation is demonstrable;
- first-output capture and provenance can be automated;
- repeated workload makes the saved human transport worth the infrastructure.

Conversely, do not replace a preregistered Host with a more automatable surface after seeing the design merely to remove a handful of copy/paste operations. That would change the experiment to optimize the workflow.

## Current disposition

Treat the distinction as a repeated Workbench method candidate, not a universal law.

This occurrence now supplies the full cycle:

```text
ISOLATION DESIGNED
-> MANAGER MECHANICS AUTOMATED
-> FRESH EXECUTION REMAINED MANUAL
-> FOUR RUNS COMPLETED
-> NO REPLICATION
-> NO RUNNER INFRASTRUCTURE EARNED
```

The next useful evidence is either:

- successful use of a genuinely callable fresh-worker surface in repeated real work; or
- another case where information/process isolation is solved but execution isolation remains the irreducible boundary and the residual manual burden becomes materially larger.

Keep following:

`USE -> REPEAT -> PAIN -> ABSTRACT`.
