# Change Contract: setup-examples

**Status:** approved<br>
**Process owner:** Project Manager<br>
**Current responsibility:** Project Manager<br>
**Current blocker:** none<br>
**Created:** 2026-11-03<br>
- **Operation Mode**: autonomous, agreed with the User on 2026-11-04. Specifics: an actor stops and asks the User whenever a decision does not follow from the current context, and pauses only its own step until answered. The User-owned `Contract release` and User validation gates stay with the User.

- **autonomous** - every actor decides on its own; when genuinely unsure, it asks the user directly and pauses only its own step until answered.

## Handover log

Owned by: Project Manager

The handing-over actor appends one line as the last act before handing over, in the same commit that changes `Current responsibility`, taking `Date` as `YYYY-MM-DD` and `Time` as `HH:MM` in 24-hour local time from the system clock at that moment. The note states what the owner did and the facts that change the next owner's situation; evidence stays in the owner's section and remaining work in the open rows. The handover goes to the next actor that follows from the logical flow of the Change. The log explains transitions; the header stays authoritative.

| Date | Time | From | To | Note |
|--|--|--|--|--|
| 2026-11-04 | 09:22 | Project Manager | Architect | Contract released by the User on 2026-11-04 in autonomous mode; the five open decisions are in Architecture And Specification. |
| 2026-11-04 | 10:17 | Architect | Technical Writer | Decided the five questions and specified `SYSP_REQ_EXAMPLES` with the changed Requirements and process documents; the move of `process-maintenance.md` and the `index.md` cleanup are in your row. |
| 2026-11-04 | 10:31 | Technical Writer | Admin | Created both example folders and their `doc` Needs, applied the Architect's three review findings, and completed my two rows; the Technical Writer example card deviates and is declared. `tests/test_acceptance_adoption_feedback.py` still asserts the old `process-maintenance.md` path (Tester row). |
| 2026-11-04 | 10:45 | Admin | Tester | Infrastructure impact is not applicable: no workflow or script references the moved or new paths, and the docs build test passes. |
| 2026-11-04 | 11:01 | Tester | Quality | Wrote 25 requirement tests and moved the earlier tests to the new `process-maintenance.md` path; suite of 98 and strict build pass. Setup's run-time copy from the example folders is untested. |
| 2026-11-04 | 11:06 | Quality | Admin | Review blocked by QI-1 (yours) and QI-2 (Technical Writer's row); the delivered artifacts are sound, remaining work is in Open Quality Issues. |
| 2026-11-04 | 11:07 | Admin | Technical Writer | QI-1 fixed: the empty `Infrastructure Impact` section is removed; QI-2 is next. |
| 2026-11-04 | 11:09 | Technical Writer | Quality | QI-2 fixed: the Example Sync Build row now records the current result; I reran the strict build (succeeded). QI-1 and QI-2 await your confirmation. |
| 2026-11-04 | 11:10 | Quality | Admin | QI-1 and QI-2 verified fixed; one new defect, QI-3, in your row's time. |
| 2026-11-04 | 11:10 | Admin | Quality | QI-3 fixed: the earlier Admin row's time now reads 11:07, the commit's system-clock time. |
| 2026-11-04 | 11:11 | Quality | Admin | QI-3 verified fixed; QI-4 remains: the time of your last row. |
| 2026-11-04 | 11:11 | Admin | Quality | QI-4 fixed: the earlier Admin-to-Quality row's time now reads 11:10, the time of its commit. |
| 2026-11-04 | 11:12 | Quality | User | QI-4 verified fixed; review judgment `proceed`; ready for User validation. |
| 2026-11-05 | 13:49 | User | Project Manager | The User widened the intent: Setup asks which Contracts to install and `docs/Example Contracts/` becomes flat; Intent and outcome is `draft` until the User approves the text. |
| 2026-11-05 | 13:50 | Project Manager | Architect | The User approved the widened intent on 2026-11-05; Quality's earlier `proceed` no longer holds, and the four open points are in Scope. |
| 2026-11-05 | 13:55 | Architect | Technical Writer | Decided the four open points and widened the specification and `setup.md`; the folder move, the example `index.md`, the Process Maintenance links, and the guides are in your rows, and the Tester's tests still describe the old layout. |
| 2026-11-05 | 13:59 | Technical Writer | Tester | Flattened `docs/Example Contracts/`, reworded the Process Maintenance opening, described Contract selection in the guides, and completed my two rows after the Architect's review; the strict build succeeds. Eight tests fail on the old `examples/` layout (3 failures, 5 errors in `test_acceptance_adoption_feedback.py` and `test_acceptance_setup_examples.py`). |
| 2026-11-05 | 14:03 | Tester | Quality | Tests now follow the flat layout and Setup's Contract selection; 102 tests and the strict build pass. Your earlier `proceed` row needs reassessing for the widened scope. |
| 2026-11-05 | 14:05 | Quality | Technical Writer | Earlier `proceed` is void; the widened artifacts are sound, review is blocked by QI-1 and QI-2 (yours) and QI-3 and QI-4 (Project Manager's). |
| 2026-11-05 | 14:06 | Technical Writer | Quality | QI-1 and QI-2 fixed: the Example Sync Build row records the Tester's resolution, and my earlier handover time now reads 13:59, the time of its commit; strict build succeeded. QI-3 and QI-4 remain with the Project Manager. |
| 2026-11-05 | 14:07 | Quality | Technical Writer | QI-1 and QI-2 verified fixed; QI-5, the time of your last row, remains; QI-3 and QI-4 follow with the Project Manager. |
| 2026-11-05 | 14:08 | Technical Writer | Project Manager | QI-5 fixed: the earlier row's time now reads 14:06, the time of its commit; QI-3 and QI-4 are yours, and your Scope edits are still to be applied. |
| 2026-11-05 | 14:12 | Project Manager | Quality | QI-3 and QI-4 dispositions recorded in Intent and outcome and in Architecture And Specification; the Scope text and the `setup.md` recommendation are aligned; the User accepted the untested Setup copy and choice for the widened scope on 2026-11-05. |
| 2026-11-05 | 14:15 | Quality | User | QI-3 to QI-5 verified fixed or disposed; recorded `proceed` for the widened scope; strict build and 102 tests pass; Setup's run-time copy and Contract choice remain untested. |
| 2026-11-05 | 14:34 | User | Project Manager | The User accepted the outcome; closure recorded. |

## Intent And Outcome

**Status:** approved<br>
**Approval evidence:** The User approved the widened text on 2026-11-05. Direction decided by the User on 2026-11-03: Syspilot's own actors and Contracts stay the active project artifacts; generic copies live in separate example folders; the examples stay in the Needs graph; the Technical Writer maintains them in every Change. The User decided the widening on 2026-11-04 (the dates differ because the decision and the approval of the text were separate steps): Setup asks which Contracts to install and recommends starting with the Change Process only; the `examples` subfolder of `docs/Example Contracts/` is removed.

### Goal

Syspilot ships generic example actors and example Contracts that a project copies at Setup and then owns. The Technical Writer maintains them in every Change, so a release needs no manual merge of accumulated process changes. Setup lets the User choose which example Contracts a project installs and recommends starting with the Change Process, tailored to the project; adding other Contracts later is the project's own task.

### Value

The Setup inventory labels the role cards and the Contract processes `release-owned`, although an adopting project adapts them. With separate example sources, `release-owned` is true of the source, and Setup names it as the source of the copy. Maintaining the examples in each Change, by the Technical Writer who already writes the project-neutral text, decides "does this also hold for a general project?" while the context is fresh, instead of reconstructing it at the release. A project that installs only the Contracts it uses has a smaller process to tailor and a registry that lists exactly what it has adopted, so an optional example such as the Process Maintenance Contract no longer looks adopted.

### Scope

- `docs/Syspilot Actors/` and `docs/Syspilot Contracts/` stay Syspilot's own active artifacts.
- New `docs/Example Actors/` and `docs/Example Contracts/` hold the generic copies. For the role cards the intent is one source, identical to `docs/Syspilot Actors/` unless a deviation is declared; for the Contracts, differences are expected.
- Both folders are `doc` Needs in the Needs graph and are linked to their Requirements, so a Requirement change reaches them through Impact.
- The Change Process template gains an `Example sync` row, included by default, owned by the Technical Writer for Example Actors and Example Contracts alike, and set to `not applicable` only with a reason. Each Change names the owner in that row, so the maintainer is clear from the start of the Change.
- `docs/Example Contracts/` is flat: every file in it is an example Contract, and the `examples` subfolder with `process-maintenance.md` goes away. A project's registry lists only the Contracts it installed.
- Setup asks the User which example Contracts to install and recommends the Change Process first. The Setup inventory names the example folders as the source of the copied role cards and the chosen Contract processes.
- The Release Process states that it verifies the `Example sync` rows of the Changes since the last tag instead of merging them.
- The requirements and tests that describe these follow; the Architect lists the affected artifacts and decides the open points below.

The Architect decided the open points of the widened intent and recorded them in Architecture And Specification: `contract-documents.md` is always installed because the other Contracts link to it; a selection also contains the Contracts a selected one requires; all nine role cards are installed whichever Contracts are selected; Setup generates the registry; the source folder is flat.

Syspilot supports only the initial Setup. A project that later adds a Contract may look in `docs/Example Contracts/` for a template; that is the project's own task and Syspilot does not provide it. The User decided this on 2026-11-05.

### Observable Outcome

The two example folders exist and build as `doc` Needs with zero warnings; `docs/Example Contracts/` has no subfolder. Setup names them as its source, asks which Contracts to install, and recommends the Change Process first. The Change template carries the `Example sync` row. A test fails when a role card in `docs/Example Actors/` and `docs/Syspilot Actors/` differ without a declared deviation. The tests pass. Setup's run-time copy and choice are not tested; no harness exists. The User accepted that limit for the first scope on 2026-11-04 and for the widened scope, including the Contract choice, on 2026-11-05.

## Artifacts, Ownership And Process Gates

**Applicability:** Each artifact owner decides and updates its own row.<br>
**Scope change:** When the approved intent widens after a row reached a terminal status, `Intent and outcome` returns to `draft` until it is approved again, and each owner whose terminal row the wider intent may affect reassesses it: the owner sets the row back to `pending` or records in the row why its evidence still holds.<br>
**Ownership:** The `Owner` column of this table is the only statement of artifact and gate ownership in the Contract; section headings name no artifact owner.<br>
**Status:** pending

| Artifact or gate | Included | Owner | Completion evidence | Status |
|---|---|---|---|---|
| Intent and outcome | yes | Project Manager | Goal, value, scope, and observable outcome are explicit and approved | approved |
| Contract release | yes | User | User authorization to start the Change; no other actor may set this gate | approved |
| Version control | yes | Project Manager | Feature branch `feature/setup-examples`; squash-integrated into `development` at closure | complete |
| Infrastructure impact | yes | Admin | Affected workflow, CI, and packaging artifacts are updated, confirmed by their current owner rather than inferred from a Needs-only impact query; Admin sets `not applicable` with a reason if the new folders touch none | not applicable: `release.yml` and `scripts/` reference no actor, Contract, or `process-maintenance.md` path; the docs build test passes with the new folders |
| Product specification and architecture decisions | yes | Architect | Changed specification and architecture artifacts are linked and checked; the open decisions below are decided and recorded | complete |
| Example sync | yes | Technical Writer | Both folders created from the current actors and Contracts, generalized where needed, with `doc` Needs and `includes` links; deviations from `docs/Syspilot Actors/` declared; documentation builds cleanly | complete |
| User-facing documentation | yes | Technical Writer | Agreed documentation surface is coherent and user-oriented; factual-owner review is recorded; `doc` Needs and `includes` links are current; documentation builds cleanly | complete |
| Implementation and unit verification | not applicable: no code or script changes; the requirement tests belong to the Tester | Developer | Changed artifacts and durable technical decisions are linked; the Developer wrote and ran the unit tests, and their commands and results are recorded | not applicable |
| Acceptance test design and results | yes | Tester | Requirement tests written and run by the Tester, with their commands and results, and the means for User validation trace to the intended outcome | complete |
| Quality review | yes | Quality | Quality review recorded `proceed` at cb2ef67 for the widened scope; see Quality Review | complete |
| User validation and approval | yes | User | Observable outcome is accepted or changes are requested | accepted |
| Closure decision | yes | Project Manager | Final outcome, validation disposition, and integration state are recorded | complete |

## Architecture And Specification

**Status:** complete

### Open Decisions For The Architect

None. The five decisions the Project Manager raised are decided in Decisions And Evidence, and so are the four points of the widened intent (2026-11-05).

### Affected Artifacts

| Artifact | Change | Rationale |
|---|---|---|
| `SYSP_US_EXAMPLES`, `SYSP_AC_EXAMPLES_1`, `SYSP_AC_EXAMPLES_2` (`us_examples.rst`) | add | Story and acceptance criteria for the User-approved intent |
| `SYSP_REQ_EXAMPLES`, `SYSP_VC_EXAMPLES_1` (`req_examples.rst`) | add | Folder contents, layout, role-card identity with declared deviations, `doc` Needs, build, maintenance |
| `SYSP_REQ_SETUP`, `SYSP_VC_SETUP_1` | modify | Class `seeded copy`; example folders as source; `setup.md` not installed |
| `SYSP_REQ_CHANGE_CONTRACT`, `SYSP_VC_CHANGE_CONTRACT_1` | modify | `Example sync` row |
| `SYSP_REQ_RELEASE_CONTRACT`, `SYSP_VC_RELEASE_CONTRACT_1` | modify | Release verifies `Example sync` rows |
| `SYSP_REQ_TECHNICAL_WRITER`, `SYSP_VC_TECHNICAL_WRITER_1` | modify | Maintenance duty and deviation declaration |
| `SYSP_REQ_PROCESS_MAINTENANCE` | modify | Realization path and registry location move to `docs/Example Contracts/` |
| `docs/Syspilot Contracts/setup.md`, `change.md`, `release.md`; `docs/Syspilot Actors/Technical Writer.md` | modify | Realizations of the Requirements above (done by the Architect) |
| `docs/Example Actors/`, `docs/Example Contracts/` incl. `examples/process-maintenance.md` (moved), two `doc` Needs, `docs/index.rst` toctree | add / move | Technical Writer row |
| `docs/Syspilot Contracts/index.md` | modify | Remove the `Examples` section and the intro sentence that points adopters to worked examples; state that adopters receive generic copies from `docs/Example Contracts/`. Done together with the move so the build stays clean (Technical Writer row) |
| `tests/test_acceptance_adoption_feedback.py` | modify | Asserts the old `process-maintenance.md` path and registry location (Tester row) |
| Widened intent 2026-11-05: `SYSP_US_EXAMPLES` (new `SYSP_AC_EXAMPLES_3`), `SYSP_REQ_EXAMPLES`, `SYSP_VC_EXAMPLES_1`, `SYSP_REQ_SETUP`, `SYSP_VC_SETUP_1`, `SYSP_REQ_PROCESS_MAINTENANCE`, `SYSP_VC_PROCESS_MAINTENANCE_1`, `docs/Syspilot Contracts/setup.md` | modify | Contract selection, generated registry, flat example folder (done by the Architect) |
| `docs/Example Contracts/` | modify | Move `examples/process-maintenance.md` to the folder root and fix its links `../change.md` and `../contract-documents.md` to same-folder links; reword its opening, which calls it separate from the source project's processes and says to adopt it explicitly; `index.md` lists it under `Processes`, loses the `Examples` section, and keeps the preamble above `Processes` as the text Setup reuses (Technical Writer row) |
| `docs/getting-started.md`, `docs/operations.md`, `docs/upgrade.md`, `docs/methodology.md`, `docs/customization.md` | reassess | They describe Setup or link the moved example (Technical Writer rows) |
| `tests/test_acceptance_setup_examples.py`, `tests/test_acceptance_adoption_feedback.py` | modify | File set, mirror-layout test, link rule, registry location (Tester row) |

### Decisions And Evidence

| Decision or check | Evidence |
|---|---|
| Class of the copy: new class `seeded copy`, not `release-owned`. Reason: `release-owned` means a destination must equal its source, which is false once a project adapts the copy; Setup's own gate only runs once on a pristine project, so it checks identity at verification and never again | `setup.md` inventory paragraph and Integrity gate; `SYSP_REQ_SETUP` |
| Destinations stay `docs/Syspilot Actors/` and `docs/Syspilot Contracts/`. Reason: generated actor contexts, the installed-project instructions, and existing installs point there; only the source changes | `setup.md` Actor Setup; `SYSP_REQ_SETUP` |
| `docs/Example Contracts/` mirrors the destination layout, so Setup copies one source directory and relative links resolve in both | Superseded 2026-11-05 by the flat folder below |
| `process-maintenance.md` moves into `docs/Example Contracts/examples/`. Reason: it is already generic, adopters receive it, and a second source directory for it would duplicate the Setup job; it keeps its `Examples` heading in the example registry, so it still gains authority only through adoption | Superseded 2026-11-05: the User removed the `examples` subfolder |
| Generic examples: `index.md`, `contract-documents.md`, `change.md`, `release.md`, `process-maintenance.md`. Syspilot-only: `setup.md`. Reason for `release.md`: every project installs the Release actor, which needs a process, and today receives Syspilot's own with its workflow and Pages details; the example keeps those as values to fill in. Reason for `setup.md`: the Setup Contract is a runbook of one installation and is retained at `.syspilot/setup-contract.md`, so a project gains nothing from a second copy. This is the decision most open to disagreement | `SYSP_REQ_EXAMPLES`, `SYSP_REQ_SETUP` |
| Product-maintenance elements stay out of the generic Contracts: the `Example sync` row in `change.md` and the example verification in `release.md` exist only because Syspilot ships examples | `SYSP_REQ_EXAMPLES` ("only what holds for any adopting project") |
| Folder names `Example Actors` and `Example Contracts` confirmed; they follow `Syspilot Actors` and `Syspilot Contracts`, and no workflow, test, or instruction path names them yet | Search of `.github/workflows`, `docs/conf.py`, `docs/docs-build.py`, `tests/` |
| Deviations are declared in a `Deviations` table (card, reason) in `docs/Example Actors/index.md`. Reason: that file is not installed because Setup generates the adopter's registry, so the declaration never lands in an adopting project; a test can read a table; the test fails both on an undeclared difference and on a declared deviation without a difference | `SYSP_REQ_EXAMPLES`, `SYSP_VC_EXAMPLES_1` |
| Example folders are built with the documentation, not excluded. Reason: the build then checks their internal links, and the `doc` Needs describe built files | `SYSP_REQ_EXAMPLES` |
| Process documents of Syspilot (`setup.md`, `change.md`, `release.md`, role card) were edited by the Architect as realizations of the modified Requirements; the Contract has no separate row for process documents | This section |
| Strict build `python docs/docs-build.py clean` succeeded; `python -m unittest discover -s tests` 73 tests pass; `python docs/test_docs_build.py` 4 tests pass. The new `SYSP_REQ_EXAMPLES` has no `included_in` links until the Technical Writer creates the `doc` Needs | Commands run in the working tree on 2026-11-04 |
| Widened intent, point 1: `contract-documents.md` is always installed. Reason: `change.md`, `release.md`, and `process-maintenance.md` each link to it as their method, so without it every installed Contract has a link that does not resolve and the target's zero-warning build fails. The Scope text says the instructions reference it; a search of `.github/instructions/` finds no such reference, so the reason is the links, not the instructions | `SYSP_REQ_SETUP`; `setup.md` Contract Selection table; grep of relative links in `docs/Example Contracts/` |
| Widened intent, selection rule: a selection also contains every Contract a selected Contract requires, and Setup tells the User what it added. Reason: the same link rule; the links show one dependency beyond the method, `process-maintenance.md` to `change.md` (two links); `release.md` links only the method, so Release is selectable without the Change Process | `setup.md` Contract Selection table `Requires` column; `SYSP_REQ_EXAMPLES` link rule |
| Widened intent, point 2: the Release role card needs no change and all nine cards are installed whichever Contracts are selected. Reason: no card names a Contract process file (Admin names the Process Maintenance Contract only as an example, Release names none), so a card has no dependency on the selection; an actor whose process is not installed has no assignment from it until the project adopts it, and Setup says so in the handoff to the Project Manager | `docs/Example Actors/*.md`; `SYSP_REQ_SETUP`; `setup.md` Phase 7 |
| Widened intent, point 3: Setup generates the project's registry instead of copying `index.md`. Reason: a copied index would list Contracts the project did not install and break the build; the registry preamble is taken from the text of `docs/Example Contracts/index.md` above its `Processes` heading, so the wording stays in one place, and the example `index.md` serves the documentation build and is not installed, as `docs/Example Actors/index.md` already does | `SYSP_REQ_SETUP`, `SYSP_REQ_EXAMPLES`; `setup.md` inventory job `Contract registry` |
| Widened intent, point 4: the mirror rule reads as a flat rule. Every file in `docs/Example Contracts/` other than `index.md` is one Contract and is installed under its own name directly in `docs/Syspilot Contracts/`; the folder has no subfolder; links between Contracts are same-folder links that resolve in both places. Process Maintenance is then a normal selectable Contract, so `SYSP_REQ_PROCESS_MAINTENANCE` loses its "listed apart under `Examples`" boundary and now states that it is optional and requires the Change Process | `SYSP_REQ_EXAMPLES`, `SYSP_REQ_PROCESS_MAINTENANCE` |
| Widened intent, later addition of a Contract: out of scope by the User's decision of 2026-11-05. Reason: Syspilot supports only the initial Setup; a project that adds a Contract later may look in `docs/Example Contracts/` of its pinned release (`.syspilot/project.toml`) for a template, and that is the project's task. No requirement is added; the Setup recommendation says so | User decision 2026-11-05; Scope; `setup.md` Contract Selection paragraph; `upgrade.md` manual copy steps |
| Strict build `python docs/docs-build.py clean` succeeded with 0 schema warnings and `python -m unittest discover -s tests` ran 98 tests OK after the widened specification (2026-11-05). The tests still describe the old layout, because the example folder is unchanged until the Technical Writer moves it | Commands run in the working tree on 2026-11-05 |

## Example Sync

**Status:** complete

| Artifact | Change | Verification evidence |
|---|---|---|
| `docs/Example Actors/` (nine role cards, `index.md` with one `Deviations` row) | Copied from `docs/Syspilot Actors/`; the Technical Writer card omits the example-maintenance paragraph, declared in `Deviations`, because an adopting project has neither example folder nor an `Example sync` row (Architect finding) | Eight cards identical; `SYSP_DOC_EXAMPLE_ACTORS` links the nine role requirements and `SYSP_REQ_EXAMPLES` |
| `docs/Example Contracts/` `contract-documents.md`, `change.md`, `release.md`, `index.md` | Copied from Syspilot's Contracts and generalized: `change.md` loses the `Example sync` row and section and names `{integration branch}`; `release.md` carries `{integration branch}`, `{release branch}`, `{tag form}`, `{publication workflow}`, `{publication target}`, `{release notes file}`, and check commands as values to fill in and drops the `Example sync` verification; `contract-documents.md` names opening the document in the editor as the default; `index.md` is the adopter registry without `setup.md` | `SYSP_DOC_EXAMPLE_CONTRACTS` links the four Contract requirements and `SYSP_REQ_EXAMPLES`; no Syspilot repository path, workflow, branch, or tag form remains (grep) |
| `docs/Example Contracts/process-maintenance.md` | Moved from `examples/` to the folder root (`git mv`), the empty `examples` folder removed; links to `change.md` and `contract-documents.md` are now same-folder links; the opening no longer calls it separate from the source project's processes and says it is optional and gains authority once installed; `index.md` lists it under `Processes` and has no `Examples` section | Strict build succeeded; no `../` link remains in `docs/Example Contracts/` (grep); the example's two other links resolve to files in the folder |
| `docs/Syspilot Contracts/index.md`, `docs/index.rst` | `Examples` section and worked-example sentence removed; adopters pointed to `docs/Example Contracts/`; both example folders added to the toctree, the example role cards through a hidden toctree in `docs/Example Actors/index.md` | |
| Build | | `python docs/docs-build.py clean`: build succeeded on 2026-11-05 after the move, `git diff --check` clean. `python -m unittest discover -s tests`: the 3 failures and 5 errors on the old `examples/` layout were resolved by the Tester at 7971051 (102 tests OK, as the Tester recorded) |

## User-Facing Documentation

**Status:** complete

### Documentation Plan And Ownership

| Documentation surface | `doc` Need | Requirements included | Status |
|---|---|---|---|
| `docs/getting-started.md` | `SYSP_DOC_GETTING_STARTED` | Contract selection described; `SYSP_REQ_SETUP` already included | verified |
| `docs/upgrade.md` | `SYSP_DOC_UPGRADE`, `docs/upgrade.md` | adds `SYSP_REQ_EXAMPLES`; step 6 now says to copy the Contracts used, Change Process first | verified |
| `docs/methodology.md` | `SYSP_DOC_METHODOLOGY`, `docs/methodology.md` | adds `SYSP_REQ_EXAMPLES`; moved example link | verified |
| `docs/customization.md` | existing `doc` Need | moved example link only | verified |
| `docs/operations.md`, `docs/product-model.md`, `docs/branching.md`, `docs/change-contract.md`, `README.md` | unchanged | Reassessed against the widened intent: they mention Setup or the Release process without naming the example folders or the Contract set | no change |

### Consultations And Factual Reviews

| Documentation surface | Consulted artifact owner | Review question | Evidence and disposition |
|---|---|---|---|
| `upgrade.md`, `methodology.md`, `customization.md` | Architect | Is this accurate and understandable for the intended user? | Reviewed on 25d8659: no finding on `upgrade.md`, `customization.md`, the methodology table row, and the generalization of `change.md`, `contract-documents.md`, `index.md`. Three findings fixed: Technical Writer example card deviation declared, `methodology.md` sentence on the registry reworded, `release.md` whitespace and tag form made consistent |
| `getting-started.md`, `upgrade.md` step 6, `docs/Example Contracts/process-maintenance.md` and `index.md` | Architect | Does the Contract selection text match `setup.md`, and does the flat layout read correctly? | Reviewed on 107c9a9: no finding on `getting-started.md` or the example `index.md`. Two findings fixed: `upgrade.md` step 6 now says the upgrading project writes its own registry (no Setup runs) and names the Process Maintenance and Release dependencies; the `process-maintenance.md` opening now says the example adds a Contract for maintaining process documents and requires the Change process and the method |

### Changed Documentation And Verification

| Artifact | Change | Verification evidence |
|---|---|---|
| `docs/getting-started.md` | Setup asks which Contracts to install, recommends the Change Process alone, always installs Contract Documents, adds required Contracts and says so, and generates a registry listing the installed Contracts | Strict build clean |
| `docs/upgrade.md` | Step 6 names `docs/Example Contracts/` and `docs/Example Actors/` as the source and says to copy the Contracts in use, each under its own name | Strict build clean |
| `docs/methodology.md` | Table row for the example folders; moved example link | Strict build clean |
| `docs/customization.md` | Moved example link | Strict build clean |

## Acceptance Testing

**Status:** complete

| Scenario | Traces to | Result | Evidence |
|---|---|---|---|
| AT-1 Both folders hold exactly the listed files; `setup.md` stays out; `docs/Example Contracts/` is flat | `SYSP_REQ_EXAMPLES`, `SYSP_VC_EXAMPLES_1`, widened Scope | pass | `FolderContentTests` (7) |
| AT-2 A role card differs undeclared, or a declared deviation does not differ: the test fails | `SYSP_REQ_EXAMPLES`, observable outcome | pass | `DeviationTests` (3); mutation-checked both directions |
| AT-3 The Contract examples hold no Syspilot-specific value, carry the placeholders, differ from Syspilot's own, and use no Needs markup | `SYSP_REQ_EXAMPLES` | pass | `GenericContractTests` (5); mutation-checked |
| AT-4 Each folder is a `doc` Need whose `includes` equal the carried requirements, all of which exist | `SYSP_REQ_EXAMPLES`, `SYSP_VC_EXAMPLES_1` | pass | `DocNeedTests` (4) |
| AT-5 The Change template carries the `Example sync` row (Technical Writer, default yes), Release verifies it, Setup names the example folders as source of a seeded copy | `SYSP_AC_EXAMPLES_1`, `SYSP_AC_EXAMPLES_2`, Change Scope | pass | `ProcessRuleTests` (7); mutation-checked |
| AT-5b Every link between example Contracts points at `contract-documents.md` or a required Contract; Setup's Contract selection table states exactly those requirements; selected Contracts are copied under their own names and the registry is generated | `SYSP_REQ_EXAMPLES`, `SYSP_REQ_SETUP`, widened Scope | pass | `FolderContentTests` (4 of the 7) and `ProcessRuleTests`; five mutations of links, the requires row, copy mode, the registry row, and the Process Maintenance path were detected |
| AT-6 Documentation builds with zero warnings | observable outcome | pass | `python docs/docs-build.py clean`: build succeeded, 0 schema warnings; `python docs/test_docs_build.py` 4 tests OK |
| AT-7 Earlier tests follow the flat location of `process-maintenance.md` | Tester row | pass | `tests/test_acceptance_adoption_feedback.py` reads both registries and the flat path |

Commands: `python -m unittest tests.test_acceptance_setup_examples` 29 tests OK; `python -m unittest discover -s tests` 102 tests OK. Not tested: Setup's run-time copy and Contract choice (no harness; accepted by the User on 2026-11-04).

## Quality Review

**Status:** proceed

**Current judgment:** proceed at cb2ef67 for the widened scope; QI-1 to QI-5 are verified fixed or disposed. The earlier `proceed` at f088982 covered the first scope and is void; verification restarted for the widened scope, and the widened artifacts are sound. QI-3: the dates differ because the User's decision and the approval of the text were separate steps, and the User's acceptance of the untested Setup copy and choice for the widened scope is recorded for 2026-11-05. QI-4: later addition of a Contract is out of scope by the User's decision of 2026-11-05, stated in Scope, `setup.md`, and Decisions. Quality reran `python docs/docs-build.py clean` (build succeeded) and `python -m unittest discover -s tests` (102 tests OK) at cb2ef67. Reviewed and in agreement with the approved widened intent: the flat `docs/Example Contracts/` (four Contracts plus `index.md`, no subfolder), the Contract Selection table with its `Requires` column against the actual links, the generated registry, `SYSP_REQ_EXAMPLES`, `SYSP_REQ_SETUP`, `SYSP_REQ_PROCESS_MAINTENANCE`, `SYSP_AC_EXAMPLES_3`, and the changed guides. Setup's run-time copy and Contract choice stay untested because no harness exists; the User accepted that limit for the widened scope on 2026-11-05, and it remains a limit for validation.

### Applied Review Methods

| Method | Selected scope | Evidence | Findings | Limits |
|---|---|---|---|---|
| Impact discovery | Candidates from the Trace neighborhoods of `SYSP_REQ_EXAMPLES`, `SYSP_REQ_SETUP`, `SYSP_REQ_PROCESS_MAINTENANCE`, `SYSP_US_EXAMPLES`, `SYSP_AC_EXAMPLES_3`, `SYSP_DOC_GETTING_STARTED`, `SYSP_DOC_UPGRADE`, `SYSP_DOC_EXAMPLE_CONTRACTS`, built from the strict clean build. | `SYSP_REQ_SETUP` reaches `SYSP_DOC_GETTING_STARTED`, `SYSP_DOC_UPGRADE`, `SYSP_DOC_OPERATIONS`, `SYSP_DOC_README`, `SYSP_DOC_PRODUCT_MODEL`, `SYSP_DOC_BRANCHING`, `SYSP_DOC_CUSTOMIZATION`, and `SYSP_DOC_METHODOLOGY`; the Documentation Plan lists five changed and five reassessed-unchanged surfaces. | No omitted candidate. | Needs discovery supplies candidates, not semantic Markdown review. |
| MECE horizontal coverage | `SYSP_REQ_SETUP` and `SYSP_REQ_PROCESS_MAINTENANCE`, all-type (21 Requirement peers each); earlier all-type runs for `SYSP_REQ_EXAMPLES` and `SYSP_DOC_EXAMPLE_ACTORS` stand. | Script findings are empty. Selection and registry sit in Setup, the flat layout and link rule in Examples, optionality and the Change Process dependency in Process Maintenance, with no overlap or contradiction. | No structural finding. | Reports `semantic-content-review-required` and `structured-coverage-data-unavailable`. |
| Trace relationship analysis | The eight objects named under Impact discovery; both directions, depth 1. | Zero unresolved targets. `SYSP_US_EXAMPLES` -> `SYSP_AC_EXAMPLES_1`, `SYSP_AC_EXAMPLES_2`, `SYSP_AC_EXAMPLES_3`, `SYSP_REQ_EXAMPLES`, `ROOT_SYSPILOT`; `SYSP_AC_EXAMPLES_3` -> `SYSP_US_EXAMPLES`; `SYSP_DOC_EXAMPLE_CONTRACTS` -> the Change, Contract Documents, Examples, Process Maintenance, and Release Requirements. | No inconsistent relationship. | Depth 1 only. |
| Manual artifact review | `setup.md` Contract Selection, inventory, and Integrity rows; the three modified Requirements and the Story; the Contract's rows, log, and Build rows; the commit chronology for the log times. | Compared the Selection table with the Requirement text and the Decisions rows; compared each log row's time with its commit time. | QI-1 to QI-4. | Reader-based. |
| Acceptance evidence | AT-1 to AT-7 including AT-5b. | Reran the suite and the strict build as stated. | Supports the testable claims. | Tests do not execute Setup. |

Verification is fully automated. Quality reviews the commands and results that the Developer and the Tester recorded, and executes a check itself only when a recorded result cannot support its judgment, recording the reason in the table above. A Markdown process artifact whose content has no automated check is verified by Quality's review, and the table above records that review and its limits.

Quality communicates its `proceed` judgment and supporting evidence directly to the Project Manager before the Project Manager presents the verified outcome for validation. Another actor's forwarded claim does not establish Quality's decision.

### Open Quality Issues

Keep this table synchronized with currently open issues. A missing automation is an open issue whose row names the task that closes it, the owner of that task, and the completion evidence. For each issue, Quality transfers current responsibility to the owner of the affected artifact. When Quality confirms the required outcome, update the affected artifact or evidence and remove the resolved row. At closure this table contains `None`.

None

## User Validation And Approval

**Recorded by:** Project Manager<br>
**Status:** accepted

Quality's `proceed` judgment verifies that the change is ready for validation; it does not validate user value. For an included validation, the Project Manager presents the observable outcome after receiving Quality's direct judgment and evidence. The User communicates the validation decision directly to the Project Manager, who records the decision and evidence. Another actor's forwarded claim does not establish the User's decision. If the user requests changes, the Project Manager transfers responsibility to an included artifact owner that can produce the required outcome.

Current responsibility remains with the User from Quality's handoff until the validation decision is recorded. The Project Manager's presentation and recording duties support that User-owned artifact; they do not make the Project Manager the validation owner or an intermediate responsibility relay.

**Decision and evidence:** The User accepted the outcome directly to the Project Manager on 2026-11-05 after the presentation of Quality's `proceed` at 0e204af. The presentation named three limits: Setup's run-time copy and Contract choice are untested, `setup.md` stays Syspilot-only while `release.md` has a generic example, and whether the `{...}` placeholders of the example `release.md` suffice shows only at its first use in a project.

## Closure

**Status:** complete

- [x] Every included artifact or gate has terminal status and completion evidence.
- [x] Intent and outcome are `approved`.
- [x] Quality has recorded a `proceed` judgment.
- [x] Open Quality Issues contains `None`.
- [x] User validation is `accepted`, or its `not applicable` status and explicit User delegation are recorded in the artifact row.
- [x] Current blocker is `none`.
- [x] The observable outcome is demonstrated.

**Final outcome:** Syspilot ships `docs/Example Actors/` and a flat `docs/Example Contracts/` as `doc` Needs; Setup asks which Contracts to install and recommends the Change Process first; the Change template carries the `Example sync` row, owned by the Technical Writer; the Release Process verifies those rows. The User accepted on 2026-11-05. Integrated by squash into `development` from `feature/setup-examples` as the commit titled `feat: setup-examples`. Not tested: Setup's run-time copy and Contract choice, accepted by the User. Later addition of a Contract is the project's own task.
