# Closing honestly: landed artifacts, failing gates, and expiring workspaces

Date: 2026-09-13
Status: `METHOD_RECORD` — transferable practice, stated without relying on any product-specific
concept, artifact or internal state name. Occurrences are cited as evidence, not as the definition.

This continues `2026-09-12-VERIFYING-THE-VERIFIER.md` and
`2026-09-12-UNPRIMED-ADOPTER-SURFACES-AND-MUTATION-TEETH.md`. Those covered how to obtain an
independent evaluation and how to attack your own checks. This one covers the end of a work cycle:
the three moments where a team believes something is finished — a decision was accepted, a
workspace was cleaned up, a verification was promoted — and the artifact disagrees.

The common shape:

```text
A STATEMENT IS NOT A STATE.
Ask the artifact what happened. If the artifact cannot answer, the state is UNKNOWN,
and UNKNOWN must never be rendered as PASS / DONE / CLEAN.
```

## 1. An accepted decision is not a landed change

A decision recorded in a coordination channel — a ruling, a disposition, a "yes, do that" — feels
like work that has happened. It has not. It has happened when an artifact carries it.

Observed occurrence: a maintainer disposition to promote a narrow consistency check into the
product's CI was accepted and posted in the morning. Ten hours later, nothing in the product tree
implemented it, no CI step ran it, and no issue tracked it. Everyone had moved on; every later
summary inherited the belief that the item was handled. Two independent searches were needed to
falsify it: one for the check in the tree, one for it in the CI definition.

Disciplines:

- **Give every accepted decision a landing site at the moment it is accepted** — a file, a
  commit, a CI step, or an explicit owner and date. A decision with no landing site is a wish.
- **Audit closure by artifact, not by memory.** For each item believed finished, name the artifact
  that would have to exist. "There is a ruling" is not an artifact; "the test exists and CI runs
  it" is.
- **Do not treat your own summary as evidence.** Summaries are the most likely place for an
  unlanded decision to become permanent, because later readers stop looking.
- When you find one, **execute it rather than re-deciding it**, then report the artifact. The
  disposition was already adjudicated; a second round of discussion is pure loss.

## 2. A gate whose command failed has not passed

A cleanup or validation gate usually reads as "the check produced no complaint, therefore clear".
That inference is only valid if the command actually ran and its output means what you think.

Two occurrences, one session, both inside the *verifier's* own tooling:

| what the gate did | what was read | what was true |
| --- | --- | --- |
| ran a version-control query in a directory that was not a repository | empty output → "no unique commits" | the command exited 128 and printed a fatal error; it never examined anything |
| fetched a stored object through an API using a default ref | not found → "the content is missing" | the request pointed at the wrong ref; the object was present all along |

The second case is the more dangerous shape, because "not found" is a *plausible* result: it agrees
with the hypothesis the gate was testing. The first is caught by reading the exit code, the second
only by reading the request.

Disciplines:

- **Read exit status and error text before interpreting output.** Non-zero plus empty stdout is not
  "empty"; it is "did not run".
- **A command that could not run leaves the gate UNKNOWN**, and UNKNOWN blocks the action it guards
  — it does not authorize it.
- **Prefer a structural proof to a spot check.** Where a spot check asked "is this one object
  reachable?", the replacement asked "does the whole tree hash match?" — one value, no sampling, and
  no interpretation. A stronger proof often costs fewer steps than defending a weaker one.
- When a human realizes mid-gate that *their instruction* was the defective part, say so and
  substitute the stronger evidence explicitly. Silently working around a bad gate is how the next
  run inherits it.

## 3. Expiring a workspace: prove the negative before deleting

Temporary workspaces — clones, scratch trees, cleanrooms, branches — should expire. The cheap
failure is keeping everything forever; the expensive failure is deleting the one copy of something
that exists nowhere else.

Observed occurrence: an authorized cleanup of a batch of scratch directories was gated by one
question per repository copy — "does anything here exist only here?". One copy held a commit that
was genuinely unreachable from the remote: the same-named remote branch had been rewritten and was
missing an entire subdirectory, plus a script the local version had. Deleting on the tidy-looking
list would have destroyed it silently and permanently.

The gate that worked, in order:

1. **List what would be deleted**, with size and modification time — and treat anything whose
   ownership is unclear as a stop-and-report item, not a judgement call.
2. **Ask the negative question structurally**: which commits/objects/files here are not reachable
   from the remote? Beware the two lies from §2 while asking it.
3. **Preserve first, verify the preservation byte-for-byte, then delete.** The preservation was
   pushed as a new descriptive branch, and the proof was whole-tree hash equality plus per-object
   equality — not "the push command returned 0".
4. **Only then remove the local copy**, and re-check the boundary objects (services, existing
   scheduled jobs, protected directories) afterwards rather than before.

A useful asymmetry: pushing a new branch is cheap and reversible, deleting a workspace is neither.
When the two options are "publish an unwanted branch" and "lose an unrecoverable commit", publish.

## 4. The reporting layer must not be the failure surface

A suite that runs forty probes, all of them fine, and then dies while printing its summary has not
found a defect. It has a reporting defect — but the operator sees a failure, and the cheapest wrong
conclusion available is "the thing I was testing is broken".

Observed occurrence: a runner crashed after every probe had completed, because one probe's summary
contained a character the console encoding could not represent. The verdict table never printed.

Disciplines:

- **Separate execution from reporting.** Collect results, then render; make the renderer unable to
  fail on data (widen the encoding, replace unrepresentable characters) rather than trusting the
  data to stay printable.
- **Keep machine-readable output available**, so a human-facing table is never the only path to the
  result.
- When a red signal appears, **read the artifact's own message before believing the verdict** — the
  same rule as in `2026-09-12-VERIFYING-THE-VERIFIER.md`, applied to your own tooling.
- Prefer ASCII in generated summaries unless a specific reader needs otherwise. Portability of the
  report is part of the report.

## 5. A check against false positives needs its own sample tested in both directions

Adding a guard whose purpose is to *avoid* flagging something is a real and valuable move — for
example, "a bare name in backticks is not a path; only an explicit path is a path". Such a guard is
itself code, and it is usually tested only with the case it is meant to reject.

Observed occurrence: the lock-in assertion written to prove that restraint was wrong on first run —
its own sample text contained the explicit path form, which *should* be resolved. The assertion was
correct about the rule and incorrect about its fixture.

Disciplines:

- Test the negative guard in **both** directions in the same check: the bare form must not be read,
  and the explicit form must be read. A guard half-tested is a future over-correction.
- Keep the guard's rationale in the code next to the assertion, so a later maintainer "fixing" the
  restraint has to argue with the reason rather than with a silent `assertEqual`.

## 6. Promote narrowly; keep the external verifier independent

When an external audit finds that an area is worth guarding continuously, the tempting move is to
import the audit. Do not. Extract instead.

The shape that worked:

```text
external oracle (broad, heuristic, owned by the verifier)
  -> identify the small stable contract worth guarding forever
  -> implement that contract as a narrow product-side regression, in the product's idiom
  -> run it where the product's tests run
  -> LEAVE the oracle external and broader than the promoted check
```

Reasons the two must stay different artifacts: the oracle is allowed to be speculative and to
change weekly; the promoted check must be stable enough that a red build means something. If the
broad version lives in the product, its heuristics become product policy by accident, and its
independence — the property that made its findings worth reading — is gone.

Two implementation notes from doing it:

- **Say what the promoted check does not do.** Its non-goals (it does not execute side-effecting
  examples; it does not re-implement the interface it verifies; it deliberately excludes historical
  documents) belong in its header, because those exclusions are exactly what a later reader will
  try to "improve".
- **Prove the promotion landed** per §1: the file exists, CI runs it on every required platform, and
  the job log shows the new tests executing rather than merely a green check.

## 7. Closure is an artifact

Across all six: the honest end of a cycle is a *pointer to something that exists*, not a sentence
saying it is over.

```text
decision accepted        -> the change landed, and its check runs
gate reported clean      -> the gate's command ran, and its output means what you read
workspace removed        -> the unique content is provably reachable elsewhere
suite reported green     -> the suite executed and its reporting did not fail
a guard was added        -> the guard was tested on both the rejected and the accepted case
a check was promoted     -> the product runs it, and the oracle stayed independent
```

The single habit that produces all of them: when someone says "done", ask **which artifact would
have to exist for that to be true**, then go look at it.

## 8. A message you never read is not a message you sent

Sending feels like a terminal action: the text is out, the channel shows it, something else can have
your attention. So an agent that works in turns will send a question to a peer or a human, end its
turn, and never look at the answer. From the sender's side nothing is missing. From the other side the
collaboration has quietly become a **broadcast**, and the human ends up saying the sentence nobody
should have to say: *you sent it, so read the reply.*

Observed occurrence: several exchanges in one long session where each outgoing message was written and
dispatched, and the answer — including a substantive ruling that changed what should happen next —
was only read after the human pointed out the pattern. The cost was not just the missed ruling: the
work continued on assumptions that the reply had already superseded.

Why it happens is structural, not careless:

- **Sending is rewarded immediately; reading is not.** The send completes a thought.
- **The reply arrives in a different surface** from the one the agent is working in, and nothing
  interrupts to say it landed.
- **A turn boundary looks like a safe stopping point**, and the reply has not arrived by then.

Disciplines:

- **Treat send-and-read as one atomic step.** A message is not delivered until its reply has been read;
  until then it is *outstanding*, and outstanding is a state, not a completion.
- **When work is asynchronous, the read must be scheduled, not hoped for** — a concrete trigger (the
  next turn in that collaboration, a check at a natural boundary, a watcher), never "later".
- **At the start of any turn inside an ongoing collaboration, read the channel before acting.** Acting
  on a stale assumption is worse than waiting one step.
- **Carry unread replies as open items**, with the same status as an unfinished task, because that is
  what they are.

## 9. Deferring an action is allowed; deferring durability is not

"Do it next time" is sometimes the right call — a release that would add churn, a change waiting on
evidence, a decision that genuinely needs a field signal. The failure mode is not the delay. It is the
**delay with no artifact**.

Observed occurrence: a maintainer's release ruling (hold the fix, ship it as a patch when one of three
conditions occurs) existed **only inside a chat transcript**. The code had landed and was verified; the
decision about when it becomes a release lived nowhere a future session would look. Recovering it later
would cost exactly what the transcript costs to re-read, and if the topic were interleaved with others
first, the ruling might not be recovered at all.

The distinction that makes this decidable:

```text
DEFER AN ACTION            allowed, if the TRIGGER is written into an artifact AT THE MOMENT of
                           deferring: what would cause it to proceed, who checks, and where the
                           pending item is recorded.
DEFER MAKING IT DURABLE    never allowed. An item that exists only as "we will deal with it later"
                           in a conversation is a plan to lose it.
DEFER THE EVIDENCE         allowed and often correct: the action is blocked on reality, not on
                           attention. The threshold must still be written down now.
```

Practical form that works: a **pending ledger** with one line per deferred item — the decision, the
trigger, the artifact that would change, and the link to where the reasoning lives. It is cheap to
write at the moment of deferral and it removes the entire reconstruction cost later.

A useful test before ending a turn: **if the context disappeared right now, what would be lost?**
Anything in that answer belongs in a file, an issue, or a ledger — not in the conversation.

