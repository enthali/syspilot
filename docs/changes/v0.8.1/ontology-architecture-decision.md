# Change Document: ontology-architecture-decision

**Status**: ready-for-merge
**Branch**: feature/ontology-arch-qm-fixup (fix-up of feature/ontology-architecture-decision)
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
| SYSP_REQ_ONTOLOGY_TEMPLATES | Ontology Templates | SYSP_US_ONTOLOGY_TEMPLATES | mandatory |
| SYSP_REQ_ONTOLOGY_CAPABILITIES | Capability Vocabulary Declaration | SYSP_US_ONTOLOGY_ARCH | mandatory |
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
| SYSP_SPEC_ONTOLOGY_DEFAULT_TEMPLATE | Syspilot-Default Ontology Template | SYSP_REQ_ONTOLOGY_TEMPLATES |
| SYSP_SPEC_ONTOLOGY_CAPABILITIES | Capability Vocabulary | SYSP_REQ_ONTOLOGY_CAPABILITIES |
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

All QM findings resolved across two review rounds:
- Round 1 (MECE+Trace): 3 findings — all fixed-now.
- Round 2 (MECE+Trace): 5 findings — 4 fixed-now (#1, #3, #4, #5), 1 deferred (#2: missing `:links:` convention in L0 stories, deferred to Phase 1).

### Sign-off

- [x] All levels completed (no ⚠️ DEPRECATED markers remaining)
- [x] All conflicts resolved
- [x] Traceability verified
- [x] Ready for merge (Phase 0: no implementation; Dev Engineer step not applicable)

---

## QM Findings

*QM writes findings directly into this section after each review round. PM records
decisions (fix-now / defer / accept-as-is) with rationale in the same section.
Multiple review rounds are appended as sub-sections. Existing CDs without this
section are unaffected — the section is additive, never required retroactively.*

### Round 2 (consolidated — MECE + Trace Engineer audit)

**Reviewed by:** QM + Trace Engineer
**Review date:** 2026-07-17

#### Findings

| # | Level | Element ID | Finding | Severity |
|---|-------|------------|---------|----------|
| 1 | L1 | SYSP_REQ_ONTOLOGY_SEPARATION | AC-3 undefined term "configuration surface" — testers cannot determine compliance criteria | medium |
| 2 | L0 | SYSP_US_ONTOLOGY_ARCH, SYSP_US_ONTOLOGY_TEMPLATES | Missing `:links:` fields (reverse traceability convention); sphinx-build -W passes | low |
| 3 | UAT | us_uat_ontology_arch.rst | Stale counts: "five spec elements" → 6; "six REQ elements" → 7 | medium-high |
| 4 | UAT | spec_uat_ontology_arch.rst (TC-TRACE) | Same stale counts in expected outcomes | medium-high |
| 5 | UAT | (coverage gap) | No TC-* scenario covers CAPABILITIES REQ/SPEC | medium-high |

#### PM Decisions

| # | Finding # | Decision | Rationale |
|---|-----------|----------|-----------|
| 1 | 1 | fix-now | Testability gap; AC-3 must be precise before Phase 1 builds on this spec |
| 2 | 2 | defer | Build passes; `:links:` convention clarification deferred to Phase 1 when ontology is live |
| 3 | 3 | fix-now | Stale counts create false UAT pass criteria; minor but must be accurate |
| 4 | 4 | fix-now | Same rationale as #3 |
| 5 | 5 | fix-now | CAPABILITIES was added in Round 1 fix-up; UAT coverage must follow |

**Fix-now routing:** #1 → Design (CM); #3–5 → Test Designer. Fix-up branch: `feature/ontology-arch-qm-fixup`.

**Note:** Branch was merged before Round 2 findings arrived (CM declared ready-for-merge before Trace Engineer audit completed). Fix-up proceeds on a new branch off `development`.

---

---

*Generated by syspilot Change Agent*
