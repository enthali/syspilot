---
description: "Governs Contract responsibility, committed handoffs, consultation, and blocker escalation for every Syspilot actor."
applyTo: "**"
---
# Contract Handling

- `Current responsibility` is temporary authority to maintain the Contract instance; durable artifact ownership does not change.
- After completing work, select the next logical included artifact owner whose work can progress the Contract.
- Before `SEND`, update Contract status, artifact evidence, and `Current responsibility`, then commit the Contract and related artifacts as one consistent state. This intentionally prioritizes single-writer, consistent Contract state over uninterrupted communication and accepts the brief notification gap.
- In the handoff, identify the Contract path, commit, completed outcome, and remaining work.
- Any actor may request advice or review from another actor at any time without transferring `Current responsibility`; the consulting actor remains read-only for the Contract and versioned work artifacts and returns only advice or findings.
- Questions and escalation do not transfer `Current responsibility`.
- When no included artifact owner can progress the Contract, record an actionable blocker and escalate.