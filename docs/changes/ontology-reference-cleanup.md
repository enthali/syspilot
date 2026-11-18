# Change Contract: ontology-reference-cleanup

**Status:** active<br>
**Process owner:** Project Manager<br>
**Current responsibility:** Project Manager<br>
**Current blocker:** none<br>
**Created:** 2026-11-18<br>
- **Operation Mode**: autonomous, agreed with the User on 2026-11-18.

- **autonomous** - every actor decides on its own; when genuinely unsure, it asks the user directly and pauses only its own step until answered.

## Handover log

Owned by: Project Manager

The handing-over actor appends one line as the last act before handing over, in the same commit that changes `Current responsibility`, taking `Date` as `YYYY-MM-DD` and `Time` as `HH:MM` in 24-hour local time from the system clock at that moment.

| Date | Time | From | To | Note |
|--|--|--|--|--|
| 2026-11-18 | 19:14 | Project Manager | Architect | User released the Contract in autonomous mode; finalize the tracked-page specification, disposition every impact candidate, and resolve the generator metadata boundary. |
| 2026-11-18 | 19:15 | Architect | Developer | Requirements and VCs for the tracked page are specified, impact candidates dispositioned, and the `diagram_edges` consumers named; remove generator and metadata, write the page, move the tests. |
| 2026-11-18 | 19:21 | Developer | Technical Writer | Generator, metadata and ignore rule removed, tracked page written, tests moved; one local-only test failure from .syspilot/stats is flagged for Architect or Tester. |
| 2026-11-18 | 19:26 | Technical Writer | Tester | Live reference claims and documentation map updated; Architect and Developer reviewed, strict build and 260 tests pass. |
| 2026-11-18 | 19:30 | Tester | Quality | 8 acceptance tests, mutation-checked, strict build leaves the page unchanged, suite 268 OK; no findings. |
| 2026-11-18 | 19:34 | Quality | Admin | Review `revise`: only the Infrastructure impact row is open; everything else re-verified. Hand back to Quality after you record it. |
| 2026-11-18 | 19:34 | Admin | Quality | Source archive includes the tracked reference; Setup retains the Example ontology boundary and release workflow needs no change. |
| 2026-11-18 | 19:35 | Quality | User | Review `proceed`; Infrastructure impact recorded, all results re-verified, no open quality issue. Validation is yours; the Project Manager presents the outcome. |
| 2026-11-18 | 19:37 | User | Project Manager | User accepted the outcome after Quality's `proceed`; integration and closure follow. |

## Intent And Outcome

**Status:** approved<br>
**Approval evidence:** The User asked the Project Manager to create this Contract on 2026-11-18 after reviewing the proposed cleanup boundary, agreed to autonomous mode, and released it with "ok go ahead".

### Goal

Syspilot no longer generates its own reader-oriented ontology reference at Sphinx build time. `docs/Syspilot Ontology/ontology.md` becomes a tracked, hand-maintained page beside `ontology.toml`, with the same artifact model as the Example Ontology and other installed-project ontologies.

### Value

The current build-time generator gives Syspilot a private ontology path that differs from the Example Ontology and every installed project. Removing it reduces special behavior in `docs/conf.py`, makes the reader page reviewable in version control, and leaves Setup's selected-ontology boundary explicit: Setup installs a seeded ontology page but never installs or creates an automatic reference generator.

### Scope

- Replace the ignored, generated `docs/Syspilot Ontology/ontology.md` with a tracked reader-oriented page that covers Syspilot's configured Need types and named links.
- Remove the ontology-reference generator, hook and now-unused imports from `docs/conf.py`.
- Remove the generator-only `[[syspilot.diagram_edges]]` metadata from `docs/Syspilot Ontology/ontology.toml`; real endpoint obligations remain in the ontology.
- Remove the ontology page from the generated-file ignore rules and keep all navigation links pointed at the same path.
- Change `SYSP_REQ_ONTOLOGY_LOCATION` and its VCs so Syspilot's own page is tracked and maintained rather than generated.
- Update user-facing and Setup wording that calls Syspilot's page generated or describes it as an automatic build artifact.
- Add focused verification that the tracked page remains aligned with the configured types and links and that the build no longer writes it.
- Keep installed-project Setup behavior unchanged: it seeds `docs/Example Ontology/` only when no ontology exists, and it does not install or generate a Syspilot-specific reference capability.
- Out of scope: historical Change Contracts and historical Release Notes; ontology semantics, link obligations, Setup selection rules, and generated reference delivery to installed projects; redesigning the optional project-owned ontology reference workflow.
- Crew: Architect, Developer, Technical Writer, Tester, Quality, Admin.

### Observable Outcome

- A tracked `docs/Syspilot Ontology/ontology.md` exists, is visible in navigation, and describes every configured Need type and named link.
- `docs/conf.py` contains no ontology-reference generation hook and does not write the page during a strict build.
- Generator-only `diagram_edges` metadata and the matching ignore rule are removed.
- Requirements, VCs, Setup/product documentation and focused tests agree that Syspilot's page is hand-maintained and installed projects receive no automatic generator.
- The strict documentation build and the full test suite pass with zero warnings.

## Artifacts, Ownership And Process Gates

**Applicability:** Each artifact owner decides and updates its own row.<br>
**Scope change:** When the approved intent widens after a row reached a terminal status, `Intent and outcome` returns to `draft` until it is approved again, and each affected terminal row is reassessed by its owner.<br>
**Ownership:** The `Owner` column is the only statement of artifact and gate ownership in this Contract.<br>
**Status:** pending

| Artifact or gate | Included | Owner | Completion evidence | Status |
|---|---|---|---|---|
| Intent and outcome | yes | Project Manager | Goal, value, scope and observable outcome are explicit and approved | approved |
| Contract release | yes | User | The User reviews and authorizes this Contract to start | approved: the User released it in the Project Manager chat on 2026-11-18 with "ok go ahead" |
| Version control | yes | Project Manager | Feature branch `feature/ontology-reference-cleanup`; squash-integrated into `development` at closure | active |
| Infrastructure impact | yes | Admin | Source archive includes the tracked reference and Example page; Setup's selection boundary and existing release workflow remain applicable, as recorded below | complete |
| Product specification and architecture decisions | yes | Architect | Affected Artifacts is sourced from the impact queries, every candidate is dispositioned, and the requirements and VCs define the tracked-page behavior | approved |
| User-facing documentation | yes | Technical Writer | Live generated-reference claims corrected; reference has its own `doc` Need; Architect and Developer factual reviews accepted; strict build and 260 tests pass | complete |
| Example sync | not applicable: the Example Ontology is already hand-maintained and its behavior does not change | Technical Writer | The Architect confirms no Example Ontology change is required | not applicable |
| Implementation and unit verification | yes | Developer | Generator, metadata and ignore rule removed; tracked page and focused tests added; unit results recorded | complete |
| Acceptance test design and results | yes | Tester | Observable outcomes and no-write/no-generator behavior are tested and results recorded | complete |
| Quality review | yes | Quality | Quality reviews the Contract, implementation and evidence and records `proceed` or actionable findings | complete |
| User validation and approval | yes | User | The User validates the finished outcome after Quality's `proceed` judgment | accepted |
| Closure decision | yes | Project Manager | Final outcome, validation disposition and integration state are recorded | pending |

## Architecture And Specification

**Status:** approved

### Affected Artifacts

Built with the project's impact skill. The query output is a candidate list, not complete scope; the Architect gives every reported ID a disposition and adds artifacts that the query cannot report.

Impact query: `get_need_links.py SYSP_REQ_ONTOLOGY_LOCATION --direction both --depth 1 --flat --no-build`; candidates `SYSP_DOC_CUSTOMIZATION`, `SYSP_DOC_UPGRADE`, `SYSP_US_ONTOLOGY_MANAGEMENT`, `SYSP_VC_ONTOLOGY_LOCATION_1`, `_2`, `_3`

Impact query: `get_need_links.py SYSP_REQ_SETUP_DOCS --direction both --depth 1 --flat --no-build`; candidates `SYSP_DOC_GETTING_STARTED`, `SYSP_REQ_SETUP`, `SYSP_US_SETUP`, `SYSP_VC_SETUP_DOCS_1` through `_5`

| Artifact | Change | Rationale |
|---|---|---|
| `SYSP_REQ_ONTOLOGY_LOCATION`, `SYSP_VC_ONTOLOGY_LOCATION_2`, `_3` | modified | Tracked, hand-maintained page; no build-time write; no `diagram_edges`; drift checks by test (`_2` page lists every type and link and stays unchanged by a build, `_3` diagram edges equal the observed triples). |
| `SYSP_VC_ONTOLOGY_LOCATION_1` | no change | Binding and absent old paths are unaffected. |
| `SYSP_REQ_ONTOLOGY_SCHEMA` | modified | Reported by neither query; its guidance sentence about `[[syspilot.diagram_edges]]` feeding a generated diagram is removed. Added by hand. |
| `SYSP_REQ_SETUP_DOCS` | modified | One sentence: Syspilot's own page is neither installed nor generated, instead of "generated ontology reference page". Behavior unchanged. |
| `SYSP_VC_SETUP_DOCS_1` to `_5` | no change | They hold: generated config has no reference hook, Setup installs the Example page. |
| `SYSP_US_ONTOLOGY_MANAGEMENT`, `SYSP_REQ_SETUP`, `SYSP_US_SETUP` | no change | Ownership and installed-project Setup behavior stay the boundary. |
| `SYSP_DOC_CUSTOMIZATION`, `SYSP_DOC_UPGRADE`, `SYSP_DOC_GETTING_STARTED` | no change decided here | A search of current guides found no generated-page claim; the Technical Writer confirms and edits only where a live claim exists. |
| `docs/Syspilot Contracts/setup.md` line on the generated `docs/conf.py` | modified | It calls the Syspilot page "Syspilot's own generated reference"; Developer rewords to "hand-maintained"; the no-hook rule stays. |
| `docs/Example Ontology/` | no change | Confirms the Example sync row: already hand-maintained, behavior unchanged. |
| `docs/conf.py` | modified | Remove the builder hook and generator-only imports. |
| `docs/Syspilot Ontology/ontology.toml` | modified | Remove descriptive `diagram_edges` used only by the deleted generator; preserve Needs types, links and schema obligations. |
| `docs/Syspilot Ontology/ontology.md` | added | Track the reader-oriented type and link reference beside the ontology definition. |
| `.gitignore` | modified | Stop ignoring the now-tracked ontology page. |
| `docs/syspilot/requirements/req_ontology_management.rst` | modified | Replace generated-page requirements and VCs with tracked-page obligations. |
| `tests/test_acceptance_ontology_example.py` | modified | Replace generated-page assertions with tracked-page and no-generator checks. |
| `docs/traceability/index.rst`, `docs/Syspilot Contracts/setup.md`, `docs/releasenotes.md` | inspect | Update only live claims in current product surfaces; historical Change evidence and Release Notes are preserved unless the Technical Writer finds a current contract requiring a change. |
| `docs/index.rst`, `docs/namingconventions.md`, `docs/syspilot/index.rst` | no change proposed | Their links remain valid at the unchanged page path; strict build verifies resolution. |

### Decisions And Evidence

The Architect owns the final decisions. Open design points for the Architect:

| Decision or check | Evidence or question |
|---|---|
| Tracked Syspilot page | Enforceable alignment without generation is tests: the page lists every configured type and link, and its Mermaid edges equal the (type, link, type) triples observed in the built Needs data. The diagram stays on the page, with hand-written edges, because the Change keeps one node per type and the User wanted it on both ontology pages; drift is caught by the triple test. Alternative: drop the diagram; rejected as removing reader value. |
| `diagram_edges` removal | Consumers found by a repository search: `docs/conf.py` (removed with the hook) and `tests/test_acceptance_ontology_example.py` (Developer moves the two diagram checks to read the page). No skill or other document reads them. Removed from the requirements. |
| Historical wording | Historical Contracts and Release Notes stay unchanged; live claims are `docs/Syspilot Contracts/setup.md`, `SYSP_REQ_ONTOLOGY_SCHEMA` and `SYSP_REQ_SETUP_DOCS`. |
| Example sync | Confirmed not applicable: the Example Ontology page is already hand-written and nothing changes there. |

## Infrastructure Impact

**Status:** complete

| Infrastructure artifact | Impact | Evidence and disposition |
|---|---|---|
| Source archive | The hand-maintained Syspilot reference must be present without a build-time generator | At 4350ef7, both ontology pages are tracked, have no `export-ignore` attribute, and appear in `git archive --format=tar HEAD` for their paths. The future tagged release has not yet been published |
| Setup installation | Installed projects continue to preserve an existing ontology or receive the Example Ontology, not Syspilot's own reference | The Setup installation inventory retains this selection and copies seeded directory files from the verified commit; a live Setup run was not performed |
| `.github/workflows/release.yml` | No workflow or packaging change is needed | The unchanged workflow checks out the tracked source, builds documentation strictly, runs the test suite, and publishes the documentation and GitHub Release on a tag. Quality re-ran the strict build and full suite; no release workflow run was performed for this Change |

## User-Facing Documentation

**Status:** complete

### Documentation Plan And Ownership

| Surface | Documentation Need and requirements | Disposition |
|---|---|---|
| `docs/Syspilot Ontology/ontology.md` | New SYSP_DOC_SYSPILOT_ONTOLOGY, `realized_by` that path; includes SYSP_REQ_ONTOLOGY_LOCATION and SYSP_REQ_ONTOLOGY_LINK_OBLIGATIONS | Developer's tracked reader page reviewed; now has an owner-visible documentation surface |
| `docs/customization.md` | SYSP_DOC_CUSTOMIZATION; existing SYSP_REQ_ONTOLOGY_LOCATION link remains applicable | Explains hand maintenance, no build-time writes, drift tests and unchanged Setup boundary |
| `docs/getting-started.md` | SYSP_DOC_GETTING_STARTED; existing SYSP_REQ_SETUP_DOCS link remains applicable | Replaces the live generated-reference claim; explicitly states no installed generator |
| `docs/traceability/index.rst` | Graph navigation rather than an independently maintained guide; links to the reference Need's realized page | Replaces the live generated-catalogue label |

Impact evidence: incoming and outgoing depth-one discovery from SYSP_REQ_ONTOLOGY_LOCATION confirms Customization, Upgrade, its story and three VCs as candidates. Customization gains an explicit explanation; Upgrade already describes a reader page beside the ontology without claiming generation and needs no change. Search of current documentation also finds the Getting Started and Traceability claims outside that candidate set, which are corrected. Historical Change evidence, Release Notes and Field Notes remain unchanged. Operations, navigation and naming links stay accurate at the same path. The Example Ontology is already hand-maintained, so the Example sync disposition remains not applicable.

### Consultations And Factual Reviews

| Surface | Owner consulted | Review question and status |
|---|---|---|
| Reference, Customization, Getting Started and Traceability | Architect | Direct review on 2026-11-18: page matches configured types, links, options, statuses, diagram and required links; reader wording and documentation includes are correct; Example sync confirmed unnecessary |
| Reference, Customization, Getting Started and Traceability | Developer | Direct review on 2026-11-18: implementation fidelity confirmed; Customization clarified that diagram drift comparison requires a prior documentation build because the test otherwise skips |

### Changed Documentation And Verification

| Artifact | Change | Evidence |
|---|---|---|
| `docs/getting-started.md`, `docs/traceability/index.rst` | Removes live generated-page claims | Strict build and both factual reviews pass |
| `docs/customization.md` | Explains tracked-page maintenance and no generator delivery | Strict build and both factual reviews pass; Developer's build-prerequisite clarification adopted |
| `docs/syspilot/documentation/index.rst` | Gives the newly hand-maintained reference its own `doc` Need and impact links | Strict build passes; four targeted reference tests pass |

Verification (2026-11-18): `uv run python docs\docs-build.py clean` succeeds with zero warnings; `git diff --check` passes. After that build, the four methods `test_the_page_is_tracked_not_ignored_and_lists_every_type_and_link`, `test_conf_has_no_hook_that_writes_the_page_and_the_ontology_has_no_diagram_metadata`, `test_the_diagram_has_one_node_per_type_and_only_configured_links_with_each_link_drawn`, and `test_the_diagram_edges_equal_the_observed_type_link_type_triples_of_the_built_graph` under `tests.test_acceptance_ontology_example.SyspilotBindingTests` all pass via `uv run python -m unittest` with those four fully qualified names. Following the Architect's specification correction at bb066bc and Developer's test correction at 6c10be0, `uv run python -m unittest discover -s tests` passes all 260 tests.

The local `.syspilot/stats/` finding is resolved: the requirement permits untracked local state while forbidding an ontology or tracked files there. No local statistics records were removed. The Developer's shared-tree commit 6c10be0 also captured the initial documentation edits; the subsequent writer commits record verification, review and handoff.

## Implementation And Unit Verification

**Status:** complete

### Decisions And Evidence

| Decision | Chosen approach | Relevant alternatives | Rationale and evidence |
|---|---|---|---|
| Content of the tracked page | The Example Ontology page's structure without `design`/`details`: type catalogue, hand-written Mermaid diagram, links, required links, options, statuses. | Keep the generator's short two-table output; drop the diagram. | Same reader model as the Example page; the diagram stays as the Architect decided. |
| Drift protection | Tests read the page: it lists every type and link, has one node per type, every link drawn, and its edges equal the observed triples of the built `needs.json` (skipped until a build exists). | Generate the page again. | Matches `SYSP_VC_ONTOLOGY_LOCATION_2` and `_3`. |
| Imports in `docs/conf.py` | Only `tomllib`, used by the generator alone, was removed; `os` and `sys` were already unused and are left alone. | Remove them too. | Unrelated to this Change. |
| Resolved local-state finding | The original test rejected `.syspilot/stats/`. Architect corrected the requirement at bb066bc to allow untracked local state, and Developer aligned the test at 6c10be0. | Delete valid local statistics; require the folder to be absent. | Developer directly authorized this result update; Technical Writer verified the corrected full suite passes all 260 tests without deleting local records. |

### Changed Artifacts And Verification

| Artifact | Change | Verification evidence |
|---|---|---|
| `docs/conf.py` | generator, `setup()` hook and `tomllib` import removed | `python docs/docs-build.py clean`: OK, no warnings; the tracked page is unchanged by the build (`git status` shows no modification) |
| `docs/Syspilot Ontology/ontology.toml` | `[[syspilot.diagram_edges]]` removed; types, links, warnings and schemas untouched | strict build OK; tests above |
| `docs/Syspilot Ontology/ontology.md` | now tracked and hand-written | tests above |
| `.gitignore` | ontology page rule removed | `git check-ignore` reports the page not ignored (test) |
| `docs/Syspilot Contracts/setup.md` | "generated reference" reworded to "hand-maintained reference" | strict build OK |
| `tests/test_acceptance_ontology_example.py` | generated-page tests replaced by four tracked-page tests; local-state assertion aligned with Architect's correction | Initial runs had one local-state failure. After 6c10be0, Developer reports 32/32 ontology tests pass; Technical Writer independently ran `uv run python -m unittest discover -s tests`: 260 tests pass |

## Acceptance Testing

**Status:** complete

Run: `python -m unittest tests.test_acceptance_ontology_reference_cleanup` (8 tests, read independently from `ontology.toml`; each assertion mutation-checked on a changed page, conf, ontology or Setup text and fails).

| Scenario | Traces to | Result | Evidence |
|---|---|---|---|
| Every type with title and prefix, every link, option and status is on the page; the page lists no undefined type; every diagram edge uses a configured link between configured types | SYSP_REQ_ONTOLOGY_LOCATION, SYSP_VC_ONTOLOGY_LOCATION_2 | pass | PageMatchesOntologyTests (4) |
| Page tracked and not ignored; `conf.py` has no generation hook or write; no `diagram_edges` in the ontology; Setup text and requirement no longer call the page generated | SYSP_REQ_ONTOLOGY_LOCATION, SYSP_REQ_ONTOLOGY_SCHEMA, SYSP_REQ_SETUP_DOCS | pass | NoGeneratorTests (4) |
| Strict build does not write the page | SYSP_REQ_ONTOLOGY_LOCATION | pass | `python docs/docs-build.py clean` clean; page hash identical before and after, `git status` clean |
| Edges equal observed triples (VC_3) | SYSP_VC_ONTOLOGY_LOCATION_3 | pass | Developer's test in `test_acceptance_ontology_example.py`, rerun in the full suite |

Full suite: 268 tests OK. Untested: rendering of the page in a browser; the Setup text is checked as text, not by a live Setup run.

## Quality Review

**Status:** complete

**Current judgment:** `proceed` at ad61db5 (the earlier `revise` at d570395 is resolved). Tracked page, removed generator, specification, VCs, guides and tests agree and the results hold (strict build clean and the page unchanged by it; full suite 268 OK, re-run by Quality). The Infrastructure impact row is now recorded and complete by the Admin.

### Applied Review Methods

| Method | Selected scope | Evidence | Findings | Limits |
|---|---|---|---|---|
| Recorded-result review | Diff of the Change against `development`: `docs/conf.py`, `ontology.toml`, `.gitignore`, `setup.md`, requirements and VCs, guides, both test files, Contract rows | Read the removed generator against the requirement text; ran `python docs/docs-build.py clean` (success, `git status` clean afterwards) and `python -m unittest discover -s tests` (268 OK); handover stamps do not exceed their commits | Infrastructure impact row pending at d570395, resolved at ad61db5 | Browser rendering of the page and a live Setup run not performed (Tester records this) |
| MECE and Trace (`syspilot.mece` same-document, `syspilot.trace` both depth 2) | SYSP_REQ_ONTOLOGY_LOCATION | Script findings none; no unresolved target | no finding | `semantic-content-review-required` remains |

### Open Quality Issues

| Artifact | Current issue | Required outcome |
|---|---|---|
| None | None | None |

## User Validation And Approval

**Recorded by:** Project Manager<br>
**Status:** accepted

Quality's `proceed` judgment verifies readiness; it does not replace User validation. The Project Manager presents the verified outcome and records the User's decision.

**Decision and evidence:** The User accepted the presented outcome directly in the Project Manager chat on 2026-11-18.

## Closure

**Status:** pending

- [ ] Every included artifact or gate has terminal status and completion evidence.
- [ ] Intent and outcome are `approved`.
- [ ] Quality has recorded a `proceed` judgment.
- [ ] Open Quality Issues contains `None`.
- [ ] User validation is `accepted`.
- [ ] The feature branch is squash-integrated into `development`.
- [ ] Current blocker is `none`.
- [ ] The observable outcome is demonstrated.

**Final outcome:** {accepted result, integration reference, or reason for closure without integration}
