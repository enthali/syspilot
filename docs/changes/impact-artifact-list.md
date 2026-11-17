# Change Contract: impact-artifact-list

**Status:** accepted<br>
**Process owner:** Project Manager<br>
**Current responsibility:** Project Manager<br>
**Current blocker:** none<br>
**Created:** 2026-11-15<br>
- **Operation Mode**: unattended, directed by the User on 2026-11-16.

- **unattended** - the user is not reachable. When unsure, the actor flags `USER REVIEW REQUIRED` in this document, takes the simplest KISS path that is cheapest to reverse or amend, and keeps the change moving. The PM reviews flagged points once reachable again; decision ownership remains with the actor that made the decision.

## Handover log

Owned by: Project Manager

The handing-over actor appends one line as the last act before handing over, in the same commit that changes `Current responsibility`, taking `Date` as `YYYY-MM-DD` and `Time` as `HH:MM` in 24-hour local time from the system clock at that moment. The note states what the owner did and the facts that change the next owner's situation; evidence stays in the owner's section and remaining work in the open rows. The handover goes to the next actor that follows from the logical flow of the Change. The log explains transitions; the header stays authoritative.

| Date | Time | From | To | Note |
|--|--|--|--|--|
| 2026-11-16 | 23:03 | Project Manager | Architect | User directed this reviewed Change to start unattended after ontology-link-obligations; specify impact-skill use without binding the Contract to a skill implementation. |
| 2026-11-16 | 23:05 | Architect | Developer | Requirement and VC specified with the template wording in Decisions And Evidence; change the canonical template. |
| 2026-11-16 | 23:08 | Developer | Technical Writer | Canonical template changed as specified; strict build clean, 233 tests OK. The Example template and the guide still hold the old wording. |
| 2026-11-16 | 23:09 | Technical Writer | Quality | Synced the Example template and guide; Architect confirmed fidelity. Strict build clean, 29 setup-example tests pass. Methodology remains accurate without a change. |
| 2026-11-16 | 23:10 | Quality | User | Review `proceed` at the committing revision; template, Example and guide agree with the requirement and results re-verified, no open quality issue. Validation stays with you; the Project Manager presents the outcome. |
| 2026-11-17 | 09:35 | User | Project Manager | User accepted the Impact Change; integration and closure follow. |

## Intent And Outcome

**Status:** approved<br>
**Approval evidence:** The User agreed the impact-list intent on 2026-11-15, requested the implementation-independent skill reference on 2026-11-16, and confirmed the draft was reviewed before directing this Change to start unattended.

### Goal

The `Affected Artifacts` table of every Change Contract is built using the project's impact skill. The Architect records the query, gives every reported ID one row with an explicit disposition (`no change`, `modified`, `added`, `removed`), and adds by hand the artifacts the query cannot report, such as new ones.

### Value

No Syspilot artifact currently assigns anyone to determine what a Change affects; up to v0.9 the Change Manager did this, and the role no longer exists. Quality's methods already depend on the result: Quality applies MECE and Trace to "the objects the applicable Contract records as impacted", but nothing produces that record. Placing the instruction in the Contract table itself, and not only in the Architect's role card, keeps it in front of the actor, because the Contract is re-read at every acknowledgement while a role card is read once and may be lost after context compaction.

### Scope

- Canonical template `docs/Syspilot Contracts/change.md`: the `Affected Artifacts` subsection names the impact skill as its source, carries an `Impact query` line (start IDs, direction, depth), and the `Change` column takes `no change / modified / added / removed`; the completion evidence of the `Product specification and architecture decisions` row requires the table built from the query with every reported ID dispositioned.
- Example `docs/Example Contracts/change.md` carries the same change.
- Refer to the impact skill by its purpose, not a particular skill name or file, so a project can replace its implementation without changing the Contract.
- The Change Contract requirement and its VCs state the rule; the guide `docs/change-contract.md` stays consistent where it describes the Architect's or Quality's inputs.
- Scoping evidence: the impact query from `SYSP_REQ_CHANGE_ARTIFACTS`, both directions at depth one, found its parent requirement, User Story, four VCs and the Change Contract, Example Contracts and Methodology documentation Needs. These are candidates rather than a complete list.
- The impact analysis is not a separate artifact or gate; it is the method that fills the existing table.
- Out of scope: the impact skill itself; Quality's methods; other Contract kinds; role-card wording beyond what consistency requires.
- Crew: Architect, Developer, Technical Writer, Quality.

### Observable Outcome

- Canonical template and example show the sourced `Affected Artifacts` subsection, the `Impact query` line, the four dispositions, and the updated row evidence.
- The requirement and a focused VC state the rule; the strict documentation build and the test suite pass.

## Artifacts, Ownership And Process Gates

**Applicability:** Each artifact owner decides and updates its own row.<br>
**Scope change:** When the approved intent widens after a row reached a terminal status, `Intent and outcome` returns to `draft` until it is approved again, and each owner whose terminal row the wider intent may affect reassesses it: the owner sets the row back to `pending` or records in the row why its evidence still holds.<br>
**Ownership:** The `Owner` column of this table is the only statement of artifact and gate ownership in the Contract; section headings name no artifact owner.<br>
**Status:** pending

| Artifact or gate | Included | Owner | Completion evidence | Status |
|---|---|---|---|---|
| Intent and outcome | yes | Project Manager | Goal, value, scope, and observable outcome are explicit and approved | approved |
| Contract release | yes | User | User reviewed the draft and directed the Change to start unattended on 2026-11-16 after the preceding Change | approved |
| Version control | yes | Project Manager | Feature branch `feature/impact-artifact-list`; squash-integrated into `development` at closure | active |
| Infrastructure impact | not applicable: no workflow, CI, or packaging artifact changes | Admin | Affected workflow, CI, and packaging artifacts are updated, confirmed by their current owner rather than inferred from a Needs-only impact query | not applicable |
| Product specification and architecture decisions | yes | Architect | Affected Artifacts built from the impact query, every reported ID dispositioned; changed requirement and VC linked and checked | approved |
| User-facing documentation | yes | Technical Writer | Guide updated at e3b90a3; Architect confirmed fidelity to SYSP_REQ_CHANGE_ARTIFACTS and VC_5; current `doc` links remain applicable, strict build zero warnings | complete |
| Example sync | yes | Technical Writer | Example template mirrors canonical wording at e3b90a3; Architect confirmed the match; strict build clean and 29 setup-example tests pass | complete |
| Implementation and unit verification | yes | Developer | Canonical template changed; unit test commands and results recorded | complete |
| Acceptance test design and results | not applicable: a Markdown process artifact without executable behavior; Quality's review covers it | Tester | Requirement tests written and run by the Tester, with their commands and results, and the means for User validation trace to the intended outcome | not applicable |
| Quality review | yes | Quality | Quality reviewed the recorded commands and results; Quality reviewed the recorded commands and results and re-ran the build and setup-example tests; judgment `proceed` at e9e6071, no open quality issue | complete |
| User validation and approval | yes | User | User accepted the Impact Change directly on 2026-11-17 | accepted |
| Closure decision | yes | Project Manager | Final outcome, validation disposition, and integration state are recorded | pending |

## Architecture And Specification

**Status:** approved

### Affected Artifacts

| Artifact | Change | Rationale |
|---|---|---|
| SYSP_REQ_CHANGE_ARTIFACTS | modified | States the impact-skill rule, the `Impact query` line and the four dispositions. |
| SYSP_VC_CHANGE_ARTIFACTS_5 | added | Verifies the new rule. |
| SYSP_REQ_CHANGE_CONTRACT | no change | Parent; its rule is not altered. |
| SYSP_US_CHANGE_CONTRACT | no change | The story already covers Contract content. |
| SYSP_VC_CHANGE_ARTIFACTS_1 | no change | Applicability rows stay as stated. |
| SYSP_VC_CHANGE_ARTIFACTS_2 | no change | Infrastructure evidence is unaffected. |
| SYSP_VC_CHANGE_ARTIFACTS_3 | no change | Ontology Binding is unaffected. |
| SYSP_VC_CHANGE_ARTIFACTS_4 | no change | Tailoring rules are unaffected. |
| SYSP_DOC_CHANGE_CONTRACT | no change | Guide docs/change-contract.md is updated by the Technical Writer, who owns it; the `includes` link already exists. |
| SYSP_DOC_EXAMPLE_CONTRACTS | no change | Need unchanged; the example file changes (Technical Writer). |
| SYSP_DOC_METHODOLOGY | no change | Reviewed as candidate; Technical Writer decides whether the text needs a mention. |
| docs/Syspilot Contracts/change.md | modified | Developer: `Affected Artifacts` sourced from the impact skill, `Impact query` line, dispositions, row evidence wording. |
| docs/Example Contracts/change.md | modified | Technical Writer: same change in the example. |

### Decisions And Evidence

| Decision or check | Evidence |
|---|---|
| Wording for the template: source line "Built with the project's impact skill"; `Impact query: {start IDs; direction; depth}`; column `Change` takes `no change / modified / added / removed`; row evidence "Affected Artifacts built from the impact query, every reported ID dispositioned". The skill is named by purpose only. | SYSP_REQ_CHANGE_ARTIFACTS, SYSP_VC_CHANGE_ARTIFACTS_5 |
| Impact query: `get_need_links.py SYSP_REQ_CHANGE_ARTIFACTS --direction both --depth 1 --simple --no-build` on the freshly built model reported the 2 outgoing and 7 incoming IDs dispositioned above. Candidates, not complete scope. | Query result; strict build 0 warnings |

## User-Facing Documentation

**Status:** complete

### Documentation Plan And Ownership

| Documentation surface | `doc` Need | Requirements included | Status |
|---|---|---|---|
| `docs/change-contract.md` | SYSP_DOC_CHANGE_CONTRACT, `realized_by` that path | Existing SYSP_REQ_CHANGE_ARTIFACTS link remains applicable | complete |
| `docs/Example Contracts/change.md` | SYSP_DOC_EXAMPLE_CONTRACTS, `realized_by: docs/Example Contracts/index.md` covers the folder | Existing SYSP_REQ_CHANGE_ARTIFACTS link remains applicable | complete |

Documentation impact: the incoming depth-one results from SYSP_REQ_CHANGE_ARTIFACTS identify the Change Contract, Example Contracts and Methodology doc Needs. The first two surfaces change. Methodology needs no change: it explains ownership and general Contract principles without prescribing how this table is built, so its existing explanation remains accurate. The query also reports the new VC; verification remains with the responsible specification and implementation owners. No new documentation surface or `includes` link is needed.

### Consultations And Factual Reviews

| Documentation surface | Consulted artifact owner | Review question | Evidence and disposition |
|---|---|---|---|
| Guide and Example Change template | Architect | Do the query provenance, per-ID dispositions, manual additions and implementation-independent skill reference match the requirement and canonical template? | Directly confirmed e3b90a3 on 2026-11-16 at 23:09: faithful to SYSP_REQ_CHANGE_ARTIFACTS and VC_5, Example matches canonical template, no new gate or concrete skill dependency. Methodology unchanged is appropriate; no change requested |

### Changed Documentation And Verification

| Artifact | Change | Verification evidence |
|---|---|---|
| `docs/change-contract.md` | Explains the Architect's impact-sourced table, query fields, four dispositions, rationale and manual additions; no separate gate or tool-specific Contract dependency | `uv run python docs\docs-build.py clean`: zero warnings; `git diff --check`: pass (2026-11-16). Architect confirmed accuracy and understandability |
| `docs/methodology.md` | No change: current explanation remains accurate and does not duplicate this procedural detail | Reviewed against SYSP_REQ_CHANGE_ARTIFACTS |

## Example Sync

**Status:** complete

| Artifact | Change | Verification evidence |
|---|---|---|
| `docs/Example Contracts/change.md` | Mirrors the canonical Architect-row evidence, source sentence, `Impact query` fields and four dispositions verbatim | Strict clean build passes; `uv run python -m unittest discover -s tests -p test_acceptance_setup_examples.py`: 29 tests pass (2026-11-16). Architect confirmed the match |
| `docs/Example Actors/`, `docs/Example Ontology/` | No change: the rule belongs to the Change template, not actor cards or ontology definitions | No role or ontology change is required by this scope |

## Implementation And Unit Verification

**Status:** complete

### Decisions And Evidence

| Decision | Chosen approach | Relevant alternatives | Rationale and evidence |
|---|---|---|---|
| Template wording | Used the Architect's wording: a source sentence "Built with the project's impact skill", an `Impact query: {start IDs; direction; depth}` line, `Change` column `no change / modified / added / removed`, and the Architect row evidence extended with "Affected Artifacts built from the impact query, every reported ID dispositioned" | none | Wording is fixed by SYSP_REQ_CHANGE_ARTIFACTS and SYSP_VC_CHANGE_ARTIFACTS_5; the skill is named by purpose only, so a project can replace it |

### Changed Artifacts And Verification

| Artifact | Change | Verification evidence |
|---|---|---|
| `docs/Syspilot Contracts/change.md` | `Affected Artifacts` subsection sourced from the impact skill with the `Impact query` line and the four dispositions; the Architect row evidence requires the table | `python docs/docs-build.py clean` success, zero warnings; `python -m unittest discover -s tests` 233 OK. No test inspects the template text. `docs/Example Contracts/change.md` still holds the old wording (Technical Writer) |

## Quality Review

**Status:** complete

**Current judgment:** `proceed` at e9e6071. The requirement, VC_5, canonical template, Example template and guide agree: impact-sourced `Affected Artifacts`, `Impact query` line, four dispositions, and the Architect row evidence. The skill is named by purpose only. Results re-run by Quality: strict build clean, 29 setup-example tests OK.

### Applied Review Methods

| Method | Selected scope | Evidence | Findings | Limits |
|---|---|---|---|---|
| Recorded-result review | Diff 463ec01..e9e6071: SYSP_REQ_CHANGE_ARTIFACTS, SYSP_VC_CHANGE_ARTIFACTS_5, `docs/Syspilot Contracts/change.md`, `docs/Example Contracts/change.md`, `docs/change-contract.md`, Contract rows | Canonical and Example template edits are identical in wording and match the requirement; the guide describes the same fields; Quality re-ran `python docs/docs-build.py clean` (success) and `python -m unittest tests.test_acceptance_setup_examples` (29 OK); handover row times do not exceed their commits | no finding | No automated check reads template text, so the wording match is verified by reading; full suite (233) taken from the Developer's record |
| Impact check (`syspilot.impact-python`, both, depth 1) | SYSP_REQ_CHANGE_ARTIFACTS | Reports 2 outgoing and 8 incoming IDs; every one has a row in Affected Artifacts (VC_5 added), plus the two template files | no finding | Candidate list only; this Contract carries the query in Decisions And Evidence, not as an `Impact query` line, because it started on the old template |
| MECE (`syspilot.mece`, same-document) | SYSP_REQ_CHANGE_ARTIFACTS; peers in `req_change_contract.rst` | Script findings none; the new paragraph adds a table-sourcing rule beside applicability and does not contradict the peers | no finding | `semantic-content-review-required` and `structured-coverage-data-unavailable` remain |
| Trace (`syspilot.trace`, both, depth 2) | SYSP_REQ_CHANGE_ARTIFACTS | No unresolved target; VC_5 verifies the requirement | no finding | Edge semantics outside the changed links not re-read |

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

**Decision and evidence:** User accepted the outcome directly in the Project Manager chat on 2026-11-17.

## Closure

**Status:** pending

- [ ] Every included artifact or gate has terminal status and completion evidence.
- [ ] Intent and outcome are `approved`.
- [ ] Quality has recorded a `proceed` judgment.
- [ ] Open Quality Issues contains `None`.
- [ ] User validation is `accepted`, or its `not applicable` status and explicit User delegation are recorded in the artifact row.
- [ ] The feature branch is squash-integrated into `development`, or the `Version control` row is `not applicable` with its recorded reason.
- [ ] Current blocker is `none`.
- [ ] The observable outcome is demonstrated.

**Final outcome:** {accepted result, integration reference, or reason for closure without integration}
