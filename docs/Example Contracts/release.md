# Release Process

Use this process for every publication of a release of this project. A release takes a state of `{integration branch}` whose Changes are already closed and makes it public. Publication is irreversible: pushing a `{tag form}` tag on `{release branch}` triggers `{publication workflow}`, which publishes `{publication target}`. Everything this process checks is therefore true before the tag is pushed. The Release actor owns this process and its canonical template. Tailor every `{...}` value to the project when adopting this example.

This process applies the [Contract Documents](contract-documents.md) method. The canonical Release Contract template lives here. A concrete release starts as a tailored copy at `docs/changes/release-v{version}.md`, next to the Change Contracts it ships.

## Process Definition

- **Applicability:** Every publication of a project version, meaning every promotion of `{integration branch}` to `{release branch}` together with a version tag.
- **Canonical template:** The `Canonical Release Contract Template` section in this document.
- **Concrete instances:** `docs/changes/release-v{version}.md`.
- **Initial responsibility:** Project Manager, who creates the Release Contract, completes its objective and scope, and prepares it for the User-owned `Release start` gate.
- **First handoff:** Release.
- **Closure responsibility:** Release.
- **Closure conditions:** The checklist in the template's `Closure` section.

Release work starts only after the User sets the `Release start` gate to `approved`. The preflight is the final check before publication: when it passes and Quality has recorded `proceed`, Release publishes. When the preflight fails, Release records the failure as an open quality issue and transfers responsibility to the owner of the affected artifact; the release continues once the issue is resolved.

## Release Contract Initialization

The Project Manager initializes a release as one consistent version-controlled state on `{integration branch}`:

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
| Change inventory | yes | Release | Every included Change Contract is closed and integrated into `{integration branch}` | pending / complete |
| Version | yes | Release | The version is the tag under the project's versioning scheme; the tag form and the release-notes heading agree | pending / complete |
| Preflight | yes | Release | The project's build, test, and version checks, and a validation-only run of the publication workflow, pass on the preflighted commit, with commands and results recorded | pending / passed / failed |
| Release notes | yes | Release | `{release notes file}` holds exactly one heading for the version and covers every included Change | pending / complete |
| User-facing documentation | yes / not applicable: {reason; delete the corresponding empty section} | Technical Writer | User-facing documentation describes what this release ships, including its version | pending / complete / not applicable |
| Infrastructure impact | yes / not applicable: {reason; delete the corresponding empty section} | Admin | The publication workflow validates and publishes everything this release ships | pending / complete / not applicable |
| Release verification | yes | Quality | Quality reviewed the recorded preflight commands and results; current judgment is `proceed` and no open quality issue remains | pending |
| Publication | yes | Release | `{release branch}` and the tag pushed with the User's recorded authorization, the publication workflow succeeded, and `{publication target}` shows the version | pending / published |
| Closure | yes | Release | Closure checklist complete | pending |

## Change Inventory

**Status:** pending | complete

A Change is release-ready when its Change Contract is closed. Including a Change whose Contract is still open requires a User decision recorded here.

| Change | Integrated commit | Contract closed |
|---|---|---|
| {change} | {sha} | yes / no |

## Version

**Status:** pending | complete

Semantic versioning is the default; replace it with the project's scheme if it differs. The version of a release is its tag, which has the form `{tag form}`; `{publication workflow}` rejects any other form. `{release notes file}` holds exactly one heading for the version, which the workflow publishes as the release text.

**Version:** {version} - {reason}

## Preflight

**Status:** pending | passed | failed

Run in order on the preflighted commit, which is the `{integration branch}` commit to be released, and stop at the first failure, before `{release branch}` or a tag moves. The release notes and the release-facing documentation are committed on `{integration branch}` before the preflight, because the version check reads the release-notes heading and the tree check in Publication step 1 compares the release commit with this commit; any later commit on `{integration branch}` needs a new preflight.

1. `{documentation build check command}`
2. `{strict documentation build command}`, which builds with zero warnings
3. `{test suite command}`
4. `{version check command} {tag form}`, the automated version check, which verifies the tag form and exactly one release-notes heading for the version and writes nothing; the publication workflow otherwise checks both only after the tag is pushed
5. A validation-only run of `{publication workflow}` on a pushed branch of the preflighted commit, which never publishes. A passing run does not show that publication works, because tag validation and publication run only on a tag push. Pushing the branch is the one exception to keeping feature branches local and requires the User's explicit authorization, recorded in the row

| Check | Command and commit | Result |
|---|---|---|
| {check} | {command} @ {sha} | pass / fail: {failing item} |

A failure becomes a row in Open Quality Issues and responsibility goes to the owner of the affected artifact.

## Release Notes

**Status:** pending | complete

Release is the only writer of `{release notes file}`. Add one entry per included Change, in integration order, stating what changed and why it matters to a user.

## User-Facing Documentation

**Status:** pending | complete | not applicable

| Document | Required update | Evidence |
|---|---|---|
| {path} | {what this release makes true or false in it} | {commit or review result} |

## Infrastructure Impact

**Status:** pending | complete | not applicable

| Infrastructure artifact | Impact | Required action and evidence |
|---|---|---|
| `{publication workflow}` | {new or removed publication target, permission, or build step} | {action and evidence; Release is mandatory consultee} |

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

1. Merge `{integration branch}` into `{release branch}` as the release commit, then verify that the release commit carries the tree of the preflighted commit (`git diff --quiet {preflighted commit} {release branch}` exits 0). A difference means the preflight did not cover the release commit and stops the release.
2. Record the User's explicit authorization to push `{release branch}` and the tag in the table below. `Release start` authorizes starting the release and does not authorize the push.
3. Push `{release branch}` first, then tag that release commit with the version in `{tag form}` and push the tag. The tag sits only on the release commit on `{release branch}`, because `{publication workflow}` publishes any pushed tag of the form `{tag form}`. The workflow's own validation then runs on the tagged commit, after the push, and does not replace the preflight.
4. Watch `{publication workflow}` to completion.
5. Verify that the published release text is the version's release-notes entry and that `{publication target}` shows the version.

If `{publication workflow}` fails after the tag is pushed, stop, record the failure as the Contract's blocker, and escalate to the User. The tag stays where it is; moving or deleting it and any force-push need the User's explicit decision, and the usual fix is a new patch version.

| Evidence | Value |
|---|---|
| Preflighted commit | {sha} |
| Release commit on `{release branch}` | {sha} |
| User authorization to push `{release branch}` and the tag | {reference} |
| Tag | {tag form} |
| Workflow run | {link or id} |
| Published release | {link} |
| Publication target | {link} |

## Closure

**Status:** pending | closed

- [ ] Every included artifact or gate has terminal status and completion evidence.
- [ ] Preflight passed on a commit whose tree equals the release commit's tree.
- [ ] Quality has recorded `proceed`.
- [ ] Open Quality Issues contains `None`.
- [ ] Publication evidence is recorded.
- [ ] Current blocker is `none`.

**Final outcome:** {published version and workflow run}
