# Change Document: verify-agent-specs

**Status**: completed
**Branch**: feature/verify-agent-specs
**Created**: 2026-04-16
**Author**: System Designer

---

## Summary

Create the full sphinx-needs specification set (US → REQ → SPEC) for the Verify Engineer agent, which previously had agent and prompt files but no specs.

---

## Level 0: User Stories

**Status**: ✅ completed

### New User Stories

| ID | Title | Priority |
|----|-------|----------|
| SYSP_US_VERIFY | Verify Engineer Agent | mandatory |

### Decisions

- Follow the same pattern as all other engineer agents (single US linking to SYSP_US_AGENT_ARCH)

---

## Level 1: Requirements

**Status**: ✅ completed

### New Requirements

| ID | Title | Priority |
|----|-------|----------|
| SYSP_REQ_VERIFY_SOUL | Verify Engineer Soul | mandatory |
| SYSP_REQ_VERIFY_DUTIES | Verify Engineer Duties | mandatory |
| SYSP_REQ_VERIFY_WORKFLOW | Verify Engineer Workflow | mandatory |
| SYSP_REQ_VERIFY_FRONTMATTER | Verify Engineer Frontmatter Configuration | mandatory |

### Decisions

- FRONTMATTER also links to SYSP_REQ_AGENT_ARCH_FRONTMATTER (consistent with other engineers)
- Tools: read, search, execute, todo (no edit — verify never modifies files)

---

## Level 2: Design Specs

**Status**: ✅ completed

### New Design Specs

| ID | Title |
|----|-------|
| SYSP_SPEC_VERIFY_SOUL | Verify Engineer Soul |
| SYSP_SPEC_VERIFY_DUTIES | Verify Engineer Duties |
| SYSP_SPEC_VERIFY_WORKFLOW | Verify Engineer Workflow |
| SYSP_SPEC_VERIFY_FRONTMATTER | Verify Engineer Frontmatter |

### Decisions

- Workflow includes validation report output at docs/changes/val-<name>.md
- Scope rule: verify only what the Change Document declares as changed
