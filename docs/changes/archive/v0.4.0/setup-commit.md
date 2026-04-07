# Change Document: setup-commit

**Status**: implemented
**Branch**: feature/setup-commit
**Created**: 2026-04-07
**Author**: @syspilot.change
**Issue**: #11

---

## Summary

After a successful fresh install or adoption, the Setup Agent leaves all placed files unstaged. The user must manually `git add` and commit everything, which breaks the flow and is error-prone. This change adds an auto-commit step to the Setup Agent's install workflow (Sections 6/7) to stage and commit all syspilot-placed files with a descriptive message after successful validation.

Note: The UPDATE workflow already commits (v0.3.1, Step 7). This change targets the FRESH INSTALL and ADOPTION paths only.

---

## Level 0: User Stories

**Status**: ✅ completed

### Modified User Stories
- SYSPILOT_US_INST_NEW_PROJECT: +AC-6 (commit all newly created files after successful install)
- SYSPILOT_US_INST_ADOPT_EXISTING: +AC-6 (commit all added syspilot files after successful adoption, handle pre-existing changes gracefully)

### Decisions
- D-1: No new User Story — auto-commit is part of a complete install, not a separate need
- D-2: UPDATE path already covered by v0.3.1 (INST_UPDATE AC-8) — not in scope
- D-3: ADOPT_EXISTING gets its own wording ("handle pre-existing changes gracefully") because adopted projects may already have staged files

---

## Level 1: Requirements

**Status**: ✅ completed

### New Requirements
- SYSPILOT_REQ_INST_INSTALL_COMMIT: Post-Install Git Commit — new because no REQ covered the install-time baseline commit

### Decisions
- D-4: One new REQ covers both fresh-install and adoption paths (same mechanism, different commit message)
- D-5: UPDATE mode explicitly excluded (AC-6 defers to SYSPILOT_REQ_INST_UPDATE_BRANCH) — separation enforced in `:links:`
- D-6: Commit is confirmation-gated (AC-3: user confirms, not just notified) — interactive setup agent pattern
- D-7: Git-not-initialized / missing identity edge case deferred to Level 2 SPEC
- D-8: Commit message format: `chore: install syspilot v{version}` (fresh install) / `chore: adopt syspilot v{version}` (adoption) — aligns both paths, resolves US-level asymmetry (MECE L0 minor finding)

---

## Level 2: Design

**Status**: ✅ completed

### New Design Specs
- SYSPILOT_SPEC_INST_INSTALL_COMMIT: Post-Install Git Commit — full design (git detect → pre-existing check → confirm → commit)

### Modified Design Specs
- SYSPILOT_SPEC_INST_SETUP_AGENT: +Section 6 reference to SYSPILOT_SPEC_INST_INSTALL_COMMIT; +link to SYSPILOT_REQ_INST_INSTALL_COMMIT

### Decisions
- D-9: Graceful skip (not abort) for pre-existing changes — aligns REQ AC-4 and SPEC Option B
- D-10: install vs adopt message determined by docs/conf.py detection in Section 3 (pre-existing file)
- D-11: Git-not-initialized is a graceful skip with informational message (no error exit)
- D-12: Missing git identity: surface error message with manual recovery instructions, skip commit
- D-13: SYSPILOT_SPEC_INST_FILE_OWNERSHIP added to INSTALL_COMMIT links (file list reference)
