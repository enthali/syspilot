# Release Contract: 0.10.0

**Status:** proposed<br>
**Process owner:** Release<br>
**Current responsibility:** Project Manager<br>
**Current blocker:** User agreement on Operation Mode and Release start<br>
**Created:** 2026-11-10<br>
- **Operation Mode:** pending User selection

## Handover log

The handing-over actor appends one line immediately before handing over, in the same commit that changes Current responsibility, using the observed local date and time. Evidence stays in the corresponding sections; the header is authoritative.

| Date | Time | From | To | Note |
|---|---|---|---|---|

## Objective And Scope

**Status:** draft<br>
**Approval evidence:** The User requested preparing the 0.10 release on 2026-11-10; release-start approval remains pending.

### Objective

Publish Syspilot v0.10.0: the v2 Contract-driven source release, with project-owned Actor and Contract examples, ontology-aware skills, pristine Setup and its feedback corrections, user documentation and the revised release process. The deliverable is the source state on main and its version tag, rendered documentation and GitHub Release, not an installer package.

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
| Objective and scope | yes | Project Manager | Objective, included Changes and limits approved | draft |
| Release start | yes | User | Explicit authorization to start, not permission to push | pending |
| Change inventory | yes | Release | Integrated Changes closed; Example sync verified or justified | pending |
| Version | yes | Release | Tag, newest release-note heading and documentation agree | pending |
| Preflight | yes | Release | Four local checks on P; triggered CI validation separately authorized | pending |
| Release notes | yes | Release | One v0.10.0 heading covers all included Changes | pending |
| User-facing documentation | yes | Technical Writer | Release-accurate guidance and limitations | pending |
| Infrastructure impact | yes | Admin | Workflow inputs, environment baseline and revalidation assessment | pending |
| Release verification | yes | Quality | Independent proceed and no open issue | pending |
| Publication | yes | Release | Explicit push authorization, main/tag, successful workflow, Pages and GitHub Release verified | pending |
| Closure | yes | Release | Closure checklist and publication evidence complete | pending |

## Change Inventory

**Status:** pending

Release verifies the candidates above, closure and Example sync, and records the final inventory here before P. No prior-release commit is included merely because it appears in branch history.

| Change | Integrated commit | Contract closed | Example sync |
|---|---|---|---|
| Pending Release verification | Pending | pending | pending |

## Version

**Status:** pending

**Version:** 0.10.0 - User-requested v2 minor release.

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

**Status:** pending

| Document | Required update | Evidence |
|---|---|---|
| Pending Technical Writer assessment | Check release/version consistency and honest limits | pending |

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
