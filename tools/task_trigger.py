#!/usr/bin/env python3
"""Optional, Host-neutral task trigger ledger; it never launches an Agent."""

import argparse
import datetime as dt
import json
import re
import sqlite3
import sys
from pathlib import Path


TASK_ID = re.compile(r"[A-Za-z0-9_.:-]{1,80}\Z")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def validate_task(value):
    require(isinstance(value, dict), "task must be an object")
    ident = value.get("id")
    deps = value.get("after", [])
    require(isinstance(ident, str) and TASK_ID.fullmatch(ident), "invalid task id")
    require(isinstance(deps, list), "after must be a list")
    require(all(isinstance(dep, str) and TASK_ID.fullmatch(dep) for dep in deps), "invalid dependency")
    require(len(deps) == len(set(deps)) and ident not in deps, "duplicate or self dependency")
    return ident, deps


def validate_plan(raw):
    require(isinstance(raw, dict) and isinstance(raw.get("tasks"), list), "plan needs tasks list")
    require(raw["tasks"], "plan must have at least one task")
    tasks = dict(validate_task(item) for item in raw["tasks"])
    require(len(tasks) == len(raw["tasks"]), "duplicate task id")
    for ident, deps in tasks.items():
        require(all(dep in tasks for dep in deps), f"unknown dependency of {ident}")
    visiting, visited = set(), set()

    def visit(ident):
        require(ident not in visiting, "dependency cycle")
        if ident not in visited:
            visiting.add(ident)
            for dep in tasks[ident]:
                visit(dep)
            visiting.remove(ident)
            visited.add(ident)

    for ident in tasks:
        visit(ident)
    return tasks


def db_open(path):
    require(Path(path).is_file(), "ledger not initialized")
    conn = sqlite3.connect(path, timeout=10)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA busy_timeout = 10000")
    return conn


def mode(conn):
    row = conn.execute("SELECT value FROM meta WHERE key='mode'").fetchone()
    require(row is not None, "invalid ledger")
    return row[0]


def event(conn, action, task=None, detail=""):
    conn.execute(
        "INSERT INTO events(at, action, task, detail) VALUES(?,?,?,?)",
        (dt.datetime.now(dt.timezone.utc).isoformat(), action, task, detail),
    )


def view(conn):
    state = mode(conn)
    items = [dict(row) for row in conn.execute("SELECT id, after_json, state FROM tasks ORDER BY id")]
    done = {item["id"] for item in items if item["state"] == "done"}
    ready = [
        item["id"] for item in items
        if state == "active" and item["state"] == "pending"
        and set(json.loads(item["after_json"])) <= done
    ]
    counts = {key: sum(item["state"] == key for item in items) for key in ("pending", "running", "done", "failed")}
    if state in ("stopped", "accepted", "needs_revision"):
        next_action = {"stopped": "none", "accepted": "none", "needs_revision": "revise_plan"}[state]
    elif ready:
        next_action = "dispatch_ready"
    elif counts["failed"]:
        next_action = "review_failure"
    elif counts["running"]:
        next_action = "await_running_event"
    elif counts["pending"]:
        next_action = "blocked_on_dependencies"
    else:
        next_action = "acceptance_due"
    return {"mode": state, "ready": ready, "counts": counts, "next_action": next_action}


def change_task(conn, ident, expected, new_state, action, detail=""):
    row = conn.execute("SELECT state FROM tasks WHERE id=?", (ident,)).fetchone()
    require(row is not None, "unknown task")
    require(row[0] == expected, f"task must be {expected}")
    conn.execute("UPDATE tasks SET state=? WHERE id=?", (new_state, ident))
    event(conn, action, ident, detail)


def run(args):
    if args.command == "init":
        tasks = validate_plan(json.loads(Path(args.plan).read_text(encoding="utf-8")))
        require(not Path(args.db).exists(), "ledger already exists; refusing overwrite")
        conn = sqlite3.connect(args.db, timeout=10)
        conn.row_factory = sqlite3.Row
        try:
            with conn:
                conn.execute("CREATE TABLE meta(key TEXT PRIMARY KEY, value TEXT NOT NULL)")
                conn.execute("CREATE TABLE tasks(id TEXT PRIMARY KEY, after_json TEXT NOT NULL, state TEXT NOT NULL)")
                conn.execute("CREATE TABLE events(seq INTEGER PRIMARY KEY, at TEXT NOT NULL, action TEXT NOT NULL, task TEXT, detail TEXT NOT NULL)")
                conn.execute("INSERT INTO meta VALUES('mode','active')")
                conn.executemany("INSERT INTO tasks VALUES(?,?,'pending')", ((i, json.dumps(deps)) for i, deps in tasks.items()))
                event(conn, "init", detail=f"{len(tasks)} tasks")
            return view(conn)
        finally:
            conn.close()

    conn = db_open(args.db)
    try:
        if args.command == "status":
            return view(conn)
        with conn:
            conn.execute("BEGIN IMMEDIATE")  # Serialize competing dispatchers.
            current = mode(conn)
            if args.command == "stop":
                require(current != "accepted", "project already accepted")
                conn.execute("UPDATE meta SET value='stopped' WHERE key='mode'")
                event(conn, "stop")
            elif args.command == "claim":
                require(args.task in view(conn)["ready"], "task is not ready")
                change_task(conn, args.task, "pending", "running", "claim")
            elif args.command == "finish":
                require(current == "active", "project is not active")
                change_task(conn, args.task, "running", args.result, args.result, args.evidence or "")
            elif args.command == "retry":
                require(current == "active", "project is not active")
                change_task(conn, args.task, "failed", "pending", "retry")
            elif args.command == "accept":
                require(current == "active", "project is not active")
                snap = view(conn)
                require(snap["counts"]["done"] == sum(snap["counts"].values()), "unfinished tasks")
                conn.execute("UPDATE meta SET value=? WHERE key='mode'", ("accepted" if args.result == "pass" else "needs_revision",))
                event(conn, "accept_" + args.result, detail=args.evidence or "")
            elif args.command == "add":
                require(current in ("active", "needs_revision"), "project cannot accept new tasks")
                ident, deps = validate_task({"id": args.task, "after": args.after})
                available = {row[0] for row in conn.execute("SELECT id FROM tasks")}
                require(ident not in available, "duplicate task id")
                require(set(deps) <= available, "unknown dependency")
                conn.execute("INSERT INTO tasks VALUES(?,?,'pending')", (ident, json.dumps(deps)))
                conn.execute("UPDATE meta SET value='active' WHERE key='mode'")
                event(conn, "add", ident)
            else:
                raise ValueError("unknown command")
        return view(conn)
    finally:
        conn.close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", required=True, help="One SQLite ledger per project")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("status")
    command = sub.add_parser("init")
    command.add_argument("--plan", required=True, help='JSON: {"tasks":[{"id":"build","after":[]}]}')
    for name in ("claim", "retry"):
        command = sub.add_parser(name)
        command.add_argument("--task", required=True)
    command = sub.add_parser("finish")
    command.add_argument("--task", required=True)
    command.add_argument("--result", required=True, choices=("done", "failed"))
    command.add_argument("--evidence", default="")
    sub.add_parser("stop")
    command = sub.add_parser("accept")
    command.add_argument("--result", required=True, choices=("pass", "fail"))
    command.add_argument("--evidence", default="")
    command = sub.add_parser("add")
    command.add_argument("--task", required=True)
    command.add_argument("--after", action="append", default=[])
    args = parser.parse_args()
    try:
        print(json.dumps(run(args), ensure_ascii=False, sort_keys=True))
    except (ValueError, OSError, sqlite3.Error, json.JSONDecodeError) as exc:
        print(json.dumps({"error": str(exc)}), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
