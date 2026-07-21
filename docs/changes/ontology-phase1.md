# Change Document: ontology-phase1

**Status**: draft
**Branch**: feature/ontology-phase1
**Created**: 2026-07-21
**Author**: Project Manager (triage), Change Manager (engineering)
**Operation Mode**: autonomous

---

## Summary

Phase 1 of the ontology-architecture-decision ADR (CR #49, merged). Phase 0
established the principle that `.syspilot/ontology.toml` is the canonical,
tooling-agnostic ontology master and that sphinx-needs/ubCode is just one
consumer, accessed via an adapter/generator. Phase 1 delivers the **capability**
— the infrastructure to make that real — without yet populating syspilot's own
`ontology.toml` (that is a follow-up CR).

**Deliverables:**

1. **`syspilot.ontology` skill** (read by the System Designer): how to edit
   `ontology.toml`, how to invoke the generator, governance guardrail
   (guarded artifact + additive/breaking change classification +
   migration-CR requirement), and schema documentation for the superset sections.
   The schema itself is to be defined interactively by the System Designer
   during this CR, subject to one constraint: syspilot-only sections must be
   cleanly separable from ubCode-understood sections.

2. **Generator Python script** (proposed location:
   `syspilot/sphinx/generate_ubproject.py`): strips syspilot-only sections from
   `.syspilot/ontology.toml` → produces `docs/ubproject.toml` (the ubCode
   projection). Must include a `--compare` mode that exits non-zero when the
   committed `docs/ubproject.toml` differs from a fresh generation (used by the
   Release Agent).

3. **Release Agent extension**: add a compare-mode generator check in the Release
   Agent's early steps, before squash-merge to main. Fails the release if
   `docs/ubproject.toml` is stale relative to `ontology.toml`.

4. **Governance Guardrail** at spec level: `ontology.toml` as a guarded artifact,
   additive vs. breaking change classification documented, migration-CR requirement.

5. **Installer template** (proposed, CM to decide final scope):
   `syspilot.ontology.template.toml` offered at install time as a starter file.

**Safety architecture (three nets):**
- `sphinx-build -W` (every CR run, already enforced): catches any type/link
  mismatch immediately; provides incremental blast-radius reporting for free.
  A spec that doesn't match the ontology cannot pass the CM pipeline.
- Release Agent compare-mode (before squash-merge): last automated checkpoint.
- Governance Guardrail (process lock): spec-level, enforced by process.
CI gate on main is explicitly **not** used — too late, broken version already pushed.

**Out of scope:**
- Populating syspilot's own `ontology.toml` (follow-up CR).
- Blast-radius diff tool (separate later CR — sphinx-build -W covers the safety need).

**GitHub Issue:** #53

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

