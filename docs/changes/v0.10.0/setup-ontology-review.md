# Change Contract: Setup Ontology Review

**Status:** closed<br>
**Process owner:** Syspilot Project Manager<br>
**Current responsibility:** Syspilot Project Manager<br>
**Current blocker:** none<br>
**Created:** 2026-08-26<br>
**Branch:** feature/setup-ontology-review<br>
**Collaboration mode:** Autonomous. The User explicitly authorized autonomous execution on 2026-08-26 after agreeing the bounded behavior; User validation is not applicable when the observable outcome is demonstrated without adding a new Skill or Contract type.

## Intent And Outcome

**Owner:** Syspilot Project Manager<br>
**Status:** approved<br>
**Approval evidence:** The User directly approved autonomous execution of `setup-ontology-review` on 2026-08-26. The agreed behavior is that Setup preserves or installs the ontology, then the Project Manager explains the selected ontology and asks whether it fits; only a requested change starts a normal Change using the existing Ontology skill.

### Goal

Make the first Project Manager interaction after successful Setup explicitly review the selected project ontology with the User and route any requested ontology adjustment through the normal Change process.

### Value

A new project confirms that its traceability model fits before ordinary work begins, without inventing an unapproved ontology, a new Skill, or a special ontology Contract.

### Scope

- Clarify the Setup Contract handoff so it identifies the selected ontology, instructs the Project Manager to explain its artifact types, statuses, and relationships, and asks the User whether it fits the project.
- Define the two outcomes: acceptance permits normal project intake; requested adjustment starts a normal Change before ontology modification.
- Use the existing `syspilot.ontology` skill only as technical guidance inside an applicable Change.
- Align the Setup Requirement and Verification Criterion with this post-Setup review.
- Assess and update user-facing setup/customization guidance and documentation traceability where applicable.
- Do not add a Skill, a Contract type, a persistent Setup actor, or an ontology designed before User agreement.
- Do not modify the unrelated untracked `.github/agents/syspilot.setup.agent.md` v1 artifact.

### Observable Outcome

A reader can determine from the Setup Contract, Requirement, and applicable user guidance that successful Setup hands the selected ontology to the Project Manager for explanation and an explicit User fit decision; acceptance continues normal intake, while requested changes use the ordinary Change process and existing Ontology skill.

## Artifact Applicability And Ownership

**Applicability:** Each artifact owner decides and updates its own row.<br>
**Status:** complete

| Artifact type | Included | Owner | Completion evidence | Status |
|---|---|---|---|---|
| Intent and outcome | yes | Syspilot Project Manager | Goal, boundaries, authority, and observable outcome are explicit | approved |
| Product specification and architecture decisions | yes | Syspilot Architect | Setup Requirement/process boundary and affected traceability are coherent | complete |
| User-facing documentation | yes | Syspilot Technical Writer | Applicable setup/customization guidance and `doc` Needs are current | complete |
| Implementation and unit verification | yes | Syspilot Developer | Phase 7 identifies the selected ontology, requires the PM explanation and User fit decision, and routes adjustment through a normal Change; focused checks pass | complete |
| Acceptance test design and results | yes | Syspilot Tester | Black-box scenarios cover ontology acceptance and requested-change routing | passed |
| Quality review | yes | Syspilot Quality | Independent review confirmed coherent decision routing, bounded product scope, traceability, and passing validation; judgment is `proceed` | proceed |
| User validation and approval | not applicable: User explicitly delegated autonomous closure for this bounded outcome on 2026-08-26 | User | Closure records that User validation did not occur | not applicable |
| Closure decision | yes | Syspilot Project Manager | Outcome, validation disposition, and integration are recorded | complete |

## Architecture And Specification

**Owner:** Syspilot Architect<br>
**Status:** complete

### Affected Artifacts

| Artifact | Change | Rationale |
|---|---|---|
| `SYSP_REQ_SETUP`, `SYSP_VC_SETUP_1` | modify | Make the existing PM handoff and ontology-fit decision explicit |
| `docs/Syspilot Processes/setup.md` | modify | Realize the post-Setup review without a new process type |
| `README.md`, `docs/getting-started.md`, `docs/product-model.md`, `docs/customization.md`, `docs/operations.md` and their `doc` Needs | Technical Writer impact review | Incoming `included_in` links identify all current user-facing consumers of `SYSP_REQ_SETUP` |

### Decisions And Evidence

| Decision or check | Evidence |
|---|---|
| No new Skill or Contract type | The existing Ontology skill owns technical schema guidance; the normal Change process governs any requested edit |
| Setup boundary | Setup detects, preserves or installs, validates, and identifies the selected ontology; it does not evaluate fit or modify the ontology |
| First PM interaction | The successful handoff requires the Project Manager to explain the selected ontology's artifact types, statuses, and relationships and ask whether it fits |
| Accepted outcome | User acceptance continues normal project intake without creating an ontology Change |
| Adjustment outcome | A User-requested adjustment requires a normal Change before modification; `syspilot.ontology` supplies technical guidance only inside that Change |
| PM specification impact | `SYSP_REQ_PROJECT_MANAGER` already owns intake, outcome-oriented work with the User, and applicable user-decision artifacts; no duplicate PM Requirement is needed |
| Pre-edit impact analysis | Incoming traversal from `SYSP_REQ_SETUP` returned `SYSP_VC_SETUP_1`, `SYSP_DOC_README`, `SYSP_DOC_GETTING_STARTED`, `SYSP_DOC_PRODUCT_MODEL`, `SYSP_DOC_CUSTOMIZATION`, and `SYSP_DOC_OPERATIONS` |
| Specification validation | `python docs/docs-build.py clean` passed with zero warnings; `python docs/test_docs_build.py -v` passed 4/4; `git diff --check` passed; editor diagnostics found no errors |

## User-Facing Documentation

**Owner:** Syspilot Technical Writer<br>
**Status:** complete

### Documentation Plan And Ownership

| Documentation surface | `doc` Need | Requirements included | Status |
|---|---|---|---|
| `README.md` | `SYSP_DOC_README` | `SYSP_REQ_SETUP` | verified |
| `docs/getting-started.md` | `SYSP_DOC_GETTING_STARTED` | `SYSP_REQ_SETUP` | verified |
| `docs/product-model.md` | `SYSP_DOC_PRODUCT_MODEL` | `SYSP_REQ_SETUP` | verified |
| `docs/customization.md` | `SYSP_DOC_CUSTOMIZATION` | `SYSP_REQ_SETUP`, `SYSP_REQ_ONTOLOGY_SCHEMA`, `SYSP_REQ_ONTOLOGY_EDITING` | verified |
| `docs/operations.md` | `SYSP_DOC_OPERATIONS` | `SYSP_REQ_SETUP` | verified |

### Consultations And Factual Reviews

| Documentation surface | Consulted artifact owner | Review question | Evidence and disposition |
|---|---|---|---|
| Setup and ontology user guidance | Not requested; the completed Architecture decisions and Developer handoff are explicit | Does the guidance preserve Setup, PM, User, and Ontology-skill authority boundaries? | Confirmed against the Contract and implemented Phase 7: Setup selects and validates but does not evaluate or redesign; the Project Manager explains and asks; the User decides; a requested adjustment uses a normal Change; the Ontology skill remains technical guidance |

### Changed Documentation And Verification

| Artifact | Change | Verification evidence |
|---|---|---|
| Five Setup-consuming user guides and their `doc` Needs | Explain the selected-ontology handoff, explicit fit decision, accepted intake path, and Change-controlled adjustment path at each existing Setup or ontology boundary | `python docs/docs-build.py clean` passed with zero Sphinx/schema warnings; `python docs/test_docs_build.py -v` passed 4/4; `git diff --check`, targeted stale-wording scan, and editor diagnostics passed |

## Implementation And Unit Verification

**Owner:** Syspilot Developer<br>
**Status:** complete

### Decisions And Evidence

| Decision | Chosen approach | Relevant alternatives | Rationale and evidence |
|---|---|---|---|
| Setup handoff payload | Include the selected ontology and configured path, then instruct the Project Manager to explain artifact types, statuses, and relationships and ask whether it fits | Let Setup evaluate fit or leave the post-Setup review implicit | Setup owns detection and validation; the Project Manager owns the first User interaction after successful handoff |
| User decision routing | Acceptance continues normal intake without an ontology Change; an adjustment request starts a normal Change before modification, using `syspilot.ontology` only as technical guidance | Create a special Contract or modify the ontology during Setup | The ordinary Change process preserves User agreement and Contract authority without adding a Skill, Contract type, or persistent Setup actor |

### Changed Artifacts And Verification

| Artifact | Change | Verification evidence |
|---|---|---|
| `docs/Syspilot Processes/setup.md` Phase 7 | Replaced the ambiguous evaluate/propose instruction with the selected ontology identity, explicit PM explanation and fit question, and deterministic acceptance/adjustment outcomes | Strict documentation/schema build and focused docs tests pass; scoped wording scan confirms all required handoff elements and no new process artifact |

## Acceptance Testing

**Owner:** Syspilot Tester<br>
**Status:** passed

| Scenario | Traces to | Result | Evidence |
|---|---|---|---|
| User accepts the selected ontology and normal project intake continues without an ontology Change | observable outcome, `SYSP_REQ_SETUP` | pass | A whitespace-normalized decision-routing oracle confirmed that Setup Phase 7 and the Requirement explicitly route acceptance to normal intake without an ontology Change; all five reviewed user guides present acceptance as the normal-intake branch after the PM explains the selected ontology and asks for fit |
| User requests an ontology adjustment and PM starts a normal Change before modification | observable outcome, `SYSP_REQ_SETUP` | pass | The same independent oracle confirmed process, Requirement, and all five guides order the adjustment path as User request, normal Change, then ontology modification; Phase 7 restricts the existing `syspilot.ontology` skill to technical guidance inside that Change |
| No new Skill, Contract type, or pre-approved ontology design is introduced | scope boundary | pass | The exact Contract range from `6537f8c` added no Skill, process/Contract type, or ontology file; the process registry still contains only Contract Documents, Change, and Setup, and the installable tree still contains only the existing Impact and Ontology skills |

## Quality Review

**Owner:** Syspilot Quality<br>
**Status:** complete

**Current judgment:** proceed

Setup Phase 7, `SYSP_REQ_SETUP`, `SYSP_VC_SETUP_1`, and all five Setup-consuming user guides consistently identify the selected ontology, assign explanation and the fit question to the Project Manager, continue normal intake without an ontology Change after acceptance, and require a normal Change before any requested modification. The exact Contract range from merge base `6537f8c` adds no Skill, process or Contract type, or ontology file; the installable Skill tree remains limited to the existing Impact and Ontology skills.

Independent validation passed `python docs/docs-build.py clean` with zero warnings, `python docs/test_docs_build.py -v` with 4/4 tests, `git diff --check`, editor diagnostics, and a fresh `needs.json` assertion that `SYSP_VC_SETUP_1` verifies `SYSP_REQ_SETUP` and the five expected `doc` Needs include it. The unrelated untracked `.github/agents/` path was not modified.

### Open Quality Issues

None.

## User Validation And Approval

**Owner:** User<br>
**Recorded by:** Syspilot Project Manager<br>
**Status:** not applicable

**Decision and evidence:** The User explicitly authorized autonomous execution and closure for this bounded Change on 2026-08-26. User validation will not occur during autonomous execution and must not be claimed.

## Closure

**Owner:** Syspilot Project Manager<br>
**Status:** closed

- [x] Every included artifact has terminal status and completion evidence.
- [x] Intent and outcome are `approved`.
- [x] Quality has recorded a `proceed` judgment.
- [x] Open Quality Issues contains `None`.
- [x] User validation is `not applicable` and autonomous authority is recorded.
- [x] Current blocker is `none`.
- [x] The observable outcome is demonstrated.
- [x] Integration into `development` has been completed by the Syspilot Project Manager through the resulting squash integration commit.

**Final outcome:** Under the User's autonomous authority, successful Setup now identifies the selected ontology and hands it to the Project Manager for explanation and an explicit User fit decision. Acceptance continues normal project intake without an ontology Change; a requested adjustment starts a normal Change before modification and uses the existing Ontology skill only as technical guidance. No new Skill, Contract type, persistent Setup actor, or ontology design was introduced. Quality recorded direct `proceed` evidence in `a182ba0`; User validation did not occur and is correctly not applicable. The Syspilot Project Manager closed the Change and integrated `feature/setup-ontology-review` into `development` by squash.
