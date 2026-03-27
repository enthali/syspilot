# Change Document: prod-inst-instance

**Status**: approved
**Branch**: feature/product-instance
**Created**: 2026-03-20
**Updated**: 2026-03-27
**Author**: Georg Doll
**Sequence**: 3 of 3

---

## Summary

Build the Instance spec tree for syspilot itself. Instance specs describe how syspilot
uses its own toolkit — the project-specific decisions that every consumer will also make.
Focus on the two agents that are always project-specific: **Release** and **Implement**.

---

## Decisions

1. **Instance scope**: Only agents that are "customized" per project — Release and Implement
2. **Not instance-scoped**: Change, MECE, Trace — these ARE the methodology, not project-specific
3. **Scaffolding deferred**: Setup Agent won't scaffold instance dirs for customers yet (later release)
4. **Naming**: `INST_SYSPILOT_US_*`, `INST_SYSPILOT_REQ_*`, `INST_SYSPILOT_SPEC_*`
5. **Location**: `docs/inst/syspilot/userstories/`, `docs/inst/syspilot/requirements/`, `docs/inst/syspilot/design/`

## Level 0: User Stories

### New Instance User Stories

- `INST_SYSPILOT_US_REL_OWN_RELEASE`: Release syspilot Using Our Own Process
- `INST_SYSPILOT_US_IMPL_OWN_AGENTS`: Implement syspilot Agents as Product Artifacts

## Level 1: Requirements

### From INST_SYSPILOT_US_REL_OWN_RELEASE

- `INST_SYSPILOT_REQ_REL_VERSION_FILE`: Version File Location
- `INST_SYSPILOT_REQ_REL_GITHUB_PUBLISH`: GitHub Release Publication
- `INST_SYSPILOT_REQ_REL_NOTES_FORMAT`: Release Notes Format
- `INST_SYSPILOT_REQ_REL_CHANGE_ARCHIVE`: Change Document Archival
- `INST_SYSPILOT_REQ_REL_CI_PIPELINE`: CI/CD Pipeline

### From INST_SYSPILOT_US_IMPL_OWN_AGENTS

- `INST_SYSPILOT_REQ_IMPL_WRITE_BOUNDARY`: Implement Agent Write Boundary
- `INST_SYSPILOT_REQ_IMPL_SETUP_SYNC`: Setup Agent Synchronization

## Level 2: Design Specs

### spec_release.rst

- `INST_SYSPILOT_SPEC_REL_AGENT_CONFIG`: Release Agent Configuration
- `INST_SYSPILOT_SPEC_REL_WORKFLOW`: Release CI/CD Workflow
- `INST_SYSPILOT_SPEC_REL_ARCHIVE_PROCESS`: Change Document Archive Process

### spec_implement.rst

- `INST_SYSPILOT_SPEC_IMPL_DIR_STRUCTURE`: Product Directory Structure
- `INST_SYSPILOT_SPEC_IMPL_SYNC_PROCESS`: Setup Agent Synchronization Process

---

## Dependencies

- prod-inst-concept (Change 1) — naming decisions ✅ approved
- prod-inst-migrate (Change 2) — product tree in place ✅ committed
