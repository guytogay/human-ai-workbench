# ENA Rapid-Current Progression Pressure Test — 2026-09-06

Status: `REAL_USE_OBSERVATION / PROJECT_METHOD_CANDIDATE / NOT_UNIVERSAL_POLICY`

## Origin

During ENA v0.3.8 work, the maintainer challenged a recurring project pattern: repeated statements that v0.3.7 Current had not been modified were functioning as a sign of process drag, not as a success signal.

The underlying failure was not version immutability itself. It was coupling two different protections:

```text
PRESERVE OLD RELEASE IDENTITY
!=
KEEP THE ACTIVE DEFAULT IMMOBILE
```

ENA's prior release process applied a heavy candidate/freeze/fresh-falsification/reconciliation path broadly, including to adopter-surface repairs that did not alter Constitution IDs or core machine behavior. That made the control cost weakly sensitive to actual change risk.

## Real change

ENA changed release governance to three lanes:

- `R0` — adoption / projection / documentation / tooling / field patch;
- `R1` — decision-material operational behavior change;
- `R2` — core semantic or high-consequence change.

v0.3.8 was classified R0 because it primarily repaired adopter narration, zh-CN hot-surface fidelity, retrieval mapping, fixture coverage and enforcement visibility while preserving the inherited semantic trunk and key machine paths.

After proportional machine/regression gates and rollback preservation, v0.3.8 moved to Current without waiting for unrelated Metamemory research or a generic fresh-cleanroom cycle.

## Candidate general lesson

```text
CONTROL COST SHOULD TRACK CHANGE RISK
```

and:

```text
PROTECT HISTORY
NOT STASIS
```

A protected artifact and a movable active pointer solve different problems.

A reusable project pattern may be:

```text
immutable previous state / rollback anchor
+
small classified successor
+
validation proportional to changed consequence surface
+
fast active-pointer move
+
post-change observation
```

This is different from weakening verification. It asks which verification can still change the decision for this class of change.

## Interaction with existing Workbench lessons

This extends the same family as:

```text
REDUCE COORDINATION BY DESIGN
BEFORE
AUTOMATING COORDINATION
```

The release bottleneck was not solved by automating a long heavy pipeline first. It was reduced by removing gates whose decision value did not match the bounded change.

Related distinction:

```text
AUTOMATED HEAVY PROCESS
!=
NECESSARY HEAVY PROCESS
```

and:

```text
UNRELATED OPEN WORK
!=
BLOCKING DEPENDENCY
```

Parallel research can remain open while a product/default surface moves when the two decisions do not depend on each other.

## Human role

Human judgment remains important for:

- classifying the consequence/risk surface of the change;
- detecting when an apparently small patch actually changes semantics;
- deciding whether rollback is credible;
- escalating R0 -> R1/R2 when evidence warrants it.

Human work should not consist of repeating high-cost release ceremony whose outcome is already determined by a narrower machine/regression check.

## Boundaries / counterexamples

Do **not** use rapid progression to justify:

- silent mutation of an already identified release;
- calling a core semantic change a documentation patch;
- skipping external/adversarial evidence where changed behavior can create material consequence;
- using rollback as an excuse when rollback cannot recover escaped external effects;
- promoting because a calendar or version number demands motion;
- turning every project into fixed R0/R1/R2 labels before real use shows the classification is useful.

The reusable property is proportional validation and movable active state, not ENA's exact lane names.

## What to measure next

Future real projects should record:

- elapsed coordination steps from observed defect to active corrected default;
- number of gates and which actually changed the decision;
- whether rollback was real and usable;
- defects found only after progression;
- false classification: change treated as low-risk that later proved material;
- whether faster progression caused or reduced maintenance debt.

## Current disposition

Keep as a Workbench method candidate with one strong real-use occurrence. Do not yet declare a universal release template.

Follow:

`USE -> REPEAT -> PAIN -> ABSTRACT`
