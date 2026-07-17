# Change Document: simplify-orchestration-jarvis-skill

**Status**: ready-for-merge
**Branch**: feature/simplify-orchestration-jarvis-skill
**Created**: 2026-07-17
**Author**: PM + User
**GH Issue**: #47
**Operation Mode**: autonomous

---

## Summary

The `syspilot.orchestration-jarvis` skill (`SKILL.md`) carries three kinds of content that no longer belong in a shared orchestration vocabulary skill:

1. **Runtime RESPOND mode-detection logic** — the skill explains how an agent should decide at runtime whether to SEND its result back or emit direct output, based on whether RECEIVE found a pending message. This is unnecessary: the skill variant itself determines the mode statically at install time. No runtime branching logic is needed.
2. **The `agents:` frontmatter / `runSubagent` exception section** — a carve-out for the Setup Bootloader's `runSubagent` call to the Installer. This is not the shared skill's concern; if an agent needs a specific tool for a structural reason, that belongs in the agent's own spec, not in the orchestration vocabulary skill.
3. **Traceability header prose** (`> Implements:`, `> Requirements:`) — build/tooling metadata irrelevant to an LLM reading the skill. Should move to structured YAML frontmatter, not Markdown body prose.

Motivation: trimming these makes the skill purely about SEND/RECEIVE/RESPOND and reduces the context an LLM has to parse to use it correctly. No agent loses functionality — `runSubagent` documentation moves to the Setup Bootloader's own agent spec if still needed.

Acceptance criteria:
- `SKILL.md` body contains only: skill description, SEND/RECEIVE/RESPOND definitions, and concrete tool-call syntax for each verb
- No runtime mode-detection logic, no `agents:`/`runSubagent` exception content in the body
- Traceability metadata moved to YAML frontmatter fields
- sphinx-build `-W` passes clean

---

## Level 0: User Stories

**Status**: ✅ completed

### Impacted User Stories

| ID | Title | Impact | Notes |
|----|-------|--------|-------|
| SYSP_US_SKILL_ORCHESTRATION | Orchestration Skill Architecture | context only | No text change; US is abstract enough to cover simplified skill |

### New User Stories

None.

### Decisions

- No L0 changes needed — the US already says "exchangeable skill variants" without prescribing mode-detection logic.

### Horizontal Check (MECE)

- [x] No contradictions with existing User Stories
- [x] No redundancies
- [x] Gaps identified and addressed

---

## Level 1: Requirements

**Status**: ✅ completed

### Impacted Requirements

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| SYSP_REQ_SKILL_ORCHESTRATION_VERBS | SYSP_US_SKILL_ORCHESTRATION | no change needed | RESPOND defined as "deliver result to initiator, variant routes appropriately" — already abstract enough; no mode-detection prescribed at L1 |

### New Requirements

None.

### Conflicts Detected

None.

### Decisions

- SYSP_REQ_SKILL_ORCHESTRATION_VERBS AC-6 says "only RESPOND is mode-dependent" — this means it differs *between variants* (Jarvis vs Subagent), not within a single variant at runtime. The requirement text is already correct and does not prescribe runtime mode-detection. No change.

### Horizontal Check (MECE)

- [x] No contradictions with existing Requirements
- [x] No redundancies
- [x] All new REQs link to User Stories

---

## Level 2: Design

**Status**: ✅ completed

### Impacted Design Elements

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| SYSP_SPEC_SKILL_ORCHESTRATION_VERB_MODEL | SYSP_REQ_SKILL_ORCHESTRATION_VERBS | modified | RESPOND row updated; mode-detection subsection removed |
| SYSP_SPEC_SKILL_ORCHESTRATION_MATRIX | SYSP_REQ_SKILL_ORCHESTRATION_VERBS | modified | Removed `agents:` frontmatter bullets |

### New Design Elements

None.

### Conflicts Detected

None.

### Decisions

- RESPOND in Jarvis variant is now simply "SEND result back to originating sender via `jarvis_sendToSession`" — no runtime mode-detection.
- `agents:` / `runSubagent` carve-out removed from shared orchestration spec — belongs in Setup Bootloader's own spec (`spec_setup_engineer.rst`), which already documents it.

### Horizontal Check (MECE)

- [x] No contradictions with existing Designs
- [x] All new SPECs link to Requirements

---

## Final Consistency Check

**Status**: ✅ passed

### Traceability Verification

| User Story | Requirements | Design | Complete? |
|------------|--------------|--------|-----------|
| SYSP_US_SKILL_ORCHESTRATION | SYSP_REQ_SKILL_ORCHESTRATION_VERBS (unchanged) | SYSP_SPEC_SKILL_ORCHESTRATION_VERB_MODEL (modified), SYSP_SPEC_SKILL_ORCHESTRATION_MATRIX (modified) | ✅ |

### Artefakt-Removal-Check

Removed content (prose sections, not IDs):

| Removed Artefact | Class (a): Code/Workflow refs | Class (b): Doc refs | Class (c): Historic Change Docs |
|------------------|-------------------------------|---------------------|---------------------------------|
| RESPOND mode-detection subsection | Fixed in SYSP_SPEC_SKILL_ORCHESTRATION_VERB_MODEL | none | 1 — acceptable (uat-skill-orchestration-vocab CD mentions it historically) |
| `agents:` frontmatter bullets | Fixed in SYSP_SPEC_SKILL_ORCHESTRATION_MATRIX | `spec_setup_engineer.rst` already documents its own `runSubagent` — no fix needed | 1 — acceptable |

- [x] All class (a) active code/workflow references fixed in this CR
- [x] All class (b) active documentation references fixed in this CR
- [x] Class (c) historical Change Documents accepted as "acceptable historic stranding" and disclosed above

### Issues Found

None. MECE and Trace checks both clean on first review round.

### Sign-off

- [x] All levels completed (no ⚠️ DEPRECATED markers remaining)
- [x] All conflicts resolved
- [x] Traceability verified
- [x] Ready for merge

---

## QM Findings

*QM writes findings directly into this section after each review round. PM records
decisions (fix-now / defer / accept-as-is) with rationale in the same section.
Multiple review rounds are appended as sub-sections. Existing CDs without this
section are unaffected — the section is additive, never required retroactively.*

### Round 1

**Reviewed by:** MECE Engineer + Trace Engineer
**Review date:** 2026-07-17

#### Findings

None. AC-6 interpretation verified correct (mode-dependent = variant differs, not runtime branching). Setup Bootloader spec covers removed `agents:` content. No active class (a)/(b) references unaddressed.

---

### Round 2

**Reviewed by:** Quality Manager (independent verification)
**Review date:** 2026-07-17

#### Findings

| # | Severity | Level | Element | Issue |
|---|----------|-------|---------|-------|
| 1 | MEDIUM-HIGH | L2 | SYSP_SPEC_SKILL_ORCHESTRATION_VERB_MODEL | The "Verb Mapping — Jarvis Variant" table (SEND, RECEIVE, and the RESPOND row rewritten by this CR) documents `jarvis_sendToSession(...)` and `jarvis_readMessage()`. Both are **deprecated and disabled** — the current Jarvis tools are `jarvis_sendMessage(session, text, senderSession)` and `jarvis_receiveMessage(destination)`. Root cause is in the spec (not just the SKILL.md, which correctly implements the spec as written): the tool rename to `jarvis_sendMessage`/`jarvis_receiveMessage` was never propagated to this spec element. This CR's own AC ("concrete tool-call syntax for each verb") is violated by stale syntax. |
| 2 | MEDIUM-HIGH | Skill (implementation) | `.github/skills/syspilot.orchestration-jarvis/SKILL.md` and `syspilot/skills/syspilot.orchestration-jarvis/SKILL.md` | Same three tool-call cells (SEND, RECEIVE, RESPOND) carry the same deprecated/disabled tool names, inherited directly from the spec table above. Any agent following this skill literally would call disabled tools. |

**Note:** This is CR-adjacent, not CR-introduced by intent — the RESPOND row was rewritten by this CR and still used the stale name, so the defect is touched by this CR's own diff. Recommend fix-now (small, mechanical rename) rather than defer, since the skill is actively used by every orchestrating agent including QM itself.

---

---

*Generated by syspilot Change Agent*
