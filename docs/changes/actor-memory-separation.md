# Change Contract: Actor Memory Separation

**Status:** closed<br>
**Process owner:** Syspilot Project Manager<br>
**Current responsibility:** Syspilot Project Manager<br>
**Current blocker:** none<br>
**Created:** 2026-08-26<br>
**Branch:** feature/actor-memory-separation<br>
**Collaboration mode:** User-guided. The User directly requested removal of the two remaining actor Context files from the public repository after confirming their migration to the private actor-memory repository.

## Intent And Outcome

**Owner:** Syspilot Project Manager<br>
**Status:** approved<br>
**Approval evidence:** The User directly requested the public removal on 2026-08-26 after the private migration completed at `5919368`.

### Goal

Stop the public Syspilot repository from tracking the Architect and Technical Writer Context files while preserving both files in the private actor-memory repository and at Jarvis's local runtime path.

### Value

Actor memory remains private without changing Jarvis path resolution or deleting the migrated local memory graphs.

### Scope

- Remove `.jarvis/actors/Syspilot Architect/context.md` and `.jarvis/actors/Syspilot Technical Writer/context.md` from the public Git index without deleting either local file.
- Verify that both files remain tracked in the private `.jarvis/actors` repository on `main`.
- Do not modify actor memory content, the unrelated untracked `.github/agents/` directory, or Jarvis runtime state.
- Do not push either repository without explicit User authorization.

### Observable Outcome

The public repository no longer lists either Context file, while the private repository lists both at commit `5919368` or a descendant and both files remain present on disk.

## Artifact Applicability And Ownership

**Applicability:** Each artifact owner decides and updates its own row.<br>
**Status:** complete

| Artifact type | Included | Owner | Completion evidence | Status |
|---|---|---|---|---|
| Intent and outcome | yes | Syspilot Project Manager | Goal, boundaries, and observable outcome are explicit and User-approved | approved |
| Product specification and architecture decisions | yes | Syspilot Architect | Exact public index-only removal, private prerequisite, local preservation, ignore behavior, and scope guards are verified | complete |
| User-facing documentation | not applicable: no product behavior or user guidance changes | Syspilot Technical Writer | Public tracking cleanup has no user-facing documentation surface | not applicable |
| Implementation and unit verification | yes | Syspilot Developer | Exactly the two public Context entries are staged as deletions; both files remain local and private-tracked on clean private `main` | complete |
| Acceptance test design and results | yes | Syspilot Tester | Black-box repository checks demonstrate the observable outcome | passed |
| Quality review | yes | Syspilot Quality | Independent repository-boundary review confirmed exact public removal, private and local preservation, and bounded scope; judgment is `proceed` | proceed |
| User validation and approval | yes | User | User directly accepted the demonstrated public/private separation on 2026-08-26 | accepted |
| Closure decision | yes | Syspilot Project Manager | Validation and integration are recorded | complete |

## Architecture And Specification

**Owner:** Syspilot Architect<br>
**Status:** complete

### Affected Artifacts

| Artifact | Change | Rationale |
|---|---|---|
| `.jarvis/actors/Syspilot Architect/context.md` | remove from public index only | The private actor-memory repository owns the migrated Architect context at the same local path |
| `.jarvis/actors/Syspilot Technical Writer/context.md` | remove from public index only | The private actor-memory repository owns the migrated Technical Writer context at the same local path |

### Decisions And Evidence

| Decision or check | Evidence |
|---|---|
| Repository boundary | `git rev-parse --show-toplevel` resolves to the workspace root, while `git -C .jarvis/actors rev-parse --show-toplevel` resolves to `.jarvis/actors`; the public and private indexes are independent despite sharing local file paths |
| Public removal mechanism | From the workspace repository, run `git rm --cached --` with exactly the two Context paths; index-only removal stages public deletions without deleting their shared working-tree files or changing private tracking |
| Local persistence after public removal | `.gitignore` ignores `.jarvis/`; `git check-ignore -v --no-index` resolves both Context paths to that rule, so the retained local files do not reappear as public untracked content |
| Private migration prerequisite | Private `main` is clean at `5919368`, that commit is an ancestor of private `HEAD`, and private `git ls-files` lists both Context files |
| Current public prerequisite | Public `git ls-files` lists exactly both target Context paths before implementation, and both files are present on disk |
| Scope guard | Stage and verify exactly the two public deletions; do not operate on the private index, actor-memory content, `.github/agents/`, Jarvis runtime state, or either remote |
| Product impact | No Sphinx-Needs specification or user-facing behavior changes: this Change removes duplicate public index ownership only, so no product Requirement or documentation artifact is affected |

## User-Facing Documentation

**Owner:** Syspilot Technical Writer<br>
**Status:** not applicable

No product behavior or user-facing documentation changes.

## Implementation And Unit Verification

**Owner:** Syspilot Developer<br>
**Status:** complete

### Decisions And Evidence

| Decision | Chosen approach | Relevant alternatives | Rationale and evidence |
|---|---|---|---|
| Public removal method | `git rm --cached` for the two exact paths | Delete files from disk | Index-only removal preserves Jarvis's local private memory path |

### Changed Artifacts And Verification

| Artifact | Change | Verification evidence |
|---|---|---|
| `.jarvis/actors/Syspilot Architect/context.md`, `.jarvis/actors/Syspilot Technical Writer/context.md` | Removed from the public index only with `git rm --cached`; local files and private memory content were not modified | Public staged scope contains exactly two deletions and passes `git diff --cached --check`; both `Test-Path` checks pass; private `main` at `5919368` remains clean and `git ls-files` lists both files; `.gitignore` covers both through `.jarvis/`; `.github/agents/` remains untouched |

## Acceptance Testing

**Owner:** Syspilot Tester<br>
**Status:** passed

| Scenario | Traces to | Result | Evidence |
|---|---|---|---|
| Public repository no longer tracks either Context file | observable outcome | pass | Black-box checks confirmed neither path exists in the public index or `HEAD` tree and both resolve to the public `.jarvis/` ignore rule |
| Private repository still tracks both files and both remain on disk | observable outcome | pass | Both local files exist and their blobs equal the corresponding private migration-baseline blobs; private `HEAD` remains exactly `5919368` on clean `main` and tracks both paths |
| Unrelated `.github/agents/` and Jarvis runtime state remain untouched | scope boundary | pass | The complete public commit tree contains exactly the two Context deletions plus Contract evidence; `.github/agents/` retains its untracked disposition and no declared Jarvis runtime path entered the commit. Historical content changes to unversioned runtime files are not observable without a pre-change hash |

## Quality Review

**Owner:** Syspilot Quality<br>
**Status:** complete

**Current judgment:** proceed

The complete Change range against `development` contains only the two intended public Context deletions and this Contract. Neither Context path remains in the public index or `HEAD`; both local files exist, are ignored publicly, remain tracked on clean private `main` at `5919368`, and equal their private migration-baseline blobs. The unrelated `.github/agents/` directory remains untracked and no Jarvis runtime path entered the Change.

The historical public blobs differ from the private baseline only by actor-memory migration content already present before this separation Change, including private-repository guardrails and migrated links. This review therefore makes no unsupported claim about pre-Change unversioned edits. Independent validation passed the strict documentation build with zero warnings, documentation tests 4/4, `git diff --check development...HEAD`, and editor diagnostics.

### Open Quality Issues

None.

## User Validation And Approval

**Owner:** User<br>
**Recorded by:** Syspilot Project Manager<br>
**Status:** accepted

**Decision and evidence:** The User directly accepted the Quality-approved result on 2026-08-26 after being shown that public tracking was removed while local and private tracking remained intact.

## Closure

**Owner:** Syspilot Project Manager<br>
**Status:** closed

- [x] Every included artifact has terminal status and completion evidence.
- [x] Intent and outcome are `approved`.
- [x] Quality has recorded a `proceed` judgment.
- [x] Open Quality Issues contains `None`.
- [x] User validation is `accepted`.
- [x] Current blocker is `none`.
- [x] The observable outcome is demonstrated.
- [x] Integration into `development` has been completed by the Syspilot Project Manager through the resulting squash integration commit.

**Final outcome:** The public Syspilot repository no longer tracks the Architect or Technical Writer Context file. Both files remain present at Jarvis's expected local paths and tracked on clean private actor-memory `main` at `5919368`. The User accepted the Quality-approved separation, and the closed Change was squash-integrated into `development`.