# Change Document: ontology-phase2

**Status**: draft
**Branch**: feature/ontology-phase2
**Created**: 2026-07-23
**Author**: Project Manager
**Operation Mode**: user-guided

---

## Summary

Phase 1 delivered the flat single-master ontology architecture: `.syspilot/ontology.toml`
is the canonical source read directly by sphinx-needs, with the generator and projection
removed. Phase 2 populates the syspilot-specific supersections and enriches the `[needs]`
schema so the ontology captures **who owns what** and **how the method flows**, not just the
type catalogue. Scope: (1) `[syspilot.actors]` actor catalogue mapping each Need type to its
owning actor (PM owns none — Portfolio plane only); (2) `[syspilot.type_links]` explicit
bottom-up type relationships (provides/refines/implements/validates/verifies/defines);
(3) `[[needs.extra_links]]` adding those typed link fields additively, with `:links:` kept as
a generic fallback (no breaking change, no forced migration; optional lint warns on residual
`:links:`); (4) split the single `TEST_` type into three — `uat` (UAT_), `test` (TEST_),
`unit_test` (UNIT_) — with `TEST_` kept as a deprecated alias for organic migration;
(5) `[syspilot.status_transitions]` lifecycle state machine (allowed transitions, TBD by
System Designer); (6) an ontology reference page generated at build time by a `conf.py` hook
(type catalogue table + Mermaid type-relationship diagram + Mermaid lifecycle diagram),
always in sync with the master. Out of scope: migrating existing `:links:`, agents consuming
the ontology at runtime (Phase 3 / #57), the blast-radius diff tool (Phase 4 / #55), and V&V
model detail — the `test`/verifies-`REQ_` ownership stays TBD pending the CRAFT/dspace pilot.
Design guidance: author the supersections so a generic actor could read them alone and act,
not merely so humans get a reference page.

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
