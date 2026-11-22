# Change Contract: ontology-link-obligations

**Status:** closed<br>
**Process owner:** Project Manager<br>
**Current responsibility:** Project Manager<br>
**Current blocker:** none<br>
**Created:** 2026-11-16<br>
- **Operation Mode**: unattended, directed by the User on 2026-11-16 and confirmed directly by the Project Manager at 22:45.

- **unattended** - the user is not reachable. When unsure, the actor flags `USER REVIEW REQUIRED` in this document, takes the simplest KISS path that is cheapest to reverse or amend, and keeps the change moving. The PM reviews flagged points once reachable again; decision ownership remains with the actor that made the decision.

## Handover log

Owned by: Project Manager

The handing-over actor appends one line as the last act before handing over, in the same commit that changes `Current responsibility`, taking `Date` as `YYYY-MM-DD` and `Time` as `HH:MM` in 24-hour local time from the system clock at that moment. The note states what the owner did and the facts that change the next owner's situation; evidence stays in the owner's section and remaining work in the open rows. The handover goes to the next actor that follows from the logical flow of the Change. The log explains transitions; the header stays authoritative.

| Date | Time | From | To | Note |
|--|--|--|--|--|
| 2026-11-16 | 22:31 | Project Manager | Architect | User released the Contract in autonomous mode; agree the link obligations and their applicability with the User. |
| 2026-11-16 | 22:37 | Architect | Developer | Obligations agreed with the User and specified in SYSP_REQ_ONTOLOGY_LINK_OBLIGATIONS; one reading flagged USER REVIEW REQUIRED. |
| 2026-11-16 | 22:42 | Developer | Technical Writer | Obligations enforced by `[needs.warnings]` in both `ontology.toml` files (Syspilot 4 keys, Example 6); strict build clean, 232 tests OK. Reader docs and the Example page should say that a missing link fails the build and that the console names the Need and key; an existing project ontology is untouched. |
| 2026-11-16 | 22:46 | Technical Writer | Quality | Documented link obligations and diagnostic limits; Architect and Developer confirmed accuracy. Strict build clean, 30 targeted tests pass after specification alignment. PM-confirmed unattended mode and validation delegation recorded; USER REVIEW REQUIRED reading preserved. |
| 2026-11-16 | 22:48 | Quality | Project Manager | Review `proceed` at 778fd1f; no open quality issue. Validation was delegated to you; the User's `USER REVIEW REQUIRED` reading on `req` outbound links stays open for the User. |
| 2026-11-16 | 22:49 | Project Manager | Quality | Delegated review found that checks do not enforce the agreed endpoint types; Quality withdrew `proceed` in consultation. Record the finding and route it to the relevant owner. |
| 2026-11-16 | 22:49 | Quality | Architect | Review `revise`: the checks enforce link presence, not the agreed endpoint types, and no User acceptance of the narrowing is recorded; see Open Quality Issues. Architect decides the route (type-aware enforcement or flagged narrowing), then the Developer. |
| 2026-11-16 | 22:50 | Architect | Developer | Typed enforcement is required and the requirement is restored; Developer finds a mechanism that checks endpoint types (Sphinx-Needs 8 offers `needs_schema` link validation); if none exists, return to me with evidence for a flagged narrowing. |
| 2026-11-16 | 22:57 | Developer | Technical Writer | Typed enforcement implemented with `needs_schema` endpoint-type rules beside the presence filters; wrong-type probes fail the build, 233 tests OK. Reader docs and Example page still state presence-only limits and need rewording; incoming types are proved by source and target rules, not by a filter. |
| 2026-11-16 | 23:00 | Technical Writer | Quality | Updated all three reader surfaces for typed enforcement; Architect and Developer confirmed accuracy. Strict build clean, 31 targeted tests pass; earlier presence-only documentation is superseded. |
| 2026-11-16 | 23:01 | Quality | Project Manager | Review `proceed` at the committing revision; typed endpoint obligations enforced and re-verified, no open quality issue. Validation was delegated to you; the User's `USER REVIEW REQUIRED` reading on outbound `req` links stays open for the User. |

## Intent And Outcome

**Status:** approved<br>
**Approval evidence:** The User reopened link obligations on 2026-11-16, chose this as the next Change and confirmed autonomous mode. The individual obligations and their applicability remain open for the User and Architect.

### Goal

The User and Architect agree which ontology link obligations are enforced automatically and where they apply; violations of the agreed obligations cause the applicable strict documentation build to fail.

### Value

Automatic checks make agreed minimum relationships visible when they are missing or invalid. They complement human review and the MECE and Trace methods, but cannot prove semantic completeness.

### Scope

- The Architect agrees the exact obligations, terminology and applicability to Syspilot's ontology, the Example Ontology, or both with the User. Existing project ontologies remain user-owned.
- The Developer implements the agreed checks and focused verification; the Technical Writer updates affected reader documentation and examples.
- Initial proposals, not settled obligations: each `story` has an incoming `validates` from an `ac`; each `req` and each Example `design` has an incoming `verifies` from a `vc`; each `req` has an outgoing `implements` to a `story`. `doc` to `req` via `includes` and `req` to `req` via `specializes` are optional. The Architect confirms the User's term "verification citation" rather than assuming it means `vc`.
- Mechanism, strict-build integration, existing-model updates and any installed-project effect follow from those decisions; no specific implementation is presumed.
- Impact discovery on the current built model, depth one in both directions, found candidates from `SYSP_REQ_EXAMPLE_ONTOLOGY` and `SYSP_REQ_ONTOLOGY_SCHEMA`, including their VCs, stories and documentation Needs. These are candidates, not a complete scope; the Architect assesses them and other affected artifacts.

### Observable Outcome

- The Contract records the User and Architect's decisions on obligations and applicability.
- Focused verification demonstrates a passing valid model and strict-build failures for violations of the agreed rules; existing intended builds remain valid.
- Specifications, ontology configuration, implementation and user-facing documentation agree with the decisions, and the documentation builds cleanly.

## Artifacts, Ownership And Process Gates

**Applicability:** Each artifact owner decides and updates its own row.<br>
**Scope change:** When the approved intent widens after a row reached a terminal status, `Intent and outcome` returns to `draft` until it is approved again, and each owner whose terminal row the wider intent may affect reassesses it: the owner sets the row back to `pending` or records in the row why its evidence still holds.<br>
**Ownership:** The `Owner` column of this table is the only statement of artifact and gate ownership in the Contract; section headings name no artifact owner.<br>
**Status:** complete

| Artifact or gate | Included | Owner | Completion evidence | Status |
|---|---|---|---|---|
| Intent and outcome | yes | Project Manager | Goal, value, scope, and observable outcome are explicit and approved | approved |
| Contract release | yes | User | User authorized release directly to the Project Manager on 2026-11-16 | approved |
| Version control | yes | Project Manager | Branch `feature/ontology-link-obligations` squash-integrated into `development` as `233a03d`; integrated tree matches reviewed tip | merged |
| Infrastructure impact | not applicable: the agreed scope is checks in the existing strict build, not workflow, CI or packaging changes; reassess if that scope changes | Admin | Affected workflow, CI, and packaging artifacts are updated, confirmed by their current owner rather than inferred from a Needs-only impact query | not applicable |
| Product specification and architecture decisions | yes | Architect | Decisions agreed with the User and changed specifications are linked and checked | approved |
| User-facing documentation | yes | Technical Writer | Typed-enforcement revision at 24b9b42: Example Ontology, Customization and Operations describe presence filters, endpoint schemas and diagnostics. Architect and Developer confirmed accuracy; strict clean build and 31 targeted tests pass; existing `doc` links remain current | complete |
| Example sync | yes | Technical Writer | Example page describes typed obligations and both diagnostic kinds; Architect and Developer confirmed accuracy; strict clean build and 31 targeted tests pass. Generic Actor and Contract examples remain unaffected | complete |
| Implementation and unit verification | yes | Developer | Changed artifacts and durable technical decisions are linked; the Developer wrote and ran the tests, including positive and violation cases, and recorded commands and results | complete |
| Acceptance test design and results | not applicable: User selected a lightweight crew without Tester; Developer verifies the agreed behavior and Quality reviews the evidence | Tester | Requirement tests written and run by the Tester, with their commands and results, and the means for User validation trace to the intended outcome | not applicable |
| Quality review | yes | Quality | Quality reviewed the recorded commands and results and re-ran the build and module; judgment `proceed` at 5cc7c1f, no open quality issue | complete |
| User validation and approval | not applicable: on 2026-11-16 the User explicitly delegated validation of this Change only to the Project Manager, who confirmed the decision directly at 22:45 | User | User validation did not occur. PM completed the delegated review after Quality `proceed`; User intends to inspect the outcome tomorrow | not applicable |
| Closure decision | yes | Project Manager | Final outcome, validation disposition, and integration state are recorded below | complete |

## Architecture And Specification

**Status:** approved

### Affected Artifacts

| Artifact | Change | Rationale |
|---|---|---|
| SYSP_REQ_ONTOLOGY_LINK_OBLIGATIONS, SYSP_VC_ONTOLOGY_LINK_OBLIGATIONS_1, _2 (req_ontology_management.rst) | add | Mandatory link obligations fail the strict build. |
| Existing Needs of Syspilot and the Example Ontology | modify as needed | Developer adds missing links the check reveals; no Need is exempted. |

### Decisions And Evidence

| Decision or check | Evidence |
|---|---|
| Obligations agreed with the User on 2026-11-16: story needs incoming ac (validates) and incoming req (implements); req needs incoming vc (verifies) and outgoing story (implements); design needs incoming vc (verifies) and outgoing req (details). | User answer in session; SYSP_REQ_ONTOLOGY_LINK_OBLIGATIONS |
| Applicability: Syspilot ontology and Example Ontology; design exists only in the Example Ontology. Existing project ontologies stay unchanged. | User answer; requirement text |
| "Verification citation" means an incoming `verifies` link from a `vc`. | User confirmed |
| The User wrote "req needs outbound req"; I read it as outbound `implements` to a story, since a req-to-req link is only `specializes`, which stays optional. USER REVIEW REQUIRED if a req-to-req obligation was meant. | Open reading, cheapest reversible |
| Typed enforcement stays required. Quality is right: my 0ee74b5 narrowed the requirement to presence without User agreement. Reverted at this commit; the User agreed typed obligations. No narrowing is accepted. | Quality finding; SYSP_REQ_ONTOLOGY_LINK_OBLIGATIONS |
| Mechanism is not prescribed; Developer chooses and records it. The descriptive `[[syspilot.diagram_edges]]` entries already hold endpoint types for Syspilot's links and may help. | Developer row |

## User-Facing Documentation

**Status:** complete

### Documentation Plan And Ownership

| Documentation surface | `doc` Need | Requirements included | Status |
|---|---|---|---|
| `docs/Example Ontology/ontology.md` | SYSP_DOC_EXAMPLE_ONTOLOGY, `realized_by` that path | Existing links plus SYSP_REQ_ONTOLOGY_LINK_OBLIGATIONS | complete |
| `docs/customization.md` | SYSP_DOC_CUSTOMIZATION, `realized_by` that path | Existing links plus SYSP_REQ_ONTOLOGY_LINK_OBLIGATIONS | complete |
| `docs/operations.md` | SYSP_DOC_OPERATIONS, `realized_by` that path | Existing links plus SYSP_REQ_ONTOLOGY_LINK_OBLIGATIONS | complete |

Impact evidence: `get_need_links.py SYSP_REQ_EXAMPLE_ONTOLOGY --direction in --depth 1 --simple --no-build` found the Example, Customization, Getting Started and Upgrade doc Needs and three VCs. The new obligation requirement's both-direction query found its story and two VCs, but no documentation yet. The first two guides need obligation explanations; Operations adds troubleshooting outside that candidate set. Getting Started already explains preservation and seeding and links to the ontology; Upgrade preserves the project's existing model, so neither needs a change. The VCs remain covered by Developer verification. Both queries used the current built model on 2026-11-16 and supplied candidates, not authoritative scope.

### Consultations And Factual Reviews

| Documentation surface | Consulted artifact owner | Review question | Evidence and disposition |
|---|---|---|---|
| Example Ontology, Customization, Operations | Developer and Architect | Are the minimum links, diagnostics, applicability and explicit presence-only limitation accurate and understandable? | Both directly confirmed a935ac7 on 2026-11-16. Developer confirmed quiet/non-quiet diagnostics and all minima; Architect confirmed fidelity and understandability and aligned the presence-only requirement wording at 0ee74b5. No reader-doc change requested |
| Typed-enforcement revision: same three surfaces | Developer and Architect | Do the revised mechanism, endpoint restrictions, diagnostics and remaining semantic limit match the restored obligation? | Both directly confirmed 24b9b42 on 2026-11-16 at 22:59 without changes: endpoint types, directions, rule IDs and semantic limit match the requirement and implemented schemas. Earlier presence-only explanations and their approvals above are superseded |

### Changed Documentation And Verification

| Artifact | Change | Verification evidence |
|---|---|---|
| `docs/Example Ontology/ontology.md` | Required incoming/outgoing links, optional links, strict-build failure and diagnostic keys, presence-only limits; replaces the unsupported claim that Trace finds missing required links | Strict clean build and 30 targeted acceptance tests pass (commands below); Architect and Developer confirmed accuracy |
| `docs/customization.md` | Minimum relationships, User/Architect agreement for changes, seeded vs existing ontology boundary and filter limitations | Strict clean build passes; Architect and Developer confirmed accuracy |
| `docs/operations.md` | Missing-link troubleshooting, non-quiet diagnostics and source-side repair for incoming links | Strict clean build passes; Architect and Developer confirmed accuracy |
| `docs/syspilot/documentation/index.rst` | Three existing `doc` Needs include SYSP_REQ_ONTOLOGY_LINK_OBLIGATIONS | Strict clean build passes |

Validation (2026-11-16): `uv run python docs\docs-build.py clean` succeeds with zero warnings and all four Syspilot link checks passing; `uv run python -m unittest discover -s tests -p test_acceptance_ontology_example.py` runs 30 tests successfully; `git diff --check` passes.

After the Architect's specification alignment at 0ee74b5, the same 30 targeted tests were rerun successfully; the Architect also reported a clean strict build at that commit.

Typed-enforcement revision after 883bfd5: the three reader surfaces now distinguish presence filters from source/target schema rules and show both diagnostic kinds. Endpoint types are enforced; semantic correctness still requires review. Impact discovery from SYSP_REQ_ONTOLOGY_LINK_OBLIGATIONS, incoming depth one against the current built model, found exactly the three existing documentation Needs and its two VCs; the current `includes` links remain applicable. Earlier presence-only verification and review above are historical and do not establish this revision's completion. Current verification (2026-11-16): `uv run python docs\docs-build.py clean` passes with zero warnings and zero schema violations; `uv run python -m unittest discover -s tests -p test_acceptance_ontology_example.py` passes 31 tests; `git diff --check` passes. Architect and Developer confirmed the current documentation without changes at 22:59.

## Example Sync

**Status:** complete

| Artifact | Change | Verification evidence |
|---|---|---|
| `docs/Example Ontology/ontology.md` | Documents all six seeded obligations and which links remain optional; the example already carries the filters from Developer work | Strict clean build and 30 targeted acceptance tests pass; Architect and Developer confirmed accuracy |
| `docs/Example Actors/`, `docs/Example Contracts/` | No change: generic roles and Contract templates do not define specific link minima; those belong to the selected ontology | Obligations introduced no role or Contract-process change |
| Typed-enforcement revision: `docs/Example Ontology/ontology.md` | Replaces the presence-only limit with source/target enforcement and the remaining semantic-review boundary; generic Actor and Contract examples stay unchanged | Strict clean build and 31 targeted tests pass; Architect and Developer confirmed accuracy without changes |

## Implementation And Unit Verification

**Status:** complete

### Decisions And Evidence

| Decision | Chosen approach | Relevant alternatives | Rationale and evidence |
|---|---|---|---|
| Mechanism | A `[needs.warnings]` table of presence filters plus `[[needs.schema_definitions.schemas]]` endpoint-type schemas in each `ontology.toml`. Warnings: Syspilot four keys, Example six (adds the two `design` keys). Schemas: per link a source rule (`<link>_from_<type>`) and a target rule (`<link>_to_<type>`): Syspilot 6 (`validates`, `implements`, `verifies`), Example 8 (adds `details`; `verifies` may reach `req` or `design`). A violation fails the strict build; the console names the Need and the rule id | A checker script run by `conf.py`; a build hook in the docs scripts; filters that look up other Needs | The obligations live in the ontology file, so they travel with the Example Ontology into installed projects and a project with its own ontology gains none; no Python is added to the generated `conf.py`, which must stay literal and neutral. `needs_schema` validates only outgoing links, so incoming types are proved by pairing: a link can leave only a Need of the source type (local schema on the linking Need) and reach only a Need of the target type (network schema), hence a nonempty `validates_back` proves an `ac` source. A filter cannot do this: Sphinx-Needs 8.0.0 gives a `needs.warnings` filter only the single Need (`len(needs) == 1`) |
| Incoming source type | Enforced by the source rules: `validates` only from `ac`, `implements` only from `req`, `verifies` only from `vc`, `details` only from `design` | Filters on `<link>_back` alone (presence only, the earlier row, withdrawn) | Quality finding: presence let any type satisfy an obligation. Probes: a `vc` validating a story and a `design` implementing a story each fail the build |
| Violation details need a non-quiet build | With `-q` only the generic line appears; the Need and rule id are printed without `-q` | none | Sphinx-Needs prints failed Needs at info level; `docs/docs-build.py` runs without `-q`; tests run violation cases without `-q` |

### Changed Artifacts And Verification

| Artifact | Change | Verification evidence |
|---|---|---|
| `docs/Syspilot Ontology/ontology.toml`, `docs/Example Ontology/ontology.toml` | `[needs.warnings]` presence table (story, req, design as before) plus endpoint-type schemas for `validates`, `implements`, `verifies` (and `details` in the Example) | `python docs/docs-build.py clean` exit 0, zero warnings and zero schema violations: no existing Need is exempt and none violates; `python docs/test_docs_build.py` 4 OK |
| `tests/test_acceptance_ontology_example.py` | `LinkObligationTests`: six missing-link cases, plus eight wrong-type cases (each source and target rule; the cases include a `vc` validating a story and a `design` implementing a story) that each fail the strict build naming the Need and the rule id; complete sample builds clean; the settings-equality test excludes `warnings` and `schema_definitions`; the sample's `SMP_VC_REQ` also verifies `SMP_REQ_GEN` | `python -m unittest discover -s tests`: 233 tests OK |

## Quality Review

**Status:** complete

**Current judgment:** `proceed` at 5cc7c1f (the earlier `proceed` at 778fd1f was withdrawn and the `revise` finding is resolved). Typed endpoint obligations are enforced by `needs_schema` source and target rules; implementation, tests, requirement and documentation agree and the results were re-run by Quality (strict build clean, acceptance module 31 OK). The User's separate reading on outbound `req` links stays flagged `USER REVIEW REQUIRED`.

### Applied Review Methods

| Method | Selected scope | Evidence | Findings | Limits |
|---|---|---|---|---|
| Recorded-result review | Diff 2336522..778fd1f: requirement and VCs, both `ontology.toml`, `LinkObligationTests`, three guides, Contract rows | Read each filter against the agreed obligations (story: incoming `validates`, `implements`; req: incoming `verifies`, outgoing `implements`; design: incoming `verifies`, outgoing `details`); read the six violation cases and the clean case; Quality re-ran `python docs/docs-build.py clean` (success) and `python -m unittest tests.test_acceptance_ontology_example` (30 OK); handover row times match their commits | no finding | Full suite (232) taken from the Developer's record, not re-run; no test for a project with its own ontology gaining no obligation beyond the Setup preservation tests of earlier Changes |
| MECE (`syspilot.mece`, same-document) | SYSP_REQ_ONTOLOGY_LINK_OBLIGATIONS; peers EDITING, LOCATION, SCHEMA; needs data from the build above | Script findings none; read: SCHEMA states no type-pair schema, and the new requirement likewise checks presence only, so no contradiction; Trace's "absent link needs a requiredness rule" now has one in the ontology, without changing Trace | no finding | `semantic-content-review-required` and `structured-coverage-data-unavailable` remain |
| Re-review of the typed-enforcement revision | Diff c318d2c..5cc7c1f: requirement, both `ontology.toml` schema rules, `LinkObligationTests`, three guides, Contract rows | Eight wrong-type cases cover each source and target rule and assert the Need and rule id in the output; the Syspilot model has no `details` rules and the Example has `details_to_req`; Quality re-ran `python docs/docs-build.py clean` (success) and `python -m unittest tests.test_acceptance_ontology_example` (31 OK); MECE and Trace re-run, no findings | no finding | Full suite (233) taken from the Developer's record; test mutation sensitivity read, not mutated |
| Trace (`syspilot.trace`, both, depth 2) | SYSP_REQ_ONTOLOGY_LINK_OBLIGATIONS | Neighborhood resolves: story SYSP_US_ONTOLOGY_MANAGEMENT, VCs _1 and _2, `includes` from Customization, Operations, Example Ontology docs; no unresolved target | no finding | Edge semantics outside the changed links not re-read |

Resolved finding: the presence-only checks (0ee74b5) narrowed the agreed typed obligations without recorded User acceptance. The Architect reverted the narrowing (d766351), the Developer added endpoint-type schemas (883bfd5), and the Technical Writer aligned the guides (24b9b42). No narrowing remains. The User-delegated validation is recorded in the artifact row as the Contract requires.

Verification is fully automated. Quality reviews the commands and results that the Developer and the Tester recorded, and executes a check itself only when a recorded result cannot support its judgment, recording the reason in the table above. A Markdown process artifact whose content has no automated check is verified by Quality's review, and the table above records that review and its limits.

Quality communicates its `proceed` judgment and supporting evidence directly to the Project Manager before the Project Manager presents the verified outcome for validation. Another actor's forwarded claim does not establish Quality's decision.

### Open Quality Issues

Keep this table synchronized with currently open issues. A missing automation is an open issue whose row names the task that closes it, the owner of that task, and the completion evidence. For each issue, Quality transfers current responsibility to the owner of the affected artifact. When Quality confirms the required outcome, update the affected artifact or evidence and remove the resolved row. At closure this table contains `None`.

| Artifact | Current issue | Required outcome |
|---|---|---|
| None | None | None |

The separate `USER REVIEW REQUIRED` reading on outbound `req` links stays open for the User.

## User Validation And Approval

**Recorded by:** Project Manager<br>
**Status:** not applicable

Quality's `proceed` judgment verifies that the change is ready for validation; it does not validate user value. For an included validation, the Project Manager presents the observable outcome after receiving Quality's direct judgment and evidence. The User communicates the validation decision directly to the Project Manager, who records the decision and evidence. Another actor's forwarded claim does not establish the User's decision. If the user requests changes, the Project Manager transfers responsibility to an included artifact owner that can produce the required outcome.

Current responsibility remains with the User from Quality's handoff until the validation decision is recorded. The Project Manager's presentation and recording duties support that User-owned artifact; they do not make the Project Manager the validation owner or an intermediate responsibility relay.

Set this artifact to `not applicable` only when the User explicitly delegates validation of the finished outcome and that delegation is recorded in its artifact row. Operation mode does not delegate validation. In unattended mode, keep it `pending` until the User returns.

**Decision and evidence:** The User explicitly delegated validation to the Project Manager, authorizing squash and closure after Quality and PM review. User validation did not occur. On 2026-11-16, after Quality's direct `proceed` at `831618a`, the PM reviewed the typed source and target schema rules, the missing-link and wrong-type tests, and the recorded strict-build and test evidence; the agreed typed obligations are covered. The User intends to inspect the result tomorrow. The Architect's `USER REVIEW REQUIRED` interpretation remains open for that inspection.

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

**Final outcome:** Typed link obligations are enforced in the Syspilot and Example ontologies and were squash-integrated into `development` at `233a03d`. Quality reported `proceed` with a clean strict build and 31 targeted tests; the Developer recorded 233 passing tests. The User explicitly delegated validation; the PM reviewed the result, and User validation did not occur. On 2026-11-17 the User confirmed the Architect's previously flagged interpretation: `req` must implement a `story`, while `req`-to-`req` specialization remains optional. Nothing was pushed.
