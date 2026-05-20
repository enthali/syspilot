# Change Document: orchestration-agent-adoption

## Summary

Migrate all agent files from the deprecated `DELEGATE` communication verb to the
orchestration skill vocabulary (`SEND`). Add `skills:` frontmatter declaration to
all agents that perform cross-session communication.

## Change Request

**Source:** PM (via Jarvis)
**Mode:** user-guided
**Branch:** `feature/orchestration-agent-adoption`

## Intent

The orchestration skill `syspilot.orchestration-jarvis` defines INVOKE/SEND/RECEIVE/RESPOND
as the canonical verb vocabulary. `DELEGATE` pre-dates the skill and has no tool mapping.
All agent workflow steps using `DELEGATE` for cross-session communication must be updated
to `SEND`.

## Impact Scope

**DELEGATE as communication verb (must fix):**

Product `syspilot/agents/`:
- `syspilot.cm.agent.md`: Steps 9, 11, quick-reference flow block
- `syspilot.pm.agent.md`: Step 7 (CR to CM), Step 4 (merge decision to CM)
- `syspilot.qm.agent.md`: Step 6 (Findings Report to PM), process flow block

Instance `.github/agents/` — corresponding copies.

**`skills:` frontmatter missing (must add):**
- `syspilot.cm.agent.md`, `syspilot.pm.agent.md`, `syspilot.qm.agent.md`

**Not in scope (prose/description, not verb instructions):**
- Lowercase "delegate" in description fields and guardrail prose
- `syspilot.setup.agent.md` — uses "delegate" only in prose, not as verb

## Artefakt-Removal Check

Removed artefact: `DELEGATE` verb in agent workflow steps.

Grep results:
- (a) Active code/workflow references: 8 occurrences in 3 agent files — fixed in this CR
- (b) Active documentation references: none in docs/
- (c) Historic Change Documents: prior CRs may reference DELEGATE — acceptable historic stranding

## Status

🔄 In progress.
