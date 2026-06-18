# Change Document: calver-release-versioning

**Status**: ready-for-merge
**Branch**: feature/calver-release-versioning
**Created**: 2026-06-18
**Author**: PM
**Operation Mode**: autonomous

---

## Summary

Replace semver (`0.6.x`) with date-based versioning (CalVer, `YYYY.MM.DD`). The Release Agent writes the release date as the version string. No Major/Minor/Patch judgment call needed. Closes GitHub issue #25.

---

## WHY

semver requires a subjective scope judgment on every release (patch vs. minor vs. major). For syspilot there is no public API that breaks — the distinction is meaningless. Worse, version numbers leak into CRs and Change Documents before the release date is known, causing the recurring "version-labeling leak" problem.

CalVer solves this structurally: the version is the release date, which no agent can know before the release actually happens.

Field evidence: Bosch internal adoption of syspilot already uses date-based versioning.

---

## WHAT

Update the Release Agent spec and agent file to use `YYYY.MM.DD` as the version string. The `v` prefix is retained (`v2026.06.18`). For two releases on the same day: `v2026.06.18.1`, `v2026.06.18.2`.

No changes to sphinx-needs `version:` field semantics — the value format changes, the field does not.

---

## Acceptance Criteria

- Release Agent spec describes CalVer format `vYYYY.MM.DD` as the version scheme
- Release Agent spec describes collision handling (`vYYYY.MM.DD.N` suffix)
- Release Agent agent file reflects the updated versioning rule
- `docs/releasenotes.md` documents the versioning scheme change
- `docs/methodology.md` updated if it references semver
- No other files reference semver as the syspilot versioning scheme

---

## Level 0: User Stories

**Status**: ✅ completed

### Impacted User Stories

None — the user intent "Release Engineer produces tagged releases" is unchanged; only the format of the version string changes.

### New User Stories

None.

### Decisions

- Decision 1: Mini-CR. No L0 changes. The user story `SYSP_US_RELEASE` covers "release is published with a tag" — that intent is unchanged. The version format is an implementation detail of the Release Workflow, not a user-visible goal.

### Horizontal Check (MECE)

- [x] No contradictions with existing User Stories
- [x] No redundancies
- [x] Gaps identified and addressed

---

## Level 1: Requirements

**Status**: ✅ completed

### Impacted Requirements

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| `SYSP_REQ_RELEASE_WORKFLOW` | `SYSP_US_RELEASE` | no text change | AC-2 ("reads current version…bumps it") is format-agnostic; wording remains valid for CalVer |

### New Requirements

None.

### Decisions

- Decision 1: No L1 text changes required. `SYSP_REQ_RELEASE_WORKFLOW` AC-2 says "reads the current version…and bumps it there" — this is format-agnostic and correct for CalVer. The CalVer format is a design-level detail.

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
| `SYSP_SPEC_RELEASE_WORKFLOW` | `SYSP_REQ_RELEASE_WORKFLOW` | modified | Step 2 rewritten: CalVer format + collision handling |

### New Design Elements

None.

### Decisions

- Decision 1: Mini-CR — Design subagent not invoked; edit applied directly by CM.
- Decision 2: SYSP_SPEC_RELEASE_WORKFLOW Step 2 now describes CalVer `vYYYY.MM.DD`, collision suffix `vYYYY.MM.DD.N`, and directs the agent to read the current `version:` field solely to detect same-day collisions.
- Decision 3: Agent file (`syspilot/agents/syspilot.release.agent.md`) updated in parallel with the SPEC — same wording.

### Horizontal Check (MECE)

- [x] No contradictions with existing Designs
- [x] All new SPECs link to Requirements

---

## Final Consistency Check

**Status**: ✅ passed

### Traceability Verification

| User Story | Requirements | Design | Complete? |
|------------|--------------|--------|-----------|
| `SYSP_US_RELEASE` | `SYSP_REQ_RELEASE_WORKFLOW` | `SYSP_SPEC_RELEASE_WORKFLOW` | ✅ |

### Artefakt-Removal-Check

No artefacts removed. The `SYSP_REQ_REL_SEMVER` example ID in `docs/syspilot/namingconventions.md` is a naming-convention illustration, not an active requirement. Its comment was updated from "semantic versioning" to "versioning scheme (CalVer)".

Historic semver label references in `docs/releasenotes.md` (entries describing past major/minor/patch releases) are accepted as Class (c) historical stranding — they accurately describe those past releases.

| Reference | Class | Disposition |
|-----------|-------|-------------|
| `docs/releasenotes.md` line 888: "Semantic versioning with pre-release support" | (c) historic | acceptable historic stranding |
| `docs/syspilot/namingconventions.md` SEMVER example comment | (b) doc | fixed — comment updated to "CalVer" |

- [x] All class (a) active code/workflow references fixed in this CR
- [x] All class (b) active documentation references fixed in this CR
- [x] Class (c) historical Change Documents accepted as "acceptable historic stranding" and disclosed above

### Issues Found

None.

### Sign-off

- [x] All levels completed (no ⚠️ DEPRECATED markers remaining)
- [x] All conflicts resolved
- [x] Traceability verified
- [x] Ready for implementation

---

## QM Findings

### Round 1

**Reviewed by:** QM  
**Review date:** 2026-06-18

#### Findings

No findings. MECE-L2 PASS: SYSP_SPEC_RELEASE_WORKFLOW Step 2 correctly specifies CalVer format `vYYYY.MM.DD` (e.g. `v2026.06.18`) with collision handling (`vYYYY.MM.DD.N` suffix). Trace PASS: chain SYSP_US_RELEASE → SYSP_REQ_RELEASE_WORKFLOW → SYSP_SPEC_RELEASE_WORKFLOW valid; AC-2 format-agnostic and correct. Schema: 0 sphinx-needs warnings. Cross-artefact: spec and agent Step 2 wording aligned.

#### PM Decisions

*(No findings — no decisions required.)*
