# UAT Validation: bootloader-installer-split

**Date**: 2026-05-05
**Change Document**: [docs/changes/v0.5.3/bootloader-installer-split.md](bootloader-installer-split.md)
**Branch**: feature/bootloader-installer-split
**Status**: ⏳ PENDING

---

## Scope

This document covers User Acceptance Testing for the Bootloader/Installer split.
The Bootloader (`syspilot.setup.agent.md`) replaces the monolithic Setup Agent as
the user-invocable entry point. The Installer (`syspilot.installer.agent.md`) is
the full installation engine, internal-only.

---

## Test Coverage Summary

| Req ID | Description | Scenarios | Coverage |
|--------|-------------|-----------|---------|
| SYSP_REQ_SETUP_BOOTLOADER_FETCH | Bootloader fetches Installer from upstream | T-1, T-2, T-3 | AC-1, AC-2, AC-3 |
| SYSP_REQ_SETUP_BOOTLOADER_VERSION | Bootloader validates bootstrap_version | T-4, T-5 | AC-1, AC-2, AC-3 |
| SYSP_REQ_SETUP_BOOTLOADER_INVOKE | Bootloader invokes Installer as subagent | T-6, T-7 | AC-1, AC-2 |
| SYSP_REQ_SETUP_INSTALLER_NOT_USER_INVOCABLE | Installer is not user-invocable | T-8, T-9 | AC-1, AC-2 |
| SYSP_US_INST_BOOTSTRAP | bootstrap.json stays server-side | T-10 | — |

---

## Test Scenarios

### T-1 — Bootloader fetches manifest from canonical GitHub URL

**Requirement**: SYSP_REQ_SETUP_BOOTLOADER_FETCH AC-1  
**Design ref**: SYSP_SPEC_SETUP_BOOTLOADER_SOUL (Step 1 — Fetch Manifest)

| Field | Value |
|-------|-------|
| **Precondition** | Network access available; `syspilot.setup.agent.md` is the Bootloader |
| **Action** | User invokes the Setup Agent (Bootloader) in a VS Code Copilot session |
| **Expected** | Agent fetches `https://raw.githubusercontent.com/enthali/syspilot/main/syspilot/bootstrap.json` before any other step |
| **Pass criterion** | Manifest JSON is read; `bootstrap_version` and `entry_point` keys are present |
| **Fail criterion** | Agent proceeds without reading manifest, or reads from a local/different URL |

---

### T-2 — Bootloader resolves Installer URL from entry_point field

**Requirement**: SYSP_REQ_SETUP_BOOTLOADER_FETCH AC-2  
**Design ref**: SYSP_SPEC_SETUP_BOOTLOADER_SOUL (Step 3 — Fetch Installer)

| Field | Value |
|-------|-------|
| **Precondition** | Manifest fetched with `entry_point: "syspilot/agents/syspilot.installer.agent.md"` |
| **Action** | Bootloader constructs fetch URL from `entry_point` |
| **Expected** | Installer fetched from `https://raw.githubusercontent.com/enthali/syspilot/main/syspilot/agents/syspilot.installer.agent.md` |
| **Pass criterion** | URL is exactly `https://raw.githubusercontent.com/enthali/syspilot/main/<entry_point>` |
| **Fail criterion** | Hardcoded URL ignoring `entry_point`, or wrong base URL |

---

### T-3 — Bootloader fetches Installer on every run (no caching)

**Requirement**: SYSP_REQ_SETUP_BOOTLOADER_FETCH AC-3  
**Design ref**: SYSP_SPEC_SETUP_BOOTLOADER_SOUL (Step 1)

| Field | Value |
|-------|-------|
| **Precondition** | Bootloader has been run at least once before |
| **Action** | Invoke Bootloader a second time |
| **Expected** | Agent fetches manifest and Installer again from GitHub — does not reuse a previously fetched copy |
| **Pass criterion** | Each invocation performs fresh HTTP fetch (no local cache file written or read) |
| **Fail criterion** | Bootloader reads Installer from a local `.github/` path or session cache |

---

### T-4 — Bootloader stops on unsupported bootstrap_version (happy-path: version = 1)

**Requirement**: SYSP_REQ_SETUP_BOOTLOADER_VERSION AC-1, AC-2  
**Design ref**: SYSP_SPEC_SETUP_BOOTLOADER_SOUL (Step 2 — Validate Version)

| Field | Value |
|-------|-------|
| **Precondition** | Manifest returns `{"bootstrap_version": 1, "entry_point": "..."}` |
| **Action** | Bootloader reads `bootstrap_version` |
| **Expected** | Version 1 is within supported range; Bootloader proceeds to Step 3 |
| **Pass criterion** | No error message; execution continues to Installer fetch |
| **Fail criterion** | False-positive error displayed for supported version |

---

### T-5 — Bootloader stops with user-visible error on bootstrap_version > 1

**Requirement**: SYSP_REQ_SETUP_BOOTLOADER_VERSION AC-2, AC-3  
**Design ref**: SYSP_SPEC_SETUP_BOOTLOADER_SOUL (Step 2 — Validate Version)

| Field | Value |
|-------|-------|
| **Precondition** | Manifest returns `{"bootstrap_version": 2, "entry_point": "..."}` (simulated by editing agent prompt with a mock manifest) |
| **Action** | Bootloader reads `bootstrap_version` = 2 |
| **Expected** | Bootloader displays a user-visible error and stops; does NOT proceed to Installer fetch |
| **Pass criterion** | Error message is shown; message instructs user to update their Bootloader; no further steps executed |
| **Fail criterion** | Execution continues past version gate; silent failure; no instruction to update |

---

### T-6 — Bootloader invokes Installer as subagent

**Requirement**: SYSP_REQ_SETUP_BOOTLOADER_INVOKE AC-1  
**Design ref**: SYSP_SPEC_SETUP_BOOTLOADER_SOUL (Step 4 — Invoke Installer)

| Field | Value |
|-------|-------|
| **Precondition** | Manifest fetched successfully; `bootstrap_version` = 1; Installer content fetched |
| **Action** | Bootloader reaches Step 4 of its workflow |
| **Expected** | Bootloader calls `runSubagent()` with the fetched Installer content |
| **Pass criterion** | Installer begins executing (installation workflow appears in output); Bootloader has handed off control |
| **Fail criterion** | Bootloader attempts to run the installation logic itself inline |

---

### T-7 — Bootloader passes user context to Installer subagent

**Requirement**: SYSP_REQ_SETUP_BOOTLOADER_INVOKE AC-2  
**Design ref**: SYSP_SPEC_SETUP_BOOTLOADER_SOUL (Step 4)

| Field | Value |
|-------|-------|
| **Precondition** | User provides install parameters (e.g., source path or GitHub repo URL) before invoking |
| **Action** | Bootloader invokes Installer subagent |
| **Expected** | Installer subagent receives the original user message / context |
| **Pass criterion** | Installer asks no redundant questions about information already provided to the Bootloader |
| **Fail criterion** | Installer starts from scratch, re-prompting for already-supplied context |

---

### T-8 — Installer frontmatter declares user-invocable: false

**Requirement**: SYSP_REQ_SETUP_INSTALLER_NOT_USER_INVOCABLE AC-1  
**Design ref**: SYSP_SPEC_INSTALLER_FRONTMATTER

| Field | Value |
|-------|-------|
| **Precondition** | `syspilot/agents/syspilot.installer.agent.md` exists |
| **Action** | Inspect the YAML frontmatter of `syspilot/agents/syspilot.installer.agent.md` |
| **Expected** | Field `user-invocable: false` is present |
| **Pass criterion** | `user-invocable: false` present in frontmatter |
| **Fail criterion** | Field absent, set to `true`, or file has no frontmatter |

---

### T-9 — Installer documentation states it is invoked by Bootloader only

**Requirement**: SYSP_REQ_SETUP_INSTALLER_NOT_USER_INVOCABLE AC-2  
**Design ref**: SYSP_SPEC_INSTALLER_SOUL

| Field | Value |
|-------|-------|
| **Precondition** | `syspilot/agents/syspilot.installer.agent.md` exists |
| **Action** | Read the Soul / description section of `syspilot.installer.agent.md` |
| **Expected** | Documentation clearly states the agent is invoked by Bootloader only and is not user-invocable |
| **Pass criterion** | Soul or description contains explicit statement that user direct invocation is not supported |
| **Fail criterion** | No such statement; agent could be mistaken for a user-facing agent |

---

### T-10 — bootstrap.json is NOT copied to customer system during installation

**Requirement**: SYSP_US_INST_BOOTSTRAP (constraint: server-side only manifest)  
**Design ref**: Change Document summary

| Field | Value |
|-------|-------|
| **Precondition** | Bootloader + Installer complete a fresh install on a test repository |
| **Action** | Inspect the files written to the target repository |
| **Expected** | `syspilot/bootstrap.json` does NOT appear in the target repository |
| **Pass criterion** | No `bootstrap.json` found anywhere in the installed `.github/` or `syspilot/` directory of the target repo |
| **Fail criterion** | `bootstrap.json` is present in the customer repository after installation |

---

## Testability Notes

| Scenario | Testability | Notes |
|----------|-------------|-------|
| T-1 | ✅ Directly observable | Agent chat output shows fetch step |
| T-2 | ✅ Directly observable | URL logged in agent reasoning |
| T-3 | ✅ Testable by re-running | Verify no local cache file created |
| T-4 | ✅ Directly observable | Normal happy-path run |
| T-5 | ⚠️ Requires mock | `bootstrap_version: 2` is not live; must simulate by modifying agent prompt in a test session |
| T-6 | ✅ Observable via output | Installer workflow steps appear after Bootloader handoff |
| T-7 | ✅ Observable via output | Installer does not re-prompt for already-supplied context |
| T-8 | ✅ Static file check | Inspect YAML frontmatter directly |
| T-9 | ✅ Static file check | Read Soul section of agent file |
| T-10 | ✅ File system check | Run install, then `Get-ChildItem -Recurse bootstrap.json` |

---

## Conclusion

10 test scenarios covering all 7 acceptance criteria across 4 requirements.
T-5 requires a simulated manifest (mock `bootstrap_version: 2`) since the live manifest
will always carry version 1 at this time — this is a known testability constraint.

**Status**: ⏳ PENDING — awaiting test execution
