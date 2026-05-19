# UAT Validation: orchestration-skill-split

**Date**: 2026-05-19
**Change Document**: [docs/changes/v0.5.4/orchestration-skill-split.md](orchestration-skill-split.md)
**Branch**: feature/orchestration-skill-split
**Status**: ⏳ PENDING

---

## Scope

This document covers User Acceptance Testing for the orchestration skill split.
The monolithic `syspilot.orchestration` skill is replaced by an orchestration skill
group: a Group Contract Spec (`SYSP_SPEC_SKILL_ORCHESTRATION_CONTRACT`) declares the
four-verb vocabulary (INVOKE, SEND, RECEIVE, RESPOND), and the `syspilot.orchestration-jarvis`
skill variant implements them using `runSubagent` / `jarvis_sendToSession` / `jarvis_readMessage`.
The old standalone skill is deleted and all active references are updated.

**Note on AC-5 / AC-6:** These criteria cover file deletion and reference updates that
are implementation tasks executed by the Dev Engineer. The test scenarios below describe
the expected outcome state — a tester verifies the resulting artefact presence/absence
and content after the implementation is complete.

---

## Precondition (all scenarios)

Branch `feature/orchestration-skill-split` is checked out and all committed changes are
present in the working tree.

---

## Test Coverage Summary

| AC | Description | Scenarios |
|----|-------------|-----------|
| AC-1 | Group Contract Spec exists, declares DEFINITIONS with correct semantics | T-1, T-2, T-3, T-4, T-5, T-6, T-7 |
| AC-2 | `syspilot.orchestration-jarvis` exists, implements all 4 verbs | T-8, T-9, T-10, T-11, T-12 |
| AC-3 | RESPOND detects invocation mode internally via RECEIVE | T-13, T-14, T-15 |
| AC-4 | Skill content describes patterns only — no agent names, no matrix | T-16, T-17 |
| AC-5 | `syspilot.orchestration` standalone skill is removed | T-18, T-19 |
| AC-6 | All active `syspilot.orchestration` references updated | T-20, T-21, T-22, T-23 |

---

## Test Scenarios

### T-1 — Group Contract Spec node exists in design spec file

**AC**: AC-1  
**Requirement ref**: `SYSP_SPEC_SKILL_ORCHESTRATION_CONTRACT`  
**Design ref**: `docs/syspilot/design/spec_skill_orchestration.rst`

| Field | Value |
|-------|-------|
| **Precondition** | Branch checked out; `docs/syspilot/design/spec_skill_orchestration.rst` is readable |
| **Action** | Open `docs/syspilot/design/spec_skill_orchestration.rst` and search for `:id: SYSP_SPEC_SKILL_ORCHESTRATION_CONTRACT` |
| **Expected** | A `.. spec::` directive with `:id: SYSP_SPEC_SKILL_ORCHESTRATION_CONTRACT` is present |
| **Pass criterion** | Spec node found with correct id; `:status:` is `approved` |
| **Fail criterion** | Node absent, or id differs, or status is not `approved` |

---

### T-2 — DEFINITIONS section present with exactly four terms

**AC**: AC-1  
**Requirement ref**: `SYSP_SPEC_SKILL_ORCHESTRATION_CONTRACT` AC-1

| Field | Value |
|-------|-------|
| **Precondition** | T-1 passed |
| **Action** | Read the body of `SYSP_SPEC_SKILL_ORCHESTRATION_CONTRACT`; inspect the DEFINITIONS table |
| **Expected** | The DEFINITIONS table lists exactly four terms: `INVOKE`, `SEND`, `RECEIVE`, `RESPOND` — no more, no less |
| **Pass criterion** | Exactly 4 rows in the DEFINITIONS table; terms are `INVOKE`, `SEND`, `RECEIVE`, `RESPOND` |
| **Fail criterion** | Any term is missing, misspelled, or an additional term appears (e.g. `DELEGATE`, `REPLY`) |

---

### T-3 — INVOKE definition has synchronous-blocking semantics

**AC**: AC-1  
**Requirement ref**: `SYSP_REQ_SKILL_ORCHESTRATION_INVOKE` AC-1

| Field | Value |
|-------|-------|
| **Precondition** | T-2 passed |
| **Action** | Read the INVOKE row in the DEFINITIONS table of `SYSP_SPEC_SKILL_ORCHESTRATION_CONTRACT` |
| **Expected** | Semantics state that INVOKE is a synchronous call where the caller blocks until the callee returns a structured result |
| **Pass criterion** | Definition includes "synchronous", "blocks", "structured result" or equivalent meaning |
| **Fail criterion** | Definition is absent, describes async behaviour, or omits caller-blocking semantics |

---

### T-4 — SEND definition has non-blocking cross-session semantics

**AC**: AC-1  
**Requirement ref**: `SYSP_REQ_SKILL_ORCHESTRATION_INVOKE` AC-2

| Field | Value |
|-------|-------|
| **Precondition** | T-2 passed |
| **Action** | Read the SEND row in the DEFINITIONS table of `SYSP_SPEC_SKILL_ORCHESTRATION_CONTRACT` |
| **Expected** | Semantics describe message delivery to another session, non-blocking, used for cross-session communication |
| **Pass criterion** | Definition includes "cross-session", "non-blocking" (or "message delivery"), and "session" |
| **Fail criterion** | Definition is absent, or confuses SEND with INVOKE, or omits non-blocking nature |

---

### T-5 — RECEIVE definition describes inbox-check semantics

**AC**: AC-1  
**Requirement ref**: `SYSP_REQ_SKILL_ORCHESTRATION_INVOKE` AC-3

| Field | Value |
|-------|-------|
| **Precondition** | T-2 passed |
| **Action** | Read the RECEIVE row in the DEFINITIONS table of `SYSP_SPEC_SKILL_ORCHESTRATION_CONTRACT` |
| **Expected** | Semantics describe checking an inbox for pending messages; result is either the next pending message or an indication that no messages are available |
| **Pass criterion** | Definition includes "inbox", "pending messages", and "no messages" (or empty/absent) outcome |
| **Fail criterion** | Definition is absent, or conflates RECEIVE with RESPOND |

---

### T-6 — RESPOND definition describes mode-detected terminal delivery

**AC**: AC-1  
**Requirement ref**: `SYSP_REQ_SKILL_ORCHESTRATION_INVOKE` AC-4

| Field | Value |
|-------|-------|
| **Precondition** | T-2 passed |
| **Action** | Read the RESPOND row in the DEFINITIONS table of `SYSP_SPEC_SKILL_ORCHESTRATION_CONTRACT` |
| **Expected** | Semantics state that RESPOND auto-detects invocation mode: if a pending message triggered this run (via RECEIVE), the result is routed back to the sender; otherwise the result is returned directly as structured output |
| **Pass criterion** | Definition includes "auto-detects", "pending message", "sender" (for async path), and "directly" or "structured output" (for sync path) |
| **Fail criterion** | Definition is absent, or describes only one delivery mode, or omits the RECEIVE-based detection |

---

### T-7 — DEFINITIONS are tool-agnostic in the Group Contract Spec

**AC**: AC-1  
**Requirement ref**: `SYSP_SPEC_SKILL_ORCHESTRATION_CONTRACT` AC-3

| Field | Value |
|-------|-------|
| **Precondition** | T-2 passed |
| **Action** | Search the entire body of `SYSP_SPEC_SKILL_ORCHESTRATION_CONTRACT` for the strings `runSubagent`, `jarvis_sendToSession`, `jarvis_readMessage` |
| **Expected** | None of these runtime API names appear anywhere inside the spec node body |
| **Pass criterion** | Zero occurrences of any of the three API names within the spec node |
| **Fail criterion** | Any runtime API name found inside the DEFINITIONS section or constraints of the spec node |

---

### T-8 — `syspilot.orchestration-jarvis` skill file exists in product and installed locations

**AC**: AC-2  
**Requirement ref**: `SYSP_REQ_SKILL_ORCHESTRATION_GROUP` AC-4; `SYSP_SPEC_SKILL_ORCHESTRATION_GROUP`

| Field | Value |
|-------|-------|
| **Precondition** | Branch checked out |
| **Action** | Check for the existence of `syspilot/skills/syspilot.orchestration-jarvis/SKILL.md` and `.github/skills/syspilot.orchestration-jarvis/SKILL.md` |
| **Expected** | Both files exist |
| **Pass criterion** | Both paths resolve to readable files |
| **Fail criterion** | Either file is missing or the directory structure is wrong |

---

### T-9 — Jarvis skill frontmatter declares `group: orchestration`

**AC**: AC-2  
**Requirement ref**: `SYSP_REQ_SKILL_ORCHESTRATION_GROUP`; `SYSP_SPEC_SKILL_ORCHESTRATION_GROUP`

| Field | Value |
|-------|-------|
| **Precondition** | T-8 passed |
| **Action** | Open `syspilot/skills/syspilot.orchestration-jarvis/SKILL.md` and read the YAML frontmatter |
| **Expected** | Frontmatter contains `group: orchestration` and `name: syspilot.orchestration-jarvis` |
| **Pass criterion** | Both `group` and `name` fields are present with the expected values |
| **Fail criterion** | `group` field absent, wrong value, or `name` does not match |

---

### T-10 — INVOKE maps to `runSubagent()` in jarvis variant

**AC**: AC-2  
**Requirement ref**: `SYSP_SPEC_SKILL_ORCHESTRATION_VERB_MODEL`

| Field | Value |
|-------|-------|
| **Precondition** | T-8 passed |
| **Action** | Open `syspilot/skills/syspilot.orchestration-jarvis/SKILL.md` and locate the INVOKE definition |
| **Expected** | INVOKE is documented as mapping to `runSubagent("syspilot.<agent>", "<prompt>")` |
| **Pass criterion** | `runSubagent` appears in the INVOKE section with the correct pattern |
| **Fail criterion** | INVOKE section is absent, or maps to a different mechanism |

---

### T-11 — SEND and RECEIVE map to jarvis tools in jarvis variant

**AC**: AC-2  
**Requirement ref**: `SYSP_SPEC_SKILL_ORCHESTRATION_VERB_MODEL`

| Field | Value |
|-------|-------|
| **Precondition** | T-8 passed |
| **Action** | Open `syspilot/skills/syspilot.orchestration-jarvis/SKILL.md`; locate the SEND and RECEIVE definitions |
| **Expected** | SEND maps to `jarvis_sendToSession("<session>", "<message>")`; RECEIVE maps to `jarvis_readMessage()` |
| **Pass criterion** | Both `jarvis_sendToSession` and `jarvis_readMessage` appear in the respective definition sections |
| **Fail criterion** | Either mapping is absent, or maps to a different tool |

---

### T-12 — RESPOND section is present in jarvis variant

**AC**: AC-2  
**Requirement ref**: `SYSP_SPEC_SKILL_ORCHESTRATION_VERB_MODEL`

| Field | Value |
|-------|-------|
| **Precondition** | T-8 passed |
| **Action** | Open `syspilot/skills/syspilot.orchestration-jarvis/SKILL.md`; search for a RESPOND section |
| **Expected** | A RESPOND section exists and describes the delivery logic |
| **Pass criterion** | RESPOND section found with substantive content |
| **Fail criterion** | RESPOND section absent; only INVOKE/SEND/RECEIVE covered |

---

### T-13 — RESPOND implementation calls `jarvis_readMessage` for mode detection

**AC**: AC-3  
**Requirement ref**: `SYSP_SPEC_SKILL_ORCHESTRATION_VERB_MODEL` (RESPOND mode-detection)

| Field | Value |
|-------|-------|
| **Precondition** | T-12 passed |
| **Action** | Read the RESPOND section of `syspilot/skills/syspilot.orchestration-jarvis/SKILL.md`; check whether mode detection uses `jarvis_readMessage()` |
| **Expected** | The RESPOND logic describes calling `jarvis_readMessage()` as step 1 to determine if a pending message triggered this run |
| **Pass criterion** | `jarvis_readMessage` appears explicitly inside the RESPOND definition as the mode-detection call |
| **Fail criterion** | Mode detection uses a different mechanism, or `jarvis_readMessage` is absent from RESPOND |

---

### T-14 — RESPOND async path routes result via `jarvis_sendToSession`

**AC**: AC-3  
**Requirement ref**: `SYSP_SPEC_SKILL_ORCHESTRATION_VERB_MODEL` (RESPOND step 2)

| Field | Value |
|-------|-------|
| **Precondition** | T-13 passed |
| **Action** | Read the RESPOND section; locate the path where `jarvis_readMessage` returns a message |
| **Expected** | When a triggering message is found, the result is sent back to the original sender via `jarvis_sendToSession` |
| **Pass criterion** | RESPOND describes: message found → route via `jarvis_sendToSession` to sender |
| **Fail criterion** | Async path absent, or uses a different delivery mechanism |

---

### T-15 — RESPOND sync path returns result directly

**AC**: AC-3  
**Requirement ref**: `SYSP_SPEC_SKILL_ORCHESTRATION_VERB_MODEL` (RESPOND step 3)

| Field | Value |
|-------|-------|
| **Precondition** | T-13 passed |
| **Action** | Read the RESPOND section; locate the path where `jarvis_readMessage` returns empty/no message |
| **Expected** | When no triggering message is found, the result is returned directly as structured output (captured by the `runSubagent()` return value) |
| **Pass criterion** | RESPOND describes: no message → return result directly as structured output |
| **Fail criterion** | Sync path absent, or incorrectly routes via `jarvis_sendToSession` even when no message is present |

---

### T-16 — Skill content contains no agent names

**AC**: AC-4  
**Requirement ref**: `SYSP_SPEC_SKILL_ORCHESTRATION_MATRIX` (Prohibited)

| Field | Value |
|-------|-------|
| **Precondition** | T-8 passed |
| **Action** | Open `syspilot/skills/syspilot.orchestration-jarvis/SKILL.md`; search for strings `syspilot.cm`, `syspilot.pm`, `syspilot.qm`, `syspilot.implement`, `syspilot.design`, `syspilot.uat`, `syspilot.trace`, `syspilot.release`, `syspilot.docu`, `syspilot.mece` |
| **Expected** | None of these agent names appear anywhere in the skill body |
| **Pass criterion** | Zero occurrences of any named agent in the skill content |
| **Fail criterion** | Any agent name found in the skill content |

---

### T-17 — Skill content contains no orchestration matrix

**AC**: AC-4  
**Requirement ref**: `SYSP_SPEC_SKILL_ORCHESTRATION_MATRIX` (Prohibited)

| Field | Value |
|-------|-------|
| **Precondition** | T-8 passed |
| **Action** | Open `syspilot/skills/syspilot.orchestration-jarvis/SKILL.md`; check for any table or list that describes which agent may call which other agent (e.g. "CM invokes Design", "PM invokes CM") |
| **Expected** | No who-calls-whom matrix or equivalent prose appears in the skill |
| **Pass criterion** | Skill content is free of caller→callee mappings beyond the generic verb descriptions |
| **Fail criterion** | Any listing of specific agent-to-agent calling relationships found |

---

### T-18 — `syspilot.orchestration` directory removed from product source

**AC**: AC-5

| Field | Value |
|-------|-------|
| **Precondition** | Branch checked out |
| **Action** | Check whether the path `syspilot/skills/syspilot.orchestration/` exists in the repository |
| **Expected** | The directory does not exist |
| **Pass criterion** | Path is absent; no `SKILL.md` or any file under `syspilot/skills/syspilot.orchestration/` |
| **Fail criterion** | Directory or any file under it still present |

---

### T-19 — `syspilot.orchestration` directory removed from installed location

**AC**: AC-5

| Field | Value |
|-------|-------|
| **Precondition** | Branch checked out |
| **Action** | Check whether the path `.github/skills/syspilot.orchestration/` exists |
| **Expected** | The directory does not exist |
| **Pass criterion** | Path is absent |
| **Fail criterion** | `.github/skills/syspilot.orchestration/SKILL.md` or any file under the directory still present |

---

### T-20 — `docs/architecture.md` no longer references `syspilot.orchestration` standalone

**AC**: AC-6

| Field | Value |
|-------|-------|
| **Precondition** | Branch checked out |
| **Action** | Open `docs/architecture.md` and search for `syspilot.orchestration` (exact string, without `-jarvis` suffix) |
| **Expected** | The standalone `syspilot.orchestration` name does not appear; any orchestration reference reflects the new group (`syspilot.orchestration-jarvis` or `orchestration` group) |
| **Pass criterion** | No occurrence of `syspilot.orchestration` without the `-jarvis` (or other variant) suffix |
| **Fail criterion** | `syspilot.orchestration` (standalone) still listed as an installed skill |

---

### T-21 — `docs/methodology.md` no longer references `syspilot.orchestration` standalone

**AC**: AC-6

| Field | Value |
|-------|-------|
| **Precondition** | Branch checked out |
| **Action** | Open `docs/methodology.md` and search for `syspilot.orchestration` (without `-jarvis` suffix) |
| **Expected** | The standalone `syspilot.orchestration` name does not appear in any skill listing or directory tree |
| **Pass criterion** | No occurrence of standalone `syspilot.orchestration` |
| **Fail criterion** | Old standalone name still present in the skill directory listing |

---

### T-22 — `docs/syspilot/conventions.md` entry updated to new variant

**AC**: AC-6

| Field | Value |
|-------|-------|
| **Precondition** | Branch checked out |
| **Action** | Open `docs/syspilot/conventions.md` and search for any entry describing the orchestration skill |
| **Expected** | The entry reflects `syspilot.orchestration-jarvis` (not the old `syspilot.orchestration`); description mentions INVOKE/SEND/RECEIVE/RESPOND vocabulary (not the old INVOKE/DELEGATE/REPLY) |
| **Pass criterion** | Entry references `syspilot.orchestration-jarvis` and the four-verb model |
| **Fail criterion** | Entry still names `syspilot.orchestration` and/or uses DELEGATE/REPLY verbs |

---

### T-23 — Class (b) RST specification documents updated

**AC**: AC-6

| Field | Value |
|-------|-------|
| **Precondition** | Branch checked out |
| **Action** | Search the following files for standalone `syspilot.orchestration` (exact, without `-jarvis` suffix): `docs/syspilot/design/spec_skill_orchestration.rst`, `docs/syspilot/requirements/req_skill_orchestration.rst`, `docs/syspilot/design/spec_skill_arch.rst` |
| **Expected** | No file contains a reference to the standalone `syspilot.orchestration` skill name in normative content (historical stranding in change documents is acceptable) |
| **Pass criterion** | All three files reference `syspilot.orchestration-jarvis` or the `orchestration` group where a skill name is needed; no normative statement points to the removed standalone skill |
| **Fail criterion** | Any of the three RST files contains a normative reference to `syspilot.orchestration` without a variant suffix |

---

## Testability Notes

| # | Note |
|---|------|
| 1 | **T-16 / T-17 (AC-4 — no agent names, no matrix):** This is a content-review check performed by reading the skill file. There is no automated assertion — the tester must read the RESPOND/INVOKE/SEND/RECEIVE sections and confirm no specific agent names or caller→callee tables appear. |
| 2 | **T-13 / T-14 / T-15 (AC-3 — RESPOND mode detection):** These scenarios verify the _documented_ logic in the skill file, not runtime behaviour. Runtime validation (actually invoking an agent in both sync and async modes and observing routing) is out of scope for this UAT cycle. |
| 3 | **T-23 (AC-6 — RST spec updates):** The phrase "normative content" excludes historical change documents under `docs/changes/` and `.jarvis/` session files — standalone `syspilot.orchestration` references in those paths are classified as acceptable historic stranding per the Change Document. |
