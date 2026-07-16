# Change Document: ontology-architecture-decision

**Status**: ready-for-merge
**Branch**: feature/ontology-architecture-decision
**Created**: 2026-07-16
**Author**: PM + User
**GH Issue**: #49
**Operation Mode**: user-guided

---

## Summary

**Architecture Decision: syspilot becomes ontology-agnostic.**

syspilot currently embeds its default ontology (User Story → Requirement → Design Spec, L0/L1/L2) directly into agent prose, workflows, templates, and tools. This means every migration to a different ontology (e.g. ASPICE: SW_REQ → SW_DES → SW_DD → SW_VER) requires rewriting all affected agents individually — a repeatable effort without a structural solution.

**Decision:** syspilot separates four concerns cleanly:
1. **Ontology** — which Work-Product types exist, how they are linked, which lifecycle rules apply.
2. **Capabilities** — which operations can create, modify, check, and validate Work Products.
3. **Actors** — which Capabilities and Work-Product types each Actor owns.
4. **Process** — in which order Actors operate, which gates control transitions.

**Key invariants:**
- `syspilot.toml` is the single source of truth for ontology selection and tailoring — `conf.py` is an adapter/consumer, not an authority.
- Every active Work-Product type has exactly one Primary-Actor-Owner (1:N Work-Product-type-to-Actor forbidden as ownership; reading is allowed).
- An Actor processes *all and only* its own affected types in the dependency order of the ontology graph.
- Branching graphs are first-class — "dependency order" is graph order, not a numbered L0/L1/L2 loop.

**Delivery:** This is Phase 0 — pure architecture documentation. New US/REQ/SPEC elements anchoring the `.syspilot/` directory structure and `ontology.toml` schema in the spec tree. No code, no agent changes, no installer update. Subsequent phases (1–8) are separate CRs.

**Acceptance Criteria:**
- This Change Document (ADR) is versioned in the repo.
- `.syspilot/` structure and `ontology.toml` schema (candidate) documented in new spec elements: directory structure, installer invariant, typed relations, ownership assignments, lifecycle states, validation constraints.
- New US/REQ/SPEC elements exist in the spec tree — existing tree unchanged.
- `sphinx-build -W` clean.

---

## Level 0: User Stories

**Status**: ✅ completed

### Impacted User Stories

None — greenfield addition.

### New User Stories

| ID | Title | Priority |
|----|-------|----------|
| SYSP_US_ONTOLOGY_ARCH | Ontology-Agnostic Architecture | mandatory |
| SYSP_US_ONTOLOGY_TEMPLATES | Ontology Templates | mandatory |

### Decisions

- Single US for the architecture decision (no split by sub-concern); the four concerns are one indivisible promise.
- Templates added as a separate US discovered during design — different WHY (adoptability vs. agnosticism).
- Process concern acknowledged as future-phase candidate for per-project workflow definitions; not in scope here.

### Horizontal Check (MECE)

- [x] No contradictions with existing User Stories
- [x] No redundancies
- [x] Gaps identified and addressed

---

## Level 1: Requirements

**Status**: ✅ completed

### Impacted Requirements

None — greenfield addition.

### New Requirements

| ID | Title | Links | Priority |
|----|-------|-------|----------|
| SYSP_REQ_ONTOLOGY_SEPARATION | Four-Concern Separation | SYSP_US_ONTOLOGY_ARCH | mandatory |
| SYSP_REQ_ONTOLOGY_CONFIG_AUTHORITY | Configuration Authority | SYSP_US_ONTOLOGY_ARCH | mandatory |
| SYSP_REQ_ONTOLOGY_OWNERSHIP | Primary-Actor-Owner Invariant | SYSP_US_ONTOLOGY_ARCH | mandatory |
| SYSP_REQ_ONTOLOGY_GRAPH_ORDER | Graph-Order Processing | SYSP_US_ONTOLOGY_ARCH | mandatory |
| SYSP_REQ_ONTOLOGY_DIRECTORY | Ontology Storage | SYSP_US_ONTOLOGY_ARCH | mandatory |
| SYSP_REQ_ONTOLOGY_CAPABILITIES | Capability Vocabulary Declaration | SYSP_US_ONTOLOGY_ARCH | mandatory |
| SYSP_REQ_ONTOLOGY_TEMPLATES | Ontology Templates | SYSP_US_ONTOLOGY_TEMPLATES | mandatory |
| SYSP_REQ_UAT_ONTOLOGY_ARCH | UAT Test Data: Ontology Arch | SYSP_US_UAT_ONTOLOGY_ARCH | mandatory |

### Conflicts Detected

None.

### Decisions

- `.syspilot/` path is L2 detail; L1 says "dedicated project-local directory" only.
- Schema structural requirements (not full TOML syntax) at L2; keeps spec stable across syntax iterations.

### Horizontal Check (MECE)

- [x] No contradictions with existing Requirements
- [x] No redundancies
- [x] All new REQs link to User Stories

---

## Level 2: Design

**Status**: ✅ completed

### Impacted Design Elements

None — greenfield addition.

### New Design Elements

| ID | Title | Links |
|----|-------|-------|
| SYSP_SPEC_ONTOLOGY_FOUR_CONCERNS | Four-Concern Model | SYSP_REQ_ONTOLOGY_SEPARATION |
| SYSP_SPEC_ONTOLOGY_TOML_SCHEMA | syspilot.toml Ontology Configuration | SYSP_REQ_ONTOLOGY_CONFIG_AUTHORITY, SYSP_REQ_ONTOLOGY_OWNERSHIP |
| SYSP_SPEC_ONTOLOGY_DIRECTORY | .syspilot/ Directory Structure | SYSP_REQ_ONTOLOGY_DIRECTORY |
| SYSP_SPEC_ONTOLOGY_GRAPH | Ontology Graph & Dependency Order | SYSP_REQ_ONTOLOGY_GRAPH_ORDER |
| SYSP_SPEC_ONTOLOGY_CAPABILITIES | Capability Vocabulary | SYSP_REQ_ONTOLOGY_CAPABILITIES |
| SYSP_SPEC_ONTOLOGY_DEFAULT_TEMPLATE | Syspilot-Default Ontology Template | SYSP_REQ_ONTOLOGY_TEMPLATES |
| SYSP_SPEC_UAT_ONTOLOGY_ARCH | UAT Expected Outcomes: Ontology Arch | SYSP_REQ_UAT_ONTOLOGY_ARCH |

### Conflicts Detected

None.

### Decisions

- Schema spec defines structural requirements (sections, keys, constraints), not concrete TOML syntax — allows iteration without spec changes.
- Default template serves dual purpose: adoption starting point + schema validation proof.
- `.syspilot/templates/` reserved for future additional templates (ASPICE, V-model, etc.).

### Horizontal Check (MECE)

- [x] No contradictions with existing Designs
- [x] All new SPECs link to Requirements

---

## Final Consistency Check

**Status**: ✅ passed

### Traceability Verification

| User Story | Requirements | Design | Complete? |
|------------|--------------|--------|-----------|
| SYSP_US_ONTOLOGY_ARCH | SYSP_REQ_ONTOLOGY_SEPARATION, SYSP_REQ_ONTOLOGY_CONFIG_AUTHORITY, SYSP_REQ_ONTOLOGY_OWNERSHIP, SYSP_REQ_ONTOLOGY_GRAPH_ORDER, SYSP_REQ_ONTOLOGY_DIRECTORY, SYSP_REQ_ONTOLOGY_CAPABILITIES | SYSP_SPEC_ONTOLOGY_FOUR_CONCERNS, SYSP_SPEC_ONTOLOGY_TOML_SCHEMA, SYSP_SPEC_ONTOLOGY_DIRECTORY, SYSP_SPEC_ONTOLOGY_GRAPH, SYSP_SPEC_ONTOLOGY_CAPABILITIES | ✅ |
| SYSP_US_ONTOLOGY_TEMPLATES | SYSP_REQ_ONTOLOGY_TEMPLATES | SYSP_SPEC_ONTOLOGY_DEFAULT_TEMPLATE | ✅ |
| SYSP_US_UAT_ONTOLOGY_ARCH | SYSP_REQ_UAT_ONTOLOGY_ARCH | SYSP_SPEC_UAT_ONTOLOGY_ARCH | ✅ |

### Artefakt-Removal-Check

Not applicable — this CR is a greenfield addition. No artefacts removed.

### Issues Found

None outstanding. Three QM MECE findings were all resolved in fix-up rounds:
- Finding #1 (high): TC-CONFIG-AUTH untestable — resolved: `conf.py` adapter/consumer authority clause added to `SYSP_SPEC_ONTOLOGY_TOML_SCHEMA`.
- Finding #2 (medium-high): Capabilities concern had no dedicated REQ/SPEC — resolved: `SYSP_REQ_ONTOLOGY_CAPABILITIES` + `SYSP_SPEC_ONTOLOGY_CAPABILITIES` added.
- Finding #3 (low): `SYSP_REQ_ONTOLOGY_DIRECTORY` had no explicit parent AC — resolved: AC-5 added to `SYSP_US_ONTOLOGY_ARCH`.

Trace Engineer: Clean. No broken links, no orphans.

### Sign-off

- [x] All levels completed (no ⚠️ DEPRECATED markers remaining)
- [x] All conflicts resolved
- [x] Traceability verified
- [x] Ready for merge (Phase 0: no implementation; Dev Engineer step is not applicable)

---

## QM Findings

*QM writes findings directly into this section after each review round. PM records
decisions (fix-now / defer / accept-as-is) with rationale in the same section.
Multiple review rounds are appended as sub-sections. Existing CDs without this
section are unaffected — the section is additive, never required retroactively.*

### Round 1

**Reviewed by:** MECE Engineer + Trace Engineer
**Review date:** 2026-07-16

#### Findings

| # | Level | Element ID | Finding | Severity |
|---|-------|------------|---------|----------|
| 1 | L2/UAT | SYSP_SPEC_UAT_ONTOLOGY_ARCH (TC-CONFIG-AUTH) | conf.py adapter/consumer text absent from SYSP_SPEC_ONTOLOGY_TOML_SCHEMA — test untestable as written | high |
| 2 | L1/L2 | (missing) | Capabilities concern has no dedicated REQ/SPEC despite US AC-1 requiring all four concerns independently defined | medium-high |
| 3 | L1 | SYSP_REQ_ONTOLOGY_DIRECTORY | No explicit parent AC in SYSP_US_ONTOLOGY_ARCH — grounded in prose only | low |

#### CM Fix-up Decisions

| # | Finding # | Decision | Rationale |
|---|-----------|----------|-----------|
| 1 | 1 | fix-now | Add authority clause to SYSP_SPEC_ONTOLOGY_TOML_SCHEMA naming conf.py as adapter/consumer. |
| 2 | 2 | fix-now | Add SYSP_REQ_ONTOLOGY_CAPABILITIES + SYSP_SPEC_ONTOLOGY_CAPABILITIES. |
| 3 | 3 | fix-now | Add AC-5 to SYSP_US_ONTOLOGY_ARCH (directory discoverability). |

---

### Round 2

**Reviewed by:** MECE Engineer (L0, L1, L2) + Trace Engineer (all levels)
**Review date:** 2026-07-17
**Reviewer:** Quality Manager

#### Findings

| # | Level | Element ID | Finding | Severity |
|---|-------|------------|---------|----------|
| 1 | L1 | SYSP_REQ_ONTOLOGY_SEPARATION | AC-3 ("Each of the four concerns has its own configuration surface") lacks concrete definition. Term "configuration surface" is undefined; testers cannot determine compliance criteria. Compare with AC-1/AC-2 (concrete actions) and CONFIG_AUTHORITY ACs (reference specific files/consumers). | medium |
| 2 | L0 | SYSP_US_ONTOLOGY_ARCH, SYSP_US_ONTOLOGY_TEMPLATES | Both elements lack `:links:` fields pointing to child requirements. This breaks reverse traceability visibility in sphinx-needs dependency trees. Per specification convention, L0 elements should link to their child requirements (e.g. SYSP_US_ONTOLOGY_ARCH :links: SYSP_REQ_ONTOLOGY_SEPARATION, SYSP_REQ_ONTOLOGY_CONFIG_AUTHORITY, etc.). Note: Build (sphinx-build -W) passes despite this gap, suggesting either reverse links are inferred or not enforced at Phase 0. **Recommend:** clarify whether this is a style convention or a build requirement before deferring. | low |

#### UAT Element Verification

Note: Trace Engineer initially reported missing SYSP_US_UAT_ONTOLOGY_ARCH, SYSP_REQ_UAT_ONTOLOGY_ARCH, SYSP_SPEC_UAT_ONTOLOGY_ARCH. Verification complete: all three elements exist in separate dedicated files (us_uat_ontology_arch.rst, req_uat_ontology_arch.rst, spec_uat_ontology_arch.rst) and are properly traced in the CD matrix. The separate file structure is correct per project ontology. **Status:** ✅ CLEAN (no finding).

#### CM Round 1 Fix-up Verification

- Finding #1 (high): conf.py authority clause — ✅ VERIFIED present in SYSP_SPEC_ONTOLOGY_TOML_SCHEMA
- Finding #2 (medium-high): Capabilities REQ/SPEC — ✅ VERIFIED SYSP_REQ_ONTOLOGY_CAPABILITIES and SYSP_SPEC_ONTOLOGY_CAPABILITIES added
- Finding #3 (low): SYSP_REQ_ONTOLOGY_DIRECTORY parent AC — ✅ VERIFIED AC-5 added to SYSP_US_ONTOLOGY_ARCH

#### PM Decisions (to be filled by PM)

| # | Finding # | Decision | Rationale |
|---|-----------|----------|-----------|
| 1 | 1 | [fix-now / defer / accept] | |
| 2 | 2 | [fix-now / defer / accept] | |

---

---

*Generated by syspilot Quality Manager*
