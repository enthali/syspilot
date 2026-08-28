# Change Contract: Version Control Ownership

**Status:** closed<br>
**Process owner:** Syspilot Project Manager<br>
**Current responsibility:** none, the Contract is closed<br>
**Current blocker:** none<br>
**Created:** 2026-08-28<br>
**Branch:** feature/version-control-ownership<br>
**Collaboration mode:** autonomous — every actor decides on its own within the released scope; when genuinely unsure it asks the User directly and pauses only its own step until answered.

## Intent And Outcome

**Owner:** Syspilot Project Manager<br>
**Status:** approved<br>
**Approval evidence:** The User's release is recorded in the `Contract release` gate row rather than here, so that a settled intent text and an authorization to start remain two separate statements with two different owners.

### Goal

Make version control a named, owned artifact of every Change Contract, so that the authority to create the Change's branch and to integrate it into `development` is stated where every other artifact ownership is stated, instead of being delegated to a branching policy that does not exist.

### Value

Closure already requires that "integration or publication has been completed by the authorized actor", but no artifact, process, or Requirement says who that actor is. The rule therefore cannot be checked. Naming version control as an owned artifact makes the authority visible in the same table a reader already consults for every other artifact, and it lets the existing closure condition — every included artifact carries a terminal status — enforce integration without adding a new rule.

The branch name also stops being stated twice. Today it appears in the preamble and is referenced as the single authoritative place; moving it into the artifact row leaves exactly one location, which is the property that keeps two statements from drifting apart.

### Scope

- Add one artifact row for version control to the canonical Change Contract template, owned by the Syspilot Project Manager. One row, not two: the feature branch is the object with a lifecycle, while `development` is the state it ends in.
- Define the row's completion evidence as the branch name plus its integration state, and define its status values as `active` while the branch carries the work and `merged` once it has been squash-integrated into `development`. `merged` is a terminal status, so the existing closure condition covers integration.
- Extend the status vocabulary only when a real case requires it, and extend it in the canonical template rather than in a single Contract instance, so the vocabulary cannot drift per document.
- State the Project Manager's two version-control duties explicitly: creating the Change's feature branch at Contract initialization, and squash-integrating that branch into `development` at closure.
- Record why these two duties sit with one actor: all actors share a single working tree, so a branch switch changes state underneath every other actor. It must be single-writer, and the Project Manager is the only actor holding responsibility at exactly the two moments a switch occurs.
- Exclude promotion from `development` to `main`. That is release publication and belongs to the Syspilot Release actor within a Release Contract. This Change must not grant the Project Manager release authority as a side effect.
- Remove the `Branch:` preamble field from the canonical template so the artifact row is the single place the branch name is recorded, and update every statement that currently designates the preamble field as authoritative.
- Resolve the contradiction between mandatory Change branching and `Branch: NOT APPLICABLE` by using the artifact table's existing `Included` column instead of a special value, so no exception rule is needed.
- Replace the Change Contract Initialization step that delegates to "the project's branching policy" with the concrete rule this Change defines.
- Update the affected specification, process, and user-facing surfaces so the Requirement, the process, the template, and the reader-facing branching guide state one consistent rule.
- Keep `docs/branching.md` a derived reader view rather than a second authority.
- Do not rewrite closed Change Contracts in `docs/changes/`. They are an archive of what was agreed at the time, and retrofitting them would destroy that record.
- Do not add an actor, a workflow, or an approval step.
- Do not push the public Syspilot repository without explicit User authorization.

### Observable Outcome

The canonical template carries a version-control artifact row owned by the Project Manager, with `active` and `merged` as its status values and the branch name as part of its evidence. The `Branch:` preamble field is gone and no surface still designates it as authoritative. The specification states who creates the Change branch and who integrates it into `development`, and states that promotion to `main` is not part of that authority. `Branch: NOT APPLICABLE` no longer exists as a special value. The strict documentation and schema build passes with zero warnings, and this Contract itself demonstrates the new row by reaching `merged`.

## Artifacts, Ownership And Process Gates

**Applicability:** Each artifact owner decides and updates its own row.<br>
**Status:** pending

This section is deliberately tailored ahead of the canonical template: the heading names process gates alongside artifacts, and `Contract release` appears as a User-owned gate row. The current canonical template offers neither. Tailoring is piloted here so the follow-up Contract that changes the template can rely on observed use rather than on an untested design. Until that Contract closes, this shape is a pilot and not the authoritative template.

| Artifact or gate | Included | Owner | Completion evidence | Status |
|---|---|---|---|---|
| Intent and outcome | yes | Syspilot Project Manager | Goal, value, scope, and observable outcome are explicit and coherent | approved |
| Contract release | yes | User | Released by the User on 2026-08-28 for autonomous execution, after requiring that the collaboration mode describe execution behavior only and that this table name process gates alongside artifacts; no other actor may set this row | approved |
| Version control | yes | Syspilot Project Manager | `feature/version-control-ownership`, squash-integrated into `development` at closure | merged |
| Product specification and architecture decisions | yes | Syspilot Architect | The version-control artifact, its ownership, its status values, and the excluded `main` promotion are specified and consistent with the Change Process | complete |
| User-facing documentation | yes | Syspilot Technical Writer | Documentation impact is assessed from changed Requirements; `docs/branching.md` and other applicable `doc` Needs state one authoritative rule | complete |
| Implementation and unit verification | yes | Syspilot Developer | Canonical Change Process and template realize the specified version-control ownership; executable-impact assessment and documentation verification are recorded | complete |
| Acceptance test design and results | yes | Syspilot Tester | Black-box scenarios demonstrate the new row, its terminal status, the removed preamble field, the `Included` resolution of the former `NOT APPLICABLE` case, and the excluded `main` promotion | passed |
| Quality review | yes | Syspilot Quality | Quality applied MECE and Trace from both Contract-recorded impacted objects, confirmed the corrected evidence provenance, and recorded `proceed` with no open issue | proceed |
| User validation and approval | yes | User | The User validated the outcome on 2026-08-28 and corrected the review basis to template-versus-specification rather than instance-versus-specification | accepted |
| Closure decision | yes | Syspilot Project Manager | Final outcome, validation disposition, and integration state are recorded | complete |

## Architecture And Specification

**Owner:** Syspilot Architect<br>
**Status:** complete

### Known Evidence

| Source | Observation |
|---|---|
| `docs/Syspilot Processes/change.md`, closure checklist | Requires integration "by the authorized actor" without defining that actor anywhere |
| `docs/Syspilot Processes/change.md`, initialization step 2 | Delegates branch creation to "the project's branching policy", which does not exist as an artifact |
| `docs/change-contract.md` | Already states that the Project Manager creates a feature branch at Contract release, so branch creation is confirmed rather than newly assigned |
| `docs/branching.md` | Designates the Contract's `Branch:` field as the only authoritative place for a branch name; must follow the field's removal |
| `docs/syspilot/requirements/req_change_contract.rst` | Requires that the integration state is recorded, but names no integration authority |

### Affected Artifacts

| Artifact | Change | Rationale |
|---|---|---|
| `SYSP_REQ_CHANGE_CONTRACT` | modify | Names version control as an owned artifact, its Project Manager owner, its `active` and `merged` statuses, its single branch location, the `Included` resolution, and the excluded `main` promotion; also removes the Requirement's own delegation to a nonexistent branching policy |
| `SYSP_VC_CHANGE_CONTRACT_1` | modify | Makes each of those properties checkable by inspection of the realized process and template |
| `docs/Syspilot Processes/change.md`, canonical template artifact table | modify, Developer-owned | Realize the Project Manager-owned version-control row with `active` and `merged` |
| `docs/Syspilot Processes/change.md`, initialization step 2 | modify, Developer-owned | Replace the delegation to a nonexistent branching policy with the specified Project Manager duty |
| `docs/Syspilot Processes/change.md`, preamble `Branch:` field | remove, Developer-owned | The artifact row becomes the single place the branch name is recorded |
| `docs/Syspilot Processes/change.md`, closure checklist | modify, Developer-owned | The previously undefined "authorized actor" is now the version-control artifact's owner, and `merged` being terminal already enforces integration |
| `docs/branching.md` | modify, Technical Writer-owned | It currently states that the Contract's `Branch:` field is the only place a branch name is binding, which the field's removal invalidates |

### Decisions And Evidence

| Decision or check | Evidence |
|---|---|
| Gap independently verified | `docs/Syspilot Processes/change.md` line 205 requires integration "by the authorized actor" and no artifact, process, or Requirement defined that actor; line 31 delegated branch creation to "the project's branching policy"; a repository-wide search found that policy only as prose in Contracts, never as an artifact |
| The Requirement carried the same defect | `SYSP_REQ_CHANGE_CONTRACT` itself delegated initialization to "the project's branching policy". The specification was therefore part of the gap, not merely a bystander, and now names the Project Manager directly |
| Branch creation confirmed, not newly assigned | `docs/change-contract.md` already states that the Project Manager creates a feature branch, so the specification records existing behavior rather than moving authority |
| No new closure rule added | `merged` is terminal, so the existing condition that every included artifact carries a terminal status enforces integration. Adding a separate integration rule would duplicate an already sufficient one |
| Single-writer rationale preserved in the specification | The Requirement states that all actors share one working tree, so a branch switch changes state for every actor at once, and that creation and integration therefore stay with the actor holding responsibility at exactly those two moments |
| `development` and `main` named concretely | The released scope settled these two names. Introducing an abstraction for branch naming would reopen a settled decision; adoptability of different names remains a reader-view concern of `docs/branching.md`, which already says a project may choose another shape |
| Release authority not granted | The Requirement limits the authority to creating the branch and squash-integrating it into `development`, and states that promotion of `development` to `main` belongs to the Syspilot Release actor within a Release Contract |
| Piloted table shape deliberately not specified | The renamed "Artifacts, Ownership And Process Gates" heading and the User-owned `Contract release` gate row are excluded from this Change. Nothing in the modified Requirement or Verification Criterion refers to them, so the follow-up Contract remains free to decide that design |
| Closed Contracts left untouched | No archived Contract in `docs/changes/` was modified; they record what was agreed at the time |
| New finding for the Technical Writer | `docs/branching.md` has no `doc` Need and appears in no `includes` link, so it is invisible to impact analysis from `SYSP_REQ_CHANGE_CONTRACT`. That is why its now-stale authority statement was not surfaced by traceability and had to be found by reading |
| Specification validation | `python docs/docs-build.py clean` passed with `Schema validation completed with 0 warning(s)` and `build succeeded`; `python docs/test_docs_build.py` passed 4/4; `git diff --check` passed |
| Traceability validation | Exported `needs.json` confirms `SYSP_VC_CHANGE_CONTRACT_1` still verifies `SYSP_REQ_CHANGE_CONTRACT`, that the Requirement no longer contains "branching policy", and that it now states the `merged` status and the excluded `main` promotion |

## User-Facing Documentation

**Owner:** Syspilot Technical Writer<br>
**Status:** complete

### Documentation Plan And Ownership

| Documentation surface | `doc` Need | Requirements included | Status |
|---|---|---|---|
| `docs/branching.md` | `SYSP_DOC_BRANCHING` (added) | `SYSP_REQ_CHANGE_CONTRACT`, `SYSP_REQ_SETUP`, `SYSP_REQ_RELEASE` | verified |
| `docs/change-contract.md` | `SYSP_DOC_CHANGE_CONTRACT` | `SYSP_REQ_CHANGE_CONTRACT`, unchanged link set | verified |
| `docs/methodology.md` | `SYSP_DOC_METHODOLOGY` | `SYSP_REQ_CHANGE_CONTRACT`, unchanged link set | verified without change; it describes Contract types and authority and makes no branch claim |

### Consultations And Factual Reviews

| Documentation surface | Consulted artifact owner | Review question | Evidence and disposition |
|---|---|---|---|
| Branch authority wording | Not requested; the modified `SYSP_REQ_CHANGE_CONTRACT` and the realized Change process each state their part directly | Do the guides state the new rule without granting authority the Requirement withholds? | Two sources, deliberately kept apart. From `SYSP_REQ_CHANGE_CONTRACT`: the Project Manager owns version control, the artifact row is the single branch location, `active` and `merged` are its statuses, the branch is squash-integrated into `development`, and promotion of `development` to `main` is excluded and belongs to Release. From `docs/Syspilot Processes/change.md` step 2: the branch is created from `development`. The Requirement names who creates the branch and how it is named, not where it comes from. `docs/branching.md` introduces that list as what the Change process fixes and attributes the origin accordingly, so no reader-facing statement required correction |

### Changed Documentation And Verification

| Artifact | Change | Verification evidence |
|---|---|---|
| `docs/branching.md` | Replaced the now-false rule that the Contract's `Branch:` field is the only binding branch location. The page now opens with the version-control artifact row, its Project Manager owner, its evidence, and its `active`/`merged` statuses, explains the `Included` resolution instead of a placeholder value, and adds what the process and the Requirement prescribe: branch creation from `development`, which is stated by Change process step 2, together with the joint initial commit, squash integration at closure, and the excluded promotion to `main`, which are stated by `SYSP_REQ_CHANGE_CONTRACT`. Retention, local-only branches, and the repository shape moved under an explicit "What This Repository Practices" heading so prescription and practice stay distinguishable | Strict Sphinx/schema build passes with zero warnings; `python docs/test_docs_build.py -v` passes 4/4; `git diff --check` passes; a targeted scan confirms no statement about a binding `Branch:` field remains |
| `docs/change-contract.md` | Named `development` as the branch origin, matching Change process step 2, and added version control to the artifact list the guide enumerates, with a sentence on why the branch belongs in a row rather than in prose | Same build and test evidence |
| `docs/syspilot/documentation/index.rst` | Added `SYSP_DOC_BRANCHING` | Impact query from `SYSP_REQ_CHANGE_CONTRACT` now returns `SYSP_DOC_BRANCHING` alongside `SYSP_DOC_CHANGE_CONTRACT` and `SYSP_DOC_METHODOLOGY`, so the guide is discoverable by traceability rather than by reading |

### Impact Assessment

The Architect recorded that `docs/branching.md` was invisible to impact analysis, which is why its stale authority statement had to be found by reading. That gap is now closed. When the guide was created it had no requirement to include, and inventing one would have faked a coupling; `SYSP_REQ_CHANGE_CONTRACT` now genuinely states branch authority, so the link is real rather than convenient.

| Requirement | Incoming documentation consumers | Disposition |
|---|---|---|
| `SYSP_REQ_CHANGE_CONTRACT` (modified) | `SYSP_DOC_CHANGE_CONTRACT`, `SYSP_DOC_METHODOLOGY`, and now `SYSP_DOC_BRANCHING` | All three assessed; two updated, methodology verified unchanged |

## Implementation And Unit Verification

**Owner:** Syspilot Developer<br>
**Status:** complete

### Decisions And Evidence

| Decision | Chosen approach | Relevant alternatives | Rationale and evidence |
|---|---|---|---|
| Version-control lifecycle realization | One Project Manager-owned `Version control` artifact records the feature branch and uses `active`, `merged`, or owner-decided `not applicable`; initialization creates the feature branch from `development` and Closure relies on terminal artifact status | Keep the duplicated preamble field, delegate to an external branching policy, or retain a separate undefined integration checklist item | A single lifecycle row realizes the approved Requirement without duplicating branch authority or adding a second closure rule; `merged` is terminal, so the existing all-artifacts-terminal condition enforces integration |
| Executable impact | No script or automated test changes | Update tests speculatively | Repository-wide search of Python files found no assertion or parser dependency on `Branch:`, `branching policy`, `authorized actor`, or the removed integration checklist sentence |

### Changed Artifacts And Verification

| Artifact | Change | Verification evidence |
|---|---|---|
| `docs/Syspilot Processes/change.md` | Replaced branching-policy delegation, removed the `Branch:` preamble field, added the Project Manager-owned version-control row, and removed the redundant undefined integration checklist item | Direct inspection satisfies `SYSP_VC_CHANGE_CONTRACT_1`; strict Sphinx/schema build passes with zero warnings; docs tests pass 4/4; `git diff --check` passes |

## Acceptance Testing

**Owner:** Syspilot Tester<br>
**Status:** passed

| Scenario | Traces to | Result | Evidence |
|---|---|---|---|
| The canonical Change Contract carries one Project Manager-owned version-control artifact row | owned artifact | pass | Structural inspection found exactly one `Version control` row in the canonical template, owned by the Syspilot Project Manager, with branch name and integration state as evidence |
| A Change Contract records its branch in exactly one canonical field | single-authority scope | pass | The canonical template contains no `Branch:` preamble field; its sole branch evidence field is the version-control row. Archived Contracts retain their historical preambles as the approved scope requires, but no current process or guide designates those fields as authoritative |
| The version-control row reaches `merged` only after squash integration into `development` | status vocabulary | pass | `SYSP_REQ_CHANGE_CONTRACT` defines `merged` only once the branch has been squash-integrated into `development`, explicitly identifies `merged` as terminal, and the canonical Closure requires terminal status and completion evidence for every included artifact |
| A Change with no versioned artifacts expresses this through `Included`, without a `NOT APPLICABLE` branch value | contradiction resolution | pass | The canonical row offers `yes / not applicable: {reason}` in `Included`; the Requirement directs no-branch Changes to that column, and direct scans of the current process and guides found no `Branch: NOT APPLICABLE` sentinel |
| The specification does not grant the Project Manager promotion from `development` to `main` | excluded authority | pass | `SYSP_REQ_CHANGE_CONTRACT` limits Project Manager authority to branch creation and squash integration into `development`, explicitly assigning promotion from `development` to `main` to Syspilot Release within a Release Contract |

## Quality Review

**Owner:** Syspilot Quality<br>
**Status:** proceed

**Current judgment:** `proceed`

The version-control artifact is coherent across the Requirement, canonical Change Process and template, user-facing guides, Acceptance evidence, and explicit Release boundary. Q-01 is resolved because documentation evidence now attributes branch origin to Change process step 2 and keeps the Requirement's ownership, lifecycle, integration, single-location, and release-exclusion authority distinct.

### Applied Review Methods

| Method | Selected scope | Evidence | Findings | Limits |
|---|---|---|---|---|
| MECE horizontal coverage | `same-document` and `all-type` for `SYSP_REQ_CHANGE_CONTRACT` and `SYSP_VC_CHANGE_CONTRACT_1` | Fresh built data returned no same-document peers. The exact Requirement peers were `SYSP_REQ_ACTOR_MODEL`, `SYSP_REQ_ARCHITECT`, `SYSP_REQ_CONTRACT_DOCUMENTS`, `SYSP_REQ_CONTRACT_HANDLING`, `SYSP_REQ_DEVELOPER`, `SYSP_REQ_IMPACT_QUERY`, `SYSP_REQ_MECE_ANALYSIS`, `SYSP_REQ_ONTOLOGY_EDITING`, `SYSP_REQ_ONTOLOGY_SCHEMA`, `SYSP_REQ_PROJECT_MANAGER`, `SYSP_REQ_QUALITY`, `SYSP_REQ_RELEASE`, `SYSP_REQ_RESEARCH`, `SYSP_REQ_SETUP`, `SYSP_REQ_TECHNICAL_WRITER`, `SYSP_REQ_TESTER`, `SYSP_REQ_TRACE_ANALYSIS`; the exact VC peers were `SYSP_VC_ACTOR_MODEL_1`, `SYSP_VC_ARCHITECT_1`, `SYSP_VC_CONTRACT_DOCUMENTS_1`, `SYSP_VC_CONTRACT_HANDLING_1`, `SYSP_VC_DEVELOPER_1`, `SYSP_VC_IMPACT_QUERY_1`, `SYSP_VC_MECE_ANALYSIS_1`, `SYSP_VC_ONTOLOGY_EDITING_1`, `SYSP_VC_ONTOLOGY_SCHEMA_1`, `SYSP_VC_PROJECT_MANAGER_1`, `SYSP_VC_QUALITY_1`, `SYSP_VC_RELEASE_1`, `SYSP_VC_RESEARCH_1`, `SYSP_VC_SETUP_1`, `SYSP_VC_TECHNICAL_WRITER_1`, `SYSP_VC_TESTER_1`, `SYSP_VC_TRACE_ANALYSIS_1`. Quality read the complete peer content and compared role, process, release, Setup, and Contract-handling boundaries | No overlapping or contradictory obligation, missing semantic coverage, ambiguous partition, or responsibility collision. Version-control authority belongs to the Change Contract Requirement, while release publication remains separate | Built Needs contain no structured quality claims, so automation reports `structured-coverage-data-unavailable`; semantic review supplied the judgment. The same-document scope reports `no-comparable-peers-discovered` |
| Trace relationship and chain analysis | `--direction both --depth 2` for both impacted objects | `SYSP_REQ_CHANGE_CONTRACT` returned the exact 25-object neighborhood `ROOT_SYSPILOT`, `SYSP_AC_CHANGE_CONTRACT_1`, `SYSP_DOC_BRANCHING`, `SYSP_DOC_CHANGE_CONTRACT`, `SYSP_DOC_METHODOLOGY`, `SYSP_DOC_PRODUCT_MODEL`, `SYSP_REQ_ACTOR_MODEL`, `SYSP_REQ_ARCHITECT`, `SYSP_REQ_CHANGE_CONTRACT`, `SYSP_REQ_CONTRACT_DOCUMENTS`, `SYSP_REQ_CONTRACT_HANDLING`, `SYSP_REQ_DEVELOPER`, `SYSP_REQ_IMPACT_QUERY`, `SYSP_REQ_MECE_ANALYSIS`, `SYSP_REQ_PROJECT_MANAGER`, `SYSP_REQ_QUALITY`, `SYSP_REQ_RELEASE`, `SYSP_REQ_SETUP`, `SYSP_REQ_TECHNICAL_WRITER`, `SYSP_REQ_TESTER`, `SYSP_REQ_TRACE_ANALYSIS`, `SYSP_US_CHANGE_CONTRACT`, `SYSP_US_CONTRACT_DOCUMENTS`, `SYSP_VC_CHANGE_CONTRACT_1`, `SYSP_VC_CONTRACT_HANDLING_1`. `SYSP_VC_CHANGE_CONTRACT_1` returned the exact seven-object neighborhood `SYSP_DOC_BRANCHING`, `SYSP_DOC_CHANGE_CONTRACT`, `SYSP_DOC_METHODOLOGY`, `SYSP_REQ_CHANGE_CONTRACT`, `SYSP_REQ_CONTRACT_HANDLING`, `SYSP_US_CHANGE_CONTRACT`, `SYSP_VC_CHANGE_CONTRACT_1` | All discovered edges resolved and matched ontology-permitted types and directions; no structural finding. Semantic review confirmed the canonical process, Requirement, VC, three linked documentation surfaces, inherited Contract handling, Story intent, and excluded Release authority are coherent | The analyzer reports `semantic-content-review-required`; Quality discharged that limit by reading every resolved neighbor relevant to the changed obligations. Ontology relationships are permitted rather than required |

### Open Quality Issues

| Artifact | Current issue | Required outcome |
|---|---|---|
| None | None | None |

## User Validation And Approval

**Owner:** User<br>
**Recorded by:** Syspilot Project Manager<br>
**Status:** accepted

**Decision and evidence:** The User validated the outcome on 2026-08-28 after the Project Manager checked the canonical template against each clause of the changed Requirement. The User also corrected the Project Manager's review basis: this Contract instance was copied from the previous template, so it cannot satisfy a rule it produces, and conformance is a property of the template and of Contracts created from it.

## Closure

**Owner:** Syspilot Project Manager<br>
**Status:** closed

- [x] Every included artifact or gate has terminal status and completion evidence.
- [x] Intent and outcome are `approved`.
- [x] The version-control artifact is `merged`.
- [x] No surface still designates the `Branch:` preamble field as authoritative.
- [x] Promotion from `development` to `main` remains outside Project Manager authority.
- [x] Quality has recorded a `proceed` judgment.
- [x] Open Quality Issues contains `None`.
- [x] User validation is `accepted`.
- [x] Current blocker is `none`.
- [x] The observable outcome is demonstrated.

**Final outcome:** Version control is now a named artifact of the Change Contract, owned by the Syspilot Project Manager, with `active` and `merged` as its statuses. Because `merged` is terminal, the existing closure condition enforces integration and the separate integration checklist line was removed rather than duplicated. The branch name lives in exactly one place, a Change needing no branch says so through `Included`, and promotion of `development` to `main` is explicitly excluded from that authority and reserved for the Syspilot Release actor.

The Project Manager verified the template against each clause of the changed Requirement rather than restating Quality's report: initialization step, artifact row, absent preamble field, `Included` expression, and the excluded `main` promotion each check out. Documentation tests 4/4, schema validation and strict build at zero warnings.

**Scope note carried forward:** this Contract instance retains the preamble `Branch:` field because it was copied from the previous template. Instances are not retrofitted; the rule governs the template and the Contracts created from it.

**Integration:** Squash-integrated into `development`; no public push was performed.
