# Verification Report: setup-update

**Date**: 2026-03-30  
**Change Proposal**: docs/changes/setup-update.md  
**Status**: ✅ PASSED

## Summary

| Category | Total | Verified | Issues |
|----------|-------|----------|--------|
| User Stories (modified) | 2 | 2 | 0 |
| Requirements (new) | 2 | 2 | 0 |
| Requirements (modified) | 6 | 6 | 0 |
| Design Specs (rewritten) | 2 | 2 | 0 |
| Design Specs (path fixes) | 6 | 6 | 0 |
| Implementation (agent code) | 4 | 4 | 0 |
| Stale paths | — | — | 0 |
| Sphinx build | — | — | 0 |

## Specification Verification

### Level 0: User Stories

**SYSPILOT_US_INST_UPDATE** (status: implemented)
- ✅ AC-2 refined: "methodology agents (change, verify, mece, trace, memory) are replaced with the latest version and project-specific agents (release, implement) are never modified"
- ✅ AC-5 added: "setup agent updates itself first before updating other files"

**SYSPILOT_US_INST_AGNOSTIC** (status: implemented)
- ✅ AC-3 refined: "implement agent is never modified by the update process"
- ✅ AC-5 added: "contain a reminder to customize via @syspilot.change"

### Level 1: Requirements

**New Requirements:**
- ✅ `SYSPILOT_REQ_INST_BOOTSTRAP_SELF` — present, status implemented, 3 ACs
- ✅ `SYSPILOT_REQ_INST_FILE_OWNERSHIP` — present, status implemented, 4 ACs

**Modified Requirements:**
- ✅ `SYSPILOT_REQ_INST_VERSION_UPDATE` — AC-7 (bootstrap) confirmed present
- ✅ `SYSPILOT_REQ_INST_CUSTOM_PRESERVE` — AC-3 references FILE_OWNERSHIP
- ✅ `SYSPILOT_REQ_INST_TEMPLATE_SOURCE` — `syspilot/` paths throughout
- ✅ `SYSPILOT_REQ_INST_NEW_PROJECT` — AC-6 path fixed
- ✅ `SYSPILOT_REQ_INST_ADOPT_EXISTING` — AC-6 path fixed
- ✅ `SYSPILOT_REQ_INST_IMPL_SKELETON` — AC-6 (template banner) present

### Level 2: Design Specs

**Rewritten Specs:**
- ✅ `SYSPILOT_SPEC_INST_UPDATE_PROCESS` — contains "Step 0: Bootstrap Self-Update" with full bootstrap logic
- ✅ `SYSPILOT_SPEC_INST_FILE_OWNERSHIP` — 3 explicit ownership categories (methodology, project, user)

**Path Fixes:**
- ✅ `SYSPILOT_SPEC_INST_CURL_BOOTSTRAP` — uses `syspilot/` paths
- ✅ `SYSPILOT_SPEC_INST_SETUP_AGENT` — uses `syspilot/` paths
- ✅ `SYSPILOT_SPEC_INST_VERSION_MARKER` — uses `syspilot/` paths
- ✅ `SYSPILOT_SPEC_INST_TEMPLATE_LAYOUT` — uses `syspilot/` paths
- ✅ `SYSPILOT_SPEC_INST_RELEASE_STRUCTURE` — uses `syspilot/` paths
- ✅ `SYSPILOT_SPEC_INST_SELF_INSTALL` — uses `syspilot/` paths

## Implementation Verification

### Bootstrap Self-Update (SPEC_INST_UPDATE_PROCESS → Setup Agent Section 7)

| Check | Spec Requirement | Agent Implementation | Status |
|-------|-----------------|---------------------|--------|
| Step 0 exists | "Step 0: Bootstrap Self-Update" | `### Step 0: Bootstrap Self-Update` at line 280 | ✅ |
| Fetch remote | Fetch setup agent from GitHub main | `Invoke-WebRequest -Uri $setupUrl` | ✅ |
| Compare | Compare with local copy | `if ($remoteSetup -ne $localSetup)` | ✅ |
| Replace + abort | Replace and ask user to re-invoke | `Set-Content ... ; "re-invoke @syspilot.setup"` | ✅ |
| Prompt update | Also update setup prompt | Separate block updates prompt file | ✅ |

### File Ownership Tables (SPEC_INST_FILE_OWNERSHIP → Setup Agent Section 7, Step 4)

| Check | Spec Requirement | Agent Implementation | Status |
|-------|-----------------|---------------------|--------|
| Methodology → REPLACE | 18 files listed in spec | 16-row table under "Methodology-Owned → REPLACE always" | ✅ |
| Setup → skip | Already updated in Step 0 | "Setup agent → already updated in Step 0 (skip)" | ✅ |
| Project → SKIP | release + implement agents & prompts | 4 bullets under "Project-Owned → SKIP (never modify)" | ✅ |
| User → NEVER | docs/**, conf.py, copilot-instructions | Listed under "User-Owned → NEVER touch" | ✅ |

### Fresh Install (SPEC_INST_SETUP_AGENT → Setup Agent Section 4)

| Check | Spec Requirement | Agent Implementation | Status |
|-------|-----------------|---------------------|--------|
| All agents copied | On fresh install, ALL agents including release/implement | Table in Step 3 shows `agents/syspilot.*.agent.md → Copy all` | ✅ |
| Template note | Generic templates with customization reminder | Note: "project-owned agents are generic templates" + banner text | ✅ |
| First Install Exception | Documented in SPEC_INST_UPDATE_PROCESS | Agent Section 4 copies all; Section 7 protects on update | ✅ |

### Template Banners (SPEC_INST_TEMPLATE_LAYOUT → Product Agents)

| Check | File | Banner Present | Status |
|-------|------|---------------|--------|
| Release agent | `syspilot/agents/syspilot.release.agent.md` line 11 | `⚠️ **This is the generic syspilot template.**` | ✅ |
| Implement agent | `syspilot/agents/syspilot.implement.agent.md` line 11 | `⚠️ **This is the generic syspilot template.**` | ✅ |

### Agent Sync

| Check | Status |
|-------|--------|
| `syspilot/agents/syspilot.setup.agent.md` = `.github/agents/syspilot.setup.agent.md` | ✅ SYNCED |

### Spec Status Verification

| File | All `:status: implemented` | Status |
|------|---------------------------|--------|
| `docs/syspilot/design/spec_setup.rst` | 8/8 specs → implemented | ✅ |
| `docs/syspilot/requirements/req_installation.rst` | 13/13 reqs → implemented | ✅ |
| `docs/syspilot/userstories/us_installation.rst` | 6/6 stories → implemented | ✅ |

### Stale Reference Check
- ✅ No `templates/` source-path references in spec_setup.rst (only correct `.syspilot/templates/` installed-path refs)

### Sphinx Build
- ✅ 0 errors, 0 warnings (`sphinx-build -W` passes)

## Traceability Matrix

| Requirement | Design | Implementation | Status |
|-------------|--------|----------------|--------|
| REQ_INST_BOOTSTRAP_SELF | SPEC_INST_UPDATE_PROCESS | Setup Agent §7 Step 0 | ✅ |
| REQ_INST_FILE_OWNERSHIP | SPEC_INST_FILE_OWNERSHIP | Setup Agent §7 Step 4 | ✅ |
| REQ_INST_VERSION_UPDATE | SPEC_INST_UPDATE_PROCESS | Setup Agent §7 Steps 1-6 | ✅ |
| REQ_INST_CUSTOM_PRESERVE | SPEC_INST_FILE_OWNERSHIP | Setup Agent §7 "Project-Owned → SKIP" | ✅ |
| REQ_INST_IMPL_SKELETON | SPEC_INST_TEMPLATE_LAYOUT | Template banners in release/implement | ✅ |

## Conclusion

All setup-update changes verified across all 3 spec levels and agent code implementation. Bootstrap self-update, file ownership model, template banners, path fixes, and spec statuses are all correct. Sphinx build passes with zero warnings.
