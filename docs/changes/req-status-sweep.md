# Change Document: req-status-sweep

**Status**: ready-for-merge
**Branch**: feature/req-status-sweep
**Created**: 2026-05-23
**Author**: PM
**Operation Mode**: autonomous

---

## Summary

Elevate `:status:` from `draft` to `approved` on every REQ in `docs/syspilot/requirements/req_setup_engineer.rst` whose child SPECs already carry `:status: approved`. Today the file is full of draft REQs while their downstream SPECs were elevated to approved by recent CRs (CR-B, CR-C, installer-spec-rewrite) — a structural hierarchy violation surfaced by QM as T-F1 on installer-spec-rewrite. **Motivation**: a draft REQ cannot legitimately authorise an approved child SPEC; the hierarchy must hold both ways. **Acceptance criteria**: (AC1) Every REQ in `req_setup_engineer.rst` that has ANY child SPEC at `:status: approved` is itself at `:status: approved`. (AC2) Any REQ that is intentionally kept at `:status: draft` carries a one-line justification recorded in the CD. (AC3) No semantic changes to REQ content — this is pure status hygiene; the REQ wording, IDs, and links remain identical. (AC4) Scope is limited to `req_setup_engineer.rst`; other requirement files are out of scope. (AC5) sphinx-build remains clean after the sweep (no new schema warnings).

---

## Level 0: User Stories

**Status**: ✅ completed

### Impacted User Stories

None — this CR makes no semantic change. Pure metadata hygiene on existing REQs (per AC3).

### New User Stories

None.

### Decisions

- Decision 1: No L0 changes. Status hygiene is a process-internal correction; no user-facing intent changes.

### Horizontal Check (MECE)

- [x] No contradictions with existing User Stories
- [x] No redundancies
- [x] Gaps identified and addressed (no gap; no new US needed)

---

## Level 1: Requirements

**Status**: ✅ completed

### Impacted Requirements

Audit of every REQ in `docs/syspilot/requirements/req_setup_engineer.rst` against AC1 (REQ status must be `approved` when ANY child SPEC is `approved`):

| REQ | Status before | Child SPEC(s) | Child status | Action |
|-----|---------------|---------------|--------------|--------|
| `SYSP_REQ_SETUP_SOUL` | draft | `SYSP_SPEC_SETUP_SOUL` | draft | keep draft |
| `SYSP_REQ_INSTALLER_DUTIES` | approved | `SYSP_SPEC_INSTALLER_DUTIES` | approved | unchanged |
| `SYSP_REQ_INSTALLER_WORKFLOW` | approved | `SYSP_SPEC_INSTALLER_WORKFLOW` | approved | unchanged |
| `SYSP_REQ_INSTALLER_GITHUB_SOURCE` | approved | `SYSP_SPEC_INSTALLER_GITHUB_SOURCE` | approved | unchanged |
| `SYSP_REQ_INSTALLER_ENCODING` | approved | `SYSP_SPEC_INSTALLER_ENCODING` | approved | unchanged |
| `SYSP_REQ_INSTALLER_DIRECT_OPS` | approved | `SYSP_SPEC_INSTALLER_DIRECT_OPS` | approved | unchanged |
| `SYSP_REQ_INSTALLER_ROLLBACK` | approved | `SYSP_SPEC_INSTALLER_ROLLBACK` | approved | unchanged |
| `SYSP_REQ_INSTALLER_SCOPE` | draft | `SYSP_SPEC_INSTALLER_SCOPE` | draft | keep draft |
| `SYSP_REQ_INSTALLER_DOC_BOOTSTRAP` | draft | `SYSP_SPEC_INSTALLER_DOC_BOOTSTRAP` | draft | keep draft |
| `SYSP_REQ_SETUP_BOOTLOADER_DUTIES` | draft | `SYSP_SPEC_SETUP_DUTIES` | draft | keep draft |
| `SYSP_REQ_SETUP_FRONTMATTER` | approved | `SYSP_SPEC_SETUP_FRONTMATTER` | approved | unchanged |
| `SYSP_REQ_SETUP_PROMPT` | draft | (no individual L2 SPEC; aggregated in `SYSP_SPEC_AGENT_ARCH_PROMPT`) | n/a | keep draft |
| `SYSP_REQ_SETUP_BOOTLOADER_FETCH` | draft | `SYSP_SPEC_SETUP_WORKFLOW` | draft | keep draft |
| `SYSP_REQ_SETUP_BOOTLOADER_INVOKE` | draft | `SYSP_SPEC_SETUP_WORKFLOW` | draft | keep draft |
| `SYSP_REQ_SETUP_BOOTLOADER_VERSION` | draft | `SYSP_SPEC_SETUP_WORKFLOW` | draft | keep draft |
| **`SYSP_REQ_SETUP_INSTALLER_NOT_USER_INVOCABLE`** | **draft** | `SYSP_SPEC_INSTALLER_SOUL` (approved); `SYSP_SPEC_INSTALLER_FRONTMATTER` (approved) | **all approved** | **FLIP → approved** |
| `SYSP_REQ_SETUP_SKILL_MUTEX` | draft | `SYSP_SPEC_INSTALLER_SKILL_MUTEX` | draft | keep draft |

### New Requirements

None (AC3: no semantic changes).

### Intentionally Kept Draft (per AC2)

The following REQs remain `:status: draft` because their child SPEC(s) are also still `:status: draft` — status hygiene at this CR is unidirectional (child approved → parent approved). Elevation will follow naturally when each subsystem's L2 SPECs are themselves elevated by a future CR:

- `SYSP_REQ_SETUP_SOUL`, `SYSP_REQ_INSTALLER_SCOPE`, `SYSP_REQ_INSTALLER_DOC_BOOTSTRAP`, `SYSP_REQ_SETUP_BOOTLOADER_DUTIES`, `SYSP_REQ_SETUP_BOOTLOADER_FETCH`, `SYSP_REQ_SETUP_BOOTLOADER_INVOKE`, `SYSP_REQ_SETUP_BOOTLOADER_VERSION`, `SYSP_REQ_SETUP_SKILL_MUTEX`: child SPEC still draft.
- `SYSP_REQ_SETUP_PROMPT`: no individual L2 SPEC element exists (aggregated in `SYSP_SPEC_AGENT_ARCH_PROMPT`); cannot determine child status from the spec_setup_engineer file. Conservatively kept draft.

### Conflicts Detected

None.

### Decisions

- Decision 1: Apply AC1 strictly — only flip REQs whose child SPECs are ALL approved. REQs with any draft child SPEC remain draft.
- Decision 2: This CR is one-shot for the Installer subsystem. A future CR that elevates SCOPE / DOC_BOOTSTRAP / SKILL_MUTEX SPECs to approved will need a follow-up sweep on their parent REQs.
- Decision 3: Scope limited to `req_setup_engineer.rst` per AC4. Other requirement files (req_change_mgr.rst, req_project_mgr.rst, req_system_designer.rst, etc.) are out of scope; a future broader-sweep CR may address them.

### Horizontal Check (MECE)

- [x] No contradictions with existing Requirements
- [x] No redundancies
- [x] All REQs examined; classification complete

---

## Level 2: Design

**Status**: ✅ completed

### Impacted Design Elements

None — this CR makes no L2 changes (AC3: no semantic changes; only L1 metadata).

### New Design Elements

None.

### Conflicts Detected

None.

### Decisions

- Decision 1: L2 is untouched. The CR's purpose is to bring L1 status into alignment with already-approved L2 — a one-way correction.

### Horizontal Check (MECE)

- [x] No contradictions with existing Designs
- [x] No L2 changes — nothing to MECE-check at this level

---

## Final Consistency Check

**Status**: ✅ passed

### Traceability Verification

| CR AC | Coverage |
|-------|----------|
| AC1 | Single REQ flipped: `SYSP_REQ_SETUP_INSTALLER_NOT_USER_INVOCABLE` draft → approved (both child SPECs already approved). Verified via grep of `:status: draft` in req_setup_engineer.rst after edit: the matching REQ is no longer draft. |
| AC2 | 9 REQs intentionally kept draft are listed in L1 "Intentionally Kept Draft" subsection with justification ("child SPEC still draft" / "no individual L2 SPEC"). |
| AC3 | Diff verified: only the `:status:` line changed; no REQ wording, IDs, links, ACs, or descriptions altered. |
| AC4 | Scope confined to `req_setup_engineer.rst`. No other requirement file touched. |
| AC5 | sphinx-build clean (1 pre-existing unrelated warning; 0 new schema warnings). |

### Artefakt-Removal-Check

No artefact removal in this CR — only a single `:status:` value flip. Check informational only.

- [x] No artefact removed; check is informational only

### Issues Found

None.

### Sign-off

- [x] All levels completed
- [x] All conflicts resolved
- [x] Traceability verified (5/5 ACs)
- [x] sphinx-build clean
- [x] Ready for QM targeted check + PM merge to development

---

## Appendix: Link Discovery Results

```
{paste output from get_need_links.py as needed}
```

---

*Generated by syspilot Change Agent*
