# Change Document: installer-scoped-cleanup

**Status**: complete
**Branch**: feature/installer-scoped-cleanup
**Created**: 2026-06-30
**Author**: PM
**Operation Mode**: autonomous

---

## Summary

The Installer's orphan-cleanup step currently removes every file in `.github/agents/`, `.github/prompts/`, and `.github/skills/` that has no corresponding source in the upstream syspilot release. This means customer-owned agents, project-specific agents, and instance-only tailoring files (`*.tailoring.md`) are silently deleted on every update — a data-loss risk for any project that places non-syspilot files in those directories. The orphan-cleanup scope must be restricted to files that were originally installed by syspilot, identifiable by the `syspilot.` filename prefix, so that all other files in those directories are left untouched. Acceptance criterion: after an update run, non-syspilot files (e.g. a file named `myproject.pm.agent.md` or `syspilot.pm.tailoring.md`) in `.github/agents/` remain present and unmodified.

---

## Level 0: User Stories

**Status**: ✅ completed

### Impacted User Stories

| ID | Title | Impact | Notes |
|----|-------|--------|-------|
| SYSP_US_INSTALLER | Installer Agent | modified | AC-11: a file is orphan-removable only if it starts with `syspilot.` AND does not end with `.tailoring.md` |

### New User Stories

None.

### Decisions

- Orphan eligibility is a **two-part condition**: removable iff name starts with `syspilot.` **and** does not end with `.tailoring.md`.
- Customer-owned, project-specific (`myproject.*`), and instance tailoring files (`syspilot.*.tailoring.md`) are preserved across updates.
- Refinement from Test Designer finding: `syspilot.pm.tailoring.md` carries the `syspilot.` prefix but is not installer-managed; the prefix-only rule would have wrongly removed it.

### Horizontal Check (MECE)

- [x] No contradictions with existing User Stories
- [x] No redundancies
- [x] Gaps identified and addressed

---

## Level 1: Requirements

**Status**: ✅ completed

### Impacted Requirements

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| SYSP_REQ_INSTALLER_DUTIES | SYSP_US_INSTALLER | modified | AC-6 orphan cleanup scoped to `syspilot.` prefix |
| SYSP_REQ_INSTALLER_WORKFLOW | SYSP_US_INSTALLER | modified | AC-8 orphan detection scoped to `syspilot.` prefix |
| SYSP_REQ_INSTALLER_SCOPE | SYSP_US_INSTALLER | modified | AC-6 (duplicate orphan-cleanup AC) scoped — **not in original impact list**, found via grep |

### New Requirements

None.

### Conflicts Detected

None.

### Decisions

- `SYSP_REQ_INSTALLER_SCOPE` AC-6 carried the identical orphan-cleanup wording and was scoped in the same pass — leaving it unscoped would have contradicted DUTIES/WORKFLOW. Impact lists are hints, not complete scope.

### Horizontal Check (MECE)

- [x] No contradictions with existing Requirements
- [x] No redundancies (the two orphan-cleanup ACs are now consistent)
- [x] All modified REQs link to the User Story

---

## Level 2: Design

**Status**: ✅ completed

### Impacted Design Elements

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| SYSP_SPEC_INSTALLER_DUTIES | SYSP_REQ_INSTALLER_DUTIES | modified | Orphan Cleanup duty bullet scoped to `syspilot.` prefix |
| SYSP_SPEC_INSTALLER_WORKFLOW | SYSP_REQ_INSTALLER_WORKFLOW | modified | Step 6 enumerates/removes only `syspilot.`-prefixed orphans |

### New Design Elements

None.

### Conflicts Detected

None.

### Decisions

- Step 6 enumerates only `syspilot.`-prefixed target files for comparison; non-prefixed files are out of scope for removal entirely.

### Horizontal Check (MECE)

- [x] No contradictions with existing Designs
- [x] Both modified specs trace to their Requirements

---

## Final Consistency Check

**Status**: ✅ passed

### Traceability Verification

| User Story | Requirements | Design | Complete? |
|------------|--------------|--------|-----------|
| SYSP_US_INSTALLER | SYSP_REQ_INSTALLER_DUTIES, SYSP_REQ_INSTALLER_WORKFLOW, SYSP_REQ_INSTALLER_SCOPE | SYSP_SPEC_INSTALLER_DUTIES, SYSP_SPEC_INSTALLER_WORKFLOW | ✅ |

sphinx-build `-W` passes clean (EXIT=0) — all RST valid, all traceability links resolve.

### Artefakt-Removal-Check

This CR removes no artefact (file, field, configuration key, or REQ-ID). It narrows the
behaviour of an existing step (orphan cleanup) by adding a prefix condition. No grep sweep
required.

- [x] N/A — no artefact removed

### Issues Found

- None blocking. Implementation note for Dev Engineer: orphan cleanup must filter target
  enumeration by the `syspilot.` filename prefix **excluding** any file ending in `.tailoring.md`
  before computing the orphan set.
- **Pre-work (System Designer):** Working tree on branch carried ~21 stale uncommitted reversions of prior merged work (product-owns-tool-lists / agent-spec-base-toolset-links). Verified via git reflog — no destructive command; disk was behind HEAD. Restored to HEAD with `git restore` and user approval. No committed work lost.
- **Spec gap (Test Designer Round 1):** `SYSP_US_INSTALLER` AC-11 and `SYSP_REQ_INSTALLER_SCOPE` AC-6 as written did not protect `syspilot.*.tailoring.md` files (tailoring files carry the `syspilot.` prefix but were not installed by the installer). CD Summary explicitly lists them as protected. Spec gap sent back to System Designer for refinement: orphan eligibility requires `syspilot.` prefix **and** not `.tailoring.md` suffix. TC-SC-TAILORING parked pending spec fix.

### Sign-off

- [x] All levels completed (no ⚠️ DEPRECATED markers remaining)
- [x] All conflicts resolved
- [x] Traceability verified
- [x] Ready for implementation

---

## UAT

**Status**: ✅ completed

### UAT Artefacts

| ID | Title | Scenarios |
|----|-------|-----------|
| SYSP_US_UAT_INSTALLER_SCOPED_CLEANUP | UAT — Installer Scoped Cleanup | 3 executable |
| SYSP_REQ_UAT_INSTALLER_SCOPED_CLEANUP | UAT Fixtures | F-CUSTOMER-FILE, F-SYSPILOT-ORPHAN, F-TAILORING |
| SYSP_SPEC_UAT_INSTALLER_SCOPED_CLEANUP | UAT Checklists | TC-SC-CUSTOMER, TC-SC-ORPHAN, TC-SC-TAILORING |

### Scenario Summary

| Scenario | Test Data | Traces to | Status |
|----------|-----------|-----------|--------|
| TC-SC-CUSTOMER | `myproject.pm.agent.md` survives update untouched | SYSP_US_INSTALLER AC-11; SYSP_REQ_INSTALLER_SCOPE AC-6 | executable |
| TC-SC-ORPHAN | `syspilot.oldagent.agent.md` (no upstream source) is removed | SYSP_REQ_INSTALLER_SCOPE AC-6 | executable |
| TC-SC-TAILORING | `syspilot.pm.tailoring.md` survives update untouched | SYSP_US_INSTALLER AC-11; SYSP_REQ_INSTALLER_SCOPE AC-6 | executable (un-parked after spec gap fix) |

### Issues Found

- Round 1 (commit `eff59f2`): TC-SC-TAILORING parked — spec gap: `syspilot.*.tailoring.md` not yet protected by spec text. Sent back to System Designer for refinement.
- Round 2 (commit `24a4739`): TC-SC-TAILORING un-parked after spec gap closed (commit `2a667f0`). All 3 scenarios executable.

---

## Implementation

**Status**: ✅ completed

### Changed Files

| File | Nature |
|------|--------|
| `syspilot/agents/syspilot.installer.agent.md` | Product source — Duties + Workflow Step 6 updated |
| `.github/agents/syspilot.installer.agent.md` | Installed instance — kept in sync |

### Summary

Both installer agent files now enforce the two-part eligibility condition in Duties (Orphan Cleanup bullet) and Workflow (Step 6): a file is removable only if its name starts with `syspilot.` **and** does not end with `.tailoring.md`.

### Issues Found

- None.

---

## Documentation

**Status**: ✅ completed

### Changed Files

| File | Nature |
|------|--------|
| `docs/architecture.md` | Updated "Update Safety" section: added Orphan Cleanup paragraph with two-part eligibility; strengthened tailoring-file guarantee |

### Reviewed, No Change Needed

- `docs/workflows.md` — no Installer orphan-removal description
- `docs/methodology.md` — no Installer cleanup description
- `README.md` — no file-removal claims
- Release notes — no in-flight file; behaviour gets entry at release time

### Issues Found

- None.

---

## QM Findings

*QM writes findings directly into this section after each review round. PM records
decisions (fix-now / defer / accept-as-is) with rationale in the same section.
Multiple review rounds are appended as sub-sections. Existing CDs without this
section are unaffected — the section is additive, never required retroactively.*

### Round 1

**Reviewed by:** Quality Manager
**Review date:** 2026-06-30
**Scope:** L0–L2 targeted check — all declared specs + agent files + trace links + UAT artefacts + schema validation.

#### Findings

No findings.

- **L0**: `SYSP_US_INSTALLER` AC-11 correctly specifies two-part orphan eligibility condition (name starts with `syspilot.` **AND** does not end with `.tailoring.md`) ✅
- **L1**: All three impacted REQs carry the two-part condition with consistent wording:
  - `SYSP_REQ_INSTALLER_DUTIES` AC-6 ✅
  - `SYSP_REQ_INSTALLER_SCOPE` AC-6 ✅ (correctly identified as impacted despite not being in initial CM scope hint)
  - All REQs link correctly to `SYSP_US_INSTALLER` ✅
- **L2**: All two impacted SPECs carry the two-part condition:
  - `SYSP_SPEC_INSTALLER_DUTIES` Orphan Cleanup duty bullet ✅
  - `SYSP_SPEC_INSTALLER_WORKFLOW` Step 6 (enumeration + removal rules) ✅
- **Agent files**: Both `syspilot/agents/syspilot.installer.agent.md` and `.github/agents/syspilot.installer.agent.md` carry both bullets with matching two-part condition wording ✅
- **Trace links**: All L0–L2 elements have correct parent-child trace links; UAT artefacts exist with full trace chain (`SYSP_US_UAT_INSTALLER_SCOPED_CLEANUP` → REQ → SPEC) ✅
- **Schema validation**: sphinx-needs 0 warnings ✅
- **Documentation**: `docs/architecture.md` updated with orphan-cleanup two-part eligibility explanation ✅

**Verdict: CLEAN. All acceptance criteria met.**

#### PM Decisions

| # | Finding # | Decision | Rationale |
|---|-----------|----------|-----------|
| — | — | — | No findings — no decisions required. |

---

## Appendix: Link Discovery Results

```
{paste output from get_need_links.py as needed}
```

---

*Generated by syspilot Change Agent*
