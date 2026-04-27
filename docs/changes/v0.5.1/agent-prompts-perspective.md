# Change Document: agent-prompts-perspective

**Status**: in-progress
**Branch**: feature/agent-prompts-perspective
**Created**: 2026-04-16
**Author**: @syspilot.design

---

## Summary

Two connected changes: (1) Correct the perspective formulation in all 9 Engineer User Stories from "As a syspilot user, I want to have a [Agent]..." to "As a syspilot user, I want my agentic managers to have a [Agent] that..." — because users don't invoke engineers directly, managers orchestrate them. (2) Add prompt file specifications at REQ and SPEC levels defining that user-invocable agents (managers) SHALL have prompt files.

---

## Level 0: User Stories

**Status**: ✅ completed

### Impacted User Stories

| ID | Title | Impact | Notes |
|----|-------|--------|-------|
| SYSP_US_DESIGN | System Designer Agent | modified | Perspective corrected |
| SYSP_US_IMPLEMENT | Dev Engineer Agent | modified | Perspective corrected |
| SYSP_US_UAT | Test Engineer Agent | modified | Perspective corrected |
| SYSP_US_DOCU | Documentation Engineer Agent | modified | Perspective corrected |
| SYSP_US_MECE | Quality Engineer MECE Agent | modified | Perspective corrected |
| SYSP_US_TRACE | Quality Engineer Trace Agent | modified | Perspective corrected |
| SYSP_US_RELEASE | Release Engineer Agent | modified | Perspective corrected |
| SYSP_US_SETUP | Setup Engineer Agent | modified | Perspective corrected |
| SYSP_US_VERIFY | Verify Engineer Agent | modified | Perspective corrected |

### Decisions

- All 9 engineer US formulations changed from "I want to have a [Agent]" to "I want my agentic managers to have a [Agent] that..."
- 3 manager US files (PM, CM, QM) intentionally NOT changed — they are directly user-invocable

---

## Level 1: Requirements

**Status**: ✅ completed

### New Requirements

| ID | Title | Links | Priority |
|----|-------|-------|----------|
| SYSP_REQ_AGENT_ARCH_PROMPT | Agent Prompt File | SYSP_US_AGENT_ARCH | mandatory |
| SYSP_REQ_PM_PROMPT | Project Manager Prompt File | SYSP_US_PM; SYSP_REQ_AGENT_ARCH_PROMPT | mandatory |
| SYSP_REQ_CM_PROMPT | Change Manager Prompt File | SYSP_US_CM; SYSP_REQ_AGENT_ARCH_PROMPT | mandatory |
| SYSP_REQ_QM_PROMPT | Quality Manager Prompt File | SYSP_US_QM; SYSP_REQ_AGENT_ARCH_PROMPT | mandatory |

### Decisions

- Generic prompt requirement (SYSP_REQ_AGENT_ARCH_PROMPT) placed in req_agent_arch.rst alongside other architecture meta-requirements
- Each manager gets a concrete prompt requirement in its own REQ file
- Engineers explicitly excluded from prompt files (AC-2 of SYSP_REQ_AGENT_ARCH_PROMPT)

---

## Level 2: Design Specs

**Status**: ✅ completed

### New Design Specs

| ID | Title | Links |
|----|-------|-------|
| SYSP_SPEC_AGENT_ARCH_PROMPT | Prompt File Definition | SYSP_REQ_AGENT_ARCH_PROMPT |

### Decisions

- Prompt file format: `syspilot.<name>.prompt.md` with minimal frontmatter `agent: syspilot.<name>`
- Only managers (PM, CM, QM) have prompt files
- Engineers use `runSubagent()` invocation — no prompt files needed
- Spec placed in spec_agent_arch.rst alongside other architecture meta-specs

---

## Commits

| # | Hash | Message | Files |
|---|------|---------|-------|
| 1 | 02c7dc7 | fix: correct engineer US perspective to manager-orchestrated formulation | 9 US files |
| 2 | bcfcaf3 | feat: add prompt file requirements (SYSP_REQ_AGENT_ARCH_PROMPT, PM/CM/QM prompt REQs) | req_agent_arch.rst, req_project_mgr.rst, req_change_mgr.rst, req_quality_mgr.rst |
| 3 | 844d329 | feat: add prompt file design spec (SYSP_SPEC_AGENT_ARCH_PROMPT) | spec_agent_arch.rst |
