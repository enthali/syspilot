---
description: "Governs Contract responsibility, committed handoffs, consultation, and blocker escalation for every Syspilot actor."
applyTo: "**"
---
# Contract Handling

`Current responsibility` is temporary authority to maintain the Contract instance; durable artifact ownership does not change.

## Handoff

- **HANDOFF** (via `SEND`) — after completing work, select the next logical included artifact owner whose work can progress the Contract. Update Contract status, artifact evidence, and `Current responsibility`, then commit the Contract and related artifacts as one consistent state before sending HANDOFF. This intentionally prioritizes single-writer, consistent Contract state over uninterrupted communication and accepts the brief notification gap. In the HANDOFF message, identify the Contract path, commit, completed outcome, and remaining work.
- **ACK** (via `RESPOND`) — before starting work received through a HANDOFF, verify that the named commit's Contract header actually states `Current responsibility` as yourself. If verified, RESPOND with ACK. If not, do not acknowledge; escalate the discrepancy instead.

## Consultation

- **CONSULT** (via `SEND`) — request advice or review from another actor at any time, explicitly marked as a consultation. Consultation never transfers `Current responsibility`; the consulting actor remains read-only for the Contract and versioned work artifacts.
- **CONSULTRESPOND** (via `RESPOND`) — return the consulted actor's answer or findings to the asker. Does not transfer `Current responsibility`.

Questions and escalation do not transfer `Current responsibility`. When no included artifact owner can progress the Contract, record an actionable blocker and escalate.