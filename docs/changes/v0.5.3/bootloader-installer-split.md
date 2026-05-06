# Change Document: bootloader-installer-split

**Status**: review
**Branch**: feature/bootloader-installer-split
**Created**: 2026-05-05
**Author**: Change Manager

---

## Summary

Split the Setup Agent into two components: a lightweight **Bootloader** (`syspilot.setup.agent.md`)
and a full **Installer** (`syspilot.installer.agent.md`). The Bootloader fetches the latest
Installer from upstream (`main` branch, GitHub raw URL) on every run and invokes it as a subagent.
This breaks the self-referential bootstrap cycle where the old version installs the new version.
`syspilot/bootstrap.json` is server-side only and never stored on the customer system.

---

## Intent Gate

**CR contained implementation details** — underlying intent extracted and confirmed:

> Decouple the installation UX from the installation logic. The Bootloader ensures that
> every setup run uses the current version of the installer, regardless of what version
> was previously installed.

Proceeding in non-interactive mode as requested by PM.

---

## Impact Analysis

**Scope of change:**

- `docs/syspilot/userstories/us_setup_engineer.rst` — extend with bootstrap user story
- `docs/syspilot/requirements/req_setup_engineer.rst` — extend with 4 new requirements
- `docs/syspilot/design/spec_setup_engineer.rst` — modify SOUL and WORKFLOW specs
- `docs/syspilot/design/spec_installer.rst` — new file (Installer spec)
- `syspilot/agents/syspilot.setup.agent.md` — replace with Bootloader logic
- `syspilot/agents/syspilot.installer.agent.md` — new file (today's Setup Agent, renamed)
- `syspilot/prompts/syspilot.installer.prompt.md` — new file (today's Setup Prompt, renamed)
- `syspilot/bootstrap.json` — new server-side manifest file

---

## Level 0: User Stories

**Status**: ✅ completed

### New User Stories

| ID | Title | Priority |
|----|-------|----------|
| SYSP_US_INST_BOOTSTRAP | As a developer, I want Setup to always use the current Installer regardless of locally installed version | mandatory |

### Decisions

- `SYSP_US_INST_BOOTSTRAP` links to `SYSP_US_SETUP` as parent

---

## Level 1: Requirements

**Status**: ✅ completed

### New Requirements

| ID | Title | Links | Priority |
|----|-------|-------|----------|
| SYSP_REQ_SETUP_BOOTLOADER_FETCH | Bootloader SHALL fetch Installer from upstream on every run | SYSP_US_INST_BOOTSTRAP | mandatory |
| SYSP_REQ_SETUP_BOOTLOADER_INVOKE | Bootloader SHALL invoke Installer as subagent | SYSP_US_INST_BOOTSTRAP | mandatory |
| SYSP_REQ_SETUP_BOOTLOADER_VERSION | Bootloader SHALL stop with user-visible error if bootstrap_version is higher than supported | SYSP_US_INST_BOOTSTRAP | mandatory |
| SYSP_REQ_SETUP_INSTALLER_NOT_USER_INVOCABLE | Installer SHALL NOT be user-invocable | SYSP_US_INST_BOOTSTRAP | mandatory |

---

## Level 2: Design

**Status**: ✅ completed

### Modified Specs

| ID | File | Change |
|----|------|--------|
| SYSP_SPEC_SETUP_SOUL | spec_setup_engineer.rst | Describe Bootloader role |
| SYSP_SPEC_SETUP_WORKFLOW | spec_setup_engineer.rst | Bootloader workflow: fetch manifest → validate version → fetch Installer → invoke as subagent |

### New Specs

| ID | File | Links |
|----|------|-------|
| SYSP_SPEC_INSTALLER_SOUL | spec_installer.rst | SYSP_REQ_SETUP_DUTIES |
| SYSP_SPEC_INSTALLER_FRONTMATTER | spec_installer.rst | SYSP_REQ_SETUP_INSTALLER_NOT_USER_INVOCABLE |
| SYSP_SPEC_INSTALLER_WORKFLOW | spec_installer.rst | SYSP_REQ_SETUP_WORKFLOW |

---

## Implementation

**Status**: ✅ completed

### Files to create/modify

- [x] `docs/syspilot/userstories/us_setup_engineer.rst` — add SYSP_US_INST_BOOTSTRAP
- [x] `docs/syspilot/requirements/req_setup_engineer.rst` — add 4 new requirements
- [x] `docs/syspilot/design/spec_installer.rst` — new file
- [x] `docs/syspilot/design/spec_setup_engineer.rst` — modify SOUL and WORKFLOW
- [x] `syspilot/agents/syspilot.setup.agent.md` — replace with Bootloader
- [x] `syspilot/agents/syspilot.installer.agent.md` — new (today's Setup Agent)
- [x] `syspilot/prompts/syspilot.installer.prompt.md` — new (today's Setup Prompt)
- [x] `syspilot/bootstrap.json` — new server-side manifest

---

## Quality Checks

**Status**: ✅ completed

- [x] MECE check (final) — passed (blocking findings fixed)
- [x] Trace check — passed

---

## Documentation

**Status**: ✅ completed

---

## Engineer Log

| Timestamp | Engineer | Action | Result |
|-----------|----------|--------|--------|
| 2026-05-05 | CM | CR received from PM | Accepted, branch created |
| 2026-05-05 | CM | Change document created | `docs/changes/v0.5.3/bootloader-installer-split.md` |
| 2026-05-05 | System Designer | Design completed | spec_setup_engineer.rst updated, spec_installer.rst created |
| 2026-05-05 | Dev Engineer | Implementation completed | All 8 files created/modified |
| 2026-05-05 | MECE | MECE check passed | Blocking findings fixed, all levels pass |
| 2026-05-05 | Trace | Trace check passed | All links resolve, coverage complete |
| 2026-05-05 | Docu Engineer | Documentation updated | Change doc and release notes updated |
