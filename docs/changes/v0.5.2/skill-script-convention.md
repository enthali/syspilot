# Change Document: skill-script-convention

**Status**: approved
**Branch**: feature/skill-script-convention
**Created**: 2026-04-30
**Author**: syspilot.design

---

## Summary

Two QA findings from the `skill-owns-scripts` CR require spec updates:
(1) scripts within a skill SHALL live in a named subdirectory (e.g. `scripts/`),
not directly at the skill root; (2) the change process (Design + Implement agents)
is explicitly scoped to `syspilot/` and `docs/` — the `.github/` installed instance
is exclusively maintained by the Setup Agent.

---

## Level 0: User Stories

**Status**: ✅ completed

### Impacted User Stories

| ID | Title | Impact | Notes |
|----|-------|--------|-------|
| — | — | none | Existing US already covers exchangeability; no change needed |

### Decisions

- No changes at Level 0. The existing `SYSP_US_SKILL_IMPACT` covers the
  exchangeability principle at a sufficiently abstract level.

### Horizontal Check (MECE)

- [x] No contradictions with existing User Stories
- [x] No redundancies
- [x] No gaps at this level

---

## Level 1: Requirements

**Status**: ✅ completed

### Impacted Requirements

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| `SYSP_REQ_SKILL_IMPACT_EXCHANGE` | `SYSP_US_SKILL_IMPACT` | modified | AC-4 clarified + AC-5 added |

### Changes Made

**`SYSP_REQ_SKILL_IMPACT_EXCHANGE`** (`docs/syspilot/requirements/req_skill_impact.rst`):

- **AC-4** extended: added explicit constraint that scripts SHALL be placed in a
  named subdirectory (e.g. `scripts/`), not directly at the skill root
- **AC-5** added: change process (Design Agent, Implement Agent) SHALL operate
  exclusively on `syspilot/` and `docs/`; `.github/` is the installed instance
  and SHALL be maintained exclusively by the Setup Agent

### Decisions

- AC-5 belongs here (not in a new requirement) because it is a constraint on the
  exchangeability implementation, not a separate capability.

### Horizontal Check (MECE)

- [x] No contradictions with existing Requirements
- [x] No redundancies
- [x] All modifications link to existing User Stories

---

## Level 2: Design

**Status**: ✅ completed

### Impacted Design Elements

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| `SYSP_SPEC_SKILL_IMPACT_EXCHANGE` | `SYSP_REQ_SKILL_IMPACT_EXCHANGE` | modified | File structure + scope rule |
| `SYSP_SPEC_SKILL_IMPACT_QUERY` | `SYSP_REQ_SKILL_IMPACT_QUERY` | modified | Tool path updated (cascading) |

### Changes Made

**`SYSP_SPEC_SKILL_IMPACT_EXCHANGE`** (`docs/syspilot/design/spec_skill_impact.rst`):

- **Skill File Structure** diagram: changed from `.github/` path to `syspilot/`
  product path as primary; added `scripts/` subdirectory containing
  `get_need_links.py`; self-containment note updated to state scripts SHALL use
  a named subdirectory
- **Change Process Scope** section added: explicitly states change agents operate
  on `syspilot/` and `docs/` only; `.github/` is installed instance, Setup Agent
  exclusive; installed instance structure shown for reference
- **Exchange Contract** step 1 updated: new skill folder created under
  `syspilot/skills/` with `SKILL.md` at root and scripts in a named subdirectory
- **Product Copy** section removed (superseded — primary structure already shows
  the `syspilot/` product path)

**`SYSP_SPEC_SKILL_IMPACT_QUERY`** (`docs/syspilot/design/spec_skill_impact.rst`):

- Tool path updated from `syspilot/skills/syspilot.impact-python/get_need_links.py`
  to `syspilot/skills/syspilot.impact-python/scripts/get_need_links.py`
  (cascading from subdirectory convention)

### Decisions

- `SYSP_SPEC_SKILL_IMPACT_QUERY` updated as cascading impact even though not in
  the original scope — the tool path reference would have been inconsistent.
- Installed instance structure shown as reference-only diagram under the new
  "Change Process Scope" section to make the two-path distinction concrete.

### Horizontal Check (MECE)

- [x] No contradictions with existing Design Specs
- [x] All modified SPECs link to Requirements
- [x] Product vs installed instance distinction is now unambiguous

---

## Final Consistency Check

**Status**: ✅ passed

### Traceability Verification

| User Story | Requirements | Design | Complete? |
|------------|--------------|--------|-----------|
| `SYSP_US_SKILL_IMPACT` | `SYSP_REQ_SKILL_IMPACT_EXCHANGE` | `SYSP_SPEC_SKILL_IMPACT_EXCHANGE` | ✅ |

### Sign-off

- [x] All levels completed
- [x] All conflicts resolved
- [x] Traceability verified
- [x] Ready for implementation

---

## Appendix: Implementation Notes for Implement Agent

The Implement Agent needs to:

1. Move `syspilot/skills/syspilot.impact-python/get_need_links.py` →
   `syspilot/skills/syspilot.impact-python/scripts/get_need_links.py`
2. Update any path references in `syspilot/skills/syspilot.impact-python/SKILL.md`
   to reflect the new `scripts/` subdirectory location
3. Do NOT touch `.github/skills/syspilot.impact-python/` (Setup Agent territory)

---

*Generated by syspilot.design*
