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
| Preflight | yes | Release | The project's build, test, and version checks pass on the preflighted commit, with commands, commit, and results recorded; a validation-only workflow run is recorded only when a revalidation trigger fired | pending / passed / failed |
| Release notes | yes | Release | `{release notes file}` holds exactly one heading for the version and covers every included Change | pending / complete |
| User-facing documentation | yes / not applicable: {reason; keep the section with status `not applicable`} | Technical Writer | User-facing documentation describes what this release ships, including its version | pending / complete / not applicable |
| Infrastructure impact | yes / not applicable: {reason; keep the section with status `not applicable`} | Admin | The publication workflow validates and publishes everything this release ships | pending / complete / not applicable |
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

Semantic versioning is the default; replace it with the project's scheme if it differs. The version of a release is its tag, which has the form `{tag form}`; `{publication workflow}` rejects any other form. The newest version heading in `{release notes file}` is the version source. `{documentation configuration}` derives its release metadata from that heading; exactly one heading matches the version. The same checker verifies the tag, heading, and documentation metadata in preflight and in the tag-triggered workflow, which publishes that entry as the release text.

**Version:** {version} - {reason}

This section, the `Change Inventory`, and the `Objective And Scope` section are final before the preflight: they are protected content, and the record comparison in Publication fails on any change to them after the preflighted commit.

## Preflight

**Status:** pending | passed | failed

Run in order on the preflighted commit P, which is the `{integration branch}` commit to be released, and stop at the first failure, before `{release branch}` or a tag moves. The release notes, version heading, and user-facing documentation are committed on `{integration branch}` before the preflight, because the version check reads the heading and Publication compares the release commit R with P. Any difference between P and R other than this release record needs a new preflight on the new commit.

**Preflighted commit P:** {sha}

The list below is protected content: it does not change after P.

1. `{documentation build check command}`
2. `{strict documentation build command}`, which builds with zero warnings
3. `{test suite command}`
4. `{version check command} {tag form}`, the automated version check, which verifies the tag form, exactly one matching heading that is also the newest version heading, and consistent documentation release metadata, and writes nothing; the tag-triggered workflow runs the same check

**Build-time network requirements:** {external inventories or other resources needed by the strict build, or none; record an unavailable resource as an environment failure, not a content failure}

| Check | Command and commit | Result |
|---|---|---|
| {check} | {command} @ {sha} | pass / fail: {failing item} |

A failure becomes a row in Open Quality Issues and responsibility goes to the owner of the affected artifact.

### What local evidence does not show

Local preflight does not prove execution on the publication workflow's platform. Differences such as path case, line endings, or tools available only on the runner may fail first after the tag exists, and publication is not exercised. The User's authorization in Publication acknowledges this trade-off. Publication follows successful validation and build, so failed prerequisites publish nothing. A later failure can leave a partial publication, for example when `{publication target}` was updated but the release was not created. Publication is not atomic; the failure path in Publication handles that outcome.

### Revalidation triggers

At release start Release reviews the Admin's Infrastructure Impact statement and decides whether the project's trigger path list and environment-change comparison are sufficient. Record the concrete inputs below when adopting this example; an earlier successful run is not assumed to cover future releases.

**Trigger path list:** {workflow definition, version checker, dependency and lock files, files fixing language and documentation-tool versions, and every file read by the documentation configuration}

Except `{release notes file}` from that list: it changes with every release, and the version checker verifies its heading format. This exception holds only while release-heading parsing stays in the checker behind `{version check command}` and in `{documentation configuration}`; a file that takes over that parsing joins the trigger list.

**Environment-change comparison:** {observable comparison with the last successful tag run's baseline, including floating runner images and resolved dependencies; state inputs that cannot be compared}

A validation-only run of `{publication workflow}` on a pushed branch of P is required only when a trigger below fired. It must not publish. State which validation and build jobs it exercises; a passing run does not prove tag-only validation or publication. Pushing the branch requires the User's explicit authorization naming the run, recorded before the push.

| Trigger | Observable test | Fired |
|---|---|---|
| Workflow input changed | `git diff --name-only {last tag-run commit} P -- {trigger path list}` | yes / no |
| Environment change | Admin's recorded environment-change comparison with the last tag-run baseline | yes / no |
| No tag-run evidence | No successful tag-triggered run of the immediately preceding release | yes / no |

| Validation-only run | Authorization | Result |
|---|---|---|
| {run id, or not required} | {User authorization reference, or not required} | {result and exercised jobs} |

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

**Version and tag:** {version} / {tag form} (protected content: not changed after the preflighted commit)

Quality verifies independently that every included Change is closed and represented in the release notes, that release-facing documentation describes the release honestly, and that the preflight evidence is complete and current. Quality reviews the recorded commands and results and executes a check itself only when a recorded result cannot support its judgment, recording the reason here. Quality communicates its judgment directly to Release.

### Open Quality Issues

Keep this table synchronized with currently open issues. For each issue, Quality transfers current responsibility to the owner of the affected artifact. When Quality confirms the required outcome, remove the row. At publication this table contains `None`.

| Artifact | Current issue | Required outcome |
|---|---|---|
| {artifact} | {observable issue} | {positive condition needed for proceed} |

## Publication

**Status:** pending | published

Publish only when `Release verification` is `proceed` and Open Quality Issues is `None`.

1. Record the User's explicit authorization to push `{release branch}` and the tag in the table below, separately from `Release start`, which does not authorize a push. Commit it on `{integration branch}` after P and before the merge, changing only this record, so R contains it and the review in step 2 covers it. The authorization states that tests ran locally on the preparing platform only, that execution on the workflow's platform is first proven by the tag run, that a failed tag run is corrected by a new version and the tag is not moved, and, when a trigger fired, the validation-only run that precedes the push. This acknowledgement must be present in the record at R and is reviewed by Quality; it is not an append-only mechanism.
2. Merge `{integration branch}` into `{release branch}` as the release commit R, then verify the record rule with `{release-record check command} P R {tag form}`. The project-tailored checker reads committed state with `git`, writes nothing, exits 0 on success or 1 on failure, and begins its stderr diagnostic with the failing condition. P is an ancestor of R, and the difference from P to R is exactly `docs/changes/release-v{version}.md`, with no other file, rename, mode change, or deletion. The automated comparison of this record at P and R rejects changes to protected content: Operation Mode; the sections `Objective And Scope`, `Version`, and `Change Inventory`; the columns `Artifact or gate`, `Included`, and `Owner` of every artifact-table row; every cell of the rows `Objective and scope`, `Release start`, and `Version`; the list of preflight commands; and the version/tag text of `Release Verification`. The checker also fails if the record is absent at P or R, the full SHA of P is missing from an evidence row at R, the `**Version:**` line of its Version section disagrees with the tag's version or the newest release-notes heading, any second-level heading of the project's Release Contract template at R is missing (presence only, not order or content), or expected headings and rows read by the check are missing; it names a missing heading or changed protected block. Any failure stops the release. Header status, responsibility and blocker, Handover log, preflight results, Release Verification and Open Quality Issues, publication evidence, Closure, status/evidence cells of other rows, and narrative in unprotected sections may differ at R. This is bounded automation: it cannot detect changed procedures, failure rules or narrative in unprotected text, and does not prove evidence-only differences. Quality and Release must review the complete P-to-R diff before publication. A change that alters release content, a procedure or a failure rule is rejected or requires a new preflight and cannot inherit the earlier results.
3. Push `{release branch}` first, then tag R with the version in `{tag form}` and push the tag. The tag sits only on the release commit on `{release branch}`, because `{publication workflow}` publishes any pushed tag of the form `{tag form}`. The workflow's own validation and build then run on the tagged commit, after the push, and do not replace the preflight.
4. Watch `{publication workflow}` to completion.
5. Verify that the published release text is the version's release-notes entry and that `{publication target}` shows the version.
6. After the tag run, record evidence that cannot exist in R (R's commit, the tag, workflow run, published release, publication target and outcome) in a later commit changing only this record. It does not move the tag. After a successful tag run, also record its baseline below: run id, commit, runner image version, resolved dependency list, and language/build-tool versions. Admin's environment comparison for the next release reads this record rather than relying on an old run log remaining available.

If `{publication workflow}` fails after the tag is pushed, stop, record the failure as the Contract's blocker, and escalate to the User. This includes a partial publication in which a publication target was updated and a later job failed. The tag stays where it is; moving or deleting it and any force-push need the User's explicit decision, and the usual fix is a new patch version.

Recorded before R, in the commit of step 1 or earlier (P as its full SHA):

| Evidence | Value |
|---|---|
| Preflighted commit P | {sha} |
| User authorization to push `{release branch}` and the tag, with the acknowledgement above | {reference} |

Recorded after the tag, in the record-only commit of step 6:

| Evidence | Value |
|---|---|
| Release commit R on `{release branch}` | {sha} |
| Tag | {tag form} |
| Workflow run | {link or id} |
| Published release | {link} |
| Publication target | {link} |
| Tag-run baseline (run id, commit, runner image, resolved dependencies, language/build tools) | {baseline} |

## Closure

**Status:** pending | closed

- [ ] Every included artifact or gate has terminal status and completion evidence.
- [ ] Preflight passed on P, R differs from P only in this record with no change in protected content, and Quality and Release reviewed the complete P-to-R diff.
- [ ] Quality has recorded `proceed`.
- [ ] Open Quality Issues contains `None`.
- [ ] Publication evidence is recorded after the tag, including the tag-run baseline.
- [ ] Current blocker is `none`.

**Final outcome:** {published version and workflow run}
