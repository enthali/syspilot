# Process Maintenance Example

Adopt and tailor this example explicitly before using it as authority in a project. It is separate from the source project's own processes: their maintenance follows the [Change process](../change.md), where the Needs graph covers specification Needs and their realization links, and Quality's recorded review verifies the Markdown content.

This example applies the [Contract Document method](../contract-documents.md) to a project's own Contract templates, process registry, role cards, and governing instructions and skills. The Admin maintains changed process documents; Quality supplies an independent comparison with their same-kind peers. A project adopting this example decides its paths, integration target, and approval arrangements before starting an instance.

## Process Definition

- **Applicability:** Maintenance of an adopting project's own process documents: Contract templates, process registry, role cards, and instructions and skills that govern those processes; enumerate the included paths in each instance.
- **Process owner:** Admin in the adopting project.
- **Canonical template:** The `Process Maintenance Contract: {NAME}` section below, at the project-approved location of this example's adopted copy.
- **Concrete instances:** `docs/changes/process-maintenance-{name}.md`, unless the adopting project explicitly selects another location.
- **Initial responsibility:** Project Manager, who settles the intent, affected documents, and approval arrangements with the User.
- **First handoff:** Admin, after the User approves `Contract release`.
- **Closure responsibility:** Project Manager.
- **Closure conditions:** The template's Closure checklist.

## Initialization And Handoffs

1. Tailor a copy of the canonical template at the agreed instance path; record intent, affected documents, applicable checks, and the agreed Operation Mode definition.
2. Present the instance to the User and ask the User to approve `Contract release`; artifact work starts after that gate is approved.
3. Commit the initialized instance and hand it to Admin. Admin consults each affected process owner and, for changed role cards, the actor whose domain the card describes. Admin records their responses, changes the included documents, and records the rationale and checks; consultation does not transfer current responsibility.
4. Hand the committed instance and artifacts to Quality for the peer comparison. Quality returns findings to the affected artifact owner for resolution, then reassesses them.
5. Quality communicates its `proceed` judgment and supporting evidence directly to the Project Manager. The Project Manager then presents the verified outcome to the User for validation and records the User's decision; Project Manager closes the instance after its checklist is satisfied.

Each handoff commits the current Contract state, its Handover log entry, and related artifacts before sending its path, commit, completed outcome, and remaining work. The receiving actor reads its context, role card, and Contract and verifies the committed `Current responsibility` before ACK.

## Manual Comparison Limits

Quality compares each affected document with peers of the same kind for overlapping or duplicated obligations, contradiction, missing coverage, and responsibility-boundary collisions. It records each peer set and reading in the review-methods table.

- The reviewer enumerates the peer set; a script does not discover it, because Needs-based analysis reads specification Needs rather than Markdown Contracts.
- A peer not listed by the reviewer is not examined.
- The judgment rests on a recorded reading; another reader may reach a different result.
- A clean result means nothing was found among the listed peers; it says nothing about documents outside that set.

Build, link, or schema checks support the review but do not establish semantic consistency. Record their commands and results separately from the reading-based judgment.

For a mechanical headings-and-fields inventory, substitute the selected peer paths in `git grep -n -E '^#{1,3} |^\*\*|^\|' -- '{peer-path-1}' '{peer-path-2}'`. Comparing this output can expose missing sections or fields cheaply; it does not establish consistency or replace the recorded reading. Record the actual paths, command, result, and limits as an automated supporting check.

## Canonical Template

# Process Maintenance Contract: {NAME}

**Status:** proposed | active | blocked | review | accepted | closed<br>
**Process owner:** Admin<br>
**Current responsibility:** Project Manager<br>
**Current blocker:** none | {needed decision or action}<br>
**Created:** {DATE}<br>
**Operation Mode:** {User-agreed mode as defined in the project's adopted [Change template](../change.md), and the specifics for this instance; tailor the link when adopting; User-owned gates remain User-owned}

## Handover log

Format owned by: Project Manager

The handing-over actor appends one line as the last act before handing over, in the same commit that changes `Current responsibility`, taking `Date` as `YYYY-MM-DD` and `Time` as `HH:MM` in 24-hour local time from the system clock at that moment. The handover goes to the next actor that follows from the logical flow of the Contract. The log explains transitions; the header stays authoritative.

| Date | Time | From | To | Note |
|--|--|--|--|--|

## Intent And Outcome

**Status:** draft | approved<br>
**Approval evidence:** {User decision and reference}

**Goal and value:** {What becomes true, for whom, and why?}

**Scope:** {Affected Contract templates, registry entries, role cards, and governing instructions and skills; enumerate the project-approved paths.}

**Observable outcome:** {Inspectable documents and evidence that demonstrate the intent.}

## Artifacts, Ownership And Process Gates

**Ownership:** This table states each included artifact or gate owner once; section headings name no artifact owner.<br>
**Scope change:** If intent widens after a row is terminal, return intent to `draft` for renewed approval; each affected owner reopens its row or records why its evidence remains applicable.

| Artifact or gate | Included | Owner | Completion evidence | Status |
|---|---|---|---|---|
| Intent and outcome | yes | Project Manager | Goal, scope, and observable outcome approved | draft / approved |
| Contract release | yes | User | Explicit authorization to start artifact work | pending / approved |
| Version control | yes | Project Manager | User-agreed integration target and integration commit recorded | pending / integrated |
| Changed process documents | yes | Admin | Included documents, rationale, applicable checks, and affected process-owner and described-actor consultations are linked | pending / complete |
| Quality review | yes | Quality | Each affected document compared with listed same-kind peers; findings resolved; current judgment `proceed` | pending / proceed / blocked |
| User validation | yes | User | Observable outcome accepted or changes requested | pending / accepted / changes requested |
| Closure | yes | Project Manager | Closure checklist satisfied | pending / complete |

## Version Control

**Status:** pending | integrated<br>
**Integration target:** {User-agreed repository and branch or other integration arrangement}<br>
**Working branch:** {branch, or not applicable with reason}<br>
**Integration evidence:** {integrated commit and target; do not claim integration before it exists}

## Changed Process Documents

**Status:** pending | in progress | complete

| Document | Change and rationale | Consultations | Check and evidence |
|---|---|---|---|
| {path} | {what changed and why} | {affected process owner; described actor for a role card; their responses and disposition} | {applicable build/link/schema command and result, or review evidence} |

## Quality Review

**Status:** pending | in progress | proceed | blocked<br>
**Current judgment:** {reasoned assessment of the currently valid documents and evidence}

### Applied Review Methods

| Method | Affected document and kind | Selected peer set | Evidence | Findings | Limits |
|---|---|---|---|---|---|
| Manual same-kind comparison: overlap/duplication, contradiction, coverage, responsibility boundaries | {path; template / registry / role card} | {explicit paths of every peer read} | {reviewed commit; recorded reading and reasoning for each comparison} | {issue references or no finding} | Reviewer-enumerated peers, not script-discovered; unlisted peers unexamined; reading-based judgment may differ between readers; clean result covers listed peers only |
| Automated supporting checks | {paths} | {not applicable: command scope} | {command, commit, exit status, result} | {failures or no finding} | {what the command does and does not establish} |

Enumerate peers for every affected document, explain same-kind selection, and explicitly record when none are found. Needs-based tools do not discover Markdown peers. The semantic comparison retains all four limits stated above even if supporting checks pass.

### Open Findings

Keep only current findings; resolve each through its artifact owner, and let Quality confirm the outcome. An unresolved finding keeps the judgment `blocked`.

| Artifact | Current issue | Required outcome |
|---|---|---|
| {path} | {observable issue} | {checkable resolution} |

## User Validation

**Status:** pending | accepted | changes requested<br>
**Decision and evidence:** {User's decision on the observable outcome and its reference; a review judgment does not replace this decision}

## Closure

**Status:** pending | complete

- [ ] Intent is approved and Contract release is approved.
- [ ] Every included changed document has completion evidence.
- [ ] Affected process-owner and described-actor consultations are recorded and addressed.
- [ ] Quality recorded the peer sets, reading evidence, findings, and all four limits.
- [ ] Quality's current judgment is `proceed` and Open Findings contains `None`.
- [ ] The User accepted the observable outcome.
- [ ] Every included row is terminal and the current blocker is `none`.
- [ ] The integration commit and User-agreed integration target are recorded.
- [ ] The final Contract state and owned artifacts are committed together.

**Final outcome:** {accepted outcome and integrated commit, or reason closure remains blocked}