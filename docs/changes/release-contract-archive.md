# Change Contract: release-contract-archive

**Status:** accepted<br>
**Process owner:** Project Manager<br>
**Current responsibility:** Project Manager<br>
**Current blocker:** none<br>
**Created:** 2026-11-11<br>
- **Operation Mode**: autonomous, agreed with the User on 2026-11-11.

- **autonomous** - every actor decides on its own; when genuinely unsure, it asks the user directly and pauses only its own step until answered.

## Handover log

Owned by: Project Manager

The handing-over actor appends one line as the last act before handing over, in the same commit that changes `Current responsibility`, taking `Date` as `YYYY-MM-DD` and `Time` as `HH:MM` in 24-hour local time from the system clock at that moment. The note states what the owner did and the facts that change the next owner's situation; evidence stays in the owner's section and remaining work in the open rows. The handover goes to the next actor that follows from the logical flow of the Change. The log explains transitions; the header stays authoritative.

| Date | Time | From | To | Note |
|--|--|--|--|--|
| 2026-11-11 | 22:43 | Project Manager | Architect | Contract released by the User in autonomous mode; scope is the archive layout and paths only. |
| 2026-11-11 | 22:46 | Architect | Developer | Specified the path `docs/releases/v{version}.md` and the archiving step (move included Change Contracts to `docs/changes/v{version}/` before the preflight, no content change); strict build passes. Yours: Release Process, example, checker, tests as listed in my decisions; I added `SYSP_AC_RELEASE_CONTRACT_4`, which the Project Manager may veto. |
| 2026-11-11 | 22:55 | Developer | Quality | Release Process, example, checker and tests use `docs/releases/v{version}.md` and the archiving step before the preflight; strict build and 202 tests pass. The step is text only: no check verifies the move, as the Requirement states it for Release. Yours: review. |
| 2026-11-11 | 22:58 | Quality | Developer | Blocked: two branching-guide path statements remain obsolete; Project Manager confirmed their correction is in scope. |
| 2026-11-11 | 23:04 | Developer | Quality | QI-1 corrected: both path statements in `docs/branching.md` name `docs/releases/v{version}.md`; evidence in my section. Yours: confirm and remove the row. |
| 2026-11-11 | 23:06 | Quality | User | Proceed for validation: archive layout and path corrections agree; specification restructuring remains explicitly deferred. |
| 2026-11-11 | 23:10 | User | Project Manager | The User accepted the outcome; closure recorded. |

## Intent And Outcome

**Status:** approved<br>
**Approval evidence:** The User reviewed the narrowed text in the editor and released the Contract on 2026-11-11, moving requirement tightening, VC style, and trigger 3 out of scope.

### Goal

A published release leaves a clean tree: its Release Contract lives at `docs/releases/v{version}.md` and the Change Contracts it shipped in `docs/changes/v{version}/`.

### Value

v0.10.0 was published with all 20 Change Contracts and the Release Contract flat in `docs/changes/`, because the current Release Process has no archiving step; earlier releases archived by hand. The cleanup had to follow after publication.

### Scope

- Release Contract path becomes `docs/releases/v{version}.md`: Release Process, its initialization, the record checker, and its tests follow.
- Release moves the included Change Contracts to `docs/changes/v{version}/` before the preflight, so the published commit is already clean and the difference from P to R stays the Release Contract alone.
- `SYSP_REQ_RELEASE_CONTRACT`, its VC, and `SYSP_US_RELEASE_CONTRACT` change only where they state the path or the archiving step.
- The example `docs/Example Contracts/release.md` follows.
- Out of scope: tightening the requirement and the VC style (separate Change); the revalidation triggers; the release workflow.

### Observable Outcome

- Release Process, example, requirement, checker, and tests name `docs/releases/v{version}.md`; the Release Process archives Change Contracts before the preflight.
- Strict documentation build and the test suite pass.

## Artifacts, Ownership And Process Gates

**Applicability:** Each artifact owner decides and updates its own row.<br>
**Scope change:** When the approved intent widens after a row reached a terminal status, `Intent and outcome` returns to `draft` until it is approved again, and each owner whose terminal row the wider intent may affect reassesses it: the owner sets the row back to `pending` or records in the row why its evidence still holds.<br>
**Ownership:** The `Owner` column of this table is the only statement of artifact and gate ownership in the Contract; section headings name no artifact owner.<br>
**Status:** pending

Lightweight crew by User decision of 2026-11-11: Architect, Developer, Quality. The Developer produces the Markdown process artifacts, including the example, in this Change.

| Artifact or gate | Included | Owner | Completion evidence | Status |
|---|---|---|---|---|
| Intent and outcome | yes | Project Manager | Goal, value, scope, and observable outcome are explicit and approved | approved |
| Contract release | yes | User | User released the Contract on 2026-11-11 | approved |
| Version control | yes | Project Manager | Feature branch `feature/release-contract-archive`; squash-integrated into `development` at closure | active |
| Infrastructure impact | not applicable: the release workflow reads no Contract path | Admin | Affected workflow, CI, and packaging artifacts are updated, confirmed by their current owner rather than inferred from a Needs-only impact query | not applicable |
| Product specification and architecture decisions | yes | Architect | Changed specification and architecture artifacts are linked and checked | complete |
| User-facing documentation | not applicable: crew limited by User decision; the Architect names any guide that states the old path as an open issue | Technical Writer | Agreed documentation surface is coherent and user-oriented; factual-owner review is recorded; `doc` Needs and `includes` links are current; documentation builds cleanly | not applicable |
| Example sync | yes | Developer | `docs/Example Contracts/release.md` carries the changes that hold for a general project; documentation builds cleanly | complete |
| Implementation and unit verification | yes | Developer | `docs/Syspilot Contracts/release.md`, `scripts/check_release_record.py`, and its tests changed; commands and results recorded | complete |
| Acceptance test design and results | not applicable: Quality reviews the VCs directly | Tester | Requirement tests written and run by the Tester, with their commands and results, and the means for User validation trace to the intended outcome | not applicable |
| Quality review | yes | Quality | Re-review at c81d57f confirms both branching-guide path corrections; canonical/example process and checker agree; recorded strict build, 202 tests and 76 focused tests support the bounded judgment | proceed |
| User validation and approval | yes | User | The User accepted the outcome on 2026-11-11 | accepted |
| Closure decision | yes | Project Manager | Final outcome, validation disposition, and integration state are recorded | accepted |

## Architecture And Specification

**Status:** complete

### Affected Artifacts

| Artifact | Change | Rationale |
|---|---|---|
| `SYSP_REQ_RELEASE_CONTRACT` (`req_release_contract.rst`) | Release Contract path `docs/releases/v{version}.md` (initialization, preflight evidence, soundness of the evidence exception); new obligation: Release moves every included Change Contract to `docs/changes/v{version}/` before the preflight; the VC states the paths, the archiving step and the exclusion of the archive from the build | Scope states the path and the archiving step only; no other rule is touched |
| `SYSP_US_RELEASE_CONTRACT` (`us_release_contract.rst`) | New `SYSP_AC_RELEASE_CONTRACT_4`: a published release leaves a clean tree | The story and the existing ACs state neither path nor archiving; without an AC the new obligation has nothing to validate against. The Project Manager may remove it if the scope is read as excluding a new AC |

### Decisions And Evidence

| Decision or check | Evidence |
|---|---|
| Archiving lives in the Release Contract's own preflight sequence, before the preflight, in a commit on `development`. Reason: the preflighted commit P then already carries the archive layout, so the difference from P to R stays the record alone and the existing path-exact record check needs no new exception; archiving after P would add paths to the P-to-R difference and fail the check | `SYSP_REQ_RELEASE_CONTRACT`; `scripts/check_release_record.py` rejects any other path |
| The move changes no content. Reason: a moved Contract is a closed historical record; rewriting its relative links is a content change that Quality would have to review for every moved file, and the archived v0.10.0 Contracts show that links resolve only from their old location. Accepted consequence: relative links inside archived Contracts dangle; they are not read by the build or any check. Open for the Project Manager and Release if a link-preserving move is wanted: that is a different rule, not specified here | `docs/changes/v0.10.0/` (relative links such as `../Syspilot%20Contracts/...`) |
| Soundness of the evidence exception moves with the path: it holds while the build excludes the record's folder and the record check is the only reader. `docs/conf.py` already lists `releases/*` and `changes/*` in `exclude_patterns`, so no configuration change is needed; the clean strict build with `docs/releases/v0.10.0.md` and `docs/changes/v0.10.0/` present produced no page under either folder | `docs/conf.py` lines 84-85; `python docs/docs-build.py clean` on 2026-11-11 22:46: built successfully; zero HTML pages under `changes` or `releases` |
| Revalidation triggers and the release workflow are out of scope by the User. Note for Release, no action in this Change: `docs/conf.py` is on the trigger list, and this Change does not edit it; the checker `scripts/check_release_record.py` is not on the list, because it is not an input of the workflow | Scope of this Contract |
| Open for the Developer, not specified: the Release Process text (`docs/Syspilot Contracts/release.md` lines 5, 11, 23, 198), the example (lines 5, 11, 23, 206), `scripts/check_release_record.py` (lines 141, 212) and the tests that pin `docs/changes/release-v` need the new path and the archiving step; the Release Process gives the archiving step its place before the preflight and names the Change Inventory as the list of Contracts to move | `grep` of `release-v` and `docs/changes/` over `docs/syspilot`, `docs/Syspilot Contracts`, `docs/Example Contracts`, `scripts`, `.github` on 2026-11-11 |
| Checks: `python docs/docs-build.py clean` (strict) built successfully. The test suite was not run by me, because no test file changed; `tests/test_release_record.py` and `tests/test_acceptance_release_record.py` mention the record path and are the Developer's to repoint (`tests/test_acceptance_adoption_feedback.py` mentions `docs/changes` and needs a look for the same reason) | Command run in the working tree; `grep` of `tests` |

## Example Sync

**Status:** complete

| Artifact | Change | Verification evidence |
|---|---|---|
| `docs/Example Contracts/release.md` | Record path `docs/releases/v{version}.md` in the intro, concrete instances, initialization step 1 and the Publication record rule; Change Inventory gains the archiving paragraph and the Preflight intro names it, in project-neutral wording (`{integration branch}`) | Strict `uv run python docs/docs-build.py clean` built successfully on 2026-11-11; the Release card test of the full suite passes |

## Implementation And Unit Verification

**Status:** complete

### Decisions And Evidence

| Decision | Chosen approach | Relevant alternatives | Rationale and evidence |
|---|---|---|---|
| Archiving step placement | Paragraph `Archiving:` under the Change Inventory table of the canonical template, plus a clause in the Preflight intro; Release moves the listed Contracts with `git mv` in a commit on `development` before the preflight | A new numbered step in Release Contract Initialization; a Publication step | The Inventory is the list of what to move and is protected content final before P, so the step sits where it is read; initialization happens before the Changes are final and Publication is after P, which would add paths to the P-to-R difference |
| Checker | Only the record path changed to `docs/releases/{tag}.md`; no other check changed | An exception for moved Contracts | The move happens before P, so the P-to-R difference is still the record alone and the path-exact check needs no exception |
| Tests | Repointed the record path in `tests/test_release_record.py` and `tests/test_acceptance_release_record.py`; the one-reader test now searches `docs/releases/` and also requires `releases` in the build's `exclude_patterns`; `tests/test_acceptance_adoption_feedback.py` pins the new path in the record rule | Leaving the old pins | The old pins named a path that no longer exists |
| Not done | No test pins the archiving paragraph text, and no check verifies that Contracts were moved; Quality and Release review it by the Release Process | A checker for `docs/changes/` | The Requirement states the obligation for Release, not an automated check, and tightening is out of scope |

### Changed Artifacts And Verification

| Artifact | Change | Verification evidence |
|---|---|---|
| `docs/Syspilot Contracts/release.md`, `scripts/check_release_record.py`, `tests/test_release_record.py`, `tests/test_acceptance_release_record.py`, `tests/test_acceptance_adoption_feedback.py` | As above | `uv run python docs/docs-build.py clean`: built successfully; `uv run python -m unittest discover -s tests`: 202 tests OK (2026-11-11 22:55). Not run: a real release with the archive step |
| `docs/branching.md` (QI-1) | Both release-record path statements (the Release Contract path and the authorization commit) now name `docs/releases/v{version}.md`; no other change | `git grep -n "changes/release-"` outside `docs/changes`, `docs/releases` and `docs/_build` finds nothing; strict `uv run python docs/docs-build.py` built successfully (the `clean` variant failed on a locked `docs/_build/html` held by another process, not on content); `tests.test_release_record`, `tests.test_acceptance_release_record`, `tests.test_acceptance_adoption_feedback`: 76 tests OK (2026-11-11 23:04) |

## Quality Review

**Status:** proceed

**Current judgment:** proceed for User validation at `c81d57f`. QI-1 is resolved: both release-record path instructions in `docs/branching.md` now agree with `docs/releases/v{version}.md`. The changed canonical process, generic example, checker and tests agree on this path and archiving the included Change Contracts before P, without widening the record-only P-to-R exception. The recorded strict build and 202 passing tests, followed by the corrected guide's successful build and 76 focused tests, support this scoped judgment. The later clean-build attempt failed because its output directory was locked; it is not recorded as a pass or a content failure. Project Manager confirmed Developer ownership of the two guide corrections and AC4's inclusion. No open quality issue remains within the approved archive-layout scope; User validation and closure remain pending.

**Major, explicitly deferred:** the existing Requirement/VC combine many independently assessable obligations, and the added archive passage mixes obligation, procedure and rationale. This is the material assessability/KISS concern already discussed with the User and acknowledged by Project Manager, explicitly deferred by this Contract to a separate specification Change for Architect. It is not cleared by this proceed and does not widen this Change. The new AC4 is a concise, coherent archive-layout outcome.

Quality reviewed the recorded commands/results rather than rerunning passing suites. No product artifacts, guides, workflow, archived Contracts or another actor's evidence were edited by Quality. Actual release execution and automatic verification of the archive move are not demonstrated or claimed.

### Applied Review Methods

| Method | Selected scope | Evidence | Findings | Limits |
|---|---|---|---|---|
| Impact discovery | `SYSP_REQ_RELEASE_CONTRACT`, `SYSP_VC_RELEASE_CONTRACT_1`, `SYSP_US_RELEASE_CONTRACT`, `SYSP_AC_RELEASE_CONTRACT_1` to `_4`; both directions, depth 2 | Seven successful `get_need_links.py ID --direction both --depth 2 --flat --no-build` queries on the final built Needs | 49-object union exposes shared Contract, release/version, Setup and documentation neighbors; direct guide review found QI-1 | Candidate discovery is not an exhaustive filesystem scope or a scope decision |
| Horizontal coverage | Same-document peers of all seven starting objects | Seven successful `analyze_mece.py ID --scope same-document` queries; no structural findings. AC1 to AC4 are each other's exact peers; Requirement, VC and Story have no same-document peers. Read all four ACs | AC4 adds archive layout, distinct from assessability, local verification and version outcomes. Baseline mixed-obligation AC/VC concern remains explicitly deferred | Empty peer sets and unavailable structured coverage are limits, not clearance of prose quality |
| Relationship analysis | Same seven starts; both directions, depth 2; 49-object neighborhood | Seven successful `analyze_trace.py ID --direction both --depth 2` queries with no structural findings; reviewed changed Requirement/VC, Story/AC4 and canonical/example realizations, plus affected branching guidance | QI-1: the guide instructs readers to use a path rejected by the updated checker. No graph-link defect established | Full resolved-neighbor semantic clearance remains open for re-review; structural success is not semantic or runtime proof |
| Artifact and evidence review | Complete specification/process/example/checker/test delta from released Contract through 6889249; final configuration exclusions | Checker changes only the expected record path and success text; unit/acceptance fixtures follow it, rejection assertions remain intact. Both `changes/*` and `releases/*` were already excluded. Owner records strict build and 202 tests passing | Archiving is an explicit manual preflight obligation, not a new automated guard. No checker exception for archived Changes was added; moving them after P still fails the existing path rule | No actual release run; byte-preserving moves intentionally leave historical relative links unchanged, as the approved scope requires |
| Re-review at c81d57f | Complete two-file correction delta; repeated all 21 Impact/MECE/Trace queries at the same scopes | Both guide statements corrected with no other guide change; no old record path in the five reviewed release-facing guides. All queries succeed; same 49-object union and exact AC1-to-AC4 peer sets, no structural findings. Owner records successful guide build and 76 focused tests | QI-1 resolved. Changed Requirement/VC and AC4 reviewed against canonical/example archiving and checker rules; remaining neighborhood sources are unchanged from the completed v0.10.0 Quality review at 03db5ca, verified by source diff, so that semantic baseline is retained | Semantic clearance is bounded to the archive change and retained unchanged baseline; the Major specification-structure finding remains deferred. No redundant Quality suite/build was needed |

Project Manager's consultation on 2026-11-11 confirmed the guide correction owner and AC4 scope; it also acknowledged that the monolithic-VC concern remains deferred. No responsibility transfer occurred during consultation.

The initial relationship row records the incomplete first review. Re-review completes its deferred semantic assessment through direct review of all changed neighborhood sources and realizations and retention of the unchanged reviewed baseline. Absence of graph findings does not prove prose correctness or require a link not mandated by the model.

Quality communicates its `proceed` judgment and supporting evidence directly to the Project Manager before the Project Manager presents the verified outcome for validation. Another actor's forwarded claim does not establish Quality's decision.

### Open Quality Issues

Keep this table synchronized with currently open issues. For each issue, Quality transfers current responsibility to the owner of the affected artifact. When Quality confirms the required outcome, update the affected artifact or evidence and remove the resolved row. At closure this table contains `None`.

| Artifact | Current issue | Required outcome |
|---|---|---|
| None | None | None |

## User Validation And Approval

**Recorded by:** Project Manager<br>
**Status:** accepted

Quality's `proceed` judgment verifies that the change is ready for validation; it does not validate user value. The Project Manager presents the observable outcome after receiving Quality's direct judgment and evidence; the User communicates the decision directly to the Project Manager, who records it.

**Decision and evidence:** The User accepted the outcome directly to the Project Manager on 2026-11-11 after the presentation of Quality's `proceed` at 8dbfeca. The presentation named two limits: the archiving step is text only and is first executed at the next release, and the Requirement and VC restructuring is deferred to a separate Change.

## Closure

**Status:** accepted

- [x] Every included artifact or gate has terminal status and completion evidence.
- [x] Intent and outcome are `approved`.
- [x] Quality has recorded a `proceed` judgment.
- [x] Open Quality Issues contains `None`.
- [x] User validation is `accepted`.
- [x] Current blocker is `none`.
- [x] The observable outcome is demonstrated.

**Final outcome:** Release Contracts live at `docs/releases/v{version}.md`; Release archives the included Change Contracts to `docs/changes/v{version}/` before the preflight. Process, example, checker, tests, requirement, story and branching guide agree. The User accepted on 2026-11-11. Not proven: the archive move itself runs first at the next release; Requirement and VC tightening is a separate Change.
