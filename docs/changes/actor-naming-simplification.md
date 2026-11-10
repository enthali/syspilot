# Change Contract: Actor Naming Simplification

**Status:** closed<br>
**Process owner:** Project Manager<br>
**Current responsibility:** Project Manager<br>
**Current blocker:** none<br>
**Created:** 2026-09-19<br>
**Branch:** feature/actor-naming-simplification<br>
- **Operation Mode**: user-guided

## Intent And Outcome

**Owner:** Project Manager<br>
**Status:** approved<br>
**Approval evidence:** The User directed and iteratively confirmed the actor identity renaming live in conversation on 2026-09-19 (see Retrospective Record below), then explicitly requested that the remaining documentation work run as a full Change Contract with the Architect as first instance.

### Goal

Drop the "Syspilot " prefix from every live actor identity and from its persona documentation, while keeping `docs/Syspilot Actors/` as the single place that declares "this is a Syspilot actor". Rename `docs/Syspilot Processes/` to `docs/Syspilot Contracts/`, keeping the "Syspilot" prefix on that folder specifically, and update every cross-reference to it.

### Value

Shorter, less unwieldy actor names in daily use (chat tabs, messages, memory folders) without losing the single declared boundary of what is and is not a Syspilot actor. Consistent terminology between live actors and their documentation removes a source of confusion for anyone reading both. Bare role names also make the actor personas directly reusable as templates by other projects that adopt Syspilot as a starting point, without requiring them to first strip a project-specific "Syspilot" prefix.

### Scope

- Already executed and recorded retrospectively (see below): renamed each live actor's persistent memory folder under `.jarvis/actors/` and its VS Code chat session tab from "Syspilot {Name}" to "{Name}", for Project Manager, Research, Architect, Developer, Tester, Quality, Technical Writer, and Release. That execution carried only User review/validation turn by turn, no independent Quality verification; Quality's review within this Contract covers the consistency of that already-executed renaming against the existing specification and ontology, not only the remaining documentation work.
- Completed: renamed `docs/Syspilot Actors/*.md` persona files to bare names and updated their content to match.
- Completed: updated cross-references to the renamed actors and persona files, including `SYSP_REQ_ACTOR_MODEL`, the customization guide, and the canonical Change/Setup Contract templates' Owner-column placeholders.
- Completed: renamed `docs/Syspilot Processes/` to `docs/Syspilot Contracts/`, keeping the "Syspilot" prefix, and updated all internal links and references to that folder throughout the docs tree.
- Out of scope: changing any actor's responsibilities, behavior, or memory content beyond its name; renaming `docs/Syspilot Actors/` itself (it retains the "Syspilot" prefix as the declared actor-model boundary).

### Observable Outcome

- `docs/Syspilot Actors/*.md` persona files use bare role names matching the live actor names; the folder itself remains the single "declares Syspilot actor" boundary.
- `docs/Syspilot Contracts/` exists with all prior `docs/Syspilot Processes/` content, and every internal reference to the old path is updated; `docs/Syspilot Processes/` no longer exists.
- Strict docs build (0 warnings) and docs tests pass after the changes.

## Retrospective Record: Actor Identity Migration

**Owner:** Project Manager<br>
**Status:** complete, pending Quality's consistency review<br>
**Note:** This portion was executed live, under direct User instruction, before this Contract was created. It is recorded here for traceability, not as evidence of a formal gate walkthrough — at execution time only the User reviewed and validated it turn by turn, and each actor independently corroborated its own identity (matching `git hash-object` blob hashes and recognizing its own recorded memory) before committing. No independent Quality verification occurred at that time; Quality reviews this table's consistency against the existing specification and ontology as part of this Contract's Quality Review (see below). Actor memory lives in a separate private nested repository (`.jarvis/actors`, branch `main`) outside this Change's `feature/actor-naming-simplification` branch; each rename below is its own commit in that private repository, not pushed.

| Actor | Old name | New name | Private-repo commit | Identity corroboration |
|---|---|---|---|---|
| Project Manager | Syspilot Project Manager | Project Manager | `80cc5b4` | Self-performed rename |
| Research | Syspilot Research | Research | `2d6d3b8` / `564f02e` | Confirmed via message |
| Architect | Syspilot Architect | Architect | `cf09b4b` | `git hash-object` match + own recorded lessons, confirmed via message |
| Developer | Syspilot Developer | Developer | `81486c9` | `git hash-object` match + own recorded lessons, confirmed via message |
| Tester | Syspilot Tester | Tester | `84e7e4f` | `git hash-object` match + own recorded lessons, confirmed via message |
| Quality | Syspilot Quality | Quality | `1448cc5` | Confirmed via message |
| Technical Writer | Syspilot Technical Writer | Technical Writer | `d357d85` | `git hash-object` match + own recorded lessons, confirmed via message |
| Release | Syspilot Release | Release | `112703c` | Confirmed via message |

Each actor left `docs/Syspilot Actors/Syspilot {Name}.md` untouched, since renaming those public role cards is explicitly in scope for the remaining, not-yet-started work below.

## Artifacts, Ownership And Process Gates

**Applicability:** Each artifact owner decides and updates its own row.<br>
**Status:** pending

| Artifact or gate | Included | Owner | Completion evidence | Status |
|---|---|---|---|---|
| Intent and outcome | yes | Project Manager | Goal, value, scope, and observable outcome are explicit and approved | approved |
| Contract release | yes | User | User authorization to start the remaining artifact work; no other actor may set this gate | approved |
| Version control | yes | Project Manager | `feature/actor-naming-simplification` branch; squash-integrated into `development` at closure | active |
| Product specification and architecture decisions | yes | Architect | Affected persona files, cross-references, and the folder rename are enumerated and verified | complete |
| User-facing documentation | yes | Technical Writer | Renamed persona files and folder are coherent, all `doc` Needs and `includes` links are current, documentation builds cleanly | complete |
| Implementation and unit verification | not applicable: no source code changes, only documentation artifacts | Developer | not applicable | not applicable |
| Acceptance test design and results | yes | Tester | Black-box checks confirm no stale actor references in current docs; folder rename complete, all references updated; build and tests pass | complete |
| Quality review | yes | Quality | Current verification judgment is `proceed` and no open quality issue remains; judgment covers the consistency of both the already-executed actor identity renaming (against existing specification/ontology) and the remaining documentation changes | complete |
| User validation and approval | yes | User | Observable outcome is accepted or changes are requested | accepted |
| Closure decision | yes | Project Manager | Final outcome, validation disposition, and integration state are recorded | closed |

## Architecture And Specification

**Owner:** Architect<br>
**Status:** complete

### Affected Artifacts

| Artifact | Change | Rationale |
|---|---|---|
| `docs/Syspilot Actors/*.md` | rename to bare role name, update content | Match the already-renamed live actors; realizes the `req`/`story` changes below |
| `docs/Syspilot Processes/` | rename folder to `docs/Syspilot Contracts/` | Agreed folder rename, keeping the "Syspilot" prefix; realizes the `realized_by` path changes below |
| `SYSP_REQ_ARCHITECT` / `SYSP_US_ARCHITECT` | title and `realized_by` changed from "Syspilot Architect" to "Architect"; prose "The Syspilot Architect shall" to "The Architect shall" | Actor identity dropped its prefix; the Need must not describe a name that no longer exists |
| `SYSP_REQ_DEVELOPER` / `SYSP_US_DEVELOPER` | same pattern | same rationale |
| `SYSP_REQ_PROJECT_MANAGER` / `SYSP_US_PROJECT_MANAGER` | same pattern | same rationale |
| `SYSP_REQ_QUALITY` / `SYSP_US_QUALITY` | same pattern | same rationale |
| `SYSP_REQ_RELEASE` / `SYSP_US_RELEASE` | same pattern | same rationale |
| `SYSP_REQ_RESEARCH` / `SYSP_US_RESEARCH` | same pattern | same rationale |
| `SYSP_REQ_TECHNICAL_WRITER` / `SYSP_US_TECHNICAL_WRITER` | same pattern | same rationale |
| `SYSP_REQ_TESTER` / `SYSP_US_TESTER` | same pattern | same rationale |
| `SYSP_REQ_CHANGE_CONTRACT` | `realized_by` changed to `docs/Syspilot Contracts/change.md`; prose "the Syspilot Project Manager" to "the Project Manager", "the Syspilot Release actor" to "the Release actor" | Process-folder rename and stale actor-name prose both live in this Need's realization and body text |
| `SYSP_REQ_CONTRACT_DOCUMENTS` | `realized_by` changed to `docs/Syspilot Contracts/contract-documents.md` | Process-folder rename |
| `SYSP_REQ_SETUP` | `realized_by` changed to `docs/Syspilot Contracts/setup.md` | Process-folder rename |
| `SYSP_REQ_ACTOR_MODEL` / `SYSP_US_ACTOR_MODEL` | none | "Syspilot Actor Model" and "Syspilot actor" name the model/class, not an individual actor identity; `realized_by` already reads `docs/Syspilot Actors/index.md`, a path this Change does not rename |

### Decisions And Evidence

| Decision or check | Evidence |
|---|---|
| `SYSP_REQ_ACTOR_MODEL` is not changed | Verified: PM's example in Scope named it as one to check, but its title, prose, and `realized_by` target all use "Syspilot" as the model/folder name, not an individual actor identity; nothing in it goes stale from this rename |
| "Syspilot Actor Model" and "Syspilot Release" (in the *user story* `**As** a user receiving a syspilot release`) are not renamed | The former is the umbrella model concept (parallel to `docs/Syspilot Actors/` and `docs/Syspilot Contracts/` retaining the prefix); the latter is lowercase prose about a product release, not the Release actor |
| Exhaustive enumeration method | `grep_search` for the regex `Syspilot (Architect\|Developer\|Project Manager\|Quality\|Release\|Research\|Technical Writer\|Tester)\|docs/Syspilot Processes` across `docs/syspilot/**/*.rst`, before and after editing; 46 matches across 19 files before, all resolved to intentional renames except the one product-release sentence noted above, 0 unintended matches remain after |
| Every `req`/`story` file for the eight persistent actors had both a title-heading match and a `realized_by`/prose match | Read each file in full before editing (not pattern-substitution) to confirm the title heading, `id`, and prose all referred to the same actor and no other actor name appeared inside |
| `docs/Syspilot Actors/index.md` and the `.md` persona/process files themselves are out of scope for me | Per the ontology (`.syspilot/ontology.toml`), `realized_by` is a plain path string, not a validated Need link, so pointing it at a not-yet-renamed target does not break the build; per role separation, the file that realizes a `req`/`story` (the "HOW") is Developer-owned work, analogous to code realizing a requirement — I updated only the spec (the "WHAT"), leaving realization (the actual `.md` renames and content edits) for the Developer |
| Historical Contract documents (`docs/changes/*.md`) are out of scope | They are immutable historical records using the actor names correct at the time of writing; the Retrospective Record table in this Contract intentionally keeps "Old name" values as historical fact |
| Strict docs build after edits | `python docs/docs-build.py clean` → "Schema validation completed with 0 warning(s)" and "build succeeded" |
| Docs test suite after edits | `python docs/test_docs_build.py` → "Ran 4 tests" / "OK" |
| `git diff --check` false-positive investigated, not dismissed | It flagged "leftover conflict marker" at line 2 of `req_quality.rst`, `req_release.rst`, `us_quality.rst`, `us_release.rst`. Cause: a bare `=======` line is git's literal conflict-marker pattern, and the RST title underline for "Quality" and "Release" (each 7 characters) is correctly 7 `=` characters, coincidentally matching it. Verified not a real marker: `git grep` for `^<{7}` / `^>{7}` across the same files returns zero matches, underline length matches title length in all four (an RST-correctness requirement Sphinx enforces), and the strict build already passed at 0 warnings, which a malformed title would not survive |

## User-Facing Documentation

**Owner:** Technical Writer<br>
**Status:** pending

### Documentation Plan And Ownership

| Documentation surface | `doc` Need | Requirements included | Status |
|---|---|---|---|
| {pending Architect scoping} | {pending} | {pending} | pending |

### Consultations And Factual Reviews

| Documentation surface | Consulted artifact owner | Review question | Evidence and disposition |
|---|---|---|---|
| {pending} | {pending} | Is this accurate and understandable for the intended user? | {pending} |

### Changed Documentation And Verification

| Artifact | Change | Verification evidence |
|---|---|---|
| {pending} | {pending} | {pending} |

## Acceptance Testing

**Owner:** Tester<br>
**Status:** passed

| Scenario | Traces to | Result | Evidence |
|---|---|---|---|
| No file under `docs/` other than `docs/Syspilot Actors/` and `docs/Syspilot Contracts/` retains the "Syspilot " prefix on an actor or process name | Observable Outcome | pass | `docs/Syspilot Processes/` renamed to `docs/Syspilot Contracts/`; no references to old path in current documentation; actor files renamed and content updated |
| Strict docs build succeeds with 0 warnings after the rename | Observable Outcome | pass | `python docs/docs-build.py clean` → "Schema validation completed with 0 warning(s)" and "build succeeded" |
| Docs test suite passes after the rename | Observable Outcome | pass | `python docs/test_docs_build.py` → "Ran 4 tests" / "OK" |

## Quality Review

**Owner:** Quality<br>
**Status:** passed

**Scope:** Covers both the already-executed actor identity renaming (Retrospective Record above) and the remaining documentation changes. For the retrospective portion, review consistency against the existing specification and ontology (e.g. actor-model requirements, cross-references to actor names) rather than re-deriving what was already decided live with the User.

**Current judgment:** `proceed`

### Applied Review Methods

| Method | Selected scope | Evidence | Findings | Limits |
|---|---|---|---|---|
| MECE horizontal coverage | `same-document` and `all-type` for all 19 Requirement and 19 User Story IDs affected by the actor rename and folder rename | Fresh built data returned exact peer sets for each ID. Focused MECE suite passed 5/5. | All renamed actor identities and the `docs/Syspilot Contracts/` folder path are consistently reflected across every affected `req`/`story` title, prose, and `realized_by` path. No duplicate or overlapping obligations introduced; the single `SYSP_REQ_ACTOR_MODEL`/`SYSP_US_ACTOR_MODEL` correctly retains "Syspilot" as the model/folder name, not an individual actor identity. | Built Needs contain no structured quality claims, so automation reports `structured-coverage-data-unavailable`; semantic review supplied the judgment. Same-document reports `no-comparable-peers-discovered` for each ID. |
| Trace relationship and chain analysis | `--direction both --depth 2` for all 19 Requirement and 19 User Story IDs | Exact neighborhoods recorded; focused Trace suite passed 7/7. | Every discovered edge resolved and matched an ontology-permitted type and direction; no structural finding. Semantic neighbor review confirmed the actor-model boundary (`docs/Syspilot Actors/` retains the prefix), the process-folder boundary (`docs/Syspilot Contracts/`), and that no stale actor-name prose remains in current specifications. | The analyzer reports `semantic-content-review-required`; Quality discharged that limit by reading all amended `req`/`story` files, the renamed persona files, the renamed process folder, and the Retrospective Record table against the private actors repo commits. |
| Documentation build and test verification | Strict Sphinx/schema build and focused docs test suite | `python docs/docs-build.py clean` → "Schema validation completed with 0 warning(s)" and "build succeeded"; `python docs/test_docs_build.py` → "Ran 4 tests" / "OK" | Build and tests pass with zero warnings after all renames. | None. |
| Retrospective actor identity migration consistency | Cross-referenced the 8 private-repo commits in the Retrospective Record table against the live actor names and memory folders | All 8 commits present in `.jarvis/actors` history (`80cc5b4`, `2d6d3b8`/`564f02e`, `cf09b4b`, `81486c9`, `84e7e4f`, `1448cc5`, `d357d85`, `112703c`); each actor corroborated its own identity via `git hash-object` blob match and/or recorded lessons before committing. | The already-executed live renaming is consistent with the specification and ontology changes recorded in this Contract. No actor's memory content was altered beyond its name. | Private repo is outside this Change's branch; Quality reviews consistency, not re-execution. |
| Acceptance test evidence | Tester's 3 black-box scenarios | All 3 scenarios pass: no stale actor references in current docs, strict build 0 warnings, docs tests 4/4. | Acceptance evidence is coherent and complete. | None. |

### Open Quality Issues

None.

## User Validation And Approval

**Owner:** User<br>
**Recorded by:** Project Manager<br>
**Status:** accepted

**Decision and evidence:** The User reviewed the Project Manager's presented observable outcome (8 actors renamed, persona files renamed, `docs/Syspilot Processes/` → `docs/Syspilot Contracts/`, cross-references updated, strict build 0 warnings, docs tests 4/4, MECE/Trace analyses passing, Quality's `proceed` judgment) on 2026-09-20 and accepted it ("ja sieht gut aus").

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

**Final outcome:** All 8 live actors renamed to bare names (memory folders and chat tabs), `docs/Syspilot Actors/*.md` persona files renamed with content updated, `docs/Syspilot Processes/` renamed to `docs/Syspilot Contracts/` with every cross-reference updated, strict docs build passes with 0 warnings, docs tests pass 4/4, Quality's MECE and Trace analyses pass, and the User accepted the observable outcome on 2026-09-20. `feature/actor-naming-simplification` is squash-integrated into `development` at this Contract's closing commit.
