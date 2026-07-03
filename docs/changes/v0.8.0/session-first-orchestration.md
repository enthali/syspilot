# Change Document: session-first-orchestration

**Status**: draft
**Branch**: feature/session-first-orchestration
**Created**: 2026-06-19
**Author**: PM
**Operation Mode**: user-guided

---

## Summary

Flip syspilot's orchestration default from synchronous `runSubagent` to asynchronous Jarvis-session messaging. Every orchestrating agent runs as its own persistent Jarvis session with its own `context.md`. Synchronous `runSubagent` is retained only as an explicit exception (Setup → Installer, where Jarvis is not yet available) and as the graceful-degradation path for installations without Jarvis.

This CR completes the exchangeable orchestration-skill group defined in `SYSP_US_SKILL_ARCH` (only `orchestration-jarvis` was ever implemented) by adding the second member `orchestration-subagent`, and finally implements the Setup-enforced mutual exclusion that `SYSP_US_SKILL_ARCH` AC-5 has required all along.

Tracks GitHub issue #35. This is an experimental change developed on `feature/session-first-orchestration`; it is not merged to `main` until validated in real use.

---

## WHY

`runSubagent` is synchronous and nested-invocation-limited: an agent invoked as a subagent cannot itself dispatch further subagents. This constrains the CM pipeline (CM → Design → UAT → Implement → Docu) and forces inline workarounds.

Async-first Jarvis-session communication removes this limitation and yields three further benefits:

1. **Full audit trail** — every agent-to-agent message is visible in the Jarvis message log (directly addresses the audit need demonstrated by the independent QM audit in #18).
2. **Context hygiene** — each agent reasons in its own unpolluted context, critical for QM independence (e.g. MECE must not inherit QM's context).
3. **Learning agents** — a persistent `context.md` per agent lets each accumulate lessons across CRs.

---

## WHAT

### New orchestration skill (group member)

Add `syspilot.orchestration-subagent` as a second member of `group: orchestration`, implementing the same group contract (INVOKE/SEND/RECEIVE/RESPOND) using only `runSubagent` — no Jarvis dependency. This is the graceful-degradation variant.

### Setup / Installer behavior

- The Installer asks the user whether to use Jarvis. The default is inferred from the presence of a `.jarvis/` directory in the workspace.
- Based on the answer, the Installer writes exactly one orchestration-group skill into the installed skill location, enforcing mutual exclusion across the group (`SYSP_US_SKILL_ARCH` AC-5). If a skill of the same group is already installed, the previous one is removed before the new one is written.
- As the final installation step (Jarvis path only), the Installer creates a session scaffold for every installed agent except `syspilot.setup` and `syspilot.installer`: a directory `.jarvis/sessions/<name>/` containing a `session.yaml` with `name:` and `agent:` fields. Both values are read from the agent file's frontmatter.
- On update, the Installer ensures a scaffold exists for every eligible agent; missing directories and `session.yaml` files are created. Existing scaffolds and any `context.md` are left untouched (the agent owns its `context.md`).

### Agent files

- Every agent file carries a `name:` frontmatter field (human-readable session name, e.g. `Project Manager`) and an `agent:` identifier.
- Every orchestrating agent is `user-invocable: true` so Jarvis can start a session in the correct agent mode.

### Orchestration default in specs

- PM, CM, QM specs describe dispatch via SEND (sendToSession) as the default; INVOKE (runSubagent) is the explicit exception, reserved for stateless one-off agents and the Setup → Installer bootstrap.

### Known limitation (documented, not solved)

Parallel change pipelines (e.g. git worktrees) would collide on shared session names. This is documented as a known limitation in the orchestration skill and deferred.

---

## Acceptance Criteria

- `syspilot.orchestration-subagent` skill exists, declares `group: orchestration`, and implements every DEFINITION of the orchestration group contract using `runSubagent` only
- Both orchestration skills are interchangeable without modifying any agent that uses the group (`SYSP_US_SKILL_ARCH` AC-7)
- Setup/Installer spec describes the Jarvis question, default inference from `.jarvis/` presence, and mutual-exclusion installation of exactly one orchestration-group skill (`SYSP_US_SKILL_ARCH` AC-5)
- Setup/Installer spec describes creation of `.jarvis/sessions/<name>/session.yaml` (fields `name:`, `agent:`) for every agent except setup and installer, as the final step on the Jarvis path
- Setup/Installer spec describes the update behavior: missing scaffolds created, existing scaffolds and `context.md` preserved
- Every agent file except setup/installer carries `name:` and `agent:` frontmatter and is `user-invocable: true`
- PM, CM, QM specs describe SEND as the default dispatch mechanism and INVOKE as the explicit exception
- The git-worktree session-name collision is documented as a known limitation
- sphinx-build -W passes clean

---

## Notes

- Setup and Installer themselves never get a session — they are the bootstrap layer. This also keeps the user's entry point unambiguous.
- Session creation is lazy: the scaffold only declares a session; Jarvis materializes it on the first `sendToSession` or user click.

---

## Design Log (System Designer)

> The Summary / WHAT / Acceptance-Criteria sections above were authored before
> the **design steering update** that refined the model during analysis. Where
> those sections still say "four verbs (INVOKE/SEND/RECEIVE/RESPOND)" or
> "INVOKE is the explicit exception", the authoritative design is the
> three-verb model recorded below. The PM/Summary text is left intact (PM
> territory); this Design Log is the engineering source of truth.

### Steering Decisions (supersede the original brief)

1. **Three verbs, not four.** INVOKE is dropped from the group contract.
   The contract is **SEND / RECEIVE / RESPOND**. "Synchronous dispatch" is
   just SEND under the synchronous variant — no separate verb.
2. **Peer-to-peer, role-agnostic.** Any agent may communicate with any other;
   the orchestration contract carries no manager/engineer framing.
3. **RESPOND is the only mode-dependent verb.** SEND and RECEIVE map
   identically across variants; only RESPOND differs (active send-back vs.
   plain output).
4. **Bootstrap is outside the contract.** Setup → Installer is a synchronous
   in-process `runSubagent` call that explicitly does NOT use the
   orchestration skill or its verbs.
5. **`agents:` frontmatter = SEND-whitelist** (a documentation/topology
   constraint), not a synchronous-invocation privilege. RESPOND to the
   initiator never requires the initiator to be listed.
6. **Variants are L1/L2, not user stories** (Option A). The single L0 story
   carries the value; the two variants live in requirements + design.
7. **Verb word = RESPOND** (not REPLY): request/response semantics.

### L0 — User Stories

| ID | Change |
|----|--------|
| `SYSP_US_SKILL_ORCHESTRATION` | Header subtitle → "Peer-to-peer agent communication pattern". Context: peer-to-peer; "syspilot leverages both asynchronous and synchronous communication". Verb list → **SEND/RECEIVE/RESPOND** (INVOKE removed). Reduced to 3 ACs (3 verbs → 3 UATs); spec mechanics (`agents:` whitelist, report format, decoupling) moved to L1. |
| `SYSP_US_INSTALLER` | Mutex AC: **reject → replace**. New ACs: variant question + default inference, session-scaffold creation, update-preserves-existing, identity from frontmatter. |
| `SYSP_US_CM` | ACs: dispatch via SEND; INVOKE removed. |
| `SYSP_US_QM` | Duties translated EN; "invocation" → SEND. |

*A separate `SYSP_US_ORCHESTRATION_SUBAGENT` story was drafted and then removed
(Option A): variants are an L1/L2 concern, not a distinct user need.*

### L1 — Requirements

| ID | Change |
|----|--------|
| `SYSP_REQ_SKILL_ORCHESTRATION_VERBS` | Renamed from `..._INVOKE` (misnamed after INVOKE dropped). Three-verb model; peer-to-peer; AC-5 "no separate sync verb"; AC-6 "only RESPOND is mode-dependent". |
| `SYSP_REQ_SKILL_ORCHESTRATION_FRONTMATTER` | `agents:` = SEND-whitelist; AC-5 RESPOND needs no listing. |
| `SYSP_REQ_SKILL_ORCHESTRATION_REPORTING` | Report delivered via RESPOND; tool-name AC + deferred note removed. |
| `SYSP_REQ_SKILL_ORCHESTRATION_GROUP` | Two variants (async + sync); DEFINITIONS = three verbs. |
| `SYSP_REQ_SKILL_ORCHESTRATION_AGENT_VOCAB` | Three verbs; "invoke/dispatch/delegate" prohibited. |
| `SYSP_REQ_INSTALLER_DUTIES` | AC-2 EN; AC-5 reject → replace. |
| `SYSP_REQ_SETUP_SKILL_MUTEX` | Mutual exclusion via replacement; exactly one per group. |
| `SYSP_REQ_INSTALLER_ORCHESTRATION_SELECT` *(new)* | Variant question + default from workspace context. |
| `SYSP_REQ_INSTALLER_SESSION_SCAFFOLD` *(new)* | Scaffold per eligible agent; update preserves existing + context. |
| `SYSP_REQ_INSTALLER_WORKFLOW` | New steps: variant-select (AC-8), session scaffold (AC-12). |
| `SYSP_REQ_SETUP_BOOTLOADER_INVOKE` | Bootstrap = sync in-process call, explicitly outside the orchestration contract. |
| `SYSP_REQ_AGENT_ARCH_FRONTMATTER` | New AC-7 session-identity fields, AC-8 user-invocable, AC-9 Setup/Installer excluded. |
| `SYSP_REQ_CM_WORKFLOW` | Procedural ACs → outcome guarantees; flow in Description; SSoT/scope-creep removed; QM-review trigger. |
| `SYSP_REQ_PM_WORKFLOW` | Procedural ACs → guarantees; SEND dispatch; pink-elephant removed; bracket flow in Description. |
| `SYSP_REQ_QM_WORKFLOW` | QM = final gate (CM-triggered after impl+validation); SEND to MECE/Trace; self-assess impl/validation; findings recorded in CD. |

*Engineer L1 workflow reqs unchanged: the RECEIVE…RESPOND bracket is a
workflow-completeness concern handled at L2 (consistent with the managers).*

### L2 — Design Specs

| ID | Change |
|----|--------|
| `SYSP_SPEC_SKILL_ORCHESTRATION_PATTERN` / `_MATRIX` / `_CONTRACT` / `_VERB_MODEL` / `_GROUP` / `_AGENT_VOCAB` | Three-verb model; peer-to-peer; Jarvis variant = async mapping; `agents:` = SEND-whitelist; bootstrap exception noted. |
| `SYSP_SPEC_SKILL_ORCHESTRATION_VERB_MODEL_SUBAGENT` *(new)* | Sync variant mapping: SEND→`runSubagent`, RECEIVE→start prompt, RESPOND→return value. |
| `SYSP_SPEC_CM_WORKFLOW` | SEND/RECEIVE/RESPOND flow; QM = final gate; PM+QM dispatch; status → draft. Spec-quality MECE gate lives in the Designer (not a separate CM step). |
| `SYSP_SPEC_DESIGN_WORKFLOW` | RECEIVE…RESPOND bracket; MECE per level upgraded from advisory to a **quality gate** owned by the Designer. |
| `SYSP_SPEC_PM_WORKFLOW` | SEND to CM/Release/Setup; pink-elephant removed; tool-agnostic. |
| `SYSP_SPEC_QM_WORKFLOW` | Final-gate flow; SEND MECE/Trace; self-assess impl/validation; record findings in CD. |
| `SYSP_SPEC_IMPLEMENT/UAT/DOCU/MECE/TRACE/VERIFY/RELEASE_WORKFLOW` | RECEIVE…RESPOND bracket added; internal `Report` steps → RESPOND; Verify subagent calls → SEND; Release trigger source → PM. |
| `SYSP_SPEC_INSTALLER_SKILL_MUTEX` | Reject → replace. |
| `SYSP_SPEC_INSTALLER_WORKFLOW` | Variant-select (step 5) + session-scaffold (step 9). |
| `SYSP_SPEC_INSTALLER_ORCHESTRATION_SELECT` *(new)* | `.jarvis/` inference + user prompt + mutex install. |
| `SYSP_SPEC_INSTALLER_SESSION_SCAFFOLD` *(new)* | `.jarvis/sessions/<name>/session.yaml` with `name:`/`agent:`; preserve on update; worktree limitation. |
| `SYSP_SPEC_SETUP_WORKFLOW` | Bootstrap `runSubagent` call explicitly outside the orchestration contract. |
| `SYSP_SPEC_AGENT_ARCH_FRONTMATTER` | `name:`/`agent:` session-identity fields; Setup/Installer excluded. |

### New product files

- `syspilot/skills/syspilot.orchestration-subagent/SKILL.md` (sync variant, three-verb mapping).
- `syspilot/skills/syspilot.orchestration-jarvis/SKILL.md` modified: INVOKE stripped; SEND/RECEIVE/RESPOND only; `agents:` = SEND-whitelist.

### Validation

- `sphinx-build -W` passes clean; sphinx-needs schema validation: 0 warnings; no broken links.
- **MECE gate (L1, Designer-run):** clean after two fixes —
  (C1) `SYSP_REQ_CM_WORKFLOW` AC-5 "triggers a QM review" → "SENDs a quality review to QM";
  (C3) `SYSP_REQ_QM_DUTIES` AC-7 tool-name leak ("ephemeral Jarvis messages") reworded
  tool-agnostic and reconciled with RESPOND. Other MECE items were either by-design
  (RECEIVE…RESPOND bracket lives in the Description/L2, not in L1 ACs), false positives
  (Release/Setup workflows exist), or pre-existing refactors deferred to a separate CR
  (manager frontmatter/prompt redundancy; bootstrap-layer single-owner).

### Open items for the Implement Engineer (not spec work)

- Apply the agent files (`syspilot/agents/*.agent.md`): drop INVOKE, use
  SEND/RECEIVE/RESPOND, replace any "REPLY" with RESPOND, add `name:`/`agent:`
  frontmatter (all agents except Setup/Installer), set `user-invocable: true`
  accordingly.
- Create the `syspilot.orchestration-subagent` instance skill on install (handled by Installer).

### Deferred (separate CR candidate: `workflow-spec-shape-sweep`)

- Broader "procedure-as-AC" cleanup across remaining engineer workflow reqs.
- Frontmatter-prose alignment ("invoke" → SEND) in the CM/PM/QM frontmatter
  rationale text (descriptions only; not workflow prose).

---

## Dogfooding Log (CM)

This CR was developed using the session-first orchestration pattern it specifies —
testing the mechanism live as it was being designed. This section records
observations made during that process.

### Observation 1 — Three distinct session-creation paths

Three mechanisms exist for making an agent addressable as a Jarvis session.
Each bypasses a different subset of the latencies:

| Path | Mechanism | Bypasses | Still bound by |
|------|-----------|----------|----------------|
| **File scaffold** | write `session.yaml` to `.jarvis/sessions/<name>/` | — | Jarvis folder scan (~1 min each direction) |
| **`jarvis_createSession` API** | call the API directly | Jarvis folder scan | VS Code agent-registry refresh (reads `.github/agents/`, not `syspilot/agents/`) |
| **VS Code auto-refresh** | reload window or wait | — | Registry re-reads `.github/agents/` |

**Key finding:** `jarvis_createSession` validates against the **installed instance**
(`.github/agents/`) — not the product source (`syspilot/agents/`). Editing only
the product source (which is correct for a CR) does not make an agent invocable
via the API until the Installer has propagated the change. `jarvis_sendToSession`
to a file-scaffolded session bypasses this constraint and works regardless of the
installed copy's `user-invocable` value.

**Implication for the Installer spec:** `SYSP_SPEC_INSTALLER_SESSION_SCAFFOLD` and
`SYSP_SPEC_INSTALLER_ORCHESTRATION_SELECT` should note that newly written session
scaffolds are not immediately addressable — they become reachable on the next
Jarvis folder scan. Agents newly set to `user-invocable: true` in `.github/agents/`
may additionally require a VS Code window reload before `jarvis_createSession`
accepts them.

### Observation 2 — Jarvis folder scan lags in both directions

The Jarvis session list lags filesystem changes by up to ~1 scan interval
(~1 minute) in **both** directions:
- A newly created `session.yaml` is not immediately listed as a valid destination.
- A deleted session folder lingers in the destination list until the next scan.

Neither direction is an error — both are expected scan-interval behavior. The UAT
for installer session scaffolds already accounts for this by asserting against the
filesystem (file exists) rather than the live destination list.

### Observation 3 — Parallel sessions share the working tree

Multiple agent sessions running in parallel edit files in the same physical
working directory. This is safe **when and only when** their write sets are
disjoint. The additional risk is **read-staleness (TOCTOU)**: if Session A
reads a file, Session B writes it, and Session A acts on its stale read, the
result may be logically inconsistent even though git sees no conflict and
sphinx builds clean.

**Mitigations applied during this CR:**
- Sessions were dispatched with explicitly disjoint file ownership (System
  Designer → `docs/syspilot/`, Test Designer → `docs/syspilot/userstories/uat_*`,
  Dev Engineer → `syspilot/agents/`).
- Each session staged only its own files (`git add <explicit paths>`), never
  `git add -A`.
- The Change Document (written by all sessions) is protected by sectionised
  ownership: each session appends only to its designated section. The MECE gate
  catches any cross-section logical inconsistencies that slip through.

**Deferred:** git worktrees would provide true filesystem isolation for parallel
sessions. This is already documented as a Known Limitation in the orchestration
skill. The above mitigations are sufficient for the current single-worktree
setup.

### Observation 4 — `.github/` is the running instance; product-source edits do not take effect until installed

VS Code, Jarvis, and the `jarvis_createSession` API all read from `.github/agents/`
(the installed instance). Changes to `syspilot/agents/` (the product source) are
not visible to the runtime until propagated by an Installer run. During live
dogfooding of this CR, the `.github/agents/syspilot.implement.agent.md` copy was
hand-edited to `user-invocable: true` to enable the session — this is a deliberate
dogfooding exception, not product practice. The installed copy will be correctly
regenerated by the next Installer run.

### Observation 5 — Spec-quality MECE gate moved to System Designer

Originally anticipated as a separate CM step. During the design session the user
and Designer agreed that the MECE gate belongs in the **Designer workflow** as its
outbound quality gate — single source of truth for MECE responsibility. This
decision is recorded in `SYSP_SPEC_DESIGN_WORKFLOW` and reflected in the updated
`SYSP_SPEC_CM_WORKFLOW`.

### Observation 6 — context.md is the per-session customization layer

Each agent accumulates design decisions, lessons, and preferences in its
`context.md` across sessions. The tailoring of the process happens in these
files — not in the specs (which define the contract). This is the "learning
agents" benefit from the CR's WHY, validated live.

---

## QM Findings

*QM writes findings directly into this section after each review round. PM records
decisions (fix-now / defer / accept-as-is) with rationale in the same section.*

### Round 1

**Reviewed by:** QM
**Review date:** 2026-06-19

#### Findings

| # | Level | Element ID | Finding | Severity |
|---|-------|------------|---------|----------|
| 1 | L1 | `SYSP_REQ_CM_DUTIES` (AC-4), `SYSP_REQ_CM_WORKFLOW` (AC-10) | SSoT violation (stale-copy): both ACs enumerate the Change-Document section list ("L0/L1/L2, MECE, Traceability, Sign-off"), which is owned by the CD template + its SPEC. Restating it creates a copy that silently drifts if the template changes. Detected by experimental QM Standing Check SC-SSOT ("Reference, don't copy"). | medium |

#### PM Decisions

| # | Finding # | Decision | Rationale |
|---|-----------|----------|-----------|
| 1 | 1 | fix-now (fold into this CR) | `req_change_mgr.rst` is already being reworked in this CR (CM workflow → SEND/RECEIVE chains, send→SEND vocabulary fix). Both AC-4 and AC-10 live in that same file with the same SSoT issue — fixing them in the same pass is opportunistic and clean, no separate Mini-CR needed. Designer corrects both ACs to reference the CD template/spec instead of copying the section list. |

### Round 2

**Reviewed by:** QM
**Review date:** 2026-06-19
**Scope:** CM-triggered targeted check of the full CR (L0/L1/L2 MECE per level,
Trace, schema, cross-artefact agent/skill sweep, experimental Standing Checks).

**Gate summary:** Trace PASS · Schema PASS (0 sphinx-needs warnings, build
succeeded) · Vocabulary CAPS consistent in specs (no INVOKE/DELEGATE/REPLY as
orchestration verbs; `Invoke-WebRequest` = cmdlet in the bootstrap Installer,
outside the contract) · Role rename Test Engineer → Test Designer complete (0
leftovers in product) · MECE-gate ownership clean (Designer owns, no double
ownership) · Two orchestration variants cleanly separated · Rename
`_INVOKE → _VERBS` fully propagated (no stale references).

#### Findings

| # | Level | Element ID | Finding | Severity |
|---|-------|------------|---------|----------|
| 2 | L2 + artefact | `SYSP_SPEC_CM_FRONTMATTER` + `syspilot.cm.agent.md`; `SYSP_SPEC_PM_FRONTMATTER` + `syspilot.pm.agent.md` | **SEND-whitelist contradiction with the CR's own Decision 5 / Matrix rule** ("an agent may only SEND to agents declared in its `agents:` frontmatter"). CM workflow Step 7 SENDs a review trigger to QM **and** a readiness notification to PM, but CM `agents:` = `[design, uat, implement, mece, trace, release, docu]` — **lacks `syspilot.qm` and `syspilot.pm`**. PM workflow Step 9 SENDs to CM, but PM `agents:` = `[release, setup]` — **lacks `syspilot.cm`**. Manifests identically in spec and agent file. Root cause may be an unresolved scope question: does the whitelist rule govern manager-to-manager SEND (session messaging) or only subagent dispatch? Either way the current state is self-contradictory. | high |
| 3 | L0 | `SYSP_US_INSTALLER` (AC-9/10/12); new L0 UAT stories `SYSP_US_UAT_INSTALLER_SESSION_FIRST`, `SYSP_US_UAT_SKILL_ORCHESTRATION_VOCAB` | **L0 layer-purity (HOW leaking into WHY).** New/rewritten L0 ACs embed L2 mechanics: file paths (`.jarvis/sessions/<name>/session.yaml`), YAML field names (`name:`, `agent:`), and tool names (`runSubagent()`, `jarvis_sendToSession()`). Contradicts the project's own L0=WHY guideline and the experimental SC-LAYER-PURITY check. (`SYSP_US_SKILL_ORCHESTRATION` itself was correctly reduced to 3 verb-level ACs — the leak is localized to the Installer + UAT stories.) | medium |
| 4 | L2 | `SYSP_SPEC_CM_FRONTMATTER` + `syspilot.cm.agent.md` | **Redundant SEND-whitelist entries.** CM `agents:` lists `mece`, `trace`, `release`, but CM never SENDs to them (Designer runs the per-level MECE gate; QM SENDs to Trace; PM SENDs to Release). Aligns with the Designer's already-disclosed deferral "manager frontmatter redundancy". | low |
| 5 | artefact | `syspilot.cm.agent.md:18` | **Vocabulary nit.** Soul line "you delegate to specialized engineers" uses the lowercase synonym instead of the SEND vocabulary. Aligns with the disclosed deferral "frontmatter-prose alignment (invoke → SEND)". | low |

**Pre-existing / out-of-scope (disclosed, not blocking this CR):** L1
procedure-as-AC and tool-name leaks in `SYSP_REQ_INSTALLER_WORKFLOW` (AC-5
read→fetch→replace→write steps; AC-2 names Python/Sphinx; AC-11 names
sphinx-build). The diff shows this CR only renumbered/reworded these — they were
introduced by earlier CRs (`agent-tool-token-fix` / `installer-spec-rewrite`) and
are already captured by the Designer's disclosed deferral to a separate
`workflow-spec-shape-sweep` CR. Confirmed pre-existing; no action required here.

#### PM Decisions

| # | Finding # | Decision | Rationale |
|---|-----------|----------|-----------|
| 1 | 2 | fix-now — **resolve by removal** | The `agents:` frontmatter is obsolete in the async session model: it enforces nothing (any session may SEND to any session) and the visualization tooling reads the real `message_log.json`, not the frontmatter — so the declared graph has no consumer and can only drift/lie (F2 is proof). Action: REMOVE the `agents:` field from all session-capable agents AND remove the Decision-5 / Matrix "may only SEND to agents in its `agents:` list" rule from the CR's specs (US/REQ/SPEC + agent files). The comm graph is observable from `message_log.json`; it is not declared. **Exception:** `agents:` MAY remain ONLY on `syspilot.setup` (listing `syspilot.installer`) — a genuine synchronous `runSubagent` invoke relationship outside the orchestration contract. |
| 2 | 3 | fix-now | Rewrite the leaking L0 ACs (`SYSP_US_INSTALLER` AC-9/10/12 + the two new L0 UAT stories) to state WHY only — remove file paths, YAML field names, tool names. L2 mechanics belong in the SPEC layer. E.g. "after install, the user's agents are reachable as sessions" — not "`.jarvis/sessions/<name>/session.yaml` exists". |
| 3 | 4 | dissolved by F2 removal | The whole whitelist is gone, so redundant entries no longer exist. No separate action. |
| 4 | 5 | fix-now | `cm.agent.md` Soul line "delegate to" → SEND vocabulary. |

**Merge condition:** PM requires a fully-clean state before merge — this CR seeds a
new `experimental` integration line and must start clean. QM to run **Round 3** and
re-verify after the above fixes are applied.

### Round 3

**Reviewed by:** QM
**Review date:** 2026-06-19
**Scope:** Re-verification of the Round 2 fixes (F2/F3/F5) on HEAD 750a327.

**Verified clean:**
- **F2 (high) — RESOLVED.** `SYSP_REQ_SKILL_ORCHESTRATION_FRONTMATTER` removed
  entirely; no dangling `:links:` or prose reference to it anywhere; no orphaned
  child SPEC. SEND-whitelist rule gone from `SYSP_SPEC_SKILL_ORCHESTRATION_MATRIX`
  and both SKILL.md files. All 13 agent files carry `agents: []` except
  `syspilot.setup` → `["syspilot.installer"]` (the sanctioned bootstrap exception).
- **F4 (low) — DISSOLVED** as designed (no whitelist remains).
- **F5 (low) — RESOLVED.** CM Soul line now reads "you SEND work to specialized
  engineers."
- **Schema PASS** — sphinx-build -W clean, 0 sphinx-needs warnings, build succeeded.

**New / residual finding:**

#### Findings

| # | Level | Element ID | Finding | Severity |
|---|-------|------------|---------|----------|
| 6 | L0 | `SYSP_US_INSTALLER` AC-9 | **F3 only partially applied.** PM's F3 decision explicitly named AC-9/10/12. AC-10 was rewritten WHY-only ✓ and AC-12 removed ✓, but **AC-9 was not touched** — it still reads "Given the workspace contains a ``.jarvis/`` directory …", leaking a tool-specific directory name at L0. Notably the corresponding **L1** AC already carries the correct abstraction ("Given a workspace with session-messaging infrastructure present"), so L0 is now *less* abstract than L1 — an inverted layer gradient. Fix: rewrite AC-9 to the same tool-agnostic phrasing (e.g. "Given the workspace already uses session-based orchestration infrastructure"). | medium |
| 7 | L0 (UAT) | `SYSP_US_UAT_INSTALLER_SESSION_FIRST` | **Judgment item for PM.** The AC outcomes were correctly abstracted (YAML field names `name:`/`agent:` and tool names removed; AC-1 now says "carries the agent's identity as declared in its frontmatter"). However `.jarvis/sessions/` still appears in *Artifacts Under Test* and in the AC-5 *Action* step ("List ``.jarvis/sessions/``"). For a UAT this is the human's observation surface, not an implementation prescription — arguably legitimate. But PM named the UAT stories explicitly under F3 and wants a fully-clean seed. PM to rule: are UAT observation surfaces exempt from L0 layer-purity, or should the directory be abstracted here too? | low |

*Minor note (no finding): `SYSP_US_INSTALLER` AC-11 names ``context.md`` (a
filename). PM did not list AC-11 under F3; flagged only for awareness — same
abstraction question as F3 if PM wants it swept.*

#### PM Decisions

| # | Finding # | Decision | Rationale |
|---|-----------|----------|-----------|
| | 6 | _(awaiting PM)_ | |
| | 7 | _(awaiting PM)_ | |

### Round 4

**Reviewed by:** QM
**Review date:** 2026-06-19
**Scope:** Re-verification of Round 3 fixes (F6/F7) on HEAD 895a63c.

**Verified clean:**
- **F6 (medium) — AC-9 RESOLVED.** `SYSP_US_INSTALLER` AC-9 now reads
  "Given a session-messaging infrastructure is present … session-based
  orchestration variant … synchronous fallback variant" — tool-agnostic,
  matching the L1 abstraction level.
- **F7 (low) — RESOLVED as decided.** UAT I-want, Artifacts Under Test, and AC-5
  action abstracted ("agent's accumulated context", "session scaffold directory").
  AC-1/AC-2 `.jarvis/` preconditions intentionally retained as tester-observable
  setup conditions — accepted-with-disclosure.
- **Schema PASS** — sphinx-build -W clean.

**New residual (same partial-application pattern as Round 3):**

#### Findings

| # | Level | Element ID | Finding | Severity |
|---|-------|------------|---------|----------|
| 8 | L0 | `SYSP_US_INSTALLER` AC-10 | **Adjacent AC missed by the F6 sweep.** AC-9 was abstracted, but the very next AC still reads "Given **the Jarvis orchestration path** is selected …" — a variant/tool name at L0, now inconsistent with the AC-9 it sits beside. (This same AC-10 was reported "rewritten WHY-only" in Round 2, but only its consequent was touched; the precondition clause kept the leak through two rounds.) Fix: "Given the session-based orchestration variant is selected …" to match AC-9. | medium |

*Minor note (no finding, repeat from Round 3): `SYSP_US_INSTALLER` AC-11 still
names ``context.md`` (a filename). Not yet ruled on by PM. Same abstraction
question — flag only.*

**Process observation (routed to PM, logged in scan-state):** three rounds in a
row (R3 AC-9, R4 AC-10) have found the *same class* of leak in an *adjacent*
element that the targeted fix skipped. Recommendation: rather than fixing the
single named AC each round, sweep the whole layer-purity class across
`SYSP_US_INSTALLER` (AC-9/10/11) in one pass. This converges faster than
per-AC whack-a-mole.

#### PM Decisions

| # | Finding # | Decision | Rationale |
|---|-----------|----------|-----------|
| | 8 | _(awaiting PM)_ | |

### Round 5

**Reviewed by:** QM
**Review date:** 2026-06-19
**Scope:** Re-verification of the Round 4 full layer-purity class sweep on HEAD 892838b.

**Verdict:** CLEAN

**Verified clean:**
- **F8 (medium) — RESOLVED.** `SYSP_US_INSTALLER` AC-10 now reads "Given the
  session-based orchestration variant is selected ..." and no longer leaks the
  old variant/tool naming at L0.
- `SYSP_US_INSTALLER` AC-11 now says "agent's accumulated context" instead of
  naming `context.md`.
- `SYSP_US_UAT_INSTALLER_SESSION_FIRST` was swept consistently: context text,
  AC-1/2/4/5 labels and wording are abstracted; the only remaining `.jarvis/`
  references are the already accepted tester-observable AC-1/AC-2 preconditions.
- **Schema PASS** — sphinx-build -W clean, 0 sphinx-needs warnings, build succeeded.

**Scope note:** A separate pre-existing bootstrap workflow line in
`SYSP_US_SETUP` still says "invoke Installer as subagent". That line is outside
the Round-5 fix scope, describes the sanctioned bootstrap exception, and does
not affect the clean verdict for the Round-4 findings.

#### Findings

No findings. Round 4 residual closed; full layer-purity sweep converged.

#### PM Decisions

*(No findings — no decisions required.)*

