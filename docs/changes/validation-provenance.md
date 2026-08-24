# Change Contract: Validation Provenance

**Status:** closed<br>
**Process owner:** Syspilot Project Manager<br>
**Current responsibility:** Syspilot Project Manager<br>
**Current blocker:** none<br>
**Created:** 2026-08-24<br>
**Branch:** feature/validation-provenance<br>
**Collaboration mode:** User-guided for intent and validation; otherwise autonomous within the approved intent.

## Intent And Outcome

**Owner:** Syspilot Project Manager<br>
**Status:** approved<br>
**Approval evidence:** User approved recording the agreed verification-to-validation evidence flow in the Change Contract template on 2026-08-24.

### Goal

Require the Project Manager to receive Quality verification evidence directly from Quality before presenting the outcome, and to receive the User validation decision directly from the User before recording it.

### Value

Closure decisions rely on first-hand evidence in the Project Manager's session rather than an actor's forwarded claim about another owner's decision.

### Scope

- Clarify direct provenance for Quality `proceed` evidence and User validation decisions in the canonical Change Contract template.
- Align the Change Contract and Project Manager requirements and verification criteria.
- Preserve direct `Quality -> User -> Project Manager Closure` responsibility flow.
- Preserve autonomous and unattended collaboration behavior.

### Observable Outcome

The Change Process and approved requirements state that Quality sends its verification judgment and evidence directly to the Project Manager, after which the Project Manager presents the verified outcome; the User then communicates the validation decision directly to the Project Manager, who records it before Closure.

## Artifact Applicability And Ownership

**Applicability:** Each artifact owner decides and updates its own row.<br>
**Status:** complete

| Artifact type | Included | Owner | Completion evidence | Status |
|---|---|---|---|---|
| Intent and outcome | yes | Syspilot Project Manager | Goal, value, scope, and observable outcome are explicit and approved | approved |
| Product specification and architecture decisions | yes | Syspilot Architect | Provenance semantics and affected requirements are approved; strict documentation checks pass | approved |
| User-facing documentation | yes | Syspilot Technical Writer | Impact on derived workflow guidance is assessed and applicable updates are reviewed | complete |
| Implementation and unit verification | yes | Syspilot Developer | Approved process and specification changes are realized and focused checks pass | complete |
| Acceptance test design and results | yes | Syspilot Tester | Evidence-source scenarios verify direct Quality and User provenance | passed |
| Quality review | yes | Syspilot Quality | Current verification judgment is `proceed` and no open quality issue remains | proceed |
| User validation and approval | yes | User | Observable outcome is accepted or changes are requested directly to the Project Manager | accepted |
| Closure decision | yes | Syspilot Project Manager | Final outcome, validation disposition, and integration state are recorded | complete |

## Product Specification And Architecture Decisions

**Owner:** Syspilot Architect<br>
**Status:** approved

### Decisions And Evidence

| Decision | Chosen approach | Relevant alternatives | Rationale and evidence |
|---|---|---|---|
| Evidence provenance | Quality communicates its `proceed` judgment and evidence directly to the Project Manager; the User communicates an applicable validation decision directly to the Project Manager; forwarded claims do not establish either owner's decision | Trust forwarded statements from another actor | Direct evidence preserves the authority of each decision owner and gives the Project Manager first-hand evidence before presentation, recording, and Closure |
| Responsibility flow | Preserve `Quality -> User -> Project Manager Closure`; direct communication to the Project Manager provides evidence but does not transfer User validation responsibility to the Project Manager | Route validation responsibility through the Project Manager | Separating evidence delivery from responsibility preserves the approved ownership model |
| Collaboration modes | Keep autonomous validation `not applicable` only under explicit delegated authority and keep unattended validation pending until the User returns | Infer validation from absence or forwarded statements | Existing approved semantics remain valid and must not be weakened by the provenance rule |
| Specification impact | Update `SYSP_REQ_CHANGE_CONTRACT`, `SYSP_VC_CHANGE_CONTRACT_1`, `SYSP_REQ_PROJECT_MANAGER`, and `SYSP_VC_PROJECT_MANAGER_1`; no User Story, Actor Model, or Contract Document Method change is required | Broaden the change to unrelated specification chains | The intent and ownership model are unchanged; only decision-source evidence becomes explicit |
| Documentation impact | `SYSP_DOC_CHANGE_WORKFLOW` includes both affected Requirements and therefore requires Technical Writer impact assessment | Assume no derived documentation impact | The incoming `included_in` relationship identifies the affected user guide |
| Architecture verification and handoff | Strict Sphinx/schema build passes with zero warnings; responsibility transfers to the Syspilot Developer to realize the approved process changes | Hand off before executable validation | The approved requirements and Contract form one validated state before implementation starts |

## User-Facing Documentation

**Owner:** Syspilot Technical Writer<br>
**Status:** complete

### Documentation Plan And Ownership

| Documentation surface | `doc` Need | Requirements included | Status |
|---|---|---|---|
| `docs/change-workflow.md` | `SYSP_DOC_CHANGE_WORKFLOW` | `SYSP_REQ_CHANGE_CONTRACT`, `SYSP_REQ_PROJECT_MANAGER` | verified |

### Changed Documentation And Verification

| Artifact | Change | Verification evidence |
|---|---|---|
| `docs/change-workflow.md` | Make direct Quality and User decision provenance explicit while preserving `Quality -> User -> Project Manager Closure`, autonomous `not applicable`, and unattended `pending` | Four focused tests passed; clean strict Sphinx/schema build passed with zero warnings; direct provenance wording reviewed against the realized Change Process and Project Manager role |

## Implementation And Unit Verification

**Owner:** Syspilot Developer<br>
**Status:** complete

### Decisions And Evidence

| Decision | Chosen approach | Relevant alternatives | Rationale and evidence |
|---|---|---|---|
| Realize direct provenance without changing validation ownership | Require direct Quality and User communication to the Project Manager while responsibility still flows `Quality -> User -> Project Manager Closure` | Transfer validation responsibility through the Project Manager | Direct evidence establishes decision provenance; explicit process and role wording preserves User-owned validation and PM-only closure responsibility |

### Changed Artifacts And Verification

| Artifact | Change | Verification evidence |
|---|---|---|
| `docs/Syspilot Processes/change.md` | Require direct Quality evidence and direct User decisions; reject forwarded claims; preserve autonomous and unattended handling | Four focused docs-build tests passed; clean strict Sphinx/schema build passed with zero warnings |
| `docs/Syspilot Actors/Syspilot Project Manager.md` | Add presentation, direct evidence reception, recording, and closure boundaries | Clean strict Sphinx/schema build passed with zero warnings |

## Acceptance Testing

**Owner:** Syspilot Tester<br>
**Status:** passed

| Scenario | Traces to | Result | Evidence |
|---|---|---|---|
| Project Manager treats Quality readiness as established only from Quality's direct judgment and evidence | observable outcome | pass | The canonical Change Process requires direct Quality-to-Project-Manager evidence before presentation and explicitly rejects an identical claim forwarded by another actor; the Project Manager requirement and role card preserve the same source boundary |
| Project Manager records User validation only from the User's direct decision | observable outcome | pass | The canonical Change Process requires the User's direct decision before recording and explicitly rejects an identical claim forwarded by another actor; the Project Manager requirement, role card, and user workflow preserve User-owned responsibility until that direct decision is recorded |

These scenarios validate the documented process boundary. Runtime sender authentication or automated enforcement by Jarvis is outside this Change's scope.

## Quality Review

**Owner:** Syspilot Quality<br>
**Status:** proceed

**Current judgment:** Proceed. The approved requirements, canonical Change Process, Project Manager role, and user workflow consistently require direct Quality and User decision provenance while preserving User-owned validation and `Quality -> User -> Project Manager Closure` responsibility. The boundary is explicitly normative and does not claim Jarvis sender authentication or automated enforcement. The strict documentation build and schema validation pass without warnings, all four focused tests pass, and both acceptance scenarios support the approved outcome.

### Open Quality Issues

None.

## User Validation And Approval

**Owner:** User<br>
**Recorded by:** Syspilot Project Manager<br>
**Status:** accepted

**Decision and evidence:** The User directly selected `Accepted` in the Syspilot Project Manager session on 2026-08-24 after the Project Manager presented Quality's direct `proceed` evidence and the realized observable outcome. Responsibility then transferred to the Syspilot Project Manager for Closure.

## Closure

**Owner:** Syspilot Project Manager<br>
**Status:** closed

- [x] Every included artifact has terminal status and completion evidence.
- [x] Intent and outcome are `approved`.
- [x] Quality has recorded a `proceed` judgment.
- [x] Open Quality Issues contains `None`.
- [x] User validation is `accepted`, or its `not applicable` status and autonomous authority are recorded.
- [x] Current blocker is `none`.
- [x] The observable outcome is demonstrated.
- [x] Integration into `development` has been completed by the Syspilot Project Manager through the resulting squash integration commit.

**Final outcome:** The User directly accepted the demonstrated validation-provenance outcome after Quality directly supplied its `proceed` evidence to the Syspilot Project Manager. The Change now requires first-hand Quality verification evidence and first-hand User validation decisions before PM recording and Closure, while preserving `Quality -> User -> Project Manager Closure`, autonomous authority, and unattended pending behavior. The Syspilot Project Manager closed the Change and integrated `feature/validation-provenance` into `development` by squash.