# Change Contract: closure-integration-check

**Status:** accepted<br>
**Process owner:** Project Manager<br>
**Current responsibility:** Project Manager<br>
**Current blocker:** none<br>
**Created:** 2026-11-12<br>
- **Operation Mode**: autonomous, agreed with the User on 2026-11-12.

- **autonomous** - every actor decides on its own; when genuinely unsure, it asks the user directly and pauses only its own step until answered.

## Handover log

Owned by: Project Manager

The handing-over actor appends one line as the last act before handing over, in the same commit that changes `Current responsibility`, taking `Date` as `YYYY-MM-DD` and `Time` as `HH:MM` in 24-hour local time from the system clock at that moment. The note states what the owner did and the facts that change the next owner's situation; evidence stays in the owner's section and remaining work in the open rows. The handover goes to the next actor that follows from the logical flow of the Change. The log explains transitions; the header stays authoritative.

| Date | Time | From | To | Note |
|--|--|--|--|--|
| 2026-11-12 | 15:14 | Project Manager | Architect | Contract released by the User in autonomous mode; add the integration item to the Change closure checklist and requirement. |
| 2026-11-12 | 15:18 | Architect | Developer | Explicit integration obligation and focused VC are specified and checked; the guide's alternative closure condition awaits Project Manager scope disposition. |
| 2026-11-12 | 15:24 | Developer | Quality | Added the integration item to the Closure checklist of the canonical template and the example; strict build and 202 tests pass. No test pins the item. Yours: review; the guide discrepancy stays with the Project Manager. |
| 2026-11-12 | 15:26 | Quality | Developer | Checklist and focused VC satisfy the integration condition; the Project Manager assigned the remaining conflicting guide sentence to Developer. |
| 2026-11-12 | 15:31 | Developer | Quality | Q1 corrected: the closure sentence in `docs/change-contract.md` now requires squash integration unless Version control is `not applicable` with its reason; strict build and 202 tests pass. Yours: confirm and remove the row. |
| 2026-11-12 | 15:33 | Quality | User | Guide, Requirement and both checklists agree; Q1 is cleared and the change can proceed to validation. |
| 2026-11-12 | 17:07 | User | Project Manager | The User accepted the outcome; closure recorded. |

## Intent And Outcome

**Status:** approved<br>
**Approval evidence:** The User found the gap on 2026-11-12, asked for this Change, and released it the same day in autonomous mode.

### Goal

The Change Contract's closure checklist requires that the feature branch is squash-integrated into the integration branch before the Contract is closed.

### Value

The `Version control` row says the branch is squash-integrated into `development` at closure, but no closure item checks it, so a Change can be closed with its result not integrated. The generic example Contract, which adopting projects copy at Setup, has the same gap.

### Scope

- The closure checklist of the canonical Change Contract template, `docs/Syspilot Contracts/change.md`, gains the item "The feature branch is squash-integrated into `development`", and the Contract kind's closure requirement names it.
- The example `docs/Example Contracts/change.md` carries the same item with its `{integration branch}` placeholder.
- A row marked `not applicable` for version control needs no integration; the item then reads as satisfied by that recorded reason.
- Out of scope: the closure checklists of other Contract kinds, the order of acceptance, integration and closure, and the content of `requirement-cleanup`.
- Crew: Architect, Developer, Quality; the Developer writes the Markdown artifacts including the example.

### Observable Outcome

The canonical template and the example closure checklist both contain the integration item, the requirement states it, and the documentation builds strictly clean.

## Artifacts, Ownership And Process Gates

**Applicability:** Each artifact owner decides and updates its own row.<br>
**Scope change:** When the approved intent widens after a row reached a terminal status, `Intent and outcome` returns to `draft` until it is approved again, and each owner whose terminal row the wider intent may affect reassesses it: the owner sets the row back to `pending` or records in the row why its evidence still holds.<br>
**Ownership:** The `Owner` column of this table is the only statement of artifact and gate ownership in the Contract; section headings name no artifact owner.<br>
**Status:** pending

Lightweight crew by User decision of 2026-11-12: Architect, Developer, Quality. The change overlaps `requirement-cleanup` in `req_change_contract.rst`; whichever integrates second reconciles that file.

| Artifact or gate | Included | Owner | Completion evidence | Status |
|---|---|---|---|---|
| Intent and outcome | yes | Project Manager | Goal, value, scope, and observable outcome are explicit and approved | approved |
| Contract release | yes | User | User released the Contract on 2026-11-12 | approved |
| Version control | yes | Project Manager | Feature branch `feature/closure-integration-check`; squash-integrated into `development` at closure | active |
| Infrastructure impact | not applicable: no workflow, CI or packaging artifact changes | Admin | Affected workflow, CI, and packaging artifacts are updated, confirmed by their current owner rather than inferred from a Needs-only impact query | not applicable |
| Product specification and architecture decisions | yes | Architect | `e6fe284` adds the integration item and `SYSP_VC_CHANGE_INTEGRATION_1`; strict build has zero warnings, 33 relevant existing checks pass and fresh Impact links resolve; guide discrepancy is recorded below | complete |
| User-facing documentation | not applicable: crew limited by User decision; the Architect names any guide that states the closure checklist as an open issue | Technical Writer | Agreed documentation surface is coherent and user-oriented; factual-owner review is recorded; `doc` Needs and `includes` links are current; documentation builds cleanly | not applicable |
| Example sync | yes | Developer | `docs/Example Contracts/change.md` carries the integration item; documentation builds cleanly | complete |
| Implementation and unit verification | yes | Developer | `docs/Syspilot Contracts/change.md` carries the integration item; commands and results recorded | complete |
| Acceptance test design and results | not applicable: Quality reviews the artifacts directly | Tester | Requirement tests written and run by the Tester, with their commands and results, and the means for User validation trace to the intended outcome | not applicable |
| Quality review | yes | Quality | Review at `e33231c`: proceed; canonical/example items, focused VC and corrected guide agree, Q1 cleared | complete |
| User validation and approval | yes | User | The User accepted the outcome on 2026-11-12 | accepted |
| Closure decision | yes | Project Manager | Final outcome, validation disposition, and integration state are recorded | accepted |

## Architecture And Specification

**Status:** complete

### Affected Artifacts

| Artifact | Change | Rationale |
|---|---|---|
| `docs/syspilot/requirements/req_change_contract.rst` | Explicit integration closure obligation and focused `SYSP_VC_CHANGE_INTEGRATION_1`; remove the contrary claim that no separate rule is needed | The checklist must assess integration directly rather than rely on interpretation of terminal artifact status |
| `docs/Syspilot Contracts/change.md` | Developer adds the explicit Closure checklist item, including the reasoned `not applicable` case | The canonical process must refuse closure with an active, unintegrated feature branch |
| `docs/Example Contracts/change.md` | Developer mirrors the item with `{integration branch}` | Setup's generic source must carry the same condition without imposing Syspilot's branch name |

### Decisions And Evidence

| Decision or check | Evidence |
|---|---|
| Impact discovery | Successful both-direction depth-1 flat and typed queries from `SYSP_REQ_CHANGE_CONTRACT`, plus the existing VC query, found the story, handling parent, existing VC and five documentation Needs; source content determines disposition, not graph presence alone |
| Candidate disposition | Story and handling parent are unchanged. Existing VC and other obligations remain. The example is included. Branching guide already requires integration at closure; Methodology names the process as authority; Upgrade describes its own migration integration, not the closure checklist. No edits to those three guides are needed |
| Narrow specification boundary | Add one concise closure obligation and one independently assessable VC; retain existing IDs and leave unrelated clauses to the parallel `requirement-cleanup` Change. Whichever Change integrates second reconciles this obligation/VC with the extracted closure topic |
| No order redesign | The item gates closure on completed integration or a reasoned Version control exclusion; it does not prescribe a new acceptance/integration sequence, authorize publication, or alter any other Contract kind |
| Guide discrepancy: open, Project Manager decision | `docs/change-contract.md`, “The Project Manager Closes”, permits closure when integration/publication is complete **or its next authorized owner is explicit**. That alternative does not establish integration before closure. CONSULT sent to Project Manager to decide scope/ownership; no guide edit is authorized in the current artifact set |
| Verification at `e6fe284` | Isolated detached-worktree `python docs\docs-build.py clean` passed with zero schema/build warnings. Four `ChangeTemplateTests` and all 29 `test_acceptance_setup_examples.py` checks passed. Fresh depth-1 both-direction Impact queries resolve the changed Requirement and new VC. `git diff --check` passes |
| Evidence and limits | Build log `C:\Users\DOE4SI\.copilot\session-state\334ed166-2820-4c7b-bf2b-648112d9fa4c\files\closure-integration-check-build.log`; fresh combined/per-ID graph in sibling `closure-integration-check-needs\`. The clean validation worktree was removed; the unrelated dirty instruction remains untouched. These checks cover specification/build integrity and existing behavior, not the still-unimplemented checklist item or Quality approval |

## Example Sync

**Status:** complete

| Artifact | Change | Verification evidence |
|---|---|---|
| `docs/Example Contracts/change.md` | Closure checklist gains "The feature branch is squash-integrated into `{integration branch}`, or the `Version control` row is `not applicable` with its recorded reason." before the `Current blocker` item | Strict `uv run python docs/docs-build.py` built successfully; full suite 202 tests OK (2026-11-12 15:24) |

## Implementation And Unit Verification

**Status:** complete

### Decisions And Evidence

| Decision | Chosen approach | Relevant alternatives | Rationale and evidence |
|---|---|---|---|
| Item wording and place | One checklist item before `Current blocker`, in the words of the Requirement: integrated, or `not applicable` with its recorded reason; the template names `development`, the example `{integration branch}` | Two items (integration and exclusion); a place after the outcome item | The Requirement and `SYSP_VC_CHANGE_INTEGRATION_1` state one condition with its exception; the item sits with the other state checks and before the blocker, which is the last state to clear |
| Not done | No test pins the new item; no other Contract kind or guide changed | A pin in the acceptance tests | Quality reviews the artifacts directly (Tester row not applicable); the guide discrepancy in `docs/change-contract.md` is the Project Manager's decision |

### Changed Artifacts And Verification

| Artifact | Change | Verification evidence |
|---|---|---|
| `docs/Syspilot Contracts/change.md`, `docs/Example Contracts/change.md` | As above | `uv run python docs/docs-build.py`: built successfully; `uv run python -m unittest discover -s tests`: 202 tests OK (2026-11-12 15:24). The `clean` build variant was not used because another process holds `docs/_build/html` |
| `docs/change-contract.md` (Q1) | In "The Project Manager Closes" the clause "integration or publication is complete or its next authorized owner is explicit" now reads "the feature branch is squash-integrated into the integration branch, unless the Version control row is `not applicable` with its reason recorded"; no other text changed | `git grep -i "next authorized owner"` outside `docs/changes`, `docs/releases` and `docs/_build` finds nothing; strict `uv run python docs/docs-build.py` built successfully; `uv run python -m unittest discover -s tests`: 202 tests OK (2026-11-12 15:31) |

## Quality Review

**Status:** complete

**Current judgment:** proceed at `e33231c`.

The canonical and example checklist items match the focused Requirement/VC:
an active unintegrated branch fails; completed squash integration passes;
`not applicable` passes only with the Version control row's recorded reason.
The canonical target is `development`; the example retains `{integration branch}`.
No acceptance/integration order or publication authority was changed. The new
VC is short and independently assessable; unrelated compound baseline content
remains with the parallel `requirement-cleanup` Change.

Q1 is cleared: the corrected guide requires completed squash integration or
the reasoned Version control `not applicable` case. Naming a next owner no
longer substitutes for integration, and Change closure requires no publication.
The complete `022d62b..e33231c` correction diff changes only that sentence and
Contract evidence/state; specification and both checklist items remain intact.
Project Manager directly assigned the bounded guide correction to Developer;
the documentation row remains not applicable by the crew decision.

### Applied Review Methods

| Method | Selected scope | Evidence | Findings | Limits |
|---|---|---|---|---|
| Scoped content and verification review | Complete original product diff and `022d62b..e33231c` correction: Requirement, focused VC, both checklists and guide closure sentence | Direct assessment: unintegrated applicable branch fails, completed squash integration passes, `not applicable` needs a reason; Architect's isolated strict-clean build; Developer's recorded strict build and 202 passing tests after correction; `git diff --check` passes | All four surfaces agree; Q1 cleared | No automated test pins the item; recorded Markdown review provides verification. No suite rerun: recorded results and direct reading support the bounded documentation correction. Implementation build was strict but not clean due to the recorded shared lock |
| MECE horizontal coverage | Original REQ/two VCs plus `SYSP_DOC_CHANGE_CONTRACT`; same-document, complete same-type peers | Retained three analyses remain valid because Need sources/links are unchanged; added guide analysis returns exactly the other eleven documentation Needs; all peer content read | Focused integration criterion complements existing coverage; guide and Branching agree, other documentation surfaces retain distinct purposes; no new overlap or authority collision | The REQ has no comparable peer; structured coverage data is unavailable. Content judgment supplies semantic assessment; broad baseline cleanup remains separate |
| Trace relationship analysis | Four starts, both directions, depth 1; exact 21-Need neighborhood union | Prior three Trace/Impact analyses retained; added guide Trace/Impact queries against `closure-integration-check-needs\needs_id`; linked Requirement/story/doc content and changed Markdown read | No unresolved target or remaining semantic conflict; the corrected guide follows the closure authority declared by the Requirement and checklists | Depth 1 is not completeness proof. Need sources/links are unchanged from the retained export through `e33231c`; current guide/checklist content was read directly rather than inferred from the older export |

Exact per-object peers, neighborhoods and edges are retained in
`C:\Users\DOE4SI\.copilot\session-state\31d89b9f-bcdb-4323-9a89-60ceae73d649\files\closure-quality-final-analysis.json`.
No unrelated dirty instruction or other actor's artifact was modified.

Quality communicates its `proceed` judgment and supporting evidence directly to the Project Manager before the Project Manager presents the verified outcome for validation. Another actor's forwarded claim does not establish Quality's decision.

### Open Quality Issues

Keep this table synchronized with currently open issues. For each issue, Quality transfers current responsibility to the owner of the affected artifact. When Quality confirms the required outcome, update the affected artifact or evidence and remove the resolved row. At closure this table contains `None`.

| Artifact | Current issue | Required outcome |
|---|---|---|
| None | | |

## User Validation And Approval

**Recorded by:** Project Manager<br>
**Status:** accepted

Quality's `proceed` judgment verifies that the change is ready for validation; it does not validate user value. The Project Manager presents the observable outcome after receiving Quality's direct judgment and evidence; the User communicates the decision directly to the Project Manager, who records it.

**Decision and evidence:** The User accepted the outcome directly to the Project Manager on 2026-11-12 after the presentation of Quality's `proceed` at fd0241c. The presentation named the change: both closure checklists carry the integration item, the Requirement states it, and the closure sentence in `docs/change-contract.md` agrees.

## Closure

**Status:** accepted

- [x] Every included artifact or gate has terminal status and completion evidence.
- [x] Intent and outcome are `approved`.
- [x] Quality has recorded a `proceed` judgment.
- [x] Open Quality Issues contains `None`.
- [x] User validation is `accepted`.
- [x] Current blocker is `none`.
- [x] The observable outcome is demonstrated.
- [ ] The feature branch is squash-integrated into `development`.

**Final outcome:** The Change Contract closure checklist in the canonical template and the example requires that the feature branch is squash-integrated into the integration branch, or that the Version control row is `not applicable` with its reason; the Requirement and the closure sentence in `docs/change-contract.md` agree. The User accepted on 2026-11-12.
