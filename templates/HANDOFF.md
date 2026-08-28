# Handoff

A handoff is not a project archive. It should carry the minimum context needed for the next session to continue correctly.

## 1. Current state

Attach or paste the project's current `NOW.md`.

Do not rewrite the same state into a second long summary unless the transfer surface cannot carry `NOW.md` directly.

## 2. Recent conversation slice

Default: **10 relevant user/assistant exchanges**.

One exchange = one user message + the assistant response.

Choose depth:

- **LIGHT — 5 exchanges**: simple continuation, little ambiguity.
- **NORMAL — 10 exchanges**: default for ordinary project continuation.
- **DEEP — 15–20 exchanges**: use only when a recent argument, design turn, or correction cannot be represented safely in a shorter slice.

Prefer contiguous recent exchanges when possible so the next session can see how decisions evolved.

Do not dump the full conversation by default.

## 3. Earlier context worth carrying

Add at most 3 earlier items by default when recency alone would hide something decision-relevant.

For each item:

- **What:** quote, decision, artifact, or link.
- **Why it still matters:** one sentence.

Do not add historical context merely because it is interesting.

## 4. Current artifacts

Link only what the next action needs.

- Working file / branch / PR:
- Active issue:
- Test or evidence artifact:

Machine-known facts such as CI run IDs, commit lists, and checksums should normally be retrieved from Git/CI rather than copied here.

## 5. Explicit human direction

Carry any instruction whose loss would materially change the work, especially:

- rejected approaches;
- scope boundaries;
- required tone or output constraints;
- decisions that should not be silently reopened.

## 6. Next consequential action

Write one concrete next action.

If the next session can understand the goal, decisions, unknowns, and this next action from the material above, the handoff is sufficient.

## Receiver behavior

The receiving AI should normally:

1. Read `NOW.md`.
2. Read the conversation slice.
3. Read only the linked artifacts needed for the next action.
4. State or internally resolve: current goal, decided facts, unknowns, next consequential action.
5. Start work.

Do **not** perform a full repository/project audit unless the current action genuinely depends on it.

If the handoff is insufficient, retrieve the smallest missing piece rather than rebuilding the entire project history.
