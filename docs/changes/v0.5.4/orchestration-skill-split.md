# Change Request: orchestration-skill-split

**Status**: in-progress
**Created**: 2026-05-19
**Branch**: feature/orchestration-skill-split
**Author**: PM

---

## WHY

The current `syspilot.orchestration` skill mixes sync and async communication
in a single non-exchangeable standalone skill. When the async backend changes,
every agent must change. Additionally, the skill references specific agent roles,
coupling it to the current topology. A separate concern: agents can be called both
synchronously and asynchronously but must currently choose different reporting verbs —
that detection belongs in the skill.

---

## WHAT

Replace `syspilot.orchestration` with an `orchestration` skill group. The group
contract defines four UPPERCASE vocabulary terms. The skill content describes
communication patterns only — no agent names, no orchestration matrix.

**Vocabulary (DEFINITIONS in the Group Contract Spec):**

- `INVOKE` — synchronous call; caller blocks, callee returns structured result
- `SEND` — deliver a message to another session
- `RECEIVE` — check inbox for pending messages
- `RESPOND` — deliver your result; skill auto-detects invocation mode via RECEIVE:
  if a message triggered the work, RESPOND routes back to sender; otherwise direct
  structured output

**Skill implementation delivered in this CR:**

- `syspilot.orchestration-jarvis` — SEND/RECEIVE/RESPOND use `jarvis_sendToSession` /
  `jarvis_readMessage`; enables parallel Change Manager sessions

Note: `syspilot.orchestration-sync` (no external tooling, blocking SEND, no parallelism)
is deferred to a follow-up CR.

---

## Acceptance Criteria

- AC-1: Group Contract Spec `SYSP_SPEC_SKILL_ORCHESTRATION_CONTRACT` exists, declares
  DEFINITIONS: INVOKE, SEND, RECEIVE, RESPOND with the semantics above
- AC-2: `syspilot.orchestration-jarvis` exists, implements all 4 DEFINITIONS using
  `runSubagent` (INVOKE) and `jarvis_sendToSession` / `jarvis_readMessage` (SEND, RECEIVE, RESPOND)
- AC-3: RESPOND performs invocation-mode detection internally via RECEIVE — agents call
  RESPOND uniformly regardless of how they were invoked
- AC-4: Skill content describes patterns only — no agent names, no "who orchestrates whom"
- AC-5: `syspilot.orchestration` standalone skill is removed; Artefakt-Removal-Check
  completed for all references
- AC-6: All agents currently referencing `syspilot.orchestration` are updated to reference
  the new group contract

---

## Impact Analysis

### Artefakt Removal: `syspilot.orchestration`

Grep performed on all plausible variants. Results classified:

| Removed Artefact | Class (a): Code/Workflow refs | Class (b): Doc refs | Class (c): Historic Change Docs |
|------------------|-------------------------------|---------------------|---------------------------------|
| `syspilot.orchestration` | `syspilot/skills/syspilot.orchestration/SKILL.md`, `.github/skills/syspilot.orchestration/SKILL.md` → delete | `docs/architecture.md`, `docs/methodology.md`, `docs/syspilot/conventions.md`, `docs/syspilot/design/spec_skill_orchestration.rst`, `docs/syspilot/requirements/req_skill_orchestration.rst`, `docs/syspilot/design/spec_skill_arch.rst` → update | `docs/changes/` references, `.jarvis/` session files, `docs/releasenotes.md` — acceptable historic stranding |

- [ ] All class (a) active code/workflow references fixed in this CR
- [ ] All class (b) active documentation references fixed in this CR
- [x] Class (c) historical Change Documents and session files accepted as "acceptable historic stranding"

---

## Level 0: User Stories

**Status**: ✅ completed

### Impacted User Stories

| ID | Title | Impact | Notes |
|----|-------|--------|-------|
| SYSP_US_SKILL_ORCHESTRATION | Orchestration skill | modified | Vocab changes: DELEGATE→SEND/RECEIVE; REPLY→RESPOND; new RECEIVE verb |

---

## Level 1: Requirements

**Status**: ✅ completed

### Impacted Requirements

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| SYSP_REQ_SKILL_ORCHESTRATION_INVOKE | SYSP_US_SKILL_ORCHESTRATION | modified | Vocab: INVOKE keeps, DELEGATE replaced by SEND, REPLY replaced by RESPOND, new RECEIVE |
| SYSP_REQ_SKILL_ORCHESTRATION_GROUP | SYSP_US_SKILL_ORCHESTRATION | modified | Default variant: no longer `syspilot.orchestration` (removed); `syspilot.orchestration-jarvis` is delivered in this CR |
| SYSP_REQ_SKILL_ORCHESTRATION_AGENT_VOCAB | SYSP_US_SKILL_ORCHESTRATION | modified | Verb routing table updated to INVOKE/SEND/RECEIVE/RESPOND |

---

## Level 2: Design Specs

**Status**: ✅ completed

### Impacted Design Specs

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| SYSP_SPEC_SKILL_ORCHESTRATION_CONTRACT | SYSP_REQ_SKILL_ORCHESTRATION_INVOKE; SYSP_REQ_SKILL_ORCHESTRATION_GROUP | **added** | Group Contract Spec with DEFINITIONS: INVOKE, SEND, RECEIVE, RESPOND |
| SYSP_SPEC_SKILL_ORCHESTRATION_VERB_MODEL | SYSP_REQ_SKILL_ORCHESTRATION_INVOKE | modified | Renamed to Jarvis Variant; 4-verb mapping with RESPOND mode-detection |
| SYSP_SPEC_SKILL_ORCHESTRATION_GROUP | SYSP_REQ_SKILL_ORCHESTRATION_GROUP | modified | Removed default variant; references DEFINITIONS in CONTRACT spec |
| SYSP_SPEC_SKILL_ORCHESTRATION_AGENT_VOCAB | SYSP_REQ_SKILL_ORCHESTRATION_AGENT_VOCAB | modified | Routing table: INVOKE/SEND/RECEIVE/RESPOND; added jarvis_readMessage to prohibited list |
| SYSP_SPEC_SKILL_ORCHESTRATION_PATTERN | SYSP_REQ_SKILL_ORCHESTRATION_INVOKE | modified | Three-phase description uses INVOKE/SEND/RECEIVE/RESPOND |
| SYSP_SPEC_SKILL_ORCHESTRATION_MATRIX | SYSP_REQ_SKILL_ORCHESTRATION_FRONTMATTER | modified | Stripped agent-specific rows; repurposed as generic constraint spec |

---

## Level 2: Design

**Status**: 🔄 in progress

### New Design Elements

| ID | Title | Links |
|----|-------|-------|
| SYSP_SPEC_SKILL_ORCHESTRATION_CONTRACT | Group Contract Spec | SYSP_REQ_SKILL_ORCHESTRATION_INVOKE, SYSP_REQ_SKILL_ORCHESTRATION_GROUP |

### Impacted Design Elements

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| SYSP_SPEC_SKILL_ORCHESTRATION_VERB_MODEL | SYSP_REQ_SKILL_ORCHESTRATION_INVOKE | modified | Replace INVOKE/DELEGATE/REPLY mapping → INVOKE/SEND/RECEIVE/RESPOND; update to jarvis variant |
| SYSP_SPEC_SKILL_ORCHESTRATION_GROUP | SYSP_REQ_SKILL_ORCHESTRATION_GROUP | modified | Default variant updated; `syspilot.orchestration` entry removed |
| SYSP_SPEC_SKILL_ORCHESTRATION_AGENT_VOCAB | SYSP_REQ_SKILL_ORCHESTRATION_AGENT_VOCAB | modified | Verb routing table updated |

---

## Final Consistency Check

**Status**: ⏳ not started

### Artefakt-Removal-Check

*Artefakt removed: `syspilot.orchestration` (directory + SKILL.md)*

| Removed Artefact | Class (a): Code/Workflow refs | Class (b): Doc refs | Class (c): Historic Change Docs |
|------------------|-------------------------------|---------------------|---------------------------------|
| `syspilot/skills/syspilot.orchestration/` | deleted in this CR | n/a | n/a |
| `.github/skills/syspilot.orchestration/` | deleted in this CR | n/a | n/a |
| name reference `syspilot.orchestration` | n/a | spec_skill_orchestration.rst, req_skill_orchestration.rst, spec_skill_arch.rst, conventions.md, architecture.md, methodology.md → updated in this CR | docs/changes/ entries, .jarvis/ session files, releasenotes.md → acceptable historic stranding |

- [ ] All class (a) active code/workflow references fixed in this CR
- [ ] All class (b) active documentation references fixed in this CR
- [x] Class (c) historical references accepted as "acceptable historic stranding"

### Sign-off

- [ ] All levels completed
- [ ] All conflicts resolved
- [ ] Traceability verified
- [ ] Ready for implementation
