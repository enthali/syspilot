# Change Document: ontology-phase2

**Status**: ready-for-merge
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

**Status**: ✅ completed

### Impacted User Stories

None — greenfield additions building on Phase 1 baseline.

### New User Stories

| ID | Title | Priority |
|----|-------|----------|
| SYSP_US_ONTOLOGY_ACTOR_CATALOG | Actor Catalogue in Ontology | mandatory |
| SYSP_US_ONTOLOGY_TYPE_LINKS | Type Link Relationships in Ontology | mandatory |
| SYSP_US_ONTOLOGY_LIFECYCLE | Lifecycle State Machine in Ontology | mandatory |
| SYSP_US_ONTOLOGY_REF_PAGE | Ontology Reference Page | mandatory |
| SYSP_US_ONTOLOGY_TYPE_SPLIT | TEST Type Split | mandatory |

### Decisions

- Five separate US — each deliverable has a distinct WHY and distinct actor perspective.
- ACTOR_CATALOG framed from agent perspective (routing), not human-readable reference.
- REF_PAGE framed from developer perspective (documentation maintenance).
- TYPE_SPLIT framed from developer perspective (distinct ownership/lifecycle).

### Horizontal Check (MECE)

- [x] No contradictions with existing User Stories
- [x] No redundancies (Phase 1 US cover single-master, governance, skill — no overlap)
- [x] No gaps identified

---

## Level 1: Requirements

**Status**: ✅ completed

### Impacted Requirements

None.

### New Requirements

| ID | Title | Links | Priority |
|----|-------|-------|----------|
| SYSP_REQ_ONTOLOGY_ACTOR_CATALOG | Actor Catalogue in Ontology | SYSP_US_ONTOLOGY_ACTOR_CATALOG | mandatory |
| SYSP_REQ_ONTOLOGY_TYPE_LINKS | Type Link Relationships | SYSP_US_ONTOLOGY_TYPE_LINKS | mandatory |
| SYSP_REQ_ONTOLOGY_LIFECYCLE | Lifecycle Status Transitions | SYSP_US_ONTOLOGY_LIFECYCLE | mandatory |
| SYSP_REQ_ONTOLOGY_REF_PAGE | Ontology Reference Page Generation | SYSP_US_ONTOLOGY_REF_PAGE | mandatory |
| SYSP_REQ_ONTOLOGY_TYPE_SPLIT | TEST Type Split | SYSP_US_ONTOLOGY_TYPE_SPLIT | mandatory |

### Decisions

- LIFECYCLE REQ uses "universal fallback + type-specific override" pattern (AC-3).
- REF_PAGE REQ specifies three output sections: type table, relationship diagram, lifecycle diagram.
- TYPE_SPLIT REQ mandates deprecated alias (AC-3) — no forced migration.

### Horizontal Check (MECE)

- [x] No contradictions with existing Requirements
- [x] No redundancies
- [x] All new REQs link to User Stories

---

## Level 2: Design

**Status**: ✅ completed

### Impacted Design Elements

None.

### New Design Elements

| ID | Title | Links |
|----|-------|-------|
| SYSP_SPEC_ONTOLOGY_ACTOR_CATALOG | Actor Catalogue Schema | SYSP_REQ_ONTOLOGY_ACTOR_CATALOG |
| SYSP_SPEC_ONTOLOGY_TYPE_LINKS | Type Link Relationships Schema | SYSP_REQ_ONTOLOGY_TYPE_LINKS |
| SYSP_SPEC_ONTOLOGY_LIFECYCLE | Lifecycle Status Transitions Schema | SYSP_REQ_ONTOLOGY_LIFECYCLE |
| SYSP_SPEC_ONTOLOGY_REF_PAGE | Ontology Reference Page Hook | SYSP_REQ_ONTOLOGY_REF_PAGE |
| SYSP_SPEC_ONTOLOGY_TYPE_SPLIT | TEST Type Split | SYSP_REQ_ONTOLOGY_TYPE_SPLIT |

### Decisions

- **Actor catalogue:** flat key=value map (directive→actor name). Consumer contract: agent finds its own name, collects all keys.
- **Type links:** array-of-tables `[[syspilot.type_links]]` with `from`/`to`/`rel` fields. Direction is always bottom-up (child→parent).
- **Lifecycle:** `[syspilot.status_transitions]` with `universal` array + `universal_exit` + per-type `overrides` (override replaces, not merges).
- **Stories skip "implemented"** — go draft→approved→verified directly.
- **Definitions:** only draft↔approved (no implementation/verification lifecycle).
- **Ref page:** Sphinx extension hook on builder-inited; generates RST with `.. mermaid::` directives; output gitignored.
- **Type split colours:** uat=#A8E6CF (green), test=#DCB239 (kept), unit_test=#FFD3B6 (peach).

### Horizontal Check (MECE)

- [x] No contradictions with existing Designs
- [x] All new SPECs link to Requirements

---

## Final Consistency Check

**Status**: ✅ passed

### Traceability Verification

| User Story | Requirements | Design | Complete? |
|------------|--------------|--------|-----------|
| SYSP_US_ONTOLOGY_ACTOR_CATALOG | SYSP_REQ_ONTOLOGY_ACTOR_CATALOG | SYSP_SPEC_ONTOLOGY_ACTOR_CATALOG | ✅ |
| SYSP_US_ONTOLOGY_TYPE_LINKS | SYSP_REQ_ONTOLOGY_TYPE_LINKS | SYSP_SPEC_ONTOLOGY_TYPE_LINKS | ✅ |
| SYSP_US_ONTOLOGY_LIFECYCLE | SYSP_REQ_ONTOLOGY_LIFECYCLE | SYSP_SPEC_ONTOLOGY_LIFECYCLE | ✅ |
| SYSP_US_ONTOLOGY_REF_PAGE | SYSP_REQ_ONTOLOGY_REF_PAGE | SYSP_SPEC_ONTOLOGY_REF_PAGE | ✅ |
| SYSP_US_ONTOLOGY_TYPE_SPLIT | SYSP_REQ_ONTOLOGY_TYPE_SPLIT | SYSP_SPEC_ONTOLOGY_TYPE_SPLIT | ✅ |

### Artefakt-Removal-Check

Not applicable — no artefacts removed. (TEST_ kept as deprecated alias.)

### Issues Found

- **Stray working-tree change (discarded):** `syspilot/agents/syspilot.setup.agent.md` had an unrelated modification on checkout — discarded. Not part of this CR.
- **User-guided L2 checkpoint:** 2 PM corrections (req→story label, uat target) applied before implementation.

### Sign-off

- [x] All levels completed
- [x] All conflicts resolved
- [x] Traceability verified
- [x] Ready for merge

---

## QM Findings

*QM writes findings directly into this section after each review round. PM records
decisions (fix-now / defer / accept-as-is) with rationale in the same section.
Multiple review rounds are appended as sub-sections. Existing CDs without this
section are unaffected — the section is additive, never required retroactively.*

### Round 1

**Reviewed by:** MECE Engineer + Trace Engineer
**Review date:** 2026-07-24

#### Findings

| # | Level | Element ID | Finding | Severity |
|---|-------|------------|---------|----------|
| 1 | L1 | SYSP_REQ_ONTOLOGY_TYPE_LINKS | REQ example used "refines"; spec defines 5 semantics without refines | medium-low |
| 2 | L2 | SYSP_SPEC_ONTOLOGY_TYPE_SPLIT | Organic migration path unspecified in AC-3 | medium |
| 3 | L2 | SYSP_SPEC_ONTOLOGY_REF_PAGE | Output path/type mismatch vs implementation; gitignore unset | medium |
| 4 | L2 | SYSP_SPEC_ONTOLOGY_SKILL_CONTENT | Not updated for Phase 2 sections | medium |
| 5 | SKILL | syspilot.ontology/SKILL.md | Body still referenced "Future phases" placeholder | medium |

#### CM Decisions

| # | Finding # | Decision | Rationale |
|---|-----------|----------|-----------|
| 1 | 1 | fix-now | REQ example corrected to "provides" |
| 2 | 2 | fix-now | Organic migration defined as per-CR manual reclassification; lint Phase 3 |
| 3 | 3 | fix-now (Option A) | Spec updated to Markdown at docs/ontology-reference.md; .gitignore entry added |
| 4 | 4 | fix-now | SPEC expanded to include actors, type_links, lifecycle sections |
| 5 | 5 | fix-now | SKILL.md Phase 2 sections documented |
### Round 2

**Reviewed by:** MECE Engineer + Trace Engineer
**Review date:** 2026-07-24
**Verification of Round 1 fixes:** All 5 items confirmed repaired

#### Findings

None. All corrections verified:

1. **REQ TYPE_LINKS:** Example now uses "provides" semantics (consistent with SPEC definition of 5 link types)
2. **TYPE_SPLIT migration:** AC-3 now documents organic migration path (per-CR manual reclassification; lint Phase 3)
3. **REF_PAGE implementation:** Spec aligned to Markdown output at `docs/ontology-reference.md`; `.gitignore` entry present; builder-inited hook (conf.py) generates type table, relationship Mermaid diagram, lifecycle Mermaid diagram
4. **SKILL_CONTENT sections:** SPEC expanded to document Phase 2 sections (Actor Catalogue, Type Link Relationships, Lifecycle State Machine)
5. **SKILL.md body:** Phase 2 sections documented in full with example code blocks; "Future phases" placeholder removed

**Sphinx build:** Exit 0 (clean).

**Traceability:** All 5 new US/REQ/SPEC elements linked correctly. No broken `:links:`.

**Status:** ✅ CLEAN — Ready for merge.
---

---

*Generated by syspilot Change Agent*
