# Change Contract: model-recommendation

**Status:** active<br>
**Process owner:** Project Manager<br>
**Current responsibility:** Project Manager<br>
**Current blocker:** none<br>
**Created:** 2026-11-20<br>
- **Operation Mode**: autonomous, agreed with the User on 2026-11-20; the User reviews the document itself directly with the Technical Writer.

- **autonomous** - every actor decides on its own; when genuinely unsure, it asks the user directly and pauses only its own step until answered.

## Handover log

Owned by: Project Manager

The handing-over actor appends one line as the last act before handing over, in the same commit that changes `Current responsibility`, taking `Date` as `YYYY-MM-DD` and `Time` as `HH:MM` in 24-hour local time from the system clock at that moment. The note states what the owner did and the facts that change the next owner's situation; evidence stays in the owner's section and remaining work in the open rows. The handover goes to the next actor that follows from the logical flow of the Change. The log explains transitions; the header stays authoritative.

| Date | Time | From | To | Note |
|--|--|--|--|--|
| 2026-11-20 | 04:31 | Project Manager | Architect | Contract released by the User in autonomous mode. Open for you: the Affected Artifacts query, the ownership entry in the requirements with its pointer to the document, and the location of the document in the documentation. The Technical Writer follows with the document, which the User reviews directly with it. |
| 2026-11-20 | 04:33 | Architect | Technical Writer | Ownership is in `SYSP_REQ_TECHNICAL_WRITER` and `SYSP_REQ_ADMIN`; no further requirement. Location `docs/model-recommendation.md` with a User Guides toctree entry and a new `doc` Need are yours. The Admin row is still open. |
| 2026-11-20 | 04:57 | Technical Writer | Developer | User accepted `docs/model-considerations.md` at `a43e0bd`; `SYSP_DOC_MODEL_RECOMMENDATION`, role cards, and Example sync are complete, and post-Setup `docs/getting-started.md` alignment stays open on the documentation row. Note the guide path was renamed from `docs/model-recommendation.md` to `docs/model-considerations.md`. |
| 2026-11-20 | 05:00 | Developer | Technical Writer | Setup change done in docs/Syspilot Contracts/setup.md; build and setup tests pass. The guide's link to the Setup Contract breaks in a target build, see the open item in my section; Getting Started alignment is yours. |
| 2026-11-20 | 05:04 | Technical Writer | Admin | Replaced the Syspilot-only relative link in `docs/model-considerations.md`, aligned `docs/getting-started.md` with `setup.md`, and verified Syspilot's strict build, 80 Setup/Example tests, and a pristine target `-W` build with `model-considerations` adopted. Documentation is complete; `Infrastructure impact` is yours before `Quality`. |
| 2026-11-20 | 05:07 | Admin | Quality | The guide is tracked in the source archive, referenced by Setup and included in the documentation build; no release workflow change is needed. |
| 2026-11-20 | 05:10 | Quality | Developer | Verdict revise: two Developer-owned issues, see Open Quality Issues. |
| 2026-11-20 | 05:11 | Quality | User | Verdict proceed; both issues resolved and re-checked. Validation is the User's. |
| 2026-11-20 | 05:10 | Developer | Quality | Stale note marked resolved and my earlier log stamp corrected to the commit time 05:00. |
| 2026-11-20 | 12:44 | User | Project Manager | The User validated the outcome ("validation passed"); closure follows. |

## Intent And Outcome

**Status:** approved<br>
**Approval evidence:** On 2026-11-20 the User described the document, its ownership, its monthly refresh and the Setup step in chat, said "ja mach das" to starting the Change, wants it in Release 0.11.0, and set autonomous mode with the document review held directly with the Technical Writer.

### Goal

Syspilot ships one dated document that recommends a Copilot model per Syspilot actor, with the reasons and the steps to refresh it. The Technical Writer owns it and refreshes it monthly; a refresh that changes a recommendation is agreed with the User, and the Admin then changes the `model:` lines of the agent files. Setup asks the User whether to adopt the recommendation; on yes it places the document in the project's documentation and sends the Technical Writer the task to run steps 1 to 3 of the document and to set a monthly heartbeat.

### Value

Model choice per role drives cost and speed, and today every project decides it from scratch. The document gives the reasons (for example Quality on a different model family than the actors it reviews, and cost computed from the observed cache share) and a way to renew the numbers when prices change. One document with one owner, as the Contracts have, avoids a second place that goes stale.

### Scope

- A new user-documentation document, written by the Technical Writer from the Jarvis Project Manager's analysis `C:\workspace\actor-context\jarvis\Project Manager\memory\copilot-models.md`, read only, and generalized so that it holds no content specific to that project. It carries its date, the refresh steps 1 to 3, the fallback when the data source cannot be read, and the ownership rule above.
- The specification holds one ownership entry and a pointer to the document; the document itself is not specified further (User decision of 2026-11-20).
- `docs/Syspilot Contracts/setup.md`: the question to the User, the placement of the document in the project's documentation, and the message to the Technical Writer.

### Observable Outcome

- The document exists in the Syspilot documentation, is dated, names its owner and the Admin's part, and contains no content specific to the Jarvis project.
- The requirement set names the document's ownership and points to it.
- Setup describes the question, the placement and the message to the Technical Writer, and changes nothing without the User's yes.
- The strict documentation build and the test suite pass.

## Artifacts, Ownership And Process Gates

**Applicability:** Each artifact owner decides and updates its own row.<br>
**Scope change:** When the approved intent widens after a row reached a terminal status, `Intent and outcome` returns to `draft` until it is approved again, and each owner whose terminal row the wider intent may affect reassesses it: the owner sets the row back to `pending` or records in the row why its evidence still holds.<br>
**Ownership:** The `Owner` column of this table is the only statement of artifact and gate ownership in the Contract; section headings name no artifact owner.<br>
**Status:** pending

Order of work: Architect (ownership entry, location of the document), Technical Writer (document, reviewed by the User directly), Developer (`setup.md`), Quality.

| Artifact or gate | Included | Owner | Completion evidence | Status |
|---|---|---|---|---|
| Intent and outcome | yes | Project Manager | Goal, value, scope, and observable outcome are explicit and approved | approved |
| Contract release | yes | User | The User released the Contract in chat on 2026-11-20 at 04:31 ("ok proceed") and confirmed in a follow-up question that the Project Manager may record it; the Project Manager set the gate on that instruction | approved |
| Version control | yes | Project Manager | Feature branch `feature/model-recommendation`; squash-integrated into `development` at closure | active |
| Infrastructure impact | yes | Admin | The guide is tracked in the current source archive, Setup selects it from the verified release commit, and the documentation build includes it; evidence and release limitations are recorded below | complete |
| Product specification and architecture decisions | yes | Architect | Changed specification and architecture artifacts are linked and checked; Affected Artifacts built from the impact query, every reported ID dispositioned | approved |
| User-facing documentation | yes | Technical Writer | `docs/model-considerations.md` accepted directly by the User on 2026-11-20 (`a43e0bd`) and target-link-clean; `docs/getting-started.md` aligned with `setup.md`; `doc` Needs and `includes` links current; Syspilot strict build, 80 Setup/Example tests, and pristine target `-W` build pass | complete |
| Example sync | yes | Technical Writer | Optional adoption carried into the Example Technical Writer card; Admin card matches; deviation declared; 29 Example tests and strict build pass | complete |
| Implementation and unit verification | yes | Developer | `docs/Syspilot Contracts/setup.md` changed; commands and results recorded | complete |
| Acceptance test design and results | not applicable: Quality reviews the Markdown process artifacts and the requirement directly | Tester | Requirement tests written and run by the Tester, with their commands and results, and the means for User validation trace to the intended outcome | not applicable |
| Quality review | yes | Quality | Quality reviewed the recorded commands and results; current verification judgment is `proceed` and no open quality issue remains | complete |
| User validation and approval | yes | User | The User validated the outcome in chat on 2026-11-20 at 12:43 ("validation passed") | accepted |
| Closure decision | yes | Project Manager | Final outcome, validation disposition, and integration state are recorded | pending |

## Architecture And Specification

**Status:** approved

### Affected Artifacts

Impact queries: `SYSP_REQ_TECHNICAL_WRITER` and `SYSP_REQ_ADMIN`; both directions; depth 1, run with `get_need_links.py ... --flat --no-build`. The document itself is not specified (User decision of 2026-11-20), so no requirement is added for it or for Setup.

| Artifact | Change | Rationale |
|---|---|---|
| `SYSP_REQ_TECHNICAL_WRITER` | modified | One ownership bullet: the Technical Writer owns `docs/model-recommendation.md`, refreshes it monthly, agrees changed recommendations with the User, then leaves the `model:` lines to the Admin. This is the pointer to the document. |
| `SYSP_REQ_ADMIN` | modified | One bullet: the Admin changes the `model:` lines after the User agreed a changed recommendation. Without it the Admin's authority list would not name who changes the agent files. |
| `SYSP_VC_TECHNICAL_WRITER_1` to `_4`, `SYSP_VC_ADMIN_1` to `_4`, `SYSP_US_TECHNICAL_WRITER`, `SYSP_US_ADMIN`, `SYSP_REQ_ACTOR_MODEL` | no change | The new bullets add no verification of their own; the document is checked by Quality's review of the Markdown artifact. |
| `SYSP_DOC_CHANGE_CONTRACT`, `SYSP_DOC_PRODUCT_MODEL`, `SYSP_DOC_EXAMPLE_ACTORS`, `SYSP_DOC_CUSTOMIZATION`, `SYSP_DOC_GETTING_STARTED`, `SYSP_DOC_OPERATIONS` | Technical Writer decides | They include the two requirements; the Technical Writer decides whether any guide needs a pointer to the new document. |
| New `doc` Need `SYSP_DOC_MODEL_RECOMMENDATION` | added (Technical Writer) | Realized by `docs/model-recommendation.md`; includes `SYSP_REQ_TECHNICAL_WRITER` and `SYSP_REQ_ADMIN`. |
| `docs/Syspilot Contracts/setup.md`, `SYSP_REQ_SETUP*` | no requirement change | The Developer changes the Setup Process under the existing Setup requirements; the User chose not to specify the document further. |

### Decisions And Evidence

| Decision or check | Evidence |
|---|---|
| Location: `docs/model-recommendation.md`, listed in the `User Guides` toctree of `docs/index.rst`, because it is a user-facing guide shipped with the release and Setup's source is the pinned release. In a target project Setup places it in that project's `docs/`; how the target root lists it follows the existing additive-navigation rule and the Developer's Setup change. | `docs/index.rst` User Guides toctree |
| Two ownership statements instead of one: the User asked for the document's ownership to be regulated; the Admin's part (the `model:` lines) is a second owner's authority and is stated in the Admin requirement, not hidden in the Technical Writer's. Alternative rejected: one bullet only in the Technical Writer requirement, which would leave the Admin's list silent on the agent files. | `SYSP_REQ_TECHNICAL_WRITER`, `SYSP_REQ_ADMIN` |
| Open for others: the role cards `docs/Syspilot Actors/Technical Writer.md` and `Admin.md` realize these requirements and may need one line each; the Technical Writer and the Developer decide with the Example sync, since both card sets are Markdown process artifacts. | not yet changed |
| Consistency check | `python docs/docs-build.py clean`: build succeeded, schema validation 0 warnings; no Need added, no new link obligation. |

## Infrastructure Impact

**Status:** complete

| Infrastructure artifact | Impact | Required action and evidence |
|---|---|---|
| Source release and Setup | The optional guide must be available in the pinned release used by Setup | At f00c3b7, `git ls-files` lists `docs/model-considerations.md`, its `export-ignore` attribute is unspecified, and `git archive --format=tar HEAD docs/model-considerations.md` contains it. Setup verifies the release commit and copies the guide from that tree only upon User adoption. The future tagged release has not yet been published |
| Documentation build | The guide must be included in the built documentation | `docs/index.rst` includes `model-considerations` under User Guides; the recorded strict build succeeded and `docs/_build/html/model-considerations.html` exists. Technical Writer also recorded a pristine target strict build with the guide adopted |
| `.github/workflows/release.yml` | No workflow or packaging change is needed | The unchanged workflow checks out the source, runs the strict documentation build and full test suite, and publishes Pages and the GitHub Release on a tag. No release workflow run was performed for this Change |

## User-Facing Documentation

**Status:** complete

### Documentation Plan And Ownership

| Documentation surface | `doc` Need | Requirements included | Status |
|---|---|---|---|
| `docs/model-considerations.md` | SYSP_DOC_MODEL_RECOMMENDATION | SYSP_REQ_TECHNICAL_WRITER, SYSP_REQ_ADMIN | Accepted directly by the User on 2026-11-20 (`a43e0bd`); Syspilot-only relative link removed so target copies build cleanly |
| `docs/product-model.md`, `docs/operations.md` | SYSP_DOC_PRODUCT_MODEL, SYSP_DOC_OPERATIONS | Existing actor ownership links remain applicable | Adds a pointer and the User/Admin boundary |
| `docs/index.rst` | SYSP_DOC_PORTAL | Existing portal requirements remain applicable | Lists the guide under User Guides |
| `docs/getting-started.md` | SYSP_DOC_GETTING_STARTED | Existing setup/actor links remain applicable | Aligned with `setup.md` (optional adoption question, target `docs/index.rst` entry, and Technical Writer task message) |

Impact queries were rerun from SYSP_REQ_TECHNICAL_WRITER and SYSP_REQ_ADMIN, both directions, depth 1, flat, no build. SYSP_DOC_PRODUCT_MODEL, SYSP_DOC_OPERATIONS, and SYSP_DOC_GETTING_STARTED carry aligned pointers and Setup summaries; SYSP_DOC_EXAMPLE_ACTORS is aligned through the cards and declared deviation. SYSP_DOC_CHANGE_CONTRACT needs no change because model selection adds no Contract gate. SYSP_DOC_CUSTOMIZATION already describes project-owned tailoring; the dedicated guide and portal supply the new detail. SYSP_REQ_ACTOR_MODEL, SYSP_US_TECHNICAL_WRITER, SYSP_US_ADMIN and both roles' four VCs are unchanged because this documentation creates no additional specification.

### Consultations And Factual Reviews

| Documentation surface | Consulted artifact owner | Review question | Evidence and disposition |
|---|---|---|---|
| The model considerations document | User | Is this accurate and understandable for the intended user? | Accepted directly by the User on 2026-11-20 at 04:55 ("ok ich glaube das passt so") after renaming to `model-considerations.md` and incorporating `Default Selection Principles`, `Min Index` plus explicit `GPT-6.1 Terra` fallbacks on `MAI Code 2` rows, the 12-model active Copilot table, and compact Steps 1–3 (`a43e0bd`) |
| Role cards and ownership boundary | Architect | Do the aligned cards preserve authority and optional project adoption? | Direct review accepted at 0e941f6; renamed requirement pointers and choice-oriented wording committed by Architect at 29ac791 |
| Role cards and pricing/application steps | Admin | Are the cards and environment-dependent procedures accurate? | Direct review accepted the cards and read-only cache access; step 3 now says add or update a field, use runtime completions, and verify effective selection despite manual overrides. Admin did not independently verify all rates or service freshness. |

### Changed Documentation And Verification

| Artifact | Change | Verification evidence |
|---|---|---|
| `docs/model-considerations.md` | Dated selection principles, nine-actor + subagent mapping (`Min Index` and explicit fallbacks), 12-model active Copilot reference table, workload estimate, compact Steps 1–3 with warning/deprecation filtering and missing-data fallback, and target-safe Setup adoption prose (no `Syspilot Contracts/setup.md` relative link) | Strict build passes; all 12 Copilot model rates/flags and 10 benchmarked scores/effort spans verified on 2026-11-20; four Decimal calculations match; User accepted content at `a43e0bd`; pristine target `sphinx -b html -W --keep-going -q` build with `model-considerations` adopted exits 0 |
| `docs/getting-started.md` | Aligns optional `Model Considerations` adoption question, generated `docs/index.rst` entry, and post-handoff Technical Writer task message with `setup.md` | `uv run python docs\docs-build.py clean`: zero warnings; 80 Setup/Example tests pass |
| Documentation map, portal, Product Model and Operations | Adds the doc Need and navigation/pointers | `uv run python docs\docs-build.py clean`: zero warnings; `git diff --check`: passes |
| Syspilot Technical Writer and Admin cards | Realizes the ownership bullets without assigning a model | Architect and Admin direct reviews accepted; 29 Example tests pass after rename |

The supplied read-only analysis was used as an initial candidate mapping, not copied as project evidence. No source-project usage ratios, local backend configuration (`Aphrodite`/`Qwen`), private memory links or task-specific performance claims appear in the guide. On 2026-11-20 the writer independently read only the model-cache key from VS Code's database in SQLite read-only mode, distinguishing vendor `copilot` from duplicate names under other vendors and verifying the 12 active current-generation Copilot models alongside the excluded warning-flagged (`statusIcon.id == "warning"`) and superseded entries. The public Artificial Analysis leaderboard and releases pages confirmed the 10 benchmarked scores and effort spans; MAI entries remain explicitly `n/a`. The cost example uses invented, labeled illustration buckets rather than a project average.

No agent frontmatter has been changed and no monthly heartbeat has been created by this Change's drafting step. The guide explicitly reports unavailable scheduling rather than claiming it exists; Setup's adoption task is realized in `docs/Syspilot Contracts/setup.md`.

During direct review on 2026-11-20, the User renamed the guide to **Model Considerations**, `docs/model-considerations.md`, because its purpose is explaining choices, not prescribing them. The model table remains a concrete starting choice. Navigation, the documentation Need's realized path and both card sets are aligned; the Need ID stays stable. Architect aligned the requirement pointers at 29ac791. The Contract filename and branch name are unchanged because they identify the Change, not the reader guide. Architect's concurrent build failed during the rename; the writer's clean build after rename passes.

## Example Sync

**Status:** complete

| Artifact | Change | Verification evidence |
|---|---|---|
| `docs/Example Actors/Technical Writer.md` | Carries the monthly review/User-agreement responsibility only when the project adopts the optional guide | Deviation declared in Example Actors index; 29 Example tests pass |
| `docs/Example Actors/Admin.md` | Same User-agreed agent-model update boundary as Syspilot's card | `uv run python -m unittest tests.test_acceptance_setup_examples`: 29 tests pass |
| `docs/Example Actors/index.md` | Extends the existing Technical Writer deviation rationale to optional adoption | Same parity suite and strict build pass |
| Example Contracts and Example Ontology | No change: model choice creates no Contract gate or ontology semantics, and pristine Setup is not an installed Example Contract | Disposition checked against scope |

The model recommendation is itself generalized and shipped from the pinned release's documentation; no second Example copy is added because it would duplicate the maintained recommendation. Developer owns the Setup placement and Technical Writer message.

## Implementation And Unit Verification

**Status:** complete

### Decisions And Evidence

| Decision | Chosen approach | Relevant alternatives | Rationale and evidence |
|---|---|---|---|
| Where the question sits | New subsection `Model Considerations Adoption` in Phase 3 directly after Contract Selection, asked in the same step | Phase 1 or Phase 7 | The guide is a documentation install job, so the answer must exist before the script and the scaffold are generated. |
| Navigation | The adopted guide is listed in the generated `docs/index.rst` and offered as an additive edit for an existing build | Leave it orphaned | The target's zero-warning build reports an orphaned page. |
| Technical Writer message | Phase 7 step 3, after the Project Manager message; failure is recorded and does not block the handoff | Send it in Phase 4 | The Technical Writer exists only after Actor creation, and the task is not an installation gate. |
| Evidence | New Evidence Summary row `Model Considerations`, outside the Phase 5 gates | New gate | The answer and message are delivery records; the guide file itself is covered by the Integrity gate as a seeded copy. |

### Changed Artifacts And Verification

| Artifact | Change | Verification evidence |
|---|---|---|
| `docs/Syspilot Contracts/setup.md` | Adoption subsection, installation job row, scaffold navigation, Phase 7 step 3 (later steps renumbered), Evidence Summary row | `python docs/docs-build.py clean` OK; `python -m unittest tests.test_acceptance_setup_examples tests.test_setup_contract_feedback`: 55 tests OK. One existing assertion needed its wording kept: the toctree sentence still contains the old phrase, followed by `plus model-considerations`. |

**Resolved:** the guide link that did not resolve in a target project was replaced by the Technical Writer; their row records the pristine target build.

## Quality Review

**Status:** complete

**Current judgment:** proceed. Specification, guide, Setup change, cards and documentation are consistent, verification is clean, and the Contract's recorded state is consistent.

### Applied Review Methods

| Method | Selected scope | Evidence | Findings | Limits |
|---|---|---|---|---|
| Build | Whole documentation | `python docs/docs-build.py clean` re-run: build succeeded | No finding | Browser rendering not checked |
| Test suite | Whole repository | `python -m unittest discover -s tests` re-run: 268 tests OK | No finding | Live Setup run and target build not repeated by Quality; Technical Writer's recorded target `-W` build relied on |
| MECE and Trace | `SYSP_REQ_TECHNICAL_WRITER`, `SYSP_REQ_ADMIN`; same-document, both directions, depth 2 | `analyze_mece.py`, `analyze_trace.py` | No finding | Semantic review required; no comparable peers discovered |
| Diff and text search | Setup Contract, getting-started, cards, requirements, `doc` Need, guide | Adoption question, step renumbering, navigation entry and cards agree; no `Aphrodite`, `actor-context` or `model-recommendation` path left outside this Contract | No finding | Guide content (rates, scores) accepted by the User and checked by the Technical Writer; not re-verified by Quality |
| Contract review | This Contract | Rows, sections, log | Two Developer-owned findings resolved at c3c9662 and re-checked | Advisory: the Architect's Affected Artifacts still names `docs/model-recommendation.md` and its role-card row reads 
ot yet changed; the Technical Writer section records the rename and the cards, so the record stays coherent. The Project Manager's first log row is stamped 04:33, later than its commit f0cb39b (04:31); a PM-owned closure note |

Verification is fully automated. Quality reviews the commands and results that the Developer and the Tester recorded, and executes a check itself only when a recorded result cannot support its judgment, recording the reason in the table above. A Markdown process artifact whose content has no automated check is verified by Quality's review, and the table above records that review and its limits.

Quality communicates its `proceed` judgment and supporting evidence directly to the Project Manager before the Project Manager presents the verified outcome for validation. Another actor's forwarded claim does not establish Quality's decision.

### Open Quality Issues

Keep this table synchronized with currently open issues. A missing automation is an open issue whose row names the task that closes it, the owner of that task, and the completion evidence. For each issue, Quality transfers current responsibility to the owner of the affected artifact. When Quality confirms the required outcome, update the affected artifact or evidence and remove the resolved row. At closure this table contains `None`.

| Artifact | Current issue | Required outcome |
|---|---|---|
| None | None | None |

## User Validation And Approval

**Recorded by:** Project Manager<br>
**Status:** accepted

Quality's `proceed` judgment verifies that the change is ready for validation; it does not validate user value. For an included validation, the Project Manager presents the observable outcome after receiving Quality's direct judgment and evidence. The User communicates the validation decision directly to the Project Manager, who records the decision and evidence. Another actor's forwarded claim does not establish the User's decision. If the user requests changes, the Project Manager transfers responsibility to an included artifact owner that can produce the required outcome.

Current responsibility remains with the User from Quality's handoff until the validation decision is recorded. The Project Manager's presentation and recording duties support that User-owned artifact; they do not make the Project Manager the validation owner or an intermediate responsibility relay.

**Decision and evidence:** The User validated the outcome in chat on 2026-11-20 at 12:43 ("validation passed"), after Quality's `proceed` at `0bdef1c` and after reading how Setup installs the guide.

## Closure

**Status:** accepted

- [ ] Every included artifact or gate has terminal status and completion evidence.
- [ ] Intent and outcome are `approved`.
- [ ] Quality has recorded a `proceed` judgment.
- [ ] Open Quality Issues contains `None`.
- [ ] User validation is `accepted`, or its `not applicable` status and explicit User delegation are recorded in the artifact row.
- [ ] The feature branch is squash-integrated into `development`, or the `Version control` row is `not applicable` with its recorded reason.
- [ ] Current blocker is `none`.
- [ ] The observable outcome is demonstrated.
- [ ] The Project Manager ran the `syspilot.contract-statistics` skill after validation and the record exists in `.syspilot/stats/`.

**Final outcome:** pending
