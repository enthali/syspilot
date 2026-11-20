# Change Contract: revalidation-baseline

**Status:** closed<br>
**Process owner:** Project Manager<br>
**Current responsibility:** Project Manager<br>
**Current blocker:** none<br>
**Created:** 2026-11-19<br>
- **Operation Mode**: autonomous, agreed with the User on 2026-11-19.

- **autonomous** - every actor decides on its own; when genuinely unsure, it asks the user directly and pauses only its own step until answered.

## Handover log

Owned by: Project Manager

The handing-over actor appends one line as the last act before handing over, in the same commit that changes `Current responsibility`, taking `Date` as `YYYY-MM-DD` and `Time` as `HH:MM` in 24-hour local time from the system clock at that moment. The note states what the owner did and the facts that change the next owner's situation; evidence stays in the owner's section and remaining work in the open rows. The handover goes to the next actor that follows from the logical flow of the Change. The log explains transitions; the header stays authoritative.

| Date | Time | From | To | Note |
|--|--|--|--|--|
| 2026-11-19 | 23:18 | Project Manager | Architect | Contract released by the User in autonomous mode. Open for you: the baseline-rule wording named under Decisions And Evidence, the Affected Artifacts query, and the spec change to `SYSP_REQ_RELEASE_REVALIDATION` and `SYSP_VC_RELEASE_REVALIDATION_1`. |
| 2026-11-19 | 23:17 | Architect | Developer | Baseline rule decided and the requirement and `SYSP_VC_RELEASE_REVALIDATION_1` changed; no guide states the trigger list. Both process documents need the row removed and the rule added. |
| 2026-11-19 | 23:19 | Developer | Quality | Row removed and rule added in both release documents; strict docs build passes; no code or test change. |
| 2026-11-19 | 23:20 | Quality | Developer | Verdict revise: two Developer-owned issues, see Open Quality Issues. |
| 2026-11-19 | 23:20 | Quality | User | Verdict proceed; both issues resolved and re-checked. Validation is the User's. |
| 2026-11-19 | 23:20 | Developer | Quality | Example Sync section filled and the earlier log stamp corrected to 23:19. |
| 2026-11-19 | 23:25 | User | Project Manager | The User accepted the outcome; closure follows. |

## Intent And Outcome

**Status:** approved<br>
**Approval evidence:** On 2026-11-19 the User asked why the third revalidation trigger exists, accepted the proposal to drop it and replace it with a baseline rule, and chose autonomous mode.

### Goal

The revalidation triggers consist of the two observable comparisons against the last successful tag run. A missing baseline is handled by one stated rule: when no successful tag run exists to compare against, triggers 1 and 2 count as fired.

### Value

The third trigger, "No tag-run evidence", tested the preceding release, while the two comparisons it protects need a baseline of any earlier successful tag run. v0.10.0 recorded it as not relied on, because triggers 1 and 2 sufficed. A baseline rule says what the trigger was meant to say, in the place where the comparisons are defined, and removes a row that names a different condition than it needs.

### Scope

- `docs/Syspilot Contracts/release.md`, `Revalidation triggers`: the third trigger row is removed and the baseline rule is added.
- `SYSP_REQ_RELEASE_REVALIDATION` and `SYSP_VC_RELEASE_REVALIDATION_1` state the baseline rule in place of the third trigger.
- `docs/Example Contracts/release.md` follows.
- Out of scope: the validation-only run itself (kept by the User on 2026-11-19), the trigger path list, the environment-change statement, the release workflow, the checker, and the record of v0.10.0 (a protected historical record).

### Observable Outcome

- The Release Process and the example name two triggers and the baseline rule; neither contains "No tag-run evidence".
- The Requirement and its VC state the same rule.
- The strict documentation build and the test suite pass.

## Artifacts, Ownership And Process Gates

**Applicability:** Each artifact owner decides and updates its own row.<br>
**Scope change:** When the approved intent widens after a row reached a terminal status, `Intent and outcome` returns to `draft` until it is approved again, and each owner whose terminal row the wider intent may affect reassesses it: the owner sets the row back to `pending` or records in the row why its evidence still holds.<br>
**Ownership:** The `Owner` column of this table is the only statement of artifact and gate ownership in the Contract; section headings name no artifact owner.<br>
**Status:** complete

Lightweight crew, as in `release-contract-archive`: Architect, Developer, Quality. The Developer produces the Markdown process artifacts, including the example, in this Change.

| Artifact or gate | Included | Owner | Completion evidence | Status |
|---|---|---|---|---|
| Intent and outcome | yes | Project Manager | Goal, value, scope, and observable outcome are explicit and approved | approved |
| Contract release | yes | User | The User released the Contract in chat on 2026-11-19 at 23:17 ("go ahead du hast mein ok") after reviewing it in the editor; the Project Manager recorded the User's statement and set the gate on that instruction | approved |
| Version control | yes | Project Manager | Feature branch `feature/revalidation-baseline`; squash-integrated into `development` at closure | complete: squash commit 70f7602 `feat: revalidation-baseline` |
| Infrastructure impact | not applicable: the release workflow and its trigger path list do not change | Admin | Affected workflow, CI, and packaging artifacts are updated, confirmed by their current owner rather than inferred from a Needs-only impact query | not applicable |
| Product specification and architecture decisions | yes | Architect | Changed specification and architecture artifacts are linked and checked; Affected Artifacts built from the impact query, every reported ID dispositioned | approved |
| User-facing documentation | not applicable: no guide states the trigger list; the Architect names any guide that does as an open issue | Technical Writer | Agreed documentation surface is coherent and user-oriented; factual-owner review is recorded; `doc` Needs and `includes` links are current; documentation builds cleanly | not applicable |
| Example sync | yes | Developer | `docs/Example Contracts/release.md` carries the change; documentation builds cleanly | complete |
| Implementation and unit verification | yes | Developer | `docs/Syspilot Contracts/release.md` changed; commands and results recorded; no code or test change is expected | complete |
| Acceptance test design and results | not applicable: Quality reviews the VC directly | Tester | Requirement tests written and run by the Tester, with their commands and results, and the means for User validation trace to the intended outcome | not applicable |
| Quality review | yes | Quality | Quality reviewed the recorded commands and results; current verification judgment is `proceed` and no open quality issue remains | complete |
| User validation and approval | yes | User | The User accepted the outcome on 2026-11-19 | accepted |
| Closure decision | yes | Project Manager | Final outcome, validation disposition, and integration state are recorded | complete |

## Architecture And Specification

**Status:** approved

### Affected Artifacts

Impact query: `SYSP_REQ_RELEASE_REVALIDATION`; both directions; depth 2. Depth 2 passes through the graph root and returns the whole release and Contract neighborhood; the depth 1 result decides the dispositions, and a text search outside `docs/changes` and `docs/releases` found the third trigger only in the two release Contract documents.

| Artifact | Change | Rationale |
|---|---|---|
| `SYSP_REQ_RELEASE_REVALIDATION` | modified | The third trigger is removed; the baseline rule is stated. |
| `SYSP_VC_RELEASE_REVALIDATION_1` | modified | Names the two conditions and the baseline rule instead of the no-run condition. |
| `SYSP_VC_RELEASE_REVALIDATION_2` to `_5` | no change | Path list and notes exception, release-start assessment, authorization and baseline recording are unaffected. |
| `SYSP_REQ_RELEASE_CONTRACT`, `SYSP_US_RELEASE_CONTRACT` | no change | Parent requirement and story do not name the triggers. |
| `SYSP_DOC_OPERATIONS`, `SYSP_DOC_BRANCHING`, `SYSP_DOC_EXAMPLE_CONTRACTS` | no change | They include the requirement; the text search found no trigger list in them. `SYSP_DOC_EXAMPLE_CONTRACTS` realizes the example, which the Developer changes. |
| `docs/Syspilot Contracts/release.md` | modified (Developer) | Remove the row `No tag-run evidence`; add the baseline rule in `Revalidation triggers`. |
| `docs/Example Contracts/release.md` | modified (Developer) | Same change in the example. |
| `docs/releases/v0.10.0.md`, `docs/releasenotes.md` | no change | Protected historical record; the release notes sentence names no trigger list. |

### Decisions And Evidence

| Decision or check | Evidence |
|---|---|
| Baseline rule wording: "when no successful tag run exists to compare against, triggers 1 and 2 count as fired". It differs from the removed trigger, which fired when only the preceding release lacked a successful tag run. Triggers 1 and 2 compare against the last successful tag run, which may be older than the preceding release; when it exists, both comparisons are observable and sound, so the old condition added a run that the comparisons do not need. The rule is stronger where it matters: with no baseline at all both comparisons are impossible, so a validation-only run is required. Alternative rejected: keep the preceding-release condition inside the rule; it forces a run when a valid older baseline exists. | `SYSP_REQ_RELEASE_REVALIDATION`, `SYSP_VC_RELEASE_REVALIDATION_1` |
| Where the rule sits in the Process documents | Directly under the trigger table's lead paragraph in `Revalidation triggers`, so it applies to the two comparison rows; the table keeps two rows. The "Fired" column is filled `yes` for both when the rule applies. | Developer's edit of `release.md` and the example |
| Consistency check | The strict documentation build passes after the requirement edit; no Need was added, so no new link obligation applies. | `python docs/docs-build.py clean`: build succeeded, schema validation 0 warnings |
| Documentation | No guide states the trigger list: the text search found none; the row `User-facing documentation` stays not applicable. | search over `docs`, `tests`, `.github` |

## Example Sync

**Status:** complete

| Artifact | Change | Verification evidence |
|---|---|---|
| `docs/Example Contracts/release.md` | Row `No tag-run evidence` removed; rule "When no successful tag run exists to compare against, triggers 1 and 2 count as fired." added above the trigger table | Same text as in `docs/Syspilot Contracts/release.md`; `python docs/docs-build.py clean` strict build OK |

## Implementation And Unit Verification

**Status:** complete

### Decisions And Evidence

| Decision | Chosen approach | Relevant alternatives | Rationale and evidence |
|---|---|---|---|
| Rule wording | Architect's sentence verbatim, directly under the trigger table's lead paragraph, above the table | none | Applies to the two comparison rows; the table keeps two rows. |

### Changed Artifacts And Verification

| Artifact | Change | Verification evidence |
|---|---|---|
| `docs/Syspilot Contracts/release.md`, `docs/Example Contracts/release.md` | Row `No tag-run evidence` removed; rule "When no successful tag run exists to compare against, triggers 1 and 2 count as fired." added | `python docs/docs-build.py clean`: strict build OK, exit 0. No code or test change. |

## Quality Review

**Status:** complete

**Current judgment:** proceed. The two release documents and the requirement text carry the change consistently, verification is clean, and the Contract's recorded state is consistent.

### Applied Review Methods

| Method | Selected scope | Evidence | Findings | Limits |
|---|---|---|---|---|
| Build | Whole documentation | `python docs/docs-build.py clean` re-run: build succeeded | No finding | Browser rendering not checked |
| Diff and text search | Both release documents, requirement rst | Third row absent, baseline rule present once in each document; requirement and VC_1 text state the same rule | No finding | The rule says "triggers 1 and 2" while the table rows are unnumbered; wording is the Architect's decision text, noted for the User |
| MECE | `SYSP_REQ_RELEASE_REVALIDATION`, same-document | `analyze_mece.py` | No finding | Semantic review required |
| Trace | `SYSP_REQ_RELEASE_REVALIDATION`, both, depth 2 | `analyze_trace.py` | No finding | Semantic review required |
| Contract review | This Contract | Rows, sections, log | Two findings (Example Sync section, handover stamp) resolved at b56869b and re-checked | No test suite run: no code or test change |

Verification is fully automated. Quality reviews the commands and results that the Developer and the Tester recorded, and executes a check itself only when a recorded result cannot support its judgment, recording the reason in the table above. A Markdown process artifact whose content has no automated check is verified by Quality's review, and the table above records that review and its limits.

Quality communicates its `proceed` judgment and supporting evidence directly to the Project Manager before the Project Manager presents the verified outcome for validation. Another actor's forwarded claim does not establish Quality's decision.

### Open Quality Issues

Keep this table synchronized with currently open issues. A missing automation is an open issue whose row names the task that closes it, the owner of that task, and the completion evidence. For each issue, Quality transfers current responsibility to the owner of the affected artifact. When Quality confirms the required outcome, update the affected artifact or evidence and remove the resolved row. At closure this table contains `None`.

| Artifact | Current issue | Required outcome |
|---|---|---|
| None | None | None |

## User Validation And Approval

**Recorded by:** Project Manager<br>
**Status:** accepted

Quality's `proceed` judgment verifies that the change is ready for validation; it does not validate user value. For an included validation, the Project Manager presents the observable outcome after receiving Quality's direct judgment and evidence. The User communicates the validation decision directly to the Project Manager, who records the decision and evidence. Another actor's forwarded claim does not establish the User's decision. If the user requests changes, the Project Manager transfers responsibility to an included artifact owner that can produce the required outcome.

Current responsibility remains with the User from Quality's handoff until the validation decision is recorded. The Project Manager's presentation and recording duties support that User-owned artifact; they do not make the Project Manager the validation owner or an intermediate responsibility relay.

Set this artifact to `not applicable` only when the User explicitly delegates validation of the finished outcome and that delegation is recorded in its artifact row. Operation mode does not delegate validation. In unattended mode, keep it `pending` until the User returns.

**Decision and evidence:** The User accepted the outcome in chat on 2026-11-19 at 23:24 ("1" to the offered choice "accept and close the Change"), after the Project Manager presented the diff and Quality's `proceed` at 5474d68. Quality's advisory on the unnumbered trigger rows was presented and did not block acceptance.

## Closure

**Status:** closed

- [x] Every included artifact or gate has terminal status and completion evidence.
- [x] Intent and outcome are `approved`.
- [x] Quality has recorded a `proceed` judgment.
- [x] Open Quality Issues contains `None`.
- [x] User validation is `accepted`, or its `not applicable` status and explicit User delegation are recorded in the artifact row.
- [x] The feature branch is squash-integrated into `development`, or the `Version control` row is `not applicable` with its recorded reason.
- [x] Current blocker is `none`.
- [x] The observable outcome is demonstrated.
- [x] The Project Manager ran the `syspilot.contract-statistics` skill after validation and the record exists in `.syspilot/stats/`.

**Final outcome:** The User accepted the Change on 2026-11-19 and it was squash-integrated into `development` as `70f7602`. The third revalidation trigger "No tag-run evidence" is replaced by a baseline rule: when no successful tag run exists to compare against, triggers 1 and 2 count as fired. `SYSP_REQ_RELEASE_REVALIDATION`, `SYSP_VC_RELEASE_REVALIDATION_1`, the Release Process and its example carry the rule; code, workflow and the v0.10.0 record are unchanged. Quality reported `proceed` at 5474d68 with strict build, MECE and Trace clean; no test suite was run because no code or test changed. Checkout statistics recorded 4 actors, 74 calls and 239.6 AIU, with 52% before the first handover to Quality; the window starts at the release gate, so the earlier discussion is not counted. Advisory not acted on: the rule says "triggers 1 and 2" while the table rows are unnumbered. Nothing was pushed.
