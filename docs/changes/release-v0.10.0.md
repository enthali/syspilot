# Release Contract: 0.10.0

**Status:** approved<br>
**Process owner:** Release<br>
**Current responsibility:** Technical Writer<br>
**Current blocker:** none<br>
**Created:** 2026-11-10<br>
- **Operation Mode:** user-guided

- **user-guided** - every actor involves the user in its decision-making before proceeding.

## Handover log

The handing-over actor appends one line immediately before handing over, in the same commit that changes Current responsibility, using the observed local date and time. Evidence stays in the corresponding sections; the header is authoritative.

| Date | Time | From | To | Note |
|---|---|---|---|---|
| 2026-11-10 | 11:54 | Project Manager | Release | User approved release start in user-guided mode; preparation can begin. |
| 2026-11-10 | 11:58 | Release | Technical Writer | Inventory verified, v0.10.0 release notes written; user-facing documentation check next. |

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
| Preflight | yes | Release | Four local checks on P; triggered CI validation separately authorized | pending |
| Release notes | yes | Release | One v0.10.0 heading covers all included Changes | complete: single `## v0.10.0` heading with 20 entries in integration order and known limitations; `check_release_version.py v0.10.0` passes |
| User-facing documentation | yes | Technical Writer | Release-accuracy review in progress; User-approved portal/shared-Contract wording corrections, documentation-map coverage and Release-owned Setup-note correction | in progress |
| Infrastructure impact | yes | Admin | Workflow inputs, environment baseline and revalidation assessment | pending |
| Release verification | yes | Quality | Independent proceed and no open issue | pending |
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

**Status:** pending

**Preflighted commit P:** pending

Commit release notes and release-facing documentation before choosing P. Apply the canonical Release Process's protected-record and revalidation rules.

1. `uv run python docs/test_docs_build.py -v`
2. `uv run python docs/docs-build.py clean`
3. `uv run python -m unittest discover -s tests -v`
4. `uv run python scripts/check_release_version.py v0.10.0`

The strict build needs network access to docs.python.org. Local success does not prove execution on Linux or publication.

| Check | Command and commit | Result |
|---|---|---|
| Pending | Pending | pending |

### Revalidation triggers

Admin records the trigger paths/environment comparison against the last successful tag-run baseline; Release decides sufficiency. Use the canonical trigger conditions, including its bounded release-notes exception. No successful current-workflow baseline has yet been established in this record.

| Trigger | Observable test | Fired |
|---|---|---|
| Workflow input changed | Compare canonical trigger inputs against the last successful tag-run commit | pending |
| Environment change | Admin statement against prior runner/tool baseline | pending |
| No tag-run evidence | Verify evidence for the preceding release | pending |

| Validation-only run | Authorization | Result |
|---|---|---|
| Pending trigger assessment | Not granted | pending |

## Release Notes

**Status:** pending

Release is the only writer of docs/releasenotes.md. Cover the verified inventory in integration order, explaining user value and limitations.

## User-Facing Documentation

**Status:** in progress

The User approved the release-accuracy check and requesting the Setup-note correction from Release on 2026-11-10. After reviewing the findings, the User also approved correcting the portal and shared-Contract explanations, explicitly retaining Syspilot's experimental status while recognizing implemented Setup. These are explanations of existing released behavior, not new release scope or authorization to push.

Impact queries for `SYSP_REQ_RELEASE_CONTRACT` and `SYSP_REQ_SETUP` (both directions, depth 1, `--flat --no-build`) succeeded on 2026-11-10. The results identify candidate guides; the direct review also includes the rendered portal, documentation map, notes and all nine user-facing guides/README.

| Document | Required update | Evidence |
|---|---|---|
| `docs/index.rst` | Replace obsolete unimplemented-bootstrap/repository-preview claim with implemented release-bound Setup, keeping experimental-project framing and linking evidence limits | User approved; factual review/build pending |
| `docs/methodology.md` | Qualify tailoring by Contract kind: Release retains required headings and excludes unattended mode | Matches canonical Release and shared Contract Documents; factual review/build pending |
| `docs/product-model.md` | State that every Contract kind carries the Handover log, not Change alone | Shared Contract rule; factual review/build pending |
| `docs/syspilot/documentation/index.rst` | Add `SYSP_DOC_PORTAL` for the independently maintained rendered entry point; existing guide Needs/includes still cover their explanations | Map update; strict validation pending |
| `README.md`, `docs/getting-started.md`, `docs/customization.md`, `docs/change-contract.md`, `docs/operations.md`, `docs/branching.md`, `docs/upgrade.md` | Reviewed against v0.10.0 notes: current stack, ordinary-session Setup/Admin path, project-owned examples/ontology, authority, upgrade-to-0.10 guidance, four checks, bounded record review and partial-publication limits remain applicable; no edits needed | Source review complete; no runtime installation/publication claimed |
| `docs/releasenotes.md` (Release-owned) | Remove the new v0.10.0 entry's blanket unverified-installation claim; preserve reported-run versus deferred-scenario distinction from Operations | Release reports correction committed as `3d86026`; final source check pending |

## Infrastructure Impact

**Status:** pending

| Infrastructure artifact | Impact | Required action and evidence |
|---|---|---|
| .github/workflows/release.yml | Assess current workflow inputs and Linux revalidation triggers | Admin records findings; Release is mandatory consultee |

## Release Verification

**Status:** pending

**Current judgment:** pending

**Version and tag:** 0.10.0 / v0.10.0

Quality independently reviews Change closure, release-note coverage, documentation and preflight evidence and reports directly to Release. At R it reviews the complete P..R record diff: the checker covers protected blocks only; unprotected changes must remain evidence-only in substance, or require a new preflight. Actual push authorization must be present in R.

### Open Quality Issues

Quality maintains this table, routes issues to artifact owners and removes rows only after confirmation. At publication it contains None.

| Artifact | Current issue | Required outcome |
|---|---|---|
| Pending review | Pending | Pending |

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
| Preflighted commit P | pending |
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
