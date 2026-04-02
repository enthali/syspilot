# Change Document: concept-docs

**Status**: approved
**Branch**: feature/concept-docs
**Created**: 2026-04-02
**Author**: @enthali
**GitHub Issue**: #15

---

## Summary

Add two new conceptual documentation pages: `docs/architecture.md` (Product/Instance concept) and `docs/workflows.md` (syspilot process overview). Both with full traceability (REQ + SPEC chapter structure + Document Registry).

**Amendment (2026-04-02):** Extend workflows.md with Branching Strategy section. Add missing outgoing links from SPEC_DOC_WORKFLOWS_STRUCTURE to agent design specs (SPEC_CHG_*, SPEC_REL_*) so impact analysis catches documentation when agent specs change.

---

## Level 0: User Stories

**Status**: ✅ completed

- No new US needed — SYSPILOT_US_DOC_MAINTAIN covers documentation maintenance

---

## Level 1: Requirements

**Status**: ✅ completed

### New Requirements
- SYSPILOT_REQ_DOC_ARCHITECTURE: Architecture Documentation (Product/Instance concept)
- SYSPILOT_REQ_DOC_WORKFLOWS: Workflows Documentation (central syspilot process)

### Decisions
- Workflows = central syspilot process; Process docs = mapping to external standards (A-SPICE, 26262, CMMI)

---

## Level 2: Design

**Status**: ✅ completed

### New Design Elements
- SYSPILOT_SPEC_DOC_ARCHITECTURE_STRUCTURE: Chapter structure for docs/architecture.md (7 chapters)
- SYSPILOT_SPEC_DOC_WORKFLOWS_STRUCTURE: Chapter structure for docs/workflows.md (6 chapters + sub-sections)

### Modified Design Elements
- SYSPILOT_SPEC_DOC_SCOPE_SYSPILOT: Added architecture.md + workflows.md to Document Registry
- SYSPILOT_SPEC_DOC_INDEX_STRUCTURE: Added architecture + workflows to "Guides & Process" toctree
- SYSPILOT_SPEC_DOC_WORKFLOWS_STRUCTURE: Added Branching Strategy chapter (#7) + outgoing links to SPEC_CHG_CHANGE_DOCUMENT, SPEC_CHG_LEVEL_PROCESSING, SPEC_REL_WORKFLOW, SPEC_REL_GIT_TAG

### Modified Requirements
- SYSPILOT_REQ_DOC_WORKFLOWS: Added AC-7 (branching strategy)
