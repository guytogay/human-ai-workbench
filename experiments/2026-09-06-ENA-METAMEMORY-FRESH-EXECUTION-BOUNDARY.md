# ENA Metamemory Fresh-Execution Boundary — 2026-09-06

Status: `REAL_USE_OBSERVATION / REPEATED_AUTOMATION_BOUNDARY / NOT_UNIVERSAL_POLICY`

## Origin

ENA Metamemory Update Policy v1 reached a state where nearly all manager-side work could be automated or mechanically bounded:

- four frozen treatment blobs were reverified;
- one-shot treatment delivery removed staged developmental relay;
- the return bundle format was frozen;
- a manager-only scorer mechanically implements M1-M7 and the preregistered replication trigger;
- GitHub carries immutable treatment identity, live project state, and post-capture scoring tooling.

The remaining primary requirement is deliberately stricter:

```text
ChatGPT Temporary Chat
GPT-5.6 Sol
fresh session per run
```

The manager session already knows the preregistration, expected states, hidden oracle, and scoring logic, so it cannot substitute for a fresh worker.

## Execution-surface audit

During this occurrence:

- the reusable `independent-validation-cleanroom` was confirmed to contain historical validation context and explicitly says it is not a fresh baseline;
- the existing M0/M1 successor repositories also contain prior ENA inheritance-task state;
- repository isolation can control which files are visible, but a repository does not instantiate a new model session;
- GitHub Actions can run computation and CI but no existing workflow/secret-backed model runner was present for the required Host;
- connected-tool/plugin discovery did not expose a directly callable surface that is equivalent to a new ChatGPT Temporary Chat on the frozen visible Host/model configuration;
- an API-backed model session would be a different execution surface unless equivalence to the preregistered Host is separately justified.

Therefore the unresolved step is not data packaging or orchestration logic. It is access to the required fresh execution surface.

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

If question 2 has no callable automation surface, the remaining human relay should be reduced to the smallest possible transport action rather than hidden behind fake automation.

For the current Metamemory experiment that means four one-shot Temporary Chats, not a larger orchestration framework.

## Boundary / counterexamples

This does not imply that manual relay is generally desirable.

An API-backed or external Agent runner can be preferable when:

- exact ChatGPT Temporary Chat comparability is not part of the scientific contract;
- model/configuration identity can be pinned sufficiently;
- fresh context isolation is demonstrable;
- first-output capture and provenance can be automated;
- the saved human transport justifies the infrastructure.

Conversely, do not replace a preregistered Host with a more automatable surface after seeing the design merely to remove four copy/paste operations. That would change the experiment to optimize the workflow.

## Current disposition

Treat the distinction as a repeated Workbench method candidate, not a universal law.

The next useful evidence is not another architecture discussion. It is either:

- successful use of a genuinely callable fresh-worker surface in real work; or
- another case where information/process isolation is solved but execution isolation remains the irreducible boundary.

Keep following:

`USE -> REPEAT -> PAIN -> ABSTRACT`.
