# Scope Drift to Null Result: a simple seed became a framework, then the framework's own claims were questioned

Date: `2026-09-06`
Status: `REAL_PROJECT_OCCURRENCE / OBSERVATION / NOT_A_TEMPLATE / ENA-DERIVED`

Per Workbench `NOW.md` next-action #1 (stop using ENA as the sole source of method evidence):
this is an ENA-derived occurrence and therefore does **not** count toward cross-project promotion
signals. It is recorded as a repeated instance of discipline already described in the README
(scope re-check before machinery; interpretation before looking; preserve first output; null
results stay null), because repetition is what the Workbench tracks.

## 1. The occurrence: simple seed -> expanded research project

The project owner described the original seed as two simple needs:

> remind a newly installed agent to back up before self-modifying because agents had repeatedly
> edited themselves into a dead state; and keep the agent flexible/open-minded while working.

Through iterative work with ChatGPT, that seed grew into ENA: Constitution, capability maps,
schemas, validators, release discipline and a research program. The owner later reported:

> "等我把这些简单的需求告诉chatgpt，它弄出来了个ena，洋洋洒洒这么多，我也骑虎难下。"

This does **not** establish that one assistant, in one turn/session, unilaterally created the whole
current project. It establishes something narrower and more useful: the owner experienced a large
gap between the simplicity of the original practical need and the machinery accumulated around
it.

Three pressure signals converged:

```text
SIMPLE HUMAN NEED -> LARGE AI-MEDIATED PROJECT
PROJECT VALUE CAN BE REAL -> OWNER CAN STILL FEEL CAPTURED BY ITS MACHINERY
MACHINERY CAN BECOME SELF-MAINTAINING -> RECHECK WHETHER IT STILL PAYS RENT
```

The recovery was a human-AI audit sequence, not autonomous Agent enlightenment:

1. **Human discomfort became a trigger.** The owner said the project felt "骑虎难下" instead of
   treating that feeling as noise.
2. **The owner interrogated the framework.** He asked whether an Agent should fully obey ENA and
   whether the lease loop was actually useful. The Agent answered that proportionality matters and
   that authorization is not recoverability.
3. **The owner then asked the missing operational question explicitly:** whether ENA lacked support
   for helping the Agent itself evolve. That question caused the DSH Agent to inspect its own LXC
   Host rather than continue discussing ENA abstractly.
4. **The Agent found a Host gap and proposed concrete organs:** rescue snapshot/canary, a durable
   variation/idea ledger, and a lightweight before/after baseline. The owner authorized the build;
   the Agent implemented and drilled them.

The important causal lesson is therefore not "the Agent naturally operationalized ENA". It is:

```text
HUMAN DISCOMFORT
-> VALUE / SCOPE AUDIT
-> HUMAN ASKS FOR THE MISSING OPERATIONAL LAYER
-> AGENT INSPECTS REAL HOST
-> AGENT PROPOSES SMALL ORGANS
-> HUMAN AUTHORIZES IMPLEMENTATION
-> REALITY CONTACT
```

This is consistent with `HUMAN IN THE LOOP != HUMAN AS THE LOOP`: the human did not design the
scripts line-by-line, but the human intervention was decision-material in getting from framework
interpretation to Host operationalization.

## 2. The occurrence: measuring the framework's own claim

ENA's own open question was whether its default-resident kernel adds measurable fresh-session
salience. A 3-arm observation was run (kernel resident / same-host control / ENA-neutral control),
with a pre-written rubric and preserved transcripts.

The maintainer reconciliation narrowed the contributor's headline correctly:

1. one control run self-read the treatment file, so it ceased to be an untreated comparator;
2. the two same-host arms shared an ENA-derived global baseline, so they could not estimate a true
   ENA-vs-no-ENA margin;
3. the frozen rubric defined a treat-vs-control comparison while the report emphasized the neutral
   arm, and T2 checkpoint mapping changed post hoc.

The durable lesson is:

```text
PREREGISTER THE COMPARISON THE REPORT WILL USE, OR SAY WHICH ONE CHANGED
STRUCTURAL ISOLATION CAN FAIL EVEN WITH HONEST INTENT
NULL / NON-DISCRIMINATING RESULT -> DO NOT RENAME IT AS A WIN
PRESERVE FIRST OUTPUTS + ORIGINAL RUBRIC -> LATER INTERPRETATION CAN BE SEPARATED FROM OCCURRENCE TRUTH
```

The maintainer disposition (`ACCEPT_AS_FIELD_EVIDENCE_WITH_NARROWING /
FIELD_UNRESOLVED_FOR_DURABLE_CLAIM / NO_NEW_PRIMARY`) is itself the pattern: evidence discipline
protects corrigibility, not a favorite hypothesis.

## 3. What this occurrence adds

- **Scope drift is recoverable mid-flight.** Recovery did not require abandoning ENA; it required
  separating research value from the original personal operating need and rechecking what still
  earns its cost.
- **Human discomfort can be decision-material evidence about process fit.** "骑虎难下" triggered a
  useful audit. It does not prove the framework was worthless; it proved that ownership and scope
  needed re-examination.
- **Semantic understanding did not naturally trigger Host operationalization.** The Agent became
  concrete only after the owner explicitly asked whether ENA lacked self-evolution support. This is
  a Human-AI workflow finding, not proof that every Agent needs the same three tools.
- **The human can set the problem while the Agent proposes the organ.** The owner did not specify
  rescue/ledger/baseline implementations in detail; the Agent proposed them after inspecting the
  Host, then implemented them after authorization.

A candidate audit sequence, still **NOT_A_TEMPLATE**, is:

```text
1. Restate the original need in one paragraph.
2. Ask which accumulated machinery is still load-bearing and what it costs.
3. Ask explicitly whether the current system lacks a practical/operational layer.
4. Inspect the real Host before proposing new machinery.
5. Prefer the smallest measurable organ that can change the real outcome.
```

## 4. Boundary

This remains one ENA-derived project occurrence. It does not count toward cross-project promotion
signals and does not establish a universal scope-drift template. Promotion requires recurrence in
non-ENA work with different humans/Agents/projects.

The self-maintenance implementation is also owner-directed dogfood: the owner's question triggered
the Host audit and the owner authorized installation. It is not evidence that semantic adoption
alone causes an Agent to grow the right local organs.

## Files

- `experiments/2026-09-06-SCOPE-DRIFT-AND-NULL-RESULT-DISCIPLINE.md` (this file)
- Related upstream: `guytogay/evolution-native-agent-architecture` — `research/field-validation/2026-09-06-ena-v0312-kernel-salience-dsh-lxc*`
- Related downstream: `guytogay/ena-field-guide` — `entries/2026-09-06-agent-self-maintenance-kit.md`
