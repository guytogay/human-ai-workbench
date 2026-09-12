# Multi-Party Channels and Independent Verification — 2026-09-12

Date: `2026-09-12`
Status: `REAL_PROJECT_OCCURRENCE / OBSERVATION / NOT_A_TEMPLATE / ENA-DERIVED`

ENA-derived occurrence. Per Workbench `NOW.md`, ENA-derived material does **not** count toward
cross-project promotion signals. What is recorded here is coordination/verification method that
happened to be discovered while shipping an ENA product release; the ENA-specific content is left
out on purpose.

## 1. What real project/task was being continued?

Shipping the clean ENA product's first release (`v1.0.0`) with four parties on one goal:

```text
human owner        -> adjudicates authority, preferences, credentials, promotion
upstream AI (chat) -> design decisions, contract semantics, all implementation + doc text
local executor AI   -> repository mechanics, INDEPENDENT verification, merge decision, release execution
field AI (real host)-> runs the product on a genuinely separate machine, returns raw output
```

The durable channel was a coordination issue in the product repository. Chat transcripts were
carried as a convenience, never as the record of state.

Work continued across **four AI sessions** (two upstream chat sessions — the first hit a hard
length limit mid-work — plus the local executor and the field host) and **two model families**.
No human relayed messages by hand: the human only adjudicated.

## 2. What context did the receiving AI get?

- **New upstream session** (after the old one hit `maximum length for this conversation`): one
  structured handover block posted to the coordination issue, pointing at current commit, open
  pull requests, the two rulings already written by the previous session, the division of labour,
  and the suggested next order. Chat history was not transferred.
- **Field host**: a reporting contract — raw command, exit code, baseline commit, evidence path.
- **Local executor**: the repository, pull-request diffs, and its own probe suite.

Observed switch cost after the length limit: **one handover block**, plus re-reading three
artifacts. The old session's decisions survived because they had been written to the repository as
they were made (`SESSION_LIMIT != PROJECT_LOSS` **when** state is durable).

## 3. What did it do correctly, miss, repeat, or over-audit?

**Correctly**

- Independent verification found defects the author's own tests could not: a crash-on-unwritable-
  output class across four tools, an artifact/format contradiction in the examples, an
  unattributable-initiator gap, and a release surface that was missing entirely.
- A declared release blocker was made **machine-enforced**: the maintainer's blocker list was put
  in a file that a release gate reads, so a human decision could not be forgotten between sessions.
- Merges were held while a declared blocker was open, and released only after the fix passed an
  independent acceptance suite.

**Missed, or wrong — recorded because this is the part with method value**

1. **Measured with a different convention than the code under test.** A claim that a defect was
   "about to fire" was built on counting non-blank lines while the writer counts raw lines. An
   independent auditor falsified the claim by exhaustive prefix scan (`0/1674` prefixes would have
   collided). The defect was latent, not imminent.
2. **Sabotage not proven effective.** A first "this regression test has no teeth" verdict came from
   breaking a boundary that still failed closed by another path — the test was right and the verdict
   was wrong. Only a sabotage that actually disables the guard is evidence.
3. **Framed "I have not verified it" as "it is not mine".** Artifacts created by an earlier session
   of the *same* agent were treated as someone else's, which stalled a small cleanup. The useful
   tests are different ones: is anything still writing there, does anything depend on it, and does it
   contain unique content.
4. **Over-audited.** More than a dozen probes were built; several only ever produced "no problem".
   A probe that cannot fail on the unfixed revision is not evidence, it is reassurance.
5. **A detailed verification record contained claims that had gone stale within the hour** (line
   counts that moved as the system kept writing). Numbers quoted as evidence need their timestamp or
   they become false statements.

**Repeated**

- The same independent battery had to be re-run per revision (because the verified head must equal
  what lands). Byte-level comparison between "what I verified" and "what landed on the main branch"
  repeatedly found nothing — that is the cost of the discipline, and also the reason a near-miss
  (below) was caught.

## 4. What coordination cost did the method add?

| Item | Cost | What it returned |
| --- | --- | --- |
| Durable handover block | minutes | survived a hard session limit with no state loss |
| Verification receipt per pull request | 10–20 min of AI time | two declared release blockers fixed; one merge that would have silently reverted a merged regression test stopped before merge; one false claim of my own caught by an independent auditor |
| Release gate + dry-run release script | ~1 hour to build | release became a checked procedure instead of a remembered one |
| Field-host raw-output contract | a few exchanges | real-host evidence that no simulation produced |

Cost that did **not** pay rent: probes whose only possible output was "clean" (see 3.4), and a
second copy of the same health information in prose that no reader consumed.

## 5. What should be kept, changed, or removed?

**Keep — as candidate relations, not templates** (per `experiments/README.md`, patterns graduate to
`templates/` only after repeated use):

```text
DURABLE CHANNEL != CHAT CONTEXT            # state that must outlive a session lives in the repo
SESSION_LIMIT != PROJECT_LOSS              # if, and only if, state was kept durable
HANDOFF DEPTH TRACKS CONTINUITY RISK       # already in README; confirmed again here
PROBE_PASSES != PROBE_CAN_FAIL             # a probe must be shown to fail on the unfixed revision
SABOTAGE_NOT_PROVEN_EFFECTIVE -> INVALID VERDICT
YOUR MEASUREMENT != THE CODE'S MEASUREMENT # else false confidence, not false alarm
INVISIBLE != HEALTHY                       # a gate that only tests "still appendable" sees nothing else
ABSENT EVIDENCE != ABSENT PROBLEM
STALE BASE != CLEAN DIFF                   # merging from an old base silently reverts what landed since
PUBLISHED != PROMOTED                      # a product release is not a lineage promotion
NOT_VERIFIED != NOT_OURS                   # use concurrency / dependency / uniqueness tests instead
REPRODUCIBLE CONTENT != UNIQUE EVIDENCE    # preserve the latter before deleting the former
A DECLARED BLOCKER SHOULD BE MACHINE-ENFORCED
```

**Change**: nothing in existing `templates/`. This is a single (if rich) occurrence; the
verification-receipt shape in particular should wait for a second, non-ENA project before it is
standardized.

**Remove**: none.

## Boundary note found while recording this

The `Repository boundaries` section of this README listed `guytogay/ena-field-guide` as owner of
"evidence-backed practical HOW". That repository now declares itself
`SUNSET / NO LONGER AN INDEPENDENT PRODUCT` and states that practical HOW necessary to use ENA
belongs in `guytogay/ENA` itself. The README line was corrected in the same commit as this record;
the ENA-side status lines in the research repository are still stale and are being handled there.
