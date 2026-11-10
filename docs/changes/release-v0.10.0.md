# Release Contract: 0.10.0

**Status:** approved<br>
**Process owner:** Release<br>
**Current responsibility:** Admin<br>
**Current blocker:** QI-1: superseded preflight candidate; QI-2: required hosted validation pending<br>
**Created:** 2026-11-10<br>
- **Operation Mode:** user-guided

- **user-guided** - every actor involves the user in its decision-making before proceeding.

## Handover log

The handing-over actor appends one line immediately before handing over, in the same commit that changes Current responsibility, using the observed local date and time. Evidence stays in the corresponding sections; the header is authoritative.

| Date | Time | From | To | Note |
|---|---|---|---|---|
| 2026-11-10 | 11:54 | Project Manager | Release | User approved release start in user-guided mode; preparation can begin. |
| 2026-11-10 | 11:58 | Release | Technical Writer | Inventory verified, v0.10.0 release notes written; user-facing documentation check next. |
| 2026-11-10 | 12:50 | Technical Writer | Release | Documentation accuracy complete with User approval; stale portal/shared-Contract claims corrected, factual review clear, strict build and focused checks pass. |
| 2026-11-10 | 13:05 | Release | Admin | Preflight passed at P 5637fa4; triggers 1 and 2 recorded; Infrastructure impact row to complete. |
| 2026-11-10 | 13:05 | Admin | Release | Infrastructure impact recorded; changed workflow inputs and environment make validation-only CI revalidation necessary, pending User authorization to push the branch. |
| 2026-11-10 | 13:08 | Release | Quality | Preflight, documentation and infrastructure complete; independent release review needed. |
| 2026-11-10 | 13:13 | Quality | Release | Blocked: corrected protected record and new P needed; hosted validation remains pending. |
| 2026-11-10 | 13:15 | Release | Admin | QI-3: synchronize the Infrastructure artifact row with the completed section. |
| 2026-11-10 | 13:15 | Admin | Release | Infrastructure artifact row synchronized with the completed assessment in commit ecc8b2e; hosted validation remains pending User authorization. |

## Objective And Scope

**Status:** approved<br>
**Approval evidence:** The User approved release start with "ok go" on 2026-11-10 after reviewing the scope and shortened Known Limitations, and selected user-guided mode.

### Objective

Publish Syspilot v0.10.0: the Contract-driven source release, with project-owned Actor and Contract examples, ontology-aware skills, pristine Setup and its feedback corrections, user documentation and the revised release process. The deliverable is the source state on main and its version tag, rendered documentation and GitHub Release, not an installer package.

### Included Changes

Initial inventory candidates below follow integration order. Release verifies completeness against the actual v0.9.1-to-development source difference, including changes without a modern Contract, and resolves missing closure or Example sync evidence before preflight. This list is not yet a verified release inventory.

| Candidate | Integration reference |
|---|---|
| v2-foundation | 5e68781 |
| documentation-foundation | 8c8d674 |
| validation-provenance | 998dd74 |
| pristine-setup | 547f9a1 |
| contract-handling | 41b653a |
| v2-skill-foundations | 6537f8c |
| setup-ontology-review | 1e06939 |
| actor-memory-separation | b95a75f |
| pre-initial-release-review | e20c565 |
| mece-trace-skills | 603c8b3 |
| version-control-ownership | 45dfbd5 |
| contract-gates-and-modes | e7d7540 |
| actor-naming-simplification | 2ea4a86 |
| actor-handoff-consultation-model | e94e68f |
| sphinx-needs-graph-alignment | e3343b6 |
| vse-adoption-feedback | 4afc552 |
| shorter-handover-text | 0001ee9 |
| setup-examples | 091748e |
| setup-feedback-2 | ddb8dbc |
| release-contract-preflight | eded12d |

### Known Limitations

Publication is not atomic: Pages deployment may succeed before GitHub Release creation fails. The User accepted this risk.

## Artifacts, Ownership And Process Gates

**Applicability:** Each artifact owner decides and updates its row.<br>
**Scope change:** A widened objective/inventory returns to draft until approved; affected completed rows are reassessed by their owners.<br>
**Ownership:** The Owner column is authoritative.<br>
**Status:** pending

| Artifact or gate | Included | Owner | Completion evidence | Status |
|---|---|---|---|---|
| Objective and scope | yes | Project Manager | User approved the scope on 2026-11-10; Release verifies the candidate inventory | approved |
| Release start | yes | User | User: "ok go", 2026-11-10; preparation only, no push authorization | approved |
| Change inventory | yes | Release | Integrated Changes closed; Example sync verified or justified | complete: 20 Changes verified against first-parent history on 2026-11-10, all closed (see Change Inventory) |
| Version | yes | Release | Tag, newest release-note heading and documentation agree | pending |
| Preflight | yes | Release | Four local checks on P; triggered CI validation separately authorized | complete: four checks pass at P 5637fa4; validation-only run required, not yet authorized |
| Release notes | yes | Release | One v0.10.0 heading covers all included Changes | complete: single `## v0.10.0` heading with 20 entries in integration order and known limitations; `check_release_version.py v0.10.0` passes |
| User-facing documentation | yes | Technical Writer | Portal/shared-Contract corrections cc772a6 and Release-owned Setup-note correction 3d86026 reviewed; Architect factual review clear, strict build (zero warnings), 4 build tests, 27 focused checks and v0.10.0 version check pass; User approved completion on 2026-11-10 | complete |
| Infrastructure impact | yes | Admin | Workflow-input and environment comparison, trigger assessment, and hosted revalidation requirement recorded in Infrastructure Impact; commit ecc8b2e | complete |
| Release verification | yes | Quality | Independent review on 2026-11-10; QI-1 to QI-3 below; Release agrees a corrected record and fresh P are needed | blocked |
| Publication | yes | Release | Explicit push authorization, main/tag, successful workflow, Pages and GitHub Release verified | pending |
| Closure | yes | Release | Closure checklist and publication evidence complete | pending |

## Change Inventory

**Status:** pending

Release verifies the candidates above, closure and Example sync, and records the final inventory here before P. No prior-release commit is included merely because it appears in branch history.

| Change | Integrated commit | Contract closed | Example sync |
|---|---|---|---|
| v2-foundation | 5e68781 | yes | no row |
| documentation-foundation | 8c8d674 | yes | no row |
| validation-provenance | 998dd74 | yes | no row |
| pristine-setup | 547f9a1 | yes | no row |
| contract-handling | 41b653a | yes | no row |
| v2-skill-foundations | 6537f8c | yes | no row |
| setup-ontology-review | 1e06939 | yes | no row |
| actor-memory-separation | b95a75f | yes | no row |
| pre-initial-release-review | e20c565 | yes | no row |
| mece-trace-skills | 603c8b3 | yes | no row |
| version-control-ownership | 45dfbd5 | yes | no row |
| contract-gates-and-modes | e7d7540 | yes | no row |
| actor-naming-simplification | 2ea4a86 | yes | no row |
| actor-handoff-consultation-model | e94e68f | yes | no row |
| sphinx-needs-graph-alignment | e3343b6 | yes | no row |
| vse-adoption-feedback | 4afc552 | yes | no row |
| shorter-handover-text | 0001ee9 | yes | no row |
| setup-examples | 091748e | yes | complete |
| setup-feedback-2 | ddb8dbc | yes | complete |
| release-contract-preflight | eded12d | yes | complete |

Verified 2026-11-10 against `git log --first-parent v0.9.1..development`: these 20 are the integrations of the release; the five workspace commits `5134d1f`, `266d0b1`, `a165cac`, `877acc4`, `58b426a` change only `.vscode/syspilot.code-workspace` and `.gitignore`, and `38ed5d6` only a setup agent version line, so they are not Changes of the release. `no row` marks a Contract closed before the Example sync row existed.

## Version

**Status:** pending

**Version:** 0.10.0 - User-requested minor release.

The tag is v0.10.0. Release prepares exactly one newest matching heading in docs/releasenotes.md; documentation metadata derives from that source. The version checker must pass.

## Preflight

**Status:** complete

**Preflighted commit P:** 5637fa41d6055e2287d0dbb64057061d2ef97c3f

Commit release notes and release-facing documentation before choosing P. Apply the canonical Release Process's protected-record and revalidation rules.

1. `uv run python docs/test_docs_build.py -v`
2. `uv run python docs/docs-build.py clean`
3. `uv run python -m unittest discover -s tests -v`
4. `uv run python scripts/check_release_version.py v0.10.0`

The strict build needs network access to docs.python.org. Local success does not prove execution on Linux or publication.

| Check | Command and commit | Result |
|---|---|---|
| 1 | `uv run python docs/test_docs_build.py -v` at P, 2026-11-10 | pass: 4 tests OK (the printed build-failed line belongs to a negative test) |
| 2 | `uv run python docs/docs-build.py clean` at P, 2026-11-10 | pass: strict build succeeded |
| 3 | `uv run python -m unittest discover -s tests` at P, 2026-11-10 | pass: 202 tests OK (run without `-v`; same test set) |
| 4 | `uv run python scripts/check_release_version.py v0.10.0` at P, 2026-11-10 | pass: v0.10.0 is the newest heading and matches `docs/conf.py` |

### Revalidation triggers

Admin records the trigger paths/environment comparison against the last successful tag-run baseline; Release decides sufficiency. Use the canonical trigger conditions, including its bounded release-notes exception. No successful current-workflow baseline has yet been established in this record.

| Trigger | Observable test | Fired |
|---|---|---|
| Workflow input changed | Compare canonical trigger inputs against the last successful tag-run commit | yes (Admin, 2026-11-10): `release.yml`, `.syspilot/ontology.toml`, `docs/_static/needs-dark-mode.css`, `docs/conf.py`, `docs/requirements.txt` changed and `scripts/check_release_version.py` added since v0.9.1 |
| Environment change | Admin statement against prior runner/tool baseline | yes (Admin, 2026-11-10): Python 3.11/pip became 3.13/uv; sphinx-needs bound raised; v0.9.1 run logs are gone, so no image comparison is possible |
| No tag-run evidence | Verify evidence for the preceding release | not relied on: v0.9.1 had a successful tag run, but of the older workflow, so no comparable baseline exists; triggers 1 and 2 suffice |

| Validation-only run | Authorization | Result |
|---|---|---|
| Required on a pushed branch (triggers 1 and 2) | Not granted | pending |

## Release Notes

**Status:** complete

Release is the only writer of docs/releasenotes.md. Cover the verified inventory in integration order, explaining user value and limitations.

## User-Facing Documentation

**Status:** complete

The User approved the release-accuracy check and requesting the Setup-note correction from Release on 2026-11-10. After reviewing the findings, the User also approved correcting the portal and shared-Contract explanations, explicitly retaining Syspilot's experimental status while recognizing implemented Setup. These are explanations of existing released behavior, not new release scope or authorization to push.

Impact queries for `SYSP_REQ_RELEASE_CONTRACT` and `SYSP_REQ_SETUP` (both directions, depth 1, `--flat --no-build`) succeeded on 2026-11-10. The results identify candidate guides; the direct review also includes the rendered portal, documentation map, notes and all nine user-facing guides/README.

| Document | Required update | Evidence |
|---|---|---|
| `docs/index.rst` | Replace obsolete unimplemented-bootstrap/repository-preview claim with implemented release-bound Setup, keeping experimental-project framing and linking evidence limits | Committed in `cc772a6`; Architect factual review clear; strict build and rendered `index.html` confirm the corrected text |
| `docs/methodology.md` | Qualify tailoring by Contract kind: Release retains required headings and excludes unattended mode | `cc772a6`; Architect confirms canonical Release and shared Contract Documents alignment; strict build passes |
| `docs/product-model.md` | State that every Contract kind carries the Handover log, not Change alone | `cc772a6`; Architect confirms the shared Contract rule; strict build passes |
| `docs/syspilot/documentation/index.rst` | Add `SYSP_DOC_PORTAL` for the independently maintained rendered entry point; existing guide Needs/includes still cover their explanations | Strict schema/build validation passes; exported `SYSP_DOC_PORTAL` has `realized_by: docs/index.rst` and the three intended includes; it covers Syspilot's own portal, not an adopter's generated neutral index |
| `README.md`, `docs/getting-started.md`, `docs/customization.md`, `docs/change-contract.md`, `docs/operations.md`, `docs/branching.md`, `docs/upgrade.md` | Reviewed against v0.10.0 notes: current stack, ordinary-session Setup/Admin path, project-owned examples/ontology, authority, upgrade-to-0.10 guidance, four checks, bounded record review and partial-publication limits remain applicable; no edits needed | Source review complete; no runtime installation/publication claimed |
| `docs/releasenotes.md` (Release-owned) | Remove the new v0.10.0 entry's blanket unverified-installation claim; preserve reported-run versus deferred-scenario distinction from Operations | Release committed `3d86026`; source checked against Operations, including reported successful runs, undemonstrated deferred scenarios and the limits of automated checks |

Architect's direct factual review of `cc772a6` on 2026-11-10 found no issues against `SYSP_REQ_CONTRACT_DOCUMENTS`, `SYSP_REQ_CHANGE_CONTRACT`, `SYSP_REQ_RELEASE_CONTRACT` and `SYSP_REQ_SETUP`. It confirmed the implemented/verified distinction and the portal Need's scope. No specification, canonical process or example behavior was changed.

Verification on 2026-11-10: `python docs/docs-build.py clean` succeeded with zero warnings; `python docs/test_docs_build.py -v` passed 4 tests; `python -m unittest tests.test_acceptance_adoption_feedback.SharedContractRulesTests tests.test_acceptance_adoption_feedback.ReleaseProcessTests tests.test_acceptance_setup_examples.DocNeedTests` passed 27 tests; `python scripts/check_release_version.py v0.10.0` passed and confirmed the newest heading agrees with `docs/conf.py`. The rendered portal contains the implemented Setup and experimental-project wording. These checks do not replace Release's four-check preflight or prove Linux execution, installation scenario coverage or publication.

After reviewing the corrections and results, the User explicitly approved completing this documentation row and returning responsibility to Release on 2026-11-10. No push or publication authorization was requested or granted.

## Infrastructure Impact

**Status:** complete

Admin compared preflighted commit P `5637fa4` with the last successful tag-triggered run, v0.9.1 run `30684899863` at `cc063e1` (all four jobs passed). The run used the older workflow and its logs are no longer available (HTTP 410), so it provides no evidence for the current workflow or the old runner image and resolved package versions.

The canonical trigger-path comparison found changes to `.github/workflows/release.yml`, `.syspilot/ontology.toml`, `docs/_static/needs-dark-mode.css`, `docs/conf.py`, and `docs/requirements.txt`, plus the addition of `scripts/check_release_version.py`. `docs/docs-build.py`, `docs/test_docs_build.py`, `docs/_templates/`, and `assets/syspilot-logo.svg` are unchanged. The environment also changed from Python 3.11 with pip to Python 3.13 with uv (`astral-sh/setup-uv@v6`); the `sphinx-needs` minimum changed from 2.0.0 to 4.1.0. A fresh dependency resolution recorded on 2026-11-09 selected Sphinx 9.2.0 and sphinx-needs 9.2.0. Both workflow definitions use `ubuntu-latest` and install Graphviz, but the unavailable prior logs prevent comparison of the actual runner image. These findings are the basis for the fired triggers above; Release remains responsible for the gate decision.

The current workflow runs documentation build tests and, on tag pushes, the tag/version check before the strict documentation build and QA suite; publication and GitHub Release creation remain tag-only. The four local preflight checks passed at P, but do not prove execution on the hosted Linux runner. A validation-only run is therefore required; none has been pushed or run because User authorization to push the branch has not been granted.

| Infrastructure artifact | Impact | Required action and evidence |
|---|---|---|
| `.github/workflows/release.yml` and its build inputs | No workflow defect identified; prior successful run does not cover the current workflow or resolved environment | Trigger-path and environment comparison recorded above and in Revalidation Triggers; Release was consulted and retains the gate decision. Validation-only hosted run remains pending User authorization to push its branch. |

## Release Verification

**Status:** blocked

**Current judgment:** blocked. The User authorized independent review only on 2026-11-10, not a push, workflow run, tag or publication. P `5637fa4` cannot cover the current candidate: protected sections still record unfinished preparation, and subsequent commit `8fcb53b` changes a non-record path. Release agreed through consultation to correct the record, include that commit in a new P and repeat the four local checks. The triggered validation-only run remains required and unperformed. This is not a publication-ready judgment.

**Version and tag:** 0.10.0 / v0.10.0

Quality independently reviews Change closure, release-note coverage, documentation and preflight evidence and reports directly to Release. At R it reviews the complete P..R record diff: the checker covers protected blocks only; unprotected changes must remain evidence-only in substance, or require a new preflight. Actual push authorization must be present in R.

### Review Evidence And Limits

- Inventory checks confirmed all 20 listed Change headers are closed; the three Contracts carrying an Example sync row record it complete. The 20 release-note entries follow the integration order. First-parent history includes earlier branch history already represented in v0.9.1; its presence alone does not add release scope.
- Reviewed the release-facing corrections at `3d86026` and `cc772a6` and the Technical Writer's terminal evidence. The revised portal distinguishes implemented Setup from demonstrated practical coverage, and the guide corrections agree with shared Contract and Release rules. No new documentation defect identified in these corrections.
- Reviewed the four recorded local results at P: 4 documentation-build tests, strict clean build, 202 QA tests and version check. Omitting unittest's verbosity flag does not change the discovered suite. These results remain evidence for that P, not for an enlarged candidate or the hosted runner. No build or suite rerun by Quality; fresh preflight belongs to Release.
- Quality ran `python scripts/check_release_record.py 5637fa4 efd1936 v0.10.0`: exit 0. Reviewed the complete record diff; it records responsibility, local results and infrastructure/trigger evidence without changing procedure or release content. This intermediate pass is not the final P-to-R review.
- HEAD advanced during review to `8fcb53b453001dd4628fcd87f7b7046110f3d849`. Because this added an unreviewed non-record path after P, Quality ran `python scripts/check_release_record.py 5637fa4 8fcb53b v0.10.0`: exit 1, `path other than the record in the difference from P to R: .vscode/syspilot.code-workspace`. The workspace change was not modified or reverted by Quality.
- The pending Version row and Version/Change Inventory section statuses, and the Objective's unverified-inventory wording, are protected at P. Release must settle them before choosing the replacement P; changing them afterward cannot inherit the old preflight.

### Applied Review Methods

The queried scope is the same 20 starting Needs explicitly listed in the [release-preflight Change's Quality Review](release-contract-preflight.md#quality-review), plus `SYSP_DOC_PORTAL`, the newly added documentation Need. This release review concerns inventory, release-facing documentation and release gates; it does not repeat the product acceptance of every closed Change.

| Method | Selected scope and evidence | Findings and limits |
|---|---|---|
| Impact discovery | `get_need_links.py ID --direction both --depth 2 --flat --no-build` for all 21 starting Needs, using the built Needs from the recorded final documentation build; all queries succeeded | 86-object union. Discovery is candidate evidence, not an exhaustive filesystem scope or a release judgment. |
| Horizontal coverage | `analyze_mece.py ID --scope same-document` for all 21; all queries succeeded with no structural findings. Exact documentation peer group is the prior 11-document group plus `SYSP_DOC_PORTAL`; Release Contract ACs `_1`, `_2`, `_3` remain each other's peers; other starting objects have no same-document peers | The portal owns Syspilot's rendered entry point, distinct from README, guides and the adopter's generated neutral index. Empty peer sets and unavailable structured coverage data remain limits; complete semantic peer review is deferred to the replacement-candidate review. |
| Relationship analysis | `analyze_trace.py ID --direction both --depth 2` for all 21; all queries succeeded with no structural findings. The examined neighborhood is the prior Quality Review's explicitly enumerated 85-object union plus `SYSP_DOC_PORTAL` | Release/Admin, shared-Contract and Setup authority boundaries informed QI-1 to QI-3. Complete resolved-neighbor semantic review remains open; structural success does not establish semantic consistency, platform execution or publication. |

These are preliminary analysis results, not a completed semantic clearance. Re-review must assess the replacement P, final evidence, remaining semantic coverage and the complete P-to-R diff before publication.

### Open Quality Issues

Quality maintains this table, routes issues to artifact owners and removes rows only after confirmation. At publication it contains None.

| Artifact | Current issue | Required outcome |
|---|---|---|
| Preflight and protected preparation record (Release) | QI-1: protected Version/Inventory statuses and Objective wording are not final; `8fcb53b` also introduces a non-record change after P | Finalize protected preparation content, commit the corrected candidate including current development changes, select a new P and pass all four local checks there; obtain Quality re-review. |
| Triggered hosted validation (Release) | QI-2: triggers 1 and 2 fired, but the required validation-only run has neither authorization nor a result | Obtain and record explicit User authorization naming the validation-only run before pushing its branch; record a successful run of the replacement P. Main/tag publication authorization remains separate. |
| Infrastructure artifact status (Admin) | QI-3: Admin's completed section and handoff disagree with the pending artifact-table row | Admin confirmed through consultation that its row requires an owner update, not a Release edit on its behalf. Release hands the Contract to Admin to synchronize that row against `ecc8b2e`, then receives it back before the next gate. |

## Publication

**Status:** pending

Follow the canonical Release Process. Release start does not authorize publication.

1. After preflight and Quality proceed, obtain explicit User authorization for pushing main and v0.10.0, acknowledging local-versus-Linux evidence and the accepted partial-publication risk. Commit that authorization in this record on development before creating R.
2. Merge development into main as R. Run `uv run python scripts/check_release_record.py {preflighted commit} {release commit} v0.10.0`; Quality reviews the full record diff before any push. A failed check/review stops publication.
3. Push main, tag R v0.10.0 and push the tag only with the recorded authorization.
4. Watch validation, build/tests, Pages deployment and GitHub Release creation to completion. Verify release text and published documentation version.

Validation/build failure prevents publication. Failure after Pages deployment can leave partial publication. Stop, record and escalate failures; do not move/delete a tag or force-push without explicit User decision.

| Evidence | Value |
|---|---|
| Preflighted commit P | 5637fa41d6055e2287d0dbb64057061d2ef97c3f |
| Release commit on main R | pending |
| User authorization to push main and the tag | Not granted |
| Tag | v0.10.0 (not created) |
| Workflow run | pending |
| GitHub Release | pending |
| Pages URL | https://enthali.github.io/syspilot/index.html (deployment not verified for this release) |

## Closure

**Status:** pending

- [ ] Every included artifact/gate has terminal status and evidence.
- [ ] Preflight and release-record checks passed; Quality reviewed the complete record diff.
- [ ] Quality recorded proceed.
- [ ] Open Quality Issues contains None.
- [ ] Publication evidence is recorded.
- [ ] Current blocker is none.

**Final outcome:** pending
