"""SYSP_VC_SETUP_GATES_1: fixture records evaluated against the rules of SYSP_REQ_SETUP_GATES.

These tests show that the gate rules are stated in the Setup Contract and checkable on records. They do not show
that a Setup executor obeys the rules and are not coverage of a practical Setup run. The required gates are read
from the Phase 5 table of `setup.md`, never from the record under test.
"""
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))

import setup_record_rules as rules  # noqa: E402

SETUP = ROOT / "docs" / "Syspilot Contracts" / "setup.md"


def read(path):
    return path.read_text(encoding="utf-8")


GATES = rules.required_gate_names(read(SETUP))
PASSED_EVIDENCE = "all gates: command, exit 0, ok; documentation build exit 0, 0 warnings"


def record(status, blocker="none", responsibility="Admin", gates=None, drop=(), verification=PASSED_EVIDENCE,
           verification_result="passed", log=None, delivery=("pending", "pending")):
    states = {name: "passed" for name in GATES} | (gates or {})
    gate_lines = "\n".join(f"| {name} | {state} | pass condition |" for name, state in states.items()
                           if name not in drop)
    log = log if log is not None else [("Admin", "Admin")]
    log_lines = "\n".join(f"| 2026-11-09 | 10:00 | {sender} | {receiver} | note |" for sender, receiver in log)
    evidence = [("Prerequisites", "passed", "ok"), (rules.VERIFICATION_ROW, verification_result, verification)]
    if delivery is not None:
        evidence.append((rules.DELIVERY_ROW, *delivery))
    evidence_lines = "\n".join(f"| {area} | {result} | {text} |" for area, result, text in evidence)
    return (
        "# Pristine Syspilot Setup\n\n"
        f"**Status:** {status}<br>\n**Executor:** Admin<br>\n**Current responsibility:** {responsibility}<br>\n"
        f"**Current blocker:** {blocker}<br>\n\n"
        "## Handover log\n\n| Date | Time | From | To | Note |\n|---|---|---|---|---|\n" + log_lines + "\n\n"
        "## Phase 5: Verify Installed Outcome\n\n| Gate | Status | Pass condition |\n|---|---|---|\n"
        + gate_lines + "\n\n## Phase 6: Seal Project State\n\ntext\n\n"
        "## Evidence Summary\n\n| Area | Result | Evidence or blocker |\n|---|---|---|\n" + evidence_lines + "\n"
    )


TO_PM = [("Admin", "Project Manager")]
ACKNOWLEDGED = ("passed", "acknowledged by the Project Manager at 10:50")
DISCOVERY_PENDING = "Jarvis actor discovery pending: wait for the rescan"
DOCUMENTATION_WARNINGS = "Documentation failed with 24 warnings: fix them"
WARNINGS_24 = "documentation build exit 0, 24 warnings"
SEALED_WITH_OPEN_GATE = ["open-gate-baseline", "open-gate-blocker", "open-gate-status", "sealed-with-open-gate"]

# The failure of the 2026-11-06 test run, reduced to the fields the rules read: status handed off, baseline verified,
# discovery pending, 24 documentation warnings, an aggregated result `conditional`, a PM handoff row `ready`.
REAL_FAILURE = record(
    "handed off", responsibility="Project Manager",
    gates={"Jarvis actor discovery": "pending", "Documentation": "failed"},
    verification=WARNINGS_24, verification_result="conditional",
    log=[("initiating Copilot session", "Project Manager")], delivery=("ready", "Setup record updated"))

# (name, record text, baseline_status in project.toml, expected violated rules)
CASES = [
    ("all gates passed, verified, executor still holds it", record("verified"), "verified", []),
    ("pre-acknowledgement handoff, also the record after a failed send", record(
        "verified", responsibility="Project Manager", log=TO_PM), "verified", []),
    ("acknowledged handoff", record(
        "handed off", responsibility="Project Manager", log=TO_PM, delivery=ACKNOWLEDGED), "verified", []),
    ("discovery pending, blocked, gate named", record(
        "blocked", blocker=DISCOVERY_PENDING, gates={"Jarvis actor discovery": "pending"}), "preparing", []),
    ("documentation failed with warnings, blocked, gate named", record(
        "blocked", blocker=DOCUMENTATION_WARNINGS, gates={"Documentation": "failed"}, verification=WARNINGS_24),
     "preparing", []),
    ("blocker survives a transfer to the Admin", record(
        "blocked", blocker=DISCOVERY_PENDING, gates={"Jarvis actor discovery": "pending"},
        log=[("initiating Copilot session", "Admin")]), "preparing", []),
    ("handed off while PM handoff is pending", record(
        "handed off", responsibility="Project Manager", log=TO_PM), "verified", ["handoff-row"]),
    ("handed off, PM handoff passed without evidence", record(
        "handed off", responsibility="Project Manager", log=TO_PM, delivery=("passed", "pending")), "verified",
     ["handoff-row"]),
    ("handed off but responsibility not the Project Manager", record(
        "handed off", log=TO_PM, delivery=ACKNOWLEDGED), "verified", ["handoff-record"]),
    ("handed off without a Handover-log entry to the Project Manager", record(
        "handed off", responsibility="Project Manager", delivery=ACKNOWLEDGED), "verified", ["handoff-record"]),
    ("verified, Project Manager named, no Handover-log entry", record(
        "verified", responsibility="Project Manager"), "verified", ["handoff-record"]),
    ("verified, Project Manager named, PM handoff already passed", record(
        "verified", responsibility="Project Manager", log=TO_PM, delivery=ACKNOWLEDGED), "verified", ["handoff-row"]),
    ("verified, Project Manager named, no PM handoff row", record(
        "verified", responsibility="Project Manager", log=TO_PM, delivery=None), "verified", ["handoff-row"]),
    ("Project Manager named while blocked", record(
        "blocked", responsibility="Project Manager", log=TO_PM), "preparing", ["handoff-record"]),
    ("PM handoff passed while the Admin holds the record", record("verified", delivery=ACKNOWLEDGED), "verified",
     ["handoff-row"]),
    ("discovery pending but verified and baseline verified", record(
        "verified", gates={"Jarvis actor discovery": "pending"}), "verified", SEALED_WITH_OPEN_GATE),
    ("discovery pending, blocked, but blocker none", record(
        "blocked", gates={"Jarvis actor discovery": "pending"}), "preparing", ["open-gate-blocker"]),
    ("discovery pending, blocker names another gate", record(
        "blocked", blocker="Documentation: fix", gates={"Jarvis actor discovery": "pending"}), "preparing",
     ["open-gate-blocker"]),
    ("open gate, baseline verified in project.toml", record(
        "blocked", blocker=DISCOVERY_PENDING, gates={"Jarvis actor discovery": "pending"}), "verified",
     ["open-gate-baseline", "record-baseline-disagree", "sealed-with-open-gate"]),
    ("open gate but status preparing", record(
        "preparing", blocker=DISCOVERY_PENDING, gates={"Jarvis actor discovery": "pending"}), "preparing",
     ["open-gate-status"]),
    ("a gate carries the status conditional", record(
        "blocked", blocker="Documentation conditional", gates={"Documentation": "conditional"}), "preparing",
     ["status-word"]),
    ("all gates passed but baseline preparing", record("verified"), "preparing", ["record-baseline-disagree"]),
    ("all gates passed, blocked, baseline verified", record("blocked"), "verified", ["record-baseline-disagree"]),
    ("documentation passed with warnings", record(
        "verified", verification="documentation build exit 0, 3 warnings"), "verified", ["documentation-warnings"]),
    ("documentation passed without a count", record(
        "verified", verification="documentation build exit 0"), "verified", ["documentation-warnings"]),
    ("handed off with a failed gate", record(
        "handed off", responsibility="Project Manager", gates={"Documentation": "failed"}, verification=WARNINGS_24,
        log=TO_PM, delivery=ACKNOWLEDGED), "verified",
     ["open-gate-baseline", "open-gate-blocker", "open-gate-handoff", "open-gate-status", "sealed-with-open-gate"]),
    ("passed gates without verification evidence", record("verified", verification="pending"), "verified",
     ["documentation-warnings", "gate-evidence"]),
    ("a pending gate removed from a blocked record", record(
        "blocked", blocker="Documentation pending", gates={"Documentation": "pending"},
        drop=["Jarvis actor discovery"]), "preparing", ["missing-gate"]),
    ("the 2026-11-06 failure", REAL_FAILURE, "verified",
     ["handoff-row", "open-gate-baseline", "open-gate-blocker", "open-gate-handoff", "open-gate-status",
      "sealed-with-open-gate", "status-word"]),
] + [
    (f"verified record without the {name} gate", record("verified", drop=[name]), "verified",
     ["missing-gate", "sealed-with-open-gate"])
    for name in GATES
]

ALL_RULES = {
    "status-word", "gate-evidence", "missing-gate", "sealed-with-open-gate", "open-gate-status",
    "open-gate-baseline", "open-gate-blocker", "open-gate-handoff", "documentation-warnings", "handoff-record",
    "handoff-row", "record-baseline-disagree"}


class GateRuleFixtureTests(unittest.TestCase):
    def test_each_fixture_violates_exactly_the_expected_rules(self):
        for name, text, baseline, expected in CASES:
            with self.subTest(case=name):
                self.assertEqual(rules.evaluate(text, baseline, GATES), expected)

    def test_the_fixture_set_covers_every_rule_with_valid_and_invalid_records(self):
        self.assertEqual({rule for *_, expected in CASES for rule in expected}, ALL_RULES)
        self.assertGreaterEqual(sum(1 for *_, expected in CASES if not expected), 6)
        evaluator = read(Path(rules.__file__))
        self.assertEqual(set(re.findall(r'violations\.add\("([a-z-]+)"\)', evaluator)), ALL_RULES)

    def test_the_required_gates_come_from_the_phase_five_table_of_the_contract(self):
        self.assertEqual(len(GATES), 8)
        self.assertEqual(GATES[0], "Integrity")
        self.assertNotIn(rules.DELIVERY_ROW, GATES)

    def test_an_empty_gate_inventory_is_never_all_passed(self):
        self.assertIn("sealed-with-open-gate", rules.evaluate(record("verified"), "verified", []))

    def test_the_contract_states_the_rules_the_evaluator_checks(self):
        text = " ".join(read(SETUP).split())
        self.assertIn("exactly one status: `pending`, `passed`, or `failed`", text)
        self.assertIn("No other status exists, such as `conditional`", text)
        self.assertIn("the Contract status stays `blocked`, `baseline_status` stays `\"preparing\"`, and `Current blocker` names the gate",
                      text)
        self.assertIn("only after every gate is `passed`", text)
        self.assertIn("The mandatory gates are exactly the rows of the table above; the Evidence Summary row `PM handoff` is a delivery row outside them",
                      text)
        self.assertIn("the Project Manager's own first commit on the record sets Contract status `handed off` and the row `PM handoff` to `passed`",
                      text)
        for area in (rules.VERIFICATION_ROW, rules.DELIVERY_ROW):
            self.assertIn(area, rules.evidence_rows(read(SETUP)))

    def test_the_requirement_and_the_verification_criterion_name_the_same_cases(self):
        requirements = " ".join(read(ROOT / "docs" / "syspilot" / "requirements" / "req_setup.rst").split())
        criterion = requirements.split(":id: SYSP_VC_SETUP_GATES_1", 1)[1].split(".. ", 1)[0]
        for fragment in ("discovery gate is ``pending``", "documentation gate is ``failed``",
                         "status ``blocked``, baseline status ``preparing``", "no handoff",
                         "compares the record with ``.syspilot/project.toml``"):
            self.assertIn(fragment, criterion)


if __name__ == "__main__":
    unittest.main()
