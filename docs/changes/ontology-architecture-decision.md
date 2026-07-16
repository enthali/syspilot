# Change Document: ontology-architecture-decision

**Status**: in-progress
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

**Status**: ⏳ not started | 🔄 in progress | ✅ completed

### Impacted User Stories

| ID | Title | Impact | Notes |
|----|-------|--------|-------|
| US_abc | ... | modified | ... |

### New User Stories

| ID | Title | Priority |
|----|-------|----------|
| US_xxx | As a..., I want..., so that... | mandatory |

### Decisions

- Decision 1: ...
- Decision 2: ...

### Horizontal Check (MECE)

- [ ] No contradictions with existing User Stories
- [ ] No redundancies
- [ ] Gaps identified and addressed

---

## Level 1: Requirements

**Status**: ⏳ not started | 🔄 in progress | ✅ completed

### Impacted Requirements

Found via links from User Stories above.

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| REQ_abc | US_abc | modified | ... |

### New Requirements

| ID | Title | Links | Priority |
|----|-------|-------|----------|
| REQ_xxx | ... | US_xxx | mandatory |

### Conflicts Detected

- ⚠️ REQ_xxx vs REQ_yyy: {description}
  - Resolution: {decision}

### Decisions

- Decision 1: ...

### Horizontal Check (MECE)

- [ ] No contradictions with existing Requirements
- [ ] No redundancies
- [ ] All new REQs link to User Stories

---

## Level 2: Design

**Status**: ⏳ not started | 🔄 in progress | ✅ completed

### Impacted Design Elements

Found via links from Requirements above.

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| SPEC_abc | REQ_abc | modified | ... |

### New Design Elements

| ID | Title | Links |
|----|-------|-------|
| SPEC_xxx | ... | REQ_abc, REQ_xxx |

### Conflicts Detected

- ⚠️ SPEC_xxx vs SPEC_yyy: {description}
  - Resolution: {decision}

### Decisions

- Decision 1: ...

### Horizontal Check (MECE)

- [ ] No contradictions with existing Designs
- [ ] All new SPECs link to Requirements

---

## Final Consistency Check

**Status**: ⏳ not started | ✅ passed | ❌ failed

### Traceability Verification

| User Story | Requirements | Design | Complete? |
|------------|--------------|--------|-----------|
| US_xxx | REQ_xxx | SPEC_xxx | ✅ |
...

### Artefakt-Removal-Check

*Fill in only when this CR removes an artefact (file, field, configuration key, REQ-ID).*

For each removed artefact, run a project-wide grep on all plausible name variants and classify results:

| Removed Artefact | Class (a): Code/Workflow refs | Class (b): Doc refs | Class (c): Historic Change Docs |
|------------------|-------------------------------|---------------------|---------------------------------|
| `{artefact name}` | {files + lines fixed / none} | {files + lines fixed / none} | {count — acceptable historic stranding} |

- [ ] All class (a) active code/workflow references fixed in this CR
- [ ] All class (b) active documentation references fixed in this CR
- [ ] Class (c) historical Change Documents accepted as "acceptable historic stranding" and disclosed above

### Issues Found

- [ ] Issue 1: ...
- [ ] Issue 2: ...

### Sign-off

- [ ] All levels completed (no ⚠️ DEPRECATED markers remaining)
- [ ] All conflicts resolved
- [ ] Traceability verified
- [ ] Ready for implementation

---

## QM Findings

*QM writes findings directly into this section after each review round. PM records
decisions (fix-now / defer / accept-as-is) with rationale in the same section.
Multiple review rounds are appended as sub-sections. Existing CDs without this
section are unaffected — the section is additive, never required retroactively.*

### Round 1

**Reviewed by:** QM
**Review date:** {DATE}

#### Findings

| # | Level | Element ID | Finding | Severity |
|---|-------|------------|---------|----------|
| 1 | L? | {ID} | {description} | high / medium / low |

#### PM Decisions

| # | Finding # | Decision | Rationale |
|---|-----------|----------|-----------|
| 1 | 1 | fix-now / defer / accept-as-is | {rationale} |

---

## Appendix: Link Discovery Results

```
{paste output from get_need_links.py as needed}
```

---

*Generated by syspilot Change Agent*
