# Change Process

Use this process for every modification to versioned source code or documentation. Each such modification needs a durable, checkable agreement about intent, owned artifacts, evidence, and closure. The Syspilot Project Manager owns this process and its canonical template.

This process applies the [Contract Documents](contract-documents.md) method. The canonical Change Contract template lives here. A concrete change starts as a tailored copy at `docs/changes/<change>.md`.

## Process Definition

- **Applicability:** Every modification to versioned source code or documentation.
- **Canonical template:** The `Canonical Change Contract Template` section in this document.
- **Concrete instances:** `docs/changes/<change>.md`.
- **Initial responsibility:** Syspilot Project Manager, who creates the Change Contract, completes its intent and required fields, and records user approval or the autonomous authority that makes the approval checkpoint not applicable.
- **First handoff:** Syspilot Architect, who determines the required architecture and specification work before further artifact owners proceed.
- **Closure responsibility:** Syspilot Project Manager.
- **Closure conditions:** The checklist in the template's `Closure` section.

Artifact work starts after the Project Manager records the user's approval of the intent and outcome or the autonomous authority that makes this checkpoint not applicable. The first responsibility transfer is to the Architect. Later transfers follow the included work that can progress. After Quality can proceed, Quality communicates its judgment and supporting evidence directly to the Project Manager before responsibility transfers directly to the User for validation. The User communicates an applicable validation decision directly to the Project Manager, and responsibility returns to the Project Manager only for closure. A forwarded claim from another actor is not evidence of Quality's or the User's decision.

### Change Artifact Ownership

| Artifact type | Owner | Completion evidence |
|---|---|---|
| Change Process and Change Contract template | Syspilot Project Manager | Process rules and canonical template remain coherent and current |
| Change Contract structure and lifecycle | Syspilot Project Manager | Current state, responsibility, and final outcome are explicit |
| Intent and outcome | Syspilot Project Manager | Goal, value, scope, and observable outcome are explicit and approved |
| Product specification and architecture decisions | Syspilot Architect | Changed stories, requirements, criteria, architecture, and realized files are linked; relevant checks pass |
| User-facing documentation | Syspilot Technical Writer | The agreed documentation surface is coherent and user-oriented; relevant factual owners reviewed it; `doc` Needs and `includes` links are current; the documentation build passes |
| Implementation and unit verification | Syspilot Developer | Changed implementation artifacts, durable technical decisions, and automated verification results are linked |
| Acceptance test design and results | Syspilot Tester | Black-box scenarios trace to the intended outcome and their results are recorded |
| Quality review | Syspilot Quality | Current verification judgment is `proceed` and no open quality issue remains |
| User validation and approval | User | The observable outcome is accepted, changes are requested, or autonomous authority makes validation not applicable |
| Closure decision | Syspilot Project Manager | Final outcome, validation disposition, and integration state are recorded |

User-facing documentation is optional. The Technical Writer includes it when a change must add or update derived explanations, using incoming `included_in` links on changed requirements to identify documentation surfaces for impact review. Authoritative textual product artifacts remain owned by their declared artifact owners regardless of path or file format.

The Technical Writer may consult factual artifact owners directly for clarification and review of accuracy and understandability. Consultation transfers neither current Contract responsibility, artifact ownership, nor factual authority without an explicit handoff.

## Tailoring Rules

- Intent and outcome, Quality review, and Closure are required whenever this process is used.
- User validation and approval is required in user-guided changes.
- In autonomous changes, user approval and validation checkpoints are `not applicable` when the collaboration agreement explicitly delegates that authority; the Contract records the authority and does not claim user validation.
- In unattended changes, user approval or validation remains pending until the user returns; absence does not make the checkpoint `not applicable`.

## Change Contract Initialization

The Project Manager initializes a change as one consistent version-controlled state:

1. Choose a lowercase, hyphenated change name.
2. Create the branch prescribed by the project's branching policy using that change name.
3. Copy the canonical template from `# Change Contract: {NAME}` through the end of this file to `docs/changes/<change>.md`.
4. Replace the placeholders, tailor the artifact set, and complete the header and `Intent And Outcome` section.
5. Record user agreement on the intent and outcome, or record the autonomous authority that makes this checkpoint `not applicable`, and set the intent status to `approved`.
6. Commit the branch and initialized Change Contract.
7. Transfer current responsibility to the Syspilot Architect as the first artifact owner.

## Canonical Change Contract Template

# Change Contract: {NAME}

**Status:** proposed | approved | active | blocked | review | accepted | closed<br>
**Process owner:** Syspilot Project Manager<br>
**Current responsibility:** Syspilot Project Manager<br>
**Current blocker:** none | {decision or action currently needed}<br>
**Created:** {DATE}<br>
**Branch:** {BRANCH OR NOT APPLICABLE}<br>
**Collaboration mode:** {Describe when user agreement is required during this change}

## Intent And Outcome

**Owner:** Syspilot Project Manager<br>
**Status:** draft | approved<br>
**Approval evidence:** pending | not applicable: {autonomous authority} | {user agreement reference and date}

### Goal

{What should become true?}

### Value

{Who benefits, and why does this matter?}

### Scope

{Which product behavior and artifacts may change?}

### Observable Outcome

{What evidence will demonstrate that the goal was achieved?}

## Artifact Applicability And Ownership

**Applicability:** Each artifact owner decides and updates its own row.<br>
**Status:** pending | complete

| Artifact type | Included | Owner | Completion evidence | Status |
|---|---|---|---|---|
| Intent and outcome | yes | Syspilot Project Manager | Goal, value, scope, and observable outcome are explicit and approved | draft / approved |
| Product specification and architecture decisions | yes / not applicable: {reason} | Syspilot Architect | Changed specification and architecture artifacts are linked and checked | pending / not applicable |
| User-facing documentation | yes / not applicable: {reason} | Syspilot Technical Writer | Agreed documentation surface is coherent and user-oriented; factual-owner review is recorded; `doc` Needs and `includes` links are current; documentation builds cleanly | pending / complete / not applicable |
| Implementation and unit verification | yes / not applicable: {reason} | Syspilot Developer | Changed artifacts, durable technical decisions, and automated verification results are linked | pending / not applicable |
| Acceptance test design and results | yes / not applicable: {reason} | Syspilot Tester | Black-box scenarios and results trace to the intended outcome | pending / not applicable |
| Quality review | yes | Syspilot Quality | Current verification judgment is `proceed` and no open quality issue remains | pending |
| User validation and approval | yes / not applicable: {autonomous authority} | User | Observable outcome is accepted or changes are requested; autonomous closure records that user validation did not occur | pending / accepted / changes requested / not applicable |
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

In autonomous mode, set this artifact to `not applicable` only when the collaboration agreement explicitly delegates closure authority, and record that authority. In unattended mode, keep it `pending` until the user returns.

**Decision and evidence:** {user decision and reference | autonomous authority and statement that user validation did not occur}

## Closure

**Owner:** Syspilot Project Manager<br>
**Status:** pending | accepted | closed

- [ ] Every included artifact has terminal status and completion evidence.
- [ ] Intent and outcome are `approved`.
- [ ] Quality has recorded a `proceed` judgment.
- [ ] Open Quality Issues contains `None`.
- [ ] User validation is `accepted`, or its `not applicable` status and autonomous authority are recorded.
- [ ] Current blocker is `none`.
- [ ] The observable outcome is demonstrated.
- [ ] Integration or publication has been completed by the authorized actor, or its next owner is explicit.

**Final outcome:** {accepted result, integration reference, or reason for closure without integration}
