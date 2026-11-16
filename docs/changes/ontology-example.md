# Change Contract: ontology-example

**Status:** accepted<br>
**Process owner:** Project Manager<br>
**Current responsibility:** Project Manager<br>
**Current blocker:** none<br>
**Created:** 2026-11-15<br>
- **Operation Mode**: unattended, agreed with the User on 2026-11-15; the User reviews at the end.

- **unattended** - the user is not reachable. When unsure, the actor flags `USER REVIEW REQUIRED` in this document, takes the simplest KISS path that is cheapest to reverse or amend, and keeps the change moving. The PM reviews flagged points once reachable again; decision ownership remains with the actor that made the decision.

## Handover log

Owned by: Project Manager

The handing-over actor appends one line as the last act before handing over, in the same commit that changes `Current responsibility`, taking `Date` as `YYYY-MM-DD` and `Time` as `HH:MM` in 24-hour local time from the system clock at that moment. The note states what the owner did and the facts that change the next owner's situation; evidence stays in the owner's section and remaining work in the open rows. The handover goes to the next actor that follows from the logical flow of the Change. The log explains transitions; the header stays authoritative.

| Date | Time | From | To | Note |
|--|--|--|--|--|
| 2026-11-15 | 00:43 | Project Manager | Architect | Contract released by the User in unattended mode; define the Example Ontology and the specification changes for location, Setup fallback, and the `syspilot.ontology` skill. |
| 2026-11-15 | 00:58 | Architect | Technical Writer | Specified the Example Ontology and the location, Setup, and skill requirements; `docs/Example Ontology/ontology.toml` exists. The `docs/Syspilot Ontology/` files and the moves are Developer work. |
| 2026-11-15 | 01:03 | Technical Writer | Developer | Wrote `docs/Example Ontology/ontology.md` and updated the guides; the Architect reviewed it. When the generated page moves, update the `ontology-reference` toctree entry in `docs/index.rst` and the link in `docs/namingconventions.md`. |
| 2026-11-15 | 01:07 | Developer | Tester | Moved the ontology to `docs/Syspilot Ontology/`, rebound `conf.py`, Setup runbook, skill, tests and navigation; strict build and 202 tests pass. Acceptance covers Setup with and without ontology and Example Ontology strict build with every type and link, plus Impact/MECE/Trace on it. |
| 2026-11-15 | 01:15 | Tester | Quality | Acceptance passes: 22 new tests, suite 224 OK, strict build clean. Skills resolve their default ontology from their install location. Setup's run-time copy is tested at Contract-text level only. |
| 2026-11-16 | 21:15 | Quality | Project Manager | Paused before review on the PM's scope change (Mermaid link diagrams, Intent back to draft); no Quality Review content written. Earlier handover row times (Architect 01:10 vs. commits 00:58/01:00) do not match their commits. |
| 2026-11-16 | 21:17 | Project Manager | Architect | User widened scope: Mermaid link diagram in both `ontology.md` (Goal 5); intent re-approved by that decision. Owners of terminal rows reassess them. Rendering in installed projects is open. The User authorized the Technical Writer to adopt and commit the uncommitted draft in `docs/Example Ontology/ontology.md`; it is the target form. |
| 2026-11-16 | 21:24 | Architect | Technical Writer | Specified the link diagrams and their rendering in installed projects (see Decisions). Adopt the draft with the `{mermaid}` directive in place of the plain fence; the plain fence fails the strict build. Reassess your rows. |
| 2026-11-16 | 21:26 | Technical Writer | Developer | Adopted the approved Example Ontology diagram; Architect confirmed its two requirement instances. Clean build passes; generated diagram and Setup rendering remain open. |
| 2026-11-16 | 21:31 | Developer | Tester | Implemented the generated Syspilot diagram and Mermaid in the Setup scaffold; strict build clean, suite green after relaxing the Tester's page test to allow the `{mermaid}` fence. Reassess acceptance rows for Goal 5, including an installed-project strict build of the Example page. |
| 2026-11-16 | 21:36 | Tester | Quality | Acceptance reassessed for Goal 5: 5 tests added (27 in module), suite 229 OK, strict build clean. Diagram rendering in a browser is untested; the build proves the directive only. |
| 2026-11-16 | 21:36 | Quality | Architect | Review `revise`: four minor wording and record defects, no substantive finding; see Open Quality Issues. Architect fixes the two requirement clauses, then the Developer. |
| 2026-11-16 | 21:42 | Architect | Developer | Reworded SYSP_REQ_SETUP_DOCS and SYSP_REQ_EXAMPLE_ONTOLOGY into separate clauses (meaning unchanged) and corrected my two earlier log times to my commit times. Developer rows of Open Quality Issues remain. |
| 2026-11-16 | 21:38 | Developer | Quality | Split the Setup scaffold sentence into extensions, Mermaid reason, and the no-hook statement; repaired the garbled Goal 5 implementation rows and restored the heading spacing. Strict build clean; Setup tests green. Handover-log time defect remains the Project Manager's. |
| 2026-11-16 | 21:39 | Quality | User | Review `proceed` at 2774375; no open quality issue. Browser rendering of the diagrams is untested. The Project Manager presents the outcome for validation. |
| 2026-11-16 | 21:51 | Quality | Tester | Review `revise` after the User revision: the Example diagram is sound, but the acceptance row and test still describe the two-node diagram and the test cannot detect duplicate type nodes; see Open Quality Issues. |
| 2026-11-16 | 21:53 | Tester | Quality | Row and test now describe one node per type; the test fails on a duplicated type node or a changed specialization edge (both mutated). 27 tests, suite 229 OK, strict build clean. |
| 2026-11-16 | 21:49 | User | Technical Writer | User requested changes (recorded by the Project Manager): Example diagram at type level with `req -->|specializes| req`; drop the General Requirement node, its edge, and the two-node explanation. |
| 2026-11-16 | 21:49 | Technical Writer | Quality | Unified the Example diagram at type level; Architect confirmed semantics and aligned the requirement. All 27 targeted acceptance tests pass after that alignment; strict build clean. |
| 2026-11-16 | 21:55 | Quality | User | Review `proceed` at 1ca4dd1 after the User revision; no open quality issue. The Project Manager re-presents the outcome for validation. |
| 2026-11-16 | 22:18 | User | Project Manager | User accepted the outcome (recorded by the Project Manager); closure and squash integration follow. |

## Intent And Outcome

**Status:** approved<br>
**Approval evidence:** Scope discussed and agreed with the User in the Project Manager chat on 2026-11-14/15 (location, Example Ontology types, Setup fallback, `.syspilot/` remainder, one Change). Widened by the User directly to the Project Manager on 2026-11-16 21:13: both `ontology.md` pages get a Mermaid link diagram within this Change (Goal 5); this decision re-approves the widened intent.

### Goal

1. Each ontology lives with the specifications in `docs/`, as a folder with its `ontology.toml` and a reader-oriented `ontology.md`, analogous to `docs/Example Actors/` and `docs/Example Contracts/`.
2. Syspilot's own ontology moves from `.syspilot/ontology.toml` to `docs/Syspilot Ontology/ontology.toml`; `docs/conf.py` reads it from there, and the page generated today as `docs/ontology-reference.md` becomes `docs/Syspilot Ontology/ontology.md`. Syspilot's repository then has no `.syspilot/` folder.
3. A new `docs/Example Ontology/` provides a general-purpose ontology for adopting projects with the types `root`, `story`, `req`, `design`, `ac`, `vc`, and `doc`, and a hand-written `ontology.md`. `design` is the detailed-design level below `req`; it exists only in the Example Ontology.
4. When the target project has no ontology, Setup copies `docs/Example Ontology/` to `docs/{Project} Ontology/`, replacing `Example` by the project name as it does for Actors and Contracts, and points the generated `conf.py` to it. It no longer copies Syspilot's own ontology.
5. Each `ontology.md` shows a Mermaid diagram of its types and the links between them: Syspilot's generated page and the Example Ontology's hand-written page. The User's uncommitted draft in `docs/Example Ontology/ontology.md` (2026-11-16) is the target form, as the User confirmed; the Technical Writer adopts and commits it.

### Value

A training run showed that Syspilot's own ontology is too thin as a starting point for other projects: it has no design level between requirements and realization. A separate example ontology gives adopting projects a fuller starting point without changing Syspilot's own specification model. Keeping ontologies next to the specifications they type makes them visible to readers and consistent with the other seeded examples.

### Scope

- `docs/conf.py`: `needs_from_toml` and the reference-page hook use the new location; the hook writes `docs/Syspilot Ontology/ontology.md`.
- New `docs/Syspilot Ontology/` and `docs/Example Ontology/`, each with `ontology.toml` and `ontology.md`, and their navigation entries.
- The Example Ontology keeps `root` as the graph anchor that stories trace to, so orphan detection and impact analysis start from one node, and links `design` to the `req` it details. The Architect defines the complete link set.
- Setup (`docs/Syspilot Contracts/setup.md`) and its requirements: the no-ontology fallback copies the Example Ontology into `docs/{Project} Ontology/`; an existing project ontology stays unchanged. In installed projects `.syspilot/` keeps only Syspilot's own records, `project.toml` and the Setup record.
- Skill `syspilot.ontology` refers to the active ontology bound by `needs_from_toml` instead of `.syspilot/ontology.toml` and Syspilot's type list, because it ships to projects that use the Example Ontology.
- Skills `syspilot.impact-python`, `syspilot.mece`, `syspilot.trace` already resolve the ontology through `needs_from_toml`; they change only if verification against the Example Ontology shows a need.
- All current references to `.syspilot/ontology.toml` in requirements, `docs/operations.md`, `.gitignore`, and tests. Archived Change Contracts and release notes stay unchanged.
- Link diagrams (Goal 5): Syspilot's `ontology.md` is generated by the `docs/conf.py` hook, so its diagram is generated from `ontology.toml`. The Example Ontology's page is hand-written; the Setup-generated `conf.py` loads only `myst_parser` and `sphinx_needs`, so the Architect decides how the diagram renders in an installed project (for example adding the Mermaid extension to Setup, or accepting a code block).
- Out of scope: link requiredness or cardinality checks (separate next Change `ontology-link-obligations`); changing Syspilot's own types and links; moving `project.toml` or the Setup record; an update process; delivering a reference generator to installed projects (decided against in #7).
- Crew: Architect, Technical Writer, Developer, Tester, Quality.

### Observable Outcome

- Syspilot's strict documentation build passes with the ontology read from `docs/Syspilot Ontology/ontology.toml`, and no `.syspilot/` folder remains in the repository.
- `docs/Example Ontology/ontology.toml` builds strictly clean in a sample project containing at least one Need of every type and every link.
- The Setup acceptance test of a target without ontology produces `docs/{Project} Ontology/` from the Example Ontology, and the generated `conf.py` binds it; a target with its own ontology keeps it unchanged.
- Impact, MECE, and Trace run against that installed Example Ontology.
- Both `ontology.md` pages render a link diagram in Syspilot's strict build; Syspilot's diagram matches the links of its `ontology.toml`, and the installed Example Ontology page builds strictly clean with the rendering the Architect chose.
- The full test suite passes.

## Artifacts, Ownership And Process Gates

**Applicability:** Each artifact owner decides and updates its own row.<br>
**Scope change:** When the approved intent widens after a row reached a terminal status, `Intent and outcome` returns to `draft` until it is approved again, and each owner whose terminal row the wider intent may affect reassesses it: the owner sets the row back to `pending` or records in the row why its evidence still holds.<br>
**Ownership:** The `Owner` column of this table is the only statement of artifact and gate ownership in the Contract; section headings name no artifact owner.<br>
**Status:** pending

| Artifact or gate | Included | Owner | Completion evidence | Status |
|---|---|---|---|---|
| Intent and outcome | yes | Project Manager | Goal, value, scope, and observable outcome are explicit and approved | approved |
| Contract release | yes | User | User released the Contract on 2026-11-15 00:42 by answering "ok" in the Project Manager chat to the request to release it | approved |
| Version control | yes | Project Manager | Feature branch `feature/ontology-example`; squash-integrated into `development` at closure | active |
| Infrastructure impact | not applicable: no workflow, CI, or packaging artifact references the ontology path or the example folders | Admin | Affected workflow, CI, and packaging artifacts are updated, confirmed by their current owner rather than inferred from a Needs-only impact query | not applicable |
| Product specification and architecture decisions | yes | Architect | Example Ontology types and links defined in `docs/Example Ontology/ontology.toml`; changed requirements and VCs for location, Setup fallback, and skill are linked and checked | approved |
| User-facing documentation | yes | Technical Writer | User validation revision implemented in 11ded97: Example diagram has one node per type and `req` self-edge; Architect confirmed semantics and aligned specification at cd81d0d. Strict build clean; 27 targeted tests pass after alignment | complete |
| Example sync | yes | Technical Writer | Example diagram unified with Syspilot's type-level convention; 27 targeted tests and strict build pass. Actor and Contract examples unchanged, so their earlier evidence remains valid | complete |
| Implementation and unit verification | yes | Developer | `conf.py`, file moves, Setup runbook, `syspilot.ontology` skill, `.gitignore`, and tests changed; unit test commands and results recorded | complete |
| Acceptance test design and results | yes | Tester | Setup with and without existing ontology, strict build of the Example Ontology with every type and link, and Impact/MECE/Trace on it; commands and results recorded | complete |
| Quality review | yes | Quality | Quality reviewed the recorded commands and results; current verification judgment is `proceed` and no open quality issue remains | complete |
| User validation and approval | yes | User | User accepted the outcome on 2026-11-16 22:17 at `5a7b601`, after one changes-requested round on the Example diagram | accepted |
| Closure decision | yes | Project Manager | Final outcome, validation disposition, and integration state are recorded | pending |

## Architecture And Specification

**Status:** approved

### Affected Artifacts

| Artifact | Change | Rationale |
|---|---|---|
| `docs/Example Ontology/ontology.toml` | add | Seven types (`root`, `story`, `req`, `design`, `ac`, `vc`, `doc`) and seven links; `design` links to `req` through the new `details` link, and `verifies` may target `req` or `design`. Options, statuses, and `[needs]` settings copy Syspilot's ontology, so the scaffold, its `needs.deprecated` suppression, and the Impact, MECE, and Trace skills need no change. |
| SYSP_REQ_EXAMPLE_ONTOLOGY, SYSP_VC_EXAMPLE_ONTOLOGY_1 to 3 (`req_examples.rst`) | add | Specifies the Example Ontology; implements SYSP_US_EXAMPLES, which now names the ontology, with new SYSP_AC_EXAMPLES_4 |
| SYSP_REQ_ONTOLOGY_LOCATION, SYSP_VC_ONTOLOGY_LOCATION_1 and 2 (`req_ontology_management.rst`) | add | Specifies the `docs/<Name> Ontology/` layout, Syspilot's binding, the generated `ontology.md`, and no `.syspilot/` in the repository |
| SYSP_REQ_ONTOLOGY_SCHEMA, SYSP_VC_ONTOLOGY_SCHEMA_1, SYSP_REQ_ONTOLOGY_EDITING, SYSP_VC_ONTOLOGY_EDITING_1 | modify | Skill explains the active ontology bound by `needs_from_toml`, not a fixed path or type list; Setup installs the Example Ontology |
| SYSP_REQ_SETUP_ONTOLOGY, SYSP_VC_SETUP_ONTOLOGY_1, SYSP_REQ_SETUP_DOCS, SYSP_REQ_SETUP_NAMING (`req_setup.rst`) | modify | No-ontology fallback copies the Example Ontology to `docs/<Project name> Ontology/`; the generated root lists its page; Syspilot's generated reference page stays uninstalled |

### Decisions And Evidence

| Decision or check | Evidence |
|---|---|
| The design link is named `details` (design to req), because `implements` already means req to story and `specializes` req to req; a third meaning would blur both. A `design` Need that details no requirement is found by Trace. | `docs/Example Ontology/ontology.toml` |
| `verifies` stays one link kind with targets `req` or `design`; a second kind would double the VC vocabulary for no extra traversal. | `docs/Example Ontology/ontology.toml` |
| Seeded files stay byte-identical (SYSP_REQ_SETUP_NAMING): only the folder name carries the project name, so `ontology.md` must hold under any folder name. | SYSP_VC_EXAMPLE_ONTOLOGY_3 |
| Open, Developer decides: whether `.gitignore` keeps its `.syspilot/` ignore line; the requirement fixes only that the repository has no `.syspilot/ontology.toml`. | SYSP_VC_ONTOLOGY_LOCATION_1 |
| Strict documentation build with the new requirements, ontology still at the old location | `python docs/docs-build.py clean` succeeded |
| Goal 5, rendering: the installed page uses a `{mermaid}` directive block, as `docs/branching.md` does, and Setup's generated `conf.py` loads `sphinxcontrib.mermaid`, which the installed `docs/requirements.txt` already supplies. A plain `mermaid` fence needs no extension but fails the strict build with a Pygments warning (observed on the draft), and the alternative of a plain code block shows no diagram. | SYSP_VC_SETUP_DOCS_5, SYSP_VC_EXAMPLE_ONTOLOGY_3; Setup runbook and scaffold are Developer work |
| Goal 5, Syspilot's generated diagram: node types come from `[[needs.types]]`, but `[[needs.extra_links]]` names no endpoint types, so edges come from new descriptive `[[syspilot.diagram_edges]]` entries (`link`, `from`, `to`) in `docs/Syspilot Ontology/ontology.toml`. They constrain and validate nothing. Alternative rejected: deriving edges from a previous build's `needs.json`, which is stale and not reproducible. USER REVIEW REQUIRED: this adds endpoint data to the ontology file; `ontology-link-obligations` may replace it with real link rules, and removing the entries is cheap. | SYSP_REQ_ONTOLOGY_LOCATION, SYSP_VC_ONTOLOGY_LOCATION_3 |

## User-Facing Documentation

**Status:** complete

### Documentation Plan And Ownership

| Documentation surface | `doc` Need | Requirements included | Status |
|---|---|---|---|
| `docs/Example Ontology/ontology.md` | SYSP_DOC_EXAMPLE_ONTOLOGY, `realized_by` that path | SYSP_REQ_EXAMPLE_ONTOLOGY, SYSP_REQ_SETUP_ONTOLOGY | implemented |
| `docs/customization.md`, `docs/getting-started.md`, `docs/upgrade.md` | SYSP_DOC_CUSTOMIZATION, SYSP_DOC_GETTING_STARTED, SYSP_DOC_UPGRADE | `includes` extended by SYSP_REQ_ONTOLOGY_LOCATION and SYSP_REQ_EXAMPLE_ONTOLOGY where the guide now states them | verified |
| `docs/operations.md`, `docs/methodology.md`, `docs/index.rst` | SYSP_DOC_OPERATIONS, SYSP_DOC_METHODOLOGY, SYSP_DOC_PORTAL | unchanged `includes`; wording and navigation only | verified |
| `docs/Syspilot Ontology/ontology.md` | none: generated by the build and untracked, so not a hand-maintained surface | SYSP_REQ_ONTOLOGY_LOCATION | not applicable |

### Consultations And Factual Reviews

| Documentation surface | Consulted artifact owner | Review question | Evidence and disposition |
|---|---|---|---|
| `docs/Example Ontology/ontology.md` and the guide edits | Architect | Is this accurate and understandable for the intended user? | Architect consulted 2026-11-15, reviewed a68409c: accurate; corrected the `design` placement wording in `customization.md`, replaced the ambiguous chain diagram with one line per link, and dropped the unverified type-prefix sentence. Remaining Developer-owned parts are realized outside this review |
| Goal 5: authorized Example Ontology diagram | Architect | Does the two-instance requirement illustration agree with the new one-node-per-type wording? | Architect confirmed the approved draft and all nine drawn edges; 4893ca1 permits repeated types to illustrate specialization on the Example page. Generated Syspilot diagram keeps one node per type. Getting Started's extension list follows SYSP_REQ_SETUP_DOCS; implementation verification remains with Developer |
| User validation revision, 2026-11-16 | Architect | Does the unified type-level diagram preserve all link semantics? | Confirmed 11ded97: seven type nodes, eight edges equal the link table; `specializes` retains concrete-to-general semantics. Specification aligned at cd81d0d to require one node per type and the self-edge, replacing the earlier two-instance allowance. All 27 targeted tests rerun successfully after alignment |

### Changed Documentation And Verification

| Artifact | Change | Verification evidence |
|---|---|---|
| `docs/Example Ontology/ontology.md` | New: chain, types, links, options, statuses; no Needs markup, no source folder name | Strict clean build succeeded (2026-11-15) |
| Goal 5: `docs/Example Ontology/ontology.md`, `docs/getting-started.md` | Adopted the User-authorized diagram with the `{mermaid}` directive; Getting Started names MyST, Sphinx-Needs and Mermaid for the specified Setup scaffold | `uv run python docs\docs-build.py clean` succeeded with zero warnings, and `git diff --check` passed (2026-11-16). Generated Syspilot diagram and Setup scaffold remain Developer work |
| User validation revision: `docs/Example Ontology/ontology.md` | Removed the General Requirement instance, its duplicate `implements` edge, and the two-node explanation; `specializes` now returns to the `req` type as on Syspilot's page | `uv run python -m unittest discover -s tests -p test_acceptance_ontology_example.py`: 27 tests pass; `uv run python docs\docs-build.py clean`: zero warnings; `git diff --check`: pass (2026-11-16) |
| `docs/syspilot/documentation/index.rst` | New SYSP_DOC_EXAMPLE_ONTOLOGY; `includes` of customization, getting-started and upgrade extended | as above |
| `docs/index.rst` | Toctree entry `Example Ontology/ontology` | as above |
| `docs/customization.md`, `docs/getting-started.md`, `docs/upgrade.md`, `docs/operations.md`, `docs/methodology.md` | Ontology location `docs/<Name> Ontology/`, Setup fallback to the Example Ontology, no `.syspilot/ontology.toml` | as above; `docs/test_docs_build.py` OK |
| Left for the Developer | `docs/index.rst` entry `ontology-reference` and the `ontology-reference.md` link in `docs/namingconventions.md` change with the move of the generated page; both resolve today and break if changed before it | Developer's move of the generated page updates both; the strict build proves it |

## Example Sync

**Status:** complete

| Artifact | Change | Verification evidence |
|---|---|---|
| `docs/Example Actors/`, `docs/Example Contracts/` | No change: they never name an ontology path, and the Change template's optional `Ontology Binding` subsection already assumes `doc` Needs and typed links, which the Example Ontology provides | Search for ontology paths in both folders found none; strict clean build succeeded |
| `docs/Syspilot Contracts/change.md`, `docs/Syspilot Actors/Technical Writer.md` | `Example sync` row and role card name `docs/Example Ontology/` beside the Actor and Contract folders (SYSP_REQ_CHANGE_CONTRACT, SYSP_REQ_TECHNICAL_WRITER, 5698f4e) | Strict clean build; Architect's review |
| `docs/Example Contracts/change.md`, `docs/Example Actors/Technical Writer.md` | No change: the example Change template carries no `Example sync` row, and the example card is a declared deviation without the example-maintenance duty | Read both files |
| `docs/Example Ontology/` | Carried as the new example folder above | as above |
| Goal 5 reassessment | Actor and Contract examples remain unaffected; the Example Ontology now includes the approved diagram | Strict clean build passed; Architect confirmed the two requirement instances and all nine drawn edges against 4893ca1 |
| User validation revision | Example Ontology diagram now uses the same type-level convention as Syspilot; Actor and Contract examples remain unaffected | 27 acceptance tests and strict clean build pass; earlier two-instance evidence is superseded by this revision |

The Architect confirmed the gap and fixed the specification side at 5698f4e.

## Implementation And Unit Verification

**Status:** complete

### Decisions And Evidence

| Decision | Chosen approach | Relevant alternatives | Rationale and evidence |
|---|---|---|---|
| `.gitignore` and `.syspilot/` | Keep the `.syspilot/` ignore line, drop the `!.syspilot/ontology.toml` exception, ignore `docs/Syspilot Ontology/ontology.md` | Remove the `.syspilot/` line too | The folder is gone from the repository, but Setup of a dogfooding run recreates `.syspilot/` records that must not be committed; the generated page is untracked, as `ontology-reference.md` was |
| Binding in `docs/conf.py` | `needs_from_toml = "Syspilot Ontology/ontology.toml"`, relative to `conf.py`; the reference hook reads the same folder and writes `ontology.md` beside it | Computed path | Literal binding is what the Impact, MECE, and Trace skills read; `docs/ontology-reference.md` left untracked by an earlier build is an orphan and fails the strict build, so it was deleted |

### Changed Artifacts And Verification

| Artifact | Change | Verification evidence |
|---|---|---|
| `.syspilot/ontology.toml` to `docs/Syspilot Ontology/ontology.toml` | Moved with `git mv`; no `.syspilot/` folder remains | `python docs/docs-build.py clean`: exit 0, "Documentation built successfully", schema validation 0 warnings |
| `docs/conf.py`, `docs/index.rst`, `docs/namingconventions.md`, `docs/syspilot/index.rst`, `docs/traceability/index.rst` | Binding, hook, toctree entry `Syspilot Ontology/ontology`, and links follow the moved page | as above |
| `docs/Syspilot Contracts/setup.md` | Fallback copies `docs/Example Ontology/` to `docs/<Project name> Ontology/` and binds it; scaffold index lists `<Project name> Ontology/ontology`; no Syspilot-owned ontology copied | `tests/test_setup_contract_feedback.py`, `tests/test_acceptance_setup_feedback_2.py` |
| `.github/skills/syspilot.ontology/SKILL.md` | Reads the ontology bound by `needs_from_toml`; type, status, option, and link names come from the active file | Read against SYSP_VC_ONTOLOGY_SCHEMA_1 |
| `.gitignore`, tests | Paths follow the move; scaffold tests copy the Example Ontology folder into the generated target and build it strictly | `python -m unittest discover -s tests`: 202 tests OK; `python docs/test_docs_build.py`: 4 tests OK |
| Goal 5: `docs/conf.py`, `docs/Syspilot Ontology/ontology.toml` | Hook writes a `{mermaid}` link diagram into the generated page: one node per configured type, one edge per new descriptive `[[syspilot.diagram_edges]]` entry (6 entries; equal to the 6 (type, link, type) triples observed in the built needs.json) | `python docs/docs-build.py clean` exit 0, zero warnings; `tests/test_acceptance_ontology_example.py` gains a diagram test (23 OK) |
| Goal 5: `docs/Syspilot Contracts/setup.md`, tests | Scaffold `extensions` adds `sphinxcontrib.mermaid`; Setup offers it as an additive edit for existing builds; sample-project and scaffold tests load it | `python -m unittest discover -s tests`: 225 tests, the only failure was a Tester page test that forbade the `{mermaid}` fence, relaxed to allow it; module re-run OK |

## Acceptance Testing

**Status:** complete

Tests: `tests/test_acceptance_ontology_example.py` (27 tests). Commands: `python -m unittest tests.test_acceptance_ontology_example`, `python -m unittest discover -s tests` (229 tests OK), `python docs/docs-build.py clean` (exit 0). Reassessed for Goal 5 at 70c12b8: earlier rows stand; their evidence is rerun and the rows below are added.

| Scenario | Traces to | Result | Evidence |
|---|---|---|---|
| Example Ontology defines exactly 7 types and 7 links; statuses, options, and settings equal Syspilot's; `design` and `details` exist only there | SYSP_VC_EXAMPLE_ONTOLOGY_1 | pass | `ExampleOntologyDefinitionTests` |
| `ontology.md` names every type and link, has no Needs markup, no `Example` or `Syspilot` folder name; folder holds exactly the two files | SYSP_VC_EXAMPLE_ONTOLOGY_3 | pass | `ExampleOntologyDefinitionTests` |
| Sample project with every type and link, ontology copied under `Acme Ontology`, builds with `-W` and zero warnings; built Needs hold all types and links | SYSP_VC_EXAMPLE_ONTOLOGY_2, Observable Outcome 2 | pass | `SampleProjectTests` |
| Trace (depth 3) reaches all 9 Needs over all 7 links, all resolved; Impact shows `details` and `verifies` to a design; MECE pairs VCs of requirement and design | SYSP_VC_EXAMPLE_ONTOLOGY_2, Observable Outcome 4 | pass | `SampleProjectTests` |
| A skill installed in the sample project resolves the ontology from the literal binding with no `--ontology` argument | SYSP_REQ_EXAMPLE_ONTOLOGY (skills work unchanged) | pass | `SampleProjectTests`; skills resolve the default from their own location, so a copy outside the project reads that project's ontology |
| Negative controls: unknown type fails the build; Syspilot's ontology cannot carry the sample; a dangling `details` is reported unresolved | SYSP_VC_EXAMPLE_ONTOLOGY_2 | pass | `SampleProjectNegativeControls` |
| Syspilot binds the literal new path; no `.syspilot/` folder and no tracked old files; generated page ignored and lists every type; no live artifact names `.syspilot/ontology.toml`; skill names no fixed path | SYSP_VC_ONTOLOGY_LOCATION_1 and _2, Observable Outcome 1 | pass | `SyspilotBindingTests`; the page check skips when the page is not built, and ran after the strict build |
| Setup without ontology: Example folder copied to the project-named folder, byte-identical, no Syspilot ontology, generated `conf.py` binds it; with ontology: preserved | SYSP_VC_SETUP_ONTOLOGY_1, Observable Outcome 3 | pass | `SetupOntologyTests` (Contract text and seeded-copy comparison); scaffold builds in `test_acceptance_setup_feedback_2.py` |
| Example page diagram is a `{mermaid}` directive with exactly one node per type (node id equals type) and `req -->|specializes| req`; edges equal the 8 endpoint pairs of the link table; a duplicated type node or a changed specialization edge fails the test | SYSP_VC_EXAMPLE_ONTOLOGY_3, Goal 5 | pass | `ExampleOntologyDefinitionTests`; re-recorded at the unified diagram of 11ded97/cd81d0d, 27 tests, suite 229 OK, strict build clean |
| Syspilot's generated diagram: one node per type, one edge per `diagram_edges` entry, every link has an edge, and the (type, link, type) triples of the built `needs.json` equal the declared edges | SYSP_VC_ONTOLOGY_LOCATION_3, Goal 5 | pass | `SyspilotBindingTests`; the triple check skips without a built `needs.json` and ran after the strict build |
| Installed Example page with `{mermaid}` builds strictly in a sample project and in every scaffold selection; without the extension the build fails; scaffold loads and requirements supply `sphinxcontrib.mermaid`; existing builds get it only as an approved additive edit | SYSP_VC_SETUP_DOCS_5, Observable Outcome 2 | pass | `SampleProjectTests`, `SampleProjectNegativeControls`, `SetupOntologyTests`, `test_acceptance_setup_feedback_2.py` |

Mutation check: breaking the link name, the page text, the `conf.py` binding, Setup's fallback sentence, and the skill's binding reference each fails the suite. For Goal 5, removing a drawn edge, changing the fence to a plain one, altering a `diagram_edges` entry, removing Setup's additive-edit sentence, and removing the requirements entry each fails it. Untested: rendering of the diagram in a browser (the build proves the directive, not the picture); Setup's run-time copy in a live target (text-level, as in earlier Changes); `.gitignore` effect on a dogfooding Setup run.

## Quality Review

**Status:** complete

**Current judgment:** `proceed` (re-reviewed at 1ca4dd1 after the User's validation revision). The unified type-level Example diagram, the aligned requirement, the re-recorded acceptance row and the stricter test (one node per type, specialization edge) agree; Quality re-ran the acceptance module (27 OK) and the Tester recorded suite 229 OK and a clean strict build. Residual limit: browser rendering is untested.

### Applied Review Methods

| Method | Selected scope | Evidence | Findings | Limits |
|---|---|---|---|---|
| Recorded-result review | Developer and Tester evidence; diff 9a0ea85..a1b99b9 of specs, `conf.py`, `ontology.toml`, Setup, Example page, tests | Read diff against Goal 5 and VCs; checked that drawn edges equal the link table (8 pairs, 9 edges with the specialization instance) and that `diagram_edges` are descriptive only; no check re-run, recorded results sufficed | Wording defects in the two Setup sentences and the `SYSP_REQ_EXAMPLE_ONTOLOGY` bullet; control characters in the Developer's Goal 5 rows; handover row times | Browser rendering of the diagram untested (build proves the directive only); Setup run-time copy tested at text level |
| Re-review of the User revision | `docs/Example Ontology/ontology.md`, `req_examples.rst`, Contract rows; diff de56905..deea883 | Read the diff; Example diagram now has 7 type nodes and 8 edges with `req -->|specializes| req`, matching Syspilot's convention and the requirement; Quality re-ran `python -m unittest tests.test_acceptance_ontology_example`: 27 OK | Stale acceptance row and test comment; test does not assert one node per type | Strict build not re-run; Technical Writer recorded it clean |
| MECE (`syspilot.mece`, same-document) | SYSP_REQ_EXAMPLE_ONTOLOGY (peer SYSP_REQ_EXAMPLES); SYSP_REQ_ONTOLOGY_LOCATION (peers EDITING, SCHEMA); SYSP_REQ_SETUP_DOCS (20 Setup peers); needs data built 21:35 | Script findings: none for all three. Read: the Mermaid obligation sits in SETUP_DOCS (extension), EXAMPLE_ONTOLOGY (page diagram) and ONTOLOGY_LOCATION (generated diagram) without overlap or contradiction | none beyond the wording defects above | `semantic-content-review-required` and `structured-coverage-data-unavailable` remain; semantic review is the one recorded here |
| Trace (`syspilot.trace`, both, depth 2) | Same three requirements | Neighborhoods resolve; VCs `SYSP_VC_ONTOLOGY_LOCATION_3`, `SYSP_VC_SETUP_DOCS_5` and `SYSP_AC_EXAMPLES_4` link to their requirement and story; no unresolved target observed | no finding | Edge semantics outside the changed links not individually re-read |

Verification is fully automated. Quality reviews the commands and results that the Developer and the Tester recorded, and executes a check itself only when a recorded result cannot support its judgment, recording the reason in the table above. A Markdown process artifact whose content has no automated check is verified by Quality's review, and the table above records that review and its limits.

Quality communicates its `proceed` judgment and supporting evidence directly to the Project Manager before the Project Manager presents the verified outcome for validation. Another actor's forwarded claim does not establish Quality's decision.

### Open Quality Issues

Keep this table synchronized with currently open issues. A missing automation is an open issue whose row names the task that closes it, the owner of that task, and the completion evidence. For each issue, Quality transfers current responsibility to the owner of the affected artifact. When Quality confirms the required outcome, update the affected artifact or evidence and remove the resolved row. At closure this table contains `None`.

| Artifact | Current issue | Required outcome |
|---|---|---|
| None | | |

Resolved: the four issues of the first review (2774375) and the Tester's row and test after the User revision (1ca4dd1; Quality re-ran the module, 27 OK, and read the stricter assertions). Not a quality issue: the Architect's 21:42 handover row is later than its commit (21:37); the Project Manager may correct it at closure.

## User Validation And Approval

**Recorded by:** Project Manager<br>
**Status:** accepted

Quality's `proceed` judgment verifies that the change is ready for validation; it does not validate user value. For an included validation, the Project Manager presents the observable outcome after receiving Quality's direct judgment and evidence. The User communicates the validation decision directly to the Project Manager, who records the decision and evidence. Another actor's forwarded claim does not establish the User's decision. If the user requests changes, the Project Manager transfers responsibility to an included artifact owner that can produce the required outcome.

Current responsibility remains with the User from Quality's handoff until the validation decision is recorded. The Project Manager's presentation and recording duties support that User-owned artifact; they do not make the Project Manager the validation owner or an intermediate responsibility relay.

Set this artifact to `not applicable` only when the User explicitly delegates validation of the finished outcome and that delegation is recorded in its artifact row. Operation mode does not delegate validation. In unattended mode, keep it `pending` until the User returns.

**Decision and evidence:** Accepted by the User directly to the Project Manager on 2026-11-16 22:17 after reviewing the revised rendered Example page at `5a7b601` ("accepted"). The User noted that the Markdown preview looks nicer than the HTML rendering and does not require a change. An earlier round on 2026-11-16 21:48 requested the type-level Example diagram (one node per type, `req -->|specializes| req`, no two-node explanation); that revision is implemented and verified.

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
