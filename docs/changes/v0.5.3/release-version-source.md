# Change Document: release-version-source

**Status**: in-progress
**Branch**: feature/release-version-source
**Created**: 2026-05-01
**Author**: syspilot.cm

---

## Summary

The Release Agent bumps the `version:` field in `syspilot/agents/syspilot.setup.agent.md`
(product source) as the single source of truth for the version. The subsequent Setup
Agent run propagates this to the installed instance. `syspilot/version.json` is
deleted as redundant. Release Agent spec is corrected accordingly.

---

## Change Request (from PM)

> **Intent (WHAT):**
> The Release Agent shall bump the version in the Setup Agent frontmatter
> (`version:` field in `syspilot/agents/syspilot.setup.agent.md`) instead of
> `version.json`. The `version.json` file shall be deleted.
>
> **Motivation (WHY):**
> The version's single source of truth is the Setup Agent's `version:` frontmatter
> field — the Setup Agent uses it for mode detection (fresh install vs. update).
> The `version.json` is redundant and was created by mistake. The Release Agent
> spec currently references it incorrectly.
>
> **Acceptance Criteria:**
> 1. Release Agent SHALL bump the `version:` field in `syspilot/agents/syspilot.setup.agent.md` (product) instead of version.json
> 2. The file `syspilot/version.json` SHALL be deleted
> 3. The Release Agent spec (SYSP_SPEC_RELEASE) and agent file SHALL reference Setup Agent frontmatter as the version location
>
> **Mode:** autonomous
>
> **Intent Gate clarification:** `.github/` is Setup Agent territory. Release Agent
> bumps the product file (`syspilot/agents/syspilot.setup.agent.md`); the subsequent
> Setup Agent run propagates to `.github/` (installed instance). This is the correct
> process — Release Agent does not directly modify `.github/`.

---

## Impact Analysis (CM)

**Performed**: 2026-05-01
**Method**: `get_need_links.py <id> --direction in --depth 1` from SYSP_US_RELEASE, then depth 1 from relevant REQs.

**From SYSP_US_RELEASE (direct REQs):**
```
SYSP_REQ_RELEASE_SOUL, SYSP_REQ_RELEASE_DUTIES, SYSP_REQ_RELEASE_WORKFLOW,
SYSP_REQ_RELEASE_FRONTMATTER
```

**From Release REQs (direct SPECs):**
```
SYSP_REQ_RELEASE_DUTIES   → SYSP_SPEC_RELEASE_DUTIES
SYSP_REQ_RELEASE_WORKFLOW → SYSP_SPEC_RELEASE_WORKFLOW
```

**In-scope elements:**
- SYSP_US_RELEASE
- SYSP_REQ_RELEASE_DUTIES, SYSP_REQ_RELEASE_WORKFLOW
- SYSP_SPEC_RELEASE_DUTIES, SYSP_SPEC_RELEASE_WORKFLOW

**Out of scope:** SOUL (character, not affected). FRONTMATTER (not behavioral).

**Agent file in scope:**
- `syspilot/agents/syspilot.release.agent.md`

**File deletion in scope:**
- `syspilot/version.json`

---

## Process Log

| Step | Agent | Status | Commit | Notes |
|------|-------|--------|--------|-------|
| Branch created | CM | ✅ | — | feature/release-version-source |
| Impact Analysis | CM | ✅ | — | See section above |
| Change Document | CM | ✅ | — | This file |
| Design (L0) | syspilot.design | ✅ | 9a59a80 | — |
| Design (L1) | syspilot.design | ✅ | c431aac | — |
| Design (L2) | syspilot.design | ✅ | d82b573 | — |
| Implement | syspilot.implement | ✅ | a9338e4 | — |
| Verify | syspilot.verify | ⏳ | — | — |
| PM Approval | PM | ⏳ | — | — |
| Merged | CM | ⏳ | — | — |

---

## Level 0: User Stories

**Status**: ✅ done

### Impacted User Stories

| ID | Title | Impact | Notes |
|----|-------|--------|-------|
| `SYSP_US_RELEASE` | Release Engineer Agent | modified | Version source = Setup Agent frontmatter |

### Designer Section

**Decision:** The Context paragraph of `SYSP_US_RELEASE` previously stated that the Release
Engineer reads "version file location" from project-specific configuration. This was inaccurate
and implied `version.json`. Updated Context to explicitly state the version is maintained in
the `version:` frontmatter field of `syspilot/agents/syspilot.setup.agent.md` and that the
Release Engineer bumps that field directly.

**ACs unchanged:** All four ACs describe behavior (squash-merge, semver, validation, archival)
that does not reference the version file location — no AC update required at L0.

---

## Level 1: Requirements

**Status**: ✅ done

### Impacted Requirements

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| `SYSP_REQ_RELEASE_DUTIES` | `SYSP_US_RELEASE` | modified | Version bump target updated |
| `SYSP_REQ_RELEASE_WORKFLOW` | `SYSP_US_RELEASE` | modified | Version bump step references Setup Agent frontmatter |

### Designer Section

**SYSP_REQ_RELEASE_DUTIES — AC-1 updated:**
The original AC-1 ("Release Engineer can bump versions following semantic versioning") was
vague about the target file. Updated to explicitly require the Release Engineer to bump the
`version:` field in `syspilot/agents/syspilot.setup.agent.md`.

**SYSP_REQ_RELEASE_WORKFLOW — AC-2 updated:**
The original AC-2 ("Release Engineer reads project-specific release decisions") implied a
configurable version file location. Updated to specify that the Release Engineer reads the
current version from the `version:` field in `syspilot/agents/syspilot.setup.agent.md` and
bumps it there. This fixes the ambiguity and makes the version source explicit at requirement level.

---

## Level 2: Design

**Status**: ✅ done

### Impacted Design Elements

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| `SYSP_SPEC_RELEASE_DUTIES` | `SYSP_REQ_RELEASE_DUTIES` | modified | — |
| `SYSP_SPEC_RELEASE_WORKFLOW` | `SYSP_REQ_RELEASE_WORKFLOW` | modified | version.json → Setup Agent frontmatter |

### Designer Section

**SYSP_SPEC_RELEASE_DUTIES — Duty #2 updated:**
Changed "Bump version in `version.json`" to "Bump the `version:` field in
`syspilot/agents/syspilot.setup.agent.md`". This is the single source of truth;
`version.json` is deleted.

**SYSP_SPEC_RELEASE_WORKFLOW — Steps 2 and 4 updated:**
- Step 2 was "Read Decisions (version file, tag format…)". Replaced with "Read Current
  Version — Read the `version:` field from `syspilot/agents/syspilot.setup.agent.md`".
  Tag format and release notes location are fixed conventions, not runtime decisions;
  removing the vague "read decisions" framing makes the workflow concrete and unambiguous.
- Step 4 updated to "Bump the `version:` field in `syspilot/agents/syspilot.setup.agent.md`
  to the new version" — explicit file and field reference.

---

## Final Consistency Check

**Status**: ✅ done

### Traceability Verification

| Chain | Status |
|-------|--------|
| SYSP_US_RELEASE → SYSP_REQ_RELEASE_DUTIES → SYSP_SPEC_RELEASE_DUTIES | ✅ |
| SYSP_US_RELEASE → SYSP_REQ_RELEASE_WORKFLOW → SYSP_SPEC_RELEASE_WORKFLOW | ✅ |

All three levels consistently describe the version bump targeting the `version:` field in
`syspilot/agents/syspilot.setup.agent.md`. No orphaned references to `version.json` remain
in the spec hierarchy. `version.json` deletion is an implementation concern (not spec-level).

---

## Sign-off

- [ ] Design approved by user
- [ ] Implementation complete
- [ ] Verify passed
- [ ] PM approval received
- [ ] Merged to development
