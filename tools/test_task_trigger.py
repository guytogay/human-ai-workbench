"""End-to-end checks for the opt-in event-driven task ledger."""

import json
from concurrent.futures import ThreadPoolExecutor
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("task_trigger.py")


class TaskTriggerTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.db = Path(self.temp.name) / "tasks.sqlite"
        self.plan = Path(self.temp.name) / "plan.json"
        self.plan.write_text(json.dumps({"tasks": [
            {"id": "a"}, {"id": "b", "after": ["a"]},
            {"id": "c", "after": ["a"]}, {"id": "d", "after": ["b", "c"]},
        ]}), encoding="utf-8")

    def call(self, *args, success=True):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "--db", str(self.db), *args],
            capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode == 0, success, result.stderr)
        return json.loads(result.stdout if success else result.stderr)

    def test_dependency_release_parallel_and_accept(self):
        self.assertEqual(self.call("init", "--plan", str(self.plan))["ready"], ["a"])
        self.call("claim", "--task", "a")
        self.assertEqual(self.call("finish", "--task", "a", "--result", "done")["ready"], ["b", "c"])
        self.call("claim", "--task", "b")
        self.call("claim", "--task", "c")
        self.assertEqual(self.call("finish", "--task", "b", "--result", "done")["ready"], [])
        self.assertEqual(self.call("finish", "--task", "c", "--result", "done")["ready"], ["d"])
        self.call("claim", "--task", "d")
        self.assertEqual(self.call("finish", "--task", "d", "--result", "done")["next_action"], "acceptance_due")
        self.assertEqual(self.call("accept", "--result", "pass")["mode"], "accepted")
        self.assertEqual(self.call("status")["ready"], [])

    def test_failure_and_explicit_retry(self):
        self.call("init", "--plan", str(self.plan))
        self.call("claim", "--task", "a")
        snap = self.call("finish", "--task", "a", "--result", "failed")
        self.assertEqual(snap["next_action"], "review_failure")
        self.assertEqual(snap["ready"], [])
        self.assertEqual(self.call("retry", "--task", "a")["ready"], ["a"])

    def test_stop_never_dispatches_or_restarts(self):
        self.call("init", "--plan", str(self.plan))
        self.assertEqual(self.call("stop")["mode"], "stopped")
        self.assertEqual(self.call("status")["ready"], [])
        self.call("claim", "--task", "a", success=False)
        self.call("retry", "--task", "a", success=False)
        self.call("add", "--task", "e", success=False)

    def test_failed_acceptance_requires_explicit_new_plan(self):
        self.plan.write_text('{"tasks": [{"id": "a"}]}', encoding="utf-8")
        self.call("init", "--plan", str(self.plan))
        self.call("claim", "--task", "a")
        self.call("finish", "--task", "a", "--result", "done")
        self.assertEqual(self.call("accept", "--result", "fail")["next_action"], "revise_plan")
        self.assertEqual(self.call("add", "--task", "fix", "--after", "a")["ready"], ["fix"])
        self.call("claim", "--task", "fix")
        self.call("finish", "--task", "fix", "--result", "done")
        self.assertEqual(self.call("accept", "--result", "pass")["mode"], "accepted")

    def test_validation_and_no_overwrite(self):
        self.plan.write_text('{"tasks": [{"id":"a","after":["b"]},{"id":"b","after":["a"]}]}', encoding="utf-8")
        self.call("init", "--plan", str(self.plan), success=False)
        self.assertFalse(self.db.exists())
        self.plan.write_text('{"tasks": [{"id":"a"}]}', encoding="utf-8")
        self.call("init", "--plan", str(self.plan))
        self.call("init", "--plan", str(self.plan), success=False)
        self.call("claim", "--task", "a")
        self.call("claim", "--task", "a", success=False)

    def test_parallel_dispatchers_cannot_claim_twice(self):
        self.call("init", "--plan", str(self.plan))

        def claim():
            return subprocess.run(
                [sys.executable, str(SCRIPT), "--db", str(self.db), "claim", "--task", "a"],
                capture_output=True, text=True, check=False,
            ).returncode

        with ThreadPoolExecutor(max_workers=2) as pool:
            codes = list(pool.map(lambda _: claim(), range(2)))
        self.assertEqual(sorted(codes), [0, 2])


if __name__ == "__main__":
    unittest.main()
