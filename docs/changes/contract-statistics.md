# Change Contract: contract-statistics

**Status:** active<br>
**Process owner:** Project Manager<br>
**Current responsibility:** Project Manager<br>
**Current blocker:** none<br>
**Created:** 2026-11-18<br>
- **Operation Mode**: unattended

- **unattended** - the user is not reachable. When unsure, the actor flags `USER REVIEW REQUIRED` in this document, takes the simplest KISS path that is cheapest to reverse or amend, and keeps the change moving. The PM reviews flagged points once reachable again; decision ownership remains with the actor that made the decision.

## Handover log

Owned by: Project Manager

The handing-over actor appends one line as the last act before handing over, in the same commit that changes `Current responsibility`, taking `Date` as `YYYY-MM-DD` and `Time` as `HH:MM` in 24-hour local time from the system clock at that moment. The note states what the owner did and the facts that change the next owner's situation; evidence stays in the owner's section and remaining work in the open rows. The handover goes to the next actor that follows from the logical flow of the Change. The log explains transitions; the header stays authoritative.

| Date | Time | From | To | Note |
|--|--|--|--|--|
| 2026-11-18 | 00:41 | Project Manager | Architect | User released the Contract and works unattended until the next day; specify the skill and its Setup behavior, and fix the window start rule. |
| 2026-11-18 | 00:43 | Architect | Developer | Story, requirements and VCs specified with the window start rule decided; build the skill, the Setup change and the canonical closure items. |
| 2026-11-18 | 00:52 | Developer | Technical Writer | Skill, Setup job and canonical closure items built and tested; Example closure items, reader docs and a skill guide doc Need are yours; phase split is flagged for review. |
| 2026-11-18 | 01:00 | Technical Writer | Tester | Added statistics guide, reader updates and Example closure items; Architect and Developer confirmed accuracy. Strict build clean, 242 tests pass. Architect specified the phase split; PM review of its flag remains open. |
| 2026-11-18 | 01:09 | Tester | Quality | 16 acceptance tests and real-store runs pass (79 calls, 158.4 AIU reproduced); one low finding: unchecked contract name can write outside the stats folder, Developer's call. |
| 2026-11-18 | 01:10 | Quality | Developer | Review `revise`: unchecked contract name path is open for your decision; Admin and Architect rows and two log stamps are also open, see Open Quality Issues. |
| 2026-11-18 | 01:10 | Developer | Admin | Contract name is now validated as a plain file name, with a test; Infrastructure impact row is yours, then the Architect's Impact query line. |
| 2026-11-18 | 01:11 | Admin | Architect | The tracked skill is included in the source archive and the Setup inventory covers its installation; no workflow change is needed. A live Setup run remains untested. |
| 2026-11-18 | 01:12 | Architect | Quality | Impact query line filled; the plain-file-name rule is now in the specification. Architect issue in Open Quality Issues is resolved. |
| 2026-11-18 | 01:12 | Quality | Project Manager | Review `proceed`; findings resolved and results re-verified, no open quality issue. Validation is delegated to you. Open for you: the Tester and Developer handover stamps (01:12 vs 01:09, 00:55 vs 00:52) and the phase-split flag. |

## Intent And Outcome

**Status:** approved<br>
**Approval evidence:** Content agreed with the User in the Project Manager chat on 2026-11-18, including the skill name, the closure step, the window end, the Release scope, and the Setup behavior.

### Goal

Syspilot ships a skill `syspilot.contract-statistics` that records, for a finished Contract, what the actors cost and how long they ran. It takes a Contract name and is not tied to one Contract kind, so it also serves other Contracts that a customer project runs; this Change makes it part of the closure of Change and Release Contracts. At checkout the Project Manager runs it and it writes `.syspilot/stats/<contract>-stat.md`; the folder is git-ignored. Setup installs the skill and prepares the folder and its ignore entry in an installed project.

### Value

The User wants statistics of Changes: which actors took part, how many credits (AIU) they used, and how long they ran. Today this exists only as a query against the local Copilot session store that has to be rebuilt by hand. A shipped skill makes the figures comparable from Change to Change, so cost and effort can be discussed with evidence.

### Scope

- **Specification:** a User Story, the Requirements and Verification Criteria for the skill, the record, and the Setup behavior.
- **Skill:** `.github/skills/syspilot.contract-statistics/` with `SKILL.md` and `scripts/contract_stats.py`. The name carries the `syspilot.` prefix of the other shipped skills. An unversioned prototype by the Project Manager exists at `.local/stats-prototype/contract_stats.py` and is a starting point only; the Architect specifies the behavior and the Developer may reuse or rewrite it.
- **Record:** `.syspilot/stats/<contract>-stat.md` with a header (window and its source, commits in the window, extraction time, credit definition), a usage table per actor, an activity table per actor, an AIU split by phase, one generated summary line under each table, and the limits of the figures.
- **Usage table:** actor, calls, model time, active time, AIU, premium requests, input tokens, cached share, cache write tokens, output tokens, reasoning tokens, model with reasoning effort; plus a total row. AIU is the credit.
- **Activity table:** turns, files changed, sub-agent calls per actor; plus a total row.
- **Window:** it starts at the Contract's release. It ends when the Project Manager runs the skill at checkout, the squash-merge step, which follows validation. The Project Manager ends the Contract's statistics, not the Architect. The Architect fixes a start rule that does not depend on a commit message wording, because the prototype's rule did not find the start of `ontology-example`.
- **Release Contract:** the statistics cover the cost of running the Release Contract itself; they do not aggregate the Changes of the release.
- **Closure checklist:** an item in the closure checklist of the canonical Change and Release templates and in their Example counterparts that carry such a checklist. It is a checkout step, not an artifact or gate row, and the Contract holds no statistics evidence.
- **Setup:** installs the skill, creates `.syspilot/stats/`, and adds its entry to the project's `.gitignore`. That entry is an additive edit to an existing file; it follows the Setup rule for such edits, never overwrites, and does not duplicate an existing entry.
- **Out of scope:** per-actor commit counts (the session store holds no commit references); tool calls and tool durations (not in the local store); an aggregate over the Changes of a release; stating the statistics inside the Contract. The User may later move the record to the end of the Contract instead of `.syspilot/stats/`.
- **Crew:** Architect, Developer, Technical Writer, Tester, Quality; Admin confirms the packaging impact.

### Observable Outcome

- Running the skill for a closed Change writes the record with the tables and summary lines described above. With explicit start and end times of 2026-11-16 22:03:00Z and 22:12:00Z it reports 79 calls and 158.4 AIU, the figures the Project Manager validated against the session store.
- The skill fails explicitly when the session store or the window cannot be determined.
- A fresh Setup run installs the skill, creates the ignored `.syspilot/stats/` folder, and leaves an existing `.gitignore` entry and content unchanged.
- The closure checklists of the Change and Release templates name the statistics step.
- The strict documentation build and the test suite pass.

## Artifacts, Ownership And Process Gates

**Applicability:** Each artifact owner decides and updates its own row.<br>
**Scope change:** When the approved intent widens after a row reached a terminal status, `Intent and outcome` returns to `draft` until it is approved again, and each owner whose terminal row the wider intent may affect reassesses it: the owner sets the row back to `pending` or records in the row why its evidence still holds.<br>
**Ownership:** The `Owner` column of this table is the only statement of artifact and gate ownership in the Contract; section headings name no artifact owner.<br>
**Status:** pending

| Artifact or gate | Included | Owner | Completion evidence | Status |
|---|---|---|---|---|
| Intent and outcome | yes | Project Manager | Goal, value, scope, and observable outcome are explicit and approved | approved |
| Contract release | yes | User | User authorization to start the Change; no other actor may set this gate | approved: the User read the Contract and approved the release in the Project Manager chat on 2026-11-18 |
| Version control | yes | Project Manager | Feature branch `feature/contract-statistics`; squash-integrated into `development` at closure | active |
| Infrastructure impact | yes | Admin | Skill files are tracked and present in the HEAD source archive; Setup's recursive skill-copy and statistics-folder jobs cover installation. No workflow change is required; a live Setup run has not been performed | complete |
| Product specification and architecture decisions | yes | Architect | Affected Artifacts built from the impact query, every reported ID dispositioned; User Story, Requirements, and VCs linked and checked; the window start rule decided | approved |
| User-facing documentation | yes | Technical Writer | New guide and `doc` Need; closure, Setup and Upgrade guidance updated; affected `includes` links current. Architect and Developer confirmed e976650, factual clarifications at b91a494. Strict build clean, 242 tests pass | complete |
| Example sync | yes | Technical Writer | Change and Release Example closure items match canonical wording, folder Need includes the new closure requirement and its test inventory is synchronized. Strict build clean, 242 tests pass; Actor and Ontology examples unaffected | complete |
| Implementation and unit verification | yes | Developer | Skill, Setup change, and template checklist items are linked; the Developer wrote and ran the unit tests, and their commands and results are recorded | complete |
| Acceptance test design and results | yes | Tester | Requirement tests written and run by the Tester, with their commands and results, and the means for User validation trace to the intended outcome | complete |
| Quality review | yes | Quality | Quality reviewed the recorded commands and results and re-ran the build and tests; judgment `proceed` at 9ca80b7, no open quality issue | complete |
| User validation and approval | not applicable: the User delegated validation of the finished outcome to the Project Manager in the Project Manager chat on 2026-11-18 | User | A delegated `not applicable` status records that User validation did not occur | not applicable |
| Closure decision | yes | Project Manager | Final outcome, validation disposition, and integration state are recorded | pending |

## Architecture And Specification

**Status:** approved

### Affected Artifacts

Built with the project's impact skill. Record the query and give every reported ID one row with its disposition; add by hand the artifacts the query cannot report, such as new ones. The query output is a candidate list, not a complete scope.

Impact query: `get_need_links.py` from SYSP_REQ_CHANGE_CLOSURE, SYSP_REQ_RELEASE_CLOSURE and SYSP_REQ_SETUP_INSTALLATION; both directions; depth 1

| Artifact | Change | Rationale |
|---|---|---|
| SYSP_US_CONTRACT_STATISTICS, SYSP_AC_CONTRACT_STATISTICS_1 | added | Story and acceptance criterion for the usage record (us_contract_statistics.rst). |
| SYSP_REQ_CONTRACT_STATISTICS_SKILL, _RECORD, _CLOSURE | added | Skill and window rule, record content, closure checklist step (req_contract_statistics.rst). |
| SYSP_VC_CONTRACT_STATISTICS_SKILL_1 to _3, _RECORD_1, _CLOSURE_1 | added | Verify the three requirements. |
| SYSP_REQ_SETUP_STATISTICS, SYSP_VC_SETUP_STATISTICS_1 | added | Setup installs the skill, creates and ignores the folder. |
| SYSP_REQ_SETUP_INSTALLATION | modified | The blocker for ignored generated destinations excepts Setup's own `.syspilot/stats/`. |
| SYSP_VC_SETUP_INSTALLATION_1 to _5 | no change | Their statements hold; _4 (ignored outputs block) is read with the exception, Developer to keep it consistent in tests. |
| SYSP_REQ_SETUP, SYSP_US_SETUP | no change | Parents; capability unchanged. |
| SYSP_REQ_CHANGE_CLOSURE, SYSP_VC_CHANGE_CLOSURE_1, _2, SYSP_VC_CHANGE_INTEGRATION_1 | no change | The statistics step is a separate requirement; the integration item and closure rule stay as they are. |
| SYSP_REQ_CHANGE_CONTRACT, SYSP_US_CHANGE_CONTRACT | no change | Parents of the closure rule; unchanged. |
| SYSP_REQ_RELEASE_CLOSURE, SYSP_VC_RELEASE_CLOSURE_1, SYSP_REQ_RELEASE_CONTRACT, SYSP_US_RELEASE_CONTRACT | no change | Release closure rule unchanged; the new step is carried by SYSP_REQ_CONTRACT_STATISTICS_CLOSURE. |
| SYSP_DOC_CHANGE_CONTRACT, SYSP_DOC_EXAMPLE_CONTRACTS, SYSP_DOC_METHODOLOGY | no change | Technical Writer decides the text; the `doc` Needs should `includes` the new closure requirement and add a Need for the skill guide. |
| SYSP_DOC_GETTING_STARTED, SYSP_DOC_OPERATIONS, SYSP_DOC_PRODUCT_MODEL, SYSP_DOC_UPGRADE | no change | Candidates from the Setup query; Technical Writer decides whether the folder and skill need a mention. |
| .github/skills/syspilot.contract-statistics/ (SKILL.md, scripts/contract_stats.py) | added | Developer; prototype at .local/stats-prototype is a starting point only. |
| docs/Syspilot Contracts/change.md, release.md and Example counterparts | modified | Closure checklist item; Developer for canonical, Technical Writer for examples. |
| docs/Syspilot Contracts/setup.md | modified | Developer: install the skill, create the folder, add the ignore entry. |

### Decisions And Evidence

| Decision or check | Evidence |
|---|---|
| Window start rule: the first commit, in the Contract file's history across all branches and following renames, whose file version shows the start gate (`Contract release` in a Change, `Release start` in a Release) with status `approved`. It reads the row, never a commit message; the other options (commit wording, first handover) depend on wording or on a convention that a Contract may break. Explicit start and end override. Checked: the gate row exists as `approved` in the closed Contracts `ontology-example`, `ontology-link-obligations` and `impact-artifact-list`. | SYSP_REQ_CONTRACT_STATISTICS_SKILL, SYSP_VC_CONTRACT_STATISTICS_SKILL_1 |
| Window end: the moment the Project Manager runs the skill at checkout; no closure commit is looked up. | SYSP_REQ_CONTRACT_STATISTICS_SKILL |
| The record is one file per Contract name in `.syspilot/stats/`; the skill fails explicitly with no record for a missing store, a missing start gate without a given start, or an empty window. | SYSP_VC_CONTRACT_STATISTICS_SKILL_3 |
| Setup: the existing "ignored generated destinations block" rule is excepted for `.syspilot/stats/`, which Setup itself ignores on purpose. | SYSP_REQ_SETUP_INSTALLATION, SYSP_REQ_SETUP_STATISTICS |
| Contract name: a plain file name is now specified (rejects path separators and parent references), with the VC extended; this records the Developer's fix for the Tester's finding. The phase split (Quality's first responsibility) is specified in SYSP_REQ_CONTRACT_STATISTICS_RECORD, so that flag is answered by the specification. | SYSP_REQ_CONTRACT_STATISTICS_SKILL, _RECORD |
| Impact queries: `get_need_links.py <ID> --direction both --depth 1 --flat --no-build` from SYSP_REQ_CHANGE_CLOSURE, SYSP_REQ_RELEASE_CLOSURE and SYSP_REQ_SETUP_INSTALLATION on the freshly built model. Candidates, not complete scope. | Strict build 0 warnings; link obligations satisfied |
| USER REVIEW REQUIRED: the VC for the validated figures (79 calls, 158.4 AIU) depends on the local session store, which a unit test cannot assume; the Developer supplies a fixture store of the same shape, and the real-store check stays a manual PM check. | Open reading, cheapest reversible |

## Infrastructure Impact

**Status:** complete

| Infrastructure artifact | Impact | Required action and evidence |
|---|---|---|
| Source release packaging | The new skill and its script must accompany the release source | `git ls-files .github/skills/syspilot.contract-statistics` lists both files; `git archive --format=tar HEAD .github/skills/syspilot.contract-statistics` at 28feca4 contains both. The release workflow creates a GitHub Release from the tag and does not assemble a separate skill package; the future release itself has not yet been published |
| Setup installation inventory | Setup must install the skill and prepare an ignored statistics folder | `docs/Syspilot Contracts/setup.md` copies `.github/skills/` recursively, including supporting files, and has a statistics-folder and additive ignore-entry job. These are runbook instructions for a generated Setup script, not evidence of an executed installation; the Tester records that a pristine live Setup run was not performed |
| `.github/workflows/release.yml` | No new packaging or CI wiring is needed | The workflow checks out the source, runs the documentation build and full test discovery, and publishes the release; the new skill is included in the tracked source and its tests are in `tests/`. No workflow change |

## User-Facing Documentation

**Status:** complete

### Documentation Plan And Ownership

| Documentation surface | `doc` Need | Requirements included | Status |
|---|---|---|---|
| `docs/contract-statistics.md` | New SYSP_DOC_CONTRACT_STATISTICS, `realized_by` that path | SYSP_REQ_CONTRACT_STATISTICS_SKILL, _RECORD, _CLOSURE, SYSP_REQ_SETUP_STATISTICS | complete |
| `docs/change-contract.md` | SYSP_DOC_CHANGE_CONTRACT, `realized_by` that path | Existing links plus SYSP_REQ_CONTRACT_STATISTICS_CLOSURE | complete |
| `docs/operations.md` | SYSP_DOC_OPERATIONS, `realized_by` that path | Existing links plus SYSP_REQ_SETUP_STATISTICS and SYSP_REQ_CONTRACT_STATISTICS_CLOSURE | complete |
| `docs/upgrade.md` | SYSP_DOC_UPGRADE, `realized_by` that path | Existing links plus SYSP_REQ_CONTRACT_STATISTICS_SKILL and SYSP_REQ_SETUP_STATISTICS | complete |
| `docs/Example Contracts/` | SYSP_DOC_EXAMPLE_CONTRACTS, `realized_by: docs/Example Contracts/index.md` | Existing links plus SYSP_REQ_CONTRACT_STATISTICS_CLOSURE | complete |

Impact disposition: incoming depth-one queries from SYSP_REQ_CHANGE_CLOSURE and SYSP_REQ_SETUP_INSTALLATION confirmed the guide and Example folder, Methodology, Getting Started, Operations, Product Model and Upgrade candidates already identified by the Architect. Change Contract, Operations and Upgrade need current instructions; Methodology, Getting Started and Product Model remain accurate without adding low-level checkout detail. The new guide gives the skill an independently maintained surface and is listed in `docs/index.rst`; the portal changes only navigation. Existing Actor and Ontology examples have no changed role or schema obligation to carry.

### Consultations And Factual Reviews

| Documentation surface | Consulted artifact owner | Review question | Evidence and disposition |
|---|---|---|---|
| Statistics guide, closure and Setup explanations, Example checklist items | Architect and Developer | Are window discovery, metrics, current phase split, limits and checkout/Setup behavior accurate and understandable? | Both directly confirmed e976650 on 2026-11-18. Adopted Developer's two minor clarifications at b91a494: timestamps without an offset mean UTC, and the explicit-window example uses a neutral Contract name. Architect specified the implemented phase split at 444de28 without requesting a guide change; PM review of the existing USER REVIEW REQUIRED flag remains open |

### Changed Documentation And Verification

| Artifact | Change | Verification evidence |
|---|---|---|
| `docs/contract-statistics.md` | New guide: invocation, overrides, record fields, attribution and runtime limits, failure behavior, local ignored output | Strict clean build passes; Architect and Developer confirmed accuracy |
| `docs/change-contract.md`, `docs/operations.md`, `docs/upgrade.md` | Closure step and Setup preparation; upgrade includes the new skill and manually prepares what Setup would provide | Final strict clean build passes; Architect and Developer confirmed accuracy |
| `docs/syspilot/documentation/index.rst`, `docs/index.rst` | New guide `doc` Need and navigation; affected existing Needs include the new requirements | Final strict clean build passes with zero warnings |
| `tests/test_acceptance_setup_examples.py` | Existing exact documentation-inventory expectation gains SYSP_REQ_CONTRACT_STATISTICS_CLOSURE because the Example folder now carries that obligation | Initial targeted run failed on the newly required `includes` link; after the fixture update, `uv run python -m unittest tests.test_contract_statistics tests.test_acceptance_setup_examples`: 38 tests pass |

Final verification (2026-11-18): `uv run python docs\docs-build.py clean` succeeds with zero warnings; `uv run python -m unittest discover -s tests` passes all 242 tests; `git diff --check` passes. No statistics command was run against the local session store as part of this documentation work.

After the two factual guide clarifications and the Architect's 444de28 phase specification, `uv run python docs\docs-build.py` passes with zero warnings at b91a494. The earlier full-suite result applies to unchanged executable code and the synchronized documentation-inventory expectation.

## Example Sync

**Status:** complete

| Artifact | Change | Verification evidence |
|---|---|---|
| `docs/Example Contracts/change.md`, `docs/Example Contracts/release.md` | Same statistics checklist item as the canonical templates; no new artifact row or statistics field | 38 targeted statistics/Setup-example tests pass; strict clean build passes |
| `docs/Example Actors/`, `docs/Example Ontology/` | No change: the added checkout step changes neither public role cards nor ontology definitions | Scope and canonical artifact review; Architect confirmed fidelity of the documentation and examples |

## Implementation And Unit Verification

**Status:** complete

### Decisions And Evidence

Record implementation decisions that remain relevant to understanding or maintaining the outcome. The evidence explains why the chosen approach fits better than the relevant alternatives.

| Decision | Chosen approach | Relevant alternatives | Rationale and evidence |
|---|---|---|---|
| Phase split of the AIU table (the spec names none) | Split at the first commit of the Contract file whose header shows `Current responsibility: Quality`: "before" and "from first handover to Quality"; one phase "Whole window" with an explicit `--start` or when Quality never held it. | Split per actor; split at the first handover of any kind. | Quality's first receipt is the one handover every Change has and it separates building from review; it reads the header, not a message. Documented in SKILL.md and in the record's Limits. USER REVIEW REQUIRED: the Architect or PM may prefer another split. |
| Reading older versions after a move | `git log --all --follow --name-only` gives the path at each commit; the version is read with `git show <sha>:<path-then>`. | Read only the current path. | A moved Contract must still find its gate. Test `test_start_is_first_commit_with_gate_approved_even_after_move`. |
| Setup and the ignore rule | New job row `Statistics folder`; step 9 excepts `.syspilot/stats/`; the entry is added only if no rule already ignores the folder. | A separate step outside the inventory. | The inventory is the only installation statement; the skill itself is already installed by the existing "Syspilot skills" job. |
| Contract name argument | The name must match a plain file-name pattern (letters, digits, `.`, `_`, `-`; no `..`, no separators); otherwise the skill fails before any read or write. | Resolve the path and check it stays inside `.syspilot/stats/`; accept the risk. | The name is only a file stem, so a pattern is simpler than path checks and closes the Tester finding. Test `test_contract_name_that_is_not_a_plain_file_name_is_rejected`: 26 statistics tests OK. |
| Unit test of the validated figures | Fixture store of the same schema, 5 calls of 2 AIU give 10.0 AIU; the 79 calls and 158.4 AIU stay a manual check on the real store. | Reading the real store in a test. | A test cannot assume the local store. |

### Changed Artifacts And Verification

| Artifact | Change | Verification evidence |
|---|---|---|
| `.github/skills/syspilot.contract-statistics/scripts/contract_stats.py`, `SKILL.md` | added; the prototype's commit-message start rule is replaced by the gate row rule; explicit failure for a missing store, a missing gate without `--start`, and an empty window | `python -m unittest tests.test_contract_statistics`: 9 tests OK. Manual run on the real store with `--start 2026-11-16T22:03:00Z --end 2026-11-16T22:12:00Z`: 79 calls, 158.4 AIU. Manual run for `impact-artifact-list` found its start from the gate (commit e51ef0e) and split the phases. |
| `tests/test_contract_statistics.py` | added: gate start incl. a file move, release gate and phase marker, explicit times, record parts, three failures without a record, Setup and closure text | the same 9 tests; full suite 242 tests, all OK except one that failed only because my manual runs had left `.syspilot/`; after removing it `tests.test_acceptance_ontology_example` passes (31 tests) |
| `docs/Syspilot Contracts/setup.md` | `Statistics folder` job row; ignore exception in step 9 | text tests above; strict `python docs/docs-build.py clean`: OK, no warnings |
| `docs/Syspilot Contracts/change.md`, `release.md` | closure checklist item for the statistics skill | text test above; strict docs build OK |

## Acceptance Testing

**Status:** complete

Run: `python -m unittest tests.test_acceptance_contract_statistics` (16 tests, black box through the skill's command line with temporary git repos and fixture stores). Every assertion was mutation-checked against a changed skill; the surviving mutant (`end <= start` guard removed) is equivalent, because an empty window already fails.

| Scenario | Traces to | Result | Evidence |
|---|---|---|---|
| Start comes from the approved gate, not commit wording, and survives a file move; release gate starts a release window; a pending gate gives no start | SYSP_REQ_CONTRACT_STATISTICS_SKILL_1 | pass | StartGateTests (3) |
| Explicit window: totals and AIU, other repos excluded, bounds limit calls, activity counts only in-window turns/files, offset-less timestamps are UTC | SYSP_REQ_CONTRACT_STATISTICS_SKILL_2 | pass | FigureTests (4) |
| Real session store, window 2026-11-16 22:03:00Z to 22:12:00Z of `ontology-example`: 79 calls, 158.4 AIU, 5 actors | SYSP_REQ_CONTRACT_STATISTICS_SKILL_2 | pass | manual run by the Tester; the real store has the same table columns as the fixture |
| Missing store, missing gate without `--start`, empty window, end before start: non-zero exit, cause named, no record | SYSP_REQ_CONTRACT_STATISTICS_SKILL_3 | pass | FailureTests (4) |
| Record parts, phase split at the first Quality commit, one phase otherwise | SYSP_REQ_CONTRACT_STATISTICS_RECORD_1 | pass | RecordTests (3) |
| Real Contracts from the gate: ontology-example, impact-artifact-list, ontology-link-obligations, contract-statistics | SYSP_REQ_CONTRACT_STATISTICS_RECORD_1 | pass | manual run; split 18/82, 13/87, 21/79 and one phase for this Contract |
| Setup statistics folder job and its ignore condition; closure item in the canonical and Example Change/Release templates | SYSP_REQ_SETUP_STATISTICS_1, SYSP_REQ_CONTRACT_STATISTICS_CLOSURE_1 | pass | DocumentationTests (2) |

Suite 258 tests: the one failure came from my manual runs leaving `.syspilot/`, as the Developer noted; after removing it the affected tests pass. Strict build `python docs/docs-build.py clean` clean.

**Finding (no requirement covers it; Developer decides):** the Contract name argument is joined into the record path unchecked, so `../../x` writes `x-stat.md` outside `.syspilot/stats/`. The argument is typed by the user on the local machine, so I rate it low; I did not add a failing test.

**Untested:** a live Setup run on a pristine target (the Setup rows are checked as text only); the phase split choice stays with the PM review flag; sub-agent call counts were 0 in every real window, so that column is checked only by the fixture.

## Quality Review

**Status:** complete

**Current judgment:** `proceed` at 9ca80b7. The four earlier findings are resolved: plain-file-name rule in the specification, code and test; Infrastructure impact recorded by Admin; `Impact query` line filled; skill, Setup rows, templates, guide and tests agree. Re-run by Quality: strict build clean, 55 statistics and Setup-example tests OK.

### Applied Review Methods

| Method | Selected scope | Evidence | Findings | Limits |
|---|---|---|---|---|
| Recorded-result review | Diff 1c58831..644c09e, the Contract rows, the acceptance table and finding | Re-ran `python docs/docs-build.py clean` (success) and `python -m unittest tests.test_acceptance_contract_statistics tests.test_contract_statistics` (25 OK); read the Contract against the gate table and the template | four findings at 644c09e, all resolved at 9ca80b7 (name rule: regex plus `..` check, test with six bad names asserting no file written; Admin and Architect rows read) | Full suite (258) taken from the Tester's record; a live Setup run was not performed (Admin and Tester record this) |
| MECE and Trace (`syspilot.mece` same-document, `syspilot.trace` both depth 2) | SYSP_REQ_CONTRACT_STATISTICS_SKILL | Script findings none; the plain-name sentence adds a name rule beside window and failure rules without contradicting RECORD or CLOSURE; no unresolved target | no finding | `semantic-content-review-required` and `structured-coverage-data-unavailable` remain |

Verification is fully automated. Quality reviews the commands and results that the Developer and the Tester recorded, and executes a check itself only when a recorded result cannot support its judgment, recording the reason in the table above. A Markdown process artifact whose content has no automated check is verified by Quality's review, and the table above records that review and its limits.

Quality communicates its `proceed` judgment and supporting evidence directly to the Project Manager before the Project Manager presents the verified outcome for validation. Another actor's forwarded claim does not establish Quality's decision.

### Open Quality Issues

Keep this table synchronized with currently open issues. A missing automation is an open issue whose row names the task that closes it, the owner of that task, and the completion evidence. For each issue, Quality transfers current responsibility to the owner of the affected artifact. When Quality confirms the required outcome, update the affected artifact or evidence and remove the resolved row. At closure this table contains `None`.

| Artifact | Current issue | Required outcome |
|---|---|---|
| None | None | None |

## User Validation And Approval

**Recorded by:** Project Manager<br>
**Status:** not applicable

Quality's `proceed` judgment verifies that the change is ready for validation; it does not validate user value. The User delegated validation of this Change's finished outcome to the Project Manager (artifact row). The Project Manager reviews the verified outcome and records the decision here; User validation did not occur.

**Decision and evidence:** Explicit User delegation from the artifact row; User validation did not occur. The Project Manager validated the outcome against the Observable Outcome on 2026-11-18 at 8e8e4c0: the skill run on the real store for 2026-11-16 22:03:00Z to 22:12:00Z gives 79 calls, 5 actors and 158.4 AIU with the three summary lines; a Contract name `../../x` is rejected with exit 1 and no record; the record is ignored by `.gitignore` (`.syspilot/`); the Change and Release templates carry the checkout item; Setup has the `Statistics folder` job with an additive ignore entry; 26 statistics tests pass. Accepted limits: no live Setup run was performed, and the sub-agent column is verified by fixture only.

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
