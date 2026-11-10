# Release Process

Use this process for every publication of a Syspilot release. A release takes a state of `development` whose Changes are already closed and makes it public. Publication is irreversible: pushing a `vMAJOR.MINOR.PATCH` tag on `main` runs `.github/workflows/release.yml`, which publishes the documentation and then creates the GitHub Release. Everything this process checks is therefore true before the tag is pushed. The Release actor owns this process and its canonical template.

This process applies the [Contract Documents](contract-documents.md) method. The canonical Release Contract template lives here. A concrete release starts as a tailored copy at `docs/changes/release-v{version}.md`, next to the Change Contracts it ships.

## Process Definition

- **Applicability:** Every publication of a Syspilot version, meaning every promotion of `development` to `main` together with a version tag.
- **Canonical template:** The `Canonical Release Contract Template` section in this document.
- **Concrete instances:** `docs/changes/release-v{version}.md`.
- **Initial responsibility:** Project Manager, who creates the Release Contract, completes its objective and scope, and prepares it for the User-owned `Release start` gate.
- **First handoff:** Release.
- **Closure responsibility:** Release.
- **Closure conditions:** The checklist in the template's `Closure` section.

Release work starts only after the User sets the `Release start` gate to `approved`. The preflight is the final check before publication: when it passes and Quality has recorded `proceed`, Release publishes. When the preflight fails, Release records the failure as an open quality issue and transfers responsibility to the owner of the affected artifact; the release continues once the issue is resolved.

## Release Contract Initialization

The Project Manager initializes a release as one consistent version-controlled state on `development`:

1. Copy the canonical template from `# Release Contract: {VERSION}` through the end of this file to `docs/changes/release-v{version}.md`, using the intended version.
2. Select the agreed Operation Mode, remove the template note and the non-applicable mode rule, and complete the header, `Objective And Scope`, and the list of included Changes.
3. Ask the User to set the User-owned `Release start` gate to `approved`, and in that same step open the Contract document in the User's editor, because the User reviews it before deciding; no other actor may set the gate, and release work remains blocked until it reads `approved`.
4. Commit the initialized Release Contract.
5. Transfer current responsibility to Release.

## Canonical Release Contract Template

# Release Contract: {VERSION}

**Status:** proposed | approved | active | blocked | published | closed<br>
**Process owner:** Release<br>
**Current responsibility:** Project Manager<br>
**Current blocker:** none | {decision or action currently needed}<br>
**Created:** {DATE}<br>
- **Operation Mode**: autonomous | user-guided; select one with the User before `Release start`

*(Template note - delete this line and the non-applicable mode bullet once the mode is picked. A release ends in an irreversible publication, so it always runs with the User reachable and offers no unattended mode.)*

- **autonomous** - every actor decides on its own; when genuinely unsure, it asks the user directly and pauses only its own step until answered.
- **user-guided** - every actor involves the user in its decision-making before proceeding.

## Handover log

The handing-over actor appends one line as the last act before handing over, in the same commit that changes `Current responsibility`, taking `Date` as `YYYY-MM-DD` and `Time` as `HH:MM` in 24-hour local time from the system clock at that moment. The note states what the owner did and the facts that change the next owner's situation; evidence stays in the owner's section and remaining work in the open rows. The handover goes to the next actor that follows from the logical flow of the release. The log explains transitions; the header stays authoritative.

| Date | Time | From | To | Note |
|--|--|--|--|--|

## Objective And Scope

**Status:** draft | approved<br>
**Approval evidence:** pending | {evidence that the objective and scope are settled}

### Objective

{Why this release exists and what it makes available to users.}

### Included Changes

{The closed Change Contracts this release ships, in integration order.}

### Known Limitations

{Constraints that remain true in this release.}

## Artifacts, Ownership And Process Gates

**Applicability:** Each artifact owner decides and updates its own row.<br>
**Scope change:** When the approved objective or included Changes widen after a row reached a terminal status, `Objective and scope` returns to `draft` until it is approved again, and each owner whose terminal row the wider scope may affect reassesses it: the owner sets the row back to `pending` or records in the row why its evidence still holds.<br>
**Ownership:** The `Owner` column of this table is the only statement of artifact and gate ownership in the Contract; section headings name no artifact owner.<br>
**Status:** pending | complete

| Artifact or gate | Included | Owner | Completion evidence | Status |
|---|---|---|---|---|
| Objective and scope | yes | Project Manager | Objective, included Changes, and known limitations are explicit and approved | draft / approved |
| Release start | yes | User | User authorization to start the release; no other actor may set this gate | pending / approved |
| Change inventory | yes | Release | Every included Change Contract is closed and integrated into `development`, and its `Example sync` row reads `complete` or `not applicable` with a reason | pending / complete |
| Version | yes | Release | The version is the tag under SemVer; the tag form and the release-notes heading agree | pending / complete |
| Preflight | yes | Release | Documentation build tests, strict clean documentation build, release QA suites, and the automated version check pass on the preflighted commit, with commands, commit, and results recorded; a validation-only run of the release workflow is recorded only when a revalidation trigger fired | pending / passed / failed |
| Release notes | yes | Release | `docs/releasenotes.md` holds exactly one heading for the version and covers every included Change | pending / complete |
| User-facing documentation | yes / not applicable: {reason; keep the section with status `not applicable`} | Technical Writer | User-facing documentation describes what this release ships, including its version | pending / complete / not applicable |
| Infrastructure impact | yes / not applicable: {reason; keep the section with status `not applicable`} | Admin | The release workflow validates, publishes, and creates the release for everything this release ships | pending / complete / not applicable |
| Release verification | yes | Quality | Quality reviewed the recorded preflight commands and results; current judgment is `proceed` and no open quality issue remains | pending |
| Publication | yes | Release | `main` and the tag pushed with the User's recorded authorization, the release workflow succeeded, and the GitHub Release and the published documentation at its Pages URL show the version | pending / published |
| Closure | yes | Release | Closure checklist complete | pending |

## Change Inventory

**Status:** pending | complete

A Change is release-ready when its Change Contract is closed. Including a Change whose Contract is still open requires a User decision recorded here. Release verifies each Change's `Example sync` row here instead of merging example changes at the release; a Change whose Contract has no such row was closed before the row existed and records `no row`.

| Change | Integrated commit | Contract closed | Example sync |
|---|---|---|---|
| {change} | {sha} | yes / no | complete / not applicable: {reason} / no row |

## Version

**Status:** pending | complete

Semantic versioning. The version of a release is its tag, which has the form `vMAJOR.MINOR.PATCH`; `.github/workflows/release.yml` rejects any other form. `docs/releasenotes.md` holds exactly one heading `## v{version}` or `## v{version} - {title}`, which the workflow publishes as the GitHub Release text.

**Version:** {version} - {reason}

This section, the `Change Inventory`, and the `Objective And Scope` section are final before the preflight: they are protected content, and the record comparison in Publication fails on any change to them after the preflighted commit.

## Preflight

**Status:** pending | passed | failed

Run in order on the preflighted commit P, which is the `development` commit to be released, and stop at the first failure, before `main` or a tag moves. The release notes in `docs/releasenotes.md`, the version heading, and the user-facing documentation are committed on `development` before the preflight, because check 4 reads the release-notes heading and the record comparison in Publication compares the release commit R with P. Any difference between P and R other than this release record needs a new preflight on the new commit.

**Preflighted commit P:** {full sha}

The list below is protected content: it does not change after P.

1. `uv run python docs/test_docs_build.py -v`
2. `uv run python docs/docs-build.py clean`, which builds strictly with zero warnings
3. `uv run python -m unittest discover -s tests -v`
4. `uv run python scripts/check_release_version.py v{version}`, the automated version check, which verifies the tag form `vMAJOR.MINOR.PATCH`, exactly one release-notes heading for the version, and the consistency of the version with the documentation's version metadata, and writes nothing; the release workflow runs the same check after the tag is pushed

The strict build needs network access, because the documentation configuration fetches an external inventory from `docs.python.org`; in an environment without it the build fails for that reason and not for the content.

| Check | Command and commit | Result |
|---|---|---|
| {check} | {command} @ {sha} | pass / fail: {failing item} |

A failure becomes a row in Open Quality Issues and responsibility goes to the owner of the affected artifact.

### What local evidence does not show

The preflight does not run on the workflow's platform. Platform-specific failures such as path case, line endings, or tools installed only on the runner may appear first after the tag exists, and publication is not exercised. This trade-off is accepted, and the User's authorization in Publication acknowledges it. A failure of the validation or of the documentation build after the tag publishes nothing, because publication follows them. A failure after the documentation was published, as when the GitHub Release is not created after the Pages deployment, leaves a partial publication that the failure path in Publication handles; the User accepted that risk and publication is not atomic.

### Revalidation triggers

At the release start Release decides, as the mandatory consultee of the Admin's Infrastructure Impact statement, whether the trigger path list and the environment-change statement are sufficient, and records here whether a trigger fired. A validation-only `workflow_dispatch` run of `release.yml` on a pushed branch of P, which never publishes, is required only when a trigger fired. It exercises the `validate` and `build-docs` jobs; tag validation, release-notes extraction, documentation publication, and release creation run only on a tag push. Pushing the branch is the one exception to keeping feature branches local and requires the User's explicit authorization, which names the run and is recorded before the push.

| Trigger | Observable test | Fired |
|---|---|---|
| Workflow input changed | `git diff --name-only {last tag-run commit} P -- {trigger path list}`; the list names at least the workflow definition, the version checker, the dependency and lock files, the Python and Sphinx versions the workflow installs, and every file the documentation configuration reads, except `docs/releasenotes.md`, which changes with every release and whose heading format the automated version check verifies; this exception holds only while release-heading parsing stays in `scripts/check_release_version.py` and `docs/conf.py`, and a file that takes over such parsing joins the list | yes / no |
| Environment change | The Admin's recorded environment-change statement since the last successful tag run, compared with the baseline in the release record of that run | yes / no |
| No tag-run evidence | No successful tag-triggered run of the immediately preceding release | yes / no |

| Validation-only run | Authorization | Result |
|---|---|---|
| {run id, or not required} | {User authorization reference, or not required} | {result} |

## Release Notes

**Status:** pending | complete

Release is the only writer of `docs/releasenotes.md`. Add one entry per included Change, in integration order, stating what changed and why it matters to a user.

## User-Facing Documentation

**Status:** pending | complete | not applicable

| Document | Required update | Evidence |
|---|---|---|
| {path} | {what this release makes true or false in it} | {commit or review result} |

## Infrastructure Impact

**Status:** pending | complete | not applicable

| Infrastructure artifact | Impact | Required action and evidence |
|---|---|---|
| `.github/workflows/release.yml` | {new or removed publication target, permission, or build step} | {action and evidence; Release is mandatory consultee} |

## Release Verification

**Status:** pending | in progress | proceed | blocked

**Current judgment:** {holistic assessment}

**Version and tag:** {version} / v{version} (protected content: not changed after the preflighted commit)

Quality verifies independently that every included Change is closed and represented in the release notes, that release-facing documentation describes the release honestly, and that the preflight evidence is complete and current. Quality reviews the recorded commands and results and executes a check itself only when a recorded result cannot support its judgment, recording the reason here. Quality communicates its judgment directly to Release.

### Open Quality Issues

Keep this table synchronized with currently open issues. For each issue, Quality transfers current responsibility to the owner of the affected artifact. When Quality confirms the required outcome, remove the row. At publication this table contains `None`.

| Artifact | Current issue | Required outcome |
|---|---|---|
| {artifact} | {observable issue} | {positive condition needed for proceed} |

## Publication

**Status:** pending | published

Publish only when `Release verification` is `proceed` and Open Quality Issues is `None`.

1. Record the User's explicit authorization to push `main` and the tag in the table below, separately from `Release start`, which authorizes starting the release and not the push, and commit it on `development` as a commit that changes only this record, after P and before the merge, so that R contains it and the review in step 2 covers it. The authorization states that the tests ran locally on the preparing platform only, that execution on the workflow's platform is first proven by the tag run, that a failed tag run is corrected by a new version and the tag is not moved, and, when a trigger fired, the validation-only run that precedes the push. The acknowledgement must be present in the record at R; Quality's review protects it, and no append-only mechanism does.
2. Merge `development` into `main` as the release commit R, then verify the record rule with `uv run python scripts/check_release_record.py {preflighted commit} {release commit} v{version}`, which reads P and R from git and exits 0 or 1 with the failing condition first on stderr. It checks that P is an ancestor of R, that the difference from P to R is exactly `docs/changes/release-v{version}.md` (no other file, rename, mode change, or deletion), that the record is present at R, that the full SHA of P is present in the record at R, that the `Version` row equals the release-notes heading, that every second-level heading of the Release Contract template is present at R (presence only, not order or content, so that a deleted evidence section fails), that the template's headings and rows the check reads are found, and that the comparison of this record at P and at R finds no change in the protected content, naming the block that differs. The protected content is the Operation Mode, the sections `Objective And Scope`, `Version`, and `Change Inventory`, the columns `Artifact or gate`, `Included`, and `Owner` of every row of the artifact table, every cell of the rows `Objective and scope`, `Release start`, and `Version`, the list of preflight commands, and the version and tag text of `Release Verification`. Any failure means the preflight did not cover R and stops the release. The header status, responsibility and blocker, the Handover log, the preflight results, Release Verification and Open Quality Issues, the publication evidence, the Closure, the status and evidence cells of the other rows, and the narrative of the unprotected sections may differ at R. The check is bounded automation: it cannot see a changed procedure, failure rule, or narrative in unprotected text and does not prove that R differs from P only in evidence. Quality and Release therefore review the complete difference from P to R before publication, and a change that alters release content, a procedure, or a failure rule is rejected or receives a new preflight and does not inherit the old one.
3. Push `main` first, then tag R `v{version}` and push the tag. The tag sits only on the release commit on `main`, because `release.yml` publishes any pushed tag of the form `v*.*.*`. The workflow's own validation and documentation build then run on the tagged commit, after the push, and do not replace the preflight.
4. Watch `release.yml` to completion: validation, strict documentation build with the QA suites, documentation publication, and the GitHub Release.
5. Verify that the GitHub Release text is the version's release-notes entry and that the published documentation at its Pages URL shows the version.
6. After the tag run, record the evidence that cannot exist in R (R's commit, the tag, the workflow run, the GitHub Release, the Pages URL, the outcome) in a later commit that changes only this record. It does not move the tag. After a successful tag run, also record its baseline: run id, commit, runner image version, the resolved package list, and the `uv` and Python versions. The Admin's environment comparison for the next release reads this baseline, because the platform log of an old run does not stay available.

If `release.yml` fails after the tag is pushed, stop, record the failure as the Contract's blocker, and escalate to the User. This includes a partial publication, in which the documentation was published and a later job failed, for example when the GitHub Release is not created after the Pages deployment. The tag stays where it is; moving or deleting it and any force-push need the User's explicit decision, and the usual fix is a new patch version.

Recorded before R, in the commit of step 1 or earlier (P as its full 40-character SHA):

| Evidence | Value |
|---|---|
| Preflighted commit P | {sha} |
| User authorization to push `main` and the tag, with the acknowledgement above | {reference} |

Recorded after the tag, in the record-only commit of step 6:

| Evidence | Value |
|---|---|
| Release commit R on `main` | {sha} |
| Tag | v{version} |
| Workflow run | {link or id} |
| GitHub Release | {link} |
| Pages URL | {link} |
| Tag-run baseline (run id, commit, runner image, resolved packages, `uv` and Python) | {baseline} |

## Closure

**Status:** pending | closed

- [ ] Every included artifact or gate has terminal status and completion evidence.
- [ ] Preflight passed on P, R differs from P only in this record with no change in the protected content, and Quality and Release reviewed the complete difference from P to R.
- [ ] Quality has recorded `proceed`.
- [ ] Open Quality Issues contains `None`.
- [ ] Publication evidence is recorded after the tag, including the tag-run baseline.
- [ ] Current blocker is `none`.

**Final outcome:** {published version and workflow run}
