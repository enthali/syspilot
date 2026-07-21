# Change Document: ontology-phase1

**Status**: ready-for-merge
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

**Status**: ✅ completed (reworked)

### Impacted User Stories

| ID | Impact | Notes |
|----|--------|-------|
| SYSP_US_ONTOLOGY_GOVERNANCE | AC-3 reworded | Removed generator --compare; now references sphinx-build -W |
| SYSP_US_ONTOLOGY_SKILL | AC-2 reworded | Removed generator docs; now references verification docs |

### New User Stories

| ID | Title | Priority |
|----|-------|----------|
| SYSP_US_ONTOLOGY_SINGLE_MASTER | Single-Master Ontology | mandatory |
| SYSP_US_ONTOLOGY_GOVERNANCE | Ontology Governance | mandatory |
| SYSP_US_ONTOLOGY_SKILL | Ontology Skill | mandatory |

### Removed (rescope)

| ID | Title | Reason |
|----|-------|--------|
| SYSP_US_ONTOLOGY_GENERATOR | Ontology Generator | Generator architecture removed; replaced by SYSP_US_ONTOLOGY_SINGLE_MASTER |

### Decisions

- Replaced GENERATOR US with SINGLE_MASTER US — the WHY is "one file, no projection" not "run a generator".
- GOVERNANCE and SKILL US reworded for flat-master safety model.

---

## Level 1: Requirements

**Status**: ✅ completed (reworked)

### Impacted Requirements

| ID | Impact | Notes |
|----|--------|-------|
| SYSP_REQ_ONTOLOGY_GOVERNANCE | AC-4 removed | Compare-mode gate no longer exists |
| SYSP_REQ_ONTOLOGY_SKILL | ACs reworded | Removed generator docs; now documents schema + governance only |

### New Requirements

| ID | Title | Links | Priority |
|----|-------|-------|----------|
| SYSP_REQ_ONTOLOGY_SINGLE_MASTER | Single-Master Ontology | SYSP_US_ONTOLOGY_SINGLE_MASTER | mandatory |
| SYSP_REQ_ONTOLOGY_GOVERNANCE | Ontology Governance | SYSP_US_ONTOLOGY_GOVERNANCE | mandatory |
| SYSP_REQ_ONTOLOGY_SKILL | Ontology Skill Content | SYSP_US_ONTOLOGY_SKILL | mandatory |

### Removed (rescope)

| ID | Title | Reason |
|----|-------|--------|
| SYSP_REQ_ONTOLOGY_GENERATOR | Ontology Generator | Replaced by SYSP_REQ_ONTOLOGY_SINGLE_MASTER |
| SYSP_REQ_RELEASE_ONTOLOGY_CHECK | Release Ontology Freshness Check | Compare-gate guarded two-file drift; drift eliminated by construction |

### Decisions

- SINGLE_MASTER replaces GENERATOR — the WHAT is "conf.py reads ontology.toml directly" not "run a generator".
- RELEASE_CHECK deleted entirely — it guarded a failure mode (stale projection) that no longer exists.

### Horizontal Check (MECE)

- [x] No contradictions with existing Requirements
- [x] No redundancies
- [x] All new REQs link to User Stories

---

## Level 2: Design

**Status**: ✅ completed (reworked)

### Impacted Design Elements

| ID | Impact | Notes |
|----|--------|-------|
| SYSP_SPEC_ONTOLOGY_SCHEMA | Rewritten | Flat master, no stripping/projection language |
| SYSP_SPEC_ONTOLOGY_DIRECTORY | Modified | Removed generator reference; added needs_from_toml note |
| SYSP_SPEC_ONTOLOGY_GOVERNANCE | Modified | Removed "Generator --compare" from Safety Nets |
| SYSP_SPEC_ONTOLOGY_SKILL_CONTENT | Modified | Removed Generator Invocation section; reduced to 5 sections |

### New Design Elements

| ID | Title | Links |
|----|-------|-------|
| SYSP_SPEC_ONTOLOGY_CONF | conf.py Ontology Configuration | SYSP_REQ_ONTOLOGY_SINGLE_MASTER |

### Removed (rescope)

| ID | Title | Reason |
|----|-------|--------|
| SYSP_SPEC_ONTOLOGY_GENERATOR | Ontology Generator Behaviour | No generator in flat-master architecture |

### Decisions

- SCHEMA spec rewritten: sphinx-needs reads the superset directly, no stripping.
- New SPEC_ONTOLOGY_CONF describes the `needs_from_toml` setting.
- SKILL_CONTENT reduced from 6 to 5 required sections (no Generator Invocation).
- GOVERNANCE Safety Nets reduced from 3 to 2 (sphinx-build -W + process).

### Horizontal Check (MECE)

- [x] No contradictions with existing Designs
- [x] All new SPECs link to Requirements

---

## Final Consistency Check

**Status**: ✅ passed

### Traceability Verification

| User Story | Requirements | Design | Complete? |
|------------|--------------|--------|-----------|
| SYSP_US_ONTOLOGY_SINGLE_MASTER | SYSP_REQ_ONTOLOGY_SINGLE_MASTER | SYSP_SPEC_ONTOLOGY_SCHEMA, SYSP_SPEC_ONTOLOGY_CONF | ✅ |
| SYSP_US_ONTOLOGY_GOVERNANCE | SYSP_REQ_ONTOLOGY_GOVERNANCE | SYSP_SPEC_ONTOLOGY_GOVERNANCE | ✅ |
| SYSP_US_ONTOLOGY_SKILL | SYSP_REQ_ONTOLOGY_SKILL | SYSP_SPEC_ONTOLOGY_SKILL_CONTENT | ✅ |

### Artefakt-Removal-Check

Grep for removed IDs in spec tree — **clean**, no stale references remain in RST files:

- `SYSP_US_ONTOLOGY_GENERATOR` — 0 hits in docs/syspilot/
- `SYSP_REQ_ONTOLOGY_GENERATOR` — 0 hits in docs/syspilot/
- `SYSP_SPEC_ONTOLOGY_GENERATOR` — 0 hits in docs/syspilot/
- `SYSP_REQ_RELEASE_ONTOLOGY_CHECK` — 0 hits in docs/syspilot/

(Change Document itself contains historical references in QM Findings — acceptable.)

### Issues Found

- **Stray working-tree changes (discarded):** `.github/agents/syspilot.setup.agent.md` and `.github/agents/syspilot.pm.agent.md` had unrelated modifications on checkout — discarded by CM. Not part of this CR.
- **Rescope (PM review before merge):** Generator/projection architecture replaced with flat single-master. See Summary Rescope Note. All stale prose references in architecture.md, workflows.md, conventions.md, and ontology.toml fixed in same branch.

### Sign-off

- [x] All levels completed
- [x] All conflicts resolved
- [x] Traceability verified
- [x] Artefakt-removal verified
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

### Round 3 (post-rescope)

**Reviewed by:** MECE Engineer + Trace Engineer
**Review date:** 2026-07-21

#### Findings

| # | Level | Element ID | Finding | Severity |
|---|-------|------------|---------|----------|
| 1 | prose | architecture.md, workflows.md, conventions.md, ontology.toml | 4 stale prose references still described removed generator/projection architecture | medium |

#### CM Decisions

| # | Finding # | Decision | Rationale |
|---|-----------|----------|-----------|
| 1 | 1 | fix-now | All 4 stale references updated by Documentation Engineer (commit a126c35) |

Spec-tree MECE + Trace: **clean** — no MECE violations, no dangling links, full traceability.

---

### Round 4 (post-rescope, independent)

**Reviewed by:** Quality Manager (independent verification)
**Review date:** 2026-07-21

#### Note on prior rounds

Round 2's clean sign-off (generator architecture) is superseded by the rescope —
those elements (`SYSP_US/REQ/SPEC_ONTOLOGY_GENERATOR`, `SYSP_REQ_RELEASE_ONTOLOGY_CHECK`,
`docs/ubproject.toml`, `generate_ubproject.py`, Release Agent step 7) no longer exist.
This round independently re-reviews the current (flat single-master) state from scratch;
Round 2 is historical record only.

#### Findings

| # | Severity | Level | Element | Issue |
|---|----------|-------|---------|-------|
| 1 | LOW-MEDIUM | prose | docs/architecture.md:202 | Section heading still reads `## Ontology Architecture *(Phase 0: spec · Phase 1: generator infrastructure)*` — contradicts the "Phase 1: Flat-Master Architecture" subsection immediately below it in the same file, which correctly describes the no-generator design. Missed by the Round 3 stale-prose fix (commit a126c35). |

#### Independent checks performed (all clean)

- `sphinx-build -W`: exit 0 (0 warnings) — contradicts the commit message's claim of "pre-existing -W warnings on branch"; actual current state is fully clean.
- Structural deletion confirmed: `docs/ubproject.toml` and `syspilot/sphinx/generate_ubproject.py` do not exist.
- `docs/conf.py:76` — `needs_from_toml = "../.syspilot/ontology.toml"` confirmed.
- Release Agent workflow reverted to original 12 steps; no ontology reference; step numbering consistent (squash-merge is step 7, matching pre-Phase-1 baseline).
- Repo-wide grep (md/rst/toml/py) for all 4 removed IDs + `generate_ubproject`/`ubproject.toml`: zero hits outside this CD's own historical log and specs that explicitly state "no longer exists."
- `SYSP_SPEC_ONTOLOGY_SCHEMA`, `SYSP_SPEC_ONTOLOGY_CONF`, `SYSP_SPEC_ONTOLOGY_GOVERNANCE` content reviewed — internally consistent, correctly describes flat-master / no-projection model.
- `.syspilot/ontology.toml` content matches schema description (`[syspilot]` header + `[needs]` table).
- `syspilot/skills/syspilot.ontology/SKILL.md` — zero generator/compare-mode references remaining.

#### PM Decisions

| # | Finding # | Decision | Rationale |
|---|-----------|----------|-----------|
| 1 | 1 | fix-now | One-line heading in architecture.md is self-contradictory (says "generator infrastructure" while the body below correctly describes the flat-master design). A misleading heading in a published doc is not acceptable at merge; the fix is trivial. |

---

*Generated by syspilot Change Agent*

