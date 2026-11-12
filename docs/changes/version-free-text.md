# Change Contract: version-free-text

**Status:** accepted<br>
**Process owner:** Project Manager<br>
**Current responsibility:** Project Manager<br>
**Current blocker:** none<br>
**Created:** 2026-11-11<br>
- **Operation Mode**: autonomous, agreed with the User on 2026-11-12.

- **autonomous** - every actor decides on its own; when genuinely unsure, it asks the user directly and pauses only its own step until answered.

## Handover log

Owned by: Project Manager

The handing-over actor appends one line as the last act before handing over, in the same commit that changes `Current responsibility`, taking `Date` as `YYYY-MM-DD` and `Time` as `HH:MM` in 24-hour local time from the system clock at that moment. The note states what the owner did and the facts that change the next owner's situation; evidence stays in the owner's section and remaining work in the open rows. The handover goes to the next actor that follows from the logical flow of the Change. The log explains transitions; the header stays authoritative.

| Date | Time | From | To | Note |
|--|--|--|--|--|
| 2026-11-12 | 06:25 | Project Manager | Architect | Contract released by the User in autonomous mode; remove product version labels from specifications and architecture text first. |
| 2026-11-12 | 06:30 | Architect | Technical Writer | Removed product labels from specification and architecture text; the ontology schema identifier stays unchanged. Documentation and example rows remain open. |
| 2026-11-12 | 06:36 | Technical Writer | Architect | Documentation complete, examples unchanged; factual review clear, strict build and 30 focused tests pass. Returning for the additional Requirement literal, then Developer. |
| 2026-11-12 | 06:48 | Architect | Developer | Removed the additional historical Requirement literal and recorded the User-approved extension to four test-method renames; behavior and assertions remain unchanged. |
| 2026-11-12 | 07:59 | Developer | Quality | Removed the version label from the skill and the workflow comment and renamed the four test methods without touching bodies; strict build and 202 tests pass. Yours: review. |
| 2026-11-12 | 08:03 | Quality | User | Proceed for validation: version-free current text, preserved historical provenance and behavior-neutral test renames confirmed. |
| 2026-11-12 | 08:06 | User | Project Manager | The User accepted the outcome; closure recorded. |

## Intent And Outcome

**Status:** approved<br>
**Approval evidence:** The User decided the intent and scope boundaries on 2026-11-11, reviewed the Contract in the editor and released it on 2026-11-12.

### Goal

Syspilot's current documents and specifications describe Syspilot as it is. They carry no "v1", "v2" or other version label for the product; a version appears only in release artifacts, where it is assigned during the release.

### Value

The product is simply Syspilot. Labels such as "Syspilot v2" or "the v2 graph" describe a past migration, not the product, and leave readers asking what a v3 or the former v1 was. Version labels in prose also age with every release.

### Scope

- Remove "v1", "v2" and similar product version labels from the current documents, requirements, user stories, indexes, captions and the `docs/upgrade.md` guide, reworded so the sentence states what holds without naming a version. This includes the Developer-owned skill `syspilot.ontology` and the comment in `.github/workflows/release.yml`.
- Specification and architecture text that carries such a label is corrected with the documents.
- Rename the four User-approved test methods in `tests/test_analyze_mece.py` (one), `tests/test_analyze_trace.py` (two) and `tests/test_get_need_links.py` (one), as listed in Implementation; test bodies, assertions and release-version fixtures remain unchanged. Project Manager authorized this scope alignment on 2026-11-12.
- Unchanged: "SysML v2", which names another standard; release notes of earlier releases and the published v0.10.0 entry; archived Contracts under `docs/changes/` and `docs/releases/`; version numbers of external tools and actions.
- Unchanged: dated field notes under `docs/experiences/` and their index's historical version context. Project Manager confirmed on 2026-11-12 that these numbers record historical provenance, not current product labels.
- Unchanged: the version mechanism of the Release Process.

### Observable Outcome

A search of the current documents, specifications, skills, workflow and the four test-method identifiers for product version labels finds only the unchanged items listed in Scope, including historical field-note context. The documentation builds strictly clean and the tests pass.

## Artifacts, Ownership And Process Gates

**Applicability:** Each artifact owner decides and updates its own row.<br>
**Scope change:** When the approved intent widens after a row reached a terminal status, `Intent and outcome` returns to `draft` until it is approved again, and each owner whose terminal row the wider intent may affect reassesses it: the owner sets the row back to `pending` or records in the row why its evidence still holds.<br>
**Ownership:** The `Owner` column of this table is the only statement of artifact and gate ownership in the Contract; section headings name no artifact owner.<br>
**Status:** pending

Crew by User decision of 2026-11-11: Architect and Technical Writer; the Developer owns the skill and the workflow comment.

| Artifact or gate | Included | Owner | Completion evidence | Status |
|---|---|---|---|---|
| Intent and outcome | yes | Project Manager | Goal, value, scope, and observable outcome are explicit and approved | approved |
| Contract release | yes | User | User released the Contract on 2026-11-12 | approved |
| Version control | yes | Project Manager | Feature branch `feature/version-free-text`; squash-integrated into `development` at closure | active |
| Infrastructure impact | not applicable: the workflow change is a comment owned by the Developer | Admin | Affected workflow, CI, and packaging artifacts are updated, confirmed by their current owner rather than inferred from a Needs-only impact query | not applicable |
| Product specification and architecture decisions | yes | Architect | Ten specification/architecture files corrected; broader numeric scan retains only external-tool versions; isolated strict build, four build-runner tests and 11 release-version tests pass. Evidence remains valid for the approved test-name extension: no specification obligation changes | complete |
| User-facing documentation | yes | Technical Writer | Eleven files corrected; Architect factual review of 15989f7 has no findings; current documentation scan retains only SysML v2, strict isolated build has zero warnings, 4 build-runner and 26 focused checks pass | complete |
| Example sync | yes | Technical Writer | No product labels or changed role/process obligations in Example Actors/Contracts; unchanged folders verified by search, diff, card/generic Contract/map checks and strict build | not applicable |
| Implementation and unit verification | yes | Developer | Skill `syspilot.ontology` and the `release.yml` comment carry no product version label; tests pass | complete |
| Acceptance test design and results | not applicable: the outcome is checked by search and review | Tester | Requirement tests written and run by the Tester, with their commands and results, and the means for User validation trace to the intended outcome | not applicable |
| Quality review | yes | Quality | Independent review at 2fd16d4: full text delta and remaining-label scan reviewed; parsed ontology and AST checks confirm preserved behavior; 72 graph queries succeed; recorded isolated strict builds and final 202-test pass support proceed | proceed |
| User validation and approval | yes | User | The User accepted the outcome on 2026-11-12 | accepted |
| Closure decision | yes | Project Manager | Final outcome, validation disposition, and integration state are recorded | accepted |

## Architecture And Specification

**Status:** complete

### Affected Artifacts

| Artifact | Change | Rationale |
|---|---|---|
| `docs/syspilot/index.rst`, `root.rst`, `userstories/index.rst` | Remove the product label from the specification title, graph description and story introduction; describe HOW as the realization artifact | These pages describe the current graph, not a migration generation |
| `docs/syspilot/requirements/req_ontology_management.rst`, `userstories/us_ontology_management.rst` | Refer to the configured project schema; shorten the schema VC into a direct comparison with that schema | Configured fields and Contract-owned responsibility remain the reference, with no product generation required |
| `docs/syspilot/requirements/req_impact_analysis.rst`, `userstories/us_impact_analysis.rst` | Refer to configured Syspilot or project-defined links rather than a product generation | Standard and custom link traversal remain covered |
| `docs/syspilot/requirements/req_quality_methods.rst` | Refer to current project data in the MECE and Trace VCs | The fixtures and required results do not depend on a product label |
| `.syspilot/ontology.toml` | Remove the product label from the description and realization comment; retain `schema_version = "2.0"` | Project Manager confirmed inclusion by CONSULTRESPOND on 2026-11-12; the value identifies the ontology schema, not a product release |
| `docs/syspilot/requirements/req_release_version.rst` | Remove the historical configuration's numeric version literal from the derivation rationale | The rule is that the derived value cannot drift independently of the release notes; the historical number is unnecessary and belongs outside current specification prose |

### Decisions And Evidence

| Decision or check | Evidence |
|---|---|
| Preserve obligations, Need IDs, links and runtime behavior; only generation-dependent wording and the affected schema VC's presentation change | Diff of the nine files; the schema VC still checks configured fields, absence of obsolete guidance and Contract-owned responsibility |
| Impact discovery identifies `SYSP_DOC_CUSTOMIZATION`, `SYSP_DOC_UPGRADE` and `SYSP_DOC_CHANGE_CONTRACT`, the related stories and VCs | Successful both-direction, depth-1 flat queries for `SYSP_REQ_ONTOLOGY_SCHEMA`, `SYSP_REQ_IMPACT_QUERY`, `SYSP_REQ_MECE_ANALYSIS` and `SYSP_REQ_TRACE_ANALYSIS`; documentation candidates remain with Technical Writer, realized skills with Developer |
| No product labels remain in the specification tree or ontology configuration | Case-insensitive search for `\bv\d+(?:\.\d+)*\b` over `docs/syspilot/*.rst` recursively and `.syspilot/ontology.toml`: no matches; the schema identifier is intentionally retained |
| Strict full documentation build passes with zero schema warnings; four build-runner tests pass | `uv run sphinx-build -E -a -b html -W --keep-going docs {isolated session output}`; `python docs/test_docs_build.py -v`; `git diff --check`. The normal clean build was blocked by the shared output directory being in use, so validation used a separate output directory and fresh Sphinx environment. The full QA suite remains for Developer after the remaining edits |
| Additional source correction after Technical Writer's broader numeric scan: the historical release literal is removed without changing the release mechanism | `SYSP_REQ_RELEASE_VERSION` retains the newest-heading source and derived documentation version. A fresh isolated strict build passes with zero schema warnings; `python -m unittest discover -s tests -p test_release_version.py -v`: 11 tests pass; `git diff --check` passes. Case-insensitive generation-token and numeric-version searches across specification RST files retain only Jarvis Core and Sphinx-Needs versions |
| Impact of the additional correction is wording only; no dependent release procedure or guide needs a behavior change | Successful both-direction, depth-1 query for `SYSP_REQ_RELEASE_VERSION` against the fresh isolated Needs export returns Branching, Operations, Example Contracts, Release Contract Requirement/Story and its VC; their version-consistency obligations remain unchanged |
| Scope extended to rename the four test-method identifiers containing `v2`, owned by Developer; behavior, assertions and release-version fixtures remain unchanged | Project Manager's CONSULTRESPOND of 2026-11-12 reports the User's explicit confirmation. The extension covers one identifier in `tests/test_analyze_mece.py`, two in `tests/test_analyze_trace.py` and one in `tests/test_get_need_links.py`. Project Manager will align Intent text when responsibility returns; the approved extension is recorded here for Developer's work |

## User-Facing Documentation

**Status:** complete

Documentation impact queries for `SYSP_REQ_ONTOLOGY_SCHEMA` and `SYSP_REQ_CONTRACT_DOCUMENTS` succeeded in both directions at depth 1 with `--flat --no-build`, using an isolated strict build's `needs_id` export. The default query first failed because the shared output had no Needs data; no impact conclusion was taken from that failure. Candidates include Customization, Upgrade, Change Contract, Getting Started, Methodology, Portal, Product Model and Example Contracts. Direct text search additionally identifies navigation, Naming Conventions, Traceability, README, Operations and Branching; the plan records their disposition.

### Documentation Plan And Ownership

| Documentation surface | `doc` Need | Requirements included | Status |
|---|---|---|---|
| `README.md`, `docs/getting-started.md`, `docs/operations.md`, `docs/upgrade.md` | `SYSP_DOC_README`, `SYSP_DOC_GETTING_STARTED`, `SYSP_DOC_OPERATIONS`, `SYSP_DOC_UPGRADE` | Existing actor, Setup and update-Change coverage; replace numeric migration labels with the earlier-setup/Contract-driven-actor boundary and selected release | complete; migration steps and evidence limits preserved |
| `docs/index.rst`, `docs/product-model.md`, `docs/branching.md` | `SYSP_DOC_PORTAL`, `SYSP_DOC_PRODUCT_MODEL`, `SYSP_DOC_BRANCHING` | Existing actor, Contract, Setup and realization explanations; generation-free headings/prose and symbolic release tags in the branch illustration | complete |
| `docs/Syspilot Actors/index.md`, `docs/traceability/index.rst`, `docs/namingconventions.md` | Supporting actor/graph/reference pages | Describe the current roster, graph and root ID without a migration generation | complete |
| `docs/syspilot/documentation/index.rst` | `SYSP_DOC_UPGRADE` description | Same realized path, Need ID and includes; describe the migration by its model boundary, not a release number | complete; no new independently maintained surface introduced |
| Remaining current documentation, examples and source-owned artifacts | Existing Needs/includes unchanged | Search/review excludes archived Contracts, release notes and dated Field Notes/index context under the Scope disposition; retains SysML v2, external versions and release mechanism | current-product documentation scan complete within that boundary; extra Requirement literal goes to Architect, skill/workflow text remains Developer-owned |

### Consultations And Factual Reviews

| Documentation surface | Consulted artifact owner | Review question | Evidence and disposition |
|---|---|---|---|
| Eleven changed documentation/map files | Architect | Does removing labels preserve the current model, migration steps, evidence limits and release mechanism? | Direct factual review of committed `15989f7`: no findings; selected-release baseline, concrete migration and symbolic diagram tags preserve the intended behavior. Review covers factual accuracy, not the later whole-scope verification |
| `SYSP_REQ_RELEASE_VERSION` | Architect | Is the historical `0.1.0` literal another in-scope product version label? | Architect agrees it is incidental to the rule and must be removed, retaining the rationale that the derived value cannot drift independently. No consultation edit made; hand back for source-owned correction, then Developer |
| Four test method names containing generation labels | Developer | Should current test identifiers also lose generation wording? | Developer assesses renames would be behavior-neutral but requests explicit scope confirmation; no change made. Architect/Project Manager decide before Developer acts; release-mechanism fixtures remain unchanged |

### Changed Documentation And Verification

| Artifact | Change | Verification evidence |
|---|---|---|
| Eleven current documentation/map files | Removed generation/release labels; retained concrete migration steps, evidence limitations, selected-release baseline, SysML v2 and external versions. The Branching diagram uses symbolic release tags, not literal product versions | Architect factual review clear; final strict build with a fresh Sphinx environment and isolated output passes without warnings after fixing the renamed RST heading's underline. Four build-runner tests and 26 focused example/map/shared-rule tests pass; no full-suite pass claimed |
| Current-document and preservation scan | Case-insensitive `git grep` over tracked README/docs, excluding `docs/changes/`, `docs/releases/` and `docs/releasenotes.md`, for version tokens and numeric migration labels | Only three retained SysML v2 matches for the generation/target-release scan. Broader numeric review excluded dated Field Notes and their index context; those retain historical Syspilot baseline numbers under the explicit Scope disposition confirmed by Project Manager on 2026-11-12. Current-product prose was checked separately; external-tool versions and the Architect-owned historical configuration literal were found. Release notes, archived release records and Example folders have no diff from `b8cba4a`; Developer-owned skill/workflow labels still await their row. Technical Writer authorized this bounded scan-evidence clarification through consultation on 2026-11-12 |

Verification commands: `uv run sphinx-build -E -a -b html -W --keep-going docs {isolated session output}`; `python docs/test_docs_build.py -v`; `python -m unittest tests.test_acceptance_setup_examples.DeviationTests tests.test_acceptance_setup_examples.GenericContractTests tests.test_acceptance_setup_examples.DocNeedTests tests.test_acceptance_adoption_feedback.SharedContractRulesTests`; `git diff --check`. The isolated build avoids shared-output interference; its exported Needs support the impact queries. Direct assertions on rendered HTML also confirm the portal's version-free navigation and the `Upgrading an Existing Project` heading, with the old titles absent. Full-scope search and QA follow the remaining source/implementation edits.

## Example Sync

**Status:** not applicable

| Artifact | Change | Verification evidence |
|---|---|---|
| `docs/Example Actors/`, `docs/Example Contracts/` | Not applicable: neither folder contains a product version label; no role or process behavior changes in this Change, so no new example deviation or edit is needed | No diff from `b8cba4a`; version-token scan has no matches. Card-equivalence, generic Contract, documentation-map and shared-rule checks pass (26 tests); full strict documentation build passes |

## Implementation And Unit Verification

**Status:** complete

### Decisions And Evidence

| Decision | Chosen approach | Relevant alternatives | Rationale and evidence |
|---|---|---|---|
| Skill and workflow comment | Dropped `v2` from the `syspilot.ontology` description, renamed its heading `Current V2 Schema` to `Current Schema`, and dropped `v2` from the first comment line of `release.yml`; no other text changed | Rewording the sections | The sentences already state what holds; only the label was removed. `softprops/action-gh-release@v2` is an external action version and stays |
| Test identifiers | Renamed four methods without touching bodies: `test_current_data_discovers_requirement_peers`, `test_current_data_uses_typed_impact_discovery`, `test_current_requirement_without_specializes_has_no_missing_finding`, `test_flat_traverses_standard_and_customer_links_once` | Leaving the names | Scope extension approved by the User (see the Architect's decisions); behavior and assertions are unchanged, so a rename cannot hide a regression. The `v1.2.3` fixtures are release-mechanism data and stay |

### Changed Artifacts And Verification

| Artifact | Change | Verification evidence |
|---|---|---|
| `.github/skills/syspilot.ontology/SKILL.md`, `.github/workflows/release.yml`, `tests/test_analyze_mece.py`, `tests/test_analyze_trace.py`, `tests/test_get_need_links.py` | As above | `git grep` outside `docs/changes`, `docs/releases`, `docs/releasenotes.md` for `current_v2`, `Current V2`, `Syspilot v2 ontology`, `standard_v2`, `current v2` finds nothing; strict `uv run python docs/docs-build.py` built successfully; `uv run python -m unittest discover -s tests`: 202 tests OK (2026-11-12 07:59). A first full run showed 3 failures (`Need SYSP_REQ_MECE_ANALYSIS not found`) while I rebuilt the shared `docs/_build` at the same time; the three modules pass alone (25 tests) and the full rerun passed. The `clean` build is blocked by another process holding `docs/_build/html` |

## Quality Review

**Status:** proceed

**Current judgment:** proceed for User validation at `2fd16d4`. Current specification, documentation, ontology skill and workflow comment describe Syspilot without a product-generation label. The upgrade guide retains its concrete migration steps, selected-release baseline, authorization and evidence limits. Release mechanism, external versions, SysML v2, historical release artifacts and dated field-note provenance remain intact. Project Manager directly authorized aligning this Contract with the already User-approved four test-name renames and explicitly preserving historical field-note context. No open quality issue remains within this wording-only scope; User validation and closure remain pending.

Quality read the complete source and documentation delta from `4f7451b` to `2fd16d4`, including all four test-method changes. A Python AST comparison after applying only the four approved name substitutions is identical to the new test modules: bodies, assertions and fixtures are unchanged. Parsed TOML is identical after excluding the changed description; the schema identifier remains `2.0`. Diff checks confirm release notes, archived release records, historical Change Contracts and both example folders are untouched; only this active Change record differs under `docs/changes/`.

Independent case-insensitive generation-token and numeric-version scans of committed README, documentation, specifications, skills, ontology configuration and workflow found only allowed external versions, SysML v2, schema metadata, historical field-note versions and non-version numeric literals. The dated field notes were not listed in the earlier broad-scan evidence; this review records their disposition explicitly rather than treating that earlier search claim as complete. Project Manager confirmed their exclusion through consultation on 2026-11-12.

Reviewed owner-recorded isolated strict builds with fresh Sphinx environments, 4 build-runner tests, 26 focused documentation checks, 11 release-version tests and the final full-suite result of 202 passing tests. The shared-output lock and earlier three missing-Need failures during concurrent rebuilding are recorded, not claimed as content passes; the subsequent full run passed. No runtime logic or dependency changed, so no additional Quality build/test execution was needed beyond the exact AST/TOML preservation checks and graph analyses.

KISS review: the changed User Stories retain their user goal and Contract-owned authority; the shortened ontology VC remains a bounded schema/ownership comparison. This Change neither claims nor performs a general Requirement/VC restructuring. Existing broad verification prose is not represented as newly decomposed, and no new material assessability defect was introduced by removing the version labels.

### Applied Review Methods

| Method | Selected scope | Evidence | Findings | Limits |
|---|---|---|---|---|
| Impact discovery | 24 starts: `ROOT_SYSPILOT`; every Need in `req_ontology_management.rst`, `req_impact_analysis.rst`, `req_quality_methods.rst`, `req_release_version.rst`, `us_ontology_management.rst`, `us_impact_analysis.rst`; `SYSP_DOC_README`, `SYSP_DOC_GETTING_STARTED`, `SYSP_DOC_OPERATIONS`, `SYSP_DOC_UPGRADE`, `SYSP_DOC_PORTAL`, `SYSP_DOC_PRODUCT_MODEL`, `SYSP_DOC_BRANCHING` | 24 successful `get_need_links.py ID --direction both --depth 1 --flat --no-build` queries against the final built Needs | Neighbor/peer union contains 68 objects; documentation, source guidance, release consistency and Contract boundaries were included in review | Discovery is bounded candidate evidence, not exhaustive filesystem scope |
| Horizontal coverage | Same-document peers of all 24 starts | 24 successful `analyze_mece.py ID --scope same-document` queries; no structural findings. Exact peer groups: ontology schema/editing Requirements and their two VCs; MECE/Trace Requirements and their two VCs; the 12 documentation Needs in `docs/syspilot/documentation/index.rst`. Other starts have no peers | Reviewed both ontology obligations, both analysis obligations and VCs, impacted stories/ACs, and complete documentation-map peer descriptions. Schema versus editing, peer versus relationship analysis, and current guides versus historical evidence remain distinct | Empty peers and unavailable structured coverage are limitations; semantic judgments come from content review, not empty findings |
| Relationship analysis | Same 24 starts, both directions, depth 1; exact examined neighborhood reproducible from the commands above, combined with reported same-document peers | 24 successful `analyze_trace.py ID --direction both --depth 1` queries; no structural findings. Read every changed neighborhood source and its changed realization. Compared source changes against completed release review at `03db5ca`; retained unchanged actor/Setup/Contract semantic baseline and the subsequent archive review at `c81d57f`; directly read ontology, Impact and Quality-method content beyond that baseline | No changed Need ID, link or ownership boundary; generation-free wording still covers standard and project-configured links, strict ontology validation, independent Quality and release-version consistency | One-hop scope is deliberate for editorial changes. No inference of mandatory links, completeness or runtime installation behavior |
| Exact artifact preservation | Committed diff, tracked-file searches, parsed ontology and Python AST | Four approved method-name substitutions produce identical ASTs; ontology differs semantically only in description; workflow diff is one comment; skill frontmatter discovery terms and requirements stay intact | No behavior shift or new example deviation established; field-note exception and approved test-name scope aligned with PM consent | No actual installation, release, publication or new runtime capability is demonstrated |

Quality communicates its `proceed` judgment and supporting evidence directly to the Project Manager before the Project Manager presents the verified outcome for validation. Another actor's forwarded claim does not establish Quality's decision.

### Open Quality Issues

Keep this table synchronized with currently open issues. For each issue, Quality transfers current responsibility to the owner of the affected artifact. When Quality confirms the required outcome, update the affected artifact or evidence and remove the resolved row. At closure this table contains `None`.

| Artifact | Current issue | Required outcome |
|---|---|---|
| None | None | None |

## User Validation And Approval

**Recorded by:** Project Manager<br>
**Status:** accepted

Quality's `proceed` judgment verifies that the change is ready for validation; it does not validate user value. The Project Manager presents the observable outcome after receiving Quality's direct judgment and evidence; the User communicates the decision directly to the Project Manager, who records it.

**Decision and evidence:** The User accepted the outcome directly to the Project Manager on 2026-11-12 after the presentation of Quality's `proceed` at 5d12fcf. The presentation named the preserved exceptions: SysML v2, earlier release notes and the published v0.10.0 entry, archived Contracts, and the dated field notes under `docs/experiences/`.

## Closure

**Status:** accepted

- [x] Every included artifact or gate has terminal status and completion evidence.
- [x] Intent and outcome are `approved`.
- [x] Quality has recorded a `proceed` judgment.
- [x] Open Quality Issues contains `None`.
- [x] User validation is `accepted`.
- [x] Current blocker is `none`.
- [x] The observable outcome is demonstrated.

**Final outcome:** Current Syspilot documents, specifications, the ontology skill, the workflow comment and four test method names carry no product version label; the Release mechanism is unchanged. The User accepted on 2026-11-12.
