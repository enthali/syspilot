# Change Document: split-l2-specs

**Status**: approved
**Branch**: refactor/split-l2-by-component
**Created**: 2026-02-06
**Author**: GitHub Copilot + User

---

## Summary

Split the monolithic `spec_syspilot.rst` into per-component/per-agent design specification files. Reverse-engineered 16 new specs from the actual agent `.md` files to properly document each agent's design. Reorganized L2 to follow solution-domain structure (one file per component), consistent with the methodology established during the L0/L1 refactoring.

---

## Level 0: User Stories

**Status**: ✅ completed — no changes

No User Stories were affected. This is a structural refactoring of existing Level 2 content.

---

## Level 1: Requirements

**Status**: ✅ completed — no changes

No Requirements were affected. All existing REQ links remain valid — the new SPEC IDs link to the same REQs that the old specs linked to.

---

## Level 2: Design

**Status**: ✅ completed

### Deleted Files

- `spec_syspilot.rst` — monolith containing 11 specs (content redistributed)

### New Files

| File | Component | Specs |
|------|-----------|-------|
| `spec_agent_framework.rst` | Shared agent patterns | 2 |
| `spec_change.rst` | Change Agent | 4 |
| `spec_implement.rst` | Implement Agent | 4 |
| `spec_verify.rst` | Verify Agent | 3 |
| `spec_traceability.rst` | MECE + Trace Agents | 4 |
| `spec_memory.rst` | Memory Agent | 3 |
| `spec_setup.rst` | Setup Agent | 6 |
| `spec_doc_structure.rst` | Documentation structure | 1 |

### Unchanged Files

- `spec_release.rst` — already per-component (7 specs)

### Moved Specs (from spec_syspilot.rst)

- SPEC_AGENT_WORKFLOW → `spec_agent_framework.rst`
- SPEC_AGENT_PROMPT_SEPARATION → `spec_agent_framework.rst`
- SPEC_DOC_STRUCTURE → `spec_doc_structure.rst`
- SPEC_INST_INIT_SCRIPTS → `spec_setup.rst`
- SPEC_INST_SETUP_AGENT → `spec_setup.rst`
- SPEC_INST_FILE_OWNERSHIP → `spec_setup.rst`
- SPEC_INST_UPDATE_PROCESS → `spec_setup.rst`
- SPEC_INST_AUTO_DETECT → `spec_setup.rst`
- SPEC_INST_RELEASE_STRUCTURE → `spec_setup.rst`

### Renamed Specs (moved to per-agent files with new IDs)

- SPEC_AGENT_QUALITY_GATES → SPEC_IMPL_QUALITY_GATES (`spec_implement.rst`)
- SPEC_AGENT_PRE_CHECK → SPEC_IMPL_PRE_CHECK (`spec_implement.rst`)

### New Specs (reverse-engineered from agent.md files)

| ID | Title | Links | Source |
|----|-------|-------|--------|
| SPEC_CHG_LEVEL_PROCESSING | Iterative Level Processing | REQ_CHG_ANALYSIS_AGENT, REQ_CHG_WORKFLOW_STEPS, REQ_CHG_LINK_DISCOVERY | `syspilot.change.agent.md` |
| SPEC_CHG_CHANGE_DOCUMENT | Change Document Management | REQ_CHG_CHANGE_DOC, REQ_CHG_ANALYSIS_AGENT | `syspilot.change.agent.md` |
| SPEC_CHG_BIDIR_NAVIGATION | Bidirectional Level Navigation | REQ_CHG_BIDIR_NAV, REQ_CHG_ANALYSIS_AGENT | `syspilot.change.agent.md` |
| SPEC_CHG_ATOMIC_UPDATE | Atomic RST Updates with Status Lifecycle | REQ_CHG_ANALYSIS_AGENT, REQ_CHG_FINAL_CHECK, REQ_CHG_MECE_PER_LEVEL | `syspilot.change.agent.md` |
| SPEC_IMPL_CHANGE_DOC_INPUT | Change Document Consumption | REQ_CHG_IMPL_AGENT, REQ_CHG_CHANGE_DOC | `syspilot.implement.agent.md` |
| SPEC_IMPL_CODE_TRACEABILITY | Code and Test Traceability | REQ_CHG_IMPL_AGENT, REQ_CORE_TRACEABILITY | `syspilot.implement.agent.md` |
| SPEC_VERIFY_CATEGORIES | Five-Category Verification | REQ_CHG_VERIFY_AGENT, REQ_CORE_TRACEABILITY | `syspilot.verify.agent.md` |
| SPEC_VERIFY_REPORT | Verification Report Format | REQ_CHG_VERIFY_AGENT | `syspilot.verify.agent.md` |
| SPEC_VERIFY_STATUS_LIFECYCLE | Verification Status Lifecycle | REQ_CHG_VERIFY_AGENT, REQ_CHG_FINAL_CHECK | `syspilot.verify.agent.md` |
| SPEC_MECE_HORIZONTAL_ANALYSIS | Horizontal MECE Analysis | REQ_TRACE_MECE, REQ_CHG_MECE_PER_LEVEL | `syspilot.mece.agent.md` |
| SPEC_MECE_REPORT | MECE Report Format | REQ_TRACE_MECE | `syspilot.mece.agent.md` |
| SPEC_TRACE_VERTICAL_ANALYSIS | Vertical Traceability Analysis | REQ_TRACE_VERTICAL, REQ_CHG_BIDIR_NAV | `syspilot.trace.agent.md` |
| SPEC_TRACE_REPORT | Trace Report Format | REQ_TRACE_VERTICAL | `syspilot.trace.agent.md` |
| SPEC_MEM_UPDATE_PROCESS | Memory Update Process | REQ_DX_MEMORY_AGENT | `syspilot.memory.agent.md` |
| SPEC_MEM_CONTENT_CATEGORIES | Memory Content Categories | REQ_DX_MEMORY_AGENT | `syspilot.memory.agent.md` |
| SPEC_MEM_INSTRUCTIONS_STRUCTURE | copilot-instructions.md Structure | REQ_DX_MEMORY_AGENT | `syspilot.memory.agent.md` |

### Decisions

- Quality Gates and Pre-Check belong in `spec_implement.rst` (per-agent), not in `spec_agent_framework.rst` (shared)
- MECE + Trace agents share one file (`spec_traceability.rst`) since they are complementary (horizontal vs vertical)
- L2 organized by **solution domain** (per component/agent), intentionally different from L0/L1 (problem domain)

### Horizontal Check (MECE)

- [x] No contradictions between spec files
- [x] No duplicate SPEC IDs
- [x] All new SPECs link to Requirements
- [x] All moved SPECs preserve original REQ links

---

## Final Consistency Check

**Status**: ✅ passed

### Traceability Verification

All 34 specs link to at least one REQ. No orphaned specs.

### Validation

- [x] `sphinx-build -W` passes (only pre-existing graphviz warning)
- [x] All 34 SPEC IDs are unique
- [x] `spec_syspilot.rst` fully decomposed (no content lost)
- [x] `index.rst` updated with all 9 spec files
- [x] No User Stories or Requirements modified

### Sign-off

- [x] All levels completed
- [x] All conflicts resolved
- [x] Traceability verified
- [x] Committed on branch `refactor/split-l2-by-component` (ab801d5)

---

*Generated by syspilot Change Agent*
