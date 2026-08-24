# Change Contract: Documentation Foundation

**Status:** closed<br>
**Process owner:** Syspilot Project Manager<br>
**Current responsibility:** Syspilot Project Manager<br>
**Current blocker:** none<br>
**Created:** 2026-08-24<br>
**Branch:** feature/documentation-foundation<br>
**Collaboration mode:** User-guided for intent, documentation ownership, actor boundaries, and closure; otherwise autonomous within the approved intent.

## Intent And Outcome

**Owner:** Syspilot Project Manager<br>
**Status:** approved<br>
**Approval evidence:** User approved the intent, ownership direction, and start of the Change on 2026-08-24.

### Goal

Establish the Syspilot Technical Writer as the owner of user-facing product documentation and create a coherent documentation foundation for the established Syspilot product model.

### Value

Users can understand, adopt, and operate Syspilot from documentation that is organized around their needs, uses consistent terminology, and accurately reflects the product without requiring them to reconstruct behavior from specifications, actor internals, or historical v1 material.

### Scope

- Define the Syspilot Technical Writer role and its specification chain.
- Realize the approved Technical Writer role, registry entry, and Change Process integration as authoritative product artifacts.
- Add user-facing documentation as an explicit artifact type in the Change Process, owned by the Technical Writer when included.
- Determine which existing and future documentation files or sections the Technical Writer owns.
- Define the boundary between user-facing explanation and the authoritative artifacts owned by other actors.
- Allow the Technical Writer to consult any artifact owner directly through messages for factual clarification and to request review of whether derived documentation accurately and understandably represents that owner's artifact.
- Preserve each consulted actor's authority over its own artifact; consultation does not transfer Contract responsibility unless an explicit handoff occurs.
- Assign the Technical Writer ownership of the documentation ownership map and the user-facing documentation surface it defines.
- Inventory current documentation and establish a coherent user-oriented information architecture.
- Replace, retire, or clearly classify remaining active v1-oriented documentation within the agreed scope.

### Observable Outcome

The Technical Writer has an approved role and specification chain; the approved role and Change Process integration are realized as authoritative product artifacts; the Change Process includes an optional user-facing documentation artifact with explicit ownership and completion evidence; the Technical Writer has established and realized a reviewed documentation ownership map and coherent navigation; active user documentation consistently describes the established product model; factual owners have reviewed relevant derived explanations; and the strict documentation build passes without warnings.

## Artifact Applicability And Ownership

**Applicability:** Each artifact owner decides and updates its own row.<br>
**Status:** complete

| Artifact type | Included | Owner | Completion evidence | Status |
|---|---|---|---|---|
| Intent and outcome | yes | Syspilot Project Manager | Goal, value, scope, and observable outcome are explicit and approved | approved |
| Product specification and architecture decisions | yes | Syspilot Architect | User-approved Technical Writer US/REQ/AC/VC chain, documentation authority boundaries, changed Change Contract requirement, and clean strict Sphinx evidence | approved |
| User-facing documentation | yes | Syspilot Technical Writer | Agreed documentation surface is coherent, user-oriented, factually reviewed by relevant artifact owners, and builds cleanly | complete |
| Implementation and unit verification | yes | Syspilot Developer | Approved specifications are realized in authoritative product artifacts, regardless of file format or location, and relevant automated checks pass | complete |
| Acceptance test design and results | yes | Syspilot Tester | Representative users can navigate the documentation and correctly understand the intended product behavior | passed |
| Quality review | yes | Syspilot Quality | Revised documentation has a current verification judgment and no open quality issue remains | proceed |
| User validation and approval | yes | User | Observable outcome is accepted or changes are requested | accepted |
| Closure decision | yes | Syspilot Project Manager | Final outcome, validation disposition, and integration state are recorded | complete |

## Documentation Ownership Decisions

**Owner:** Syspilot Technical Writer<br>
**Status:** approved<br>
**Approval evidence:** User agreed the six independently maintained surfaces, project-lead audience, portal role, and relaxed technical writing style on 2026-08-24.

- The Technical Writer proposes and owns the documentation ownership map and the user-facing documentation surface it defines.
- The documentation ownership map is the collection of Technical Writer-owned `doc` Needs; each independently maintained user-facing surface has one `doc` Need with a `realized_by` path and `includes` links to the requirements it contains in user-oriented form.
- User-facing documentation remains free of Sphinx-Needs markup; traceability resides in the specification graph, and incoming `included_in` links expose documentation impact when requirements change.
- Ownership follows each artifact's purpose and declared process role rather than its file extension or location under `docs/`.
- Specifications, role cards, process definitions, schemas, and similar authoritative product sources are product artifacts rather than user-facing documentation, including when they are stored under `docs/` or written in Markdown or reStructuredText.
- The owner of an authoritative source artifact retains factual authority; the Technical Writer owns the derived user-facing explanation.
- Affected artifact owners review mapped boundaries and derived explanations for factual accuracy and understandability.
- The Architect checks that the ownership map remains consistent with the Actor Model, process ownership, and specification authority.
- The ownership map classifies each existing documentation surface as Technical Writer-owned, owned by another declared artifact owner, or historical material to retain or remove.

## Architecture And Specification

**Owner:** Syspilot Architect<br>
**Status:** approved

### Affected Artifacts

| Artifact | Change | Rationale |
|---|---|---|
| `docs/Syspilot Actors/` | add / modify | Define and register the Syspilot Technical Writer role |
| `docs/syspilot/` | add / modify | Add the Technical Writer specification chain and any changed process requirements |
| `.syspilot/ontology.toml` | modify | Add the `doc` type and `includes` / `included_in` traceability relationship |
| `docs/Syspilot Processes/change.md` | modify | Add user-facing documentation as an optional Change artifact |
| Documentation ownership map | add | Technical Writer defines concrete ownership; affected owners review factual boundaries; Architect checks model consistency |

### Decisions And Evidence

| Decision or check | Evidence |
|---|---|
| Technical Writer is a durable Syspilot actor rather than a temporary task role | User approved the role represented by `SYSP_US_TECHNICAL_WRITER` and `SYSP_REQ_TECHNICAL_WRITER` |
| Artifact purpose and authority determine ownership rather than path or format | User approved the boundary specified by `SYSP_REQ_TECHNICAL_WRITER` |
| Direct consultation does not imply Contract handoff or transfer factual authority | User approved the clarification and review boundary in `SYSP_REQ_TECHNICAL_WRITER` |
| Technical Writer owns the documentation ownership map and its user-facing documentation surface | User approved one Technical Writer-owned `doc` Need per independently maintained surface; the set of Doc Needs is the ownership map |
| Documentation traceability remains outside user-facing documents | Each `doc` Need uses `realized_by` for the document path and `includes` for REQ links; incoming `included_in` links expose reverse impact |
| User-facing documentation is an optional Change artifact owned by the Technical Writer | User approved the artifact and impact rules specified by `SYSP_REQ_CHANGE_CONTRACT` |
| Technical Writer traceability is structurally valid | Exported needs graph contains the approved US/AC/REQ/VC chain and the clean strict Sphinx build passes |
| Architecture approval and handoff | User approved the Doc Need architecture on 2026-08-24; current responsibility transferred to the Syspilot Developer |
| User-validation responsibility is consistent | `SYSP_REQ_PROJECT_MANAGER` assigns validation responsibility directly to the User while the Project Manager presents the outcome, records the decision, and receives responsibility only for Closure; strict build passes |

## User-Facing Documentation

**Owner:** Syspilot Technical Writer<br>
**Status:** complete

### Documentation Plan And Ownership

| Documentation surface | `doc` Need | Requirements included | Status |
|---|---|---|---|
| `README.md` | `SYSP_DOC_README` | `SYSP_REQ_ACTOR_MODEL`, `SYSP_REQ_SETUP` | verified |
| `docs/getting-started.md` | `SYSP_DOC_GETTING_STARTED` | `SYSP_REQ_ACTOR_MODEL`, `SYSP_REQ_SETUP`, `SYSP_REQ_CONTRACT_DOCUMENTS`, `SYSP_REQ_TECHNICAL_WRITER` | verified |
| `docs/product-model.md` | `SYSP_DOC_PRODUCT_MODEL` | Actor-role requirements and `SYSP_REQ_CONTRACT_DOCUMENTS` | verified |
| `docs/change-workflow.md` | `SYSP_DOC_CHANGE_WORKFLOW` | `SYSP_REQ_CHANGE_CONTRACT`, `SYSP_REQ_CONTRACT_DOCUMENTS`, and participating actor-role requirements | verified |
| `docs/customization.md` | `SYSP_DOC_CUSTOMIZATION` | `SYSP_REQ_ACTOR_MODEL`, `SYSP_REQ_SETUP`, `SYSP_REQ_CONTRACT_DOCUMENTS`, `SYSP_REQ_TECHNICAL_WRITER` | verified |
| `docs/operations.md` | `SYSP_DOC_OPERATIONS` | `SYSP_REQ_SETUP`, `SYSP_REQ_RELEASE` | verified |

Release-facing and historical user-readable surfaces remain outside the six-guide Technical Writer ownership map:

| Documentation surface | Ownership decision | Intended audience and outcome | Status |
|---|---|---|---|
| `docs/releasenotes.md` | Syspilot Release-owned release-facing user documentation; no Technical Writer `doc` Need | Users evaluating or adopting a release can understand delivered changes and compatibility | retained; Release review complete |
| `docs/experiences/` | Originating author or research source retains factual authority over observations; Technical Writer may own user-facing navigation and framing | Readers can use dated observations and hypotheses as evidence without mistaking them for specifications or current operating guidance | retained; Research review complete |

### Existing Documentation Inventory

| Existing surface | Classification and disposition |
|---|---|
| `docs/methodology.md`, `docs/architecture.md`, `docs/workflows.md` | Historical v1 guides retained temporarily while durable content is consolidated into the v2 user guides; then retire from active navigation |
| `docs/namingconventions.md` | Legacy and v2-review-required; retain temporarily outside active Reference navigation because it defines removed v1 structures |
| `docs/ontology-reference.md`, `docs/traceability/` | Generated specification reference; retain under Architect factual authority |
| `docs/releasenotes.md` | Release-facing documentation owned by Syspilot Release; outside the Technical Writer's six-guide ownership map |
| `docs/experiences/` | Retained experiential and historical evidence, not current product authority; reuse durable observations only after checking them against the current product model |
| `docs/Syspilot Actors/` | Authoritative role cards rather than derived user documentation; factual authority remains with the product model owners |
| `docs/Syspilot Processes/` | Authoritative process definitions owned by their declared process owners |
| `docs/syspilot/` | Authoritative specification graph; contains the Technical Writer-owned `doc` Needs but not their realized prose |
| `docs/changes/` | Concrete Contract Documents governed by their process and artifact owners; not user-guide surfaces |
| `docs/_build/` | Generated build output and verification evidence; never an authored documentation source |

### Consultations And Factual Reviews

| Documentation surface | Consulted artifact owner | Review question | Evidence and disposition |
|---|---|---|---|
| All six surfaces | User | Are scope, audience, structure, and writing style suitable? | User selected the six surfaces, project-lead audience, portal README, and relaxed technical style on 2026-08-24; accepted for drafting |
| `README.md`, `docs/getting-started.md`, `docs/product-model.md`, `docs/customization.md` | User | Does the foundation explain how customer projects apply and customize Syspilot? | User confirmed backend neutrality as intended, installation-owned ontology bootstrap as upcoming work, and project-specific specialist Actors as currently usable without a dedicated product requirement; revision accepted for final Quality review |
| `README.md`, `docs/getting-started.md` | Syspilot Setup | Are the revised customer-project onboarding, prerequisites, and Setup boundaries accurate? | Setup reviewed revision `9257029`; proceed with no factual corrections |
| `README.md`, `docs/getting-started.md`, `docs/product-model.md`, `docs/customization.md` | Syspilot Architect | Are the revised extensibility claims established by current Requirements? | Architect identified missing explicit Requirements for backend neutrality, installation bootstrap, and specialist-Actor governance; User confirmed these as intended direction and directed the completed revision to Quality review |
| `docs/customization.md` | Syspilot Project Manager | Are project-defined Contract semantics consistent with the approved model? | Project Manager reviewed revision `9257029`; proceed with no corrections and recorded the requested revision in `9c2bb80` |
| `README.md`, rendered landing page, `docs/product-model.md`, ownership map and inventory | Syspilot Architect | Is the v2 model, authority boundary, and documentation map accurate and understandable? | All corrections applied; final architecture and factual review passed; proceed |
| `docs/change-workflow.md` | Syspilot Project Manager and Syspilot Architect | Does the guide accurately contain the Contract lifecycle, ownership, responsibility, validation, and closure in user-oriented form? | Earlier PM review reflected the then-current process; guide realigned to direct User validation responsibility after authoritative corrections `aae0285` and `2c71ec6`; Quality re-review pending |
| `README.md`, `docs/getting-started.md`, `docs/product-model.md`, `docs/operations.md` | Syspilot Developer | Are repository commands, product-instance boundaries, and current limitations accurate? | Corrections applied; four focused tests and strict build independently confirmed; proceed |
| `docs/getting-started.md`, `docs/operations.md`, `README.md` | Syspilot Setup | Are current limitations, prerequisites, and Setup ownership represented accurately? | Corrections received and applied; Setup indicated proceed after these corrections |
| `docs/operations.md`, `docs/releasenotes.md` inventory | Syspilot Release | Are release responsibility and release-note ownership represented accurately? | Operations and explicit Release-owned inventory classification approved; proceed |
| `docs/customization.md`, `docs/experiences/` inventory | Syspilot Research | Is the Field-Note-derived learning-organization explanation useful and appropriately bounded? | Guide approved; inventory boundary correction applied; proceed |

### Changed Documentation And Verification

| Artifact | Change | Verification evidence |
|---|---|---|
| `docs/syspilot/documentation/index.rst` | Add six Technical Writer-owned `doc` Needs and their requirement impact links | Clean strict Sphinx build passed with zero warnings and schema validation passed with zero warnings |
| `README.md` and five v2 user guides | Replace the v1 portal and add the agreed user-oriented documentation surfaces | Four focused docs-build tests passed; clean strict Sphinx build passed with zero warnings |
| `docs/index.rst` | Separate v2 user guides, reference material, legacy v1 guides, and historical Field Notes in navigation | Clean strict Sphinx build passed with zero warnings |
| `docs/change-workflow.md` | Align the derived guide with direct User validation responsibility while retaining Project Manager support and Closure duties | Four focused docs-build tests passed; clean strict Sphinx build passed with zero warnings and schema validation passed with zero warnings |
| `README.md`, `docs/getting-started.md`, `docs/product-model.md`, `docs/customization.md` | Align the documentation with customer-project setup and four-level customization feedback from User validation | Revision complete; four focused tests passed and clean strict Sphinx/schema build passed with zero warnings; Setup and Project Manager proceeded; User resolved the Architect's product-direction concerns and directed final Quality review |
| `README.md`, `docs/getting-started.md`, `docs/customization.md` | Distinguish intended backend neutrality from currently supported backend capability | Sphinx/Sphinx-Needs retained as the current supported realization; broader backend support explicitly deferred to a future Change; final Quality re-review pending |

## Implementation And Unit Verification

**Owner:** Syspilot Developer<br>
**Status:** complete

### Decisions And Evidence

| Decision | Chosen approach | Relevant alternatives | Rationale and evidence |
|---|---|---|---|
| Classify textual product artifacts | Treat approved specifications, role cards, process definitions, and registries as authoritative product realization | Classify every file under `docs/` as user-facing documentation | Artifact purpose and authority determine ownership; path and format do not |
| Express the Technical Writer role | Keep the role card concise while describing user orientation, the `doc` Need ownership map, source authority, and consultation boundaries | Repeat all directive syntax and verification detail from the requirement | The user approved the role-card wording on 2026-08-24; operational syntax remains authoritative in the requirement and Change Process |

### Changed Artifacts And Verification

| Artifact | Change | Verification evidence |
|---|---|---|
| `docs/Syspilot Actors/Syspilot Technical Writer.md`, actor roster, and documentation toctree | Realize and expose the user-approved Technical Writer role in the authoritative product model | Clean strict Sphinx build passed with zero warnings; schema validation passed with zero warnings |
| `docs/Syspilot Processes/change.md` | Realize the optional user-facing documentation artifact, impact review, authority boundaries, and canonical evidence sections | Four focused docs-build tests passed; clean strict Sphinx build passed with zero warnings |

## Acceptance Testing

**Owner:** Syspilot Tester<br>
**Status:** passed

| Scenario | Traces to | Result | Evidence |
|---|---|---|---|
| A representative user finds the correct starting point and understands the established Syspilot product model without relying on internal specifications | observable outcome | pass | The rendered landing page exposes distinct User Guide navigation; Getting Started states current capabilities and limits; Product Model explains Needs, actors, Contracts, ownership, responsibility, and product-instance boundaries; Change Workflow provides the operational path and links to canonical authority |
| A factual artifact owner reviews a derived explanation without becoming the documentation owner or receiving Contract responsibility | collaboration boundary | pass | The Contract records factual reviews by Architect, Project Manager, Developer, Setup, Release, and Research while the User-Facing Documentation artifact remains Technical Writer-owned; responsibility changed only through the explicit Technical Writer-to-Tester handoff in committed state `99ce0b5` |

## Quality Review

**Owner:** Syspilot Quality<br>
**Status:** proceed

**Current judgment:** Proceed. The revised guides now distinguish Sphinx/Sphinx-Needs as the currently supported realization from backend neutrality as intended direction requiring a future Change. Customer-project onboarding, future bootstrap, customization levels, specialist Actors, extension links, and Contract semantics are coherently bounded; the strict build and schema validation pass without warnings, all four focused tests pass, and the acceptance evidence supports final User validation.

### Open Quality Issues

None.

## User Validation And Approval

**Owner:** User<br>
**Recorded by:** Syspilot Project Manager<br>
**Status:** accepted

**Decision and evidence:** Accepted by the User on 2026-08-24 after reading the revised documents: "ja ich habe die dokumente durchgelesen Ziele erreicht :) super". The User confirmed that the agreed goals are achieved. Responsibility transferred to the Syspilot Project Manager for Closure after the final Quality `proceed` judgment in `ce36de2`.

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

**Final outcome:** The User accepted the revised documentation foundation after confirming that the documents were reviewed and the agreed goals were achieved. The Change establishes the Technical Writer role, six traced user-documentation surfaces, customer-project onboarding and customization guidance, and explicit documentation ownership while preserving source authority. Quality recorded final `proceed` evidence in `ce36de2`; the Syspilot Project Manager closed the Change and integrated `feature/documentation-foundation` into `development` by squash. Syspilot Release remains uninvolved until an actual release from `development` to `main`.
