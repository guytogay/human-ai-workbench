# Optional task trigger ledger

`task_trigger.py` is a small standard-library reference for **event-driven task
handoffs**. It is a general project-working tool, not an ENA runtime component.
It holds one project's active task/dependency registry in SQLite. A Host calls it
when an actual task event occurs and receives the newly runnable successors **in
the same response**, without sleeping for a fixed interval.

It does **not** start Agents, observe external tools, inspect private sessions,
or bind messaging channels. A real Host must own authorization, task execution,
exception detection, dispatch hooks and any channel/session continuity.

Example `plan.json`:

```json
{"tasks": [
  {"id": "design"},
  {"id": "build", "after": ["design"]},
  {"id": "test", "after": ["design"]},
  {"id": "deliver", "after": ["build", "test"]}
]}
```

Use the same durable database for all sessions that own this project:

```bash
python3 tools/task_trigger.py --db project.sqlite init --plan plan.json
python3 tools/task_trigger.py --db project.sqlite claim --task design
# Host executes the task, checks its result, then reports the actual event:
python3 tools/task_trigger.py --db project.sqlite finish --task design --result done
# Response: ready = ["build", "test"]. Host dispatches these immediately.
python3 tools/task_trigger.py --db project.sqlite status
```

After all tasks finish, `next_action` becomes `acceptance_due`; acceptance is
explicit rather than inferred from task counts. A failed acceptance gives
`revise_plan`, and the Host may add a new corrective task. A failed task yields
`review_failure` until the Host explicitly invokes `retry`; no infinite retry
is hidden inside the tool.

```bash
python3 tools/task_trigger.py --db project.sqlite accept --result pass
# Or: accept --result fail, then add --task correction --after deliver
```

`stop` immediately makes `ready` empty and prevents further claims, retries,
additions or completions. Use this when the human ends the task. Do not use
idle time as an excuse to continue a closed project. The Host must contain any
already-running side effects using its own recovery path.

The ledger is the **active task register**, not a second copy of the full
project plan. Keep the human goal and acceptance criteria in the existing
project artifact. One ledger per active project is enough; Hosts handling many
projects must retain a discoverable index of those ledgers.

Wire Host task-finish / failure / acceptance events to the CLI and consume its
JSON response. Use deadline/timer checks only for genuinely time-dependent or
missing external events, as a fallback. If there are no actionable tasks, no
useful idle work is required; optional maintenance needs its own authorization
and budget. A channel-specific session handoff is a Host integration, not a
property this file can guarantee.

Run: `python3 -m unittest discover -s tools -p 'test_task_trigger.py'`.
