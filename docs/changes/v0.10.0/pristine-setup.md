# Change Contract: Pristine Setup

**Status:** closed<br>
**Process owner:** Syspilot Project Manager<br>
**Current responsibility:** Syspilot Project Manager<br>
**Current blocker:** none<br>
**Created:** 2026-08-24<br>
**Branch:** feature/pristine-setup<br>
**Collaboration mode:** User-guided for setup architecture, project lifecycle policy, and validation; otherwise autonomous within the approved intent.

## Intent And Outcome

**Owner:** Syspilot Project Manager<br>
**Status:** approved<br>
**Approval evidence:** User approved starting Pristine Setup with direct Architect elaboration on 2026-08-24 and directed unresolved scope or process questions to the Syspilot Project Manager.

### Goal

Define and realize the release-bound process, Contract, and product interfaces for reproducible pristine Syspilot v2 setup in a new customer project. Runtime execution and verification in an isolated Jarvis or VS Code Extension Host environment remain required follow-up coverage before claiming an operationally proven installation.

### Value

A new project receives one explicit, checkable setup definition for adopting a known Syspilot release without relying on repository-development instructions, hidden local state, or an already-installed Change Process. The design pins that approved tool baseline for the project lifetime and exposes the remaining runtime-validation risk instead of implying tested installation behavior.

### Scope

- Define the bootstrap boundary before Syspilot exists in the target project.
- Define setup as a dedicated Contract capability executed by the initiating Copilot session without a persistent Setup actor.
- Define the Contract-owned authoritative installation inventory.
- Define supported target-environment prerequisites, installation actions, verification evidence, blockers, and handoff to the Project Manager.
- Pin an approved Syspilot version or commit in each project installation.
- Establish that updating Syspilot is not the normal or generally recommended project operating mode.
- Require any later Syspilot update to be authorized by a separate project-specific Change with impact analysis, revalidation, and an assigned technical executor.
- Keep the Jarvis extension lifecycle and compatibility policy outside Syspilot project-update policy and outside this Change.
- Replace current preview-only installation guidance with accurate supported guidance when implementation evidence exists.

### Out Of Scope

- Automated v1-to-v2 migration.
- A general rolling-update mechanism for customer projects.
- Jarvis extension installation, update policy, or implementation.
- Release 0.10.0 packaging and publication beyond defining the setup-facing inputs that Release must later provide.

### Observable Outcome

The product contains a release-bound, checkable Setup Contract and minimal external bootstrap interface that define how a selected Syspilot v2 release is installed into a project with no confirmed Syspilot installation. The approved capability specifies the pinned baseline, required product and project-instance artifacts, mandatory verification gates, actionable blockers, Git integration, and Project Manager handoff. Process review demonstrates these semantics without claiming that installation, actor discovery, target build, baseline readback, Git integration, or handoff has run successfully; a follow-up Change must provide an isolated Jarvis or VS Code Extension Host environment and execute that deferred runtime acceptance.

## Artifact Applicability And Ownership

**Applicability:** Each artifact owner decides and updates its own row.<br>
**Status:** complete

| Artifact type | Included | Owner | Completion evidence | Status |
|---|---|---|---|---|
| Intent and outcome | yes | Syspilot Project Manager | Goal, value, scope, boundaries, and observable outcome are explicit and approved | approved |
| Product specification and architecture decisions | yes | Syspilot Architect | Setup lifecycle, Contract inventory, pinning, ownership boundaries, and verification are approved and traced | complete |
| User-facing documentation | yes | Syspilot Technical Writer | Supported pristine setup and project-lifecycle guidance is accurate, reviewed, and builds cleanly | complete |
| Implementation and unit verification | yes | Syspilot Developer | Approved Setup process and registry integration are realized; strict build and focused tests pass | complete |
| Acceptance test design and results | yes | Syspilot Tester | Bootstrap-phase process review passes; runtime installation acceptance is explicitly deferred until an isolated Jarvis or Extension Host test environment exists | passed |
| Quality review | yes | Syspilot Quality | Current verification judgment is `proceed` and no open quality issue remains | proceed |
| User validation and approval | yes | User | Supported pristine setup outcome is accepted or changes are requested directly to the Project Manager | accepted |
| Closure decision | yes | Syspilot Project Manager | Final outcome, validation disposition, and integration state are recorded | complete |

## Product Specification And Architecture Decisions

**Owner:** Syspilot Architect<br>
**Status:** complete

### Decisions And Evidence

| Decision | Chosen approach | Relevant alternatives | Rationale and evidence |
|---|---|---|---|
| Bootstrap entry point | README prompt loads the selected release's Setup Contract, materializes it locally, and executes it; all subsequent behavior belongs to the Contract | Bootstrap prompt contains installation behavior or creates a Setup actor | A minimal stable prompt delegates version-specific behavior to the release-bound Contract |
| Setup execution | The initiating Copilot session executes the Setup Contract as a temporary Contract executor; no persistent Setup actor is installed | Retain a ninth base actor for setup and updates | Setup needs reproducible procedure and evidence, not durable memory or a standing perspective |
| Bootstrap-supplied release integrity | Setup receives the exact SemVer tag and materialized Contract from the bootstrap prompt, verifies the corresponding full commit identity, and uses that commit tree as authority without selecting or resolving another version | Duplicate release selection inside Setup or trust a tag without its commit identity | Release selection belongs to bootstrap while Setup records and verifies the reproducible baseline it was given |
| Artifact ownership classes | Separate immutable release-owned product artifacts, generated project-instance artifacts, and protected user-owned configuration | Treat every installed file as equally replaceable | Updates and local tailoring require explicit overwrite boundaries |
| Existing project state | Require `.syspilot/setup-contract.md` to be the only working-tree change before the dedicated User-approved Setup branch; preserve committed project work and ask the User to classify possible prior Syspilot artifacts that do not establish a confirmed baseline | Require an empty repository or abort on every Syspilot-like artifact | Pristine describes the Syspilot installation state, while the recorded Contract-only change provides the reliable setup and cleanup boundary |
| Existing documentation infrastructure | Inspect and preserve an existing Sphinx-Needs installation, ontology, and documentation structure; use User-guided additive integration instead of overwrite or automatic collision failure | Replace existing documentation or require one fixed Sphinx-Needs realization | Supported versions and ontology realizations vary, but the required observable build and schema outcome remains testable |
| Project baseline | Record the bootstrap-supplied release tag, commit, and approved baseline in versioned `.syspilot/project.toml` for the project lifetime | Store `latest` or rely only on historical Setup Contract text | A visible immutable pin supports verification and later impact analysis |
| Current Change tailoring | Complete the release-bound Setup capability and its reviewed semantics without claiming operational runtime proof; require a follow-up Change to execute the deferred Jarvis or VS Code Extension Host scenarios | Keep the original end-to-end installation outcome despite unavailable runtime evidence, or block all process-definition progress | The User accepted the early-bootstrap competence gap; Tester passed the process and blocker semantics while explicitly recording the unexecuted runtime surface |
| Actor installation and discovery | Generate exactly eight persistent Syspilot actors, exclude Setup, verify all eight are included in `jarvis_listActors`, and verify Setup opened no actor sessions; unrelated existing actors remain valid | Require Jarvis to contain globally exactly eight actors or start every actor session | Setup must verify its own installation outcome without constraining unrelated project actors or creating unnecessary sessions |
| Successful handoff | Complete all mandatory inventory, integrity, structure, actor/Jarvis, baseline, and zero-warning target-build gates; then obtain User guidance for commit and merge, complete Git integration, and only afterward message the Project Manager `Installation complete, welcome to this project` | Hand off before merge or request a second message-release approval after Git completion | Normal project work must start from an integrated, verified baseline and the sequence must be unambiguous to a generic executor |
| Later updates | A separate project-specific Change records old/new baselines, impact analysis, revalidation, authorization, and its technical executor before update work | A standing Setup actor or routine rolling updater independently decides or performs updates | Updates alter project process and product artifacts and therefore require project governance |
| External interface | Jarvis Syspilot may automate this interface but must invoke the release-bound Setup Contract and must not require a persistent Setup actor | Encode a second installation lifecycle in the extension | The Contract remains the single normative setup behavior across manual and automated entry points |

### Impact Scope

| Surface | Required disposition | Rationale |
|---|---|---|
| `SYSP_US_SETUP`, `SYSP_AC_SETUP_1`, `SYSP_REQ_SETUP`, `SYSP_VC_SETUP_1` | Redefine Setup from an actor role to the Pristine Setup Contract capability while retaining IDs and existing documentation impact links | The user intent remains setup; only its realization and ownership model change |
| `docs/Syspilot Processes/setup.md` | Add the canonical release-bound Setup Contract and executable process definition | All behavior after bootstrap belongs to one versioned normative document |
| External README bootstrap prompt | Add the three-step interface: load, materialize, execute the selected release's Setup Contract | Bootstrap remains minimal and delegates release-specific behavior |
| `docs/Syspilot Actors/Syspilot Setup.md` and actor roster/navigation | Remove the Setup role card and roster entry; update the base-role count from nine to eight | Setup no longer needs durable memory, authority, or a standing perspective |
| Installed `.jarvis/actors/Syspilot Setup/` entity | Remove through the authorized realization/update path, not by another actor editing its memory | Actor-memory ownership remains respected while the product ceases to install the entity |
| `.github/prompts/syspilot.setup.prompt.md` and installed Setup-agent references | Remove or replace with the contract-bootstrap interface; retain no prompt that targets a persistent Setup actor | Installed instance must match the product model |
| `.github/copilot-instructions.md` | Replace the statement that a Setup Agent installs product assets with the Setup Contract boundary | Active repository instructions currently encode the removed actor model |
| `README.md`, `docs/index.rst`, `docs/product-model.md`, `docs/getting-started.md`, `docs/operations.md` | Replace Setup-actor ownership and nine-role wording with the Contract executor, eight base roles, supported bootstrap, pin, and update policy | These are active user-facing consumers of `SYSP_REQ_SETUP` |
| `SYSP_DOC_README`, `SYSP_DOC_GETTING_STARTED`, `SYSP_DOC_PRODUCT_MODEL`, `SYSP_DOC_CUSTOMIZATION`, `SYSP_DOC_OPERATIONS` | Keep their `includes: SYSP_REQ_SETUP` links and perform Technical Writer impact review | The same Requirement now describes the setup capability those documents contain |
| `docs/Syspilot Processes/index.md` and specification/process navigation | Register the Setup Contract as a process while retaining Setup US/REQ navigation as a capability | Setup moves from the actor registry to the process registry |
| Release-facing inputs | Define that Release provides a tag resolving to an immutable commit tree containing the bootstrap prompt and canonical Setup Contract; defer release packaging/publication implementation | Pristine Setup needs an authoritative source without expanding this Change into a release |
| `.syspilot/project.toml` | Define a versioned project-instance pin for resolved tag, commit, and approved baseline | The installed project requires durable reproducibility evidence |
| `enthali.jarvis-syspilot` | External follow-up: invoke the same three-step bootstrap/Setup Contract interface and remove any dependency on a persistent Setup actor | This repository defines the integration contract but does not implement the external extension |
| Historical v1 Change Documents and release notes | Retain unchanged as historical evidence | Past references to `@syspilot.setup` describe released behavior rather than current authority |

### Specification Impact Assessment

- `SYSP_REQ_ACTOR_MODEL` does not require a change: it continues to govern the remaining persistent actors; Setup no longer specializes it.
- `SYSP_REQ_CONTRACT_DOCUMENTS` remains applicable and is the parent of `SYSP_REQ_SETUP`; its generic Contract semantics already cover the new capability.
- `SYSP_REQ_PROJECT_MANAGER` does not require a role change: receiving a verified Setup completion and beginning normal project work fits existing intake and portfolio authority.
- `SYSP_REQ_DEVELOPER` does not require a role change: a later project-specific Change may assign technical update execution through its artifact table.
- `SYSP_REQ_RELEASE` is broad enough to own later packaging and delivery; this Change defines its required setup-facing tag/commit/Contract inputs but does not implement a release.
- The Setup Requirement and verification criterion enumerate the observable gates while leaving version-dependent Sphinx-Needs discovery and additive integration to the executable Contract and User guidance.

### Specification Verification

| Check | Result |
|---|---|
| Setup US/AC and REQ/VC align on the bootstrap-supplied exact release, clean dedicated branch, preserved project state, eight-actor outcome, explicit verification, Git integration, and PM handoff | pass |
| `SYSP_REQ_SETUP` specializes `SYSP_REQ_CONTRACT_DOCUMENTS` and remains realized by `docs/Syspilot Processes/setup.md` | pass |
| Active documentation impact remains traced through the five incoming `doc` Needs listed above | pass |
| Strict Sphinx/schema build and focused documentation tests | pass: `python docs/docs-build.py clean` completed with zero warnings; `python docs/test_docs_build.py -v` passed all four tests; `git diff --check` passed |

## User-Facing Documentation

**Owner:** Syspilot Technical Writer<br>
**Status:** complete

### Documentation Plan And Ownership

| Documentation surface | `doc` Need | Change | Status |
|---|---|---|---|
| `README.md` | `SYSP_DOC_README` | Replace nine-role and future-bootstrap wording with the eight-actor release-bound Setup boundary | verified |
| `docs/getting-started.md` | `SYSP_DOC_GETTING_STARTED` | Explain the load/materialize/execute interface, pinned baseline, and deferred runtime proof | verified |
| `docs/product-model.md` | `SYSP_DOC_PRODUCT_MODEL` | Remove Setup from the persistent actor roster and explain temporary Contract execution | verified |
| `docs/customization.md` | `SYSP_DOC_CUSTOMIZATION` | Align the base roster count with eight persistent actors | verified |
| `docs/operations.md` | `SYSP_DOC_OPERATIONS` | Explain pristine installation, pinning, Change-controlled updates, and the runtime evidence boundary | verified |

### Changed Documentation And Verification

| Artifact | Change | Verification evidence |
|---|---|---|
| Five traced user-guide surfaces | Align active guidance with `SYSP_REQ_SETUP` while distinguishing defined capability from operational runtime proof | Four focused tests passed; clean strict Sphinx/schema build passed with zero warnings after correcting one local guide link; targeted stale-wording scan contains only intentional no-Setup-actor boundaries |

## Implementation And Unit Verification

**Owner:** Syspilot Developer<br>
**Status:** complete

### Realized Artifacts

- `docs/Syspilot Processes/setup.md` defines the executable pristine Setup Contract aligned with `SYSP_REQ_SETUP` and `SYSP_VC_SETUP_1`.
- `docs/Syspilot Processes/index.md` registers the Setup process.
- `docs/Syspilot Actors/index.md` and `docs/index.rst` expose exactly the eight persistent actors; the obsolete `docs/Syspilot Actors/Syspilot Setup.md` role card is removed.

### Verification

| Check | Result |
|---|---|
| `python docs/docs-build.py clean` | pass: zero Sphinx and schema warnings |
| `python docs/test_docs_build.py -v` | pass: four tests |
| `git diff --check` | pass |
| Active actor-surface scan | pass: no ninth-actor wording, Setup role-card link, or Setup actor toctree entry remains in README, active top-level docs, actor cards, or `.github` surfaces |

## Acceptance Testing

**Owner:** Syspilot Tester<br>
**Status:** passed

| Scenario | Traces to | Result | Evidence |
|---|---|---|---|
| A project with no confirmed Syspilot installation receives a pinned, verified Syspilot v2 installation through the Setup Contract | observable outcome, `SYSP_AC_SETUP_1` | not executed yet | End-to-end execution requires a tagged v2 release plus an isolated Jarvis or VS Code Extension Host target environment; neither test capability exists in this early bootstrap phase |
| An unmet prerequisite stops setup with an actionable blocker and no false success state | `SYSP_AC_SETUP_1`, `SYSP_REQ_SETUP` | pass | The missing release-bound input prevents target writes; the Setup Contract requires an actionable blocker and prohibits `verified`, success messaging, and Project Manager handoff while any mandatory gate remains open |
| A proposed later Syspilot update cannot proceed as routine Setup work without a project-specific Change | project lifecycle policy, `SYSP_REQ_SETUP` | pass | The Setup Contract and requirement permit a later update only through a separate project-specific Change containing old and proposed baselines, impact analysis, revalidation scope, authorization, and an assigned technical executor |

The Setup process, inventory, mandatory gates, blocker semantics, actor boundaries, Git sequencing, and update policy passed review. Installation, actor discovery, session behavior, target build, baseline readback, Git integration, and Project Manager handoff remain unexecuted until a dedicated test environment is available; review evidence does not claim those runtime outcomes.

**Bootstrap risk acceptance:** On 2026-08-25 the User accepted this temporary runtime-validation gap for the early bootstrap release and directed that it not block the Change. A follow-up Change shall provide the isolated Jarvis or Extension Host test environment and execute the deferred scenarios.

## Quality Review

**Owner:** Syspilot Quality<br>
**Status:** proceed

**Current judgment:** Proceed. Commit `0e02c73` removed the obsolete role card, registry entry, and navigation; the strict build and schema validation pass without warnings, all four focused tests pass, and active product sources consistently describe eight persistent actors. The Setup owner removed `.jarvis/actors/Syspilot Setup/` in the installed instance, and post-reload `jarvis_listActors` returns exactly the eight expected persistent Syspilot actors without Setup. `jarvis_listChatSessions` retains the historical Setup Engineer chat title, but no Setup actor entity backs it; the approved Requirement prohibits Setup from opening actor sessions during the deferred installation scenario, not retention of pre-Change chat history. Deferred runtime acceptance remains explicitly bounded and User-accepted.

### Open Quality Issues

None.

## User Validation And Approval

**Owner:** User<br>
**Recorded by:** Syspilot Project Manager<br>
**Status:** accepted

**Decision and evidence:** The User directly selected `Accepted` in the Syspilot Project Manager session on 2026-08-25 after presentation of Quality's direct `proceed` evidence and the explicitly runtime-bounded observable outcome. The accepted result includes the release-bound Setup capability and retirement of the persistent Setup actor; isolated Jarvis or VS Code Extension Host runtime acceptance remains a required follow-up Change and is not claimed as passed here. Responsibility then transferred to the Syspilot Project Manager for Closure.

## Closure

**Owner:** Syspilot Project Manager<br>
**Status:** closed

- [x] Every included artifact has terminal status and completion evidence.
- [x] Intent and outcome are `approved`.
- [x] Quality has recorded a `proceed` judgment directly to the Syspilot Project Manager.
- [x] Open Quality Issues contains `None`.
- [x] User validation is `accepted`, or its `not applicable` status and autonomous authority are recorded.
- [x] Current blocker is `none`.
- [x] The bounded observable outcome is demonstrated without claiming deferred runtime acceptance.
- [x] Integration into `development` has been completed by the Syspilot Project Manager through the resulting squash integration commit.

**Final outcome:** The User accepted the release-bound Pristine Setup capability, project pinning and update policy, eight-actor product model, persistent Setup actor retirement, and the explicit boundary between reviewed process semantics and operational runtime proof. Quality directly recorded `proceed` in `b31c447` with no open issues. The Syspilot Project Manager closed the Change and integrated `feature/pristine-setup` into `development` by squash. A follow-up Change must provide an isolated Jarvis or VS Code Extension Host environment and execute installation, actor discovery and session behavior, target build, baseline readback, Git integration, and Project Manager handoff before those runtime outcomes may be claimed as passed.