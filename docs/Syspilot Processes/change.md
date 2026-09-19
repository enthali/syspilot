# Change Process

Use this process for every modification to versioned source code or documentation. Each such modification needs a durable, checkable agreement about intent, owned artifacts, evidence, and closure. The Syspilot Project Manager owns this process and its canonical template.

This process applies the [Contract Documents](contract-documents.md) method. The canonical Change Contract template lives here. A concrete change starts as a tailored copy at `docs/changes/<change>.md`.

## Process Definition

- **Applicability:** Every modification to versioned source code or documentation.
- **Canonical template:** The `Canonical Change Contract Template` section in this document.
- **Concrete instances:** `docs/changes/<change>.md`.
- **Initial responsibility:** Syspilot Project Manager, who creates the Change Contract, completes its intent and required fields, and prepares it for the User-owned `Contract release` gate.
- **First handoff:** Syspilot Architect, who determines the required architecture and specification work before further artifact owners proceed.
- **Closure responsibility:** Syspilot Project Manager.
- **Closure conditions:** The checklist in the template's `Closure` section.

Artifact work starts only after the User sets the `Contract release` gate to `approved`. A settled intent or operation mode provides no alternative start condition. The first responsibility transfer is to the Architect. After Quality can proceed, Quality communicates its judgment and supporting evidence directly to the Project Manager before responsibility transfers directly to the User for validation. The User communicates an applicable validation decision directly to the Project Manager, and responsibility returns to the Project Manager only for Closure. A forwarded claim from another actor is not evidence of Quality's or the User's decision.

## Change Contract Initialization

The Project Manager initializes a change as one consistent version-controlled state:

1. Choose a lowercase, hyphenated change name.
2. Create the Change's feature branch from `development` using that change name.
3. Copy the canonical template from `# Change Contract: {NAME}` through the end of this file to `docs/changes/<change>.md`.
4. Select the agreed Operation Mode, remove the template note and the two non-applicable mode rules, replace the remaining placeholders, tailor the artifact set, and complete the header and `Intent And Outcome` section.
5. Record evidence that the intent and outcome text is settled, and set its status to `approved`.
6. Ask the User to set the User-owned `Contract release` gate to `approved`; no other actor may set the gate, and artifact work remains blocked until it reads `approved`.
7. Commit the branch and initialized Change Contract.
8. Transfer current responsibility to the Syspilot Architect as the first artifact owner.

## Canonical Change Contract Template

# Change Contract: {NAME}

**Status:** proposed | approved | active | blocked | review | accepted | closed<br>
**Process owner:** Syspilot Project Manager<br>
**Current responsibility:** Syspilot Project Manager<br>
**Current blocker:** none | {decision or action currently needed}<br>
**Created:** {DATE}<br>
- **Operation Mode**: user-guided (default) | autonomous | unattended; select one with the User before Contract release

*(Template note - delete this line and the two non-applicable mode bullets once the mode is picked.)*

- **user-guided** - every actor involves the user in its decision-making before proceeding.
- **autonomous** - every actor decides on its own; when genuinely unsure, it asks the user directly and pauses only its own step until answered.
- **unattended** - the user is not reachable. When unsure, the actor flags `USER REVIEW REQUIRED` in this document, takes the simplest KISS path that is cheapest to reverse or amend, and keeps the change moving. The PM reviews flagged points once reachable again; decision ownership remains with the actor that made the decision.


## Intent And Outcome

**Owner:** Syspilot Project Manager<br>
**Status:** draft | approved<br>
**Approval evidence:** pending | {evidence that the intent and outcome text is settled}

### Goal

{What should become true?}

### Value

{Who benefits, and why does this matter?}

### Scope

{Which product behavior and artifacts may change?}

### Observable Outcome

{What evidence will demonstrate that the goal was achieved?}

## Artifacts, Ownership And Process Gates

**Applicability:** Each artifact owner decides and updates its own row.<br>
**Status:** pending | complete

| Artifact or gate | Included | Owner | Completion evidence | Status |
|---|---|---|---|---|
| Intent and outcome | yes | Syspilot Project Manager | Goal, value, scope, and observable outcome are explicit and approved | draft / approved |
| Contract release | yes | User | User authorization to start the Change; no other actor may set this gate | pending / approved |
| Version control | yes / not applicable: {reason; delete the corresponding empty owner section} | Syspilot Project Manager | Feature branch name and integration state; the branch is squash-integrated into `development` at closure | active / merged / not applicable |
| Product specification and architecture decisions | yes / not applicable: {reason; delete the corresponding empty owner section} | Syspilot Architect | Changed specification and architecture artifacts are linked and checked | pending / not applicable |
| User-facing documentation | yes / not applicable: {reason; delete the corresponding empty owner section} | Syspilot Technical Writer | Agreed documentation surface is coherent and user-oriented; factual-owner review is recorded; `doc` Needs and `includes` links are current; documentation builds cleanly | pending / complete / not applicable |
| Implementation and unit verification | yes / not applicable: {reason; delete the corresponding empty owner section} | Syspilot Developer | Changed artifacts, durable technical decisions, and automated verification results are linked | pending / not applicable |
| Acceptance test design and results | yes / not applicable: {reason; delete the corresponding empty owner section} | Syspilot Tester | Black-box scenarios and results trace to the intended outcome | pending / not applicable |
| Quality review | yes | Syspilot Quality | Current verification judgment is `proceed` and no open quality issue remains | pending |
| User validation and approval | yes / not applicable: {explicit User delegation recorded in this row; retain the section below as evidence} | User | Observable outcome is accepted or changes are requested; a delegated `not applicable` status records that User validation did not occur | pending / accepted / changes requested / not applicable |
| Closure decision | yes | Syspilot Project Manager | Final outcome, validation disposition, and integration state are recorded | pending |

## Architecture And Specification

**Owner:** Syspilot Architect<br>
**Status:** pending | in progress | complete | not applicable

### Affected Artifacts

| Artifact | Change | Rationale |
|---|---|---|
| {path or specification ID} | {add / modify / remove} | {why} |

### Decisions And Evidence

| Decision or check | Evidence |
|---|---|
| {architecture decision, consistency check, or traceability result} | {link or result} |

## User-Facing Documentation

**Owner:** Syspilot Technical Writer<br>
**Status:** pending | in progress | complete | not applicable

### Documentation Plan And Ownership

| Documentation surface | `doc` Need | Requirements included | Status |
|---|---|---|---|
| {path or surface} | {Need ID and `realized_by` path} | {requirement IDs linked through `includes`} | pending / complete |

### Consultations And Factual Reviews

| Documentation surface | Consulted artifact owner | Review question | Evidence and disposition |
|---|---|---|---|
| {path or surface} | {owner} | Is this accurate and understandable for the intended user? | {result or link} |

### Changed Documentation And Verification

| Artifact | Change | Verification evidence |
|---|---|---|
| {path or `doc` Need} | {what changed} | {review and clean-build result} |

## Implementation And Unit Verification

**Owner:** Syspilot Developer<br>
**Status:** pending | in progress | complete | not applicable

### Decisions And Evidence

Record implementation decisions that remain relevant to understanding or maintaining the outcome. The evidence explains why the chosen approach fits better than the relevant alternatives.

| Decision | Chosen approach | Relevant alternatives | Rationale and evidence |
|---|---|---|---|
| {implementation question} | {selected algorithm, structure, or technique} | {alternatives considered} | {why this choice fits and what supports it} |

### Changed Artifacts And Verification

| Artifact | Change | Verification evidence |
|---|---|---|
| {path} | {what changed} | {test or check and result} |

## Acceptance Testing

**Owner:** Syspilot Tester<br>
**Status:** pending | in progress | passed | failed | not applicable

| Scenario | Traces to | Result | Evidence |
|---|---|---|---|
| {black-box scenario} | {outcome, story, or acceptance criterion} | pending / pass / fail | {result or link} |

## Quality Review

**Owner:** Syspilot Quality<br>
**Status:** pending | in progress | proceed | blocked

**Current judgment:** {holistic assessment of the currently valid artifacts and evidence}

### Applied Review Methods

| Method | Selected scope | Evidence | Findings | Limits |
|---|---|---|---|---|
| {review method} | {objects, peer scope, traversal depth, or other selected boundary} | {inputs and reproducible result} | {observed issues or no finding} | {data, semantic, or analysis limits} |

Quality communicates its `proceed` judgment and supporting evidence directly to the Project Manager before the Project Manager presents the verified outcome for validation. Another actor's forwarded claim does not establish Quality's decision.

### Open Quality Issues

Keep this table synchronized with currently open issues. For each issue, Quality transfers current responsibility to the owner of the affected artifact. When Quality confirms the required outcome, update the affected artifact or evidence and remove the resolved row. At closure this table contains `None`.

| Artifact | Current issue | Required outcome |
|---|---|---|
| {artifact} | {observable issue} | {positive condition needed for proceed} |

## User Validation And Approval

**Owner:** User<br>
**Recorded by:** Syspilot Project Manager<br>
**Status:** pending | accepted | changes requested | not applicable

Quality's `proceed` judgment verifies that the change is ready for validation; it does not validate user value. For an included validation, the Project Manager presents the observable outcome after receiving Quality's direct judgment and evidence. The User communicates the validation decision directly to the Project Manager, who records the decision and evidence. Another actor's forwarded claim does not establish the User's decision. If the user requests changes, the Project Manager transfers responsibility to an included artifact owner that can produce the required outcome.

Current responsibility remains with the User from Quality's handoff until the validation decision is recorded. The Project Manager's presentation and recording duties support that User-owned artifact; they do not make the Project Manager the validation owner or an intermediate responsibility relay.

Set this artifact to `not applicable` only when the User explicitly delegates validation of the finished outcome and that delegation is recorded in its artifact row. Operation mode does not delegate validation. In unattended mode, keep it `pending` until the User returns.

**Decision and evidence:** {user decision and reference | explicit User delegation from the artifact row and statement that User validation did not occur}

## Closure

**Owner:** Syspilot Project Manager<br>
**Status:** pending | accepted | closed

- [ ] Every included artifact or gate has terminal status and completion evidence.
- [ ] Intent and outcome are `approved`.
- [ ] Quality has recorded a `proceed` judgment.
- [ ] Open Quality Issues contains `None`.
- [ ] User validation is `accepted`, or its `not applicable` status and explicit User delegation are recorded in the artifact row.
- [ ] Current blocker is `none`.
- [ ] The observable outcome is demonstrated.

**Final outcome:** {accepted result, integration reference, or reason for closure without integration}
