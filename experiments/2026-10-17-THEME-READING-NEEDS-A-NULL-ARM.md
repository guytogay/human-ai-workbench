# Reading a Theme From a Batch Needs a Null Arm

Date: 2026-10-17. Source: an independent check of the method note in issue #20 ("putting a dozen
materials in front of an agent and asking it to read a theme has almost no discriminating power"),
run on a different material pool by an agent that had not seen the original materials.

A separate agent reading this file should be able to decide whether the conclusion is worth anything
without trusting the author, so the pool, the draw seeds, the blinding and the limits are all written
down.

## 1. What was checked, and what could not be checked

Issue #20 compared one "real" batch of 14 fragments against two random batches from a private
~240-item pool of daily work material, and found all three equally readable. Its **materials are
private and its group A is gone**, so the A-versus-random contrast cannot be reproduced. What *can* be
reproduced is the half that carries the claim:

> under one extraction rule, an independent random sample of the same pool is just as readable.

Substitute pool: the public issue bodies and issue comments of four related repositories — 776 items,
fetchable by anyone, hash recorded below. Reading was done on four **blinded** surfaces (item text
only: no repository names, no issue numbers, no ids), 14 fragments each, capped at 500 characters.
The interpretation and the failure criteria were written before any sample was looked at, and each
theme was written immediately after reading its own surface, before the key was revealed.

## 2. The decisive arm: a batch with no topic, read as a batch with a topic

The four surfaces were built as three plain random samples plus one **null arm** — 14 single
sentences, one taken from each of 14 different items and then shuffled, so the batch has no
batch-level subject by construction.

Read blind, all four produced a theme with the same ease. The null arm was one of them, and it was not
the weakest one:

| Surface (blind) | Arm | Theme as first written | Theme contained in a single item | Keyword support |
| --- | --- | --- | --- | --- |
| A | random | "disposition accounting: nothing is allowed to stay open" | 0.79 | 8/14 |
| **B** | **null (14 unrelated sentences)** | **"verification closure: claim and artifact reconciled by a measured receipt"** | **0.71** | **7/14** |
| C | random | "declared ≠ actual is found by re-running it" | 0.68 | 5/14 |
| D | random | "every claim needs a pinned, frozen identity" | 0.72 | 6/14 |

The null arm sits in the middle of the range. "Theme contained in a single item" is the largest
fraction of the theme's character bigrams found in any one of that arm's 14 fragments; on that
measure the null arm was also unremarkable. The quantitative proxies are weak on their own — the
blinded read is the evidence, and the numbers are there so a reader can check the author did not pick
a flattering arm.

Two further observations from the same run:

* The four themes are near-variants of one sentence (pairwise bigram Jaccard 0.32–0.39). The "theme"
  is a property of the *corpus*, not of the sample: any 14 items from this pool describe the same
  ongoing work.
* The three-question check from issue #20 rejected all four themes — including the three genuine
  random samples. It protects the record from a non-finding, but it does not give theme-reading
  discriminating power. Keep it as an admission gate; do not read it as a detector.

## 3. What to change

When testing whether an operation "finds something", add a **degenerate arm** — the same operation
applied to material that provably carries no such thing — and read it **blind**, in the same batch as
the real arms. Write the reading down before unblinding.

A null arm cannot tell you what is true. It can tell you that your instrument says "true" about
nothing, which is the cheapest substitute available when the oracle you would need does not exist.
Without it, "I read a theme" and "there was a theme" stay indistinguishable, and the reading is not
evidence of anything.

Corollary for batches of one's own work records: if every arm is drawn from the same corpus, question
2 of the three (does it cross domains?) is answered by construction, not by the reading. A
cross-domain claim needs a pool whose arms *can* differ in domain, chosen before the draw.

## 4. Boundaries of this check

* **The original contrast is not reproduced.** Group A and the private pool are unavailable; all four
  arms here are fresh draws. This checks "random is equally readable", not "the author's A was no
  better than random".
* **The pool is homogeneous**: 770 of 776 items come from two closely related repositories, so
  question 2 (cross-domain) is untestable in this run and should not be cited as evidence either way.
* **The null arm shares the corpus**: its sentences come from the same pool, so register and
  vocabulary are not controlled. A stronger null would take sentences from an unrelated corpus.
* **The judge is an agent of the same class as the original author's**, and knew the hypothesis. Only
  the arm identities were hidden. This tests "can this kind of judge always narrate"; it does not test
  whether a human reader would be fooled.
* n = 4 arms, one pool, one session.

## 5. Re-running it

Pool: issue bodies (≥200 chars) plus issue comments (≥200 chars) of `guytogay/ENA`,
`guytogay/evolution-native-agent-architecture`, `guytogay/human-ai-workbench`,
`guytogay/dsh-addon-kit`, fetched with the forge CLI (`/issues?state=all` and `/issues/comments`,
paginated), sorted by id. 776 items; the exact pool file's SHA-256 is
`7166a34f27c24995c9eaf27c19214b1a368e4993e4bf6f0371e8bf8bc2322d7b`. Note that the pool is a live
surface: re-fetching later gives a different item set and therefore different arms.

Arms: `random.Random(seed).sample(pool, 14)` with seeds 41, 42, 43; the null arm takes from seed 44
fourteen items, keeps from each only one sentence of at least 300 characters, and shuffles the
fourteen sentences. Surface labels are assigned by a separate shuffle (seed 45) and kept in a file
not opened until all readings are written.
