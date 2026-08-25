# Change Contract: Contract Handling

**Status:** closed<br>
**Process owner:** Syspilot Project Manager<br>
**Current responsibility:** Syspilot Project Manager<br>
**Current blocker:** none<br>
**Created:** 2026-08-25<br>
**Branch:** feature/contract-handling<br>
**Collaboration mode:** User-guided for Contract responsibility semantics and Change Process cleanup; otherwise autonomous within the approved intent.

## Intent And Outcome

**Owner:** Syspilot Project Manager<br>
**Status:** approved<br>
**Approval evidence:** User approved the `contract-handling` Change name and directed that the always-on Contract instruction and Change Process cleanup be handled together on 2026-08-25.

### Goal

Make Contract responsibility handoffs reliable across all Syspilot Contract types through one short always-on instruction, and simplify the Change Process pre-template content so it contains only the instructions needed to start a Change flow.

### Value

Actors can progress Contracts directly without relying on repeated process prose or a designated coordination hop, while Change initiators receive a short and unambiguous starting procedure.

### Scope

- Add a workspace-shared `.github/instructions/syspilot.contract-handling.instructions.md` with `applyTo: "**"`.
- Use the precise term `Current responsibility`; preserve durable artifact ownership.
- Require the responsible actor, after completing its work, to select the next logical included artifact owner that can progress the Contract.
- Require Contract status, artifact evidence, and Current responsibility to be updated before handoff.
- Require the Contract and related artifacts to be committed as one consistent state before `SEND` notifies the next owner of the Contract path, commit, completed outcome, and remaining work, intentionally prioritizing single-writer consistency over uninterrupted handoff communication.
- Allow any actor to request advice or review at any time without transferring Current responsibility; the consulting actor remains read-only for the Contract and versioned work artifacts and returns only advice or findings.
- State that questions and escalation do not transfer Current responsibility.
- Require a recorded blocker and escalation when no included owner can progress.
- Clean up the prose before the canonical template in `docs/Syspilot Processes/change.md`, moving or removing generic Contract-handling duplication while retaining Change-specific initialization, tailoring, mandatory first Architect handoff, validation, and Closure semantics.
- Align affected specifications, derived documentation, and actor-facing product artifacts as determined by impact analysis.

### Observable Outcome

Every Syspilot actor receives one concise always-on Contract-handling rule that distinguishes responsibility transfer from consultation and requires a committed direct handoff to the next logical owner. The Change Process pre-template section becomes a compact initiation procedure for starting a Change Contract flow, without duplicating the generic handoff behavior or weakening Change-specific governance.

## Artifact Applicability And Ownership

**Applicability:** Each artifact owner decides and updates its own row.<br>
**Status:** complete

| Artifact type | Included | Owner | Completion evidence | Status |
|---|---|---|---|---|
| Intent and outcome | yes | Syspilot Project Manager | Goal, value, scope, boundaries, and observable outcome are explicit and approved | approved |
| Product specification and architecture decisions | yes | Syspilot Architect | Contract responsibility semantics, instruction authority, and Change Process cleanup boundaries are approved and traced | complete |
| User-facing documentation | yes | Syspilot Technical Writer | Impact on Contract and Change guidance is assessed; applicable updates are reviewed and build cleanly | complete |
| Implementation and unit verification | yes | Syspilot Developer | Approved instruction and Change Process cleanup are realized; focused checks pass | complete |
| Acceptance test design and results | yes | Syspilot Tester | Direct handoff, deliberate notification gap, read-only consultation, question and blocker no-transfer behavior, and Change initialization scenarios pass | passed |
| Quality review | yes | Syspilot Quality | Current verification judgment is `proceed` and no open quality issue remains | proceed |
| User validation and approval | yes | User | Observable outcome is accepted or changes are requested directly to the Project Manager | accepted |
| Closure decision | yes | Syspilot Project Manager | Final outcome, validation disposition, and integration state are recorded | complete |

## Product Specification And Architecture Decisions

**Owner:** Syspilot Architect<br>
**Status:** complete

### Decisions And Evidence

| Decision | Chosen approach | Relevant alternatives | Rationale and evidence |
|---|---|---|---|
| Always-on Contract behavior | Short workspace instruction with `applyTo: "**"` | Repeat handoff rules in every Contract process or use an on-demand skill | Contract responsibility applies across artifact types and must be present when any responsible actor completes work |
| Requirement hierarchy | Add `SYSP_REQ_CONTRACT_HANDLING` between Contract Documents and Change Contract, realized by the always-on instruction | Add handling details to the generic method or leave them in the Change Requirement | Contract Documents defines the method, Contract Handling defines universal actor behavior, and Change Contract retains Change-specific governance |
| Change Process cleanup boundary | Retain only applicability, template/instance location, Change tailoring, PM initialization, mandatory first Architect handoff, direct Quality/User provenance, and PM Closure governance before the template | Preserve all current pre-template prose | Generic responsibility transfer belongs in the always-on instruction; lifecycle detail already represented in the canonical template should not be duplicated before it |
| Ownership table placement | Keep the operational artifact ownership table only in the canonical template copied into every Change instance | Repeat it before the template or move it to the generic Contract method | The instance is the source used by actors; a second static table creates duplicate maintenance without adding execution context |
| Handoff consistency | Commit one consistent Contract state before `SEND`, accepting a brief notification gap | Notify before commit or allow concurrent Contract edits | Single-writer consistency keeps the committed Contract authoritative even if uninterrupted communication would be temporarily smoother |
| Messaging boundary | Name `SEND` only as notification after the committed state; leave destination resolution and transport mechanics to the Actor Kernel | Repeat Jarvis tool mappings in the instruction | Contract Handling defines when and what to communicate, while the Kernel owns how messages are transported |
| Consultation boundary | Any actor may request advice or review at any time; the consulting actor remains read-only for the Contract and versioned work artifacts, returns only advice or findings, and does not receive `Current responsibility` | Let consultation imply responsibility transfer or permit both actors to edit | Consultation supplies attention and factual input without introducing competing writers or changing maintenance authority |

### Affected Specifications And Artifacts

| Artifact | Disposition | Rationale |
|---|---|---|
| `SYSP_REQ_CONTRACT_HANDLING`, `SYSP_VC_CONTRACT_HANDLING_1` | add | Own universal committed direct-handoff, deliberate notification-gap, read-only consultation, and blocker behavior |
| `SYSP_REQ_CHANGE_CONTRACT`, `SYSP_VC_CHANGE_CONTRACT_1` | modify | Specialize Contract Handling and constrain the compact Change-specific pre-template boundary |
| `.github/instructions/syspilot.contract-handling.instructions.md` | add | Realize the universal behavior for every actor with `applyTo: "**"` |
| `docs/Syspilot Processes/change.md` | modify | Remove generic and duplicated pre-template prose while retaining Change-specific initiation and governance |
| `docs/change-workflow.md` / `SYSP_DOC_CHANGE_WORKFLOW` | Technical Writer impact review | The user-facing workflow includes both affected requirements and may need terminology or lifecycle clarification |
| `docs/product-model.md` / `SYSP_DOC_PRODUCT_MODEL` | Technical Writer impact review | The product model explains Contract responsibility and direct progression |

### Specification Verification

| Check | Result |
|---|---|
| Requirement hierarchy is `SYSP_REQ_CONTRACT_DOCUMENTS` → `SYSP_REQ_CONTRACT_HANDLING` → `SYSP_REQ_CHANGE_CONTRACT` | pass: strict Needs build resolved both specialization links without warnings |
| Contract Handling VC covers committed direct handoff, deliberate notification gap, read-only consultation, and blocker escalation | pass: revised criterion exercises all four behaviors without a Project Manager special case |
| Change Contract VC retains Change initialization, first Architect handoff, validation provenance, and Closure while excluding generic handoff duplication | pass |
| Strict Sphinx/schema build and focused documentation tests | pass after clarified semantics: `python docs/docs-build.py clean` completed with zero warnings; `python docs/test_docs_build.py -v` passed all four tests; `git diff --check` passed |

## User-Facing Documentation

**Owner:** Syspilot Technical Writer<br>
**Status:** complete

### Documentation Plan And Ownership

| Documentation surface | `doc` Need | Requirements included | Status |
|---|---|---|---|
| `docs/product-model.md` | `SYSP_DOC_PRODUCT_MODEL` | `SYSP_REQ_CONTRACT_DOCUMENTS`, `SYSP_REQ_CONTRACT_HANDLING` | verified |
| `docs/change-workflow.md` | `SYSP_DOC_CHANGE_WORKFLOW` | `SYSP_REQ_CONTRACT_DOCUMENTS`, `SYSP_REQ_CONTRACT_HANDLING`, `SYSP_REQ_CHANGE_CONTRACT` | verified |

### Changed Documentation And Verification

| Artifact | Change | Verification evidence |
|---|---|---|
| `docs/product-model.md`, `docs/change-workflow.md`, and their `doc` Needs | Explain temporary Current responsibility, next-owner selection, committed pre-SEND handoff, deliberate notification gap, read-only consultation, and blocker escalation | Four focused tests passed; clean strict Sphinx/schema build passed with zero warnings; targeted wording scan confirmed the central handling rules and both `includes` links |

## Implementation And Unit Verification

**Owner:** Syspilot Developer<br>
**Status:** complete

### Changed Artifacts And Verification

| Artifact | Change | Verification evidence |
|---|---|---|
| `.github/instructions/syspilot.contract-handling.instructions.md` | Added the concise always-on Contract responsibility rules with uniform next-owner selection, deliberate post-commit notification gap, read-only consultation, and no Actor Kernel transport duplication | Direct comparison with revised `SYSP_REQ_CONTRACT_HANDLING` and `SYSP_VC_CONTRACT_HANDLING_1`: all seven required handling rules are present; frontmatter includes a meaningful `description` and `applyTo: "**"` |
| `docs/Syspilot Processes/change.md` | Removed generic Contract-handling prose and the duplicate pre-template ownership table while retaining Change applicability, locations, tailoring, initialization, first Architect handoff, direct Quality/User provenance, and PM Closure governance | Canonical template unchanged; compact pre-template content matches `SYSP_VC_CHANGE_CONTRACT_1` |
| `docs/Syspilot Processes/setup.md` | Added a release-owned `.github/instructions/` directory job and explicit installed-structure requirement for `syspilot.contract-handling.instructions.md` | Temporary target-workspace simulation copied all three release instruction files; relative inventory and SHA-256 identities matched, and the Contract-handling instruction existed at `.github/instructions/syspilot.contract-handling.instructions.md` |
| Documentation verification | Validated the complete uncommitted implementation state | `python docs/docs-build.py clean`: pass with zero Sphinx/schema warnings; `python docs/test_docs_build.py -v`: 4/4 pass; `git diff --check`: pass |

**Architecture review:** accepted without findings against architecture base `8becd6a8`; the canonical Change Contract template is unchanged and independent strict build, focused tests, diff check, and editor diagnostics pass.

## Acceptance Testing

**Owner:** Syspilot Tester<br>
**Status:** passed

| Scenario | Traces to | Result | Evidence |
|---|---|---|---|
| A responsible actor completes work, commits a consistent Contract state, and directly hands off to the next logical included owner | observable outcome, `SYSP_REQ_CONTRACT_HANDLING` | pass | Technical Writer commit `85fe984` contains completed documentation evidence and `Current responsibility: Syspilot Tester`; the subsequent SEND named the Contract, commit, completed outcome, five remaining scenarios, and Tester as the next open artifact owner |
| Any actor requests advice or review while the consulting actor remains read-only and Current responsibility stays unchanged | consultation boundary, `SYSP_REQ_CONTRACT_HANDLING` | pass | Tester sent Research an explicit read-only consultation request without handoff; the worktree remained clean and committed `Current responsibility` remained Syspilot Tester throughout the consultation check |
| A committed handoff accepts the brief pre-notification gap while preserving one authoritative writer and consistent Contract state | consistency trade-off, `SYSP_REQ_CONTRACT_HANDLING` | pass | Commit `85fe984` made the Contract authoritative with Tester responsibility before the Technical Writer's later SEND notification; no uncommitted Contract state existed when Tester received the handoff |
| A standalone question leaves `Current responsibility` unchanged | question boundary, `SYSP_REQ_CONTRACT_HANDLING` | pass | Tester sent a standalone question from committed fixture `8e7c337` and explicitly marked it as no handoff; afterward HEAD and worktree were unchanged and both parent and fixture still named Syspilot Tester as current responsibility |
| A blocked actor records the blocker and escalates when no included owner can progress | escalation boundary, `SYSP_REQ_CONTRACT_HANDLING` | pass | Fixture commit `8e7c337` recorded an actionable blocker while both parent and fixture named Syspilot Tester; Tester then sent a separate blocker escalation explicitly without handoff, after which HEAD and worktree remained unchanged and both responsibility fields still named Syspilot Tester |
| A PM can initialize a Change from the compact pre-template instructions and mandatory first Architect handoff | Change-specific initialization, `SYSP_REQ_CHANGE_CONTRACT` | pass | Executed structural check found applicability, template and instance locations, initial and closure responsibility, tailoring, seven initialization steps, and mandatory Architect handoff before the canonical template, with no duplicate pre-template ownership table |

## Quality Review

**Owner:** Syspilot Quality<br>
**Status:** proceed

**Current judgment:** Proceed. The Requirement hierarchy, seven-rule workspace instruction, compact Change Process, user-facing documentation, and release-bound instruction delivery are coherent. Commit `893405b` installs and verifies the complete release-owned `.github/instructions/` tree. Acceptance commit `abc6556` replaces the unsupported escalation evidence with committed fixture `8e7c337`, which demonstrates standalone question and actionable blocker escalation messages while both parent and fixture retain Tester responsibility. The strict documentation and schema build passes with zero warnings, all four focused tests pass, the canonical Change template remains unchanged, and no open Quality issue remains.

### Open Quality Issues

None.

## User Validation And Approval

**Owner:** User<br>
**Recorded by:** Syspilot Project Manager<br>
**Status:** accepted

**Decision and evidence:** The User directly accepted the Change in the Syspilot Project Manager session on 2026-08-25 after reviewing the Contract and validating the always-on instruction independently with multiple actors. The User confirmed that actors consistently retain responsibility during escalation and route to the applicable originating actor or User rather than assuming a designated coordination hop. The User authorized merge to `development`; responsibility then transferred to the Syspilot Project Manager for Closure.

## Closure

**Owner:** Syspilot Project Manager<br>
**Status:** closed

- [x] Every included artifact has terminal status and completion evidence.
- [x] Intent and outcome are `approved`.
- [x] Quality has recorded a `proceed` judgment directly to the Syspilot Project Manager.
- [x] Open Quality Issues contains `None`.
- [x] User validation is `accepted`, or its `not applicable` status and autonomous authority are recorded.
- [x] Current blocker is `none`.
- [x] The observable outcome is demonstrated.
- [x] Integration into `development` has been completed by the Syspilot Project Manager through the resulting squash integration commit.

**Final outcome:** The User accepted the concise always-on Contract-handling instruction and compact Change initiation procedure after independently confirming consistent escalation behavior across multiple actors. The instruction preserves one authoritative writer, committed direct handoffs, read-only consultation, and no-transfer questions or escalation without introducing a designated coordination hop. Quality recorded direct `proceed` evidence in `df786d3`; the Syspilot Project Manager closed the Change and integrated `feature/contract-handling` into `development` by squash.