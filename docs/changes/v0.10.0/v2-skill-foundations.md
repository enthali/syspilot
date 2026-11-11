# Change Contract: V2 Skill Foundations

**Status:** closed<br>
**Process owner:** Syspilot Project Manager<br>
**Current responsibility:** Syspilot Project Manager<br>
**Current blocker:** none<br>
**Created:** 2026-08-25<br>
**Branch:** feature/v2-skill-foundations<br>
**Collaboration mode:** Autonomous. On 2026-08-25 the User explicitly delegated specification, focused implementation, verification, Quality review, and Closure for Impact Python and Ontology, and later directly authorized the generic ontology-driven Impact correction required by Quality. User validation is not applicable when the expanded observable outcome is demonstrated without expanding Ontology behavior.

## Intent And Outcome

**Owner:** Syspilot Project Manager<br>
**Status:** approved<br>
**Approval evidence:** The User directly authorized this autonomous Change on 2026-08-25 before leaving for approximately two hours. The User initially required Impact Python to remain unchanged, then directly expanded the approved intent on 2026-08-25 after Quality exposed the incompatibility: Impact Python shall receive a focused, generic ontology-driven compatibility correction, including truthful Skill authority and focused tests. Ontology remains focused, and the already reviewed Ask Questions, Branching, and Orchestration Jarvis v1 remnants remain removed.

### Goal

Give Impact Python and Ontology proper v2 product intent and requirements, make Impact traversal generic across active project ontologies, focus Ontology on technical operation rather than v1 governance, and remove the three confirmed v1-only skills from the installed v2 artifact set.

### Value

Syspilot v2 retains only skills with a distinct technical capability, makes their purpose and verification explicit in the product model, and avoids parallel governance sources that conflict with Contract Driven Development.

### Scope

- Define one v2 User Story and suitable Requirements and Verification Criteria for `.github/skills/syspilot.impact-python/` and correct it to traverse standard and active-ontology custom link options generically.
- Read custom link options from the active ontology's `[[needs.extra_links]]`, supporting current v2 and customer-defined relationships without hard-coded Syspilot link names.
- Correct Impact Skill guidance so query output informs Contract-owned scope and evidence without becoming parallel authority.
- Add focused tests for v2 and synthetic customer links, directions, depth, de-duplication, cycle protection, output modes, and explicit failure behavior.
- Reverse-engineer one v2 User Story and suitable Requirements and Verification Criteria for `.github/skills/syspilot.ontology/`.
- Focus the Ontology skill on explaining and safely applying the current v2 ontology schema and technical validation.
- Remove v1 ownership tables, obsolete actor names, CR/migration-governance language, stale metadata, and other behavior unsupported by the current v2 ontology or Contract model from the Ontology skill.
- Preserve ontology decisions and responsibility in the applicable Contract; do not make the skill a governance authority.
- Preserve Setup's baseline-ontology installation behavior. The separate decision to make User and Project Manager establish the project ontology immediately after Setup is outside this focused Change and remains future Contract work.
- Remove the already reviewed `.github/skills/syspilot.ask-questions/`, `.github/skills/syspilot.branching/`, and `.github/skills/syspilot.orchestration-jarvis/` v1 remnants. Native VS Code questions, applicable Contracts, the Actor Kernel, and Contract Handling already own their useful behavior.
- Assess user-facing documentation impact and update traceability for the new skill specifications.

### Observable Outcome

The specification graph states why and what Impact Python and Ontology provide in v2; Impact Python traverses standard and active-ontology custom links without hard-coded Syspilot relationship names and its guidance preserves Contract scope authority; Ontology contains only current technical schema and validation guidance; the three v1-only skills are absent; strict documentation/schema validation and focused tests pass.

## Artifact Applicability And Ownership

**Applicability:** Each artifact owner decides and updates its own row.<br>
**Status:** complete

| Artifact type | Included | Owner | Completion evidence | Status |
|---|---|---|---|---|
| Intent and outcome | yes | Syspilot Project Manager | Autonomous authority, scope, boundaries, and observable outcome are explicit | approved |
| Product specification and architecture decisions | yes | Syspilot Architect | v2 User Stories, Requirements, Verification Criteria, realization links, and boundaries are complete and checked | complete |
| User-facing documentation | yes | Syspilot Technical Writer | Documentation impact and traceability are current; applicable surfaces build cleanly | complete |
| Implementation and unit verification | yes | Syspilot Developer | Ontology skill is focused, three v1 skills are removed, generic Impact traversal and truthful guidance are implemented, focused checks pass, and Architecture accepted the repaired slice | complete |
| Acceptance test design and results | yes | Syspilot Tester | Black-box checks demonstrate the expanded observable outcome and boundaries | passed |
| Quality review | yes | Syspilot Quality | Current verification judgment is `proceed` and no open quality issue remains | proceed |
| User validation and approval | not applicable: User explicitly delegated autonomous closure for this bounded outcome on 2026-08-25 | User | Autonomous closure records that User validation did not occur | not applicable |
| Closure decision | yes | Syspilot Project Manager | Final outcome, autonomous validation disposition, and integration state are recorded | complete |

## Architecture And Specification

**Owner:** Syspilot Architect<br>
**Status:** complete

### Affected Artifacts

| Artifact | Change | Rationale |
|---|---|---|
| `SYSP_US_IMPACT_QUERY`, `SYSP_AC_IMPACT_QUERY_1`, `SYSP_REQ_IMPACT_QUERY`, `SYSP_VC_IMPACT_QUERY_1` | modify | Require generic active-ontology traversal, customer link support, explicit failures, focused tests, and Contract-owned scope authority |
| `SYSP_US_ONTOLOGY_MANAGEMENT`, `SYSP_AC_ONTOLOGY_MANAGEMENT_1`, `SYSP_REQ_ONTOLOGY_SCHEMA`, `SYSP_REQ_ONTOLOGY_EDITING`, and their VCs | add | Define current technical schema guidance and Contract-owned ontology editing and validation |
| `.github/skills/syspilot.impact-python/SKILL.md`, script, and focused tests | modify / add | Align active guidance and implementation with generic ontology-driven traversal and tested authority boundaries |
| `.github/skills/syspilot.ontology/SKILL.md` | focus | Remove v1 governance and stale schema guidance while retaining technical capability |
| three v1-only skill directories | remove | They are not v2 product capabilities and duplicate native tools, Contracts, or Kernel behavior |
| `docs/architecture.md`, `docs/workflows.md`, `docs/customization.md`, documentation Needs | Technical Writer impact review | Existing user-facing text contains v1 ontology ownership, L2 Spec, and functional Impact traversal claims or explains project ontology customization |

### Decisions And Evidence

| Decision or check | Evidence |
|---|---|
| Pre-edit impact query | `python .github/skills/syspilot.impact-python/scripts/get_need_links.py ROOT_SYSPILOT --direction in --depth 1` returned only the root although `ROOT_SYSPILOT.tracked_by_back` contains every v2 User Story |
| Impact Python baseline | `git diff --exit-code 5b5b94e -- .github/skills/syspilot.impact-python` passed; the observed limitation is unchanged baseline behavior |
| V2 relationship representation | Exported JSON has empty `links` and `links_back` but populated typed fields, including `tracked_by_back` on `ROOT_SYSPILOT` and `implements_back` on User Stories |
| Established-v2 reproduction | Queries from `SYSP_US_CONTRACT_DOCUMENTS` and `SYSP_REQ_CONTRACT_DOCUMENTS` also returned no relationships, proving the mismatch is independent of proposed new Needs |
| User resolution of Quality blocker | User expanded the approved intent to correct Impact Python generically against the active ontology and align Skill authority with Contract Driven Development |
| Generic traversal boundary | Discover link options from active ``[[needs.extra_links]]`` entries and retain standard `links` support; do not hard-code Syspilot v2 or customer relationship names |
| Ontology selection | Use the project's configured ontology where practical; an explicit path option defaulting to the project baseline is acceptable when automatic resolution is not reliable |
| Impact authority | Query output supplies candidate scope and evidence to the applicable Contract; `SKILL.md` must not make output an independent or authoritative scope decision |
| Verification boundary | Focused tests cover current v2 links, a synthetic customer link, standard links, directions, depth, output modes, de-duplication, cycle protection, and explicit prerequisite/input failures |
| Ontology specification boundary | One mandatory Story and two Requirements separate current v2 schema guidance from Contract-owned technical editing and strict validation; Setup baseline behavior and future post-Setup ontology establishment remain unchanged |
| Traceability verification | Exported Needs JSON links both Stories to `ROOT_SYSPILOT`, their Requirements through `implements_back`, and their ACs through `validates_back`; each VC verifies its Requirement |
| Specification validation | Expanded Impact Story, Requirement, AC, and VC passed `python docs/docs-build.py clean` with zero Sphinx/schema warnings and `git diff --check` |
| Impact implementation review | Architecture independently reproduced the standard-only and unequal-length convergence regressions after repair, confirmed both fixes and retained behavior, and accepted the uncommitted slice with no remaining findings on 2026-08-25 |

## User-Facing Documentation

**Owner:** Syspilot Technical Writer<br>
**Status:** complete

### Documentation Plan And Ownership

| Documentation surface | `doc` Need | Requirements included | Status |
|---|---|---|---|
| `docs/change-workflow.md` | `SYSP_DOC_CHANGE_WORKFLOW` | `SYSP_REQ_IMPACT_QUERY` | verified |
| `docs/customization.md` | `SYSP_DOC_CUSTOMIZATION` | `SYSP_REQ_ONTOLOGY_SCHEMA`, `SYSP_REQ_ONTOLOGY_EDITING` | verified |
| `docs/architecture.md`, `docs/workflows.md` | Legacy v1 guides; no current `doc` Need | Explicitly bound stale ontology and hierarchy claims while aligning the Impact boundary with repaired generic traversal | complete |

### Consultations And Factual Reviews

| Documentation surface | Consulted artifact owner | Review question | Evidence and disposition |
|---|---|---|---|
| Current Impact guidance | Syspilot Architect | Does documentation explain generic ontology-driven traversal and preserve Contract-owned scope authority? | accepted; Architecture confirmed the Skill accurately describes ontology-driven discovery and leaves candidate disposition and scope authority with the applicable Contract |

### Changed Documentation And Verification

| Artifact | Change | Verification evidence |
|---|---|---|
| `docs/change-workflow.md` and `SYSP_DOC_CHANGE_WORKFLOW` | Replace the former compatibility warning with tested generic traversal and Contract scope-authority guidance | Eight focused Impact tests and four docs tests passed; clean strict Sphinx/schema build passed with zero warnings; targeted wording scan and editor diagnostics passed |
| `docs/workflows.md` | Retain the legacy v1 workflow boundary while replacing its obsolete typed-link incompatibility statement | Strict build and targeted wording scan passed; the page remains explicitly historical and points to current Change guidance |
| Ontology and remaining legacy v1 documentation surfaces | Existing focused Ontology guidance and explicit legacy boundaries remain applicable | Rechecked during expanded documentation review; no correction required |

## Implementation And Unit Verification

**Owner:** Syspilot Developer<br>
**Status:** complete

### Decisions And Evidence

| Decision | Chosen approach | Relevant alternatives | Rationale and evidence |
|---|---|---|---|
| Ontology guidance boundary | Describe only the current v2 schema and Contract-owned technical editing and validation | Preserve v1 ownership tables, actor assignments, and CR/migration classification | The current ontology has no centralized ownership mapping; applicable Contracts own decisions and evidence, while the skill supplies schema coherence and strict validation steps |
| Impact implementation | Parse every configured `option` from the ontology's optional `[[needs.extra_links]]`; traverse each option and its `_back` field alongside standard links; track the minimum depth reached for each ID; inject ontology and Needs-data paths through CLI options | Hard-coded v2 link names, mandatory custom-link configuration, or unchanged generic-link-only traversal | Standard-only ontologies and synthetic customer links pass without code changes; a shallower converging path still expands valid descendants; the real `ROOT_SYSPILOT` query returns all 14 incoming v2 User Stories |
| Impact failure boundary | Exit non-zero for unreadable or invalid ontology, unavailable Needs data, unusable build prerequisites, and unknown Need IDs | Return successful empty/error JSON or continue after a failed build | Failed prerequisites cannot be mistaken for an authoritative empty impact result; focused CLI tests exercise each failure class |
| Impact authority | Describe results as candidate scope and traceability evidence whose disposition remains in the applicable Contract | Make query output mandatory or independently authoritative | The Skill guidance now matches Contract Driven Development and contains no stale v1 level/SPEC or scope-authority claims |

### Changed Artifacts And Verification

| Artifact | Change | Verification evidence |
|---|---|---|
| `.github/skills/syspilot.ontology/SKILL.md` | Replaced v1 schema, actor ownership, stale metadata, and CR/migration governance with current `[needs]`/`[syspilot]` schema guidance, Contract-owned editing, coherence checks, strict validation, and Setup preservation boundary | Required v2-term and frontmatter checks pass; stale actor, type, metadata, and governance wording scan returns no matches |
| `.github/skills/` installable tree | Confirmed `syspilot.ask-questions`, `syspilot.branching`, and `syspilot.orchestration-jarvis` are absent; removed the residual empty Branching directory | Directory inventory contains exactly `syspilot.impact-python` and `syspilot.ontology` |
| `.github/skills/syspilot.impact-python/SKILL.md` and script | Implemented optional configured-ontology option discovery, standard and dynamic forward/back traversal, minimum-depth-aware convergence handling, configurable data paths, explicit failures, and Contract-owned candidate-scope guidance | Pylance reports no syntax errors or diagnostics; stale v1 guidance scan returns no matches; real `ROOT_SYSPILOT --direction in --depth 1 --flat --no-build` returns 14 User Stories |
| Impact focused tests | Added temporary ontology and per-ID JSON fixtures covering v2, customer-defined and standard-only ontologies, all directions, depth, flat/simple/nested output, de-duplication, cycles, unequal-length converging paths, and prerequisite/input failures | `python .github/skills/syspilot.impact-python/scripts/test_get_need_links.py -v` passes 8/8 tests, including rejection of malformed `extra_links` configuration |
| Documentation and schema verification | Revalidated the expanded uncommitted implementation state | `python docs/docs-build.py clean` passes with zero Sphinx/schema warnings; `python docs/test_docs_build.py -v` passes 4/4; `git diff --check` passes apart from Git's informational line-ending warning |

## Acceptance Testing

**Owner:** Syspilot Tester<br>
**Status:** passed

| Scenario | Traces to | Result | Evidence |
|---|---|---|---|
| Impact Python traverses current v2 typed links in both directions and to the requested depth | observable outcome, `SYSP_REQ_IMPACT_QUERY` | pass | A black-box CLI oracle independently derived expected links from the active ontology and exported per-ID Needs data: `ROOT_SYSPILOT` returned exactly 14 incoming elements at depth 1 and 44 at depth 2; outgoing and combined direct queries also matched their typed export fields |
| A synthetic customer-defined extra link is discovered without a code change or hard-coded option name | ontology portability | pass | An isolated ontology declared only `customer_rel`; the unchanged CLI returned the expected outgoing depth-2, incoming depth-1, and combined direct results, while `customer_rel` was absent from the implementation source |
| Standard links, output modes, de-duplication, cycle protection, and explicit failure behavior match the Requirement | technical contract | pass | A standard-only cyclic fixture passed flat, simple, and nested outputs, returned converging IDs once, and emitted truncated cycle nodes; unknown Need, missing or invalid ontology, missing Needs data, and unusable build prerequisite each returned explicit non-zero results; focused Impact tests passed 8/8 |
| Ontology skill describes only current v2 schema and technical validation | observable outcome, `SYSP_REQ_ONTOLOGY_SCHEMA`, `SYSP_REQ_ONTOLOGY_EDITING` | pass | A TOML parser compared the skill with `.syspilot/ontology.toml`: exact v2 types, statuses, options, links, type-link references, transition endpoints, Contract-owned editing, strict validation, and Setup boundary matched; selected stale v1 governance terms were absent |
| Removed v1 skills are absent from the installable skill tree | observable outcome | pass | Directory inventory contained exactly `syspilot.impact-python` and `syspilot.ontology`; `syspilot.ask-questions`, `syspilot.branching`, and `syspilot.orchestration-jarvis` paths were absent |
| New specification elements trace to retained skill realizations and strict build succeeds | observable outcome | pass | Fresh `needs.json` contained both Stories, three Requirements, and three VCs with expected reverse links and approved realization paths; clean documentation/schema build passed with zero warnings and focused tests passed 4/4 |

## Quality Review

**Owner:** Syspilot Quality<br>
**Status:** proceed

**Current judgment:** Proceed. The expanded Impact implementation resolves the prior product-boundary contradiction: active Skill guidance treats results as Contract-owned candidate scope, and the script discovers standard plus arbitrary ontology-declared links without hard-coded Syspilot relationship names. Eight focused tests cover directions, depth, output modes, de-duplication, cycles, unequal-length convergence, standard-only and customer-defined ontologies, and explicit failures. An independent oracle matched all 14 direct incoming `ROOT_SYSPILOT` IDs derived from the active ontology and per-ID Needs data. Ontology guidance matches the current v2 schema, the installable inventory contains exactly the two retained skills, strict documentation and schema validation passes with zero warnings, all four documentation tests pass, stale active claims are absent, and no open Quality issue remains.

### Open Quality Issues

None.

## User Validation And Approval

**Owner:** User<br>
**Recorded by:** Syspilot Project Manager<br>
**Status:** not applicable

**Decision and evidence:** The User explicitly authorized autonomous specification, focused implementation, verification, Quality review, integration, and Closure for this bounded Change on 2026-08-25. User validation will not occur during autonomous execution and must not be claimed.

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

**Final outcome:** Under the User's autonomous authority, Syspilot v2 now specifies and verifies its two retained technical skills. Impact Python discovers standard and arbitrary active-ontology link types, reports explicit prerequisite failures, and supplies candidate evidence without replacing Contract scope authority. Ontology guidance now reflects the current v2 schema and Contract-owned editing boundary. The three v1-only Ask Questions, Branching, and Orchestration Jarvis skills are absent. Quality recorded direct `proceed` evidence in `1c996fe`; User validation did not occur and is correctly not applicable. The Syspilot Project Manager closed the Change and integrated `feature/v2-skill-foundations` into `development` by squash.
