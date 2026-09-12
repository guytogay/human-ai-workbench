# Verifying the verifier: harness modes, stale fixtures, and auditing a new trust layer

Date: 2026-09-12
Status: `METHOD_RECORD` — transferable practice, stated without relying on any product-specific
concept, artifact or internal state name. Occurrences are cited as evidence, not as the definition.

This continues `2026-09-12-UNPRIMED-ADOPTER-SURFACES-AND-MUTATION-TEETH.md`. That record covered how
to obtain an unprimed evaluation and how to prove a check can fail. This one covers what goes wrong
*inside* the verification work itself, when an independent verifier spends a long session attacking
someone else's implementation.

## 1. A harness needs two modes, and mixes them at its peril

A verification harness gets used for two different jobs that pull in opposite directions:

```text
reproduction mode   the check passes when the DEFECT IS OBSERVED     (evidence tool)
guard mode          the check passes when the DEFECT IS ABSENT       (regression/suite tool)
```

Both are legitimate, and they are inverses of each other. The failure mode is not choosing wrongly —
it is **mixing the two conventions inside one file**. Observed twice in one session: a harness whose
checks were written as "this is the defect" passed a printed gate count that read as reassurance
while half its checks actually asserted the opposite, and a suite entry whose probe reproduced a
defect perfectly reported **PASS** because reproducing a defect was what it was written to do.

Practical rules that came out of it:

- declare the convention in the file header, and make the inversion a single function
  (`if GUARD: record(not observed)`) rather than 20 hand-written negations;
- name every check after the **defect**, not the requirement ("the run rewrites the file", not
  "the run does not rewrite the file") — then guard mode is a mechanical inversion and the printed
  line still reads correctly in reproduction mode;
- keep the two modes in the same artifact and report **both numbers** against the same revision
  (e.g. `7/20 guard, 13/20 reproduction`). Mirror numbers are hard to fake and immediately reveal a
  convention bug;
- if a probe is genuinely only an evidence tool, take it out of the suite. An accepted-but-unclear
  red light is worse than no light.

## 2. The failure you are most likely to report is your own

Across one session, **six** apparent product failures were measurement defects. The catalogue is
worth internalising, because each looked like a finding at the moment it appeared:

| apparent finding | actual cause |
| --- | --- |
| three checks failed on a config file | the probe appended a second top-level key; the parser correctly refused the now-ambiguous file |
| a tool "rejected a valid input" | the probe called it with the wrong interface and read the usage error as a verdict |
| "a status command mutates state" (one variant) | the probe passed a deliberately unusable value and the tool was right to refuse |
| a precondition check failed | the probe compared a parsed scalar to a boolean; the reader returns strings |
| "inconsistent exit codes across runs" | the exit code was read through a shell pipeline instead of directly |
| "the predicate no longer fails closed" | the fixture no longer contained the condition it was named after (see §3) |

Two habits prevent most of these:

- **read the artifact's own message before believing your verdict.** Every one of the six was
  diagnosed by printing the tool's full output instead of only the check's pass/fail line. A verdict
  without the artifact's reason is a hypothesis, not a finding.
- **measure with the raw result.** Shell pipelines, wrappers and formatting layers silently replace
  the value you meant to read.

## 3. Stale fixtures: a check that quietly stops testing anything

The most dangerous of the six, because it produces a *confident* answer in the wrong direction.

A fixture is usually built from the artifact under test (initialise a state, then edit one thing).
When the artifact changes, the fixture can stop containing the condition the check is named after —
and the check then asserts something vacuously. Observed case: a check "the predicate must fail
closed on a contradictory lifecycle entry" was built by taking an artifact-produced state and
changing a value; after the implementation changed, producing that state **correctly cleared** the
related entry, so no contradiction existed and the check silently measured nothing. It reported a
missing feature; the feature was implemented.

Discipline:

- **assert the precondition explicitly, in the fixture.** ("the entry is still present", "the file
  is still unready", "the value differs from the verified one".) If the precondition cannot be
  asserted, the check is not a check.
- when a check flips state, prefer a fixture built *by the tool under test* over one hand-written
  from a template — and re-derive it when that tool's contract changes.
- treat a cluster of "everything refused" as suspicious rather than as hardening: it is usually one
  fixture problem upstream of all of them.

## 4. When the artifact gains a new trust layer, attack the layer first

A repair that introduces a new mechanism (a provenance field, an evidence reference, a signature, a
capability token) creates a fresh surface with **no history of being attacked**. The productive move
is to run the *same* questions that broke the old layer against the new one:

- can empty, placeholder, or nonsensical content satisfy it?
- is the "confidence"/"strength" label validated, or only read?
- are timestamps required to be well-formed *and* to mean something (offset, recency)?
- is the mechanism bound to the thing it claims to be about, or is it a free-floating string that
  can be copied between subjects?
- does an inspection path exist that changes state?

Two disciplines make the result useful rather than noisy:

- **credit what is actually enforced.** In the observed case the new layer did reject empty values,
  wrong strength tokens and offset-less timestamps — reporting that is what makes the rest credible.
- **do not report what the design explicitly allows.** The same layer deliberately accepts
  arbitrary content and delegates honesty to the caller, with the boundary stated in its own docs
  and labels. Re-reporting that as a defect would be a failure to read the design; the honest output
  is a question about how clearly the boundary is *documented*, plus a concrete cheap shape if one
  exists.

## 5. Cross-subject replay is confirmation, not repetition

Re-running the same evaluation with a *different* subject (another model family, another host,
another environment) against the fixed artifact is worth doing for one reason: it can **fail to
reproduce** the old problem in the hands of someone who never saw the report. That negative result
is the confirmation. Two ways to keep it honest:

- sync the evaluated surface to the exact revision, and record that revision in the report;
- ask the evaluator, in its own words, what it could *not* verify. In the observed runs the
  evaluators volunteered their environment's limits and one of them re-downloaded raw bytes before
  trusting its own results — that self-report is what makes the rest usable.

And when the replay surfaces a residual that the design intends, carry the evaluator's own
classification forward with the evidence instead of re-labelling it: "consistent with the documented
self-asserted trust boundary" is a different claim from "the defect is back", and the difference is
the whole value of the exercise.
