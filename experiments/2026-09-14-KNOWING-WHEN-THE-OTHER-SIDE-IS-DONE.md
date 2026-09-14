# Knowing When the Other Side Is Done

Date: 2026-09-14. Source: a multi-party project where one party is a web-session AI that works "act
first, summarise at the end", one party is an execution agent with shell access, and one party is an
independent verifier on a second host.

The earlier note in this directory covered *closing* honestly. This one covers the coordination
costs that appear before closing: knowing whether the other side has finished, and knowing whether a
failed check is real. Every item below cost real time in one session and generalises past that
session.

## 1. An instrument failure and a product failure look identical

A release-publication check compared the release body published on the forge against the file in the
repository. It reported a mismatch. The release was fine: the comparison had piped the forge CLI
through a shell that joined every line into one, so the two sides could never match.

The habit that caught it is cheap and worth making explicit:

> When a check fails, ask whether *the instrument* could produce this failure before believing the
> subject failed.

Two practical forms. Read **bytes**, not formatted output, when comparing text across tools — write
the comparison in a language that reads a stream to the end rather than in a pipeline whose joining
behaviour you would have to know. And when a check fails in a way that suggests total breakage
(everything wrong, nothing matching), suspect the harness first: real breakage is usually partial.

## 2. The report layer must not be the failure surface

A watcher that had successfully detected new content crashed while printing it, because the console
encoding could not represent the characters in the payload. Detection succeeded; reporting died; the
run looked like a failure.

Any tool whose output can contain non-ASCII should configure its own output stream for encoding and
error handling at start-up rather than inheriting the console's. A diagnostic that cannot be printed
is not a diagnostic. This is the same rule as "a check that could not run is not a passing check" —
applied to the tool that *reports* checks.

## 3. You cannot cheaply poll a party that summarises at the end

Asking a web-session collaborator "are you done?" costs a full page interaction, and the answer is
only meaningful once it has finished its own turn. Polling that way repeatedly is expensive and
lossy — and the failure mode is silent: you simply keep acting on a stale assumption.

Two changes fixed it, and both are general:

* **Ask the other side to mirror every final decision to a durable shared channel** it already
  writes to (for us, an issue in the repository under work). The web session keeps working the way it
  wants; the durable channel becomes the interface.
* **Watch that channel with a cheap background job that exits when something arrives.** The
  notification is the job completing, so nobody busy-polls and no context is spent waiting. One API
  call per interval against a comments list is a rounding error next to a page interaction.

The generalisable rule: *a collaborator's channel preference is a coupling. Convert it to a durable
artifact plus a local watcher, and the coordination cost stops scaling with the number of times you
need to know.*

## 4. Two implementations of one idea will drift; pin the behaviour, not the code

One capability ended up implemented twice: once inside a host integration where it must be fast and
dependency-free, once as the shipped reference tool that other adopters take away. The owner's rule
was blunt: one function must not have two behaviours.

Removing one implementation turned out to be the wrong fix — the reference implementation exists to
be adopted, and the host one exists to be fast and not to drag a second runtime into a service path.
What actually removes the risk is a **differential guard**: drive both implementations through the
same input and the same mutation, then compare the *semantics* (not the record bytes) and fail on any
difference.

It paid for itself on its first run, by catching a real divergence: one side called the third effect
`changed`, the other called it `modified`. Nobody would have noticed from either side alone.

The precondition that makes this honest: the guard must compare semantics, and it must say so. Two
records that represent the same observation in different shapes are not a drift; two different
answers to the same question are.

## 5. A verifier's own mistakes are part of its evidence

The most useful verification report in this session included, unprompted: a probe of its own that
caused a stall on the machine under test, a forensic tool of its own that had silently decoded only
the first frame of a compressed log (turning "present" into "absent" until a positive control was
run), and an explicit list of claims it could not check.

That disclosure is what made its two positive findings believable. A verification report with no
self-reported limits is not more trustworthy — it is less, because it has not shown where its
instrument could lie.

Corollary for the party being verified: a verification report that finds nothing wrong in the thing
under test, produced by a verifier that reports nothing wrong with itself, is close to no
information.

## 6. "Not observed" is not "nothing happened"

A host integration reported zero added, zero removed and zero modified for a task that declared no
scope at all. Every number was technically accurate and the conclusion a reader would draw was
false: nothing had been observed, so nothing could be said.

The verifier's version was better — null counts with an explicit `NOT_OBSERVED` marker and an
incomplete flag — and we adopted it. The general rule:

> An absence of observation and an observation of absence must not share a representation.

This applies to any summary a human or an agent will read: a zero, an empty list and a missing field
are three different statements, and collapsing them is how a system reports success it never
verified.
