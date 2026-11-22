# Change Contract: setup-lookup-by-tags

**Status:** closed<br>
**Process owner:** Project Manager<br>
**Current responsibility:** Project Manager<br>
**Current blocker:** none<br>
**Created:** 2026-11-22<br>
- **Operation Mode**: autonomous, agreed with the User on 2026-11-22.

- **autonomous** - every actor decides on its own; when genuinely unsure, it asks the user directly and pauses only its own step until answered.

## Handover log

Owned by: Project Manager

The handing-over actor appends one line as the last act before handing over, in the same commit that changes `Current responsibility`, taking `Date` as `YYYY-MM-DD` and `Time` as `HH:MM` in 24-hour local time from the system clock at that moment. The note states what the owner did and the facts that change the next owner's situation; evidence stays in the owner's section and remaining work in the open rows. The handover goes to the next actor that follows from the logical flow of the Change. The log explains transitions; the header stays authoritative.

| Date | Time | From | To | Note |
|--|--|--|--|--|
| 2026-11-22 | 15:23 | Project Manager | Architect | Contract released by the User in autonomous mode; the Setup prompt looks up version tags instead of Release pages. |
| 2026-11-22 | 15:26 | Architect | Technical Writer | Tag-based bootstrap selection and document links are specified and checked; both current prompts still request releases and need realization. |
| 2026-11-22 | 15:28 | Technical Writer | Developer | Both prompts now request version tags; factual review, strict build and focused checks pass. Setup process and test assessment remain open. |
| 2026-11-22 | 15:34 | Developer | Quality | `setup.md` needs no change (it states no lookup); added a 3-test pin of the two identical tag prompts; strict build and 271 tests pass. Yours: review. |
| 2026-11-22 | 15:36 | Quality | User | Both prompts and the focused specification agree on tag lookup; verification reviewed, no open issue, ready for validation. |
| 2026-11-22 | 15:39 | User | Project Manager | The User accepted the outcome; closure recorded. |

## Intent And Outcome

**Status:** approved<br>
**Approval evidence:** The User decided the intent on 2026-11-22 ("das können wir ja auch bei syspilot auf github so umstellen das das setup nach release tags sucht und nicht nach releases") and released the Contract the same day.

### Goal

The Setup prompt in the README and in the getting-started guide asks the session to look up the version tags of the Syspilot repository, not its releases. Setup needs only a tag and its commit, so the same prompt works for any copy of the repository that carries the tags, including one without GitHub Release pages.

### Value

Setup pins `release_tag` and `commit_sha`; a GitHub Release page adds nothing to that. A prompt that depends on Release pages fails for a copy of the repository that has tags only, and every such copy would otherwise need its own variant of the prompt.

### Scope

- Step 1 of the Setup prompt in `README.md` and `docs/getting-started.md` says "version tags" instead of "releases", with identical wording in both files.
- Where `docs/Syspilot Contracts/setup.md`, a requirement, or a guide describes how the version is looked up, it names tags. The Architect lists those places; text that already speaks of the tag stays.
- Unchanged: the repository address in the prompt and in `source_repository`, the `project.toml` keys `release_tag` and `commit_sha`, the Release Process, the release workflow and the GitHub Release page it creates.
- Crew: Architect, Technical Writer, Quality; the Developer owns `setup.md` and tests if they need the wording.

### Observable Outcome

Both prompts carry the same tag wording, no document describes a Release page as the source of the version to install, and the documentation builds strictly clean with the test suite passing.

## Artifacts, Ownership And Process Gates

**Applicability:** Each artifact owner decides and updates its own row.<br>
**Scope change:** When the approved intent widens after a row reached a terminal status, `Intent and outcome` returns to `draft` until it is approved again, and each owner whose terminal row the wider intent may affect reassesses it: the owner sets the row back to `pending` or records in the row why its evidence still holds.<br>
**Ownership:** The `Owner` column of this table is the only statement of artifact and gate ownership in the Contract; section headings name no artifact owner.<br>
**Status:** pending

Crew by User decision of 2026-11-22: Architect, Technical Writer, Quality; the Developer owns the Markdown process artifact `setup.md` and tests where they need the wording. This Change runs in parallel to another Change on the Release Process and must not touch it.

| Artifact or gate | Included | Owner | Completion evidence | Status |
|---|---|---|---|---|
| Intent and outcome | yes | Project Manager | Goal, value, scope, and observable outcome are explicit and approved | approved |
| Contract release | yes | User | User released the Contract on 2026-11-22 | approved |
| Version control | yes | Project Manager | Feature branch `feature/setup-lookup-by-tags`; squash-integrated into `development` at closure | merged |
| Infrastructure impact | not applicable: no workflow, CI or packaging artifact changes | Admin | Affected workflow, CI, and packaging artifacts are updated, confirmed by their current owner rather than inferred from a Needs-only impact query | not applicable |
| Product specification and architecture decisions | yes | Architect | `bf28eff` adds the tag-lookup Requirement and two VCs; both prompt documents link to it. Strict build, four build-runner tests, ten focused Setup checks and five Impact starts pass; prompt realization remains open | complete |
| User-facing documentation | yes | Technical Writer | Identical version-tag prompts and adjacent prose updated; Architect factual review clear, strict build, prompt assertions and 14 focused tests pass | complete |
| Example sync | not applicable: the repository-specific Setup prompt is not installed as an example; no general-project behavior changes | Technical Writer | Changes of this Change that also hold for a general project are carried into the examples | not applicable |
| Implementation and unit verification | yes | Developer | `setup.md` and tests carry the tag wording where they state the lookup, or the row records that none do; commands and results recorded | complete |
| Acceptance test design and results | not applicable: Quality reviews the artifacts directly | Tester | Requirement tests written and run by the Tester, with their commands and results, and the means for User validation trace to the intended outcome | not applicable |
| Quality review | yes | Quality | Proceed at `14508a8`; complete scoped diff, prompt invariants, test pin, peer/relationship content and recorded green verification reviewed | complete |
| User validation and approval | yes | User | The User accepted the outcome on 2026-11-22 | accepted |
| Closure decision | yes | Project Manager | Final outcome, validation disposition, and integration state are recorded | complete |

## Architecture And Specification

**Status:** complete

### Affected Artifacts

| Artifact | Change | Rationale |
|---|---|---|
| `docs/syspilot/requirements/req_setup.rst` | Add `SYSP_REQ_SETUP_BOOTSTRAP` and focused VCs for tag lookup and identical selected-tag prompts | The existing `SYSP_REQ_SETUP_SOURCE` starts with a supplied tag and verified commit; bootstrap lookup is an independent earlier user-facing obligation |
| `docs/syspilot/documentation/index.rst` | Add the bootstrap Requirement to `SYSP_DOC_README` and `SYSP_DOC_GETTING_STARTED` | Both independently maintained surfaces carry the prompt; existing links for the supplied tag and Setup remain |
| `README.md`; `docs/getting-started.md` | Technical Writer changes identical prompt step 1 from releases to version tags and checks adjacent explanations | These are the only active product documents found that direct lookup of releases; retain repository URL and subsequent steps |
| `docs/Syspilot Contracts/setup.md` | Developer assesses current text and records whether it needs a wording change | Phase 1 already receives a release tag, verifies its full commit and uses that tree; no Release-page lookup is stated there |
| Tests | Developer assesses wording assertions and required verification | Prompt and document consistency must be checked without modifying unrelated Release Process tests |

### Decisions And Evidence

| Decision or check | Evidence |
|---|---|
| Scope and unchanged behavior | The tag lookup replaces Release-page lookup only. Keep the existing repository address, User selection, exact-tag Contract fetch, `source_repository`, `release_tag`, `commit_sha`, Release Process and workflow. No tag-ordering algorithm or new fallback is specified |
| Source inspection | README and Getting Started have identical prompt step 1, “Look up the releases”; no other active requirement, Setup Process or guide found instructs a Release-page lookup. Setup Process Phase 1 verifies the supplied tag and commit and does not discover releases |
| Related guide disposition | The documentation portal and Operations describe a selected release/Contract, not a Release page as its lookup source; Branching and Methodology describe broader process and authority, not this lookup. Retain their meaning; Technical Writer assesses adjacent prose in the two edited prompts |
| Impact and documentation ownership | Fresh baseline both-direction depth-1 Impact queries from `SYSP_REQ_SETUP_SOURCE`, `SYSP_DOC_README` and `SYSP_DOC_GETTING_STARTED` expose the Setup story, related VCs and linked guides. The new specific bootstrap topic is linked to both prompt `doc` Needs; no other existing surface contains the prompt |
| Verification at `bf28eff6d2bd73925e95db67f83c890a23c917b4` | Isolated `python docs\docs-build.py clean` succeeded with zero warnings; `python docs\test_docs_build.py -v` passed four tests. From `tests\`, `python -m unittest -v test_acceptance_setup_examples.DocNeedTests test_acceptance_setup_feedback_2.ContractTextCrossChecks` passed ten tests |
| Fresh traceability | Both-direction depth-1 Impact queries pass for the new REQ, both new VCs and the two prompt `doc` Needs; the exported links confirm specialization of `SYSP_REQ_SETUP_SOURCE`, both VC targets and both incoming document links |
| Evidence and limits | Retained under `C:\Users\DOE4SI\.copilot\session-state\334ed166-2820-4c7b-bf2b-648112d9fa4c\files\`: `setup-lookup-by-tags-spec-build.log`, `setup-lookup-by-tags-spec-tests.log`, `setup-lookup-by-tags-spec-impact.json` and `setup-lookup-by-tags-spec-needs\`. The clean detached validation worktree was removed. The current prompt blocks are still identical but still say “releases”; these checks do not claim the new VCs pass before Technical Writer's realization |

## User-Facing Documentation

**Status:** complete

### Documentation Plan And Ownership

| Documentation surface | `doc` Need | Requirements included | Status |
|---|---|---|---|
| `README.md`, `docs/getting-started.md` | `SYSP_DOC_README`, `SYSP_DOC_GETTING_STARTED` | Both include `SYSP_REQ_SETUP_BOOTSTRAP` and `SYSP_REQ_SETUP_SOURCE`; replace the identical lookup step and describe the selected tag in adjacent prose | complete |
| Portal, Operations, Branching, Methodology and other guides | Existing `doc` Needs | They describe a selected release or the publication process, not a Release page as the Setup lookup source | reassessed; no change needed |

Impact query `SYSP_REQ_SETUP_BOOTSTRAP --direction both --depth 1 --flat --no-build` against the fresh isolated documentation export returned the README and Getting Started Needs, the Setup source Requirement, story and both bootstrap VCs. The default build's stale data and the Architect's recorded export path did not contain the new Need in this workspace; neither failed lookup was treated as evidence. The new isolated build supplied usable data.

### Consultations And Factual Reviews

| Documentation surface | Consulted artifact owner | Review question | Evidence and disposition |
|---|---|---|---|
| README and Getting Started | Architect | Do the identical prompts and adjacent explanations implement `SYSP_REQ_SETUP_BOOTSTRAP` without changing the source or later steps? | Direct factual review of `72c82ad`: no findings; both prompts select from version tags, request the latest and User choice, fetch the exact-tag Contract, preserve steps 2–4 and the repository address, and retain the `doc` Need links. This is not runtime proof or a Quality judgment |

### Changed Documentation And Verification

| Artifact | Change | Verification evidence |
|---|---|---|
| README and Getting Started | Identical prompt step 1 now looks up repository version tags, presents the latest and asks the User's choice; adjacent prose refers to the selected tag | Direct assertions pass: both full prompts are identical, and relative to `66bbdb5` each changes only step 1; repository address, exact-tag fetch, remaining steps and User selection remain unchanged. Architect's factual review has no findings. The rendered Getting Started page contains the new prompt. Ten targeted Setup/map tests and four build-runner tests pass; isolated strict Sphinx build passes with zero warnings |
| Example Actors, Example Contracts and Example Ontology | No change: the repository-specific bootstrap prompt is not an adopter example and none of these folders contains its lookup instruction | Direct search of all three example folders found no Setup bootstrap lookup |

Verification: `python -m unittest tests.test_acceptance_setup_examples.DocNeedTests tests.test_acceptance_setup_feedback_2.ContractTextCrossChecks` (10 pass); `python docs/test_docs_build.py -v` (4 pass); `uv run sphinx-build -E -a -b html -W --keep-going docs {isolated session output}` (zero warnings). An active-document search found no instruction to look up releases; the only Release-page mentions found are the new Requirement and VC explicitly stating it is not required. These checks do not establish an actual tag lookup or installation; Developer owns the remaining process/test assessment and full-suite evidence.

## Implementation And Unit Verification

**Status:** complete

### Decisions And Evidence

| Decision | Chosen approach | Relevant alternatives | Rationale and evidence |
|---|---|---|---|
| `setup.md` | No change | Adding a tag-lookup sentence | Phase 1 receives a tag and verifies its full commit; a grep of `setup.md` for releases, release page, latest release and lookup finds nothing, so it states no lookup to reword. The lookup lives only in the two prompts, which the Requirement covers |
| Tests | New `tests/test_setup_bootstrap_prompt.py` (3 tests): the README and Getting Started prompts are identical; step 1 looks up the version tags of the repository and does not say releases; step 2 fetches the Contract from that exact tag | Leaving the Technical Writer's one-time direct assertions uncommitted | The two prompts are maintained separately and the Requirement demands identical selected-tag prompts, so a later edit of one would otherwise go unnoticed; the pin reads only the two prompts and no Release Process file |

### Changed Artifacts And Verification

| Artifact | Change | Verification evidence |
|---|---|---|
| `tests/test_setup_bootstrap_prompt.py` | As above | `uv run python -m unittest tests.test_setup_bootstrap_prompt`: 3 OK; mutation: README step 1 set back to "Look up the releases" makes 2 tests fail, restored with `git checkout`. Strict `uv run python docs/docs-build.py` built successfully; `uv run python -m unittest discover -s tests`: 271 tests OK (2026-11-22 15:34). Not run: an actual tag lookup or installation; the `clean` build variant |

## Quality Review

**Status:** complete

**Current judgment:** proceed at `14508a8`.

Both complete prompts are identical, ask for version tags/latest/User choice,
and retain the repository address, exact selected-tag fetch and steps 2-4.
The adjacent explanations agree. The new Requirement and two short VCs
distinguish bootstrap lookup from Setup's already-supplied source identity.
Both documentation Needs retain their prior links and include the new topic.
`setup.md` already receives and verifies a tag; no lookup change is needed.
The three new tests pin prompt equality, tag wording and exact-tag fetch
without touching the Release Process or other tests.

An independent tracked-source scan found no active instruction to use Release
pages for Setup. The old release-fetch mention in dated release notes is
historical provenance, not an installation instruction. Release publication,
workflow and baseline keys are unchanged. This review verifies the requested
wording and its consistency, not a live tag lookup or end-to-end installation.

### Applied Review Methods

| Method | Selected scope | Evidence | Findings | Limits |
|---|---|---|---|---|
| Scoped content and recorded verification | Complete `18464b0..14508a8` product diff; both full prompts and adjacent prose; Setup source phase; active tracked-document scan | Independent prompt comparison confirms equality, latest/User choice and unchanged subsequent steps. Reviewed specification strict-clean build/test logs, Technical Writer's factual review and fresh strict-build results, Developer's recorded three-test pin/mutation and 271 passing tests. `git diff --check` passes; current rendered Getting Started contains the tag prompt | No discrepancy; all requested wording surfaces agree | Quality did not rerun build/suites because recorded checks and direct source/rendered assessment support this bounded change. No live lookup or installation claimed; tag ordering/fallback behavior is not newly specified |
| MECE horizontal coverage | Five impacted Needs: bootstrap REQ, both VCs, README and Getting Started docs; same-document complete same-type peers | Five successful queries: 21 REQ peers, 60 peers per VC and 15 peers per doc; exact sets in analysis below. All 106 distinct peer/neighborhood objects' content read | Bootstrap discovery is distinct from supplied-tag verification; two VC topics and the two documentation surfaces have consistent boundaries. No new duplication, contradiction or coverage finding | Structured coverage data is unavailable; script findings are not semantic clearance. This review does not certify unrelated baseline obligations or all-type coverage |
| Trace relationship analysis | Same five starts, both directions, depth 1; exact union 31 Needs, 34 distinct resolved named edges | Five Trace and five Impact queries; all resolved neighbor content read, including untouched links. Current export contains the new REQ/VCs and both document links; exported bootstrap content matches source | No unresolved target or inconsistent source/story/verification/documentation boundary identified | Depth 1 does not establish deeper graph completeness or link requiredness; content reading supplies the bounded semantic judgment |

Quality used the available fresh `docs\_build\html\needs_id` export, created
2026-11-22 15:30, rather than assuming earlier missing exports were usable.
Exact peer sets, neighborhoods and edges are retained in
`C:\Users\DOE4SI\.copilot\session-state\31d89b9f-bcdb-4323-9a89-60ceae73d649\files\setup-tags-quality-analysis.json`.
The local rendered Getting Started page was inspected for the new tag wording;
this is separate from the owners' recorded successful Sphinx builds.

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

**Decision and evidence:** The User accepted the outcome directly to the Project Manager on 2026-11-22 after the presentation of Quality's `proceed` at bd320d6. The presentation named the change: both Setup prompts say "version tags" with identical wording, the specification and its documentation map agree, and one test pins the two prompts. No live lookup or installation was run.

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

**Final outcome:** The Setup prompt in `README.md` and `docs/getting-started.md` asks the session to look up the version tags of the Syspilot repository, with identical wording; the specification and its documentation map agree and a test pins the two prompts. The User accepted on 2026-11-22. Integrated by squash into `development` from `feature/setup-lookup-by-tags` as `aef34b0`, not pushed.
