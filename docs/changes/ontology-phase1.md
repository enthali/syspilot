# Change Document: ontology-phase1

**Status**: in-progress
**Branch**: feature/ontology-phase1
**Created**: 2026-07-21
**Author**: Project Manager (triage + rescope), Change Manager (engineering)
**Operation Mode**: autonomous

---

## Summary

Phase 1 of the ontology-architecture-decision ADR (CR #49, merged). Phase 0
established that `.syspilot/ontology.toml` is the canonical, tooling-agnostic
ontology master and that sphinx-needs/ubCode is just one consumer. Phase 1
delivers the **capability**: a single canonical ontology file that feeds both
sphinx-needs and (in later phases) the agents — without yet populating the
syspilot-specific sections (that is Phase 2, #54).

**Architecture: one flat master, no projection.** `.syspilot/ontology.toml` is a
superset holding both the `[needs]` table (the sphinx-needs / ubProject schema)
and `[syspilot.*]` sections (syspilot-only metadata: actors/ownership, lifecycle,
V&V — populated from Phase 2 on). sphinx-needs is pointed at this file directly
and reads only `[needs]`, ignoring the `[syspilot.*]` siblings. There is no
generated `docs/ubproject.toml`, no generator, and no projection step.

**Deliverables:**

1. **Single ontology master** — `.syspilot/ontology.toml` as the one canonical
   source read by both sphinx-needs and (later) the agents.
2. **sphinx-needs pointed directly at the master** — no intermediate projection file.
3. **`syspilot.ontology` skill** (read by the System Designer) — schema
   documentation, the "sphinx-needs reads only `[needs]`, ignores siblings"
   convention, and the governance guardrail (guarded artifact + additive/breaking
   change classification + migration-CR requirement). Slimmed: no generator, no
   compare mode, no staging.
4. **Governance Guardrail** at spec level — `ontology.toml` as a guarded artifact,
   additive vs. breaking change classification, migration-CR requirement.

**Safety architecture (two nets):**
- `sphinx-build -W` (every CR, already enforced) — now validates the master
  **directly**: a malformed ontology, or a spec referencing a missing type/link,
  cannot pass the CM pipeline. Earlier and stronger than a release-time gate.
- Governance Guardrail (process lock) — spec-level, enforced by process.

**Rescope note (2026-07-21, PM review before merge).** This CR originally
delivered a *staged* ontology — a superset master projected by a generator down
to a stripped `docs/ubproject.toml`, guarded by a Release Agent compare-gate.
Review established that the staging solved a consumer-intolerance problem that
does not exist here: sphinx-needs reads a single configured table (`[needs]`) and
ignores siblings, so the superset can be consumed directly; and ubCode — the only
other candidate consumer — is not in use in this project. The generator, the
projection file, and the release compare-gate were therefore removed as
over-engineering. Safety is preserved: the removed gate guarded *two-file drift*,
a failure mode now eliminated by construction, while `sphinx-build -W` already
validates the single master every CR. Should a future consuming project run a
strict ubCode needing a stripped projection, that generator becomes **that
project's tailoring**, not syspilot core.

**Out of scope (unchanged / clarified):**
- Populating `[syspilot.*]` (actors/ownership, capabilities, process, V&V) → Phase 2 (#54).
- Agents consuming the ontology → Phase 3 (#57).
- Blast-radius diff tool → Phase 4 (#55).
- Installer template — deferred (no syspilot ontology content to template yet).

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
| SYSP_REQ_RELEASE_ONTOLOGY_CHECK | Release Ontology Freshness Check | SYSP_US_ONTOLOGY_GENERATOR, SYSP_US_ONTOLOGY_GOVERNANCE, SYSP_US_RELEASE | mandatory |

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
| SYSP_SPEC_ONTOLOGY_SCHEMA | ontology.toml Concrete Schema | SYSP_REQ_ONTOLOGY_GENERATOR, SYSP_REQ_ONTOLOGY_CONFIG_AUTHORITY, SYSP_SPEC_ONTOLOGY_TOML_SCHEMA |
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

- **Stray working-tree change (discarded):** `.github/agents/syspilot.setup.agent.md` had an unrelated modification (added name/agent frontmatter fields + changed tools list) when CM checked out the branch. Discarded via `git checkout --`. Not part of this CR.
- **Installer template (scoped out):** CD Summary listed as "proposed, CM to decide." CM decision: deferred to Phase 2 — see Summary Out of Scope section.

### Sign-off

- [x] All levels completed (no ⚠️ DEPRECATED markers remaining)
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
**Review date:** 2026-07-21

#### Findings

| # | Level | Element ID | Finding | Severity |
|---|-------|------------|---------|----------|
| 1 | SKILL | syspilot.ontology/SKILL.md | Missing `implements`/`requirements` frontmatter (traceability convention) | low |
| 2 | L1 | SYSP_REQ_RELEASE_ONTOLOGY_CHECK | Missing `SYSP_US_RELEASE` in :links: | medium-low |
| 3 | - | (installer template) | Deliverable #5 neither implemented nor scoped out in CD | medium-low |
| 4 | L2 | SYSP_SPEC_ONTOLOGY_SCHEMA | No explicit link to SYSP_SPEC_ONTOLOGY_TOML_SCHEMA (Phase 0 continuity) | low |

#### CM Decisions

| # | Finding # | Decision | Rationale |
|---|-----------|----------|-----------|
| 1 | 1 | fix-now | Added `implements`/`requirements` frontmatter to SKILL.md |
| 2 | 2 | fix-now | Added `SYSP_US_RELEASE` to SYSP_REQ_RELEASE_ONTOLOGY_CHECK :links: |
| 3 | 3 | defer (Phase 2) | Installer template has no value without syspilot ontology.toml content; explicit scope-out added to CD |
| 4 | 4 | fix-now | Added `SYSP_SPEC_ONTOLOGY_TOML_SCHEMA` to SYSP_SPEC_ONTOLOGY_SCHEMA :links: |

---

### Round 2

**Reviewed by:** Quality Manager (independent verification)
**Review date:** 2026-07-21

#### Findings

None. All 4 CM Round 1 fixes independently confirmed correct:
- SKILL.md frontmatter (`implements`/`requirements`) present and correctly linked.
- `SYSP_REQ_RELEASE_ONTOLOGY_CHECK` links now include `SYSP_US_RELEASE`; AC-3 ordering matches Release Agent workflow (step 7 ontology check runs after validation/document, before step 8 squash-merge).
- `SYSP_SPEC_ONTOLOGY_SCHEMA` links to `SYSP_SPEC_ONTOLOGY_TOML_SCHEMA`.
- Installer template deferral to Phase 2 explicitly documented in CD Summary "Out of scope."

**Additional independent checks (all clean):**
- `python syspilot/sphinx/generate_ubproject.py --compare` → exit 0 ("OK: docs/ubproject.toml is up to date") — roundtrip claim verified live, not just trusted from commit message.
- `sphinx-build -W` → exit 0.
- `.gitignore` exception for `.syspilot/ontology.toml` present.
- Traceability for all 3 new US → 4 new REQ → 4 new/1 modified SPEC verified complete, no orphans.
- Release Agent workflow step ordering (validation → archive → version → document → **ontology check** → squash-merge) satisfies AC-3 ("after validation, before merge").

#### PM Decisions

| # | Finding # | Decision | Rationale |
|---|-----------|----------|-----------|

---

*Generated by syspilot Change Agent*

