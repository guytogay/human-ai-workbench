# ENA Atomic Publish / Readback Pressure Test — 2026-09-06

Status: `REAL_USE_OBSERVATION / REPEATED_PROJECT_METHOD_CANDIDATE / NOT_UNIVERSAL_POLICY`

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

## First failure caught before publication — v0.3.9

During assembly, a group of pre-created zh-CN blobs was initially associated with the wrong paths because generation order had been assumed rather than read back.

The error included a potential mapping where content intended for one semantic surface could have been attached to another path.

Because the candidate tree/commit was not yet attached to the branch, the mistake did **not** become live branch state. Path-to-content readback exposed the mismatch; later tree overlays corrected it before branch publication.

This is the concrete value-bearing occurrence:

```text
OBJECT_CREATED != ACTIVE_STATE_MUTATED
READBACK_BEFORE_ATTACH CAN CATCH ASSEMBLY ERROR
```

## Second occurrence — v0.3.10 publication coherence

The next ENA R0 successor supplied a second, different pressure test.

The initial stale-identity census was too narrow: it searched primarily for `v0.3.7 Current`. A branch-local preparation runner was deliberately written with assertions rather than permissive replacement. The first run failed before publication because the designated cold surface still contained other old `v0.3.x Current` labels.

The census was widened and the next construction pass successfully built a 43-file release commit, but GitHub then refused the final push because the Actions token was not permitted to update workflow files.

That failure separated two concerns:

```text
CONTENT CONSTRUCTION SUCCEEDED
!=
PUBLICATION AUTHORITY AVAILABLE
```

Instead of broadening CI permissions, the workflow was narrowed:

- ordinary product files were prepared on the branch;
- the generated validator was staged as ordinary content;
- the normal read-only Main Gate was restored;
- the existing connected GitHub surface, which had the necessary workflow-write capability, installed the validator and removed the staging file.

A later PR diff readback then caught a different class of mistake: mechanical de-versioning had over-normalized genuine historical provenance (`released through v0.3.6 Current`) into a misleading generic `released through Current`. The same readback also found that one release-discipline sentence still named v0.3.8 rather than the real v0.3.9 predecessor, and that the zh-CN entry text described the previous release theme.

Those errors were corrected before merge.

This second occurrence adds two important refinements:

```text
ASSERTION FAILURE BEFORE PUBLICATION IS USEFUL CONTROL
CAPABILITY TO BUILD != AUTHORITY TO PUBLISH
NORMALIZE ACTIVE STATE WITHOUT ERASING PROVENANCE
DIFF READBACK CAN CATCH SEMANTIC OVER-NORMALIZATION
```

The value was not merely atomicity. It was the combination of staged construction, bounded authority, assertions, and readback of the **actual publication candidate**.

## Candidate general lesson

When a change consists of several paths that must become coherent together, and the tool surface supports immutable/staged objects, prefer:

```text
BUILD OFF ACTIVE POINTER
-> ASSERT EXPECTED SHAPE
-> READ BACK THE OBJECT YOU WILL PUBLISH
-> USE THE NARROWEST AVAILABLE PUBLICATION AUTHORITY
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
SCRIPT COMPLETED != SEMANTIC RECONCILIATION COMPLETE
```

Useful readback targets are the small set of paths/fields that can falsify the publication decision. Do not automatically reread the entire artifact universe.

The v0.3.10 occurrence shows that readback should include both:

- structural identity: correct path, version, predecessor, active pointer;
- semantic boundary preservation: active-state normalization must not erase historical provenance or change the meaning of a stable contract.

## Interaction with synchronization debt

The v0.3.9 and v0.3.10 occurrences together exposed a repeated project-general pressure: many cold semantic documents carried a concrete Current version even when their meaning had not changed. Each release then required mechanical version edits across unrelated files, and those duplicated live-state labels drifted independently.

The strengthened candidate rule is:

```text
VERSION THE SURFACE THAT NEEDS VERSION IDENTITY
KEEP STABLE COLD CONTENT VERSION-NEUTRAL BY DEFAULT
PRESERVE HISTORICAL VERSION PROVENANCE WHERE IT IS ACTUALLY HISTORY
```

or more generally:

```text
DUPLICATED LIVE STATE -> SYNCHRONIZATION DEBT
ACTIVE IDENTITY != HISTORICAL PROVENANCE
```

This does **not** mean removing provenance or versioning where identity matters. It means separating stable content from the small pointer/manifest surface that actually declares active version state.

## Publication authority boundary

The v0.3.10 occurrence also supplies a useful counterweight to “automation everywhere”. The preparation runner could construct the release but did not have workflow-write permission. Expanding that token merely to complete the pipeline would have increased authority to remove a one-off transport inconvenience.

The lower-cost response was to use the existing authorized surface for the narrow workflow update.

Candidate principle:

```text
AUTOMATION CONVENIENCE != AUTHORITY JUSTIFICATION
USE THE NARROWEST CAPABILITY THAT CAN COMPLETE THE DECISION
```

Do not generalize this into “never broaden automation permissions”; repeated, justified workload may earn a different design. The point is that authority expansion should pay its own rent.

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
- distinguishing historical provenance from active state;
- classifying whether the change is low-risk or needs stronger independent evidence;
- deciding whether expanded tool authority is justified by repeated value.

## Boundaries / counterexamples

Do not infer:

- atomic publication makes the content correct;
- internal readback proves external-world behavior;
- an immutable candidate removes the need for semantic/adversarial review when those are decision-material;
- every tool must emulate Git trees;
- every update should wait for a batch just to gain atomicity;
- every permission failure should be solved by granting more authority;
- version-neutral cold content means deleting historical release provenance.

Atomicity protects coherence of the publication transition; it does not prove truth or fitness.

## What to measure next

Across future real project changes, observe:

- whether partial-state exposure would actually have mattered;
- assembly errors caught only by object/diff readback;
- assertion failures that prevented an invalid candidate from becoming active;
- number of mechanical synchronization edits avoided by version-neutral cold surfaces;
- cases where provenance was accidentally erased by normalization;
- whether staged publication reduces or increases total coordination steps;
- cases where direct writes were cheaper and equally safe;
- whether the candidate/pointer separation itself creates stale candidate clutter;
- whether narrow publication authority causes repeated friction large enough to justify a different capability boundary.

## Current disposition

Keep as a Workbench method candidate with **two strong real-use ENA occurrences** that failed in different ways before publication.

The repeated evidence is now stronger for:

```text
BUILD OFF ACTIVE POINTER -> READBACK -> ATOMIC ATTACH
DUPLICATED LIVE STATE -> SYNCHRONIZATION DEBT
ACTIVE IDENTITY != HISTORICAL PROVENANCE
```

Do not yet promote this into a universal transaction framework. The next useful evidence should come from another project or a materially different state/publication surface.

Follow:

`USE -> REPEAT -> PAIN -> ABSTRACT`
