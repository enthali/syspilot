# Change Contract: impact-artifact-list

**Status:** proposed<br>
**Process owner:** Project Manager<br>
**Current responsibility:** Project Manager<br>
**Current blocker:** Draft parked on `development` until `ontology-example` is closed; then the Project Manager creates `feature/impact-artifact-list`, agrees the Operation Mode with the User, and asks for `Contract release`<br>
**Created:** 2026-11-15<br>
- **Operation Mode**: user-guided (default) | autonomous | unattended; select one with the User before Contract release

*(Template note - delete this line and the two non-applicable mode bullets once the mode is picked.)*

- **user-guided** - every actor involves the user in its decision-making before proceeding.
- **autonomous** - every actor decides on its own; when genuinely unsure, it asks the user directly and pauses only its own step until answered.
- **unattended** - the user is not reachable. When unsure, the actor flags `USER REVIEW REQUIRED` in this document, takes the simplest KISS path that is cheapest to reverse or amend, and keeps the change moving. The PM reviews flagged points once reachable again; decision ownership remains with the actor that made the decision.

## Handover log

Owned by: Project Manager

The handing-over actor appends one line as the last act before handing over, in the same commit that changes `Current responsibility`, taking `Date` as `YYYY-MM-DD` and `Time` as `HH:MM` in 24-hour local time from the system clock at that moment. The note states what the owner did and the facts that change the next owner's situation; evidence stays in the owner's section and remaining work in the open rows. The handover goes to the next actor that follows from the logical flow of the Change. The log explains transitions; the header stays authoritative.

| Date | Time | From | To | Note |
|--|--|--|--|--|

## Intent And Outcome

**Status:** draft<br>
**Approval evidence:** pending; content agreed with the User in the Project Manager chat on 2026-11-15, to be confirmed at initialization.

### Goal

The `Affected Artifacts` table of every Change Contract is built from an impact query with the `syspilot.impact-python` skill. The Architect records the query, gives every reported ID one row with an explicit disposition (`no change`, `modified`, `added`, `removed`), and adds by hand the artifacts the query cannot report, such as new ones.

### Value

No Syspilot artifact currently assigns anyone to determine what a Change affects; up to v0.9 the Change Manager did this, and the role no longer exists. Quality's methods already depend on the result: Quality applies MECE and Trace to "the objects the applicable Contract records as impacted", but nothing produces that record. Placing the instruction in the Contract table itself, and not only in the Architect's role card, keeps it in front of the actor, because the Contract is re-read at every acknowledgement while a role card is read once and may be lost after context compaction.

### Scope

- Canonical template `docs/Syspilot Contracts/change.md`: the `Affected Artifacts` subsection names the impact skill as its source, carries an `Impact query` line (start IDs, direction, depth), and the `Change` column takes `no change / modified / added / removed`; the completion evidence of the `Product specification and architecture decisions` row requires the table built from the query with every reported ID dispositioned.
- Example `docs/Example Contracts/change.md` carries the same change.
- The Change Contract requirement and its VCs state the rule; the guide `docs/change-contract.md` stays consistent where it describes the Architect's or Quality's inputs.
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
| Intent and outcome | yes | Project Manager | Goal, value, scope, and observable outcome are explicit and approved | draft |
| Contract release | yes | User | User authorization to start the Change; no other actor may set this gate | pending |
| Version control | yes | Project Manager | Feature branch `feature/impact-artifact-list`; squash-integrated into `development` at closure | pending |
| Infrastructure impact | not applicable: no workflow, CI, or packaging artifact changes | Admin | Affected workflow, CI, and packaging artifacts are updated, confirmed by their current owner rather than inferred from a Needs-only impact query | not applicable |
| Product specification and architecture decisions | yes | Architect | Affected Artifacts built from the impact query, every reported ID dispositioned; changed requirement and VC linked and checked | pending |
| User-facing documentation | yes | Technical Writer | `docs/change-contract.md` is consistent with the template; documentation builds cleanly | pending |
| Example sync | yes | Technical Writer | `docs/Example Contracts/change.md` carries the change; documentation builds cleanly | pending |
| Implementation and unit verification | yes | Developer | Canonical template changed; unit test commands and results recorded | pending |
| Acceptance test design and results | not applicable: a Markdown process artifact without executable behavior; Quality's review covers it | Tester | Requirement tests written and run by the Tester, with their commands and results, and the means for User validation trace to the intended outcome | not applicable |
| Quality review | yes | Quality | Quality reviewed the recorded commands and results; current verification judgment is `proceed` and no open quality issue remains | pending |
| User validation and approval | yes | User | Observable outcome is accepted or changes are requested | pending |
| Closure decision | yes | Project Manager | Final outcome, validation disposition, and integration state are recorded | pending |

## Architecture And Specification

**Status:** pending

### Affected Artifacts

| Artifact | Change | Rationale |
|---|---|---|
| {path or specification ID} | {add / modify / remove} | {why} |

### Decisions And Evidence

| Decision or check | Evidence |
|---|---|
| {architecture decision, consistency check, or traceability result} | {link or result} |

## User-Facing Documentation

**Status:** pending

### Documentation Plan And Ownership

| Documentation surface | `doc` Need | Requirements included | Status |
|---|---|---|---|
| {path or surface} | {Need ID and `realized_by` path} | {requirement IDs linked through `includes`} | pending |

### Consultations And Factual Reviews

| Documentation surface | Consulted artifact owner | Review question | Evidence and disposition |
|---|---|---|---|
| {path or surface} | {owner} | Is this accurate and understandable for the intended user? | {result or link} |

### Changed Documentation And Verification

| Artifact | Change | Verification evidence |
|---|---|---|
| {path or `doc` Need} | {what changed} | {review and clean-build result} |

## Example Sync

**Status:** pending

| Artifact | Change | Verification evidence |
|---|---|---|
| {example path or `doc` Need} | {what changed, or why the change does not hold for a general project} | {review and clean-build result} |

## Implementation And Unit Verification

**Status:** pending

### Decisions And Evidence

Record implementation decisions that remain relevant to understanding or maintaining the outcome. The evidence explains why the chosen approach fits better than the relevant alternatives.

| Decision | Chosen approach | Relevant alternatives | Rationale and evidence |
|---|---|---|---|
| {implementation question} | {selected algorithm, structure, or technique} | {alternatives considered} | {why this choice fits and what supports it} |

### Changed Artifacts And Verification

| Artifact | Change | Verification evidence |
|---|---|---|
| {path} | {what changed} | {test or check and result} |

## Quality Review

**Status:** pending

**Current judgment:** {holistic assessment of the currently valid artifacts and evidence}

### Applied Review Methods

| Method | Selected scope | Evidence | Findings | Limits |
|---|---|---|---|---|
| {review method} | {objects, peer scope, traversal depth, or other selected boundary} | {inputs and reproducible result} | {observed issues or no finding} | {data, semantic, or analysis limits} |

Verification is fully automated. Quality reviews the commands and results that the Developer and the Tester recorded, and executes a check itself only when a recorded result cannot support its judgment, recording the reason in the table above. A Markdown process artifact whose content has no automated check is verified by Quality's review, and the table above records that review and its limits.

Quality communicates its `proceed` judgment and supporting evidence directly to the Project Manager before the Project Manager presents the verified outcome for validation. Another actor's forwarded claim does not establish Quality's decision.

### Open Quality Issues

Keep this table synchronized with currently open issues. A missing automation is an open issue whose row names the task that closes it, the owner of that task, and the completion evidence. For each issue, Quality transfers current responsibility to the owner of the affected artifact. When Quality confirms the required outcome, update the affected artifact or evidence and remove the resolved row. At closure this table contains `None`.

| Artifact | Current issue | Required outcome |
|---|---|---|
| {artifact} | {observable issue} | {positive condition needed for proceed} |

## User Validation And Approval

**Recorded by:** Project Manager<br>
**Status:** pending

Quality's `proceed` judgment verifies that the change is ready for validation; it does not validate user value. For an included validation, the Project Manager presents the observable outcome after receiving Quality's direct judgment and evidence. The User communicates the validation decision directly to the Project Manager, who records the decision and evidence. Another actor's forwarded claim does not establish the User's decision. If the user requests changes, the Project Manager transfers responsibility to an included artifact owner that can produce the required outcome.

Current responsibility remains with the User from Quality's handoff until the validation decision is recorded. The Project Manager's presentation and recording duties support that User-owned artifact; they do not make the Project Manager the validation owner or an intermediate responsibility relay.

Set this artifact to `not applicable` only when the User explicitly delegates validation of the finished outcome and that delegation is recorded in its artifact row. Operation mode does not delegate validation. In unattended mode, keep it `pending` until the User returns.

**Decision and evidence:** {user decision and reference}

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
