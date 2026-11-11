# Change Contract: v2 Foundation

**Status:** closed<br>
**Process owner:** Syspilot Project Manager<br>
**Current responsibility:** Syspilot Project Manager<br>
**Current blocker:** none<br>
**Created:** 2026-08-24<br>
**Branch:** feature/v2-foundation<br>
**Collaboration mode:** User-guided for product direction, architecture decisions, and closure; otherwise autonomous within the approved intent.

## Intent And Outcome

**Owner:** Syspilot Project Manager<br>
**Status:** approved<br>
**Approval evidence:** User confirmed the v2 Foundation intent and transition to the Change Process on 2026-08-24.

### Goal

Establish the syspilot v2 foundation around Jarvis actors, outcome-oriented Contract Documents, and a Change Process that coordinates work through artifact ownership and current responsibility rather than a dedicated Change Manager or prescribed actor sequence.

### Value

Users and actors can understand, execute, and audit a change from its currently valid intent, owned artifacts, decisions, evidence, and outcome while retaining detailed evolution in Git.

### Scope

- Establish the v2 ontology and specification baseline.
- Preserve the eight public actor role cards while defining one common v2 actor convention and one concrete user-story/requirement chain for each Syspilot actor: Project Manager, Architect, Developer, Tester, Quality, Setup, Release, and Research.
- Define the generic Contract Document method and its story and requirement.
- Define the Change Process, Change Contract template, and their story and requirement.
- Realize the agentless Syspilot actors through their public role cards, v2 specifications, and process documents.
- Remove the duplicated v1 product-copy directory `syspilot/`; v2 release artifacts use their canonical repository locations.
- Remove the temporary v1 specification archive and mark remaining v1-oriented documentation for review or replacement.

Dedicated agent and prompt files are not part of the v2 actor model.

### Observable Outcome

The v2 documentation builds without warnings; the common actor convention, all eight actor roles, the Contract Document method, and the Change Process form valid story/requirement traceability chains; the Change Process is usable through this concrete contract; and the Syspilot Project Manager follows that process without a Change Manager dependency.

## Artifact Applicability And Ownership

**Applicability:** Each artifact owner decides and updates its own row.<br>
**Status:** pending

| Artifact type | Included | Owner | Completion evidence | Status |
|---|---|---|---|---|
| Intent and outcome | yes | Syspilot Project Manager | Goal, value, scope, and observable outcome are explicit and approved | approved |
| Product specification and architecture decisions | yes | Syspilot Architect | Eleven approved US/REQ chains with AC/VC links, reviewed realizations, and clean strict Sphinx evidence | complete |
| Implementation and unit verification | yes | Syspilot Project Manager | Completed under the approved bootstrap exception because this Change first established the process and actor responsibilities needed for normal execution; canonical v2 realizations are present and relevant automated checks pass | complete |
| Acceptance test design and results | yes | Syspilot Tester | Documentation review confirms that roles and process state are inspectable from public artifacts and that incomplete closure is unambiguous | passed |
| Quality review | yes | Syspilot Quality | Current verification judgment is `proceed` and no open quality issue remains | proceed |
| User validation and approval | yes | User | User accepted the demonstrated observable outcome on 2026-08-24 | accepted |
| Closure decision | yes | Syspilot Project Manager | Final outcome and validation disposition are recorded; the Project Manager owns squash integration into `development` | complete |

## Architecture And Specification

**Owner:** Syspilot Architect<br>
**Status:** complete

### Affected Artifacts

| Artifact | Change | Rationale |
|---|---|---|
| `.syspilot/ontology.toml` | modify | Establish the v2 needs types, relations, and lifecycle model |
| `docs/syspilot/` | add / modify | Establish the v2 root, common actor convention, eight actor-role chains, Contract Document chain, and Change Contract chain |
| `docs/Syspilot Processes/contract-documents.md` | add | Define the generic outcome-oriented Contract Document method |
| `docs/Syspilot Processes/change.md` | add | Define the Change Process and canonical Change Contract template |
| `docs/Syspilot Processes/index.md` | modify | Register the v2 process documents |
| `docs/Syspilot Actors/` | add / modify | Realize the common Actor Model and preserve the eight public role cards |
| `docs/syspilot-v1/` | remove | Remove the temporary in-tree v1 archive; released history remains available in Git |
| Remaining v1-oriented documentation | modify | Mark documents for review or replacement during the v2 transition |

### Decisions And Evidence

| Decision or check | Evidence |
|---|---|
| Use Jarvis as the actor runtime and avoid duplicating kernel behavior in syspilot | `SYSP_US_ACTOR_MODEL`, `SYSP_REQ_ACTOR_MODEL`, and the public actor registry |
| Model shared actor structure once without using a template User Story | One common Actor Model US/REQ defines role cards, context links, process-derived authority, and the Jarvis kernel boundary |
| Specify each actor's distinct value and responsibilities independently | One concrete US/REQ chain each for Project Manager, Architect, Developer, Tester, Quality, Setup, Release, and Research, grounded only in the v2 actor registry, process registry, and North Star |
| Realize the Project Manager without a dedicated syspilot agent or prompt | The authoritative Project Manager role card and `SYSP_REQ_PROJECT_MANAGER` define an agentless Jarvis actor through the default Copilot session |
| Use Contract Documents as durable current state rather than event logs | `SYSP_US_CONTRACT_DOCUMENTS`, `SYSP_REQ_CONTRACT_DOCUMENTS`, and the realized method |
| Coordinate changes through artifact ownership and current responsibility rather than a Change Manager | `SYSP_US_CHANGE_CONTRACT`, `SYSP_REQ_CHANGE_CONTRACT`, and the realized Change Process |
| Select the next responsible owner from included work that can progress instead of prescribing an actor sequence | Generic handoff rule and Change Contract requirement |
| Preserve detailed document evolution in Git while keeping outcome evidence in the current contract | Contract Document state and evidence rules |
| Bootstrap the v2 method through Project Manager-authored process and specification drafts | The responsible v2 actors and process were not yet available; each artifact owner retains authority to review and complete the drafted artifact |
| Align the bootstrap branch with the initialized Change Contract | Rename `initial-cleanup` to `feature/v2-foundation` before transferring responsibility |
| v2 specification graph is complete and approved | Exported graph contains 44 approved elements across eleven chains: eleven each of story, requirement, acceptance criterion, and verification criterion |
| Documentation and needs graph remain structurally valid | Clean full Sphinx build with warnings treated as errors passes; four documentation build-script unit tests pass |

## Implementation And Unit Verification

**Owner:** Syspilot Project Manager<br>
**Status:** complete

**Bootstrap exception:** The Project Manager completed this artifact because
the Change Process and its regular actor responsibilities had to be defined by
this Change before they could be followed. This exception applies only to the
`v2-foundation` Change Contract; subsequent Changes retain the canonical
Developer ownership.

### Decisions And Evidence

| Decision | Chosen approach | Relevant alternatives | Rationale and evidence |
|---|---|---|---|
| Remove Change Manager dependency from Project Manager coordination | Let the Change Contract route responsibility between artifact owners | Retain or replace the Change Manager with another coordinator | The artifact table, current responsibility, and handoff invariant provide the required coordination state |

### Changed Artifacts And Verification

| Artifact | Change | Verification evidence |
|---|---|---|
| `docs/Syspilot Actors/` and `docs/Syspilot Processes/` | Realize the agentless v2 actors and their shared processes | Strict Sphinx build succeeds without warnings; all four focused documentation tests pass |
| `syspilot/` | Remove duplicated v1 product-copy tree | Directory removed; active v2 source scan finds no dependency on its former agent, skill, template, bootstrap, or Sphinx paths |

## Acceptance Testing

**Owner:** Syspilot Tester<br>
**Status:** passed

| Scenario | Traces to | Result | Evidence |
|---|---|---|---|
| A process participant follows the common Actor Model to each of the eight public role cards and actor contexts | `SYSP_AC_ACTOR_MODEL_1` | pass | All eight actor contexts link to their matching public role card and the process registry; the Actor Model identifies process-derived authority and the Jarvis kernel boundary |
| A participant inspects this Change Contract without prior conversation and determines the valid state and next responsible owner | `SYSP_AC_CONTRACT_DOCUMENTS_1` | pass | Intent, artifact statuses, current responsibility, blocker, evidence, and closure checklist are explicit in the current document |
| A participant challenges premature closure while Quality, User validation, and Closure remain pending | `SYSP_AC_PROJECT_MANAGER_1`, `SYSP_AC_CHANGE_CONTRACT_1` | pass | The pending artifact rows and unchecked closure conditions make closure unavailable and route the next review to Syspilot Quality |

## Quality Review

**Owner:** Syspilot Quality<br>
**Status:** proceed

**Current judgment:** Proceed. The corrected Architecture evidence matches the reproducible eleven-chain, 44-element v2 graph. A clean strict documentation build passes with zero warnings and schema violations, all four focused documentation tests pass, and the actor/process realizations support the approved intent.

### Open Quality Issues

None.

## User Validation And Approval

**Owner:** User<br>
**Recorded by:** Syspilot Project Manager<br>
**Status:** accepted

**Decision and evidence:** User accepted the demonstrated observable outcome on 2026-08-24 after Quality recorded its `proceed` judgment.

## Closure

**Owner:** Syspilot Project Manager<br>
**Status:** closed

- [x] Every included artifact has terminal status and completion evidence.
- [x] Intent and outcome are `approved`.
- [x] Quality has recorded a `proceed` judgment.
- [x] Open Quality Issues contains `None`.
- [x] User validation is `accepted`, or its `not applicable` status and autonomous authority are recorded.
- [x] Current blocker is `none`.
- [x] The observable outcome is demonstrated.
- [x] Integration or publication has been completed by the authorized actor, or its next owner is explicit.

**Final outcome:** The user accepted the demonstrated v2 foundation. The Syspilot Project Manager owns closure and squash integration of `feature/v2-foundation` into `development`. Syspilot Release remains uninvolved until an actual release integrates `development` into `main`, versions, tags, and publishes the product.
