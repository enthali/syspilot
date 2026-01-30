# Change Document: release-process

**Status**: approved
**Branch**: feature/release-process
**Created**: 2026-01-30
**Author**: syspilot Change Agent

---

## Summary

Document the complete release process for syspilot, including version management, tagging, packaging, and distribution workflows.

---

## Level 0: User Stories

**Status**: ✅ completed

### Impacted User Stories

| ID | Title | Impact | Notes |
|----|-------|--------|-------|
| US_SYSPILOT_012 | Install syspilot in New Project | closely related | Needs released artifacts |
| US_SYSPILOT_013 | Adopt syspilot in Existing Project | closely related | Requires distributed releases |
| US_SYSPILOT_014 | Update syspilot to Latest Version | closely related | Depends on release versioning |
| US_SYSPILOT_008 | Use syspilot Across Projects | related | Requires reliable releases |

### New User Stories

| ID | Title | Priority |
|----|-------|----------|
| US_SYSPILOT_015 | Create syspilot Release | mandatory |
| US_SYSPILOT_016 | Validate Release Quality | mandatory |
| US_SYSPILOT_017 | Release Agent Template | medium |

### Decisions

- **Distribution**: GitHub Releases (standard platform for version distribution)
- **Versioning**: Semantic Versioning (major.minor.patch) as per GitHub convention
- **Release Agent**: Document as template/example for users to customize
- **Rollback**: Roll forward only - bug fixes get new versions with higher numbers
- **Automation**: GitHub Actions for doc builds and release publishing

### Horizontal Check (MECE)

- [x] No contradictions with existing User Stories
- [x] No redundancies - Clear separation: US_015/016/017 (maintainer) vs US_012/013/014 (user)
- [x] Gaps identified: Distribution mechanism (GitHub Releases), versioning scheme (SemVer), automation (GH Actions)

---

## Level 1: Requirements

**Status**: ✅ completed

### Impacted Requirements

Found via links from User Stories above.

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| REQ_SYSPILOT_018 | US_SYSPILOT_012, US_SYSPILOT_013 | modified | Add link to US_SYSPILOT_015, specify GitHub Releases |
| REQ_SYSPILOT_019 | US_SYSPILOT_012 | related | No changes needed |
| REQ_SYSPILOT_020 | US_SYSPILOT_013 | related | No changes needed |
| REQ_SYSPILOT_021 | US_SYSPILOT_014 | related | No changes needed |
| REQ_SYSPILOT_022 | US_SYSPILOT_013, US_SYSPILOT_014 | related | No changes needed |
| REQ_SYSPILOT_023 | US_SYSPILOT_012, US_SYSPILOT_013 | related | No changes needed |

### New Requirements (in new file: req_release.rst)

| ID | Title | Links | Priority |
|----|-------|-------|----------|
| REQ_RELEASE_001 | Semantic Versioning | US_SYSPILOT_015 | mandatory |
| REQ_RELEASE_002 | GitHub Release Publication | US_SYSPILOT_015 | mandatory |
| REQ_RELEASE_003 | Release Notes Generation | US_SYSPILOT_015 | mandatory |
| REQ_RELEASE_004 | Pre-Release Validation | US_SYSPILOT_016 | mandatory |
| REQ_RELEASE_005 | Documentation Build Verification | US_SYSPILOT_016 | mandatory |
| REQ_RELEASE_006 | Agent Functionality Testing | US_SYSPILOT_016 | mandatory |
| REQ_RELEASE_007 | GitHub Actions Automation | US_SYSPILOT_015, US_SYSPILOT_016 | high |
| REQ_RELEASE_008 | Release Process Documentation | US_SYSPILOT_017 | medium |

### Conflicts Detected

None - clear separation between user-facing (installation/updates) and maintainer-facing (release creation) requirements.

### Decisions

- **Separate File Structure**: Create `docs/11_requirements/req_release.rst` for maintainer-facing release requirements
- **Naming Convention**: Use `REQ_RELEASE_NNN` prefix for release-specific requirements
- **Domain Separation**: Keep user-facing requirements (install/update) in `req_syspilot.rst`
- **Rationale**: Users don't need to see release validation workflows; maintainers have focused documentation

### Decisions - Finalized

1. **Release Assets**: Git tags only - GitHub automatically creates .zip/.tar.gz of entire repository
2. **Hotfix Process**: Not needed - roll forward only (fix releases get higher version numbers)
3. **Documentation Publishing**: Auto-publish to GitHub Pages via GitHub Action (requires sphinx, sphinx-needs, graphviz)
4. **Security**: Use GitHub's built-in features (automatic checksums, HTTPS delivery). Defer signing and Dependabot to future releases.

### Horizontal Check (MECE)

- [x] No contradictions with existing Requirements (creation vs consumption clearly separated)
- [x] No redundancies (each requirement has distinct focus)
- [x] All new REQs link to User Stories

---

## Level 2: Design

**Status**: ✅ completed

### Impacted Design Elements

Found via links from Requirements above.

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| SPEC_SYSPILOT_007 | REQ_SYSPILOT_018 | modified | Specify GitHub Releases auto-archiving, add link to REQ_RELEASE_002 |

### New Design Elements (in new file: spec_release.rst)

| ID | Title | Links |
|----|-------|-------|
| SPEC_RELEASE_001 | Version Number Format | REQ_RELEASE_001 |
| SPEC_RELEASE_002 | Git Tag Creation | REQ_RELEASE_002 |
| SPEC_RELEASE_003 | Release Notes Structure | REQ_RELEASE_003 |
| SPEC_RELEASE_004 | Validation Checklist | REQ_RELEASE_004, REQ_RELEASE_005, REQ_RELEASE_006 |
| SPEC_RELEASE_005 | GitHub Actions Workflow | REQ_RELEASE_007, REQ_RELEASE_005, REQ_RELEASE_006 |
| SPEC_RELEASE_006 | GitHub Pages Publishing | REQ_RELEASE_005 |
| SPEC_RELEASE_007 | Release Agent & Automation | REQ_RELEASE_003, REQ_RELEASE_008 |

### Conflicts Detected

None - clear separation between release creation and installation/adoption processes.

### Decisions

1. **Release Notes File**: `docs/releasenotes.md` (not CHANGELOG.md)
2. **Release Agent**: Interactive agent `@syspilot.release` to guide maintainer through release process
3. **Release Agent Tasks**:
   - Read merged Change Documents
   - Generate release note entry
   - Commit to `docs/releasenotes.md`
   - Guide version.json update
   - Guide Git tag creation
4. **GitHub Actions Workflow**: `.github/workflows/release.yml` created as part of implementation
5. **Documentation Publishing**: Automated via GitHub Actions to GitHub Pages
6. **Manual Fallback**: Document complete manual process in SPEC_RELEASE_004 checklist

### Horizontal Check (MECE)

- [x] No contradictions with existing Designs (creation vs consumption workflows)
- [x] All new SPECs link to Requirements
- [x] Coverage complete: versioning, tagging, notes, validation, automation, publishing, agent

---

## Final Consistency Check

**Status**: ✅ passed

### Traceability Verification

| User Story | Requirements | Design | Complete? |
|------------|--------------|--------|-----------|
| US_SYSPILOT_015 | REQ_RELEASE_001, REQ_RELEASE_002, REQ_RELEASE_003, REQ_RELEASE_007 | SPEC_RELEASE_001, SPEC_RELEASE_002, SPEC_RELEASE_003, SPEC_RELEASE_005, SPEC_RELEASE_007 | ✅ |
| US_SYSPILOT_016 | REQ_RELEASE_004, REQ_RELEASE_005, REQ_RELEASE_006 | SPEC_RELEASE_004, SPEC_RELEASE_005, SPEC_RELEASE_006 | ✅ |
| US_SYSPILOT_017 | REQ_RELEASE_008, REQ_RELEASE_003 | SPEC_RELEASE_007, SPEC_RELEASE_003 | ✅ |
| US_SYSPILOT_012 | REQ_SYSPILOT_018 (modified) | SPEC_SYSPILOT_007 (modified) | ✅ |

### Cross-Level Consistency

✅ **Level 0 → Level 1**: All User Stories have corresponding Requirements
- US_SYSPILOT_015 (Create Release) → REQ_RELEASE_001-003, 007
- US_SYSPILOT_016 (Validate Quality) → REQ_RELEASE_004-006
- US_SYSPILOT_017 (Release Template) → REQ_RELEASE_008

✅ **Level 1 → Level 2**: All Requirements have corresponding Design specs
- REQ_RELEASE_001-008 → SPEC_RELEASE_001-007
- REQ_SYSPILOT_018 → SPEC_SYSPILOT_007

✅ **Semantic Consistency**: No drift between levels
- User intent (create stable releases) → System behavior (versioned releases with validation) → Implementation (release agent + GitHub Actions)

### MECE Across Levels

✅ **Coverage**: All aspects of release process covered
- Version management: US_015 → REQ_001 → SPEC_001
- Publication: US_015 → REQ_002 → SPEC_002
- Documentation: US_015 → REQ_003 → SPEC_003, SPEC_007
- Quality: US_016 → REQ_004-006 → SPEC_004-006
- Automation: US_015/016 → REQ_007 → SPEC_005
- Template: US_017 → REQ_008 → SPEC_007

✅ **No Overlaps**: Clear separation between concerns
✅ **No Gaps**: Complete release workflow from preparation to publication

### Issues Found

None - All levels complete and consistent.

### Sign-off

- [x] All levels completed (no ⚠️ DEPRECATED markers)
- [x] All conflicts resolved
- [x] Traceability verified
- [x] Ready for implementation

---

## Appendix: Link Discovery Results

```
(empty for now)
```

---

*Generated by syspilot Change Agent*
