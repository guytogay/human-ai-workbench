# ENA Atomic Publish / Readback Pressure Test — 2026-09-06

Status: `REAL_USE_OBSERVATION / PROJECT_METHOD_CANDIDATE / NOT_UNIVERSAL_POLICY`

## Origin

During the ENA v0.3.9 R0 successor, one logical release needed to change many mutually dependent files: Current identity, adopter entrypoints, zh-CN projection identity, a validator, and live project pointers.

Writing these paths sequentially onto the active release branch would have exposed partially coherent intermediate states and multiplied commits whose only purpose was transport.

The working method was instead:

```text
build candidate objects off the active pointer
-> assemble one candidate tree
-> create a commit object without publishing it to the branch
-> read back decision-critical paths by that commit identity
-> attach the verified commit to the release branch
-> open one PR
-> run proportional gates
-> move the active default
```

## Failure caught before publication

During assembly, a group of pre-created zh-CN blobs was initially associated with the wrong paths because generation order had been assumed rather than read back.

The error included a potential mapping where content intended for one semantic surface could have been attached to another path.

Because the candidate tree/commit was not yet attached to the branch, the mistake did **not** become live branch state. Path-to-content readback exposed the mismatch; later tree overlays corrected it before branch publication.

This is the concrete value-bearing occurrence:

```text
OBJECT_CREATED != ACTIVE_STATE_MUTATED
READBACK_BEFORE_ATTACH CAN CATCH ASSEMBLY ERROR
```

## Candidate general lesson

When a change consists of several paths that must become coherent together, and the tool surface supports immutable/staged objects, prefer:

```text
BUILD OFF ACTIVE POINTER
-> READ BACK THE OBJECT YOU WILL PUBLISH
-> ATOMICALLY ATTACH / SWITCH POINTER
```

over sequentially exposing half-complete state.

The useful property is not Git-specific. Equivalent forms can include a staging directory + atomic rename, immutable artifact + pointer swap, database transaction, versioned object + alias update, or deploy candidate + traffic switch.

## Why this is not generic ceremony

This pattern is justified when **intermediate incoherence itself is a real failure mode**.

It is not a reason to stage every one-line documentation edit through an elaborate candidate pipeline.

Use a direct write when:

- only one independent state unit changes;
- partial visibility cannot create a materially false state;
- rollback/readback cost is trivial;
- the active surface already supplies safe transactional semantics.

Use staged atomic publication when:

- multiple files/objects jointly define one state;
- readers can observe intermediate writes;
- cross-file identity must agree;
- a partially updated pointer would mislead users/Agents/automation;
- one immutable candidate can be validated more cheaply than repairing exposed partial state.

## Readback rule

Validation should inspect the **actual object intended for publication**, not merely the inputs used to construct it.

```text
WRITE_REQUEST_ACCEPTED != CORRECT_OBJECT_ASSEMBLED
EXPECTED_MAPPING != OBSERVED_PATH_TO_CONTENT_MAPPING
```

Useful readback targets are the small set of paths/fields that can falsify the publication decision. Do not automatically reread the entire artifact universe.

## Interaction with synchronization debt

The same ENA occurrence exposed another project-general pressure: many cold semantic documents carried a concrete Current version even when their meaning had not changed. Each release then required mechanical version edits across unrelated files.

A candidate companion rule is:

```text
VERSION THE SURFACE THAT NEEDS VERSION IDENTITY
DO NOT VERSION-BIND STABLE COLD CONTENT BY DEFAULT
```

or more generally:

```text
DUPLICATED LIVE STATE -> SYNCHRONIZATION DEBT
```

This does **not** mean removing provenance or versioning where identity matters. It means separating stable content from the small pointer/manifest surface that actually declares active version state.

## Human / Agent division

Agent/tool work is suitable for:

- assembling the candidate object;
- enumerating changed paths;
- mechanical path/content readback;
- running deterministic consistency gates;
- attaching the verified object after criteria are satisfied.

Human judgment remains appropriate for:

- deciding whether intermediate incoherence is consequential;
- defining which fields actually establish identity;
- deciding whether a mismatch changes the release/publication decision;
- classifying whether the change is low-risk or needs stronger independent evidence.

## Boundaries / counterexamples

Do not infer:

- atomic publication makes the content correct;
- internal readback proves external-world behavior;
- an immutable candidate removes the need for semantic/adversarial review when those are decision-material;
- every tool must emulate Git trees;
- every update should wait for a batch just to gain atomicity.

Atomicity protects coherence of the publication transition; it does not prove truth or fitness.

## What to measure next

Across future real project changes, observe:

- whether partial-state exposure would actually have mattered;
- assembly errors caught only by object readback;
- number of mechanical synchronization edits avoided by version-neutral cold surfaces;
- whether staged publication reduces or increases total coordination steps;
- cases where direct writes were cheaper and equally safe;
- whether the candidate/pointer separation itself creates stale candidate clutter.

## Current disposition

Keep as a Workbench method candidate with one strong real-use occurrence.

Do not promote it to a universal transaction template until repeated use shows that the benefit persists outside this ENA release shape.

Follow:

`USE -> REPEAT -> PAIN -> ABSTRACT`
