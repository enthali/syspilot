# Change Document: install-update

**Status**: completed
**Branch**: feature/install-update
**Created**: 2026-01-29
**Author**: Change Agent

---

## Summary

Add a user story for downloading, installing, and updating syspilot in projects. This fills a gap in the "getting started" journey - existing stories assume the user already has syspilot.

---

## Level 0: User Stories

**Status**: ✅ completed

### Impacted User Stories

| ID | Title | Impact | Notes |
|----|-------|--------|-------|
| US_SYSPILOT_007 | Automatic Environment Bootstrap | context | Related - covers post-install bootstrap |
| US_SYSPILOT_008 | Use syspilot Across Projects | context | Related - covers multi-project sync |

### New User Stories

| ID | Title | Priority | Links |
|----|-------|----------|-------|
| US_SYSPILOT_012 | Install syspilot in New Project | mandatory | US_SYSPILOT_007 |
| US_SYSPILOT_013 | Adopt syspilot in Existing Project | mandatory | US_SYSPILOT_007 |
| US_SYSPILOT_014 | Update syspilot to Latest Version | mandatory | US_SYSPILOT_012, US_SYSPILOT_013 |

### Decisions

- Decision 1: Acceptance scenarios should be implementation-agnostic (WHY level, not HOW)
- Decision 2: Split into 3 stories: new project install, existing project adoption, update/migrate
- Decision 3: Install stories link to US_007 (bootstrap follows install)
- Decision 4: Update story links to both install stories (update requires prior install)

### Horizontal Check (MECE)

- [x] No contradictions with existing User Stories
- [x] No redundancies
- [x] Gaps identified and addressed (the "how do I get syspilot" gap)

---

## Level 1: Requirements

**Status**: ✅ completed

### Impacted Requirements

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| REQ_SYSPILOT_008 | US_SYSPILOT_008 | modified | Remove AC-2,3 (update/version) - now covered by REQ_021 |

### New Requirements

| ID | Title | Links | Priority |
|----|-------|-------|----------|
| REQ_SYSPILOT_018 | syspilot Distribution via Releases | US_SYSPILOT_012, US_SYSPILOT_013 | mandatory |
| REQ_SYSPILOT_019 | New Project Installation | US_SYSPILOT_012 | mandatory |
| REQ_SYSPILOT_020 | Existing Project Adoption | US_SYSPILOT_013 | mandatory |
| REQ_SYSPILOT_021 | Version Update and Migration | US_SYSPILOT_014 | mandatory |
| REQ_SYSPILOT_022 | Customization Preservation | US_SYSPILOT_013, US_SYSPILOT_014 | high |
| REQ_SYSPILOT_023 | Sphinx-Needs Mandatory Dependency | US_SYSPILOT_012, US_SYSPILOT_013 | mandatory |

### Decisions

- Decision 1: Requirements focus on user-observable behavior (WHAT), not implementation (HOW)
- Decision 2: REQ_008 modified to remove update/version tracking (now in REQ_021)
- Decision 3: Sphinx-needs is mandatory - separate requirement to make this explicit

### Horizontal Check (MECE)

- [x] No contradictions with existing Requirements
- [x] No redundancies (REQ_008 overlap resolved)
- [x] All new REQs link to User Stories

---

## Level 2: Design

**Status**: ✅ completed

### Impacted Design Elements

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| SPEC_SYSPILOT_004 | REQ_SYSPILOT_009 | reused | Init scripts - first step of installation, already exists |

### New Design Elements

| ID | Title | Links |
|----|-------|-------|
| SPEC_SYSPILOT_007 | Release Structure | REQ_SYSPILOT_018 |
| SPEC_SYSPILOT_008 | Setup Agent Design | REQ_SYSPILOT_019, REQ_SYSPILOT_020, REQ_SYSPILOT_023 |
| SPEC_SYSPILOT_009 | File Layout and Ownership | REQ_SYSPILOT_022 |
| SPEC_SYSPILOT_010 | Update Process | REQ_SYSPILOT_021 |

### Decisions

- Decision 1: Reuse SPEC_004 for init scripts (no duplication)
- Decision 2: Two-step install: init script (manual) → setup agent (interactive)
- Decision 3: Version tracking via version.json → version_installed.json rename
- Decision 4: Update agent checks GitHub for newer releases
- Decision 5: Intelligent merge for user-modified agent files during update
- Decision 6: Release process out of scope (separate user story)

### Horizontal Check (MECE)

- [x] No contradictions with existing Design specs
- [x] SPEC_004 reused, not duplicated
- [x] All new SPECs link to Requirements

---

## Final Consistency Check

**Status**: ✅ passed

### Traceability Verification

| User Story | Requirements | Design | Complete? |
|------------|--------------|--------|-----------|
| US_SYSPILOT_012 (Install New) | REQ_018, REQ_019, REQ_023 | SPEC_004, SPEC_007, SPEC_008 | ✅ |
| US_SYSPILOT_013 (Adopt Existing) | REQ_018, REQ_020, REQ_022, REQ_023 | SPEC_004, SPEC_007, SPEC_008, SPEC_009 | ✅ |
| US_SYSPILOT_014 (Update) | REQ_021, REQ_022 | SPEC_009, SPEC_010 | ✅ |

### Cross-Level Consistency

| Level 0 Intent | Level 1 Behavior | Level 2 Implementation | Aligned? |
|----------------|------------------|------------------------|----------|
| "install from beginning" | "invoke agents after install" | init script → setup agent | ✅ |
| "adopt without disruption" | "existing docs preserved" | file ownership separation | ✅ |
| "update and keep current" | "determine version, update, preserve" | version.json → version_installed.json | ✅ |
| "sphinx-needs required" | "user informed, guidance provided" | setup agent checks/installs | ✅ |

### Issues Found

- [x] SPEC_004 needs link update: add REQ_019, REQ_020 (noted for implementation)

### Sign-off

- [x] All levels completed (no ⚠️ DEPRECATED markers remaining)
- [x] All conflicts resolved (REQ_008 overlap fixed)
- [x] Traceability verified
- [x] Ready for implementation

---

## Implementation Notes

For the Implement Agent:

### Documentation (Change Agent)

1. **Add to us_syspilot.rst**: US_SYSPILOT_012, US_SYSPILOT_013, US_SYSPILOT_014 ✅ done

2. **Add to req_syspilot.rst**: REQ_SYSPILOT_018 through REQ_SYSPILOT_023 ✅ done

3. **Modify in req_syspilot.rst**: REQ_SYSPILOT_008 - simplified ACs ✅ done

4. **Add to spec_syspilot.rst**: SPEC_SYSPILOT_007, SPEC_008, SPEC_009, SPEC_010 ✅ done

5. **Modify in spec_syspilot.rst**: SPEC_SYSPILOT_004 - add links to REQ_019, REQ_020 ✅ done

6. **Sphinx-build validation**: ✅ passed (0 errors, 2 warnings)

### Code Implementation (Implement Agent)

7. **Update syspilot.setup.agent.md**: Added new Section 2 "Check Dependencies (Interactive)" ✅ done
   - Step 1: Python-Check
   - Step 2: pip/uv-Check
   - Step 3: Inform User About Required Dependencies
   - Step 4: Install with User Confirmation (uv pip install -r)
   - Step 5: Handle Graphviz (Optional, OS-specific)
   - Step 6: Validate Installation (sphinx-build --version)
   - Sections 3-7 renumbered accordingly

8. **Copy to .github/agents/**: syspilot.setup.agent.md ✅ done

### Pending

9. **init.ps1 / init.sh**: Simplified to minimal scripts ✅ done
   - One task only: copy Setup Agent to .github/agents/
   - All other logic moved to Setup Agent (interactive)
   - init.ps1: 28 lines, init.sh: 27 lines

10. **Release structure**: Create version.json with release info ⏳ pending (separate story)

---

## Status: ✅ COMPLETED

All items from this Change Document have been implemented except for the release structure (item 10), which is out of scope for this change and requires a separate user story.

---

*Generated by syspilot Change Agent, Implemented by syspilot Implement Agent*
