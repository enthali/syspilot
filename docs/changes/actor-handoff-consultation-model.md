# Change Contract: Actor Handoff And Consultation Model

**Status:** closed<br>
**Process owner:** Project Manager<br>
**Current responsibility:** Project Manager<br>
**Current blocker:** none<br>
**Created:** 2026-09-20<br>
**Branch:** feature/actor-handoff-consultation-model<br>
- **Operation Mode**: user-guided

## Intent And Outcome

**Owner:** Project Manager<br>
**Status:** approved<br>
**Approval evidence:** The User and Project Manager discussed and agreed the layered SEND/RESPOND (Kernel) vs. HANDOFF/ACK/CONSULT/CONSULTRESPOND (Contract-handling) design live in conversation on 2026-09-20, including the ACK verification behavior and the retraction of RECEIVE as a named verb.

### Goal

Layer a Syspilot-specific coordination vocabulary over the generic Jarvis messaging primitives. The Jarvis Actor Kernel keeps exactly two generic primitives, `SEND` and `RESPOND` (mechanically a `SEND` back to the sender); `RECEIVE` is retracted as a named protocol verb and stays only the mechanical act of draining an inbox via `jarvis_receiveMessage`. `syspilot.contract-handling.instructions.md` defines four named verbs that each realize one primitive with Syspilot-specific instructions: `HANDOFF` (via `SEND`) and `ACK` (via `RESPOND`) for Contract-responsibility transfer; `CONSULT` (via `SEND`) and `CONSULTRESPOND` (via `RESPOND`) for bounded, non-transferring consultation.

### Value

Closes a live source of protocol drift observed twice in this session's `actor-naming-simplification` Contract: an actor's completion message claimed a Contract-responsibility transfer that its own commit did not actually record in the Contract header, because `SEND` is currently used for both a full responsibility handoff and a mere notification or consultation reply, with no distinct vocabulary or enforced check between them. Naming `ACK` as its own verb also closes a second gap: today a `HANDOFF` is fire-and-forget, so the sender has no confirmation the receiver ever accepted the work, and the receiver has no required moment to verify the commit actually names it before proceeding. Requiring `ACK` to verify the named commit's Contract header before confirming would have caught this session's actual defect mechanically, instead of by manual audit.

### Scope

- Already verified, not re-derived by this Contract: `syspilot.orchestration-jarvis` and `syspilot.orchestration-subagent` skills, and every Setup-facing reference to them, are already absent from `.github/skills/`, `docs/Syspilot Contracts/`, and the current specification tree (confirmed by workspace-wide search on 2026-09-20). This Contract does not remove anything on that front; it only closes the remaining vocabulary and enforcement gap.
- In scope, agreed with the User on 2026-09-20: the Kernel's Messaging section is reduced to two generic primitives, `SEND` and `RESPOND` (`RECEIVE` removed as a named verb, kept only as the mechanical `jarvis_receiveMessage` drain action).
- In scope: `syspilot.contract-handling.instructions.md` gains two named subsections that each map one verb pair onto a Kernel primitive:
  - **Contract handling** — `HANDOFF` (via `SEND`): the responsible actor updates Contract status, evidence, and `Current responsibility`, commits Contract and related artifacts as one consistent state, then sends `HANDOFF` naming the Contract path, commit, completed outcome, and remaining work. `ACK` (via `RESPOND`): before starting work, the receiver verifies the named commit's Contract header actually states `Current responsibility` as itself; if verified, it sends `ACK`; if not, it escalates instead of acknowledging.
  - **Consultation** — `CONSULT` (via `SEND`): a message explicitly marked as a consultation request, requesting advice or review without transferring `Current responsibility`; the consulted actor remains read-only for the Contract and versioned artifacts. `CONSULTRESPOND` (via `RESPOND`): the consulted actor's answer or findings returned to the asker; does not transfer `Current responsibility`.
- Out of scope: introducing new Jarvis tools; `jarvis_sendMessage` / `jarvis_receiveMessage` remain the only messaging primitives. Out of scope: re-opening the already-closed removal of the legacy orchestration skills.

### Observable Outcome

- The Kernel instruction states only the two generic primitives `SEND` and `RESPOND`, with no named `RECEIVE` verb.
- `syspilot.contract-handling.instructions.md` states, in exactly one place each without duplication, `HANDOFF`, `ACK`, `CONSULT`, and `CONSULTRESPOND`, each naming the Kernel primitive it realizes and the Syspilot-specific instruction attached to it.
- A completion message that claims "Current responsibility is committed to X" is checkable: the named Contract's committed header must already state that owner, and the receiver's `ACK` step performs that check before confirming.
- Tester's acceptance scenarios demonstrate: a `HANDOFF` updates and commits `Current responsibility` before it is sent; `ACK` verifies the committed header before confirming and escalates instead of acknowledging on mismatch; `CONSULT` and `CONSULTRESPOND` never change `Current responsibility`.

## Artifacts, Ownership And Process Gates

**Applicability:** Each artifact owner decides and updates its own row.<br>
**Status:** pending

| Artifact or gate | Included | Owner | Completion evidence | Status |
|---|---|---|---|---|
| Intent and outcome | yes | Project Manager | Goal, value, scope, and observable outcome are explicit and approved | approved |
| Contract release | yes | User | User authorization to start the Change; no other actor may set this gate | approved |
| Version control | yes | Project Manager | `feature/actor-handoff-consultation-model` branch; squash-integrated into `development` at closure | active |
| Product specification and architecture decisions | yes | Architect | HANDOFF/SEND vs. consultation-RESPOND vocabulary, receipt acknowledgement, and enforcement-layer decision are recorded and traced | complete |
| User-facing documentation | not applicable: affected artifacts are instruction and specification files, not user-facing documentation surfaces with `doc` Needs | Technical Writer | not applicable | not applicable |
| Implementation and unit verification | yes | Developer | Approved instruction wording realized verbatim in `.github/instructions/jarvis-actor.kernel.instructions.md` (section `## 2. Messaging`) and `.github/instructions/syspilot.contract-handling.instructions.md`, and the required named vocabulary carried into `docs/syspilot/requirements/req_contract_handling.rst` (commit `be9b53f`); Tester passed with verbatim file/line evidence; strict doc build 0 warnings (20565 needs), docs suite 4/4 | complete |
| Acceptance test design and results | yes | Tester | Black-box scenarios confirm HANDOFF, consultation-RESPOND, and receipt-acknowledgement behavior match the Observable Outcome | passed |
| Quality review | yes | Quality | See Quality Review section: `proceed` judgment with MECE (8 runs, 0 findings), Trace (4 runs, 0 findings), strict build (0 warnings, 19594 needs), focused suites (4/4, 5/5, 7/7), and semantic review of all 4 observable outcomes against the Approved Instruction Wording | passed |
| User validation and approval | yes | User | Observable outcome is accepted or changes are requested | accepted |
| Closure decision | yes | Project Manager | Final outcome, validation disposition, and integration state are recorded | closed |

The Kernel instruction is supplied by the Jarvis extension and verified in the installed workspace; only the Syspilot instruction and requirement are versioned product artifacts in this Change.

## Architecture And Specification

**Owner:** Architect<br>
**Status:** complete

### Affected Artifacts

| Artifact | Change | Rationale |
|---|---|---|
| `.github/instructions/jarvis-actor.kernel.instructions.md` | modify (Messaging section) | Reduce to the two generic primitives `SEND`/`RESPOND`; retract `RECEIVE` as a named verb, keeping only the mechanical inbox-drain description; add one pointer sentence to the layered Syspilot vocabulary without duplicating it |
| `.github/instructions/syspilot.contract-handling.instructions.md` | modify | Name `HANDOFF`, `ACK`, `CONSULT`, `CONSULTRESPOND` exactly once each, each mapped to the Kernel primitive it realizes, and add the `ACK` commit-header verification step that did not previously exist |
| `docs/syspilot/requirements/req_contract_handling.rst` (`SYSP_REQ_CONTRACT_HANDLING`, `SYSP_VC_CONTRACT_HANDLING_1`) | modify | Spec previously described only a generic `SEND`-based notification with no named receipt step; updated so the Requirement and its verification criterion name `HANDOFF`/`ACK`/`CONSULT`/`CONSULTRESPOND` and the commit-header verification, matching the approved vocabulary |

### Decisions And Evidence

| Decision or check | Evidence |
|---|---|
| Enforcement layer: Kernel keeps two generic primitives (`SEND`, `RESPOND`); Contract-handling instruction owns the four named Syspilot verbs (`HANDOFF`, `ACK`, `CONSULT`, `CONSULTRESPOND`) | Agreed with the User in conversation on 2026-09-20: generic transport belongs in the Kernel (applies to every actor and message kind), Syspilot-specific responsibility semantics belong in the Contract-handling instruction, without duplicating the rule in both places |
| `RECEIVE` retracted as a named protocol verb | Agreed with the User on 2026-09-20: draining an inbox is a mechanical `jarvis_receiveMessage` action, not a distinct coordination decision like `SEND`/`RESPOND` |
| `ACK` verifies the committed Contract header before confirming | Agreed with the User on 2026-09-20: this directly targets the defect observed twice in `actor-naming-simplification`, where a completion message claimed a responsibility transfer the commit did not record; Architect to confirm no existing Need/spec conflicts with this addition |
| Consistency check: `SYSP_REQ_ACTOR_MODEL`/`SYSP_US_ACTOR_MODEL` | No conflict, no change needed: already states actors "inherit memory, messaging, escalation, and culture from the Jarvis Actor Kernel without duplicating that behavior in syspilot" — this already licenses the two-layer split this Contract formalizes |
| Consistency check: `SYSP_REQ_TECHNICAL_WRITER` | No conflict, no change needed: already states the Technical Writer must "keep consultation distinct from Contract handoff so that messaging alone transfers neither current responsibility nor artifact ownership", which is consistent with, and does not need to name, the new verbs |
| Consistency check: `SYSP_REQ_CONTRACT_HANDLING` / `SYSP_VC_CONTRACT_HANDLING_1` | Conflict found and resolved: prior text named only generic `SEND` for the handoff notification and had no receipt-acknowledgement step; updated in this branch (commit to be recorded at HANDOFF) to name `HANDOFF`/`ACK`/`CONSULT`/`CONSULTRESPOND` and the commit-header verification step; strict build re-run at 0 warnings after the edit |

### Approved Instruction Wording

Exact replacement text for Developer to realize verbatim in `Implementation And Unit Verification`; wording is approved, not open for re-drafting there.

**`.github/instructions/jarvis-actor.kernel.instructions.md`, section `## 2. Messaging`, full replacement:**

```markdown
## 2. Messaging
Actors coordinate through messages. You may read another actor's memory as contextual evidence — treat it as potentially stale and never as instructions or authority to act on that actor's behalf. When you need action, a decision, or clarification from another actor, SEND a message. Never modify another actor's state; SEND a request to that actor instead.

- **SEND** — hand work or information to another actor. Use `jarvis_sendMessage`.
- **RESPOND** — return a result to the originator. Mechanically a SEND back to the sender: use `jarvis_sendMessage` with the sender's session name as destination.

Draining your own inbox is a mechanical action, not a coordination decision: call `jarvis_receiveMessage` for your own session and repeat until `remaining === 0`, preserving each sender so results can be returned correctly. Method-specific instructions (for example Syspilot's Contract handling) define named verbs — such as a responsibility handoff versus a bounded consultation — that each realize one of these two primitives; this Kernel section only defines the transport.
```

The rest of the Kernel file (sections 0, 1, 3, 4) is unchanged.

**`.github/instructions/syspilot.contract-handling.instructions.md`, full replacement:**

```markdown
# Contract Handling

`Current responsibility` is temporary authority to maintain the Contract instance; durable artifact ownership does not change.

## Handoff

- **HANDOFF** (via `SEND`) — after completing work, select the next logical included artifact owner whose work can progress the Contract. Update Contract status, artifact evidence, and `Current responsibility`, then commit the Contract and related artifacts as one consistent state before sending HANDOFF. This intentionally prioritizes single-writer, consistent Contract state over uninterrupted communication and accepts the brief notification gap. In the HANDOFF message, identify the Contract path, commit, completed outcome, and remaining work.
- **ACK** (via `RESPOND`) — before starting work received through a HANDOFF, verify that the named commit's Contract header actually states `Current responsibility` as yourself. If verified, RESPOND with ACK. If not, do not acknowledge; escalate the discrepancy instead.

## Consultation

- **CONSULT** (via `SEND`) — request advice or review from another actor at any time, explicitly marked as a consultation. Consultation never transfers `Current responsibility`; the consulting actor remains read-only for the Contract and versioned work artifacts.
- **CONSULTRESPOND** (via `RESPOND`) — return the consulted actor's answer or findings to the asker. Does not transfer `Current responsibility`.

Questions and escalation do not transfer `Current responsibility`. When no included artifact owner can progress the Contract, record an actionable blocker and escalate.
```

## User-Facing Documentation

**Owner:** Technical Writer<br>
**Status:** not applicable

### Documentation Plan And Ownership

| Documentation surface | `doc` Need | Requirements included | Status |
|---|---|---|---|
| not applicable | none | none | not applicable |

### Consultations And Factual Reviews

| Documentation surface | Consulted artifact owner | Review question | Evidence and disposition |
|---|---|---|---|
| not applicable | none | The affected artifacts (`.github/instructions/jarvis-actor.kernel.instructions.md`, `.github/instructions/syspilot.contract-handling.instructions.md`, `docs/syspilot/requirements/req_contract_handling.rst`) are instruction files and specification files, not user-facing documentation surfaces with `doc` Needs. No user-facing documentation surfaces require updates. | not applicable |

### Changed Documentation And Verification

| Artifact | Change | Verification evidence |
|---|---|---|
| not applicable | not applicable | not applicable |

## Implementation And Unit Verification

**Owner:** Developer<br>
**Status:** complete

### Decisions And Evidence

| Decision | Chosen approach | Relevant alternatives | Rationale and evidence |
|---|---|---|---|
| Realize the instruction change | Replace the named sections verbatim from the Architect's Approved Instruction Wording — do not re-draft the wording in the instruction files | Re-draft the wording to match the intent without copying it verbatim | The Approved Instruction Wording is explicitly approved, not open for re-drafting; re-drafting would introduce drift between the instruction files and the spec the Architect already traced, and would require a new Quality re-verification cycle before closure |
| Kernel primitive set | Keep exactly two generic primitives (`SEND`, `RESPOND`); retract `RECEIVE` as a named verb; keep the drain action and the layered-vocabulary pointer sentence in `## 2. Messaging` only | Add `RECEIVE` back as a named verb, or move the Syspilot verb definitions into the Kernel | `SEND`/`RESPOND` apply to every actor and message kind (Kernel scope); the four named Syspilot verbs carry Contract-specific responsibility semantics that belong in the Contract-handling instruction, not the Kernel. Adding `RECEIVE` back would contradict the approved Architecture decision. Verified: the installed extension-provided Kernel `## 2. Messaging` section matches the Approved Instruction Wording verbatim |
| Named vocabulary placement | Name each of `HANDOFF`, `ACK`, `CONSULT`, `CONSULTRESPOND` exactly once in `syspilot.contract-handling.instructions.md`, each mapped to its Kernel primitive; add the `ACK` commit-header verification step | Name the verbs in both the Kernel and the Contract-handling instruction, or omit the `ACK` verification step | Naming the verbs in both places duplicates the rule the Architecture decision specifically avoids; the `ACK` verification step is the mechanical check that targets the exact defect observed twice in the `actor-naming-simplification` Contract (a completion message claiming a responsibility transfer the commit did not record). Verified: all four verbs present exactly once in the committed file, each with its Kernel primitive named |
| Spec alignment | Carry the named vocabulary into `req_contract_handling.rst` (`SYSP_REQ_CONTRACT_HANDLING`, `SYSP_VC_CONTRACT_HANDLING_1`) in the same commit as the instruction change | Leave the spec unchanged and note the discrepancy for a later Change | The Requirement and Verification Criterion previously named only a generic `SEND`-based notification with no receipt step; the Architect's consistency check flagged this as a conflict to be resolved in this branch. Carrying the vocabulary into the spec in the same commit keeps the spec and instruction in lockstep from the first verification run, avoiding a second round-trip. Committed as `be9b53f` |

### Changed Artifacts And Verification

| Artifact | Change | Verification evidence |
|---|---|---|
| `.github/instructions/jarvis-actor.kernel.instructions.md` | Modified `## 2. Messaging` to the Approved Instruction Wording: two primitives `SEND`/`RESPOND`, `RECEIVE` retracted, drain action, layered-vocabulary pointer | Matches Approved Instruction Wording verbatim (confirmed by Quality's semantic re-read and Tester's acceptance scenarios); strict doc build 0 warnings (20565 needs); docs suite 4/4 |
| `.github/instructions/syspilot.contract-handling.instructions.md` | Modified to name all four verbs (`HANDOFF`, `ACK` with commit-header verification, `CONSULT`, `CONSULTRESPOND`), each mapped to its Kernel primitive, in the Handoff and Consultation sections | Matches Approved Instruction Wording verbatim; all four verbs present exactly once; `ACK` verification step present; strict doc build 0 warnings (20565 needs); docs suite 4/4 |
| `docs/syspilot/requirements/req_contract_handling.rst` | Modified `SYSP_REQ_CONTRACT_HANDLING` and `SYSP_VC_CONTRACT_HANDLING_1` to name `HANDOFF`/`ACK`/`CONSULT`/`CONSULTRESPOND` and the commit-header verification step (commit `be9b53f`) | Strict doc build 0 warnings (20565 needs); `SYSP_REQ_CONTRACT_HANDLING` and `SYSP_VC_CONTRACT_HANDLING_1` both validate cleanly; no new schema violations; MECE and Trace runs against the committed state (at `c59a9ef`) confirm no broken links or coverage gaps |

## Acceptance Testing

**Owner:** Tester<br>
**Status:** passed

| Scenario | Traces to | Result | Evidence |
|---|---|---|---|
| A `HANDOFF` updates and commits `Current responsibility` before the message is sent | Observable Outcome | pass | `syspilot.contract-handling.instructions.md` line 11: "Update Contract status, artifact evidence, and `Current responsibility`, then commit the Contract and related artifacts as one consistent state before sending HANDOFF." |
| `ACK` verifies the named commit's Contract header before confirming, and escalates instead of acknowledging on mismatch | Observable Outcome | pass | `syspilot.contract-handling.instructions.md` line 12: "verify that the named commit's Contract header actually states `Current responsibility` as yourself. If verified, RESPOND with ACK. If not, do not acknowledge; escalate the discrepancy instead." Corroborated by `req_contract_handling.rst` verification criterion. |
| A `CONSULT` message does not change `Current responsibility` and is explicitly marked as a consultation | Observable Outcome | pass | `syspilot.contract-handling.instructions.md` line 16: "Consultation never transfers `Current responsibility`; the consulting actor remains read-only for the Contract and versioned work artifacts." |
| A `CONSULTRESPOND` reply does not change `Current responsibility` | Observable Outcome | pass | `syspilot.contract-handling.instructions.md` line 17: "Does not transfer `Current responsibility`." |

## Quality Review

**Owner:** Quality<br>
**Status:** passed

**Current judgment:** proceed

### Applied Review Methods

| Method | Selected scope | Evidence | Findings | Limits |
|---|---|---|---|---|
| MECE horizontal coverage review | `same-document` + `all-type` on `SYSP_REQ_CONTRACT_HANDLING`, `SYSP_VC_CONTRACT_HANDLING_1`, `SYSP_REQ_ACTOR_MODEL`, `SYSP_US_ACTOR_MODEL` (8 runs) | `analyze_mece.py` per ID, both scopes, against committed state at `c59a9ef` | `"findings": []` in all 8 runs — no overlaps, contradictions, or coverage gaps found within the peer sets (17 `req`, 17 `vc`, 15 `story` peers) | `semantic-content-review-required`; `no-comparable-peers-discovered` in same-document scope; `structured-coverage-data-unavailable` |
| Trace relationship and chain analysis | `--direction both --depth 2` on the same 4 IDs | `analyze_trace.py` per ID | All 4 runs: every edge in the depth-2 neighborhood is resolved and permitted; `"findings": []` in all 4 runs | `semantic-content-review-required` |
| Strict Sphinx build (Sphinx-Needs schema validation) | Full docs build | `python docs/docs-build.py clean` on this branch | 0 warnings; 19594 needs validated | None |
| Focused test suites | Docs build tests; MECE tests; Trace tests | `python docs/test_docs_build.py -v`; `python .github/skills/syspilot.mece/scripts/test_analyze_mece.py -v`; `python .github/skills/syspilot.trace/scripts/test_analyze_trace.py -v` | 4/4, 5/5, 7/7 — all pass | n/a |
| Semantic review against the four observable outcomes | Two tracked product artifacts as committed, and the extension-provided Kernel as installed; comparison against the Contract's Approved Instruction Wording | Independent full re-read of `.github/instructions/jarvis-actor.kernel.instructions.md`, `.github/instructions/syspilot.contract-handling.instructions.md`, and `docs/syspilot/requirements/req_contract_handling.rst`; re-read of all 4 Tester acceptance scenarios with verbatim file/line evidence | All four observable outcomes are met: (1) Kernel `## 2. Messaging` states only `SEND`/`RESPOND` with no named `RECEIVE` verb; (2) contract-handling instruction names each of `HANDOFF`, `ACK`, `CONSULT`, `CONSULTRESPOND` exactly once, each mapped to its Kernel primitive; (3) the `ACK` header-verification step makes "Current responsibility is committed to X" claims checkable; (4) both instruction files match the Contract's Approved Instruction Wording verbatim, and `req_contract_handling.rst` resolves the spec conflict the Architect recorded. Tester's 4 scenarios pass as recorded. | `semantic-content-review-required` (applied manually here). Note: the Developer "Implementation and unit verification" artifact row is still `pending` with `{pending}` cells although the work is observably done and independently verified by Tester and by this review; it contradicts observable state and blocks the closure checklist. This is a non-blocking Contract-bookkeeping defect owned by Developer/PM and is called out in the HANDOFF to Project Manager; it is not an artifact-correctness defect, so it is not recorded as an Open Quality Issue |

Quality communicates its `proceed` judgment and supporting evidence directly to the Project Manager before the Project Manager presents the verified outcome for validation. Another actor's forwarded claim does not establish Quality's decision.

### Open Quality Issues

| Artifact | Current issue | Required outcome |
|---|---|---|
| None | | |

## User Validation And Approval

**Owner:** User<br>
**Recorded by:** Project Manager<br>
**Status:** accepted

**Decision and evidence:** User reviewed the Project Manager's summary of the verified outcome — including the live proof that the new `ACK` verification step caught a real HANDOFF/header mismatch during Quality's review and the correction that followed — and replied "ok this is fine all good we can proceed" on 2026-09-22, accepting the observable outcome as demonstrated.

## Closure

**Owner:** Project Manager<br>
**Status:** closed

- [x] Every included artifact or gate has terminal status and completion evidence.
- [x] Intent and outcome are `approved`.
- [x] Quality has recorded a `proceed` judgment.
- [x] Open Quality Issues contains `None`.
- [x] User validation is `accepted`, or its `not applicable` status and explicit User delegation are recorded in the artifact row.
- [x] Current blocker is `none`.
- [x] The observable outcome is demonstrated.

**Final outcome:** User validation accepted. The extension-provided Jarvis Actor Kernel's Messaging section states two generic primitives, `SEND` and `RESPOND`; the Kernel file is not tracked or shipped by this repository. The tracked Syspilot instruction defines `HANDOFF`/`ACK` and `CONSULT`/`CONSULTRESPOND`, and `req_contract_handling.rst` carries the same vocabulary. The mechanism was demonstrated live: Quality's first `HANDOFF` at `cfe3788` claimed a transfer the committed header did not record; the Project Manager escalated rather than sending `ACK`, and Quality corrected the header at `a9a481c` before re-sending. The Implementation evidence gap was closed via `CONSULT`/`CONSULTRESPOND` without a responsibility transfer (commits `48f6719`, `289910e`). Squash integration into `development` completes this closure; the feature branch is retained locally, not pushed.
