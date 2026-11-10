# Change Contract: Sphinx-Needs Graph Alignment

**Status:** closed<br>
**Process owner:** Project Manager<br>
**Current responsibility:** Project Manager<br>
**Current blocker:** none<br>
**Created:** 2026-09-22<br>
**Branch:** feature/sphinx-needs-graph-alignment<br>
- **Operation Mode**: autonomous

- **autonomous** - every actor decides on its own; when genuinely unsure, it asks the user directly and pauses only its own step until answered.

## Intent And Outcome

**Owner:** Project Manager<br>
**Status:** approved<br>
**Approval evidence:** The User selected autonomous operation, requested review of the proposed Contract before handoff, then replied "ok let's go" on 2026-09-22 after it was presented for review. This settles the intent; the separate User-owned `Contract release` row records authorization to start artifact work.

### Goal

Allow Impact and Trace to navigate a project's graph using its configured Sphinx-Needs link kinds and exported relationships without requiring `[[syspilot.type_links]]` or any replacement Syspilot-only link schema. Keep Contract-specific artifact ownership in the applicable Contract, not the ontology.

### Value

Sphinx-Needs already represents named outgoing links and incoming backlinks. The extra `from`/`to`/`rel` rules currently used by Trace check only type pairs: they cannot determine whether a particular `req -> req` `specializes` link points from the concrete requirement to the appropriate general requirement, or whether other necessary links are absent. Requiring each installed project to maintain those rules for this limited check creates an additional configuration and compatibility obligation without establishing semantic correctness or graph completeness.

### Scope

- Preserve the existing Sphinx-Needs Need types, statuses, named link kinds, directed outgoing links and incoming backlinks, and traversal of exported relationships. Preserve the Setup rule that selects the existing project ontology when present and installs the Syspilot baseline only when absent.
- Remove the requirement for `[[syspilot.type_links]]` in Trace and in the released baseline, and do not replace it with mandatory Sphinx-Needs network schemas or inferred missing-link/cardinality rules. Assess whether any type-pair check should remain optional and what evidence it would actually provide; do not represent a type-pair check as validation of the meaning of two same-type Needs.
- Inspect consumers of `[syspilot.status_transitions]` and decide whether that metadata provides an active, necessary behavior or is only descriptive. Record the decision and align the baseline, ontology guidance and specification accordingly rather than silently dropping it.
- Align Impact and Trace guidance, affected Requirements and Verification Criteria, the Setup inventory/baseline, and focused tests with the chosen boundary. Confirm whether the Syspilot-internal generated reference page depends on removed metadata; any change to its existing build hook must be explicitly accounted for, without reviving automatic reference delivery to installed projects (board item #7 was closed by decision).
- Out of scope: removing Sphinx-Needs, requiring links or claiming graph completeness, assigning artifact ownership through the ontology, changing the four independent Sphinx-Needs/ontology Setup cases, or starting the 0.10.0 Release Contract.

### Observable Outcome

- A project with Sphinx-Needs-configured link kinds and exported Needs can run Impact and Trace without `[[syspilot.type_links]]`; valid existing links remain navigable in both directions to the selected depth.
- Trace reports only findings supportable from the available data and its approved specification. Neither a missing optional link nor the semantic orientation of a `req -> req` edge is certified by a type-pair rule.
- Any remaining Syspilot-specific ontology metadata has an identified consumer and reason; the baseline, guidance, Setup, and specifications consistently state which configuration is required.
- Focused tests exercise a project ontology without `[syspilot]` graph metadata, named forward/backward links, unresolved targets and honest limits; the strict documentation and schema build passes without warnings.

## Artifacts, Ownership And Process Gates

**Applicability:** Each artifact owner decides and updates its own row.<br>
**Status:** complete

| Artifact or gate | Included | Owner | Completion evidence | Status |
|---|---|---|---|---|
| Intent and outcome | yes | Project Manager | User reviewed the proposed Contract at `4c653b9` and replied "ok let's go" on 2026-09-22 | approved |
| Contract release | yes | User | User replied "ok let's go" after reviewing the proposed Contract on 2026-09-22, authorizing work in the selected autonomous mode | approved |
| Version control | yes | Project Manager | `feature/sphinx-needs-graph-alignment` squash-integrated into `development` in the closure commit; feature branch retained locally | merged |
| Product specification and architecture decisions | yes | Architect | Trace, ontology, and Quality-method Needs revised; Impact, Setup, reference hook and metadata consumers dispositioned; strict build and docs tests pass | complete |
| User-facing documentation | yes: Trace and ontology configuration guidance change | Technical Writer | Change Contract and Customization guides corrected; existing `doc` ownership map checked; strict docs build passed | complete |
| Implementation and unit verification | yes | Developer | Trace uses configured Sphinx-Needs links without Syspilot graph rules; baseline, guidance, and internal reference generator aligned. Trace 7/7, Impact 9/9, docs tests 4/4, scoped strict Sphinx build 0 warnings; the later default strict build passed as recorded by Tester and Quality | complete |
| Acceptance test design and results | yes | Tester | Three graph-navigation scenarios pass: Trace 8/8, Impact 9/9; default `python docs/docs-build.py clean` succeeds with 0 schema and Sphinx warnings after Project Manager removed obsolete untracked process pages with User confirmation | passed |
| Quality review | yes | Quality | Seven impacted Needs reviewed in both MECE scopes and bidirectional Trace at depth 2; semantic review and strict build passed; judgment `proceed` below | proceed |
| User validation and approval | not applicable: User explicitly delegated validation of this finished outcome on 2026-09-23; practical evaluation will run separately in a Jarvis Change | User | User replied "agreed" to the proposed delegation and separate practical evaluation; no User validation of this outcome occurred here | not applicable |
| Closure decision | yes | Project Manager | Delegated validation and Quality `proceed` recorded; integration and final outcome documented below in the closure commit | closed |

## Architecture And Specification

**Owner:** Architect<br>
**Status:** complete

### Affected Artifacts

| Artifact | Change | Rationale |
|---|---|---|
| `docs/syspilot/requirements/req_quality_methods.rst` (`SYSP_REQ_TRACE_ANALYSIS`, `SYSP_VC_TRACE_ANALYSIS_1`) | modify | Trace may report observed named/directed edges and unresolved targets, not rule-derived undeclared or orphan findings or semantic correctness inferred from type pairs |
| `docs/syspilot/userstories/us_quality_methods.rst` (`SYSP_US_QUALITY_METHODS`) | modify | Relationship review cannot infer an absent required link from optional link configuration; its acceptance criterion `SYSP_AC_QUALITY_METHODS_1` already requests findings and limits, so needs no edit |
| `docs/syspilot/requirements/req_ontology_management.rst` (`SYSP_REQ_ONTOLOGY_SCHEMA`, `SYSP_VC_ONTOLOGY_SCHEMA_1`, `SYSP_REQ_ONTOLOGY_EDITING`, `SYSP_VC_ONTOLOGY_EDITING_1`) | modify | Describe Sphinx-Needs configuration without claiming mandatory Syspilot type-pair or transition sections |
| `.github/skills/syspilot.trace/scripts/analyze_trace.py`, `test_analyze_trace.py`, `.github/skills/syspilot.trace/SKILL.md` | modify | Remove mandatory `type_links` load and unsupported rule-derived findings; test named incoming/outgoing links, depth, unresolved targets and limitations without `[syspilot]` graph metadata |
| `.syspilot/ontology.toml`, `.github/skills/syspilot.ontology/SKILL.md` | modify | Remove unused `type_links` and descriptive `status_transitions` from the release baseline and guidance; retain `[needs]` types, statuses, options and directed extra-link kinds |
| `docs/conf.py`, generated `docs/ontology-reference.md` | modify generator; regenerate output | The internal build hook currently derives type and lifecycle diagrams from the removed metadata. Keep the generated reference page and its type catalogue, but omit diagrams whose rules no longer exist; do not deliver the page automatically to installed projects |
| `docs/syspilot/requirements/req_impact_analysis.rst` (`SYSP_REQ_IMPACT_QUERY`, `SYSP_VC_IMPACT_QUERY_1`), `.github/skills/syspilot.impact-python/scripts/get_need_links.py` | no change; regression check | Impact already reads `[needs].extra_links` and exported `links`/`links_back` without reading `[syspilot]`; confirm existing named and customer links still work |
| `docs/syspilot/requirements/req_setup.rst` (`SYSP_REQ_SETUP`, `SYSP_VC_SETUP_1`), `docs/Syspilot Contracts/setup.md` | no change; inventory verification | Existing Setup preserves configured ontology and Sphinx-Needs independently; a release baseline without optional graph metadata is copied only when no ontology exists |

### Decisions And Evidence

| Decision or check | Evidence |
|---|---|
| User authorization and resolved editing blocker | User authorized `insert_edit_into_file` after the failed `apply_patch` attempts on 2026-09-22 (via Project Manager). The Trace Need and VC were edited with three-space directive-body indentation, inspected line-by-line, and validated with `python docs/docs-build.py clean`: zero schema warnings, build succeeded. The prior failed edit was rolled back, not accepted |
| Consumer boundary | `.github/skills/syspilot.trace/scripts/analyze_trace.py` calls `load_rules()` unconditionally and uses `syspilot.type_links` for `permitted`, `undeclared-relationship` and rule-derived `orphan`. Impact's `load_link_options()` instead reads `[needs].extra_links`; `docs/conf.py` consumes `type_links` and `status_transitions` solely to generate internal reference diagrams. No active status-transition enforcement was found in these consumers or the current specification |
| Type-pair checks are not retained in Trace, even optionally in this Change | A type-pair rule can reject an observed triple but cannot establish the semantic orientation of `req -> req` `specializes`, missing-link requiredness or graph completeness. Keeping it optional would add an unrequested second verification mode and retain the extra metadata dependency; a future Contract can authorize a separately specified optional check |
| Trace's supported findings | Reuse Impact's typed traversal over configured Sphinx-Needs `links`/`links_back` and `<option>`/`<option>_back`; preserve observed source, target, name, direction, depth and exact neighborhood; report unresolved targets. An object with no observed edges is an observation within the selected depth/direction, not a defect called an orphan. Keep semantic consistency as an explicit human/actor review limitation; do not infer missing links |
| Status transitions and baseline | `[syspilot.status_transitions]` has no active transition-enforcing consumer; the only located reader is `docs/conf.py`'s internal diagram hook, which renders universal transitions but omits type overrides. Remove it with `[[syspilot.type_links]]` from the released baseline instead of preserving a misleading descriptive lifecycle. Keep `[needs].statuses` and all named/directed extra links unchanged. Remaining `syspilot.schema_version` labels the baseline schema for ontology guidance, not a required runtime graph input |
| Internal reference page | `docs/conf.py` generates `docs/ontology-reference.md` on `builder-inited` and `docs/syspilot/index.rst` links it. Preserve the hook and page with the `[needs]` type catalogue; drop the diagrams dependent on removed Syspilot metadata, regenerate the output and verify the internal docs build. Setup's inventory does not deliver this generated page to installed projects; do not reintroduce it |
| Setup independence and scope | `SYSP_REQ_SETUP` and `docs/Syspilot Contracts/setup.md` select existing ontology vs. baseline copy independently from existing Sphinx-Needs vs. project-local install (four combinations); neither requires `[syspilot]` graph metadata. Do not alter those four cases. Baseline copy must use the revised `.syspilot/ontology.toml`; target builds and Trace tests should cover a project ontology without graph metadata |
| Impact discovery disposition | Built Needs impact queries (`--flat --direction both --depth 2`) from `SYSP_REQ_TRACE_ANALYSIS` and `SYSP_REQ_ONTOLOGY_SCHEMA` include their VC/story/doc consumers and `SYSP_REQ_IMPACT_QUERY`/`SYSP_REQ_SETUP`; depth-one Setup query exposes `SYSP_VC_SETUP_1` and documentation consumers. The latter Needs remain unchanged because their existing traversal/selection language already matches this boundary; documentation owners review their own surfaces |
| Specification verification | `python docs/docs-build.py clean`: schema validation 0 warnings, build succeeded. `python docs/test_docs_build.py -v`: 4 tests passed (the expected failure fixture prints `[FAIL]` but its test passes). `git diff --check`: no whitespace errors. Instruction and implementation changes remain pending with their owners |

## User-Facing Documentation

**Owner:** Technical Writer<br>
**Status:** complete

### Documentation Plan And Ownership

| Documentation surface | `doc` Need | Requirements included | Status |
|---|---|---|---|
| `docs/change-contract.md` | `SYSP_DOC_CHANGE_CONTRACT` | `SYSP_REQ_TRACE_ANALYSIS`, `SYSP_REQ_IMPACT_QUERY`, `SYSP_REQ_MECE_ANALYSIS` already included | Updated: observed links and unresolved targets, no missing-link or semantic inference |
| `docs/customization.md` | `SYSP_DOC_CUSTOMIZATION` | `SYSP_REQ_ONTOLOGY_SCHEMA`, `SYSP_REQ_ONTOLOGY_EDITING`, `SYSP_REQ_SETUP` already included | Updated: `[needs]` link kinds and descriptive `[syspilot]` schema version; no mandatory type-pair or transition rules |
| Other project-lead guides | Existing `doc` Needs in `docs/syspilot/documentation/index.rst` | Unchanged | Reviewed README, Getting Started, Product Model, Operations, Methodology and Branching; no contrary graph-rule claims found |

### Consultations And Factual Reviews

| Documentation surface | Consulted artifact owner | Review question | Evidence and disposition |
|---|---|---|---|
| Change Contract and Customization guides | Developer | Confirm Trace's supported observations and whether ontology guidance misses an active graph-metadata consumer | CONSULT sent; response pending, no responsibility transfer |

### Changed Documentation And Verification

| Artifact | Change | Verification evidence |
|---|---|---|
| `docs/change-contract.md` | Replace unsupported missing-link/type-rule checks with observed named/directed links, unresolved targets and explicit human semantic-review limits | `python docs/docs-build.py clean` passed; zero schema warnings |
| `docs/customization.md` | Describe Sphinx-Needs configuration and remove mandatory Syspilot type-pair/transition claims | `python docs/docs-build.py clean` passed; zero schema warnings; `git diff --check` clean |

## Implementation And Unit Verification

**Owner:** Developer<br>
**Status:** complete

### Decisions And Evidence

| Decision | Chosen approach | Relevant alternatives | Rationale and evidence |
|---|---|---|---|
| Trace findings | Reuse Impact's typed traversal of standard and configured links; report observed source, target, link option, direction, depth, resolution and neighborhood, with unresolved targets as findings | Retain optional type-pair permission checking, undeclared-relationship or orphan findings | Type-pair metadata cannot establish semantic correctness or missing-link requiredness. Tests with only `[needs]` cover depth, incoming and outgoing named links, unresolved targets and isolated Needs without unsupported defects (7/7) |
| Ontology baseline | Retain `[needs]` types, statuses, options and named links plus descriptive `syspilot.schema_version`; remove `type_links` and `status_transitions` | Keep unused rule and lifecycle metadata for reference diagrams | Impact reads `[needs].extra_links`, while the old transition metadata enforced no state changes. The removed rules would incorrectly imply semantic or lifecycle enforcement; Impact regression tests pass 9/9 |
| Internal reference | Keep the existing `builder-inited` generator and `[needs]` type catalogue; remove only diagram generation dependent on removed metadata | Retain stale diagrams or stop generating the internal reference page | The generated, ignored `docs/ontology-reference.md` retains all six Need types and has no rule-derived diagrams; a scoped warnings-as-errors Sphinx build succeeds. The normal build is blocked separately by untracked process pages referencing a missing document |

### Changed Artifacts And Verification

| Artifact | Change | Verification evidence |
|---|---|---|
| `.github/skills/syspilot.trace/scripts/analyze_trace.py`, `test_analyze_trace.py`, `SKILL.md` | Removed mandatory rule loading, `permitted`, `undeclared-relationship` and `orphan` results; updated tests and method guidance to observed links and unresolved targets | `python .github/skills/syspilot.trace/scripts/test_analyze_trace.py -v`: 7/7; synthetic ontology has no `[syspilot]` graph metadata; incoming link and isolated-object scenarios pass |
| `.syspilot/ontology.toml`, `.github/skills/syspilot.ontology/SKILL.md` | Removed obsolete type-pair and transition metadata; kept `[needs]` and descriptive schema version; updated editing guidance | `python .github/skills/syspilot.impact-python/scripts/test_get_need_links.py -v`: 9/9; Trace 7/7 against the revised baseline; `git diff --check` clean |
| `docs/conf.py` and generated, ignored `docs/ontology-reference.md` | Generator retains type catalogue while dropping metadata-based diagrams; rebuilt internal page | `uv run sphinx-build -b html docs docs/_build/html -W --keep-going -D 'exclude_patterns=_build,Thumbs.db,.DS_Store,.venv,venv,changes/*,Syspilot Processes/*'`: succeeds, schema 0 warnings; generated catalogue includes six types without diagrams |
| Default documentation build | No change to untracked process pages outside this implementation | `python docs/docs-build.py clean` fails with three warnings: missing `contract-documents` toctree target, unreferenced process index and missing cross-reference in untracked `docs/Syspilot Processes/`; `python docs/test_docs_build.py -v`: 4/4. Project Manager to resolve the missing page or references before final validation |

## Acceptance Testing

**Owner:** Tester<br>
**Status:** passed

| Scenario | Traces to | Result | Evidence |
|---|---|---|---|
| A target ontology without `[syspilot]` graph metadata still supports named, depth-bounded graph navigation | Observable Outcome | pass | Trace CLI fixture contains only `[needs]`; depths 1, 2, 3, 4 and 6 and typed named edges pass. `python .github/skills/syspilot.trace/scripts/test_analyze_trace.py -v`: 8/8; Impact regression: 9/9. |
| Forward and backward link traversal preserves actual source, target and link name | Observable Outcome | pass | Trace incoming test checks `N0 -> N1`, option `flows_to` and direction `in`; outgoing named `flows_to` and `bad_rel` edges pass. Impact typed-direction regression also passes (9/9). |
| Unresolved targets and any retained structural findings are reported without inferring missing optional or semantically wrong same-type links | Observable Outcome | pass | Trace reports `unresolved-target` for `MISSING`; isolated `OPTIONAL` yields no findings; same-type `req -> req` edge preserves observed direction with no inferred semantic finding and reports `semantic-content-review-required` (Trace 8/8). |

The default `python docs/docs-build.py clean` now succeeds with 0 schema warnings and no Sphinx warnings. Project Manager confirmed with the User that the untracked `docs/Syspilot Processes/` pages were obsolete residue after migration to tracked `docs/Syspilot Contracts/` and removed them before this independent acceptance rerun. This clears the previously recorded default-build blocker without treating the earlier scoped build as a default-build pass.

## Quality Review

**Owner:** Quality<br>
**Status:** proceed

**Current judgment:** proceed. The implementation, specifications, and guidance agree that Sphinx-Needs configured link kinds and exported edges support navigation without Syspilot type-pair rules. Trace preserves observed direction and link name and reports unresolved targets without treating absent optional links or same-type orientation as mechanically provable defects. The removed status-transition metadata had no enforcement consumer; the internal reference keeps its type catalogue. Tester's three acceptance scenarios were independently checked against the changed code, tests, and Needs. No open quality issue remains; User validation of the finished outcome is still pending.

### Applied Review Methods

| Method | Selected scope | Evidence | Findings | Limits |
|---|---|---|---|---|
| MECE horizontal coverage | `same-document` and `all-type` for `SYSP_REQ_TRACE_ANALYSIS`, `SYSP_VC_TRACE_ANALYSIS_1`, `SYSP_REQ_ONTOLOGY_SCHEMA`, `SYSP_VC_ONTOLOGY_SCHEMA_1`, `SYSP_REQ_ONTOLOGY_EDITING`, `SYSP_VC_ONTOLOGY_EDITING_1`, `SYSP_US_QUALITY_METHODS` (14 runs). Same-document peers: respectively `SYSP_REQ_MECE_ANALYSIS`, `SYSP_VC_MECE_ANALYSIS_1`, `SYSP_REQ_ONTOLOGY_EDITING`, `SYSP_VC_ONTOLOGY_EDITING_1`, `SYSP_REQ_ONTOLOGY_SCHEMA`, `SYSP_VC_ONTOLOGY_SCHEMA_1`, and none. All-type: 17 `req` peers per requirement, 17 `vc` peers per criterion, 14 `story` peers for the story. | `analyze_mece.py ID --scope same-document` and `--scope all-type` against the current built Needs; inspected changed Need text and comparable obligations. Focused MECE tests 5/5. | No structural findings in 14 runs; Trace versus Impact traversal, ontology schema versus editing, and their verification criteria retain distinct responsibilities; no contradictory changed peer obligation observed. | `structured-coverage-data-unavailable` and `semantic-content-review-required` on every run; no comparable same-document story peer, not a clean same-document story coverage claim. |
| Trace relationship and chain analysis | `--direction both --depth 2` for the same seven Needs. Neighborhoods: Trace requirement 17 IDs, Trace criterion 4, ontology schema and editing requirements 11 each, their criteria 4 each, Quality Methods story 22. | `analyze_trace.py ID --direction both --depth 2` on built Needs; inspected the associated story, acceptance and verification criteria, Impact traversal requirement, Setup boundary, and documentation links for semantic consistency. Focused Trace tests 8/8; Impact regression tests 9/9. | No unresolved targets or other findings in seven runs; the observed `implements`, `verifies`, `validates`, `includes`, and related backlinks are consistent with the revised division of work. | `semantic-content-review-required` is a mechanical limitation; the semantic assessment here covers the changed obligations and their reported neighbors, not a proof of missing-link absence or graph completeness. |
| Semantic artifact and acceptance review | All four observable outcomes; changed Trace analyzer and tests, baseline ontology and generator, Trace and ontology skill guidance, affected requirements/story, Change Contract and Customization guides; unchanged Impact and Setup boundaries. | Diff against `development`; compared each outcome with the changed artifacts and three Tester scenarios. The analyzer reuses Impact traversal and reads `[needs].extra_links` without loading Syspilot type-pair rules; the reference generator retains the type catalogue and omits metadata-derived diagrams. | No finding: directed and named traversal, unresolved targets, and limitations match specification; no status-transition enforcement is claimed; Setup retains its four independent cases. | Cannot certify semantic correctness of arbitrary same-type links or completeness of a project's graph from type pairs. |
| Strict build and focused verification | Full default docs and Needs schema build plus MECE, Trace, Impact and docs tests. | `python docs/docs-build.py clean`: succeeds with 0 schema warnings and no Sphinx warnings after Project Manager removed obsolete untracked process pages with User confirmation; `test_analyze_mece.py -v` 5/5, `test_analyze_trace.py -v` 8/8, `test_get_need_links.py -v` 9/9, `docs/test_docs_build.py -v` 4/4. | None. | The build validates the current Syspilot tree; synthetic `[needs]`-only navigation is covered by focused tests, not a separate installed-project acceptance run. |

Quality communicates its `proceed` judgment and supporting evidence directly to the Project Manager before the Project Manager presents the verified outcome for validation. Another actor's forwarded claim does not establish Quality's decision.

### Open Quality Issues

| Artifact | Current issue | Required outcome |
|---|---|---|
| None | | |

## User Validation And Approval

**Owner:** User<br>
**Recorded by:** Project Manager<br>
**Status:** not applicable

Quality's `proceed` judgment verifies that the change is ready for validation; it does not validate user value. For an included validation, the Project Manager presents the observable outcome after receiving Quality's direct judgment and evidence. The User communicates the validation decision directly to the Project Manager, who records the decision and evidence. Another actor's forwarded claim does not establish the User's decision. If the user requests changes, the Project Manager transfers responsibility to an included artifact owner that can produce the required outcome.

Quality transferred responsibility to the User at `da0b497`. After the Project Manager presented the reviewed outcome, the User explicitly delegated validation of this finished outcome and agreed to assess the integrated state separately in a Jarvis Change. Responsibility returned to the Project Manager for Closure; this does not imply that practical validation occurred.

Set this artifact to `not applicable` only when the User explicitly delegates validation of the finished outcome and that delegation is recorded in its artifact row. Operation mode does not delegate validation. In unattended mode, keep it `pending` until the User returns.

**Decision and evidence:** On 2026-09-23 the User replied "agreed" to the Project Manager's explicit proposal to mark this Contract's User validation `not applicable`, integrate it into `development`, and evaluate it separately in a Jarvis Change. This is a delegation, not acceptance of a tested Jarvis integration. Any findings from the separate evaluation require their own Change against the integrated state.

## Closure

**Owner:** Project Manager<br>
**Status:** closed

- [x] Every included artifact or gate has terminal status and completion evidence.
- [x] Intent and outcome are `approved`.
- [x] Quality has recorded a `proceed` judgment.
- [x] Open Quality Issues contains `None`.
- [x] User validation is `accepted`, or its `not applicable` status and explicit User delegation are recorded in the artifact row.
- [x] Current blocker is `none`.
- [x] The observable outcome is demonstrated.

**Final outcome:** Trace and Impact navigate configured Sphinx-Needs links without mandatory Syspilot graph metadata; focused acceptance, Quality review, and the default strict build passed. User validation of this outcome did not occur: the User explicitly delegated it and agreed to evaluate the integrated state separately in a Jarvis Change. Any findings there require new Changes. This feature branch is squash-integrated into `development` in the commit that records this closure; no push or release is implied.