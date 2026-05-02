# Change Document: release-explicit-sources

**Status**: in-progress
**Branch**: feature/release-explicit-sources
**Created**: 2026-05-02
**Author**: syspilot.cm

---

## Summary

The Release Agent's Archive and Document steps are given explicit, deterministic
data sources. Archive scans all `*.md` files in `docs/changes/` (excluding
subdirectories). Document generates release notes from the archived change docs
in `docs/changes/<version>/`. This prevents incomplete archival or release notes
due to session context drift.

---

## Change Request (from PM)

> **Mode:** autonomous
>
> **Intent (WHAT):**
> The Release Agent's Archive and Document steps shall explicitly define their
> data sources so no change documents are missed during a release.
>
> **Motivation (WHY):**
> In v0.5.2 the Release Agent skipped 5 change documents because neither the
> Archive step defines where to find them, nor the Document step defines what
> to generate notes from. The agent worked from session context instead of a
> deterministic file scan — resulting in incomplete archival and incomplete
> release notes.
>
> **Acceptance Criteria:**
> 1. The Archive step SHALL explicitly state: scan all `*.md` files in `docs/changes/` (excluding subdirectories) as the input set to be moved
> 2. The Document step SHALL explicitly state: use the archived change documents (now in `docs/changes/<version>/`) as the source for release notes generation
> 3. The release notes SHALL list ALL archived change documents, not only those known from the current session context

---

## Impact Analysis (CM)

**Performed**: 2026-05-02
**Method**: `get_need_links.py <id> --direction in --depth 1` from SYSP_US_RELEASE, then depth 1 from relevant REQs.

**From SYSP_US_RELEASE (relevant REQs):**
```
SYSP_REQ_RELEASE_DUTIES, SYSP_REQ_RELEASE_WORKFLOW
```

**From Release REQs (direct SPECs):**
```
SYSP_REQ_RELEASE_DUTIES   → SYSP_SPEC_RELEASE_DUTIES
SYSP_REQ_RELEASE_WORKFLOW → SYSP_SPEC_RELEASE_WORKFLOW
```

**In-scope elements:**
- SYSP_US_RELEASE
- SYSP_REQ_RELEASE_DUTIES, SYSP_REQ_RELEASE_WORKFLOW
- SYSP_SPEC_RELEASE_DUTIES, SYSP_SPEC_RELEASE_WORKFLOW

**Out of scope:** SOUL (character, not affected). FRONTMATTER.

**Agent file in scope:**
- `syspilot/agents/syspilot.release.agent.md`

---

## Process Log

| Step | Agent | Status | Commit | Notes |
|------|-------|--------|--------|-------|
| Branch created | CM | ✅ | — | feature/release-explicit-sources |
| Impact Analysis | CM | ✅ | — | See section above |
| Change Document | CM | ✅ | — | This file |
| Design (L0) | syspilot.design | ✅ | — | — |
| Design (L1) | syspilot.design | ✅ | — | — |
| Design (L2) | syspilot.design | ✅ | — | — |
| Implement | syspilot.implement | ✅ | 2f51482 | — |
| Verify | syspilot.verify | ⏳ | — | — |
| PM Approval | PM | ⏳ | — | — |
| Merged | CM | ⏳ | — | — |

---

## Level 0: User Stories

**Status**: ✅ done

### Impacted User Stories

| ID | Title | Impact | Notes |
|----|-------|--------|-------|
| `SYSP_US_RELEASE` | Release Engineer Agent | modified | Explicit data sources for Archive + Document steps |

### Designer Section

**Decision:** AC-4 was split into two separate acceptance criteria to express the two distinct completeness concerns:
- **AC-4 (modified):** Archive completeness — ALL `*.md` files in `docs/changes/` root (no subdirectories) must be moved; none missed.
- **AC-5 (new):** Documentation completeness — Release notes generated from archived docs in `docs/changes/<version>/`; every archived document listed.

**Rationale:** The original single AC-4 covered both archival and notes in one vague statement. Splitting them makes each concern independently verifiable and directly maps down to L1 duties/workflow.

**Status set to:** `draft` (will be approved after final consistency check).

---

## Level 1: Requirements

**Status**: ✅ done

### Impacted Requirements

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| `SYSP_REQ_RELEASE_DUTIES` | `SYSP_US_RELEASE` | modified | Archive duty: scan docs/changes/*.md; Document duty: use archived docs |
| `SYSP_REQ_RELEASE_WORKFLOW` | `SYSP_US_RELEASE` | modified | Archive step: file scan; Document step: archived docs as source |

### Designer Section

**SYSP_REQ_RELEASE_DUTIES:**
- **AC-4 (modified):** "scan ALL `*.md` files in `docs/changes/` root (excluding subdirectories)" — replaces vague "can archive change documents".
- **AC-3 (modified):** "using all archived change documents in `docs/changes/<version>/` as the sole source; every archived document MUST appear" — replaces vague "can generate and update release notes".

**SYSP_REQ_RELEASE_WORKFLOW:**
- **AC-1 (modified):** Workflow prep step now states `archive = scan docs/changes/*.md` and `release notes from archived docs` — making the data sources explicit in the workflow trigger.
- **AC-7 (new):** Document step explicitly requires: use `docs/changes/<version>/` as source; list ALL archived documents, not only session-known ones.

**Status set to:** `draft` (both elements).

---

## Level 2: Design

**Status**: ✅ done

### Impacted Design Elements

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| `SYSP_SPEC_RELEASE_DUTIES` | `SYSP_REQ_RELEASE_DUTIES` | modified | Explicit scan + source definition |
| `SYSP_SPEC_RELEASE_WORKFLOW` | `SYSP_REQ_RELEASE_WORKFLOW` | modified | Archive step: scan; Document step: archived docs |

### Designer Section

**SYSP_SPEC_RELEASE_DUTIES:**
- **Duty 1 (Archive, modified):** Now states: "Scan ALL `*.md` files in `docs/changes/` (root only — do not recurse) and move every found file to `docs/changes/<version>/`. The scan is the definitive input set; session context is not used."
- **Duty 3 (Release Notes, modified):** Now states: "using ALL change documents found in `docs/changes/<version>/` as the explicit source; every archived document MUST have an entry — no document may be omitted due to session context drift."

**SYSP_SPEC_RELEASE_WORKFLOW:**
- **Step 3 (Archive, modified):** Specifies exact scan command pattern (`Get-ChildItem docs/changes/ -Filter *.md -File` or equivalent); file-system scan is authoritative; session context MUST NOT be used.
- **Step 5 (Document, modified):** Reads ALL files in `docs/changes/<version>/`; every file produces an entry; directory listing is authoritative; session context MUST NOT be used.

**MECE advisory:** Changes are additive (new constraints on existing elements). No new elements introduced. Horizontal coverage: Archive completeness + Document completeness are two distinct, non-overlapping concerns — both covered. No gaps introduced.

**Status set to:** `draft` (both elements).

---

## Final Consistency Check

**Status**: ✅ done

### Traceability Verification

| Chain | Status |
|-------|--------|
| SYSP_US_RELEASE → SYSP_REQ_RELEASE_DUTIES → SYSP_SPEC_RELEASE_DUTIES | ✅ |
| SYSP_US_RELEASE → SYSP_REQ_RELEASE_WORKFLOW → SYSP_SPEC_RELEASE_WORKFLOW | ✅ |

All modified elements set to `:status: approved`.

---

## Sign-off

- [ ] Design approved by user
- [ ] Implementation complete
- [ ] Verify passed
- [ ] PM approval received
- [ ] Merged to development
