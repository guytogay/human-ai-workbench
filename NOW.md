# NOW

## Project

Human-AI Workbench

## Current goal

Reduce low-value human coordination and control ceremony while preserving human judgment, evidence quality, fresh-AI isolation and recoverable project state.

Current candidate relations under real-use testing:

```text
HUMAN IN THE LOOP != HUMAN AS THE LOOP
REDUCE COORDINATION BY DESIGN BEFORE AUTOMATING COORDINATION
CONTROL COST SHOULD TRACK CHANGE RISK
PROTECT HISTORY != PROTECT STASIS
BUILD OFF ACTIVE POINTER -> READBACK -> ATOMIC ATTACH
DUPLICATED LIVE STATE -> SYNCHRONIZATION DEBT
```

## Where we are

- The repository remains deliberately small: README + PROJECT-PLAN + NOW + HANDOFF + optional DECISION + experiments.
- Human-AI Workbench remains the canonical home for project-general collaboration method; ENA retains its theory, release semantics and occurrence evidence.
- Three context modes remain explicit: `NORMAL continuation`, `DEEP succession`, and `FRESH independent evaluation`.
- Treatment-exposure integrity remains explicit: `READY` or shallow readback does not prove actual resource inspection.
- ENA Temporal Assimilation supplied a real pressure test of manual fresh-session relay.
- ENA Metamemory redesigned each primary run to one complete treatment delivery, reducing relay before automating it.
- ENA v0.3.8 supplied a real pressure test of risk-insensitive release governance. Separating immutable history from a movable Current pointer reduced the bottleneck.
- ENA v0.3.9 supplied a real pressure test of multi-file publication coherence: an incorrect blob-to-path assumption was caught by readback before the candidate commit was attached to the release branch, so no half-valid state became live.
- The same v0.3.9 occurrence showed that version-binding stable cold documents creates mechanical synchronization debt; only surfaces whose identity actually depends on the active version should carry that live version state by default.

## Active observations

Automation exploration:

`experiments/2026-09-04-HUMAN-AI-AUTOMATION-EXPLORATION.md`

Completed relay pressure test:

`experiments/2026-09-04-ENA-TEMPORAL-RELAY-PRESSURE-TEST.md`

Rapid-progression pressure test:

`experiments/2026-09-06-ENA-RAPID-CURRENT-PROGRESSION-PRESSURE-TEST.md`

Atomic publish/readback pressure test:

`experiments/2026-09-06-ENA-ATOMIC-PUBLISH-READBACK-PRESSURE-TEST.md`

The current task environment can perform ordinary OS/process/repository automation, but that does not itself create a genuinely fresh independent AI worker.

```text
OS SUBPROCESS AVAILABLE != FRESH INDEPENDENT AI WORKER AVAILABLE
```

## Current methods under test

### 1. Coordination reduction

When coordination pain appears:

1. identify which steps require human judgment;
2. identify which remaining steps are transport/mechanical coordination;
3. ask whether the workflow can remove those steps without changing the phenomenon or decision quality;
4. automate only unavoidable transport;
5. add persistent orchestration only after repeated real use justifies its maintenance cost.

### 2. Proportional progression

When a control/release/review pipeline delays a useful change:

1. preserve an exact previous state or rollback anchor where meaningful;
2. identify the actual changed consequence surface;
3. ask which checks can still change the decision for that change class;
4. do not make unrelated open work a blocking dependency;
5. move the active/default pointer once proportional evidence is sufficient;
6. continue observing reality after the move;
7. escalate the next change when post-move evidence shows the original risk classification was too weak.

The reusable property is **risk-proportional validation**, not ENA's exact R0/R1/R2 vocabulary.

### 3. Staged atomic publication

When several paths jointly define one active state and partial exposure would be misleading:

1. build the candidate off the active pointer;
2. assemble one immutable/staged object where the Host supports it;
3. read back the actual object and the small set of decision-critical path/content mappings;
4. attach or switch the active pointer only after readback passes;
5. use direct writes instead when there is only one independent state unit or partial visibility is harmless.

Prefer stable cold content plus a small live identity pointer over copying the same mutable version/status fact into many files.

```text
OBJECT_CREATED != ACTIVE_STATE_MUTATED
WRITE_REQUEST_ACCEPTED != CORRECT_OBJECT_ASSEMBLED
VERSION THE SURFACE THAT NEEDS VERSION IDENTITY
```

## Human role target

Human attention should be spent on:

- purpose and priority;
- consequential choices;
- ambiguity requiring judgment;
- risk/consequence classification;
- acceptance/rejection of important changes;
- reality contact and values;
- escalation when automation cannot safely decide.

Human attention should not be spent on mechanically relaying bytes, synchronizing duplicate live-state copies, or repeating ceremony whose decision value has disappeared.

## Next consequential actions

1. Use ENA Metamemory Update Policy v1 as the next measurement point for the reduced relay workflow.
2. Observe whether ENA's rapid-Current method continues to work under future R0/R1/R2-like changes or whether risk misclassification creates new maintenance pain.
3. Observe another real multi-object publication before promoting atomic publish/readback from one strong occurrence to a reusable template.

For Metamemory record:

- human transport actions per run;
- whether any human action actually requires judgment;
- treatment-delivery/output-capture errors;
- whether remaining burden justifies an API-backed or external Agent-runner surface.

For progression/publication record:

- gates that actually changed the decision;
- time/steps from defect to corrected active default;
- rollback usability;
- post-progression defects;
- assembly errors caught only by readback;
- synchronization edits avoided by keeping cold content version-neutral;
- cases where direct writes were cheaper and equally safe.

## Current unknowns

- Which fresh-agent execution surfaces are callable and sufficiently isolated when automation becomes justified?
- Can API-backed sessions match experimental Host requirements where Temporary Chat comparability matters?
- What is the cheapest reliable evidence of treatment/resource inspection when objective tool traces are unavailable?
- How many real progression cases are needed before risk-tiered release/progression deserves a reusable template?
- How should a project detect systematic under-classification of change risk without rebuilding the heavy process it removed?
- When does staged atomic publication save more coordination than it adds?
- How much synchronization debt is actually removed by making cold semantic content version-neutral across multiple projects?

## Do not redo / do not overgrow

- Do not turn this repository into ENA.
- Do not absorb ENA theory, Current semantics, or Field Guide HOW.
- Do not equate more Agents with better collaboration.
- Do not automate consequential human judgment merely to maximize autonomy.
- Do not treat OS subprocesses as independent AI workers.
- Do not treat an Agent runner as an independent validator unless context isolation is demonstrated.
- Do not preserve unnecessary workflow stages merely so they can be automated.
- Do not add a universal orchestration, release, or transaction template before repeated real use.
- Do not use "rapid" as permission to hide semantic/high-consequence changes inside low-risk labels.
- Do not use atomic publication as proof that the candidate content itself is correct.
- Keep following `USE -> REPEAT -> PAIN -> ABSTRACT`.
