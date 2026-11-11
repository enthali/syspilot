# Change Contract: Pre-Initial-Release Review

**Status:** closed<br>
**Process owner:** Syspilot Project Manager<br>
**Current responsibility:** Syspilot Project Manager<br>
**Current blocker:** none<br>
**Created:** 2026-08-26<br>
**Branch:** feature/pre-initial-release-review<br>
**Collaboration mode:** Strictly user-guided, one file at a time. No artifact review, edit, consultation, commission, handoff, commit, or next-file selection occurs until the User approves the current checkpoint. The User selects or accepts the next file before its review starts. For the current file, the Project Manager and User inspect it together. They involve at most one factual owner at a time, and only after the User agrees that the concrete question requires that consultation. Consultation is read-only and does not transfer Current responsibility. If an owner must change an owned artifact, the Project Manager first records the User-approved required outcome, then performs the normal committed responsibility handoff. After the result returns, the User accepts that file's disposition before another file begins.

## Intent And Outcome

**Owner:** Syspilot Project Manager<br>
**Status:** approved<br>
**Approval evidence:** The User reviewed the complete proposed Contract and explicitly released it on 2026-08-26.

### Goal

Review the complete prospective Syspilot v2 release surface with the User before the initial v2 release, one file at a time, so that each included artifact is current, understandable, intentionally public or private, and free of unresolved v1 assumptions that would make the release misleading or unusable.

### Value

The initial v2 release is based on a repository state the User has examined deliberately rather than on a final bulk review. Readers receive coherent current guidance, release machinery acts on the intended files, private instance state stays private, and remaining work is visible before the Release Contract selects a candidate.

### Scope

- Review the prospective release surface area by area and exactly one file at a time. The review includes tracked root artifacts, `.github/` release and product infrastructure, `.syspilot/`, `syspilot/`, current user documentation, specifications, process and Actor documents, release configuration, tests, and packaging inputs.
- For each file, determine its purpose, audience, factual owner, release applicability, reader friendliness, v1/v2 status, consistency with authoritative artifacts, and disposition.
- Record one disposition before continuing: confirmed current; changed and accepted; retained as clearly historical evidence; excluded from the release boundary; blocked on a decision; or moved to a separately released Change.
- Preserve historical Contracts, release notes, and experience reports as evidence. Do not rewrite past decisions merely to use current terminology. Add present-day framing only when a direct reader could mistake historical material for current guidance.
- Review local and private surfaces only to define the release boundary. Private Actor memory, Jarvis runtime state, locally excluded instructions, workspace-specific generated state, and unrelated untracked files do not become release content through this Change.
- State the Sphinx-Needs boundary accurately where relevant: Contract Driven Development and ontology concepts are not inherently tied to Sphinx-Needs; Sphinx and Sphinx-Needs remain the only currently supported reference realization. Do not implement or claim another backend.
- Review the private Actor-memory repository guidance where its user-facing document is selected. The local instruction itself remains private instance configuration and is not a release artifact.
- Review release automation, version surfaces, release notes, packaging inputs, and publication assumptions. A required correction may be completed in this Change when it remains bounded and the responsible owner accepts it; larger capability work receives a separate Change.
- Use the existing Actor roster and normal Contract handling. This is a tailored Change, not a new Contract type and not a standing pre-release workflow.
- Do not create the `0.10.0` release instance or publish anything in this Change. The reviewed outcome becomes input to the later Release Contract.
- Preserve the unrelated untracked `.github/agents/` directory and do not push any repository without explicit User authorization.

### Observable Outcome

Every tracked file at the named review baseline belongs to exactly one User-accepted file or collection disposition. Current public entry points describe the v2 release they are shipped with; retained historical material is distinguishable from current instruction; release and Setup claims match the reviewed artifacts; private and local-only state is outside the release boundary; all corrections included in this Change have owner evidence; the strict documentation build and applicable focused checks pass; and every discovered blocker to a future release candidate is explicit, assigned, and planned as follow-up work.

## File Review Control

**Owner:** Syspilot Project Manager<br>
**Status:** complete

Only one row may have status `in review` at a time. A row is added when the User selects the file. No collection-level disposition substitutes for reviewing a file unless the User explicitly approves a named collection rule after seeing its contents and reason.

| Sequence | File | Factual owner | Review question | Disposition | User checkpoint | Status |
|---|---|---|---|---|---|---|
| 1 | `.github/workflows/release.yml` | Syspilot Release | Does the workflow represent current v2 release validation and publication behavior, and should it be included in the initial v2 release? | Changed and accepted: manual runs validate and build only; valid `vMAJOR.MINOR.PATCH` tag pushes publish Pages and then create the GitHub Release. Prerelease and build-metadata tags are intentionally unsupported. The workflow now uses Python 3.13, `uv`, strict documentation checks, exact tag-selected release notes, tag-gated publication, and least-privilege job permissions. Open dependency-lock reproducibility remains a later Release Contract input, not a defect in this workflow correction. | User accepted the corrected file and fixed the three-number-only tag policy on 2026-08-26 | complete |
| 2 | `.github/copilot-instructions.md` | Syspilot Project Manager | Is this workspace-wide project-governance instruction still authoritative in v2, or has its useful content moved to focused Instructions, Contracts, and current documentation? | Changed and accepted: retained only the PM-owned workspace language rule. Removed the stale v1 hierarchy, product/instance copying model, obsolete dogfooding warning, and No-Blame duplication already supplied to every session by the Jarvis Actor Kernel. Syspilot-specific technical Instructions remain Architect-owned; this workspace-level governance file does not. | User confirmed Project Manager ownership and accepted the reduced file on 2026-08-27 | complete |
| 3 | `.syspilot/ontology.toml` | Syspilot Architect | Is the current v2 ontology authoritative, validated, and ready to remain unchanged in the initial v2 release? | Confirmed current without change. The ontology was established and repeatedly validated through the closed v2 Foundation and Documentation Foundation work; it has no working-tree delta, and this review identified no new ontology decision. | User accepted the existing ontology based on its repeated prior reviews on 2026-08-26 | complete |
| 4 | `assets/syspilot-logo.svg`, `assets/syspilot-logo-dark.svg` | Syspilot Technical Writer | Are the tracked release assets intentional and suitable for the initial v2 release? | Confirmed current without change. The complete tracked `assets/` collection contains only the standard light and dark Syspilot SVG logos. | User explicitly approved these two files as one named logo collection on 2026-08-26 | complete |
| 5 | `docs/experiences/` | Syspilot Technical Writer | Should the Field Notes remain unchanged as historical stories, and does each direct-entry story identify the Syspilot version it describes? | Retained unchanged as historical evidence. The collection contains eight stories plus its index; every story has a direct-entry `Versions` section naming a concrete Syspilot version from `0.5.x` through `0.9.0`. Historical terminology and behavior therefore remain attributable to their observed product state rather than current v2 guidance. | User approved the complete version-qualified historical collection on 2026-08-26 | complete |
| 6 | `docs/syspilot/`, `docs/Syspilot Actors/`, `docs/Syspilot Processes/`, `docs/traceability/` | Syspilot Architect | Are the current specification, Actor, process, and generated traceability collections already reviewed or derived from validated v2 sources? | Confirmed current as named collections without further file-by-file review in this Change: 34 specification files, 9 Actor documents, 4 Process documents, and 1 traceability source/output entry. | User identified these collections as already reviewed or generated and accepted them on 2026-08-26 | complete |
| 7 | `README.md`, `docs/getting-started.md`, `docs/product-model.md`, `docs/change-workflow.md`, `docs/customization.md`, `docs/operations.md` | Syspilot Technical Writer | Are the six Technical Writer-owned `doc` Need surfaces current and acceptable for this review? | Confirmed current as the existing verified documentation ownership map. Each surface has a dedicated `doc` Need, `realized_by` path, and requirement coverage through `includes`. | User accepted all six Technical Writer-owned surfaces on 2026-08-26 | complete |
| 8 | `docs/methodology.md` | Syspilot Technical Writer | Does this document describe current v2 behavior, and is it worth keeping? | Changed and accepted: rewritten as Syspilot's Contract Driven Development methodology. Removed the agent-family framework, `sysmlv2`/`common` families, US/REQ/SPEC hierarchy, repository trees, write-boundary table, and agent-versus-skill model. States the two defined Contract types, per-artifact ownership with a single responsible writer, collaboration modes, why no fixed workflow exists, and the Sphinx-Needs realization boundary. Records that releases have no process of their own yet. Moved from the legacy toctree to the User Guides, and registered as `SYSP_DOC_METHODOLOGY` including `SYSP_REQ_RELEASE` so a future release Change reaches it. | User approved the colleague methodology document as the style template, requested the release sentence, and asked for the `doc` Need on 2026-08-26 | complete |
| 9 | `docs/architecture.md` | Syspilot Technical Writer | Is this document still needed, and what is its value in v2? | Excluded from the release by deletion. Every concrete claim was false for v2: the `syspilot/` product directory, `.syspilot/ontologies/` and `capabilities/`, the Setup Agent copy model, per-agent and per-skill tailoring files, `syspilot.toml` as ontology authority, and the removed agent roster. Its only durable idea, the product-versus-instance boundary, is already in `docs/product-model.md`. Removed from the toctree and the referring footer in `docs/workflows.md`. | User decided deletion over rewriting on 2026-08-26 | complete |
| 10 | `docs/change-workflow.md` | Syspilot Technical Writer | Is the guide factually current, and does its tone hold a reader? | Changed and accepted: numbered steps replaced by named sections plus an explicit statement that the order is usual rather than prescribed, because the numbering contradicted the guide's own claim that no universal sequence exists. Corrected "five agents" to eight actors, compressed the Impact Python description into one paragraph, added the reasons behind the ownership and closure rules, and replaced a pointer to a single closed Contract with an explanation of why `docs/changes/` is deliberately outside the rendered documentation. | User requested the tone review and approved the proposed rework on 2026-08-26 | complete |
| 11 | `docs/customization.md` | Syspilot Technical Writer | Same review lens: factual currency and reader value. | Changed and accepted: dissolved the empty `Tune Knowledge and Tools` signpost section, gave the ontology and documentation-matrix levels their missing reasons, ended the skills section with why the product-versus-project distinction matters, fixed a mid-sentence line break and an inconsistent checklist indent, and recorded that versioning actor memory is a project decision resolved during Setup. | User approved all five proposed corrections on 2026-08-26 | complete |
| 12 | `docs/getting-started.md` | Syspilot Technical Writer | Does the guide describe the official installation path? | Changed and accepted: the guide previously offered cloning this repository as the way in. It now leads with a copy-paste bootstrap prompt that resolves the release with the User, fetches that tag's Setup Contract, materializes it as `.syspilot/setup-contract.md`, and executes it; the clone is demoted to an optional worked example. The prompt carries no hard-coded release tag, so no document has to be touched per release, and release selection stays with bootstrap as the Pristine Setup decisions require. A prohibition without an alternative was replaced by "consult me on how to proceed". | User established that the specified bootstrap prompt had never been written, chose the generic release-resolving form, and corrected the closing instruction on 2026-08-26 | complete |
| 13 | `docs/ontology-reference.md` | Syspilot Architect | Should this auto-generated page be committed so that it is delivered? | Retained unchanged and deliberately uncommitted. The page is generated by a `builder-inited` hook in Syspilot's own `docs/conf.py` on every build and is ignored by `.gitignore`; Syspilot's published Pages therefore contain it. Committing it would create a second, drifting source of truth and would ship Syspilot's ontology to projects that have their own. Review established that installed projects do not receive the generation capability at all, because Setup copies `.syspilot/ontology.toml` but not `conf.py`. Raised with the Project Manager as a separate Change to address after this one. | User accepted keeping the file unchanged and directed that the delivery gap be raised as a follow-up issue on 2026-08-26 | complete |
| 14 | `docs/namingconventions.md` | Syspilot Technical Writer | Is the naming scheme still valid, and what is the current v2 rule? | Changed and accepted. Removed the demonstrably false v1 content: the THEME segment, the `SYSMLV2_`/`INST_`/`COMMON_` prefixes, the `SPEC` type, the `docs/inst/` and `docs/common/` directories, and the cross-family link examples. Kept the case for descriptive IDs, build-time uniqueness, the slug rules, and the rename procedure. The Architect's read-only assessment shaped the result: the ontology's per-type `prefix` values govern auto-generated IDs and are not a contract for explicit ones; `SYSP_<TYPE>_<SLUG>` is this repository's observed convention across all 67 active non-root IDs rather than a v2 rule; the customer project-prefix policy is genuinely undecided; and `ROOT_SYSPILOT` is the deliberate singleton root. The page now separates what the build enforces from what this repository practices, and states the undecided part as undecided. Moved from the legacy toctree to Reference. | User accepted the Architect-grounded rewrite and the decision to leave it without a `doc` Need on 2026-08-26 | complete |
| 15 | `docs/workflows.md` → `docs/branching.md` | Syspilot Technical Writer | Is the historical workflow guide still needed, and what of it is current? | Replaced. Deleted the v1 workflow content: the design/implement/uat/verify/docu chain, the three workflows, manager orchestration, the agent-selection table, and the reference to the removed `syspilot.branching` skill. Its branching content was cross-checked against actual Git state and against `change.md` and `setup.md`, and the User confirmed the practices are the intended rules. The new `docs/branching.md` states that a Contract's `Branch:` field is where a branch name is binding, quotes Setup's prescribed branch lifecycle, and presents the integration shape, retention, local-only feature branches, and `main`-only releases as what this repository does. Eight findings about missing Contract authority were reported to the Project Manager rather than filled in with plausible rules. Removing this file emptied the Legacy v1 Guides section, which is now gone from the index. | User directed the replacement and confirmed the branching rules on 2026-08-26 | complete |
| 16 | `README.md` | Syspilot Technical Writer | Is the project portal factually current, and does it read well enough to keep a visitor? | Changed and accepted. The copy-paste bootstrap prompt now leads the page, so the official installation path is the first thing a reader can act on. Removed the duplicated setup paragraph that had accumulated at the end. Added Methodology and Branching to the entry table. Gave Jarvis prominent credit as the framework that makes persistent actors possible, linked Sphinx-Needs, and added `enthali.jarvis-kanban`, whose description was verified against the marketplace listing. Backend neutrality is now evidenced rather than asserted, by pointing at `enthali/zonal-rc-car`, which runs the same Contract-driven actor organisation on a SysML v2 model. The early-research boundary and the absent runtime proof are stated plainly. | User requested the tone, the Jarvis and Sphinx-Needs links, the kanban extension, and the backend-neutrality reference, and corrected the extension-count wording on 2026-08-26 | complete |
| 17 | `docs/change-workflow.md` → `docs/change-contract.md` | Syspilot Technical Writer | Does the guide's name match what it describes, and can a diagram show the model without reintroducing a fixed sequence? | Renamed and extended. The file, its title, and its `doc` Need are now `change-contract`, `The Change Contract`, and `SYSP_DOC_CHANGE_CONTRACT`; calling the main guide a workflow contradicted the methodology's own argument that no standing workflow exists. All six references were repointed. A Mermaid diagram was added directly under the introduction showing one real Change's responsibility path, with a dashed consultation edge and a caption stating that another Change visits different owners and that consultation moves no responsibility — a sequence diagram would have re-established exactly the fixed relay the guide denies. | User proposed both the rename and the example diagram on 2026-08-26 | complete |
| 18 | `docs/Syspilot Processes/setup.md` | Syspilot Project Manager | Does Setup obtain the User's decision on whether actor memory is versioned? | Changed and accepted: Setup always shows the current ignore result and asks whether all eight generated Actor directories shall be versioned or kept private and ignored. The prior conditional question could silently version Actor working notes when the target did not already ignore them; the corrected sequence now satisfies the inventory's explicit-User-decision evidence in every case. | User selected the always-ask option on 2026-08-26 | complete |

### Tracked-File Collection Matrix

**Baseline:** `9a63eb06ed3e6ee87964b5132be9afcf5bc4b1e1` with 215 tracked files<br>
**Status:** accepted by User on 2026-08-27 after reviewing the corrected documents

Each tracked file belongs to exactly one row. The matrix groups files by stable purpose and authority rather than requiring 215 individual reviews.

| Collection | Count | Disposition basis |
|---|---:|---|
| Root metadata: `.gitattributes`, `.gitignore`, `LICENSE` | 3 | Repository metadata and MIT license retained as release inputs; `README.md` is reviewed separately |
| `README.md` | 1 | Individually reviewed and accepted in row 16 |
| `.github/copilot-instructions.md` | 1 | Individually reviewed and accepted in row 2 |
| `.github/instructions/` | 1 | Current Contract-handling instruction established and validated by its closed Change |
| `.github/skills/` | 4 | Current Impact and Ontology Skills plus focused scripts were reviewed and validated through v2 Skill Foundations |
| `.github/workflows/` | 1 | Release workflow individually reviewed and accepted in row 1 |
| `.syspilot/` | 1 | Ontology individually reviewed and accepted in row 3 |
| `assets/` | 2 | Technical Writer-owned logo collection reviewed and accepted in row 4 |
| `docs/changes/` | 128 | Active Contract responsibility follows `Current responsibility` while section ownership remains with each factual owner. After Closure, records and versioned historical verification archives are immutable evidence guarded as a collection by the Project Manager; guardianship does not transfer authorship of their claims. Four explicit drafts remain identified as drafts. |
| `docs/experiences/` | 9 | Version-qualified historical collection reviewed and accepted in row 5 |
| `docs/Syspilot Actors/` | 9 | Current v2 Actor collection accepted in row 6 |
| `docs/Syspilot Processes/` | 4 | Current v2 Process collection accepted in row 6; Setup additionally corrected in row 18 |
| `docs/syspilot/` | 34 | Current specification and documentation-ownership graph accepted in rows 6 and 7 and validated by the strict schema build |
| `docs/traceability/` | 1 | Generated traceability view source accepted in row 6 |
| Documentation support: `docs/_static/`, `docs/_templates/` | 2 | Build support retained; strict build verifies both are consumable |
| Root documentation and build inputs under `docs/` | 14 | User guides/references were individually or collection-reviewed; `conf.py`, `docs-build.py`, `requirements.txt`, and `test_docs_build.py` are validated build inputs; `releasenotes.md` remains the historical release record and later Release Contract input |

## Artifact Applicability And Ownership

**Applicability:** Each artifact owner decides and updates its own row when the User brings that owner into the current file review.<br>
**Status:** pending

| Artifact type | Included | Owner | Completion evidence | Status |
|---|---|---|---|---|
| Intent and outcome | yes | Syspilot Project Manager | Goal, value, scope, collaboration checkpoints, and observable outcome are explicit and User-approved | approved |
| Product specification and architecture decisions | not applicable: no Architect-owned product artifact is delivered; Architect participated through bounded factual consultation | Syspilot Architect | Changed `doc` Needs remain Technical Writer-owned; no architecture artifact changed | not applicable |
| User-facing documentation | yes | Syspilot Technical Writer | The Technical Writer assesses selected user-facing surfaces; changed prose is coherent and factually reviewed; applicable `doc` Needs remain current | complete |
| Implementation and unit verification | not applicable: no Developer-owned implementation is delivered | Syspilot Developer | Changed technical documentation surfaces use their focused validation evidence | not applicable |
| Acceptance test design and results | not applicable: the Change claims review completion, not runtime product acceptance | Syspilot Tester | Direct User checkpoints accept each selected disposition | not applicable |
| Release automation | yes | Syspilot Release | Changed `.github/workflows/release.yml` is reviewed against the User-decided publication behavior and accepted by its factual owner with focused verification evidence | complete |
| Research evidence | not applicable: no research question or Research-owned artifact was included | Syspilot Research | External factual claims used in documentation were directly checked during review | not applicable |
| Quality review | yes | Syspilot Quality | Independent re-review confirmed complete baseline coverage, coherent ownership, bounded Release acceptance, and passing validation; judgment is `proceed` | proceed |
| User validation and approval | yes | User | The User accepts the complete reviewed outcome after accepting each file disposition | accepted |
| Closure decision | yes | Syspilot Project Manager | Final outcome, validation disposition, integration state, and handoff to later Release Contract work are recorded | complete |

## Architecture And Specification

**Owner:** Syspilot Architect<br>
**Status:** not applicable

### Affected Artifacts

| Artifact | Change | Rationale |
|---|---|---|
| not applicable | No Architect-owned artifact changed | Architect supplied bounded factual consultation only |

### Decisions And Evidence

| Decision or check | Evidence |
|---|---|
| Applicability | Changed `doc` Needs are owned by the Technical Writer; no architecture or product specification artifact changed |

## User-Facing Documentation

**Owner:** Syspilot Technical Writer<br>
**Status:** complete

### Documentation Plan And Ownership

| Documentation surface | `doc` Need | Requirements included | Status |
|---|---|---|---|
| `docs/methodology.md` | `SYSP_DOC_METHODOLOGY` (added) | `SYSP_REQ_ACTOR_MODEL`, `SYSP_REQ_CONTRACT_DOCUMENTS`, `SYSP_REQ_CONTRACT_HANDLING`, `SYSP_REQ_CHANGE_CONTRACT`, `SYSP_REQ_SETUP`, `SYSP_REQ_RELEASE` | verified |
| `docs/getting-started.md` | `SYSP_DOC_GETTING_STARTED` | `SYSP_REQ_SETUP` and the bootstrap prompt it presupposes | verified |
| `docs/change-contract.md` | `SYSP_DOC_CHANGE_CONTRACT` (renamed from `SYSP_DOC_CHANGE_WORKFLOW`) | unchanged | verified |
| `docs/customization.md` | `SYSP_DOC_CUSTOMIZATION` | unchanged | verified |
| `docs/architecture.md` | none | deleted; no `doc` Need existed | removed |
| `docs/workflows.md` | none | replaced by `docs/branching.md`; no `doc` Need existed | removed |
| `docs/branching.md` | none yet | No requirement currently states the integration model, branch retention, the local-only rule, or the `feature/` prefix. The link becomes obvious once those findings turn into Contract or specification content | verified as prose; `doc` Need deliberately deferred |
| `docs/namingconventions.md` | none | Naming is not specified by any requirement, so an `includes` edge would claim a coupling that does not exist | verified as prose; `doc` Need deliberately omitted |
| `README.md` | `SYSP_DOC_README` | unchanged | verified |

### Consultations And Factual Reviews

| Documentation surface | Consulted artifact owner | Review question | Evidence and disposition |
|---|---|---|---|
| `docs/namingconventions.md` | Syspilot Architect | Is `SYSP_<TYPE>_<SLUG>` normative, does a customer project choose its own prefix, and is `ROOT_SYSPILOT` a deliberate exception? | Answered on 2026-08-26: the pattern is an observed repository convention across all 67 active non-root IDs and not a v2 rule; the ontology's type `prefix` values apply to auto-generated IDs and are not an explicit-ID naming contract; the customer project-prefix policy is undecided; `ROOT_SYSPILOT` is the deliberate singleton root. The rewrite follows this assessment and documents the undecided part as undecided |
| `docs/branching.md` | Syspilot Project Manager | The Change process delegates to a "project's branching policy" that does not exist in v2 | PM assessment received: the concrete Contract's `Branch:` field is authoritative after User release, and the Change process should not delegate to a nonexistent external policy. Authoring was treated as a cross-check; eight findings about missing authority were reported instead of being resolved in prose |
| `docs/ontology-reference.md` | Syspilot Project Manager | The generated ontology page is not delivered to installed projects | Raised as an issue to address after this Change, with the ignore rule, the `conf.py` hook, and the Setup inventory as evidence |
| `docs/customization.md` | Syspilot Project Manager | The Setup inventory requires an explicit User decision on actor-memory versioning, but the sequence asks only when the paths are already ignored | Raised as a second follow-up issue; the guide wording was weakened accordingly instead of claiming Setup always asks |

### Changed Documentation And Verification

| Artifact | Change | Verification evidence |
|---|---|---|
| `docs/methodology.md`, `docs/change-workflow.md`, `docs/customization.md`, `docs/getting-started.md` | Rewritten for current v2 behavior, reader value, and the official installation path | Strict Sphinx/schema build passes with zero warnings after each file; `python docs/test_docs_build.py -v` passes 4/4; `git diff --check` passes |
| `docs/namingconventions.md` | Rewritten from the Architect's assessment; separates what the build enforces from what this repository practices and records the undecided project-prefix policy | Strict build passes; targeted scan confirms no `FAMILY`, `SYSMLV2_`, `INST_`, `COMMON_`, or THEME wording remains; the one invented example ID was replaced with a real one |
| `docs/workflows.md` → `docs/branching.md` | Legacy workflow guide deleted and replaced by a branching guide derived from Contracts, processes, and verified Git state | Strict build passes with no dangling reference; the Legacy v1 Guides section is gone from `docs/index.rst`; eight authority findings reported to the Project Manager |
| `README.md` | Bootstrap prompt promoted to the entry point; duplicated setup paragraph removed; Jarvis, Sphinx-Needs, kanban, and the SysML v2 sibling project linked | All eight local links resolve to existing files; the kanban description was verified against the marketplace listing; `enthali/zonal-rc-car` was verified reachable after the first URL returned 404 |
| `docs/architecture.md` | Deleted, with toctree entry and referring footer removed | Strict build succeeds with 68 instead of 69 source files and no dangling reference |
| `docs/change-workflow.md` → `docs/change-contract.md` | Renamed with its title and `doc` Need; example-path diagram added | Strict build passes; a targeted scan finds no remaining `change-workflow` path or `SYSP_DOC_CHANGE_WORKFLOW` reference in any current surface |
| `docs/syspilot/documentation/index.rst`, `docs/index.rst` | Added `SYSP_DOC_METHODOLOGY`; moved `methodology` from the legacy toctree to the User Guides | Strict build resolves all six requirement links of the new `doc` Need |
| `docs/ontology-reference.md` | No change | Confirmed generated per build and ignored by `.gitignore`; delivery gap raised with the Project Manager |

## Implementation And Unit Verification

**Owner:** Syspilot Developer<br>
**Status:** not applicable

### Decisions And Evidence

| Decision | Chosen approach | Relevant alternatives | Rationale and evidence |
|---|---|---|---|
| not applicable | No Developer-owned implementation change | None | Focused checks are recorded with the changed workflow and documentation artifacts |

### Changed Artifacts And Verification

| Artifact | Change | Verification evidence |
|---|---|---|
| `.github/workflows/release.yml` | User-guided release-automation correction outside Developer ownership | YAML diagnostics, 4/4 docs-build tests, tag/release-note probes, and publication-gate checks passed |

## Acceptance Testing

**Owner:** Syspilot Tester<br>
**Status:** not applicable

| Scenario | Traces to | Result | Evidence |
|---|---|---|---|
| not applicable: no runtime acceptance claim | file-level User checkpoints | not applicable | Every selected file disposition is recorded; Setup runtime acceptance belongs to later release work |

## Release Readiness

**Owner:** Syspilot Release<br>
**Status:** complete

| Surface | Readiness question | Evidence and disposition |
|---|---|---|
| Version identities | Do all release-facing version sources agree with the intended initial v2 release? | Not assessed because this Change selects no release candidate; the future Release Contract owns exact version identity |
| Package and publication boundary | Are included and excluded repositories, paths, generated artifacts, and private state explicit? | The review and collection matrix identify current public, private, generated, and local-only boundaries; candidate payload selection belongs to the future Release Contract |
| Automation and checks | Do release automation and required checks act on the intended candidate and current toolchain? | Accepted by Syspilot Release at `3f9e051`: manual dispatch validates and builds without publication; only exact `vMAJOR.MINOR.PATCH` tag pushes publish; exact tag-selected notes feed the release; Python 3.13, `uv`, focused tests, and the strict clean documentation build validate the tag tree; Pages succeeds before GitHub Release creation; and publication permissions are job-scoped. Focused probes and editor diagnostics pass. This accepts the workflow artifact only; candidate identity, dependency locking, release notes, and publication authorization remain inputs to the future Release Contract. |
| Release-facing documentation | Are release notes, limitations, and current-versus-historical claims ready for candidate preparation? | Current guides and historical records are reviewed; concrete `0.10.0` notes and limitations belong to the future Release Contract |
| Remaining work | Which blockers or separate Changes must complete before a Release Contract can select a candidate? | Four High-priority follow-ups are recorded on the private PM Kanban: canonical v2 Release Contract and concrete `0.10.0` instance; mandatory `syspilot.mece` and `syspilot.trace` Quality skills; authoritative branching and integration governance behind the derived `docs/branching.md`; and delivery or explicit internal-only disposition of the generated ontology reference. Dependency locking remains an additional Release Contract input. |

### Known Follow-Up Release Blockers

These findings are deliberate outputs of this review, not hidden defects claimed as resolved by it. Quality shall assess whether the delivered review is coherent with these boundaries and whether any finding must instead block this Change itself.

| Finding | Current evidence | Planned authority |
|---|---|---|
| No canonical v2 Release Contract exists | Release actor and Requirement exist, but the process registry has no Release process or template | Separate Change defines the Release process/template, followed by the `0.10.0` Release Contract instance |
| MECE and Trace methods disappeared as explicit capabilities | v2 has no `syspilot.mece` or `syspilot.trace` Skill; generic Architect/Quality language does not define either method | Separate Change specifies both Skills and requires Quality to run both from impacted objects in every Quality Review |
| Branching and integration rules lack Contract authority | `docs/branching.md` can describe observed and User-confirmed practice, while current Change/Setup processes leave eight authority gaps recorded by the Technical Writer | Separate Change makes Contract branch identity, integration, retention, local-only feature branches, Setup relation, and release/main boundaries authoritative |
| Installed projects do not receive ontology-reference generation | Syspilot's own `docs/conf.py` generates the ignored page, while Setup copies the ontology but not this capability | Separate Change either delivers configured-path-aware generation or declares the page Syspilot-internal |

## Research Evidence

**Owner:** Syspilot Research<br>
**Status:** not applicable

No Research-owned artifact or unresolved investigation was included. External factual claims used in the documentation were directly checked during the User-guided review.

## Quality Review

**Owner:** Syspilot Quality<br>
**Status:** proceed

**Current judgment:** proceed

Re-review confirmed that the tracked-file matrix assigns all 215 baseline files exactly once, the current documentation and automation consistently require Python 3.13 or newer, the bootstrap describes the v2 release surface in which it will first be published, and the Observable Outcome now treats Release blockers as explicit follow-up outputs rather than claiming a blocker-free candidate. The User resolved ownership of the workspace governance instruction to the Project Manager, while Syspilot Release accepted the changed workflow automation without claiming candidate readiness.

Independent validation passed the strict documentation and schema build with zero warnings, all four focused documentation tests, exact matrix reproduction with no missing or overlapping assignment, Python-version scans, focused Release-workflow invariants, branch diff checks, and editor diagnostics. The unrelated `.github/agents/` directory remains untracked and untouched.

### Open Quality Issues

None.

## User Validation And Approval

**Owner:** User<br>
**Recorded by:** Syspilot Project Manager<br>
**Status:** accepted

Quality's `proceed` judgment verifies that the complete reviewed state is coherent and ready for validation; it does not replace the User's file-level checkpoints or final validation. The User communicates the final validation decision directly to the Project Manager.

**Decision and evidence:** The User directly accepted the complete Quality-approved Pre-Initial-Release Review on 2026-08-27 after reviewing the corrected documentation, exact 215-file collection matrix, owner dispositions, and explicit follow-up Release blockers.

## Closure

**Owner:** Syspilot Project Manager<br>
**Status:** closed

- [x] The User explicitly released this Contract before artifact work began.
- [x] Every selected release file or User-approved collection has a recorded disposition.
- [x] Every included artifact has terminal status and completion evidence.
- [x] Intent and outcome are `approved`.
- [x] Quality has recorded a `proceed` judgment.
- [x] Open Quality Issues contains `None`.
- [x] User validation is `accepted`.
- [x] Current blocker is `none`.
- [x] The observable outcome is demonstrated.
- [x] Squash integration into `development` is the Project Manager's explicit next action.
- [x] Remaining work and inputs for the later Release Contract are explicit.

**Final outcome:** The prospective v2 release surface was reviewed through explicit file and collection dispositions. Current documentation and release automation were corrected and accepted, the tracked baseline is covered 215/215, Quality recorded `proceed`, and the User accepted the result. Branching governance, MECE/Trace Skills, ontology-reference delivery, and the canonical Release Contract remain explicit High-priority follow-up Changes before the `0.10.0` Release Contract can select a candidate.
