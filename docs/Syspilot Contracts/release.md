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

The handing-over actor appends one line as the last act before handing over, in the same commit that changes `Current responsibility`, taking `Date` as `YYYY-MM-DD` and `Time` as `HH:MM` in 24-hour local time from the system clock at that moment. The handover goes to the next actor that follows from the logical flow of the release. The log explains transitions; the header stays authoritative.

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
| Change inventory | yes | Release | Every included Change Contract is closed and integrated into `development` | pending / complete |
| Version | yes | Release | The version is the tag under SemVer; the tag form and the release-notes heading agree | pending / complete |
| Preflight | yes | Release | Documentation build tests, strict clean documentation build, release QA suites, the automated version check, and a validation-only run of the release workflow pass on the preflighted commit, with commands and results recorded | pending / passed / failed |
| Release notes | yes | Release | `docs/releasenotes.md` holds exactly one heading for the version and covers every included Change | pending / complete |
| User-facing documentation | yes / not applicable: {reason; delete the corresponding empty section} | Technical Writer | User-facing documentation describes what this release ships, including its version | pending / complete / not applicable |
| Infrastructure impact | yes / not applicable: {reason; delete the corresponding empty section} | Admin | The release workflow validates, publishes, and creates the release for everything this release ships | pending / complete / not applicable |
| Release verification | yes | Quality | Quality reviewed the recorded preflight commands and results; current judgment is `proceed` and no open quality issue remains | pending |
| Publication | yes | Release | `main` and the tag pushed with the User's recorded authorization, the release workflow succeeded, and the GitHub Release and the published documentation at its Pages URL show the version | pending / published |
| Closure | yes | Release | Closure checklist complete | pending |

## Change Inventory

**Status:** pending | complete

A Change is release-ready when its Change Contract is closed. Including a Change whose Contract is still open requires a User decision recorded here.

| Change | Integrated commit | Contract closed |
|---|---|---|
| {change} | {sha} | yes / no |

## Version

**Status:** pending | complete

Semantic versioning. The version of a release is its tag, which has the form `vMAJOR.MINOR.PATCH`; `.github/workflows/release.yml` rejects any other form. `docs/releasenotes.md` holds exactly one heading `## v{version}` or `## v{version} - {title}`, which the workflow publishes as the GitHub Release text.

**Version:** {version} - {reason}

## Preflight

**Status:** pending | passed | failed

Run in order on the preflighted commit, which is the `development` commit to be released, and stop at the first failure, before `main` or a tag moves. The release notes in `docs/releasenotes.md` and the release-facing documentation are committed on `development` before the preflight, because check 4 reads the release-notes heading and the tree check in Publication step 1 compares the release commit with this commit; any later commit on `development` needs a new preflight.

1. `uv run python docs/test_docs_build.py -v`
2. `uv run python docs/docs-build.py clean`, which builds strictly with zero warnings
3. `uv run python -m unittest discover -s tests -v`
4. `uv run python scripts/check_release_version.py v{version}`, the automated version check, which verifies the tag form `vMAJOR.MINOR.PATCH` and exactly one release-notes heading for the version and writes nothing; the release workflow otherwise checks both only after the tag is pushed
5. A validation-only `workflow_dispatch` run of `release.yml` on a pushed branch of the preflighted commit, which never publishes. It exercises the `validate` and `build-docs` jobs; tag validation, release-notes extraction, documentation publication, and release creation run only on a tag push, so a passing run does not show that publication works. Pushing the branch is the one exception to keeping feature branches local and requires the User's explicit authorization, recorded in the row

| Check | Command and commit | Result |
|---|---|---|
| {check} | {command} @ {sha} | pass / fail: {failing item} |

A failure becomes a row in Open Quality Issues and responsibility goes to the owner of the affected artifact.

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

Quality verifies independently that every included Change is closed and represented in the release notes, that release-facing documentation describes the release honestly, and that the preflight evidence is complete and current. Quality reviews the recorded commands and results and executes a check itself only when a recorded result cannot support its judgment, recording the reason here. Quality communicates its judgment directly to Release.

### Open Quality Issues

Keep this table synchronized with currently open issues. For each issue, Quality transfers current responsibility to the owner of the affected artifact. When Quality confirms the required outcome, remove the row. At publication this table contains `None`.

| Artifact | Current issue | Required outcome |
|---|---|---|
| {artifact} | {observable issue} | {positive condition needed for proceed} |

## Publication

**Status:** pending | published

Publish only when `Release verification` is `proceed` and Open Quality Issues is `None`.

1. Merge `development` into `main` as the release commit, then verify that the release commit carries the tree of the preflighted commit (`git diff --quiet {preflighted commit} main` exits 0). A difference means the preflight did not cover the release commit and stops the release.
2. Record the User's explicit authorization to push `main` and the tag in the table below. `Release start` authorizes starting the release and does not authorize the push.
3. Push `main` first, then tag that release commit `v{version}` and push the tag. The tag sits only on the release commit on `main`, because `release.yml` publishes any pushed tag of the form `v*.*.*`. The workflow's own validation and documentation build then run on the tagged commit, after the push, and do not replace the preflight.
4. Watch `release.yml` to completion: validation, strict documentation build with the QA suites, documentation publication, and the GitHub Release.
5. Verify that the GitHub Release text is the version's release-notes entry and that the published documentation at its Pages URL shows the version.

If `release.yml` fails after the tag is pushed, stop, record the failure as the Contract's blocker, and escalate to the User. The tag stays where it is; moving or deleting it and any force-push need the User's explicit decision, and the usual fix is a new patch version.

| Evidence | Value |
|---|---|
| Preflighted commit | {sha} |
| Release commit on `main` | {sha} |
| User authorization to push `main` and the tag | {reference} |
| Tag | v{version} |
| Workflow run | {link or id} |
| GitHub Release | {link} |
| Pages URL | {link} |

## Closure

**Status:** pending | closed

- [ ] Every included artifact or gate has terminal status and completion evidence.
- [ ] Preflight passed on a commit whose tree equals the release commit's tree.
- [ ] Quality has recorded `proceed`.
- [ ] Open Quality Issues contains `None`.
- [ ] Publication evidence is recorded.
- [ ] Current blocker is `none`.

**Final outcome:** {published version and workflow run}
