"""Test-side evaluator of SYSP_REQ_SETUP_GATES over a Setup record and the project.toml baseline status.

It states the rules of the requirement as checks on records. It does not show that a Setup executor obeys them
and is not evidence of a practical Setup run. The mandatory gates come from the caller (the Phase 5 table of
`setup.md`), never from the record under test. Gate statuses are read from the Phase 5 table of the record; the
evidence is read from the Evidence Summary row `Mandatory verification`, and the delivery state from the row
`PM handoff`, which is outside the gates. The warning count is assumed to be written as "N warnings" in the
`Mandatory verification` evidence, because the Contract does not fix its form.
"""
import re

ALLOWED_STATUSES = ("pending", "passed", "failed")
SEALED_STATUSES = ("verified", "handed off")
VERIFICATION_ROW = "Mandatory verification"
DELIVERY_ROW = "PM handoff"


def header_field(text, name):
    match = re.search(r"^\*\*" + re.escape(name) + r":\*\*\s*(.*?)(?:<br>)?\s*$", text, re.MULTILINE)
    return match.group(1).strip() if match else None


def table_rows(text, heading):
    """Cell lists of the table under a '## heading', without header and separator rows."""
    section = text.split("\n## " + heading, 1)
    if len(section) < 2:
        return []
    body = section[1].split("\n## ", 1)[0]
    rows = [[cell.strip() for cell in line.strip().strip("|").split("|")]
            for line in body.splitlines() if line.strip().startswith("|")]
    return rows[2:]


def required_gate_names(setup_text):
    return [row[0] for row in table_rows(setup_text, "Phase 5: Verify Installed Outcome")]


def gate_rows(text):
    return {row[0]: row[1] for row in table_rows(text, "Phase 5: Verify Installed Outcome")}


def evidence_rows(text):
    return {row[0]: row[1:] for row in table_rows(text, "Evidence Summary")}


def handover_next_owners(text):
    section = text.split("\n## Handover log", 1)[1].split("\n## ", 1)[0]
    owners = []
    for line in section.splitlines():
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if line.strip().startswith("|") and len(cells) >= 5 and re.fullmatch(r"\d{4}-\d{2}-\d{2}", cells[0]):
            owners.append(cells[3])
    return owners


def warning_count(evidence):
    match = re.search(r"(\d+) warnings?", evidence or "")
    return int(match.group(1)) if match else None


def is_open(cell):
    return cell.strip().lower() in ("", "pending")


def evaluate(record_text, baseline_status, required_gates):
    """Return the sorted rule identifiers that the record and the baseline status violate."""
    violations = set()
    status = header_field(record_text, "Status")
    blocker = header_field(record_text, "Current blocker") or ""
    responsibility = header_field(record_text, "Current responsibility")
    gates = gate_rows(record_text)
    evidence = evidence_rows(record_text)
    verification = evidence.get(VERIFICATION_ROW, ["pending", "pending"])
    delivery = evidence.get(DELIVERY_ROW, ["", ""])
    open_gates = [name for name in required_gates if gates.get(name) in ("pending", "failed")]

    if any(value not in ALLOWED_STATUSES for value in gates.values()):
        violations.add("status-word")
    if any(row and row[0].lower() == "conditional" for row in evidence.values()):
        violations.add("status-word")
    if any(name not in gates for name in required_gates):
        violations.add("missing-gate")
    if any(gates.get(name) in ("passed", "failed") for name in required_gates) and is_open(verification[-1]):
        violations.add("gate-evidence")

    all_passed = bool(required_gates) and all(gates.get(name) == "passed" for name in required_gates)
    if (status in SEALED_STATUSES or baseline_status == "verified") and not all_passed:
        violations.add("sealed-with-open-gate")

    if open_gates:
        if status != "blocked":
            violations.add("open-gate-status")
        if baseline_status != "preparing":
            violations.add("open-gate-baseline")
        if blocker.lower() in ("", "none") or not any(name.lower() in blocker.lower() for name in open_gates):
            violations.add("open-gate-blocker")
        if responsibility == "Project Manager" or status == "handed off":
            violations.add("open-gate-handoff")

    if gates.get("Documentation") == "passed" and warning_count(verification[-1]) != 0:
        violations.add("documentation-warnings")

    handed_to_pm = "Project Manager" in handover_next_owners(record_text)
    delivery_result = delivery[0] if delivery else ""
    if status == "verified" and responsibility == "Project Manager":
        if not handed_to_pm:
            violations.add("handoff-record")
        if delivery_result != "pending":
            violations.add("handoff-row")
    elif status == "handed off":
        if responsibility != "Project Manager" or not handed_to_pm:
            violations.add("handoff-record")
        if delivery_result != "passed" or is_open(delivery[-1]):
            violations.add("handoff-row")
    else:
        if responsibility == "Project Manager":
            violations.add("handoff-record")
        if delivery_result == "passed":
            violations.add("handoff-row")

    if (baseline_status == "verified") != (status in SEALED_STATUSES):
        violations.add("record-baseline-disagree")

    return sorted(violations)
