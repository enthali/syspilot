# Change Document: agent-files-conformance-setup-installer

**Status**: in-progress
**Branch**: feature/agent-files-conformance-setup-installer
**Created**: 2026-05-07
**Author**: Change Manager

---

## Summary

Top-to-bottom conformance refactor for the Setup (Bootloader) and Installer agents.
Their Duties sections were written as verbatim workflow steps (procedural execution
sequences), violating the new `SYSP_REQ_AGENT_ARCH_DUTIES` definition which requires
Duties to express accountability and outcomes, distinct from the Workflow's execution
steps (Mutual Exclusion constraint). This CR rewrites Duties across all four spec
levels to express *what each agent is accountable for*, not *how* it does it.
The Workflow sections and agent behaviors are unchanged.

---

## Impact Analysis Results

**Impact tool run:** 2026-05-07, from SYSP_US_SETUP + SYSP_US_INST_BOOTSTRAP

| ID | Level | Type | Change |
|----|-------|------|--------|
| SYSP_US_SETUP | L0 | story | review — US AC alignment |
| SYSP_US_INST_BOOTSTRAP | L0 | story | review — US AC alignment |
| SYSP_REQ_SETUP_BOOTLOADER_DUTIES | L1 | req | rewrite ACs as accountability statements |
| SYSP_REQ_INSTALLER_DUTIES | L1 | req | rewrite ACs as accountability statements |
| SYSP_SPEC_SETUP_DUTIES | L2 | spec | rewrite duties from workflow steps → accountability |
| SYSP_SPEC_INSTALLER_DUTIES | L2 | spec | rewrite duties from workflow steps → accountability |
| syspilot/agents/syspilot.setup.agent.md | product | agent | rewrite Duties section |
| syspilot/agents/syspilot.installer.agent.md | product | agent | rewrite Duties section |

**Not in scope (Workflow/Soul/Frontmatter unchanged):**
- SYSP_SPEC_SETUP_WORKFLOW, SYSP_SPEC_INSTALLER_WORKFLOW
- SYSP_SPEC_SETUP_SOUL, SYSP_SPEC_INSTALLER_SOUL, SYSP_SPEC_INSTALLER_SKILL_MUTEX
- All SYSP_REQ_*_WORKFLOW elements

---

## Duties Redesign

### Bootloader Duties (accountability-based)

The Bootloader is accountable for:
1. **Upstream Delivery** — delivering an always-current Installer from upstream on every invocation
2. **Version Safety** — enforcing manifest version compatibility; blocking on unsupported versions
3. **Installation Delegation** — delegating all installation work to the Installer without performing any installation directly

### Installer Duties (accountability-based)

The Installer is accountable for:
1. **Environment Readiness** — verifying all required dependencies before installation
2. **Correct Installation** — placing all syspilot product files in correct locations
3. **Customization Preservation** — preserving `tools:` values during updates; alerting users to re-apply other customizations
4. **Project Configuration** — Sphinx configuration and initial RST structure setup
5. **Installation Validation** — verifying completed installation via sphinx-build
6. **Traceability** — creating a baseline Git commit after every successful installation

### ME check

Bootloader Duties (upstream/version/delegation) and Installer Duties (environment/install/preserve/configure/validate/commit) are fully disjoint — no behavioral item appears in both.

---

## Quality Gates

- [ ] Sphinx build: clean (0 warnings, 0 errors)
- [ ] QM CLEARED
- [ ] PM Merge Approval ⏳

---

## Traceability

No new spec IDs. Modified: SYSP_REQ_SETUP_BOOTLOADER_DUTIES, SYSP_REQ_INSTALLER_DUTIES,
SYSP_SPEC_SETUP_DUTIES, SYSP_SPEC_INSTALLER_DUTIES, plus product agent files.
