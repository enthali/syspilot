# Change Contract: requirement-cleanup

**Status:** closed<br>
**Process owner:** Project Manager<br>
**Current responsibility:** Project Manager<br>
**Current blocker:** none<br>
**Created:** 2026-11-12<br>
- **Operation Mode**: autonomous, as in the preceding Changes; the User may change it.

- **autonomous** - every actor decides on its own; when genuinely unsure, it asks the user directly and pauses only its own step until answered.

## Handover log

Owned by: Project Manager

The handing-over actor appends one line as the last act before handing over, in the same commit that changes `Current responsibility`, taking `Date` as `YYYY-MM-DD` and `Time` as `HH:MM` in 24-hour local time from the system clock at that moment. The note states what the owner did and the facts that change the next owner's situation; evidence stays in the owner's section and remaining work in the open rows. The handover goes to the next actor that follows from the logical flow of the Change. The log explains transitions; the header stays authoritative.

| Date | Time | From | To | Note |
|--|--|--|--|--|
| 2026-11-12 | 08:10 | Project Manager | Architect | Contract released by the User; clean up all requirements and VCs without changing the realized artifacts. |
| 2026-11-12 | 08:51 | Architect | Quality | Requirements are decomposed with legacy anchors retained; preservation mapping and green verification are ready for independent review. |
| 2026-11-12 | 09:00 | Quality | Architect | Review blocked on remaining mixed-topic VCs and compound method/continuation Requirements; Architect agrees with the findings. |
| 2026-11-12 | 09:24 | Architect | Quality | Method/continuation Requirements and class-wide VC topics are separated; fresh green checks and graph evidence are ready for independent confirmation. |
| 2026-11-12 | 09:28 | Quality | User | Q1/Q2 and the complete correction class are cleared; the preserved, independently assessable specification can proceed to validation. |
| 2026-11-14 | 17:15 | User | Architect | The User paused validation to fix the closure checklist; `closure-integration-check` is integrated into `development` as `827497b` and conflicts with your split of `req_change_contract.rst`. |
| 2026-11-14 | 17:26 | Architect | Quality | Integrated closure obligations and focused VC survive the split; standalone and combined-development preview checks pass, with the remaining textual merge resolution recorded. |
| 2026-11-14 | 17:27 | Quality | User | Reconciliation preserves the integrated closure rules and focused criterion; independent re-check can proceed to validation, with actual integration still outstanding. |
| 2026-11-14 | 17:57 | User | Project Manager | The User accepted the outcome; closure recorded. |

## Intent And Outcome

**Status:** approved<br>
**Approval evidence:** The User directed on 2026-11-12 that all requirements are cleaned up and the realized Markdown artifacts stay as they are, reviewed the text and released it the same day.

### Goal

All requirements and their VCs in `docs/syspilot/requirements/` follow the rule that the Architect and Quality have adopted: a requirement states concise, unambiguous obligations only, and each VC is a short item on one topic that an independent actor such as Quality can judge separately from inspectable evidence.

### Value

Requirements such as `SYSP_REQ_RELEASE_CONTRACT` (one list of about 180 lines with rationale, procedure and checker internals, and a single VC that retells it) and `SYSP_REQ_SETUP` (about 47 KB) cannot be reviewed obligation by obligation, and every process edit has to be made twice. Cleaned requirements make reviews decidable and keep the specification in line with the artifacts it describes.

### Scope

- All 29 requirements and 29 VCs in 22 files of `docs/syspilot/requirements/`, plus the references between them that the cleanup changes.
- The realized artifacts stay unchanged: the Markdown process and guide documents, the example actors and Contracts, the skills, the scripts and tests. The User subsequently authorized the reference-list-only exception below; no test assertion or logic changes.
- No obligation is added, dropped or changed in meaning. What is removed from a requirement is procedure or rationale that already lives in its realizing artifact or in a closed Change Contract.
- Out of scope: User stories and acceptance criteria, the rule itself, the Release Process behavior, and the question of dropping the validation-only workflow run, which is a separate decision.
- Crew: Architect owns the requirements; Quality reviews. Others are consulted only when a requirement cannot be reconciled with its realizing artifact, in which case the discrepancy is escalated to the User.

### Observable Outcome

- Every requirement and VC in `docs/syspilot/requirements/` meets the rule; Quality confirms this per file.
- Quality confirms that every previous obligation is retained and covered, with no contradictory or duplicated normative rule.
- No file outside the requirements and the Contract of this Change is changed, apart from references. The strict documentation build passes and the test suite passes; no new test is required.

## Artifacts, Ownership And Process Gates

**Applicability:** Each artifact owner decides and updates its own row.<br>
**Scope change:** When the approved intent widens after a row reached a terminal status, `Intent and outcome` returns to `draft` until it is approved again, and each owner whose terminal row the wider intent may affect reassesses it: the owner sets the row back to `pending` or records in the row why its evidence still holds.<br>
**Ownership:** The `Owner` column of this table is the only statement of artifact and gate ownership in the Contract; section headings name no artifact owner.<br>
**Status:** pending

Crew by User decision of 2026-11-12: Architect and Quality.

| Artifact or gate | Included | Owner | Completion evidence | Status |
|---|---|---|---|---|
| Intent and outcome | yes | Project Manager | Goal, value, scope, and observable outcome are explicit and approved | approved |
| Contract release | yes | User | User released the Contract on 2026-11-12 | approved |
| Version control | yes | Project Manager | Feature branch `feature/requirement-cleanup`; squash-integrated into `development` at closure | merged |
| Infrastructure impact | not applicable: no workflow, CI or packaging artifact changes | Admin | Affected workflow, CI, and packaging artifacts are updated, confirmed by their current owner rather than inferred from a Needs-only impact query | not applicable |
| Product specification and architecture decisions | yes | Architect | `689b874` preserves `827497b`'s closure obligation, current-actor boundary and focused VC in the split; 71 REQs / 188 VCs. Source and combined-development preview build without warnings; 33 focused tests and 28 Impact starts pass. Prior full-suite evidence remains tied to `9f77643` | complete |
| User-facing documentation | not applicable: realized prose stays unchanged; User-approved map reference updates are included in architecture | Technical Writer | Agreed documentation surface is coherent and user-oriented; factual-owner review is recorded; `doc` Needs and `includes` links are current; documentation builds cleanly | not applicable |
| Example sync | not applicable: no role card, Contract process or example changes | Technical Writer | Changes of this Change that also hold for a general project are carried into the examples | not applicable |
| Implementation and unit verification | not applicable: no implementation or test-logic changes; only the User-approved test reference list changes | Developer | Changed artifacts and durable technical decisions are linked; the Developer wrote and ran the unit tests, and their commands and results are recorded | not applicable |
| Acceptance test design and results | not applicable: Quality reviews the requirements directly | Tester | Requirement tests written and run by the Tester, with their commands and results, and the means for User validation trace to the intended outcome | not applicable |
| Quality review | yes | Quality | Proceed at `b34bbd7`: prior full review retained; reconciled Change file independently rechecked against `827497b` and tested combined preview; no open issue | complete |
| User validation and approval | yes | User | The User accepted the outcome on 2026-11-14 | accepted |
| Closure decision | yes | Project Manager | Final outcome, validation disposition, and integration state are recorded | complete |

## Architecture And Specification

**Status:** complete

### Affected Artifacts

| Artifact | Change | Rationale |
|---|---|---|
| `docs/syspilot/requirements/req_actor_model.rst` | Existing REQ; VCs 1-3 | Preserve role shape, root-relative code-span paths, project neutrality, positive instructions, process authority and Kernel boundary; remove only path-depth explanation |
| `docs/syspilot/requirements/req_project_manager.rst` | Existing REQ; VCs 1-2 | Preserve strategy, initialization, first Architect handoff, direct Quality/User provenance, closure and agentless boundary |
| `docs/syspilot/requirements/req_architect.rst` | Existing REQ; VCs 1-2 | Preserve architecture applicability, coherent decisions/specifications/realization, checks and surfaced ambiguity |
| `docs/syspilot/requirements/req_developer.rst` | Existing REQ; VCs 1-2 | Preserve implementation evidence, Developer-produced unit verification and owner decisions for conflicts/alternatives |
| `docs/syspilot/requirements/req_tester.rst` | Existing REQ; VCs 1-3 | Preserve black-box normal/boundary/adverse scenarios, Tester-produced requirement tests, reproducibility, User-validation means and separately assessed questions to the specification owner |
| `docs/syspilot/requirements/req_research.rst` | Existing REQ; VCs 1-2 | Preserve question/sources, facts/uncertainty, relevant negative results and receiving decision owner |
| `docs/syspilot/requirements/req_release.rst` | Existing REQ; VCs 1-3 | Preserve packaging, preflight/notes, terminal Technical Writer row, workflow consultation and unresolved-input boundary; remove one identical packaging bullet |
| `docs/syspilot/requirements/req_admin.rst` | Existing REQ; VCs 1-4 | Preserve direct infrastructure evidence, workflow/preflight comparison, stale-evidence inputs, separately assessed Release consultation/gate ownership and record-based Setup ACK |
| `docs/syspilot/requirements/req_quality.rst` | Existing REQ; VCs 1-3 | Preserve independent current judgment, actionable owner issues, both methods and recorded-evidence-first execution |
| `docs/syspilot/requirements/req_technical_writer.rst` | Existing REQ; VCs 1-4 | Preserve independently assessed doc map/incoming impact and plain Markdown, factual consultation without authority transfer, Example sync and exact deviations |
| `docs/syspilot/requirements/req_impact_analysis.rst` | Existing REQ; VCs 1-4 | Preserve ontology-driven traversal, direction/depth/de-duplication, output shapes/defaults, explicit failure and Contract authority |
| `docs/syspilot/requirements/req_ontology_management.rst` | Both existing REQs; schema VCs 1-2 and editing VCs 1-4 | Preserve actual-schema guidance, optional metadata, Contract governance, unrelated content and Setup preservation; strict validation and post-Setup scope authorization have separate VC outcomes |
| `docs/syspilot/requirements/req_quality_methods.rst` | Both existing REQs; MECE VCs 1-4 and Trace VCs 1-5 | Preserve exact deterministic peers, semantic findings/limits, depth-bounded named relationships, shared traversal, unresolved targets and separately assessed read-only authority and linked-content consistency |
| `docs/syspilot/requirements/req_contract_documents.rst` | Existing declaration anchor plus 12 topic REQs; VCs 1-15 | Separate state/evidence, log, responsibility, ownership, gates, widening, tailoring, inheritance, composition, modes, presentation and receiver refresh; retain five-rule inventory and all clock/note safeguards normatively |
| `docs/syspilot/requirements/req_contract_handling.rst` | Existing REQ; VCs 1-6 | Preserve commit-before-notify, bounded HANDOFF, refresh/header-check before work/ACK, read-only consultation, Kernel transport, separately assessed notification-gap policy and escalation |
| `docs/syspilot/requirements/req_examples.rst` | Existing REQ; VCs 1-6 | Preserve exact flat inventories, dependency links, generic paths/values, source/seed boundary, deviations and separately assessed doc-map links, markup exclusion and zero-warning build |
| `docs/syspilot/requirements/req_process_maintenance.rst` | Existing REQ; VCs 1-5 | Preserve optional adopter scope, Admin consultations without transfer, Version control evidence, same-kind review/four manual limits, direct presentation and Syspilot Change boundary |
| `docs/syspilot/requirements/req_release_version.rst` | Existing REQ; VCs 1-5 | Preserve sole newest-heading source, write-free shared checker/diagnostics, positive/negative cases and baseline/schema exclusions; shared callers, text extraction and workflow authority have separate outcomes |
| `docs/syspilot/requirements/req_change_contract.rst` | Existing anchor plus `CHANGE_MODE`, `CHANGE_START`, `CHANGE_ARTIFACTS`, `CHANGE_VERSION_CONTROL`, `CHANGE_DOCUMENTATION`, `CHANGE_VERIFICATION`, `CHANGE_CLOSURE`; 20 VCs | Original clauses map respectively to initialization/inherited rules, modes/unattended flags, sole User gate/presentation, owner tailoring/infrastructure/Ontology Binding, branch authority, doc/Example sync, test/Quality evidence and direct validation/closure; integrated `827497b` contributes its preserved explicit integration VC |
| `docs/syspilot/requirements/req_release_contract.rst` | Existing anchor plus nine extracted REQs; 26 VCs | Preserve initialization/ownership/modes/gate, inventory/archive, preflight/limits, triggers, P/R/checker rules, full-diff review/isolation, authorization, publication/failure and closure; editor presentation, sufficiency, branch-run authorization, next baseline and ordered publication have separate outcomes |
| `docs/syspilot/requirements/req_setup.rst` | Seven legacy anchors plus 14 extracted REQs; 58 VCs | Original main clauses map to the first six topics; continuation adds eight topics for transfer, autodelivery, delivery route, queue, request, language, receipt and failure. Additional outcomes separate Git state/approval/artifact disposition, Jarvis failures, Actor observations/settings, documentation gates/binding, naming safeguards and final integration/summary |
| `docs/syspilot/requirements/index.rst` | Reviewed; unchanged | Existing toctree still includes every requirement file; topic extraction adds no file |
| `docs/syspilot/documentation/index.rst` | `includes` additions only | Unchanged guides/example folders remain discoverable for the topics extracted from their former parent requirements |
| `tests/test_acceptance_setup_examples.py` | `DocNeedTests.CASES` reference additions only | Match the new Example Contracts `includes` links without changing exact-set assertions or test logic |

### Decisions And Evidence

| Decision or check | Evidence |
|---|---|
| Split compound requirements into topic Requirements and independent VCs, preserving existing IDs as anchors and adding necessary documentation-map references | User's direct response on 2026-11-12: "Aufteilen; Referenzen ergänzen". No obligation or product behavior changes; reference-only map changes are included |
| Preserve normative authority in Requirements rather than moving obligations solely to realizing artifacts or archived Changes | Quality's CONSULTRESPOND: stable IDs do not justify unrelated bundles; each VC needs a separate satisfied/not-satisfied outcome. Advice is not review approval |
| Reference-only test exception | Asked whether only `DocNeedTests.CASES`'s old exact Example Contracts reference list may be updated to match the new topic links, without changing assertions, test logic or product behavior; the User replied "ja darfst du". Only that list in `tests/test_acceptance_setup_examples.py` is included |
| Preservation baseline and identifier check | Compared with `f2c15be`: all 29 original REQ and 29 original VC IDs remain; 42 topic REQs and 159 VCs are added (71 REQs / 188 VCs total), including the focused integration VC preserved from `827497b`. All 258 IDs reviewed at `b8c3882` remain; every REQ has a VC and no ID is duplicated |
| Obligation-to-VC mapping | VC IDs retain their established stems even when retargeted to extracted topic REQs. The explicit correction mapping below records those relations; no legacy criterion is removed |
| Procedure/rationale disposition | Path-depth and Jarvis mechanism explanation remains in the unchanged Setup Contract and closed `docs/changes/v0.10.0/setup-feedback-2.md`; initialization, tailoring, shared-tree and publication sequencing remain in the unchanged Change/Release processes; local-evidence, record-check and non-atomic publication rationale remains in `docs/changes/v0.10.0/release-contract-preflight.md`. Normative boundaries remain in the topic Requirements |
| Impact disposition | Before rewriting, successful depth-1 both-direction queries covered all original REQs. Stories/ACs remain unchanged; role cards, processes, guides, examples, skills, scripts and ontology retain content. Only the documentation map and explicitly authorized test pin receive references |
| Validation isolation | Checked committed candidates in a detached worktree outside the shared repository. The shared workspace contains ignored source copies under `docs/_build/needs-graph-preview-20261112-0822/` that source-inventory tests scan; those files and the pre-existing uncommitted Contract-handling instruction edit were left untouched. Both completed validation worktrees were removed after retaining evidence |
| Existing QA suite | At `4b07515`, `python -m unittest discover -s tests -v`: 202 tests passed in 385.699 seconds; `python docs\test_docs_build.py -v`: 4 tests passed. No test logic/assertion changes; only the approved reference-list additions |
| Strict clean documentation/schema build | At `f40edae`, `python docs\docs-build.py clean`: exit 0, build succeeded, zero warnings. The only delta from QA-tested `4b07515` is one underline character in each of two RST titles; the strict build validates those formatting-only corrections |
| Fresh traceability evidence | Successful depth-1 both-direction flat Impact queries against the new build for all 51 REQs; no failed/empty query was treated as scope proof. Export has 249 Needs. Retained per-ID data also resolves the extracted Release Record topic to its parent, story, VCs and incoming documentation links |
| Inspectable logs and graph | Under `C:\Users\DOE4SI\.copilot\session-state\334ed166-2820-4c7b-bf2b-648112d9fa4c\files\`: `requirement-cleanup-build.log`, `requirement-cleanup-tests.log`, and `requirement-cleanup-needs\` (`needs.json` and `needs_id\`). Impact/MECE/Trace can select the retained per-ID data through `--needs-dir` |
| Change boundary and review limit | `git diff --check` passes. Committed changes are the 21 requirement-bearing files, this Contract, documentation-map references and the approved test reference list; the requirement index, stories/ACs and realized product content are unchanged. Architect's baseline comparison/mapping is complete; independent Quality judgment and User validation remain open |

### Q1/Q2 Correction Mapping

| Prior bundle | Normative topic after correction | Independently assessable VC outcomes |
|---|---|---|
| `SYSP_VC_RELEASE_CONTRACT_2` | Existing Release process REQ | VC 2 checks complete allowed modes and reachable-User evidence; new VC 4 checks same-step editor presentation |
| `SYSP_VC_RELEASE_REVALIDATION_3` | Existing revalidation REQ | VC 3 assesses sufficiency at release start; VC 4 checks run-specific User authorization before branch push; VC 5 checks each successful tag-run baseline |
| `SYSP_VC_SETUP_INSTALLATION_3` | Existing installation REQ | VC 3 checks occupied-directory preservation; VC 4 checks ignore-rule blocking; VC 5 checks versioned baseline identity/readback |
| `SYSP_VC_ONTOLOGY_EDITING_3` | Existing ontology editing REQ | VC 3 checks zero-warning validation before completion; VC 4 checks explicit scope for immediate post-Setup ontology establishment |
| `SYSP_REQ_CONTRACT_DOCUMENTS` | Anchor: process declaration | Legacy VC 1 |
| Method current state/evidence | `SYSP_REQ_CONTRACT_STATE` | Legacy VC 2: replace-in-place/log exception; VC 9: inspectable outcome evidence |
| Method log | `SYSP_REQ_CONTRACT_LOG` | VC 10: fields, clock and commit timing; VC 11: note content and bounded authority |
| Method responsibility | `SYSP_REQ_CONTRACT_RESPONSIBILITY` | VC 12: consistent transfer to an included progressing owner without ownership transfer |
| Method ownership/gates | `SYSP_REQ_CONTRACT_OWNERSHIP`; `SYSP_REQ_CONTRACT_GATES` | Legacy VC 3: single owner statement; VC 13: sole gate-setting authority |
| Method scope/tailoring/composition/modes | `SYSP_REQ_CONTRACT_SCOPE`, `_TAILORING`, `_COMPOSITION`, `_MODES` | Legacy VCs 4, 5, 7 and 8 respectively |
| Method five-rule inheritance | `SYSP_REQ_CONTRACT_INHERITANCE` | Legacy VC 6: registry-wide inventory and structural adaptation |
| Method presentation/refresh | `SYSP_REQ_CONTRACT_PRESENTATION`; `SYSP_REQ_CONTRACT_REFRESH` | VCs 14 and 15 respectively |
| `SYSP_REQ_SETUP_CONTINUATION` | Anchor: observed tool routing | Legacy VC 1; still records all four tools and blocks writes on missing creation after the before scan |
| Continuation authority | `SYSP_REQ_SETUP_ADMIN_TRANSFER` | Legacy VC 2: authority commit ordering; VC 6: existing-Admin disposition; VC 7: subsequent single executor |
| Continuation autodelivery | `SYSP_REQ_SETUP_AUTODELIVERY` | Legacy VC 3: one update, preserved names, malformed-array blocker and stated race limit |
| Continuation delivery/queue | `SYSP_REQ_SETUP_ADMIN_DELIVERY`; `SYSP_REQ_SETUP_ADMIN_QUEUE` | VCs 8/9: new-Admin initialMessage versus consent/manual route; VC 10: existing-queue fields, integrity and race limit |
| Continuation request/language | `SYSP_REQ_SETUP_CONTINUATION_REQUEST`; `SYSP_REQ_SETUP_CONTINUATION_LANGUAGE` | Legacy VC 4: exact content; VC 11: language and unchanged identifiers |
| Continuation receipt/failure | `SYSP_REQ_SETUP_CONTINUATION_RECEIPT`; `SYSP_REQ_SETUP_CONTINUATION_FAILURE` | Legacy VC 5: committed ACK within 120 seconds; VC 12: diagnostic-only queue states; VC 13: blocker/manual path without header change or false receipt |

Rechecked the four changed specification files against `52eb9c1` and the
original `f2c15be` obligations. The topic split relocates existing normative
constraints; it changes no Setup or method procedure. In particular,
autodelivery precedes the authority commit, delivery follows it, queue append
requires transfer-step consent, only the receiver's committed ACK proves
continuation, and no new guarantee of concurrent-write safety is claimed.
The map adds references only where unchanged guides/examples carry the topic;
the test AST is unchanged outside the authorized `DocNeedTests.CASES` list.
Q1/Q2 remain open for Quality's confirmation; this is Architect's correction
evidence, not a Quality disposition.

### Class-Wide VC Assessment

Read every VC in all 21 requirement-bearing files, not only Q1's examples.
Split independently governed topics when one could pass while a separate
obligation remained unassessed. Keep positive/negative cases and jointly
necessary observations of one operation together: for example, checker
diagnostics, queue-append integrity and the sending/receiving commit boundary
each remain one bounded outcome.

The additional splits retain the existing Requirements and legacy VC IDs;
they add no documentation-map or test references:

| Existing VC topic | Separate outcomes after correction |
|---|---|
| Admin VC 2; Tester VC 2 | Remote workflow evidence versus Release consultation/gate authority (new Admin 4); reproducible validation versus questions to the specification owner (new Tester 3) |
| Technical Writer VC 1; Examples VC 4 | Documentation-map traceability versus markup exclusion (new Technical Writer 4); example traceability, markup exclusion and strict build (new Examples 5-6) |
| MECE VC 3; Trace VCs 3-4 | MECE report scope versus read-only authority (new 4); Trace observed-neighborhood/requiredness limits, read-only authority and linked-content assessment (new 5) |
| Contract Handling VC 4 | Blocker/escalation without transfer versus the accepted notification-gap policy (new 6) |
| Change Contract VC 1; Start VC 1 | Initialization versus inherited-rule reuse (new Contract 2); sole User authorization versus same-step editor presentation (new Start 2) |
| Change Artifacts VC 1; Verification VC 1 | Owner-decided artifact evidence versus point-of-use optional tailoring (new Artifacts 4); producer evidence versus Quality's evidence-first rerun policy (new Verification 4) |
| Release Version VC 3 | Shared checker callers, release-text extraction and workflow ownership/consultation (new 4-5) |
| Release Contract VC 1; Publication VC 1 | Initialization/closure assignment versus User authorization (new Contract 5); direct Quality proceed versus main-before-tag publication (new Publication 4) |
| Setup Source VC 2; Jarvis VCs 1-2 | Initial Git state, branch approval and existing-artifact disposition (new Source 3-4); host identity, installation consent and command-failure evidence (new Jarvis 5) |
| Setup Actors VCs 2-3, 5 | Context resolution, observed persistence paths, before scan, subsequent discovery, message boundary and session-setting behavior (new 6-8) |
| Setup Gates VC 2; Docs VC 2 | Gate-set/status model versus recorded zero-warning gate evidence (new Gates 4); registry navigation/build versus literal ontology binding (new Docs 4) |
| Setup Naming VCs 1-3; Handoff VC 1 | Confirmation timing, path consistency, post-write changes, seed integrity, collision disposition, existing/source-name preservation and invalid-name rejection (new Naming 4-7); final integration versus handoff content (new Handoff 3) |

### Correction Verification

The pre-reconciliation specification candidate is `9f776435a786b474476bcaba2c79963529620984`.
Its handoff added only this Contract's evidence and responsibility/log update.

| Check | Observed result |
|---|---|
| Strict documentation/schema build | `python docs\docs-build.py clean`: exit 0, build succeeded, schema validation zero warnings |
| Existing QA suite | `python -m unittest discover -s tests -v`: 202 tests in 241.489 seconds, `OK` |
| Build-runner tests | `python docs\test_docs_build.py -v`: 4 tests in 0.019 seconds, `OK`; the printed failure is the expected negative-case fixture, not a failed test |
| Preservation and reference boundary | All 58 original REQ/VC IDs and all 188 first-reviewed IDs retained; 71 REQs / 187 VCs, no duplicate ID, every REQ has a VC. Baseline test AST is identical outside the authorized `DocNeedTests.CASES` list; realized artifacts, stories/ACs, scripts and other tests remain unchanged |
| Fresh graph | 319 exported Needs; all 258 REQ/VC starts passed both-direction depth-1 flat Impact queries with `--no-build` against retained per-ID data; all 13 unique code-span Requirement references resolve |
| Isolation and cleanup | Built and tested the committed candidate in the external detached worktree, verified it clean, retained logs/export, then removed that worktree; shared generated source copies and the unrelated dirty instruction remain untouched |

Final evidence under
`C:\Users\DOE4SI\.copilot\session-state\334ed166-2820-4c7b-bf2b-648112d9fa4c\files\`:
`requirement-cleanup-final-build.log`, `requirement-cleanup-final-tests.log`,
`requirement-cleanup-final-impact.json`, and `requirement-cleanup-final-needs\`
(`needs.json` and `needs_id\`). Select this export through `--needs-dir`;
the earlier exports remain intact for their recorded review baselines.
Graph resolution and green tests establish structural/build integrity, not
Quality's independent granularity or semantic-preservation judgment.

### Integrated Closure Reconciliation

Project Manager returned responsibility at `e524e91` to preserve the already
integrated `closure-integration-check` (`827497b`) in the topic split. This is
preservation of the approved integration baseline, not a new process decision.

| Integrated constraint | Location in the split | Preservation |
|---|---|---|
| Explicit squash integration before closure; reasoned Version control exclusion; generic target placeholder | `SYSP_REQ_CHANGE_CLOSURE` | Integrated normative paragraph retained verbatim |
| Branch creation/integration stays with the single current actor | `SYSP_REQ_CHANGE_VERSION_CONTROL` | Integrated normative sentence retained verbatim |
| Focused integration outcome | `SYSP_VC_CHANGE_INTEGRATION_1` | ID, title and body retained; `verifies` targets the extracted closure Requirement rather than its former compound parent |
| Canonical/example checklist and closing guide sentence | Already integrated product artifacts from `827497b` | No edits here; existing incoming documentation links already cover the extracted topics |

Depth-1 both-direction Impact discovery from closure and version control
resolved their story, parent, VCs and incoming documentation Needs using the
retained `requirement-cleanup-final-needs` export. The affected realization is
the canonical Change Process plus its generic example and closing guide
sentence. Branching/Upgrade/Methodology need no further change: the integrated
rule preserves their existing authority boundaries.

Only the Requirement file and this Contract change in this reconciliation.
The previous Quality judgment applies to its named baseline; Quality must
re-check this file after reconciliation.

| Verification | Observed result and limit |
|---|---|
| Exact specification delta at `689b874c0192d0bca362e720a44583a72e9bbd7f` | Removing the two verbatim integrated normative additions and the focused VC reproduces `e524e91`'s Requirement file exactly. The integrated VC differs only in its `verifies` target. All 258 previously reviewed IDs remain, plus `SYSP_VC_CHANGE_INTEGRATION_1`; unique IDs and complete REQ-to-VC coverage hold |
| Standalone candidate build | Isolated `python docs\docs-build.py clean`: exit 0, build succeeded, zero schema/build warnings |
| Combined-development preview | In a detached worktree only, previewed source `689b874` with `development` at `851621f260a03260985ec35689ddf8ca1e0a979d` (which includes `827497b`). Only the Requirement file conflicted; selecting its exact reconciled source resolved it. Preview tree `4d98ffba6b9328126a70a2b44db113567ead2d33` changes no other specification; both templates and the guide equal `development` byte-for-byte in Git |
| Combined build and existing regressions | Preview `python docs\docs-build.py clean`: exit 0 and zero warnings. One `python -m unittest -v test_acceptance_adoption_feedback.ChangeTemplateTests test_acceptance_setup_examples` run from `tests\` passed 33 tests in 0.025 seconds. No test assertion or logic changes and no full-suite rerun for this bounded prose/link reconciliation |
| Focused outcome and fresh graph | Exact canonical and generic integration checklist items each occur once, including the reasoned exclusion. Fresh export contains 320 Needs / 259 REQ-and-VC IDs; all 28 IDs in the changed Requirement file passed both-direction depth-1 Impact queries. The integration VC verifies closure; incoming guide/example documentation links remain intact |
| Shared-state boundary and cleanup | No merge was committed or applied to the shared branch; Project Manager integration is still outstanding. Its textual Requirement conflict remains and has the tested resolution above. The isolated preview merge was aborted and its clean worktree removed after preserving evidence. The unrelated dirty instruction remains untouched |

Evidence under
`C:\Users\DOE4SI\.copilot\session-state\334ed166-2820-4c7b-bf2b-648112d9fa4c\files\`:
`requirement-cleanup-reconciliation-source-build.log`,
`requirement-cleanup-reconciliation-preview-build.log`,
`requirement-cleanup-reconciliation-tests.log`,
`requirement-cleanup-reconciliation-impact.json`, and
`requirement-cleanup-reconciliation-needs\` (combined-preview export).
The prior review exports and logs remain intact. This evidence establishes
preservation and build integrity, not Quality's independent re-check judgment.

## Quality Review

**Status:** complete

**Current judgment:** proceed at `b34bbd7494750a841fc5fee0328a5ee059caeaee`.

The 2026-11-14 re-check covers the complete reconciliation delta and all 28
Needs in `req_change_contract.rst`. The integration paragraph and current-actor
sentence match integrated `827497b` verbatim; removing those additions and the
focused VC restores the previously reviewed file exactly. The focused VC's
only difference from its integrated form is its correct retargeting to
`SYSP_REQ_CHANGE_CLOSURE`. It remains independently assessable: an applicable
unintegrated branch fails, squash integration passes, and exclusion requires
the recorded Version control reason. No new behavior or obligation is invented.

The current inventory is 71 REQs / 188 VCs. The prior full-file, preservation
and class-wide judgments below remain valid for unchanged content. Recorded
source/combined strict builds and 33 focused tests are sufficient for this
prose/link delta; Quality did not rerun the full suite. Its previous 202-test
result remains evidence for `9f77643`, not a claim of a fresh full-suite run.
Independent Git comparison confirms that preview tree
`4d98ffba6b9328126a70a2b44db113567ead2d33` has the exact reconciled Requirement
and retains development's canonical/example checklists and corrected guide
unchanged. Their content was read directly and agrees with the specification.

This proceeds to User validation, not closure or integration. The shared
branch has not been merged with development. Project Manager must preserve
the tested Requirement resolution at integration; later changes beyond the
reviewed delta require reassessment.

The complete `b0ec731..b8c3882` correction diff and every named Q1/Q2 element
were reviewed against the earlier full baseline assessment. All 58 original
IDs and all 188 first-reviewed IDs remain; the pre-reconciliation specification has
71 REQs / 187 VCs with unique IDs. No added, dropped or changed normative
obligation, contradictory rule or unintended normative duplication was
identified. General rules and their process-specific specializations retain
distinct authority rather than competing declarations.

Reviewed all 21 requirement-bearing files and the unchanged requirement index.
The dispositions below concern this cleanup, not new runtime certification of
the unchanged product. `Retained` means the old/new obligation comparison found
the previous safeguards preserved and covered by the current topic VCs.

Q1 is cleared: modes/reachability, editor presentation, revalidation sufficiency,
branch-run authorization, later baseline, destination preservation, ignore
blocking, baseline readback, strict validation and post-Setup scope now have
their own relevant outcomes. The class-wide splits also separate reporting
from authority, navigation from binding, observations from discovery, and
verification from publication ordering. Positive/negative cases of one bounded
operation remain together; the criterion is a decidable topic, not word count.

Q2 is cleared: the method has 13 topic REQs and continuation has its routing
anchor plus eight topic REQs. Normative clock, ownership, gate, scope, queue-race,
consent, sequencing, prompt-language, acknowledgement and recovery safeguards
remain in Requirements with corresponding VCs. References preserve their
ordering without reproducing the entire procedure in one Requirement.

| Requirement file | Preservation | KISS / independent coverage disposition |
|---|---|---|
| `req_actor_model.rst` | Retained | Focused role-model obligations and three bounded VC topics |
| `req_project_manager.rst` | Retained | Role authority and direct decision provenance distinguished |
| `req_architect.rst` | Retained | Assignment and coherent realization evidence distinguished |
| `req_developer.rst` | Retained | Realization evidence and owner decisions distinguished |
| `req_tester.rst` | Retained | Black-box scenarios and reproducible validation support distinguished |
| `req_research.rst` | Retained | Evidence and receiving decision authority distinguished |
| `req_release.rst` | Retained; duplicate packaging clause removed | Package, documentation and workflow-gate boundaries distinguished |
| `req_admin.rst` | Retained | Infrastructure evidence, workflow boundary and Setup ACK distinguished |
| `req_quality.rst` | Retained | Judgment, methods and evidence-first execution distinguished |
| `req_technical_writer.rst` | Retained | Documentation map, factual authority and examples distinguished |
| `req_impact_analysis.rst` | Retained | Traversal, output, failure and authority topics distinguished |
| `req_ontology_management.rst` | Retained | Strict validation and post-Setup scope authorization have separate outcomes |
| `req_quality_methods.rst` | Retained | Peer discovery, semantic limits, traversal and authority topics distinguished |
| `req_contract_documents.rst` | Retained | Thirteen concise method topics and fifteen VCs preserve the complete shared-rule contract |
| `req_contract_handling.rst` | Retained | Committed handoff, ACK, consultation, escalation and communication distinguished |
| `req_examples.rst` | Retained | Installable inventory, portability, deviations and documentation distinguished |
| `req_process_maintenance.rst` | Retained | Adopter boundary, consultation, semantic limits, integration and presentation distinguished |
| `req_release_version.rst` | Retained | Version agreement, source derivation and shared callers distinguished |
| `req_change_contract.rst` | Retained | Extracted topics preserve gate, mode, artifact, integration and validation boundaries |
| `req_release_contract.rst` | Retained | Reachability, presentation, sufficiency, authorization, baseline and publication order are separately assessed |
| `req_setup.rst` | Retained | Continuation topic decomposition and separate installation, Actor, gate, naming and handoff outcomes clear the correction class |
| `index.rst` | Unchanged | Existing toctree still includes every requirement file |

Reference-only changes in `docs/syspilot/documentation/index.rst` preserve old
links and add extracted topics. The test diff adds only the authorized
`DocNeedTests.CASES` references; no assertion, executable logic, realization,
story or AC changes were included. The unrelated dirty Contract-handling
instruction was neither reviewed as this Change's output nor modified.

### Applied Review Methods

| Method | Selected scope | Evidence | Findings | Limits |
|---|---|---|---|---|
| Reconciliation preservation, MECE and Trace | All 28 REQ/VC IDs in the changed file; complete same-document same-type peers (7 REQ or 19 VC peers per start); both-direction depth-1 relationships | 56 successful fresh MECE/Trace queries against the combined-preview export; exact union 35 Needs and 61 resolved named edges; whole file, all seven external neighbors and combined realization content read; exact-delta comparison and recorded preview checks reviewed | No structural or semantic finding; integrated obligations and focused VC retained without conflicting authority or duplicated decision rule | No deeper/all-type completeness claim; scripts lack structured semantic coverage. Prior review covers unchanged content; combined preview is evidence, not completed integration |
| Baseline preservation and coverage reading | Full baseline review plus complete `b0ec731..b8c3882` correction diff; all 21 requirement-bearing files, unchanged index and authorized references | Per-file dispositions; unique-ID/preservation comparison; source-level obligation/VC reading; independent AST comparison against `f2c15be` | Q1/Q2 cleared; every previous obligation remains normatively represented and covered; no competing or contradictory rule identified | This wording review certifies neither new runtime behavior nor unreviewed future changes |
| MECE horizontal coverage | All 258 current REQ/VC starts; `same-document`, complete same-type sets excluding self | 258 successful queries; exact `peers`/`examined` sets in the final analysis below; complete current peer content assessed through baseline and correction reading | No structural or remaining semantic partition/coverage finding; general rules and their specializations have consistent boundaries | 15 single-REQ documents have no comparable REQ peer; all reports lack structured coverage data. Recorded content judgment, not an empty findings array, clears semantic review. No all-type claim |
| Trace relationship analysis | All 258 starts, both directions, depth 1; exact union 289 Needs: 258 starts, the same 19 stories and 12 documentation Needs | 258 Trace and 258 Impact queries; 542 distinct resolved named edges; exact neighborhoods/edges below; changed topic content and retargeted VCs read against unchanged neighbors | No unresolved target or inconsistent story, specialization, verification or documentation relationship identified; code-span sequencing references checked against their topic content | Depth 1 does not certify deeper chains; link resolution proves neither requiredness nor completeness. Semantic judgment comes from the recorded reading; unchanged neighbor content retains the prior assessment |
| Owner verification evidence review | Final source candidate `9f77643`; handoff `b8c3882` changes only Contract evidence/state | Final QA log: 202 tests in 241.489 seconds, `OK`; four build-runner tests recorded green; final build log: schema validation zero warnings and successful build; `git diff --check` passes | Fresh isolated evidence supports source/build integrity; independent content review establishes topic separation | No suite rerun by Quality: recorded checks cover the exact final source candidate. Shared ignored source copies and unrelated dirty instruction remain untouched |

Quality's fresh 774 discovery/analysis queries used the Architect's retained
`requirement-cleanup-final-needs\needs_id` export, not the shared default build.
Exact analysis evidence is retained in
`C:\Users\DOE4SI\.copilot\session-state\31d89b9f-bcdb-4323-9a89-60ceae73d649\files\cleanup-final-review-analysis.json`;
`cleanup-final-review-union.json` there enumerates the exact 289-Need union.
Reconciliation peer sets, neighborhoods and edges are retained in
`cleanup-reconciliation-quality-analysis.json` in that same directory. Its
seven external neighbors are `SYSP_REQ_CONTRACT_HANDLING`,
`SYSP_US_CHANGE_CONTRACT`, and documentation Needs for Branching, Change
Contract, Example Contracts, Methodology and Upgrade. All were assessed;
no unresolved target or new boundary conflict was found.
Final owner build/test logs and isolation limits are linked in Correction
Verification above. Independent comparison confirms that the documentation
map changes only `includes` lines and the test AST is unchanged outside the
authorized `DocNeedTests.CASES` list. No realization change was included.

Quality communicates its `proceed` judgment and supporting evidence directly to the Project Manager before the Project Manager presents the verified outcome for validation. Another actor's forwarded claim does not establish Quality's decision.

### Open Quality Issues

Keep this table synchronized with currently open issues. For each issue, Quality transfers current responsibility to the owner of the affected artifact. When Quality confirms the required outcome, update the affected artifact or evidence and remove the resolved row. At closure this table contains `None`.

| Artifact | Current issue | Required outcome |
|---|---|---|
| None | | |

## User Validation And Approval

**Recorded by:** Project Manager<br>
**Status:** accepted

Quality's `proceed` judgment verifies that the change is ready for validation; it does not validate user value. The Project Manager presents the observable outcome after receiving Quality's direct judgment and evidence; the User communicates the decision directly to the Project Manager, who records it.

**Decision and evidence:** The User accepted the outcome directly to the Project Manager on 2026-11-14 after reviewing the rebuilt HTML documentation and Quality's `proceed` at 9027279. The presentation named the scope: 21 requirement files with 71 requirements and 187 verification criteria, one test-list reference update, no change to the realized artifacts, and the reconciliation with `closure-integration-check`.

## Closure

**Status:** closed

- [x] Every included artifact or gate has terminal status and completion evidence.
- [x] Intent and outcome are `approved`.
- [x] Quality has recorded a `proceed` judgment.
- [x] Open Quality Issues contains `None`.
- [x] User validation is `accepted`.
- [x] Current blocker is `none`.
- [x] The observable outcome is demonstrated.
- [x] The feature branch is squash-integrated into `development`.

**Final outcome:** The requirements and VCs in `docs/syspilot/requirements/` follow the Architect and Quality rule: compound requirements are split into topic requirements that keep the old IDs as anchors, and each VC covers one topic. The realized Markdown artifacts, skills and scripts are unchanged. The User accepted on 2026-11-14. Integrated by squash into `development` from `feature/requirement-cleanup` as `95f29b7`, not pushed. The textual conflict in `req_change_contract.rst` with `closure-integration-check` was resolved to the branch version that Quality reviewed, which carries the integration closure obligation.
