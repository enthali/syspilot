# Change Contract: Contract Authoring Governance

**Status:** closed<br>
**Process owner:** Syspilot Project Manager<br>
**Current responsibility:** Syspilot Project Manager<br>
**Current blocker:** none<br>
**Created:** 2026-08-28<br>
- **Operation Mode**: autonomous

- **autonomous** - every actor decides on its own; when genuinely unsure, it asks the user directly and pauses only its own step until answered.

## Intent And Outcome

**Owner:** Syspilot Project Manager<br>
**Status:** approved<br>
**Approval evidence:** The User's release is recorded in the `Contract release` gate row rather than here, so that a settled intent text and an authorization to start remain two separate statements with two different owners.

### Goals

1. Make a Change Contract state its own governance where every actor reads it: the operation mode and its complete behavioral rule live in the Contract instance, while the User's release remains a separate process gate with its own row and owner.
2. Make Contract tailoring local and concise: each tailoring option and its edit or delete instruction appear exactly where the choice is made in the process Contract template. Required elements offer no omission option. One Contract may bundle multiple goals and observable outcomes when they share one responsibility, release, validation, and integration boundary.

### Value

The Tailoring Rules attach different closure consequences to each named mode, but a selected name and link still require every actor to leave the active Contract to discover its operating rule. The Contract must remain independently readable during execution. Its template therefore carries all three complete mode rules; initialization retains the selected rule and removes the template note and two non-applicable rules.

The User's release is recorded twice, in the Intent's approval evidence and in a closure checkbox, and `Intent: approved` therefore asserts both that the text is settled and that the User authorized starting. Those have different owners, and conflating them once let a Contract in this project claim an approval that had not been given.

A separate generic Tailoring section plus a process-specific Tailoring Rules section makes an author navigate and combine rules before editing the template. The option is clearer and cheaper when the affected row or field carries its own selection and deletion instruction. Only the procedure for locating options and genuine whole-Contract invariants remain generic. Explicitly allowing related goals to share one Contract prevents artificial one-goal fragmentation without allowing unrelated decision boundaries to blur.

### Scope

- Replace the linked collaboration-mode field with an `Operation Mode` template block containing `user-guided (default) | autonomous | unattended` and the complete behavioral rule for each mode.
- During initialization, delete the template note and the two non-applicable mode bullets so the concrete Contract retains exactly one selected mode and its rule.
- Remove the generic mode definitions from `contract-documents.md`; operation-mode behavior is Change Contract-specific and is carried by the Change template and each concrete instance.
- Use the User-provided behavioral wording exactly, including `USER REVIEW REQUIRED`, the reversible KISS path for unattended uncertainty, PM review on return, and retained decision ownership.
- Delete process-specific Tailoring Rules sections. In `contract-documents.md`, retain only the procedure: each tailoring option is described at the specific section in the process Contract template where the choice is made.
- Put each option and its edit or delete instruction at the affected template field or row. Optional artifact rows record a reason and instruct the author to delete the corresponding empty owner section; required rows offer no omission option.
- Keep the shared responsibility, release, validation, and integration boundary for multiple goals as a general Contract composition invariant, not as a tailoring rule.
- Keep operation mode, Contract release, and finished-outcome validation independent. Autonomous mode alone does not delegate User validation; only an explicit User delegation recorded at the local validation row may make it `not applicable`. Unattended validation remains pending until the User returns.
- Rename the artifact table to name process gates alongside artifacts, and add `Contract release` as a User-owned row with `pending` and `approved`. No other actor may set it.
- Remove the resulting duplication: the closure checkbox and the release statement in the Intent's approval evidence both give way to the gate row, which the existing terminal-status closure condition already covers.
- Update the affected specification, process, template, and user-facing surfaces to state the revised rules consistently.
- Do not add an actor, workflow, or approval step beyond the behavior contained in the three operation-mode rules.
- Do not retrofit Contracts created from the previous template; conformance is a property of the template and of Contracts created from it.
- Do not push the public Syspilot repository without explicit User authorization.

### Observable Outcome

The canonical template presents all three operation modes with complete behavioral rules and instructs its author to retain only the selected mode in the concrete Contract. An actor can therefore determine how to proceed without following an external definition link. The artifact table names process gates in its heading and carries a User-owned `Contract release` row. The User's release appears in exactly one place, and `Intent: approved` no longer asserts it.

The Contract Documents method states only where tailoring options are found, while every concrete choice and editing instruction is present at the affected template location. No process-specific Tailoring Rules section remains. Required rows expose no omission option, optional rows record a reason and direct removal of the corresponding empty owner section, and the multiple-goal boundary remains a general Contract composition invariant. The strict documentation and schema build passes with zero warnings, and this Contract itself is filled in the resulting shape.

## Artifacts, Ownership And Process Gates

**Applicability:** Each artifact owner decides and updates its own row.<br>
**Status:** pending

This Contract is tailored into the shape it defines, as its predecessor `docs/changes/version-control-ownership.md` was. The canonical template does not yet carry the renamed heading or the gate row; until this Contract closes, that shape is this Change's own subject rather than the authoritative template.

| Artifact or gate | Included | Owner | Completion evidence | Status |
|---|---|---|---|---|
| Intent and outcome | yes | Syspilot Project Manager | Goal, value, scope, and observable outcome are explicit and coherent | approved |
| Contract release | yes | User | Released by the User on 2026-08-28 for autonomous execution; on the same date the User explicitly replaced the linked mode design with Contract-local `Operation Mode` rules and directed specification alignment; no other actor may set this row | approved |
| Version control | yes | Syspilot Project Manager | `feature/contract-gates-and-modes`, squash-integrated into `development` at closure | merged |
| Product specification and architecture decisions | yes | Syspilot Architect | Contract-local operation-mode rules, local tailoring options, the release gate, and removed duplication are specified consistently | complete |
| User-facing documentation | yes | Syspilot Technical Writer | Documentation impact is assessed from changed Requirements; applicable `doc` Needs state one authoritative rule | complete |
| Implementation and unit verification | yes | Syspilot Developer | Change Process tailoring choices are localized at their point of use, and the generic method separates tailoring location from Contract composition; executable-impact assessment and documentation verification are recorded | complete |
| Acceptance test design and results | yes | Syspilot Tester | Black-box scenarios demonstrate contract-local operation modes, local tailoring choices, independent release and validation controls, and removed duplication | passed |
| Quality review | yes | Syspilot Quality | Quality independently re-applied MECE and Trace after the User-directed revisions and recorded `proceed` with no open issue | proceed |
| User validation and approval | yes | User | The User accepts the operation-mode behavior, governance vocabulary, and release gate | accepted |
| Closure decision | yes | Syspilot Project Manager | Final outcome, validation disposition, and integration state are recorded | closed |

## Architecture And Specification

**Owner:** Syspilot Architect<br>
**Status:** complete

### Known Evidence

This table records the state observed when the Change began. It is the evidence that motivated the work and is deliberately not updated as the work proceeds; the currently valid changes are in `Affected Artifacts`.

| Source | Observation |
|---|---|
| `docs/Syspilot Processes/change.md`, template preamble | Collaboration mode is a free-text placeholder while `Status` uses a named value list |
| `docs/Syspilot Processes/change.md`, Tailoring Rules | Already attaches distinct consequences to user-guided, autonomous, and unattended by name |
| `docs/Syspilot Processes/contract-documents.md`, `## Collaboration Mode` | Holds the authoritative definitions of all three modes and governs processes beyond Change |
| `docs/Syspilot Processes/contract-documents.md`, `## Tailoring` | Already permits omission of tailorable artifacts with a recorded reason, but does not define when multiple goals share one Contract or whether empty owner sections remain |
| `docs/changes/mece-trace-skills.md` | Declared `Autonomous` and was executed unattended, which is the observable drift |
| `docs/Syspilot Processes/change.md`, closure checklist and Intent approval evidence | Record the User's release twice, in two different sections |

### Affected Artifacts

| Artifact | Change | Rationale |
|---|---|---|
| `SYSP_REQ_CONTRACT_DOCUMENTS` | modify | Defines owner-exclusive process gates, requires each tailoring option to be described where its choice is made, states the multiple-goal boundary as a Contract composition invariant, and defines no operation mode |
| `SYSP_VC_CONTRACT_DOCUMENTS_1` | modify | Makes those properties checkable, including that the method carries no central list of tailoring options and no mode definition |
| `SYSP_REQ_CHANGE_CONTRACT` | modify | Carries the `Operation Mode` field with the complete rule for all three modes and its reduction to one at initialization, keeps the User-owned `Contract release` gate as the sole start control, describes each tailoring option at its point of use while required elements offer none, and permits validation `not applicable` only through an explicit User delegation recorded at that row |
| `SYSP_VC_CHANGE_CONTRACT_1` | modify | Makes those Change-specific properties checkable, including the absence of a process-specific tailoring rules section |
| `docs/Syspilot Processes/contract-documents.md` | modify, Developer-owned | Holds no mode definition, retains owner-exclusive gates, reduces tailoring to the locality rule, and states the composition invariant outside tailoring |
| `docs/Syspilot Processes/change.md`, template preamble | modify, Developer-owned | Carries the User-authored `Operation Mode` block with the template note and the complete rule for each of the three modes |
| `docs/Syspilot Processes/change.md`, `Tailoring Rules` section | remove, Developer-owned | Every choice moves to the field, row, or section where it is made; requiredness survives as rows that offer no omission option |
| `docs/Syspilot Processes/change.md`, artifact table, Intent approval evidence, Closure checklist | modify, Developer-owned | Names process gates, carries the User-owned `Contract release` row, and records the release exactly once |
| `docs/Syspilot Processes/change.md`, `User validation and approval` row and section | modify, Developer-owned | Becomes `not applicable` only through an explicit User delegation recorded there; the operation mode never delegates it and `unattended` keeps it pending |
| `docs/Syspilot Processes/change.md`, initialization and start boundary | modify, Developer-owned | Selects the Operation Mode, removes the template note and the two non-applicable rules, and starts artifact work only when the gate reads `approved` |
| User-facing surfaces carrying `SYSP_REQ_CONTRACT_DOCUMENTS` or `SYSP_REQ_CHANGE_CONTRACT` | Technical Writer impact review | Both Requirements changed, so their documentation consumers require an owner assessment |

### Decisions And Evidence

| Decision or check | Evidence |
|---|---|
| Placement across two Requirements verified, not assumed | Exported links confirm `SYSP_REQ_CHANGE_CONTRACT` specializes `SYSP_REQ_CONTRACT_HANDLING`, which specializes `SYSP_REQ_CONTRACT_DOCUMENTS`, and that `SYSP_REQ_SETUP` specializes `SYSP_REQ_CONTRACT_DOCUMENTS` directly. Generic obligations therefore belong to Contract Documents so that Setup inherits them rather than diverging |
| The generic method contradicted the goal and had to change | `docs/Syspilot Processes/contract-documents.md` described the modes as "free text", "common examples", and "starting points rather than a closed set", which is why the Change could not simply point at that section. Superseded: the User later removed mode definitions from the generic method entirely, so it now defines no mode at all |
| Named modes are generic; their required use is Change-specific | Superseded and no longer in force. Mode behavior is Change Contract-specific: the generic method defines no mode, and each Change Contract carries the complete rule for all three modes in its own `Operation Mode` block |
| Process gate introduced generically | Without a generic concept, the Change Requirement would introduce an element that its own method does not define. The generic Requirement now defines a gate as a recorded element with exactly one owner who alone may set it |
| No approval step was added | The User's release already existed before this Change; it was then recorded twice, in the Intent's approval evidence and again in a closure checkbox. The gate relocated that single authorization into one owned row, so two statements became one and the Intent evidence now points at the gate |
| Observed drift, not hypothetical | `docs/changes/mece-trace-skills.md` declared `Autonomous` and was executed unattended. At that time the field was free text and mapped to none of the three consequence rules the Change process attached to the named modes |
| Multi-goal bundling boundary | One Contract may carry multiple goals and observable outcomes only when they share one responsibility, release, validation, and integration boundary. This Contract carries two goals under one authoring-governance boundary and is therefore the first instance the rule must accept |
| Duplication removed by the existing closure rule | The release gate is an included row, so the existing condition that every included artifact or gate carries a terminal status already enforces it. No new closure rule was added |
| RST robustness correction | An inline literal spanning a line break left ``Contract release`` non-contiguous in the exported Need content, so a text-based check would not have found it although the page rendered correctly. The bullet was reworded to keep the value on one line and the assertion now passes |
| Specification validation | `python docs/docs-build.py clean` passed with `Schema validation completed with 0 warning(s)` and `build succeeded`; `python docs/test_docs_build.py` passed 4/4; `git diff --check` passed |
| Traceability validation | Exported `needs.json` confirms `SYSP_VC_CONTRACT_DOCUMENTS_1` verifies `SYSP_REQ_CONTRACT_DOCUMENTS` and `SYSP_VC_CHANGE_CONTRACT_1` verifies `SYSP_REQ_CHANGE_CONTRACT`, and that the process-gate concept, the multiple-goal boundary, and the `Contract release` gate are present in the intended Requirement |
| Closure wording defect, mine | Introducing gates as table rows left the closure statements naming only artifacts, in the `SYSP_REQ_CHANGE_CONTRACT` closure bullet, in my own rationale sentence, and in `SYSP_VC_CHANGE_CONTRACT_1`. A gate could therefore be closed past on a literal reading, which contradicted my recorded reason for adding no new closure rule |
| Closure correction | All three statements now read `artifact or gate`. Verified on whitespace-normalized exported content: `all included artifacts and gates have terminal status`, `every included artifact or gate carries a terminal status`, `checkable Closure for every included artifact or gate`, and no remaining artifact-only closure statement |
| Generic closure wording checked, not widened | `SYSP_REQ_CONTRACT_DOCUMENTS` states only that a process declares its closure conditions and contains no terminal-status statement, so the same literal gap does not exist there and no change was made |
| Tester finding on a second definition surface accepted | `docs/methodology.md` reproduced all three mode meanings in a table and then stated that those definitions lived in exactly one place, so the page was itself the second location it denied. Resolved: the guide now names the three modes without defining them |
| Boundary chosen for one authority | Superseded and no longer in force. The single-account rule was removed when the User directed the inline block, because it would have forbidden exactly that block. Its durable part survives as the reason recorded under the User-directed redesign |
| `docs/methodology.md` routed, not corrected here | The surface is Technical Writer-owned, so it was routed to that owner rather than changed by the Architect. Resolved: the guide has since been corrected and the documentation artifact is complete |
| Correction validation | `python docs/docs-build.py clean` passed with `Schema validation completed with 0 warning(s)` and `build succeeded`; `python docs/test_docs_build.py` passed 4/4; `git diff --check` passed |
| Check-robustness note | Two assertions first reported false only because the phrase wrapped across an RST line break. Content checks over exported Need text must normalize whitespace; the specification text itself was correct in both cases |
| Quality finding Q-01 confirmed, mine | Adding the release gate left the pre-existing start rule intact, so `SYSP_REQ_CHANGE_CONTRACT` still permitted artifact work to begin from recorded intent approval or from autonomous authority. Two start controls existed at once, and the gate was therefore not the authorization it was introduced to be |
| Q-01 correction | Artifact work now starts only after the `Contract release` gate reads `approved`, with no alternative start condition. A settled intent text does not authorize starting, and the operation mode governs how actors work within the released scope rather than whether release is required |
| Start authorization and outcome validation kept distinct | Superseded and no longer in force as written. At the Q-01 correction only the start checkpoint lost its waiver, and an autonomous waiver of `User validation and approval` was left untouched. The User later settled that the operation mode delegates nothing: validation becomes `not applicable` only through an explicit User delegation recorded at that row |
| Same defect class as the closure wording | Introducing the gate required re-reading every rule that already governed the same decision, not only the rules that quantify over table rows. The start rule governed the same decision from a different section and survived unchanged |
| Q-01 validation | `python docs/docs-build.py clean` passed with `Schema validation completed with 0 warning(s)` and `build succeeded`; `python docs/test_docs_build.py` passed 4/4; `git diff --check` passed; the exported Requirement contains no alternative start condition and `SYSP_VC_CHANGE_CONTRACT_1` now requires every realized start path to demand the approved gate |
| Q-02 resolved by the Project Manager | Whether this Contract's own mode line had to adopt the new vocabulary, given that Scope exempts existing Contracts from retrofit, was a Project Manager decision about self-demonstration versus legacy exemption. Resolved: this Contract now carries `Operation Mode: autonomous` |
| User-directed redesign supersedes my link design | The User rejected the named-value-plus-link outcome and authored an inline `Operation Mode` block in the Change template. My earlier design optimized for a single definition of record; the User's optimizes for a Contract that is readable during execution without opening another document. Both are coherent, the User chose, and the specification now follows the User's choice rather than defending mine |
| Mode behavior is now Change-specific | `SYSP_REQ_CONTRACT_DOCUMENTS` no longer defines any mode, matching the User's removal of the generic section, and `SYSP_VC_CONTRACT_DOCUMENTS_1` now confirms the method defines none. `SYSP_REQ_CHANGE_CONTRACT` carries the `Operation Mode` field, its three complete rules, the `user-guided` default, and the reduction to one selected rule at initialization |
| The single-account rule had to be removed, not merely relaxed | My previous rule forbade any artifact from carrying its own account of a mode. Left in place it would have forbidden exactly the inline block the User directed, so it was removed with its Verification Criterion clause rather than reworded |
| Drift risk of the copy, and why it is acceptable | An inline rule per Contract is a copy, which is what the earlier design avoided. Initialization deletes the two non-selected rules, so a concrete Contract carries exactly one rule and not a paraphrase, and closed Contracts are archives that Scope exempts from retrofit. The remaining exposure is that a later template change does not reach existing instances, which is the intended meaning of an archive |
| `unattended` mechanics specified, not only named | The mode carries governance consequences and not merely a tone: the actor records `USER REVIEW REQUIRED` in the Contract, takes the simplest path that is cheapest to reverse or amend, and keeps the change moving, while the Project Manager reviews flagged points once the User is reachable and decision ownership stays with the deciding actor |
| Setup boundary, decided by the Project Manager | Setup receives no operation-mode vocabulary. `SYSP_REQ_SETUP` specializes `SYSP_REQ_CONTRACT_DOCUMENTS`, so removing modes generically leaves Setup without one; the Project Manager decided that extending modes into Setup exceeds the directed scope and needs a separate decision. The Architect did not invent a Setup mode |
| Preserved deliberately | The User-owned `Contract release` gate, the gate as sole start control, and the gate-aware closure condition are unchanged by this amendment |
| Stale reference created by the move | Moving the definitions left `docs/Syspilot Processes/change.md` and `docs/methodology.md` pointing at content that no longer existed in the generic method. Both were routed to their owners and have since been corrected |
| Provenance of this revision | The working tree had reverted all three affected files to `e42eff4`, which would have made me specify against the design the User rejected. Specification began only after the Project Manager independently verified and restored the files to `c600363` |
| Amendment validation | `python docs/docs-build.py clean` passed with `Schema validation completed with 0 warning(s)` and `build succeeded`; `python docs/test_docs_build.py` passed 4/4; `git diff --check` passed; whitespace-normalized assertions confirm the `Operation Mode` field, the default and value list, the reduction to one rule, the `unattended` mechanics, the removal of the generic mode authority, and that the release gate and start rule remain intact |
| Tailoring becomes local, and the generic rule shrinks to one sentence | `SYSP_REQ_CONTRACT_DOCUMENTS` now requires only that each tailoring option is described at the template section where its choice is made. The author meets the option and its editing instruction at the point of use, which is the same principle the User applied to the `Operation Mode` block rather than a second idea |
| Multiple-Goals boundary lifted out of tailoring | It was bundled into the old tailoring bullet. It is now its own statement and explicitly governs Contract composition rather than tailoring, because it constrains what may share one Contract and not what an author may omit |
| Two clauses deliberately absorbed, not lost | The old generic bullet also said that tailoring preserves ownership and completion semantics and that a non-applicable optional artifact may omit its empty owner section. Both now live where the choice is made: each optional row carries its own reason and delete instruction, and each row names its owner, so a local option cannot silently change ownership. This is a deliberate removal from the central rule, not an oversight |
| Requiredness survives the deleted section | The Change `Tailoring Rules` section also carried the fact that Intent and outcome, Quality review, and Closure are required. That is a requiredness fact rather than a tailoring option, so deleting the section would have quietly deleted the rule. `SYSP_REQ_CHANGE_CONTRACT` now states that a required element offers no omission option, which places the same fact at every required row |
| Delegation separated from operation mode | `User validation and approval` becomes `not applicable` only through an explicit User delegation recorded at that row. The operation mode never delegates it. This removes the undefined "collaboration agreement" by replacing what the clause was gesturing at rather than by renaming it |
| Evidence for that separation | The Technical Writer demonstrated it from the running system rather than from wording: this Contract's `Operation Mode` is `autonomous` while its `User validation and approval` row still reads pending, so autonomous execution demonstrably did not waive validation. The two conditions are independent |
| Three authorities kept apart | Operation mode governs how actors decide, `Contract release` authorizes the start, and `User validation and approval` accepts the finished outcome. The specification now states each separately, and none implies another |
| Tailoring amendment validation | `python docs/docs-build.py clean` passed with `Schema validation completed with 0 warning(s)` and `build succeeded`; `python docs/test_docs_build.py` passed 4/4; `git diff --check` passed; whitespace-normalized assertions confirm the locality rule, the composition invariant, the removal of the general-before-specific obligation, local option and required-element rules, the local-delegation-only validation rule, and that the sole-start gate and gate-aware closure survived unchanged |
| Quality finding Q-03 confirmed, mine | `Affected Artifacts` still declared the superseded design as the current change: Contract Documents as mode authority and general tailoring source, a linked named-value field, general rules applied before process-specific ones, and a Tailoring Rules section to be modified rather than removed |
| Why the later decision rows did not cure it | A Contract Document holds current state rather than an event log. `Decisions And Evidence` explaining that a design was superseded does not correct a table that still declares the old change as what this Change does. Quality was right that the two tables have different jobs |
| Q-03 correction | `Affected Artifacts` now states only the currently valid changes: no mode in the generic method, tailoring reduced to the locality rule, the composition invariant stated outside tailoring, the `Operation Mode` block with its reduction to one, the `Tailoring Rules` section removed rather than modified, the gate as sole start control, and validation waived only by explicit local User delegation |
| Known Evidence deliberately not rewritten | That table records the state observed when the Change began and is the reason the work exists. Updating it to current state would destroy the evidence, so it now says so explicitly instead, which also prevents the same finding being raised against it |
| Routing judgment | Acceptance is `passed` against the current architecture and this correction changed no Requirement, Verification Criterion, or realization, only the Contract's own record of its architecture. The acceptance scenarios therefore still hold and responsibility returns directly to Quality; if Quality reads that differently, the Tester rerun is the cheaper of the two errors |
| Q-03 validation | `python docs/docs-build.py clean` passed with `Schema validation completed with 0 warning(s)` and `build succeeded`; `git diff --check` passed; a scan of the `Affected Artifacts` section finds none of the seven superseded phrases and all seven currently valid ones |
| Q-03 follow-up, and what my first correction actually did | Quality named two false current claims. I corrected those and four further rows containing the same phrases, and described that as a sweep of every row. It was not: it was a scan for a fixed list of seven strings. Quality then found six more rows, which is the evidence that the description was wrong |
| Root cause of the repeated finding | Each amendment corrected the Requirements but left earlier rows standing as unqualified present-tense claims. A Contract Document holds current state, so a row written truthfully at one point becomes false the moment the design it describes is replaced. The remedy is to treat every amendment as a pass over all existing claims, not only over the artifacts being changed |
| Superseded rows removed rather than annotated | The Contract Documents method states that resolved intermediate states do not accumulate and that version control preserves their history. Rows describing the abandoned link design therefore now say only that they are superseded and what replaced them, instead of restating a design that is no longer in force |
| Reported commits verified before sending | Quality could not resolve a follow-up commit `f7502406...` and worked from `adb56f1` instead. I confirmed independently that `f7502406...` does not exist in this repository either. It was not a commit of mine; my last reported hash was `adb56f1`, which resolves. I verify every hash with `git cat-file` before reporting it |
| Every Decision row read against current artifacts | All rows were read individually rather than matched. Nine were false as current statements: the six Quality named, plus one describing the deleted Tailoring Rules as still attaching mode consequences, one still using the superseded term collaboration mode, and my own row claiming a complete sweep. Each is now corrected or explicitly marked superseded with what replaced it |
| The most consequential of them | The row asserting that an autonomous waiver of `User validation and approval` remained valid contradicted the settled separation outright. It was the last place in the Contract where the operation mode still appeared to delegate User authority, which is precisely the confusion the separation exists to prevent |
| Full-read validation | `python docs/docs-build.py clean` passed with `Schema validation completed with 0 warning(s)` and `build succeeded`; `python docs/test_docs_build.py` passed 4/4; `git diff --check` passed. Facts checked against the artifacts rather than asserted: this Contract carries `Operation Mode: autonomous`, and `docs/methodology.md` names the three modes without defining them |
| Q-03 follow-up validation | A keyword scan cannot find a row that is false without containing any searched word, which is exactly how the six remaining rows survived: they described resolved intermediate conditions in their own vocabulary. Every row has now been read against the current artifacts rather than matched against a phrase list |

## User-Facing Documentation

**Owner:** Syspilot Technical Writer<br>
**Status:** complete

### Impact Assessment

Impact queries were run from both changed Requirements rather than guessing which guides discuss collaboration modes.

| Requirement | Incoming documentation consumers | Disposition |
|---|---|---|
| `SYSP_REQ_CONTRACT_DOCUMENTS` (modified) | `SYSP_DOC_CHANGE_CONTRACT`, `SYSP_DOC_CUSTOMIZATION`, `SYSP_DOC_GETTING_STARTED`, `SYSP_DOC_METHODOLOGY`, `SYSP_DOC_PRODUCT_MODEL` | Four updated; Getting Started assessed and unchanged |
| `SYSP_REQ_CHANGE_CONTRACT` (modified) | `SYSP_DOC_BRANCHING`, `SYSP_DOC_CHANGE_CONTRACT`, `SYSP_DOC_METHODOLOGY` | Branching assessed and unchanged; the other two were already in scope above |

No `doc` Need or `includes` link required a change. Every affected surface already included the Requirement that changed, which is why the impact query found them.

### Documentation Plan And Ownership

| Documentation surface | `doc` Need | Requirements included | Status |
|---|---|---|---|
| `docs/methodology.md` | `SYSP_DOC_METHODOLOGY` | `SYSP_REQ_CONTRACT_DOCUMENTS`, `SYSP_REQ_CHANGE_CONTRACT`, unchanged link set | verified |
| `docs/change-contract.md` | `SYSP_DOC_CHANGE_CONTRACT` | `SYSP_REQ_CONTRACT_DOCUMENTS`, `SYSP_REQ_CHANGE_CONTRACT`, unchanged link set | verified |
| `docs/product-model.md` | `SYSP_DOC_PRODUCT_MODEL` | `SYSP_REQ_CONTRACT_DOCUMENTS`, unchanged link set | verified |
| `docs/customization.md` | `SYSP_DOC_CUSTOMIZATION` | `SYSP_REQ_CONTRACT_DOCUMENTS`, unchanged link set | verified |
| `docs/getting-started.md` | `SYSP_DOC_GETTING_STARTED` | `SYSP_REQ_CONTRACT_DOCUMENTS`, unchanged link set | verified without change; its Contract references concern Setup and release, not collaboration modes or gates |
| `docs/branching.md` | `SYSP_DOC_BRANCHING` | `SYSP_REQ_CHANGE_CONTRACT`, unchanged link set | verified without change; its gate and release wording belongs to Setup and publication, which this Change did not touch |

### Consultations And Factual Reviews

| Documentation surface | Consulted artifact owner | Review question | Evidence and disposition |
|---|---|---|---|
| Collaboration mode wording | Syspilot Architect, Syspilot Developer, Syspilot Tester | Where does an actor find the rule for the mode a Contract is running under? | In the Contract itself. Two earlier answers were superseded: reproducing the definitions in the guide, which independent Acceptance rejected against the released Scope, and linking to an account of record in `contract-documents.md`, which the User replaced with contract-local Operation Mode. The canonical template now carries all three rules and initialization retains the selected one, so the guides name the mode, state that its rule travels with the Contract, and point nowhere |

### Changed Documentation And Verification

| Artifact | Change | Verification evidence |
|---|---|---|
| `docs/methodology.md` | Corrected two statements the Change made false. The guide said a Contract describes its collaboration expectations "in free text, and that written agreement is authoritative", and that the three modes are "starting points, not a closed set" whose specific wording "wins over the familiar label". The section now says a Contract selects exactly one Operation Mode agreed with the User before release, and that the selected rule is carried in the Contract itself because an actor should not have to leave the active Contract to learn how to work inside it. The boundary paragraph names the Operation Mode and the User-owned release gate. After the User's tailoring amendment the tailoring paragraph no longer says an instance "may omit a tailorable artifact with a recorded reason"; it says each row offers its own choice and states what that choice obliges, so a required artifact cannot be dropped at all | Strict Sphinx/schema build passes with zero warnings; `python docs/test_docs_build.py` passes 4/4; `git diff --check` passes; a repository-wide scan finds no remaining `collaboration mode` term, no pointer to a mode account of record, and no claim that autonomous work may waive validation |
| `docs/change-contract.md` | Replaced "artifact work begins after the intent and outcome are approved" with the actual mechanism: one Operation Mode agreed beforehand whose rule the Contract carries, the User's release recorded once in a `Contract release` gate only the User may set, and artifact work starting when that gate reads `approved` — with the explicit point that a settled intent is not an authorization to begin. Added that the table carries process gates alongside artifacts with one owner each. After the User's tailoring amendment: an optional artifact that does not apply is marked with a reason and its empty owner section deleted in the same step, the row states this next to the choice, and required artifacts offer no such option. The validation paragraph no longer says autonomous work may mark validation `not applicable`; it now requires an explicit User delegation recorded in the validation row and states that no Operation Mode can hand over authority belonging to the User | Same build and test evidence |
| `docs/product-model.md` | The Contract state description listed only artifacts. It now also records process gates such as the User's release, each with exactly one owner who alone may set it | Same build and test evidence |
| `docs/customization.md` | The list of what a project Contract defines said "collaboration agreement", which read as free-form, and then "collaboration mode", which named the superseded design. It now reads "operation mode". Reassessed after the tailoring amendment and left unchanged: the guide makes no claim about artifact omission or validation waiver, so it had nothing to correct | Same build and test evidence |


## Implementation And Unit Verification

**Owner:** Syspilot Developer<br>
**Status:** complete

### Decisions And Evidence

| Decision | Chosen approach | Relevant alternatives | Rationale and evidence |
|---|---|---|---|
| Contract-local operation mode | Carry all three complete rules in the canonical Change template; initialization retains the selected mode and rule and removes the template note plus two non-applicable rules | Link to Contract Documents or retain multiple rules in a concrete Contract | The User directed every actor to find its governing rule inside the Contract it executes; Contract Documents therefore defines no mode, while each concrete Change remains unambiguous and self-contained |
| Local tailoring choices | Keep only the point-of-use rule in the generic method; place every concrete option, required reason, and edit instruction at its Change template field, row, or section; state the multiple-goal boundary under Contract composition | Maintain a central list that authors must reconcile with the template or classify the multiple-goal invariant as tailoring | Required rows expose only `yes`; optional artifact rows state the reason and owner-section deletion instruction; the validation row alone offers explicit User delegation and retains its section as evidence; the generic method offers no concrete tailoring choice |
| Release ownership | Record release only as the User-owned `Contract release` gate; Intent approval evidence proves only that its text is settled | Retain release-shaped Intent evidence or a closure checkbox | The gate separates text approval from authorization and the existing terminal-status closure condition enforces its completion without another rule |
| Sole start authorization | Require `Contract release: approved` in every controlling start statement and initialization step; make finished-outcome validation `not applicable` only through explicit User delegation recorded at the validation row | Allow settled intent or operation mode to authorize artifact work, or let operation mode delegate validation | Intent approval settles text, the User alone owns release, and operation mode governs work only inside the released scope without delegating User validation authority |
| Executable impact | No script or automated test changes | Add speculative parser tests | Repository-wide Python search found no dependency on the free-text collaboration field or removed release duplication; behavior is realized and verified through the process documents |

### Changed Artifacts And Verification

| Artifact | Change | Verification evidence |
|---|---|---|
| `docs/Syspilot Processes/contract-documents.md` | Defines owner-exclusive process gates, directs each tailoring option to its point of use, and states the shared-boundary invariant under Contract composition without defining an operation mode | Direct inspection satisfies `SYSP_VC_CONTRACT_DOCUMENTS_1`: the generic method offers no concrete tailoring choice, the multiple-goal boundary is outside Tailoring, and no mode term or rule remains; strict Sphinx/schema build passes with zero warnings |
| `docs/Syspilot Processes/change.md` | Carries the complete User-directed Operation Mode block, requires initialization to retain one selected rule, localizes optional artifact and validation choices, preserves the User-owned release gate as sole start authorization, and keeps gate-aware Closure | Direct inspection confirms no process-specific Tailoring Rules section, required rows without omission, optional rows with reason/edit instructions, validation waived only by explicit User delegation at its row, and unchanged release/mode boundaries; strict Sphinx/schema build passes with zero warnings; docs tests pass 4/4; diagnostics and `git diff --check` are clean |

## Acceptance Testing

**Owner:** Syspilot Tester<br>
**Status:** passed

| Scenario | Traces to | Result | Evidence |
|---|---|---|---|
| A Contract author finds all three complete operation-mode rules at the canonical field | Contract-local mode behavior | pass | The canonical template contains the exact three-value selector and all three User-provided rules; it sends the author to no external mode authority |
| A concrete Contract retains only its selected mode and exact rule | concrete Contract shape | pass | This Contract contains only `autonomous` and its complete rule; the template note and both non-selected rules are absent |
| The generic Contract Documents method defines no operation mode | Change-specific mode boundary | pass | Case-insensitive inspection found no operation-mode term, named mode, or mode rule in `contract-documents.md` |
| Every tailoring option and editing instruction is local to the affected template element, with no central option list | local tailoring | pass | The Change template localizes every concrete choice; realized `contract-documents.md` states only the generic point-of-use procedure and contains no optional-artifact choice or owner-section instruction |
| The multiple-goal boundary is presented as a Contract composition invariant rather than tailoring | Contract composition | pass | `contract-documents.md` places the shared responsibility, release, validation, and integration boundary under `## Contract Composition`, outside `## Tailoring`, matching `SYSP_REQ_CONTRACT_DOCUMENTS` and its VC |
| Required Change elements expose no omission option | required elements | pass | Intent, Contract release, Quality review, and Closure rows offer only `yes`; optional artifact rows alone carry `not applicable` choices |
| Each optional artifact choice locally requires a reason and deletion of its empty owner section | optional artifact editing | pass | Every optional artifact row pairs `not applicable` with `{reason; delete the corresponding empty owner section}` |
| User validation becomes `not applicable` only through explicit User delegation recorded at its row | validation authority | pass | The validation row requires explicit User delegation and retains its section as evidence; neither the selector nor any mode rule grants validation authority |
| Unattended validation remains pending until the User returns | unattended validation | pass | The process template offers no unattended waiver, and its validation guidance keeps the User checkpoint pending |
| The User's release is recorded in exactly one place and no other actor can set it | release gate | pass | The canonical template contains exactly one `Contract release` row, owned by the User, with `pending / approved`; its evidence says no other actor may set it, and neither Intent evidence nor Closure records release separately |
| `Intent: approved` no longer asserts that the User authorized the start | separated statements | pass | Intent approval evidence records only that the intent and outcome text is settled; authorization to start is isolated in the User-owned release gate |
| Artifact work cannot start from intent approval, operation mode, or autonomous authority | sole start authorization | pass | Both controlling start statements require the User-owned `Contract release` gate to read `approved`; the Requirement admits no alternative start condition |

Acceptance was re-derived after the User's local-tailoring amendment and all twelve scenarios passed. The strict build and documentation tests remain supporting checks rather than substitutes for the behavior scenarios above.

## Quality Review

**Owner:** Syspilot Quality<br>
**Status:** passed

**Current judgment:** `proceed`

### Applied Review Methods

| Method | Selected scope | Evidence | Findings | Limits |
|---|---|---|---|---|
| MECE horizontal coverage | `same-document` and `all-type` for `SYSP_REQ_CONTRACT_DOCUMENTS`, `SYSP_VC_CONTRACT_DOCUMENTS_1`, `SYSP_REQ_CHANGE_CONTRACT`, and `SYSP_VC_CHANGE_CONTRACT_1` | Fresh built data returned no same-document peers. Each Requirement returned the other 17 Requirement IDs; each VC returned the other 17 VC IDs. Exact sets are recorded below. Quality read all peers and compared Contract Documents, Change, Contract Handling, Setup, role, verification, and documentation boundaries. Focused MECE passed 5/5 | The generic point-of-use tailoring procedure, Change-specific options, guides, Architecture declarations, and Implementation decisions are coherent. Q-04 is resolved because the sole-start decision now preserves User validation authority through explicit delegation only | Built Needs contain no structured quality claims, so automation reports `structured-coverage-data-unavailable`; semantic review supplied the judgment. Same-document reports `no-comparable-peers-discovered` |
| Trace relationship and chain analysis | `--direction both --depth 2` for all four impacted objects | Exact neighborhoods are recorded below and remained unchanged at counts 33, 10, 25, and 7 respectively. Focused Trace passed 7/7, shared Impact 9/9, docs 4/4, and strict build/schema validation passed with zero warnings | Every discovered edge resolved and matched an ontology-permitted type and direction; no structural finding. Semantic neighbor review confirmed local operation-mode behavior, point-of-use tailoring, sole release authorization, and explicit-User-delegation-only validation across Requirement, VC, process realization, guides, and current Contract decisions | The analyzer reports `semantic-content-review-required`; Quality discharged that limit by reading the amended specifications, both process realizations, linked guides, relevant inherited boundaries, and all current Contract decision tables. Ontology relationships are permitted rather than required |

### Exact Peer Sets

| Type | Exact all-type peers, excluding the analyzed object |
|---|---|
| Requirement | `SYSP_REQ_ACTOR_MODEL`, `SYSP_REQ_ARCHITECT`, `SYSP_REQ_CHANGE_CONTRACT`, `SYSP_REQ_CONTRACT_DOCUMENTS`, `SYSP_REQ_CONTRACT_HANDLING`, `SYSP_REQ_DEVELOPER`, `SYSP_REQ_IMPACT_QUERY`, `SYSP_REQ_MECE_ANALYSIS`, `SYSP_REQ_ONTOLOGY_EDITING`, `SYSP_REQ_ONTOLOGY_SCHEMA`, `SYSP_REQ_PROJECT_MANAGER`, `SYSP_REQ_QUALITY`, `SYSP_REQ_RELEASE`, `SYSP_REQ_RESEARCH`, `SYSP_REQ_SETUP`, `SYSP_REQ_TECHNICAL_WRITER`, `SYSP_REQ_TESTER`, `SYSP_REQ_TRACE_ANALYSIS`; for each analyzed Requirement, exclude that ID and include the other listed Requirement |
| VC | `SYSP_VC_ACTOR_MODEL_1`, `SYSP_VC_ARCHITECT_1`, `SYSP_VC_CHANGE_CONTRACT_1`, `SYSP_VC_CONTRACT_DOCUMENTS_1`, `SYSP_VC_CONTRACT_HANDLING_1`, `SYSP_VC_DEVELOPER_1`, `SYSP_VC_IMPACT_QUERY_1`, `SYSP_VC_MECE_ANALYSIS_1`, `SYSP_VC_ONTOLOGY_EDITING_1`, `SYSP_VC_ONTOLOGY_SCHEMA_1`, `SYSP_VC_PROJECT_MANAGER_1`, `SYSP_VC_QUALITY_1`, `SYSP_VC_RELEASE_1`, `SYSP_VC_RESEARCH_1`, `SYSP_VC_SETUP_1`, `SYSP_VC_TECHNICAL_WRITER_1`, `SYSP_VC_TESTER_1`, `SYSP_VC_TRACE_ANALYSIS_1`; for each analyzed VC, exclude that ID and include the other listed VC |

### Exact Trace Neighborhoods

| Impacted object | Exact depth-2 neighborhood |
|---|---|
| `SYSP_REQ_CONTRACT_DOCUMENTS` | `ROOT_SYSPILOT`, `SYSP_AC_CONTRACT_DOCUMENTS_1`, `SYSP_DOC_BRANCHING`, `SYSP_DOC_CHANGE_CONTRACT`, `SYSP_DOC_CUSTOMIZATION`, `SYSP_DOC_GETTING_STARTED`, `SYSP_DOC_METHODOLOGY`, `SYSP_DOC_OPERATIONS`, `SYSP_DOC_PRODUCT_MODEL`, `SYSP_DOC_README`, `SYSP_REQ_ACTOR_MODEL`, `SYSP_REQ_ARCHITECT`, `SYSP_REQ_CHANGE_CONTRACT`, `SYSP_REQ_CONTRACT_DOCUMENTS`, `SYSP_REQ_CONTRACT_HANDLING`, `SYSP_REQ_DEVELOPER`, `SYSP_REQ_IMPACT_QUERY`, `SYSP_REQ_MECE_ANALYSIS`, `SYSP_REQ_ONTOLOGY_EDITING`, `SYSP_REQ_ONTOLOGY_SCHEMA`, `SYSP_REQ_PROJECT_MANAGER`, `SYSP_REQ_QUALITY`, `SYSP_REQ_RELEASE`, `SYSP_REQ_RESEARCH`, `SYSP_REQ_SETUP`, `SYSP_REQ_TECHNICAL_WRITER`, `SYSP_REQ_TESTER`, `SYSP_REQ_TRACE_ANALYSIS`, `SYSP_US_CONTRACT_DOCUMENTS`, `SYSP_US_SETUP`, `SYSP_VC_CONTRACT_DOCUMENTS_1`, `SYSP_VC_CONTRACT_HANDLING_1`, `SYSP_VC_SETUP_1` |
| `SYSP_VC_CONTRACT_DOCUMENTS_1` | `SYSP_DOC_CHANGE_CONTRACT`, `SYSP_DOC_CUSTOMIZATION`, `SYSP_DOC_GETTING_STARTED`, `SYSP_DOC_METHODOLOGY`, `SYSP_DOC_PRODUCT_MODEL`, `SYSP_REQ_CONTRACT_DOCUMENTS`, `SYSP_REQ_CONTRACT_HANDLING`, `SYSP_REQ_SETUP`, `SYSP_US_CONTRACT_DOCUMENTS`, `SYSP_VC_CONTRACT_DOCUMENTS_1` |
| `SYSP_REQ_CHANGE_CONTRACT` | `ROOT_SYSPILOT`, `SYSP_AC_CHANGE_CONTRACT_1`, `SYSP_DOC_BRANCHING`, `SYSP_DOC_CHANGE_CONTRACT`, `SYSP_DOC_METHODOLOGY`, `SYSP_DOC_PRODUCT_MODEL`, `SYSP_REQ_ACTOR_MODEL`, `SYSP_REQ_ARCHITECT`, `SYSP_REQ_CHANGE_CONTRACT`, `SYSP_REQ_CONTRACT_DOCUMENTS`, `SYSP_REQ_CONTRACT_HANDLING`, `SYSP_REQ_DEVELOPER`, `SYSP_REQ_IMPACT_QUERY`, `SYSP_REQ_MECE_ANALYSIS`, `SYSP_REQ_PROJECT_MANAGER`, `SYSP_REQ_QUALITY`, `SYSP_REQ_RELEASE`, `SYSP_REQ_SETUP`, `SYSP_REQ_TECHNICAL_WRITER`, `SYSP_REQ_TESTER`, `SYSP_REQ_TRACE_ANALYSIS`, `SYSP_US_CHANGE_CONTRACT`, `SYSP_US_CONTRACT_DOCUMENTS`, `SYSP_VC_CHANGE_CONTRACT_1`, `SYSP_VC_CONTRACT_HANDLING_1` |
| `SYSP_VC_CHANGE_CONTRACT_1` | `SYSP_DOC_BRANCHING`, `SYSP_DOC_CHANGE_CONTRACT`, `SYSP_DOC_METHODOLOGY`, `SYSP_REQ_CHANGE_CONTRACT`, `SYSP_REQ_CONTRACT_HANDLING`, `SYSP_US_CHANGE_CONTRACT`, `SYSP_VC_CHANGE_CONTRACT_1` |

### Open Quality Issues

None.

## User Validation And Approval

**Owner:** User<br>
**Recorded by:** Syspilot Project Manager<br>
**Status:** accepted

**Decision and evidence:** On 2026-08-28 the User rejected the linked-name outcome because an actor reading a concrete Contract would still have to leave it to learn the active behavior. The User directed the exact Automobil-style `Operation Mode` block now present in the canonical template, removed the generic definitions from `contract-documents.md`, and requested corresponding specification alignment. The User then simplified tailoring by directing that process-specific Tailoring Rules sections be deleted and that each option and editing instruction appear only at the affected template location, with one generic sentence describing that procedure. These are approved scope amendments, not final validation of the revised outcome.

**Final validation:** On 2026-09-13 the User accepted the completed outcome. All artifacts and gates have terminal status and completion evidence.

## Closure

**Owner:** Syspilot Project Manager<br>
**Status:** closed

**Q-02 disposition:** The earlier linked-value disposition was superseded by the User's 2026-08-28 scope amendment. This active pilot now retains the selected `autonomous` rule inline, demonstrating the revised Contract-local form without imposing retrofit obligations on other legacy Contracts.

- [x] Every included artifact or gate has terminal status and completion evidence.
- [x] Intent and outcome are `approved`.
- [x] The version-control artifact is `merged`.
- [x] The template states all three operation-mode rules, and a concrete Contract retains only the selected rule.
- [x] The User's release is recorded in exactly one place.
- [x] `contract-documents.md` says where tailoring options are described, each option and edit instruction is local to its template choice, and no process-specific Tailoring Rules section remains.
- [x] Multiple goals share a Contract only under one responsibility, release, validation, and integration boundary.
- [x] Quality has recorded a `proceed` judgment.
- [x] Open Quality Issues contains `None`.
- [x] User validation is `accepted`.
- [x] Current blocker is `none`.
- [x] The observable outcome is demonstrated.

**Final outcome:** The Change Contract template now carries a Contract-local `Operation Mode` block with all three complete behavioral rules, and this Contract retains only its selected `autonomous` rule. The User-owned `Contract release` gate is the sole start authorization, recorded in exactly one place. Tailoring is local to each affected template field or row; `contract-documents.md` retains only the point-of-use procedure sentence and the multiple-goal composition invariant, with no process-specific Tailoring Rules section remaining. User validation is separated from operation mode and was recorded as `accepted` by explicit User decision. Quality's `proceed` judgment and Acceptance's 12/12 passed scenarios support the outcome. Integrated: `feature/contract-gates-and-modes` squash-merged into `development`.
