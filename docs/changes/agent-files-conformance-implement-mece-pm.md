# Change Document: agent-files-conformance-implement-mece-pm

## Change Request

Top-to-bottom Duties conformance refactor for 3 agents: Dev Engineer (implement),
MECE Engine, and Project Manager (PM). Last wave of the Duties/Workflow cleanup sweep.

## Scope

### User Stories
- `SYSP_US_IMPLEMENT` — Add Soul/Duties/Workflow sections; 4 outcome Duties (PM-wörtlich)
- `SYSP_US_MECE` — Add Soul/Duties/Workflow sections; 4 outcome Duties (PM-wörtlich)
- `SYSP_US_PM` — Add Soul/Duties/Workflow sections; 6 outcome Duties (PM-wörtlich)

### Requirements
- `SYSP_REQ_IMPLEMENT_DUTIES` — ACs as end-state guarantees (4 ACs)
- `SYSP_REQ_MECE_DUTIES` — ACs as end-state guarantees (4 ACs)
- `SYSP_REQ_PM_DUTIES` — ACs as end-state guarantees (6 ACs)

### Design Specs
- `SYSP_SPEC_IMPLEMENT_DUTIES` — numbered → outcome bullets (4)
- `SYSP_SPEC_MECE_DUTIES` — numbered → outcome bullets (4)
- `SYSP_SPEC_PM_DUTIES` — numbered → outcome bullets (6)

### Agent Files
- `syspilot/agents/syspilot.implement.agent.md` — outcome bullets (4)
- `syspilot/agents/syspilot.mece.agent.md` — outcome bullets (4)
- `syspilot/agents/syspilot.pm.agent.md` — outcome bullets (6)

## Pattern Applied

- Duties = outcome guarantees (bullets, unordered)
- Workflow = ordered action steps (numbered)
- 1 AC per Duty minimum (CE-gap prevention)
- No mechanism sentences in Duties (Obs-O prevention)
- Soul + Workflow unchanged
