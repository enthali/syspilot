# Change Contract: MECE And Trace Quality Skills

**Status:** closed<br>
**Process owner:** Syspilot Project Manager<br>
**Current responsibility:** none, the Contract is closed<br>
**Current blocker:** none<br>
**Created:** 2026-08-27<br>
**Branch:** feature/mece-trace-skills<br>
**Collaboration mode:** Autonomous after Contract release. Each artifact owner decides within the released scope and escalates only genuine blockers or decisions outside that authority. The User reviews the complete proposed Contract before work starts and performs final validation after Quality can proceed. Autonomous execution does not waive or replace final User validation.

## Intent And Outcome

**Owner:** Syspilot Project Manager<br>
**Status:** approved<br>
**Approval evidence:** The User reviewed the complete proposed Contract, required explicit MECE horizontal peer scope and Trace traversal-depth control, and released it for autonomous execution on 2026-08-27. Final User validation remains required.

**Amendment (2026-08-27, Project Manager, pending User confirmation):** Value, Scope, and negative verification below were narrowed to the capability the active ontology can support, resolving Quality finding Q-03. The User was unavailable and had authorized best-guess decisions during autonomous execution, so this narrowing is recorded as a decision to confirm or reverse at final User validation rather than as an approved scope change. Reason: `[[syspilot.type_links]]` declares which relationships are permitted, not which are required, and 7 of 18 Requirements legitimately hold no `specializes`; detecting an absent relationship would therefore require treating every permitted triple as mandatory and would misreport valid objects. Making requiredness expressible is a separate ontology decision, recorded as a follow-up rather than absorbed here.

### Goal

Restore MECE and Trace as explicit, ontology-driven quality methods in Syspilot v2 through two focused Skills, and require Syspilot Quality to apply both methods in every Quality Review starting from the impacted objects recorded by the active Contract.

### Value

A Quality judgment no longer depends on an undefined general instruction to review holistically. Every review applies two distinct, inspectable methods: MECE exposes overlap, duplication, contradiction, and missing coverage; Trace exposes unresolved relationship targets, relationship types and directions the active ontology does not declare, objects holding no declared relationship in either direction, and semantic drift across linked artifacts. Whether a permitted relationship is absent is outside this capability, because the active ontology declares permission rather than requiredness.

### Scope

- Extract durable MECE and Trace method knowledge from the historical `v0.9.1` Agent, Requirement, Design, Change, and verification records. Treat those files as evidence, not as templates to copy.
- Add `syspilot.mece` and `syspilot.trace` as focused Skills under `.github/skills/`, with any small supporting scripts and tests justified by the chosen design.
- Keep both Skills ontology-driven. They must use the active ontology's types and relationships rather than hard-coded v1 Need types, US/REQ/SPEC levels, link names, or a universal linear hierarchy.
- Define the impacted-object set recorded in the active Contract as the mandatory starting point for both methods. Use `syspilot.impact-python` to obtain relevant incoming and outgoing graph context where built Sphinx-Needs data is available.
- Define MECE as primarily horizontal coverage analysis among comparable objects: Story against Story, Requirement against Requirement, and equivalent peer types declared by a customer ontology. For each impacted object, peer discovery must support at least two caller-selected scopes: peers in the same source file or all peers of the relevant type. The method then checks complete item coverage, overlap or duplicated obligation, contradiction, missing coverage, ambiguous partitioning, and responsibility-boundary collision. Do not retain the v1 rule that every run checks exactly one hard-coded specification level.
- Define Trace as a relationship and semantic-chain assessment starting from each selected impacted object. It primarily traverses the ontology tree vertically toward intent, realization, and verification, while also checking relevant horizontal relationships and every existing linked neighbor needed for semantic consistency. Traversal depth must be a caller-selected parameter so a review can intentionally inspect direct neighbors only or dependencies to the second, third, fourth, or requested deeper degree. The method checks valid targets, permitted relationship types and directions, orphan detection, and re-verification when only one side of an existing relationship changed. It does not judge a permitted relationship to be missing, because the active ontology declares no requiredness or cardinality from which such a judgment could follow.
- Require an explicit implementation decision for graph discovery. Trace may reuse the tested traversal script supplied by `syspilot.impact-python` or introduce its own focused traversal script only when the Architect and Developer record why reuse cannot satisfy Trace semantics. MECE requires script support that deterministically discovers and reports the selected horizontal peer set, with at least `same file` and `all comparable objects` modes; this may share structured parsing or traversal helpers where doing so preserves the distinct MECE and Trace responsibilities.
- Require every Syspilot Quality Review to execute both MECE and Trace. Quality records method scope, evidence, findings, limitations, and one holistic `proceed` or `blocked` judgment in the active Contract.
- Preserve separation of concerns: `impact-python` discovers graph context; MECE and Trace evaluate different quality properties; the Contract owns scope, artifact ownership, findings, responsibility, and decisions.
- Keep both Skills read-only with respect to versioned product artifacts and the active Contract. They return findings and evidence; they do not fix artifacts, make product decisions, transfer responsibility, or introduce a second Quality actor.
- Add or update Stories, Requirements, Verification Criteria, Quality role material, Change Process/template language, documentation ownership links, and user-facing guidance needed to make this behavior authoritative and understandable.
- Verify both Skills against the current v2 ontology and at least one synthetic customer ontology with different type and relationship names. Include negative cases for unresolved relationship targets, undeclared relationship type or direction, orphaned objects, overlapping obligations, contradictions, and incomplete coverage.
- Dogfood both Skills during this Change's final Quality Review. Because Quality cannot independently validate a method solely by trusting that method's own output, retain executable fixtures and direct evidence for the method behavior.
- Do not restore MECE or Trace Actors, v1 Agent files, manager orchestration, fixed L0/L1/L2 sequencing, deprecated v1 types, generic `:links:` assumptions, or a standing workflow outside the Contract.
- Preserve unrelated `.github/agents/`, private Actor memory, Jarvis runtime state, release work, branching-governance work, ontology-reference delivery work, and all other pre-release blockers.
- Do not push the public Syspilot repository without explicit User authorization.

### Observable Outcome

The current specification graph defines distinct MECE and Trace quality capabilities and requires Quality to run both for every Quality Review. The two installed Skills accept Contract-recorded impacted objects, expose MECE peer scope and Trace traversal depth as explicit inputs, operate through active-ontology relationships, produce reproducible structured findings with explicit limits, and remain read-only. MECE script evidence reports the exact horizontal peer set checked; Trace evidence reports the exact depth-bounded relationship tree checked. Focused tests demonstrate both current-v2 and synthetic-ontology behavior, the strict documentation/schema build passes with zero warnings, Quality dogfoods both methods and records a direct judgment, and the User can inspect and accept the resulting methods without any restored v1 Actor or workflow.

## Artifact Applicability And Ownership

**Applicability:** Each artifact owner decides and updates its own row.<br>
**Status:** complete

| Artifact type | Included | Owner | Completion evidence | Status |
|---|---|---|---|---|
| Intent and outcome | yes | Syspilot Project Manager | Goal, value, scope, autonomy boundary, and observable outcome are explicit and User-approved | approved |
| Product specification and architecture decisions | yes | Syspilot Architect | Historical evidence is assessed; v2 method boundaries, ontology behavior, Quality obligation, affected specification objects, and verification approach are explicit and coherent | complete |
| User-facing documentation | yes | Syspilot Technical Writer | Documentation impact is assessed from changed Requirements; applicable `doc` Needs and current guidance are updated and factually reviewed | complete |
| Skill implementation and focused verification | yes | Syspilot Developer | Both read-only Skill packages, deterministic analyzers, and the additive typed Impact output are implemented; focused current-v2, synthetic-ontology, and negative tests pass | complete |
| Acceptance test design and results | yes | Syspilot Tester | Black-box scenarios demonstrate distinct MECE/Trace behavior, mandatory Quality use, read-only boundaries, and ontology-agnostic inputs | passed |
| Quality review | yes | Syspilot Quality | Quality independently re-dogfooded both methods across all 12 impacted specification objects; Q-01, Q-02, and Q-03 are resolved, with the Intent amendment explicitly pending final User confirmation | complete |
| User validation and approval | yes | User | The User accepts the complete Quality-approved methods and their mandatory use | accepted |
| Closure decision | yes | Syspilot Project Manager | Final outcome, validation disposition, integration state, and remaining limitations are recorded | complete |

## Architecture And Specification

**Owner:** Syspilot Architect<br>
**Status:** complete

### Historical Evidence Sources

| Source | Intended use | Excluded v1 mechanism |
|---|---|---|
| `v0.9.1:syspilot/agents/syspilot.mece.agent.md` and `req/spec_quality_mece.rst` | Horizontal peer coverage, overlap, gap, contradiction, structured findings, read-only behavior | Agent identity, fixed level input, hard-coded US/REQ/SPEC vocabulary, Agent workflow |
| `v0.9.1:syspilot/agents/syspilot.trace.agent.md` and `req/spec_quality_trace.rst` | Depth-bounded bidirectional tracing from one object, valid links, semantic consistency, orphans, modified-neighbor re-verification | Agent identity, fixed linear US→REQ→SPEC chain, hard-coded `:links:`, Agent workflow |
| Historical Change and verification records referencing MECE/Trace | Observed defects, useful checks, limits, and failure patterns | Former manager dispatch sequence and role topology |

### Affected Artifacts

| Artifact | Change | Rationale |
|---|---|---|
| `SYSP_US_QUALITY_METHODS`, `SYSP_AC_QUALITY_METHODS_1` | add | One WHY governs both methods: a quality judgment must rest on named, inspectable analysis instead of an undefined instruction to review holistically |
| `SYSP_REQ_MECE_ANALYSIS`, `SYSP_VC_MECE_ANALYSIS_1` | add | Define horizontal coverage analysis, its two caller-selected peer scopes, its deterministic peer reporting, and its read-only boundary |
| `SYSP_REQ_TRACE_ANALYSIS`, `SYSP_VC_TRACE_ANALYSIS_1` | add | Define depth-bounded relationship analysis evaluated against the relationship types and directions the active ontology declares |
| `SYSP_REQ_QUALITY`, `SYSP_VC_QUALITY_1` | modify | Make both methods a mandatory and recorded part of every Quality Review rather than optional technique |
| `SYSP_REQ_IMPACT_QUERY`, `SYSP_VC_IMPACT_QUERY_1` | modify | Add an opt-in per-pair output naming the connecting link option and direction, so Trace can evaluate relationship types without a second traversal implementation |
| `.github/skills/syspilot.mece/`, `.github/skills/syspilot.trace/` and their supporting scripts and tests | add, Developer-owned | Realize the two new Requirements as focused read-only Skills |
| Existing user-facing surfaces whose `doc` Needs include `SYSP_REQ_QUALITY` or `SYSP_REQ_IMPACT_QUERY` | Technical Writer impact review | Those Requirements changed, so their documentation consumers require an owner assessment |
| `SYSP_REQ_CHANGE_CONTRACT`, `SYSP_VC_CHANGE_CONTRACT_1` | modify | Require every Change Contract to record the applied review methods with their scope, evidence, findings, and limits, so the Quality duty has a specified place to be recorded and its absence is detectable |
| `SYSP_VC_QUALITY_1` | modify | Verify that the Quality role realization states the method obligation, not only that a quality artifact records results |
| `docs/Syspilot Actors/Syspilot Quality.md` | modify, Developer-owned | The realization of `SYSP_REQ_QUALITY` omits the method obligation the Requirement states |
| `docs/Syspilot Processes/change.md` canonical `Quality Review` section | modify, Developer-owned | The canonical template must carry the method result fields that the corrected `SYSP_REQ_CHANGE_CONTRACT` specifies |
| `SYSP_REQ_TRACE_ANALYSIS`, `SYSP_VC_TRACE_ANALYSIS_1` | modify | Narrow the relationship obligation to evidence the active ontology can express, and require that an optional permitted relationship produce no finding |

### Decisions And Evidence

| Decision or check | Evidence |
|---|---|
| One Story with two Requirements | The WHY is single, while MECE and Trace are distinct WHATs. This follows the established v2 shape of `SYSP_US_ONTOLOGY_MANAGEMENT`, which carries `SYSP_REQ_ONTOLOGY_SCHEMA` and `SYSP_REQ_ONTOLOGY_EDITING` |
| Comparable peer definition | A peer is an object of the same active-ontology type. Built per-ID Needs data exposes populated `type` and `docname` fields, so both required scopes, same source document and all peers of the type, are derivable without hard-coded Syspilot type names |
| MECE keeps no fixed level | The v1 duty "exactly one level (L0, L1, or L2)" depends on the removed US/REQ/SPEC hierarchy; peer scope is now the caller-selected input instead |
| Trace reuses the Impact traversal | Reimplementing depth-bounded traversal would duplicate the de-duplication and cycle logic in which this repository already produced a defect: the converging-path bug repaired by `minimum_depth_by_id` during V2 Skill Foundations. A second implementation would reopen that defect class |
| Reuse alone is insufficient without typed edges | Probe: `get_need_links.py SYSP_REQ_QUALITY --direction both --depth 1` returned `SYSP_REQ_ACTOR_MODEL` and `SYSP_US_QUALITY` inside one undifferentiated `links` array, although the source data distinguishes `specializes` from `implements`. `linked_ids()` merges every option into one set, so relationship type is discarded during traversal |
| Additive typed-edge output instead of a separate Trace traversal | Naming the connecting option and direction is graph-context discovery, which is already the Impact skill's concern. The extension is opt-in and leaves the default output unchanged, so the single verified traversal continues to serve both skills |
| Ontology rule evaluation belongs to Trace | The Impact skill reads only `[[needs.extra_links]]` to know what it may traverse. Judging whether an observed edge is permitted requires `[[syspilot.type_links]]`, which the Impact skill deliberately does not read. Evaluating actual edges against those declared relationships is the distinct Trace responsibility |
| Both skills stay ontology-agnostic | Types come from built specification data and permitted relationships from the active ontology, so a customer ontology with different type and relationship names needs no code change; each Verification Criterion requires a synthetic-ontology case |
| Both skills stay read-only | Each Requirement forbids correcting artifacts, deciding scope, and transferring responsibility, which preserves the Contract as the sole authority for scope and decisions |
| No new actors and no restored v1 files | The methods are realized as Skills applied by Syspilot Quality; no MECE or Trace actor, agent file, manager dispatch, or L0/L1/L2 sequencing is introduced |
| Historical evidence assessed, not copied | v1 supplied the durable checks: complete item coverage, overlap and gap visibility, link validity, orphan detection, semantic consistency beyond the parent chain, and re-verification when only one side of an existing relationship changed. The v1 Trace workflow already delegated discovery to `get_need_links.py`, which supports reuse. Agent identity, frontmatter, fixed levels, and the hard-coded `:links:` assumption were excluded |
| Specification validation | `python docs/docs-build.py clean` passed with zero Sphinx and schema warnings; `python docs/test_docs_build.py -v` passed 4/4; `git diff --check` passed; editor diagnostics reported no errors |
| Traceability validation | Exported `needs.json` confirms the new Story is tracked by `ROOT_SYSPILOT`, both Requirements resolve through `implements_back`, the Acceptance Criterion resolves through `validates_back`, each Verification Criterion verifies its Requirement, and both Requirements carry their `realized_by` skill paths |
| Open decision left to implementation | If implementation shows that the additive typed-edge output cannot satisfy Trace semantics, the Developer shall escalate so the Architect and Developer record a joint justification, rather than silently introducing a second traversal script |
| Acceptance failure confirmed, not disputed | The Tester's finding reproduces against both realizations: `docs/Syspilot Actors/Syspilot Quality.md` states only that Quality "judges holistically", and the canonical `Quality Review` section of `docs/Syspilot Processes/change.md` contains no method requirement and no result fields, although `SYSP_REQ_QUALITY` obliges Quality to apply both methods and record their scope, evidence, findings, and limits |
| The correction is specification plus realization, not realization alone | Correcting only the role card would leave the recorded result without a specified place, and `SYSP_VC_CHANGE_CONTRACT_1` could not detect its absence, because no Requirement obliged the Contract artifact to carry it. The actor duty and the Contract-artifact structure are two different obligations and both are required for every review to execute and record the methods |
| Placement of the new obligation | The artifact obligation belongs to `SYSP_REQ_CHANGE_CONTRACT`, which governs what a Change Contract records, while `SYSP_REQ_QUALITY` keeps the actor duty. Splitting them this way avoids stating one rule twice and keeps each Verification Criterion able to fail independently |
| The user guide is not a control | `docs/change-contract.md` already explains both methods and includes `SYSP_REQ_MECE_ANALYSIS` and `SYSP_REQ_TRACE_ANALYSIS` through its `doc` Need, but a derived explanation cannot make a review execute or record anything; the control must sit in the specified role realization and the canonical template |
| Realization routing | Process and role realizations are implemented by the Developer inside the Contract, following the Setup Ontology Review precedent in which the Developer realized `docs/Syspilot Processes/setup.md` Phase 7 from Architect-specified intent. The Project Manager remains the process owner and is consulted if the template wording is disputed |
| Correction validation | `python docs/docs-build.py clean` passed with `Schema validation completed with 0 warning(s)` and `build succeeded`; `python docs/test_docs_build.py` passed 4/4; `git diff --check` passed |
| Quality finding Q-01 confirmed | Verified directly against the active ontology and built data: every `[[syspilot.type_links]]` entry carries only `from`, `to`, and `rel`, and the ontology contains no requiredness or cardinality key. 7 of 18 Requirements legitimately hold no `specializes`, including `SYSP_REQ_ACTOR_MODEL`, so treating each permitted triple as mandatory misreports valid objects |
| The defect originated in my specification | `SYSP_REQ_TRACE_ANALYSIS` required reporting "chains that the ontology expects", which asks for evidence the active ontology cannot express. Permission and requiredness are different properties and only permission is declared, so the analyzer had no sound basis for an expectedness judgment |
| Correction chosen | Narrow the obligation to ontology-supported evidence: unresolved targets, undeclared relationship type or direction, and orphans holding no declared relationship in either direction. State explicitly that a declared relationship is permitted rather than required and that its absence is not a finding |
| Requiredness deliberately not invented | Adding requiredness or cardinality would change `SYSP_REQ_ONTOLOGY_SCHEMA`, the Ontology skill, the generated ontology reference, and the Setup baseline, and it is a genuine ontology design decision for the Project Manager and User. The Requirement now records that boundary rather than encoding an assumption |
| Regression guard | `SYSP_VC_TRACE_ANALYSIS_1` now requires a negative case in which a Requirement without `specializes` produces no finding, so the false positive cannot return unnoticed |
| Q-01 correction validation | `python docs/docs-build.py clean` passed with `Schema validation completed with 0 warning(s)` and `build succeeded`; `python docs/test_docs_build.py` passed 4/4; `git diff --check` passed; exported data confirms `SYSP_VC_TRACE_ANALYSIS_1` still verifies `SYSP_REQ_TRACE_ANALYSIS` |

## User-Facing Documentation

**Owner:** Syspilot Technical Writer<br>
**Status:** complete

### Documentation Plan And Ownership

| Documentation surface | `doc` Need | Requirements included | Status |
|---|---|---|---|
| `docs/change-contract.md` | `SYSP_DOC_CHANGE_CONTRACT` | `SYSP_REQ_QUALITY`, `SYSP_REQ_IMPACT_QUERY`, and the added `SYSP_REQ_MECE_ANALYSIS`, `SYSP_REQ_TRACE_ANALYSIS` | verified |
| `docs/product-model.md` | `SYSP_DOC_PRODUCT_MODEL` | `SYSP_REQ_QUALITY`, unchanged link set | verified |
| `.github/skills/syspilot.mece/`, `.github/skills/syspilot.trace/` | none | Skill guidance is Developer-owned realization, not a user-facing `doc` surface | out of scope for this owner |

### Consultations And Factual Reviews

| Documentation surface | Consulted artifact owner | Review question | Evidence and disposition |
|---|---|---|---|
| Quality method description | Not requested; the Architect's decisions and the approved Requirements state the behavior explicitly | Do the guides describe both methods without granting them authority they do not have? | Derived from `SYSP_REQ_QUALITY`, `SYSP_REQ_MECE_ANALYSIS`, and `SYSP_REQ_TRACE_ANALYSIS`: both methods are read-only, start from the Contract-recorded impacted objects, and report scope, evidence, findings, and limits. The guide states this and grants the methods no scope or correction authority |

### Changed Documentation And Verification

| Artifact | Change | Verification evidence |
|---|---|---|
| `docs/change-contract.md` | The Quality section previously described only the `proceed`/`blocked` judgment. It now explains horizontal coverage and relationship analysis in user-oriented terms, including the reported peer scope, the depth-bounded relationship check, the read-only boundary, and why a method must distinguish "found nothing" from "could not look" | Strict Sphinx/schema build passes with zero warnings; `python docs/test_docs_build.py -v` passes 4/4; `git diff --check` passes |
| `docs/product-model.md` | The Quality roster entry no longer reads as an unqualified "independent quality judgment"; it names the analysis the judgment rests on | Same build and test evidence |
| `docs/syspilot/documentation/index.rst` | `SYSP_DOC_CHANGE_CONTRACT` now includes `SYSP_REQ_MECE_ANALYSIS` and `SYSP_REQ_TRACE_ANALYSIS` | Impact query confirms both new Requirements now resolve to `SYSP_DOC_CHANGE_CONTRACT` through `included_in`, so a future change to either method reaches its documentation consumer |

### Impact Assessment

| Requirement | Incoming documentation consumers found | Disposition |
|---|---|---|
| `SYSP_REQ_QUALITY` (modified) | `SYSP_DOC_CHANGE_CONTRACT`, `SYSP_DOC_PRODUCT_MODEL` | Both updated |
| `SYSP_REQ_IMPACT_QUERY` (modified) | `SYSP_DOC_CHANGE_CONTRACT` | The change was an additive, opt-in typed-edge output that does not alter the CLI behavior the guide describes; the existing description remains accurate and was left unchanged deliberately |
| `SYSP_REQ_MECE_ANALYSIS` (added) | none before this Change | Linked to `SYSP_DOC_CHANGE_CONTRACT`, because the guide now explains the method in user-oriented form |
| `SYSP_REQ_TRACE_ANALYSIS` (added) | none before this Change | Linked to `SYSP_DOC_CHANGE_CONTRACT` for the same reason |

## Skill Implementation And Focused Verification

**Owner:** Syspilot Developer<br>
**Status:** complete

### Decisions And Evidence

| Decision | Chosen approach | Relevant alternatives | Rationale and evidence |
|---|---|---|---|
| Typed Impact discovery | Add opt-in `--typed` output containing source, target, option, direction, and minimum discovery depth; preserve nested, flat, and simple defaults | Change existing formats or write Trace traversal | Existing traversal retains one implementation for depth, de-duplication, convergence, and cycles; all nine Impact regression tests pass |
| MECE automation boundary | Deterministically discover same-type peers from ontology types plus built `type` and `docname`; report structured overlap, contradiction, missing-coverage, and responsibility-collision evidence when fixture/project data supplies claims; always require semantic content review | Hard-code v2 levels or claim text semantics are fully automated | Exact peer scope is reproducible across customer types, while explicit limitations prevent absent structured data or semantic judgment from becoming a clean result |
| Trace evaluation | Import Impact discovery directly, then evaluate resolved edge type/direction against `syspilot.type_links`; report unresolved, undeclared, and zero-relationship orphan findings without treating permitted relationships as required | Duplicate traversal inside Trace or infer requiredness from permitted type links | Direct reuse satisfies the Architecture decision and avoids reopening the repaired converging-path defect; the active ontology exposes no requiredness or cardinality from which an absent-link finding could be derived |
| Traversal boundary | Record per-edge minimum depth and return the exact caller-selected neighborhood | Reimplement or extend traversal inside Trace | Keeps traversal depth, de-duplication, convergence, and cycle behavior in the shared Impact implementation |
| Read-only authority | Skills and scripts emit evidence, findings, and limitations only; the applicable Contract owns scope, decisions, fixes, and responsibility | Let analyzers mutate artifacts or Contract state | Both Skill guides state the prohibition and no implementation path writes project artifacts |

### Changed Artifacts And Verification

| Artifact | Change | Verification evidence |
|---|---|---|
| `.github/skills/syspilot.impact-python/` | Added opt-in typed, depth-bounded relationship pairs without changing default outputs | Impact suite passes 9/9, including standard/custom links, convergence, cycle protection, failures, and typed option/direction/depth output |
| `.github/skills/syspilot.mece/` | Added read-only Skill, deterministic peer/finding analyzer, and focused fixtures | MECE suite passes 5/5 for both peer scopes, repeatability, synthetic type names, overlap, contradiction, missing coverage, responsibility collision, missing data limits, and current v2 data |
| `.github/skills/syspilot.trace/` | Added read-only Skill, Impact-reusing ontology-rule analyzer, and focused fixtures; removed unsupported inference that every permitted type link is required | Trace suite passes 7/7 for depths one through four and six, synthetic and current-v2 links, unresolved/undeclared/orphan findings, semantic limits, and both synthetic and real-v2 regressions proving an optional absent relationship produces no missing-relationship finding |
| `docs/Syspilot Actors/Syspilot Quality.md` | Aligned the compact Quality role realization with its mandatory horizontal coverage and relationship analysis duty | Inspection against `SYSP_VC_QUALITY_1` confirms the role card names both methods, their Contract-recorded impacted-object scope, and the scope, evidence, findings, and limits Quality records |
| `docs/Syspilot Processes/change.md` | Added explicit applied-method fields to the canonical Change Contract Quality Review section | Inspection against `SYSP_VC_CHANGE_CONTRACT_1` confirms fields for method, selected scope, evidence, findings, and limits without imposing a method sequence or duplicating generic Contract handling |
| Complete implementation slice | Added two Skills and changed only the additive Impact surface plus this Contract | Impact passes 9/9, MECE 5/5, and corrected Trace 7/7; Pylance syntax checks and editor diagnostics are clean; real-v2 regression confirms a Requirement without optional `specializes` produces no missing-relationship finding; strict docs/schema build passes with zero warnings; docs tests pass 4/4; `git diff --check` passes |

## Acceptance Testing

**Owner:** Syspilot Tester<br>
**Status:** passed

| Scenario | Traces to | Result | Evidence |
|---|---|---|---|
| Current v2 impacted objects produce distinct MECE and Trace results | observable outcome | pass | Independent CLI reruns covered exactly all 12 Contract-recorded impacted objects: `SYSP_US_QUALITY_METHODS`, `SYSP_AC_QUALITY_METHODS_1`, `SYSP_REQ_MECE_ANALYSIS`, `SYSP_VC_MECE_ANALYSIS_1`, `SYSP_REQ_TRACE_ANALYSIS`, `SYSP_VC_TRACE_ANALYSIS_1`, `SYSP_REQ_QUALITY`, `SYSP_VC_QUALITY_1`, `SYSP_REQ_IMPACT_QUERY`, `SYSP_VC_IMPACT_QUERY_1`, `SYSP_REQ_CHANGE_CONTRACT`, and `SYSP_VC_CHANGE_CONTRACT_1`. All 24 MECE runs, covering both `same-document` and `all-type`, and all 12 Trace runs with `--direction both --depth 2` returned the requested start object. Same-document/all-type peer counts were 0/14 for the Story and AC, 1/17 for each new method Requirement and VC, and 0/17 for the other six objects; Trace neighborhoods contained respectively 22, 5, 17, 4, 17, 4, 28, 6, 17, 4, 24, and 6 objects, with no structural findings |
| Synthetic ontology uses different type and relationship names without method changes | ontology-agnostic scope | pass | The unchanged analyzers accepted a temporary ontology using only `capability` and `flows_to`; both methods returned the expected structured scope, edges, findings, and limitations without Syspilot type or relationship names |
| MECE reports the exact peer set for both same-file and all-comparable-object scopes | MECE horizontal scope | pass | The synthetic fixture returned exactly `N1` for same-document and `BAD`, `N1` through `N6`, and `ORPHAN` for all-type; a repeated same-document run was byte-identical |
| Trace reports different complete neighborhoods for depths one through four and a caller-selected deeper value | Trace traversal depth | pass | Synthetic `N0` traversal returned exactly `N0` through `N<depth>` for depths 1, 2, 3, 4, and caller-selected depth 6 |
| Unresolved, undeclared, orphaned, overlapping, contradictory, and incomplete cases are detected | method requirements | pass | Synthetic MECE reported overlap, contradiction, missing coverage, and responsibility collision; Trace reported unresolved target, undeclared relationship, and orphan findings. Optional absent relationships produced no finding because the active ontology declares permission but not requiredness. Focused suites passed MECE 5/5, Trace 7/7, and shared Impact 9/9 |
| Skills remain read-only and do not transfer Contract responsibility | authority boundary | pass | Running both CLIs left the Contract blob `5a7a649c520dc89043dbc72647721a73b2f2a97a` and complete pre-existing Git status unchanged; both outputs retained `semantic-content-review-required`, and responsibility remained with Tester until this recorded handoff |
| Quality Review requires and records both method results | Quality obligation | pass | The initial run found that the Requirement was not realized by the Quality role card or canonical Contract. After correction, a structural rerun confirmed that the role mandates both methods for Contract-recorded impacted objects and records selected scope, evidence, findings, and limits; the canonical Quality Review block provides repeatable fields for each dimension, satisfying `SYSP_VC_QUALITY_1` and `SYSP_VC_CHANGE_CONTRACT_1` without a fixed sequence |

## Quality Review

**Owner:** Syspilot Quality<br>
**Status:** complete

**Current judgment:** `proceed`

The delivered methods are coherent with the amended Intent, independently reproducible, and supported by focused current-v2 and synthetic-ontology evidence. The pending User confirmation of the Intent amendment is preserved for final validation and is not replaced by this Quality judgment.

Quality shall execute the delivered MECE and Trace Skills from this Contract's impacted objects and compare their results with the independently inspectable fixtures and artifacts. Self-use is dogfooding evidence, not sufficient proof by itself.

### Applied Review Methods

| Method | Selected scope | Evidence | Findings | Limits |
|---|---|---|---|---|
| MECE horizontal coverage | Both `same-document` and `all-type` for all 12 impacted objects: `SYSP_US_QUALITY_METHODS`, `SYSP_AC_QUALITY_METHODS_1`, `SYSP_REQ_MECE_ANALYSIS`, `SYSP_VC_MECE_ANALYSIS_1`, `SYSP_REQ_TRACE_ANALYSIS`, `SYSP_VC_TRACE_ANALYSIS_1`, `SYSP_REQ_QUALITY`, `SYSP_VC_QUALITY_1`, `SYSP_REQ_IMPACT_QUERY`, `SYSP_VC_IMPACT_QUERY_1`, `SYSP_REQ_CHANGE_CONTRACT`, and `SYSP_VC_CHANGE_CONTRACT_1` | Fresh strict build data; exact all-type peer sets were the 15 Story IDs, 15 AC IDs, 18 Requirement IDs, and 18 VC IDs in the built project; same-document peers were the corresponding MECE/Trace pair for each new Requirement and VC and none for the other impacted objects. Quality read the complete normalized content of all four peer sets and reran the focused suite, which passed 5/5 | No overlap, contradiction, missing semantic coverage, ambiguous partition, or responsibility collision found. The common Story correctly separates into two method Requirements; Quality, Impact, and Change Contract obligations remain distinct | Project Needs contain no `quality_claims` or `expected_coverage`, so automation reports `structured-coverage-data-unavailable`; semantic content review by Quality supplied the judgment the analyzer cannot automate |
| Trace relationship and chain analysis | `--direction both --depth 2` for the same 12 impacted objects | Fresh strict build data; exact neighborhoods are recorded below. Quality read all resolved impacted objects and their relevant intent, verification, role, process, documentation, and specialization neighbors. The independent rerun returned neighborhood counts `22, 5, 17, 4, 17, 4, 28, 6, 17, 4, 24, 6` in Contract order, matching Acceptance exactly; focused Trace passed 7/7 and shared Impact passed 9/9 | Q-01's false `missing-expected-relationship` findings are corrected: every existing edge resolved and matched a permitted type/direction rule, and all 12 starts returned no structural finding. The implementation now correctly refrains from inferring requiredness from permitted type links | `semantic-content-review-required` was discharged by this review. Absent permitted relationships remain outside the delivered capability because the ontology exposes no requiredness or cardinality; the amended Intent states that limit explicitly and preserves User confirmation for final validation |

### Exact All-Type Peer Sets

| Type | Exact IDs |
|---|---|
| Story | `SYSP_US_ACTOR_MODEL`, `SYSP_US_ARCHITECT`, `SYSP_US_CHANGE_CONTRACT`, `SYSP_US_CONTRACT_DOCUMENTS`, `SYSP_US_DEVELOPER`, `SYSP_US_IMPACT_QUERY`, `SYSP_US_ONTOLOGY_MANAGEMENT`, `SYSP_US_PROJECT_MANAGER`, `SYSP_US_QUALITY`, `SYSP_US_QUALITY_METHODS`, `SYSP_US_RELEASE`, `SYSP_US_RESEARCH`, `SYSP_US_SETUP`, `SYSP_US_TECHNICAL_WRITER`, `SYSP_US_TESTER` |
| AC | `SYSP_AC_ACTOR_MODEL_1`, `SYSP_AC_ARCHITECT_1`, `SYSP_AC_CHANGE_CONTRACT_1`, `SYSP_AC_CONTRACT_DOCUMENTS_1`, `SYSP_AC_DEVELOPER_1`, `SYSP_AC_IMPACT_QUERY_1`, `SYSP_AC_ONTOLOGY_MANAGEMENT_1`, `SYSP_AC_PROJECT_MANAGER_1`, `SYSP_AC_QUALITY_1`, `SYSP_AC_QUALITY_METHODS_1`, `SYSP_AC_RELEASE_1`, `SYSP_AC_RESEARCH_1`, `SYSP_AC_SETUP_1`, `SYSP_AC_TECHNICAL_WRITER_1`, `SYSP_AC_TESTER_1` |
| Requirement | `SYSP_REQ_ACTOR_MODEL`, `SYSP_REQ_ARCHITECT`, `SYSP_REQ_CHANGE_CONTRACT`, `SYSP_REQ_CONTRACT_DOCUMENTS`, `SYSP_REQ_CONTRACT_HANDLING`, `SYSP_REQ_DEVELOPER`, `SYSP_REQ_IMPACT_QUERY`, `SYSP_REQ_MECE_ANALYSIS`, `SYSP_REQ_ONTOLOGY_EDITING`, `SYSP_REQ_ONTOLOGY_SCHEMA`, `SYSP_REQ_PROJECT_MANAGER`, `SYSP_REQ_QUALITY`, `SYSP_REQ_RELEASE`, `SYSP_REQ_RESEARCH`, `SYSP_REQ_SETUP`, `SYSP_REQ_TECHNICAL_WRITER`, `SYSP_REQ_TESTER`, `SYSP_REQ_TRACE_ANALYSIS` |
| VC | `SYSP_VC_ACTOR_MODEL_1`, `SYSP_VC_ARCHITECT_1`, `SYSP_VC_CHANGE_CONTRACT_1`, `SYSP_VC_CONTRACT_DOCUMENTS_1`, `SYSP_VC_CONTRACT_HANDLING_1`, `SYSP_VC_DEVELOPER_1`, `SYSP_VC_IMPACT_QUERY_1`, `SYSP_VC_MECE_ANALYSIS_1`, `SYSP_VC_ONTOLOGY_EDITING_1`, `SYSP_VC_ONTOLOGY_SCHEMA_1`, `SYSP_VC_PROJECT_MANAGER_1`, `SYSP_VC_QUALITY_1`, `SYSP_VC_RELEASE_1`, `SYSP_VC_RESEARCH_1`, `SYSP_VC_SETUP_1`, `SYSP_VC_TECHNICAL_WRITER_1`, `SYSP_VC_TESTER_1`, `SYSP_VC_TRACE_ANALYSIS_1` |

### Trace Neighborhoods

| Impacted object | Exact depth-2 neighborhood |
|---|---|
| `SYSP_US_QUALITY_METHODS` | `ROOT_SYSPILOT`, `SYSP_AC_QUALITY_METHODS_1`, `SYSP_DOC_CHANGE_CONTRACT`, `SYSP_REQ_MECE_ANALYSIS`, `SYSP_REQ_TRACE_ANALYSIS`, all 15 Story IDs, `SYSP_VC_MECE_ANALYSIS_1`, `SYSP_VC_TRACE_ANALYSIS_1` |
| `SYSP_AC_QUALITY_METHODS_1` | `ROOT_SYSPILOT`, `SYSP_AC_QUALITY_METHODS_1`, `SYSP_REQ_MECE_ANALYSIS`, `SYSP_REQ_TRACE_ANALYSIS`, `SYSP_US_QUALITY_METHODS` |
| `SYSP_REQ_MECE_ANALYSIS` | `ROOT_SYSPILOT`, `SYSP_AC_QUALITY_METHODS_1`, `SYSP_DOC_CHANGE_CONTRACT`, `SYSP_REQ_ARCHITECT`, `SYSP_REQ_CHANGE_CONTRACT`, `SYSP_REQ_CONTRACT_DOCUMENTS`, `SYSP_REQ_CONTRACT_HANDLING`, `SYSP_REQ_DEVELOPER`, `SYSP_REQ_IMPACT_QUERY`, `SYSP_REQ_MECE_ANALYSIS`, `SYSP_REQ_PROJECT_MANAGER`, `SYSP_REQ_QUALITY`, `SYSP_REQ_TECHNICAL_WRITER`, `SYSP_REQ_TESTER`, `SYSP_REQ_TRACE_ANALYSIS`, `SYSP_US_QUALITY_METHODS`, `SYSP_VC_MECE_ANALYSIS_1` |
| `SYSP_VC_MECE_ANALYSIS_1` | `SYSP_DOC_CHANGE_CONTRACT`, `SYSP_REQ_MECE_ANALYSIS`, `SYSP_US_QUALITY_METHODS`, `SYSP_VC_MECE_ANALYSIS_1` |
| `SYSP_REQ_TRACE_ANALYSIS` | `ROOT_SYSPILOT`, `SYSP_AC_QUALITY_METHODS_1`, `SYSP_DOC_CHANGE_CONTRACT`, `SYSP_REQ_ARCHITECT`, `SYSP_REQ_CHANGE_CONTRACT`, `SYSP_REQ_CONTRACT_DOCUMENTS`, `SYSP_REQ_CONTRACT_HANDLING`, `SYSP_REQ_DEVELOPER`, `SYSP_REQ_IMPACT_QUERY`, `SYSP_REQ_MECE_ANALYSIS`, `SYSP_REQ_PROJECT_MANAGER`, `SYSP_REQ_QUALITY`, `SYSP_REQ_TECHNICAL_WRITER`, `SYSP_REQ_TESTER`, `SYSP_REQ_TRACE_ANALYSIS`, `SYSP_US_QUALITY_METHODS`, `SYSP_VC_TRACE_ANALYSIS_1` |
| `SYSP_VC_TRACE_ANALYSIS_1` | `SYSP_DOC_CHANGE_CONTRACT`, `SYSP_REQ_TRACE_ANALYSIS`, `SYSP_US_QUALITY_METHODS`, `SYSP_VC_TRACE_ANALYSIS_1` |
| `SYSP_REQ_QUALITY` | `ROOT_SYSPILOT`, `SYSP_AC_QUALITY_1`, `SYSP_DOC_CHANGE_CONTRACT`, `SYSP_DOC_CUSTOMIZATION`, `SYSP_DOC_GETTING_STARTED`, `SYSP_DOC_METHODOLOGY`, `SYSP_DOC_PRODUCT_MODEL`, `SYSP_DOC_README`, `SYSP_REQ_ACTOR_MODEL`, all 18 Requirement IDs, `SYSP_US_ACTOR_MODEL`, `SYSP_US_QUALITY`, `SYSP_VC_ACTOR_MODEL_1`, `SYSP_VC_QUALITY_1` |
| `SYSP_VC_QUALITY_1` | `SYSP_DOC_CHANGE_CONTRACT`, `SYSP_DOC_PRODUCT_MODEL`, `SYSP_REQ_ACTOR_MODEL`, `SYSP_REQ_QUALITY`, `SYSP_US_QUALITY`, `SYSP_VC_QUALITY_1` |
| `SYSP_REQ_IMPACT_QUERY` | `ROOT_SYSPILOT`, `SYSP_AC_IMPACT_QUERY_1`, `SYSP_DOC_CHANGE_CONTRACT`, `SYSP_REQ_ARCHITECT`, `SYSP_REQ_CHANGE_CONTRACT`, `SYSP_REQ_CONTRACT_DOCUMENTS`, `SYSP_REQ_CONTRACT_HANDLING`, `SYSP_REQ_DEVELOPER`, `SYSP_REQ_IMPACT_QUERY`, `SYSP_REQ_MECE_ANALYSIS`, `SYSP_REQ_PROJECT_MANAGER`, `SYSP_REQ_QUALITY`, `SYSP_REQ_TECHNICAL_WRITER`, `SYSP_REQ_TESTER`, `SYSP_REQ_TRACE_ANALYSIS`, `SYSP_US_IMPACT_QUERY`, `SYSP_VC_IMPACT_QUERY_1` |
| `SYSP_VC_IMPACT_QUERY_1` | `SYSP_DOC_CHANGE_CONTRACT`, `SYSP_REQ_IMPACT_QUERY`, `SYSP_US_IMPACT_QUERY`, `SYSP_VC_IMPACT_QUERY_1` |
| `SYSP_REQ_CHANGE_CONTRACT` | `ROOT_SYSPILOT`, `SYSP_AC_CHANGE_CONTRACT_1`, `SYSP_DOC_CHANGE_CONTRACT`, `SYSP_DOC_METHODOLOGY`, `SYSP_DOC_PRODUCT_MODEL`, `SYSP_REQ_ACTOR_MODEL`, `SYSP_REQ_ARCHITECT`, `SYSP_REQ_CHANGE_CONTRACT`, `SYSP_REQ_CONTRACT_DOCUMENTS`, `SYSP_REQ_CONTRACT_HANDLING`, `SYSP_REQ_DEVELOPER`, `SYSP_REQ_IMPACT_QUERY`, `SYSP_REQ_MECE_ANALYSIS`, `SYSP_REQ_PROJECT_MANAGER`, `SYSP_REQ_QUALITY`, `SYSP_REQ_RELEASE`, `SYSP_REQ_SETUP`, `SYSP_REQ_TECHNICAL_WRITER`, `SYSP_REQ_TESTER`, `SYSP_REQ_TRACE_ANALYSIS`, `SYSP_US_CHANGE_CONTRACT`, `SYSP_US_CONTRACT_DOCUMENTS`, `SYSP_VC_CHANGE_CONTRACT_1`, `SYSP_VC_CONTRACT_HANDLING_1` |
| `SYSP_VC_CHANGE_CONTRACT_1` | `SYSP_DOC_CHANGE_CONTRACT`, `SYSP_DOC_METHODOLOGY`, `SYSP_REQ_CHANGE_CONTRACT`, `SYSP_REQ_CONTRACT_HANDLING`, `SYSP_US_CHANGE_CONTRACT`, `SYSP_VC_CHANGE_CONTRACT_1` |

The abbreviated Story and Requirement type sets in the Trace table refer exactly to the corresponding enumerated sets above.

### Open Quality Issues

| Artifact | Current issue | Required outcome |
|---|---|---|
| None | None | None |

## User Validation And Approval

**Owner:** User<br>
**Recorded by:** Syspilot Project Manager<br>
**Status:** accepted

Quality's `proceed` judgment verifies that the methods are coherent and supported by evidence; it does not replace the User's final validation. The User communicates the validation decision directly to the Project Manager.

**Decision and evidence:** The User accepted the complete Change on 2026-08-27 and authorized closure and integration into `development`. The User separately confirmed the Q-03 amendment after examining the argument that a declared prohibition does not prevent a wrong entry from being written: detection of forbidden and unresolved relationships is delivered and tested, while detection of an absent permitted relationship remains unavailable because the active ontology declares permission rather than requiredness. The User agreed to release `0.10.0` with that gap documented and to decide requiredness separately, so the amendment is confirmed rather than reversed.

## Closure

**Owner:** Syspilot Project Manager<br>
**Status:** complete

- [x] The User explicitly released this Contract before artifact work began.
- [x] Every included artifact has terminal status and completion evidence.
- [x] Intent and outcome are `approved`.
- [x] Both Skills are ontology-driven and read-only.
- [x] Quality is explicitly required to execute both methods in every Quality Review.
- [x] Focused and black-box verification passes for current v2 and a synthetic ontology.
- [x] Quality dogfooding is recorded and independently supported.
- [x] Quality has recorded a `proceed` judgment.
- [x] Open Quality Issues contains `None`.
- [x] User validation is `accepted`.
- [x] Current blocker is `none`.
- [x] The observable outcome is demonstrated.
- [x] Integration has been completed by the authorized actor, or its next owner is explicit.

**Final outcome:** MECE and Trace are restored as two focused, ontology-driven, read-only Skills, and every Quality Review must now execute and record both. The Project Manager re-ran the evidence independently rather than restating Quality's report: MECE 5/5, Trace 7/7, Impact 9/9, documentation tests 4/4, and the strict documentation and schema build at zero warnings.

**Known limitation carried forward:** Trace reports unresolved targets, relationships the ontology does not declare, and objects holding no relationship at all, but it cannot report that a permitted relationship is absent. This is a limitation of the active ontology, which declares permission and not requiredness, rather than a judgment that absence is harmless. Making requiredness expressible is recorded as a separate decision and deliberately excluded here because it would change `SYSP_REQ_ONTOLOGY_SCHEMA`, the Ontology skill, the generated ontology reference, and the Setup baseline.

**Integration:** Squash-integrated into `development`; no public push was performed.
