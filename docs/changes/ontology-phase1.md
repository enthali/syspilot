# Change Document: ontology-phase1

**Status**: in-progress
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

**Status**: ✅ completed

### Impacted User Stories

None — greenfield addition. Phase 0 elements (SYSP_US_ONTOLOGY_ARCH, SYSP_US_ONTOLOGY_TEMPLATES) are read-only context.

### New User Stories

| ID | Title | Priority |
|----|-------|----------|
| SYSP_US_ONTOLOGY_GENERATOR | Ontology Generator | mandatory |
| SYSP_US_ONTOLOGY_GOVERNANCE | Ontology Governance | mandatory |
| SYSP_US_ONTOLOGY_SKILL | Ontology Skill | mandatory |

### Decisions

- Three separate US for generator, governance, and skill — each has a distinct WHY.
- Added to existing us_ontology_arch.rst (same file family, not a new RST file).

### Horizontal Check (MECE)

- [x] No contradictions with existing User Stories
- [x] No redundancies
- [x] Gaps identified and addressed

---

## Level 1: Requirements

**Status**: ✅ completed

### Impacted Requirements

None.

### New Requirements

| ID | Title | Links | Priority |
|----|-------|-------|----------|
| SYSP_REQ_ONTOLOGY_GENERATOR | Ontology Generator | SYSP_US_ONTOLOGY_GENERATOR | mandatory |
| SYSP_REQ_ONTOLOGY_GOVERNANCE | Ontology Governance | SYSP_US_ONTOLOGY_GOVERNANCE | mandatory |
| SYSP_REQ_ONTOLOGY_SKILL | Ontology Skill Content | SYSP_US_ONTOLOGY_SKILL | mandatory |
| SYSP_REQ_RELEASE_ONTOLOGY_CHECK | Release Ontology Freshness Check | SYSP_US_ONTOLOGY_GENERATOR, SYSP_US_ONTOLOGY_GOVERNANCE | mandatory |

### Conflicts Detected

None.

### Decisions

- SYSP_REQ_RELEASE_ONTOLOGY_CHECK links to both GENERATOR and GOVERNANCE US — it straddles both concerns (tooling + process).
- Added to existing req_ontology_arch.rst.

### Horizontal Check (MECE)

- [x] No contradictions with existing Requirements
- [x] No redundancies
- [x] All new REQs link to User Stories

---

## Level 2: Design

**Status**: ✅ completed

### Impacted Design Elements

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| SYSP_SPEC_ONTOLOGY_DIRECTORY | SYSP_REQ_ONTOLOGY_DIRECTORY | modified | Updated layout to show generator; added generator reference |

### New Design Elements

| ID | Title | Links |
|----|-------|-------|
| SYSP_SPEC_ONTOLOGY_SCHEMA | ontology.toml Concrete Schema | SYSP_REQ_ONTOLOGY_GENERATOR, SYSP_REQ_ONTOLOGY_CONFIG_AUTHORITY |
| SYSP_SPEC_ONTOLOGY_GENERATOR | Ontology Generator Behaviour | SYSP_REQ_ONTOLOGY_GENERATOR |
| SYSP_SPEC_ONTOLOGY_GOVERNANCE | Ontology Governance Rules | SYSP_REQ_ONTOLOGY_GOVERNANCE |
| SYSP_SPEC_ONTOLOGY_SKILL_CONTENT | Ontology Skill Content | SYSP_REQ_ONTOLOGY_SKILL |

### Conflicts Detected

None.

### Decisions

- ontology.toml uses `[needs]` as the ubCode pass-through key and `[syspilot]` for syspilot-only metadata. Generator strips everything not under `needs`.
- Phase 1 minimal syspilot content: just `schema_version = "1.0"` — actors/capabilities/process deferred to Phase 2+.
- Generator works on raw text (not parsed TOML) to preserve comments and formatting.
- Generator exit codes: 0 = match, 1 = diff, 2 = input error.
- Skill file created at syspilot/skills/syspilot.ontology/SKILL.md.

### Horizontal Check (MECE)

- [x] No contradictions with existing Designs
- [x] All new SPECs link to Requirements

---

## Final Consistency Check

**Status**: ✅ passed

### Traceability Verification

| User Story | Requirements | Design | Complete? |
|------------|--------------|--------|-----------|
| SYSP_US_ONTOLOGY_GENERATOR | SYSP_REQ_ONTOLOGY_GENERATOR, SYSP_REQ_RELEASE_ONTOLOGY_CHECK | SYSP_SPEC_ONTOLOGY_SCHEMA, SYSP_SPEC_ONTOLOGY_GENERATOR | ✅ |
| SYSP_US_ONTOLOGY_GOVERNANCE | SYSP_REQ_ONTOLOGY_GOVERNANCE, SYSP_REQ_RELEASE_ONTOLOGY_CHECK | SYSP_SPEC_ONTOLOGY_GOVERNANCE | ✅ |
| SYSP_US_ONTOLOGY_SKILL | SYSP_REQ_ONTOLOGY_SKILL | SYSP_SPEC_ONTOLOGY_SKILL_CONTENT | ✅ |

### Artefakt-Removal-Check

Not applicable — no artefacts removed.

### Issues Found

- `.github/agents/syspilot.setup.agent.md` had a stray modification (added name/agent frontmatter fields + changed tools list) in the working tree on checkout. Discarded by CM via `git checkout --`. Not part of this CR.

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

