# Change Document: chg-launcher

**Status**: ready-for-merge
**Branch**: feature/chg-launcher
**Created**: 2026-07-28
**Author**: PM
**Operation Mode**: autonomous

---

## Summary

Introduce a `syspilot.change-launcher` skill that automates the four mechanical steps at the start of every change initiative: create the feature branch from `development`, copy the change-document template, and pre-fill the five header fields (Status, Branch, Created, Author, Operation Mode) before making the initial commit. These steps are deterministic and require no judgment, but they are a recurring source of errors (wrong fields touched, Operation Mode forgotten, CM territory inadvertently modified). Offloading them to a script lets the PM focus immediately on the Summary — the one part that genuinely requires human intent. The skill is delivered as a Python script under `syspilot/skills/syspilot.change-launcher/`, installed by the Setup Agent, and backed by new spec elements `SYSP_US_CHG_LAUNCHER` / `SYSP_REQ_CHG_LAUNCHER` / `SYSP_SPEC_CHG_LAUNCHER`.

---

## Level 0: User Stories

**Status**: ✅ completed

### Impacted User Stories

None.

### New User Stories

| ID | Title | Priority |
|----|-------|----------|
| SYSP_US_CHG_LAUNCHER | Change Launcher Automation | mandatory |

### Decisions

- Single US — one coherent automation capability.
- Links to SYSP_US_PM (PM is the consumer).
- Branch-exists case: warn + continue (not a failure).

### Horizontal Check (MECE)

- [x] No contradictions with existing User Stories
- [x] No redundancies
- [x] No gaps

---

## Level 1: Requirements

**Status**: ✅ completed

### Impacted Requirements

None.

### New Requirements

| ID | Title | Links | Priority |
|----|-------|-------|----------|
| SYSP_REQ_CHG_LAUNCHER | Change Launcher Automation | SYSP_US_CHG_LAUNCHER | mandatory |

### Decisions

- 9 ACs covering the full script contract (inputs, outputs, errors, SKILL.md).
- Branch-exists = warn + continue (AC-3), CD-exists = hard error (AC-7).

### Horizontal Check (MECE)

- [x] No contradictions with existing Requirements
- [x] No redundancies
- [x] All new REQs link to User Stories

---

## Level 2: Design

**Status**: ✅ completed

### Impacted Design Elements

| ID | Impact | Notes |
|----|--------|-------|
| SYSP_SPEC_PM_WORKFLOW | text update | Added launcher cross-reference note at steps 7–8 |

### New Design Elements

| ID | Title | Links |
|----|-------|-------|
| SYSP_SPEC_CHG_LAUNCHER | Change Launcher Script | SYSP_REQ_CHG_LAUNCHER |

### Decisions

- Script name: `launch_change.py`
- Three required args: `--name`, `--author`, `--mode`
- Exit codes: 0 = success, 1 = precondition failure
- SKILL.md: description + parameters + error conditions (no example section)
- PM_WORKFLOW gets informational note, not a hard dependency

### Horizontal Check (MECE)

- [x] No contradictions with existing Designs
- [x] All new SPECs link to Requirements

---

## Final Consistency Check

**Status**: ✅ passed

### Traceability Verification

| User Story | Requirements | Design | Complete? |
|------------|--------------|--------|-----------|
| SYSP_US_CHG_LAUNCHER | SYSP_REQ_CHG_LAUNCHER | SYSP_SPEC_CHG_LAUNCHER | ✅ |

### Artefakt-Removal-Check

Not applicable — no artefacts removed.

### Issues Found

None.

### Sign-off

- [x] All levels completed
- [x] All conflicts resolved
- [x] Traceability verified
- [x] Ready for implementation

---

## Documentation

**Status**: ✅ completed

### Changes Made

| File | Change |
|------|--------|
| `docs/architecture.md` | Added `syspilot.change-launcher/` to skills inventory in the Product directory tree |

### No Changes Needed

- `docs/workflows.md` — no PM step 7–8 or launcher references; skill usage is documented in SKILL.md
- `docs/methodology.md` — not affected
- `README.md` — not affected

---

## QM Findings

*QM writes findings directly into this section after each review round. PM records
decisions (fix-now / defer / accept-as-is) with rationale in the same section.
Multiple review rounds are appended as sub-sections. Existing CDs without this
section are unaffected — the section is additive, never required retroactively.*

### Round 1

**Reviewed by:** MECE Engineer + Trace Engineer
**Review date:** 2026-07-31

#### Findings

None. All 7 MECE dimensions verified clean:

- **L0 MECE:** 1 new US (SYSP_US_CHG_LAUNCHER), no contradictions, no redundancies
- **L1 MECE:** 1 new REQ (SYSP_REQ_CHG_LAUNCHER) with 9 ACs correctly specified, no contradictions
- **L2 MECE:** 1 new SPEC (SYSP_SPEC_CHG_LAUNCHER) + 1 impacted SPEC (SYSP_SPEC_PM_WORKFLOW) correctly updated
- **UAT Chain:** 3 new UAT elements (US/REQ/SPEC) with 5 test scenarios covering all 9 ACs
- **Traceability:** All L0→L1→L2 links intact, no dangling references, no cycles
- **Implementation:** launch_change.py present with full logic, SKILL.md complete with parameter/error/exit-code documentation
- **Docs:** architecture.md updated with skills inventory entry

**Sphinx build:** -W clean, exit 0.

**Status:** ✅ CLEAN — Ready for merge.

---

---

*Generated by syspilot Change Agent*
