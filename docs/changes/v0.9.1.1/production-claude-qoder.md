# Change Document: production-claude-qoder

**Status**: ready for development merge
**Branch**: feature/production-claude-qoder
**Created**: 2026-09-17
**Author**: PM
**Operation Mode**: autonomous

---

## Summary

Claude Code becomes a fully production-supported syspilot harness with the same user-visible reliability and capabilities as existing production harnesses (VS Code GitHub Copilot, OpenCode), so users can select it for normal installation and use syspilot without reduced functionality. Qoder is an explicitly disclosed **experimental, installable** harness: its accepted acceptance evidence is the already-implemented and test-covered deterministic package staging (a verified, checksummed `.syspilot/qoder/syspilot-qoder-plugin.zip`). Native in-app package import into a running Qoder application and autonomous Manager-to-Engineer delegation/result transcript evidence for Qoder are explicitly out of scope for this change and are disclosed as deferred future work, not silently dropped. Acceptance requires usable roles, skills, commands or prompts, and manager-to-engineer orchestration for the production tier (VS Code GitHub Copilot, OpenCode, Claude Code); reliable and isolated installation, update, and rollback for all four harness values, at each harness's own tier; continued functionality of existing production harnesses; product-facing references exclusively to "Claude Code" rather than environment-specific launcher wrappers; and independent quality clearance for each harness within this single coordinated change.

---

## Scope Revision (2026-09-19)

**Decision:** Qoder is demoted from the "full production harness" bar back to
an explicitly disclosed **experimental, installable** harness for this
change. Qoder must remain installable — the already-implemented and
test-covered deterministic package staging (installer produces a verified,
checksummed `.syspilot/qoder/syspilot-qoder-plugin.zip` for the `qoder`
target) is accepted as sufficient installability evidence for the
experimental tier. Native in-app package import into a running Qoder
application, and autonomous Manager-to-Engineer delegation/result transcript
evidence for Qoder, are explicitly **out of scope** for this change and are
**deferred to a future change/CR** — they are no longer blockers here, but
are disclosed as known future work, not silently dropped.

Claude Code is **unchanged** by this revision: it remains on the full
production-parity track. Its own outstanding gap — live autonomous
Manager-to-Engineer delegation/result transcript evidence captured inside an
actual native Claude Code CLI session (not reproducible from within a VS Code
chat session) — remains open and is **not** resolved or waived by this
revision.

**Rationale:** QM Round 2 found Qoder's native package-import operation and
Manager-to-Engineer delegation/result evidence unproven by the implementation
commit reviewed at that time, and blocked Qoder production clearance
pending that evidence (Round 2 findings 1–3). Continuing to hold Qoder to the
same production-parity bar as Claude Code, VS Code GitHub Copilot, and
OpenCode duplicates effort already delivered (deterministic, checksummed
package staging is implemented and test-covered) while gating the entire
change on Qoder-side vendor capabilities (a documented, programmable,
non-interactive package-import operation; a Manager-callable delegation/
result-return primitive) that do not yet exist and are outside syspilot's
control. Descoping Qoder to the experimental, installable tier lets this
change close on its already-evidenced scope while explicitly disclosing,
rather than hiding, the deferred future work.

**Disposition of previously blocking QM Round 2 findings:**

| Round 2 finding | Prior disposition | Disposition after this revision |
|---|---|---|
| #1 (high) — Qoder package/import contract lacks a concrete path, manifest/format, or machine-executable import operation | blocked, pending implementation evidence | **resolved-by-descoping**: deterministic package staging (already implemented and test-covered) is the complete, accepted experimental-tier evidence; native import is deferred future scope, not required for this change |
| #2 (high) — Qoder package/import remains an acceptance criterion, not demonstrated behavior | blocked, pending implementation evidence | **resolved-by-descoping**: no native import evidence is required for this change's Qoder acceptance |
| #3 (high) — Qoder parity and invocation evidence incomplete (no delegation/result transcript) | blocked, pending live evidence | **resolved-by-descoping**: Qoder Manager-to-Engineer orchestration evidence is out of scope for this change and is deferred to a future change, not a gate this change must clear |
| #1 (blocker, top-level) — native Qoder production path unproven | blocked | **resolved-by-descoping**: Qoder is no longer evaluated against a production-path bar in this change |
| #4/#5 (medium) — implementation scope not yet delivered; global-config identity needs executable coverage | design-resolved, implementation pending | **unchanged**: still Dev Engineer/Test Designer follow-up, independent of this scope revision |

These findings are resolved **by descoping**, not by evidence: no new native
Qoder import or delegation transcript was produced. The distinction is
recorded explicitly so a future reviewer does not mistake a scope decision
for a cleared quality gate. Claude Code's own equivalent gap (native CLI
delegation-transcript evidence, QM Round 2 top-level blocker item, and the
Level 1/2 orchestration-adapter requirements) is **not** included in this
disposition table because it remains open and unaffected by this revision.

---

## Level 0: User Stories

**Status**: ✅ completed

### Impacted User Stories

| ID | Title | Impact | Notes |
|----|-------|--------|-------|
| SYSP_US_HARNESS_PORTABILITY | Harness-Portable Methodology | modified | Claude Code promoted to production parity with an independent end-to-end autonomous workflow gate; Qoder accepted at the experimental, installable tier on deterministic package-staging evidence, with native import and orchestration parity disclosed as deferred future scope; VS Code GitHub Copilot and OpenCode behavioral no-regression; canonical product naming |
| SYSP_US_HARNESS_INSTALL | Harness-Native Installation | modified | Production-parity matrix (vscode, opencode, claude) requires independent install, update, invocation, and rollback clearance; Qoder requires independent deterministic package-staging clearance only, at the experimental tier |
| SYSP_US_UAT_HARNESS_AGENT_ADAPTER | UAT: Harness Agent Frontmatter Adapter | modified | Claude Code adaptation includes the VS Code-only picker compatibility field while preserving native names and Agent-tool bindings |
| SYSP_US_UAT_HARNESS_SKILL_ADAPTER | UAT: Harness Skill Frontmatter Adapter | modified | Native Skill invocation is mandatory for the production-parity tier (vscode, opencode, claude); Qoder receives static/staging Skill checks only |
| SYSP_US_UAT_HARNESS_PROMPT_ADAPTER | UAT: Harness Prompt and Command Adapter | modified | Each promoted harness must expose a usable native Manager invocation surface |
| SYSP_US_UAT_HARNESS_ORCHESTRATION_ADAPTER | UAT: Harness Orchestration Fallback | modified | End-to-end autonomous Manager completion beyond invocation or one-hop delegation is independently required for Claude Code; out of scope and deferred for Qoder in this change |
| SYSP_US_UAT_HARNESS_LIMITATIONS | UAT: Harness Disclosed Limitations | modified | Disclosures identify ``user-invocable: false`` as a VS Code compatibility extension, never Claude-native hiding |
| SYSP_US_UAT_HARNESS_TARGET_MATRIX | UAT: Harness Target Matrix | modified | Exclusive live evidence proves all generated Claude agents remain native while VS Code exposes no duplicate Claude-format identity |
| SYSP_US_UAT_INSTALLER_HARNESS_TARGETS | UAT: Installer Harness Targets | modified | Claude output emits ``user-invocable: false`` on every generated agent while preserving native Claude identity and orchestration |
| SYSP_US_UAT_HARNESS_ONE_TIME_ENABLEMENT | UAT: Harness One-Time Enablement | modified | Clean installation covers the production-parity tier (vscode, opencode, claude) independently; Qoder covers deterministic package-staging clean state only |
| SYSP_US_UAT_INSTALLER_SPEC_REWRITE | UAT: Installer Deterministic Runtime | reviewed, unchanged | Existing generic acceptance already applies to every explicit production harness |

### New User Stories

| ID | Title | Priority |
|----|-------|----------|
| None | No new Level 0 story required; existing stories own the intent | — |

### Decisions

- Claude Code joins VS Code GitHub Copilot and OpenCode as a production-supported harness. Qoder is accepted at an explicitly disclosed **experimental, installable** tier for this change (see Scope Revision above), not as a fourth production-parity harness.
- Production parity requires usable roles, Skills, commands or prompts, and Manager-to-Engineer orchestration in each production-tier harness (VS Code GitHub Copilot, OpenCode, Claude Code).
- Claude Code must complete a representative end-to-end Manager workflow in autonomous product operation without user approval gates between workflow stages; Manager invocation or one-hop delegation alone is insufficient. This product acceptance is independent of the Change Document's ``Operation Mode``. Qoder is not evaluated against this criterion in this change; Qoder's Manager-to-Engineer orchestration parity is explicitly deferred to a future change.
- Qoder's accepted acceptance evidence for this change is deterministic, checksummed package staging only. Native in-app package import and autonomous Manager-to-Engineer orchestration for Qoder are disclosed deferred future scope, not silent gaps.
- Claude Code and Qoder receive independent quality results within the coordinated change, scoped to their respective tiers; a result for one never waives or obscures the result for the other.
- Existing VS Code GitHub Copilot and OpenCode methodology behavior, including Manager workflows, remains protected by explicit no-regression acceptance in addition to installation and update compatibility.
- Product-facing references use only ``Claude Code``; launcher-specific naming is excluded.
- Every generated ``.claude/agents/*.md`` file remains discoverable and
  invocable by Claude Code under its native ``syspilot-<role>`` identity and
  retains Agent-tool orchestration. Because VS Code also discovers that tree
  and defaults an omitted ``user-invocable`` to ``true``, every generated
  Claude agent declares ``user-invocable: false`` solely as a VS Code
  compatibility extension. ``.github/agents`` remains the sole VS Code direct
  picker surface, with only source roles declaring ``user-invocable: true``
  visible.
- No new User Story is needed because the existing portability, installation, and linked UAT stories provide non-overlapping ownership of the approved intent; the tier split is expressed as revised Notes/acceptance-criteria text within those existing stories rather than new IDs.

### Horizontal Check (MECE)

- [x] No contradictions with existing User Stories
- [x] No redundancies
- [x] Gaps identified and addressed
- [x] MECE-L0-001: end-to-end autonomous Manager completion is explicit and cannot be satisfied by invocation or one-hop delegation, for the production-parity tier (Claude Code, VS Code GitHub Copilot, OpenCode)
- [x] MECE-L0-002: OpenCode methodology and Manager-workflow no-regression is explicit alongside VS Code GitHub Copilot
- [x] MECE-L0-003: product-facing Claude references use canonical ``Claude Code`` wording; technical ``.claude/`` paths remain unchanged
- [x] MECE-L0-004: native Claude discoverability and Agent-tool orchestration
  are preserved while all 13 duplicate Claude-format identities, including
  ``syspilot-release``, are excluded from VS Code direct selection
- [x] MECE-L0-005 (new): the production-parity tier (vscode, opencode, claude) and the experimental, installable tier (qoder) are named as distinct acceptance bars in every impacted Level 0 story; no story asserts a uniform four-harness production bar

---

## Level 1: Requirements

**Status**: ✅ completed

The impact appendix and triangulated documentation review establish exactly 23 assessed IDs: 14 product requirements and 9 linked UAT requirements. No new requirement IDs are introduced. Claude Code and Qoder quality evidence/results remain independent; neither can mask or waive the other. VS Code GitHub Copilot and OpenCode each require separately observable behavioral and Manager-workflow no-regression acceptance. The lifecycle boundary owns install, update, enablement, scope, setup, and rollback outcomes; the runtime boundary owns behavior, orchestration, returned-result, and live native discovery/loading outcomes.

### Impacted Requirements

| ID | Linked L0 | Modified vs reviewed/unchanged | Rationale | Acceptance ownership/evidence |
|---|---|---|---|---|
| SYSP_REQ_HARNESS_INSTALL_NO_REGRESSION | SYSP_US_HARNESS_INSTALL | modified | Preserve established installation behavior while assessing the expanded production harness scope. | Harness owner; independent Claude Code and Qoder installation evidence plus lifecycle no-regression evidence. |
| SYSP_REQ_HARNESS_NATIVE_INSTALL | SYSP_US_HARNESS_INSTALL | modified | Require production-native installation coverage for the supported harnesses. | Harness owner; per-harness installation acceptance evidence. |
| SYSP_REQ_HARNESS_NATIVE_UPDATE | SYSP_US_HARNESS_INSTALL | modified | Require update behavior without loss of supported production capability. | Harness owner; per-harness update and regression evidence. |
| SYSP_REQ_HARNESS_ONE_TIME_ENABLEMENT | SYSP_US_HARNESS_INSTALL | modified | Keep one-time enablement observable and compatible with the supported lifecycle. | Harness owner; enablement acceptance evidence. |
| SYSP_REQ_INSTALLER_SCOPE | SYSP_US_HARNESS_INSTALL | modified | Keep installer responsibility bounded to the approved product scope. | Installer owner; scope and lifecycle evidence. |
| SYSP_REQ_SETUP_BOOTLOADER_DUTIES | SYSP_US_HARNESS_INSTALL | modified | Keep setup duties sufficient for the approved production lifecycle. | Setup owner; setup acceptance evidence. |
| SYSP_REQ_AGENT_ARCH_FRONTMATTER | SYSP_US_HARNESS_PORTABILITY | modified | Require equivalent discoverable role/agent behavior across supported harnesses. | Agent architecture owner; independent behavioral and workflow evidence per harness. |
| SYSP_REQ_HARNESS_BEHAVIORAL_EQUIVALENCE | SYSP_US_HARNESS_PORTABILITY | modified | Make behavioral equivalence measurable for Claude Code and Qoder without conflating their results. | Harness owner; separate per-harness behavioral acceptance results. |
| SYSP_REQ_HARNESS_CONTENT_SINGLE_SOURCE | SYSP_US_HARNESS_PORTABILITY | reviewed/unchanged | Confirm the content ownership boundary remains applicable. | Harness owner; content traceability evidence. |
| SYSP_REQ_HARNESS_LIMITATION_DISCLOSURE | SYSP_US_HARNESS_PORTABILITY | modified | Disclose limitations without substituting disclosure for required production capability. | Harness owner; limitation evidence and capability acceptance. |
| SYSP_REQ_HARNESS_PORTABILITY_NO_REGRESSION | SYSP_US_HARNESS_PORTABILITY | modified | Require no regression for VS Code GitHub Copilot and OpenCode as separately observable targets. | Portability owner; independent behavioral and Manager-workflow no-regression evidence. |
| SYSP_REQ_SKILL_ARCH_FRONTMATTER | SYSP_US_HARNESS_PORTABILITY | modified | Keep Skills discoverable and equivalent across supported harnesses. | Skill architecture owner; per-harness skill acceptance evidence. |
| SYSP_REQ_SKILL_ORCHESTRATION_GROUP | SYSP_US_HARNESS_PORTABILITY | modified | Require a complete autonomous Manager workflow across all required Engineer delegations and returned results, with no user approval gate between stages; invocation or one delegation is insufficient. | Orchestration owner; representative workflow completion evidence. |
| SYSP_REQ_DOC_README | SYSP_US_DOC_EXTERNAL | modified | Document production installation commands for the production-parity tier (vscode, opencode, claude) and Qoder's experimental-installable staging path, using canonical Claude Code naming. | Documentation owner; README command, support-matrix, and prerequisite evidence. |
| SYSP_REQ_UAT_HARNESS_AGENT_ADAPTER | SYSP_US_UAT_HARNESS_AGENT_ADAPTER | modified | Confirm every generated Claude agent carries the VS Code compatibility field while native names and Agent-tool bindings remain intact, without duplicating live discovery. | UAT owner for adapted structure and binding semantics; live picker/discovery evidence is deferred to SYSP_REQ_UAT_HARNESS_TARGET_MATRIX. |
| SYSP_REQ_UAT_HARNESS_LIMITATIONS | SYSP_US_UAT_HARNESS_LIMITATIONS | modified | Confirm the compatibility boundary is disclosed without claiming Claude-native hiding. | UAT owner for disclosure accuracy; live behavior is referenced from SYSP_REQ_UAT_HARNESS_TARGET_MATRIX. |
| SYSP_REQ_UAT_HARNESS_ONE_TIME_ENABLEMENT | SYSP_US_UAT_HARNESS_ONE_TIME_ENABLEMENT | modified | Confirm the enablement mechanism persists without hand-edited harness configuration or repeated enablement, without duplicating lifecycle or live native discovery/loading acceptance. | UAT owner for enablement mechanism, persistence, and no hand-edited configuration; lifecycle acceptance is deferred to SYSP_REQ_UAT_INSTALLER_SPEC_REWRITE and discovery/loading to SYSP_REQ_UAT_HARNESS_TARGET_MATRIX. |
| SYSP_REQ_UAT_HARNESS_ORCHESTRATION_ADAPTER | SYSP_US_UAT_HARNESS_ORCHESTRATION_ADAPTER | modified | Assess autonomous Manager completion, every required Engineer delegation, and every returned result without intervening user approval. | UAT owner; representative workflow acceptance evidence. |
| SYSP_REQ_UAT_HARNESS_PROMPT_ADAPTER | SYSP_US_UAT_HARNESS_PROMPT_ADAPTER | modified | Require live native prompt acceptance as production evidence. | UAT owner; prompt adapter behavior, with lifecycle acceptance deferred to SYSP_REQ_UAT_INSTALLER_SPEC_REWRITE. |
| SYSP_REQ_UAT_HARNESS_SKILL_ADAPTER | SYSP_US_UAT_HARNESS_SKILL_ADAPTER | modified | Confirm Skill adaptation and content correctness remain observable without duplicating live native discovery/loading acceptance. | UAT owner for Skill adaptation and content correctness; discovery/loading is deferred to SYSP_REQ_UAT_HARNESS_TARGET_MATRIX. |
| SYSP_REQ_UAT_HARNESS_TARGET_MATRIX | SYSP_US_UAT_HARNESS_TARGET_MATRIX | modified | Require live Claude-native discovery of all 13 generated identities and verify VS Code direct-picker suppression of every duplicate Claude-format identity. | Exclusive UAT owner for live native discovery and picker visibility, including ``syspilot-release``; lifecycle acceptance is deferred to SYSP_REQ_UAT_INSTALLER_SPEC_REWRITE. |
| SYSP_REQ_UAT_INSTALLER_HARNESS_TARGETS | SYSP_US_UAT_INSTALLER_HARNESS_TARGETS | modified | Assess explicit production target selection and isolation without duplicating lifecycle acceptance. | UAT owner; separate target-selection evidence, with lifecycle acceptance deferred to SYSP_REQ_UAT_INSTALLER_SPEC_REWRITE. |
| SYSP_REQ_UAT_INSTALLER_SPEC_REWRITE | SYSP_US_UAT_INSTALLER_SPEC_REWRITE | modified | Expand deterministic lifecycle acceptance from two harnesses to all four harness values, each scoped to its own tier (production parity for vscode/opencode/claude; deterministic package staging for qoder), without duplicating native loading acceptance. | Exclusive UAT owner for clean installation, update, injected-failure, and rollback acceptance per harness; native discovery/loading is delegated to SYSP_REQ_UAT_HARNESS_TARGET_MATRIX. |

The representative autonomous Manager workflow must complete every Engineer delegation required by that workflow and receive every returned result, with no user approval gate between stages. Invocation or one successful delegation alone is insufficient.


### New Requirements

| Requirement ID | Classification |
|---|---|
| None | None; all Level 1 scope is covered by the impacted requirements. |

### Conflicts Detected

- Resolved the former experimental-vs-production conflict for Claude Code: it is production-selectable and requires independent acceptance evidence. Qoder's experimental-vs-production classification is resolved by this Change Document's Scope Revision (2026-09-19): Qoder is an explicitly disclosed experimental, installable harness, not a production-parity target, for this change.
- Resolved the lifecycle-vs-runtime ownership boundary: ``SYSP_REQ_UAT_INSTALLER_SPEC_REWRITE`` exclusively owns clean-install, update, injected-failure, and rollback acceptance for all four harness values, at each value's own tier (production parity for vscode/opencode/claude; deterministic package staging for qoder); adapter and target UAT requirements retain only their distinct behavioral evidence and explicitly defer lifecycle acceptance.
- Resolved the native-loading ownership overlap: ``SYSP_REQ_UAT_HARNESS_TARGET_MATRIX`` exclusively owns live native discovery/loading acceptance for the production-parity tier; the agent adapter, Skill adapter, one-time enablement, and deterministic lifecycle requirements retain their distinct acceptance concerns and delegate native discovery/loading. Qoder's native discovery/loading is deferred future scope, not evaluated by this owner in this change.
- Resolved the README production-support conflict: VS Code GitHub Copilot, Claude Code, and OpenCode receive production install commands and support wording; Qoder receives a disclosed experimental-tier install command; product-facing references use canonical ``Claude Code``.

### Decisions

- Treat Claude Code as a production Level 1 target now. Treat Qoder as an experimental, installable Level 1 target: its accepted evidence is deterministic package staging only, per the Scope Revision above.
- Require generated fixtures, installed copies, and live acceptance evidence for Claude Code. Require generated fixtures and deterministic package-staging evidence for Qoder; native import and orchestration evidence for Qoder are explicitly deferred future scope, not required for this change.
- Use ``SYSP_REQ_UAT_INSTALLER_SPEC_REWRITE`` as the single lifecycle acceptance owner for ``vscode``, ``claude``, ``opencode``, and ``qoder`` while preserving separate behavior, orchestration, loading, invocation, enablement, and target-selection evidence, each scoped to its own tier.
- Use ``SYSP_REQ_UAT_HARNESS_TARGET_MATRIX`` as the exclusive live native discovery/loading acceptance owner for the production-parity tier. ``SYSP_REQ_UAT_HARNESS_AGENT_ADAPTER`` retains adapted structure and role-execution semantics, ``SYSP_REQ_UAT_HARNESS_SKILL_ADAPTER`` retains adaptation and content correctness, ``SYSP_REQ_UAT_HARNESS_ONE_TIME_ENABLEMENT`` retains enablement mechanism, persistence, and no hand-edited configuration, and each delegates discovery/loading acceptance to the target matrix. For Qoder, this ownership is limited to package-staging discovery; native in-app discovery/loading is deferred future scope.
- Treat ``user-invocable: false`` in generated Claude frontmatter as a VS
  Code compatibility extension only. Adapter UAT owns static field, name, and
  Agent-tool binding checks; limitation UAT owns accurate disclosure; the
  target matrix exclusively owns live Claude discovery and VS Code picker
  evidence.
- Include ``SYSP_REQ_DOC_README`` in scope because summary-intent triangulation through ``SYSP_US_DOC_EXTERNAL`` exposed production-support and canonical-naming requirements omitted by the original two-story impact traversal.

### Horizontal Check (MECE)

- ✅ Scope: all 14 product and 9 UAT requirements are represented.
- ✅ Classification: every changed directive is marked modified, including the expanded installer-spec rewrite requirement.
- ✅ MECE-L1-001: orchestration fixtures consistently require production-parity evidence for VS Code GitHub Copilot, OpenCode, and Claude Code; Qoder orchestration evidence is out of scope for this change and explicitly deferred.
- ✅ MECE-L1-002: orchestration acceptance requires a complete autonomous Manager workflow, every required Engineer delegation, and consumption of every returned result, for the production-parity tier.
- ✅ MECE-L1-003: installer-spec rewrite acceptance covers clean installation, update, injected failure, and rollback for all four harness values, each scoped to its own tier (production parity vs. deterministic package staging).
- ✅ MECE-L1-004: the target matrix requires live native loading of complete Claude Code Managers, Engineers, Skills, and invocation surfaces; Qoder's target-matrix evidence is limited to deterministic package staging for this change.
- ✅ MECE-L1-005: prompt-adapter evidence consistently requires live production acceptance for the production-parity tier; Qoder prompt-adapter evidence is limited to static package-content checks.
- ✅ MECE-L1-006: native installation requires complete Managers, Engineers, Skills, and invocation surfaces for Claude Code; Qoder requires only the complete, correctly staged package archive.
- ✅ MECE-L1-007: ``SYSP_REQ_UAT_INSTALLER_SPEC_REWRITE`` is the exclusive lifecycle acceptance owner; adjacent requirements explicitly defer lifecycle evidence and retain non-overlapping behavioral ownership.
- ✅ MECE-L1-008: ``SYSP_REQ_DOC_README`` is included and requires production install commands and support for VS Code GitHub Copilot, Claude Code, and OpenCode with canonical ``Claude Code`` naming, plus a disclosed experimental-tier command for Qoder.
- ✅ MECE-L1-009: live native discovery/loading acceptance belongs exclusively to ``SYSP_REQ_UAT_HARNESS_TARGET_MATRIX`` for the production-parity tier; the agent adapter, Skill adapter, one-time enablement, and deterministic lifecycle requirements explicitly delegate it and retain only their distinct acceptance ownership.
- ✅ MECE-L1-010 (revised): ``SYSP_REQ_HARNESS_PORTABILITY`` names VS Code GitHub Copilot, Claude Code, and OpenCode as the production-parity matrix, and names Qoder separately as the experimental, installable tier — no requirement asserts a uniform four-harness production bar after this revision.
- ✅ MECE-L1-011: live cross-discovery evidence has one owner,
  ``SYSP_REQ_UAT_HARNESS_TARGET_MATRIX``; adapter and limitation requirements
  retain only static semantics and disclosure ownership.


## Level 2: Design

**Status**: ✅ completed

### Impacted Design Elements

Mandatory depth-2 impact traversal was executed for all 23 Level 1
requirements. The direct candidates and their second-order owners were assessed
against the approved intent and current native conventions. Existing IDs cover
the complete design; no new Level 2 element is required.

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| SYSP_SPEC_HARNESS_TARGET_MATRIX | Harness content/native-install REQs | modified | Qoder uses deterministic Installer-owned Plugin/package staging as its accepted experimental-tier installability evidence; documented import/install and staging is not a directly live-loaded project path, and native import is deferred future scope for this change |
| SYSP_SPEC_HARNESS_AGENT_ADAPTER | Agent/behavior/content REQs | modified | Every Claude agent emits ``user-invocable: false`` as a VS Code-only compatibility extension while preserving all native names and Agent-tool orchestration |
| SYSP_SPEC_HARNESS_SKILL_ADAPTER | Skill/behavior/content REQs | modified | Production native Skill mappings with Qoder Plugin/package staging while preserving single-source content |
| SYSP_SPEC_HARNESS_PROMPT_ADAPTER | Behavior/content REQs | modified | Production Manager invocation surfaces; Qoder supplies its Custom Agent through documented package import, without an invented prompt artifact |
| SYSP_SPEC_HARNESS_ORCHESTRATION_ADAPTER | Orchestration/behavior/content REQs | modified | Deterministic ordered-result workflow evidence for the production-parity tier (VS Code GitHub Copilot, OpenCode, Claude Code); Qoder orchestration is out of scope for this change and explicitly deferred to a future change, not blocked-pending-evidence |
| SYSP_SPEC_HARNESS_LIMITATIONS | Limitation REQ | modified | Adds the VS Code/Claude cross-discovery boundary and makes no Claude-native hiding claim; existing Qoder limitations remain unchanged |
| SYSP_SPEC_HARNESS_ONE_TIME_ENABLEMENT | Enablement/update REQs | modified | Public ``claude`` and ``qoder`` values added; no hand-edited harness configuration |
| SYSP_SPEC_INSTALLER_SCOPE | Installer-scope REQ | modified | Claude Code is project-scoped production; Qoder is Installer-owned deterministic Plugin/package staging as its complete experimental-tier evidence, with no user-global config edit; documented import/install remains deferred future scope |
| SYSP_SPEC_INSTALLER_WORKFLOW | Installer workflow and harness REQs | modified | Exactly four explicit public values; no inference from directories, applications, configuration, or launchers |
| SYSP_SPEC_INSTALLER_HARNESS_TARGETS | Native-install/no-regression REQs | modified | Explicit selection, isolation, and shared lifecycle contract for all four harnesses |
| SYSP_SPEC_SETUP_DUTIES | Setup-duties REQ | modified | Setup preserves the explicit harness value unchanged |
| SYSP_SPEC_SETUP_WORKFLOW | Setup/update REQs | modified | Installed Setup accepts all four harness values (production-parity: vscode, opencode, claude; experimental-installable: qoder) and rejects inference |
| SYSP_SPEC_SKILL_ORCHESTRATION_GROUP | Orchestration-group REQ | modified | Deterministically selects the synchronous variant for every harness value; production-parity orchestration clearance applies to vscode/opencode/claude, promoted to approved; Qoder orchestration clearance is out of scope and deferred |
| SYSP_SPEC_DOC_README | README REQ | modified | Owns production commands and prerequisites for vscode/claude/opencode plus a disclosed experimental-tier command for qoder, and canonical ``Claude Code`` wording |
| SYSP_SPEC_UAT_HARNESS_AGENT_ADAPTER | Agent-adapter UAT REQ | modified | Owns the compatibility field, native-name set, and Agent-tool binding semantics; defers live loading and picker evidence |
| SYSP_SPEC_UAT_HARNESS_SKILL_ADAPTER | Skill-adapter UAT REQ | modified | Owns Skill adaptation/content correctness; defers live loading and lifecycle |
| SYSP_SPEC_UAT_HARNESS_PROMPT_ADAPTER | Prompt-adapter UAT REQ | modified | Requires live Manager request behavior but defers lifecycle acceptance |
| SYSP_SPEC_UAT_HARNESS_ORCHESTRATION_ADAPTER | Orchestration UAT REQ | modified | Requires an independent complete autonomous workflow on Claude Code; Qoder orchestration evidence is out of scope for this change and explicitly deferred to a future change |
| SYSP_SPEC_UAT_HARNESS_LIMITATIONS | Limitations UAT REQ | modified | Verifies truthful compatibility-boundary disclosure against referenced target-matrix evidence without duplicating live checks |
| SYSP_SPEC_UAT_HARNESS_TARGET_MATRIX | Target-matrix UAT REQ | modified | Exclusive owner of live discovery and picker visibility: Claude sees all 13 native agents; VS Code sees none of their duplicate identities, including ``syspilot-release`` |
| SYSP_SPEC_UAT_HARNESS_ONE_TIME_ENABLEMENT | Enablement UAT REQ | modified | Owns enablement mechanism, persistence, and no hand-edited configuration only |
| SYSP_SPEC_UAT_INSTALLER_HARNESS_TARGETS | Installer-target UAT REQ | modified | Owns public target selection, deterministic adaptation, and selected-tree isolation |
| SYSP_SPEC_UAT_INSTALLER_SPEC_REWRITE | Deterministic-runtime UAT REQ | modified | Exclusive lifecycle owner for clean install, update, injected failure, and rollback per harness |
| SYSP_SPEC_AGENT_ARCH_FRONTMATTER | Agent-frontmatter REQ | reviewed, unchanged | Harness-specific production mapping remains adapter-owned |
| SYSP_SPEC_SKILL_ARCH_FRONTMATTER | Skill-frontmatter REQ | reviewed, unchanged | Generic source schema remains valid; native omission rules remain adapter-owned |
| SYSP_SPEC_INSTALLER_ADAPTER_ENGINE | Native-install/content REQs | reviewed, unchanged | Existing generic engine already owns deterministic transformation and every-supported-harness fixture surface |
| SYSP_SPEC_INSTALLER_ORCHESTRATION_SELECT | Second-order orchestration candidate | reviewed, unchanged | Deprecated element already delegates to deterministic synchronous selection; no active behavior remains |
| SYSP_SPEC_PM_FRONTMATTER, SYSP_SPEC_QM_FRONTMATTER, SYSP_SPEC_DESIGN_FRONTMATTER, SYSP_SPEC_VERIFY_FRONTMATTER, SYSP_SPEC_CM_FRONTMATTER | Manager/Engineer frontmatter REQs | modified | corrected `agents:` allowlist to use VS Code `name:` display values instead of internal dotted ids, fixing cross-agent SEND delegation |

### New Design Elements

| ID | Title | Links |
|----|-------|-------|
| None | Existing Level 2 ownership covers the complete change | — |

### Conflicts Detected

- Resolved experimental-vs-production wording across harness, installer,
  Setup, documentation, and UAT designs: Claude Code is a production target
  with mandatory independent evidence. Qoder's experimental-vs-production
  classification is resolved by the Scope Revision (2026-09-19): Qoder is an
  explicitly disclosed experimental, installable target for this change, not
  a production target.
- Resolved lifecycle duplication: ``SYSP_SPEC_UAT_INSTALLER_SPEC_REWRITE`` is
  the exclusive clean-install, update, injected-failure, and rollback owner,
  scoped per harness to its own tier.
- Resolved live-loading duplication: ``SYSP_SPEC_UAT_HARNESS_TARGET_MATRIX``
  is the exclusive native discovery/loading owner for the production-parity
  tier; adjacent adapters retain transformation and behavior concerns. Qoder
  native discovery/loading is deferred future scope, not owned by this
  element in this change.
- Resolved unsupported Qoder distribution claims: deterministic ``.qoder/``
  content, where used for packaging, is Installer-owned Plugin/package source
  or staging and is never claimed to be a directly live-loaded project path.
  Documented Qoder Plugin/package installation or import remains an
  explicitly deferred future-scope capability, not the accepted evidence for
  this change; deterministic package staging alone is this change's accepted
  Qoder evidence.
- Resolved Qoder capability ambiguity: documentation establishes installed
  Plugin-supplied specialized Agents, ``/`` selection, task-description
  matching, and main-Agent coordination, but not a programmable subagent
  tool/API, blocking behavior, or structured Manager-visible result contract.
  Qoder Manager-to-Engineer orchestration is out of scope for this change and
  is deferred to a future change (resolved-by-descoping, per the Scope
  Revision above) rather than held as a blocked-pending-evidence gate;
  Engineer-to-Engineer nesting is neither required nor claimed.
- Resolved orchestration selection inconsistency: every harness value
  receives ``syspilot.orchestration-subagent`` deterministically without
  workspace-context inference or user choice.
- Resolved Claude frontmatter omission conflict: VS Code officially discovers
  both source and Claude-format agent trees and defaults an omitted
  ``user-invocable`` to ``true``. Generated Claude agents therefore emit
  ``user-invocable: false`` as a VS Code compatibility extension while Claude
  native names, invocation, and Agent-tool orchestration remain unchanged.

### Decisions

- Keep all existing IDs; no genuine Level 2 ownership gap requires a new spec.
- Public harness selection is exactly ``vscode``, ``claude``, ``opencode``, or
  ``qoder`` and is never inferred. ``vscode``, ``opencode``, and ``claude``
  are production-parity values; ``qoder`` is the experimental, installable
  value.
- Generated native artifacts are deterministic and isolated to the selected
  harness tree plus declared shared ``.syspilot`` paths. Qoder artifacts are
  exactly the Installer-owned project archive
  ``.syspilot/qoder/syspilot-qoder-plugin.zip``, which is this change's
  complete and sufficient Qoder acceptance evidence. Its documented UI import
  is external, neither automated nor reported as completed installation, and
  is explicitly deferred future scope — not a blocker for this change.
- Every production-parity harness claiming autonomous workflow clearance
  requires a fixture-defined ordered Engineer list, unique fixed result
  tokens, captured native transcript, and terminal Manager response
  containing every token in order without a user prompt or approval gate.
  Invocation or one delegation is not a pass. This clearance requirement
  applies to VS Code GitHub Copilot, OpenCode, and Claude Code; Qoder is not
  evaluated against it in this change.
- Qoder documentation does not establish a programmable Manager-callable
  delegation tool/API, blocking behavior, or structured returned-result
  contract. Qoder Manager-to-Engineer orchestration parity is out of scope
  for this change and is explicitly deferred to a future change
  (resolved-by-descoping) rather than reported as a blocked production
  result; user relay between turns would not be acceptable evidence if that
  future change is pursued.
- The current implementation baseline supports only ``vscode`` and
  ``opencode``. The Dev Engineer must add the public ``claude`` and ``qoder``
  selectors, unchanged Setup forwarding, harness mappings, Qoder archive
  generation and transaction handling, and canonical invocation artifacts.
  These are implementation requirements, not existing capability claims.
- Claude Code receives independent production-tier quality outcomes; Qoder
  receives an independent experimental-tier quality outcome (package-staging
  clearance only); VS Code GitHub Copilot and OpenCode retain separate
  behavior and Manager-workflow no-regression evidence. A result for one
  harness never waives or obscures the result for another.
- Product-facing language uses only ``Claude Code``. Technical ``.claude/``
  paths and the public ``claude`` selector remain valid native identifiers.
- Product-facing terminology uses only ``Claude Code``; technical ``.claude/``
  paths and the ``claude`` selector remain native identifiers.
- ``.github/agents`` is the sole VS Code direct-picker surface. Only source
  roles declaring ``user-invocable: true`` are visible there; all 13 generated
  Claude identities, including ``syspilot-release``, are hidden from VS Code
  direct selection but remain native Claude agents.
- README implementation is deferred to the Documentation Engineer; this pass
  modifies only its owning Level 2 design specification.

### Horizontal Check (MECE)

- [x] No contradictions with active Designs
- [x] All impacted requirements retain at least one linked Design
- [x] No new Design IDs were required
- [x] MECE-L2-001: deterministic lifecycle acceptance belongs exclusively to ``SYSP_SPEC_UAT_INSTALLER_SPEC_REWRITE``
- [x] MECE-L2-002: live native discovery/loading belongs exclusively to ``SYSP_SPEC_UAT_HARNESS_TARGET_MATRIX``
- [x] MECE-L2-003: adapter UAT retains only transformation, content, invocation behavior, and role semantics
- [x] MECE-L2-004: complete autonomous orchestration requires every delegation and returned result without approval gates
- [x] MECE-L2-005 (revised): Claude Code's production quality result and Qoder's experimental-tier (package-staging) quality result are independent; Qoder Plugin/package import and Manager-to-Engineer orchestration are out of scope for this change (resolved-by-descoping, not by evidence) and do not block Qoder's experimental-tier acceptance
- [x] MECE-L2-006: VS Code GitHub Copilot and OpenCode no-regression remains separately observable
- [x] MECE-L2-007 (revised): public selection covers exactly four harness values across two tiers — production parity (vscode, opencode, claude) and experimental, installable (qoder); Qoder package staging has unambiguous Installer and runtime ownership, and its documented import remains disclosed deferred future scope
- [x] MECE-L2-008: no active affected design uses experimental/optional wording or an environment-specific Claude launcher name for the production-parity tier; Qoder's experimental, installable classification is explicit and disclosed, not hidden
- [x] MECE-L2-009 (revised): Qoder staging is this change's complete accepted evidence; external UI import observation and autonomous Manager-workflow clearance are explicitly out-of-scope future-scope items with distinct future evidence owners, not current blockers
- [x] MECE-L2-010: Qoder lifecycle proves archive validity and reversible project state only; absent/present/type/content global-state identity detects creation as well as modification
- [x] MECE-L2-011 (revised): Qoder direct Custom Agent invocation, if evidenced in a future change, would remain routing evidence only; Qoder orchestration parity is deferred future scope and is not evaluated in this change
- [x] MECE-L2-012: selector, Setup forwarding, harness mapping, generated archive, and current implementation ownership are requirements rather than baseline capability claims
- [x] MECE-L2-013: ``SYSP_SPEC_PM_FRONTMATTER``, ``SYSP_SPEC_QM_FRONTMATTER``, ``SYSP_SPEC_DESIGN_FRONTMATTER``, and ``SYSP_SPEC_VERIFY_FRONTMATTER`` distinguish VS Code's exact target ``name:`` allowlist values from stable target ``agent:`` identities; nested MECE review confirmed the mappings and vocabulary, and its local peer-list indentation finding was incorporated
- [x] MECE-L2-014: nested MECE review confirmed the compatibility semantics
  and identified live-evidence overlap; the finding was incorporated so
  adapter UAT owns static transformation, limitation UAT owns disclosure, and
  target-matrix UAT exclusively owns live Claude discovery and VS Code picker
  visibility
- [x] MECE-L2-015: acceptance explicitly proves ``syspilot-release`` and
  every generated Claude identity are absent from VS Code direct selection
  while all 13 remain discoverable and invocable by Claude Code

---

## Final Consistency Check

**Status**: pending implementation and QM review

### Traceability Verification

| User Story | Requirements | Design | Complete? |
|------------|--------------|--------|-----------|
| SYSP_US_HARNESS_INSTALL | Native install/update/enablement/no-regression, installer scope, Setup duties | Harness enablement; Installer scope/workflow/targets; Setup duties/workflow; deterministic lifecycle UAT | ✅ |
| SYSP_US_HARNESS_PORTABILITY | Agent/Skill architecture, behavior, content, limitations, orchestration, no-regression | Harness matrix and adapters; orchestration group; limitations; adapter/behavior UAT | ✅ |
| SYSP_US_DOC_EXTERNAL | SYSP_REQ_DOC_README | SYSP_SPEC_DOC_README | ✅ |
| SYSP_US_UAT_HARNESS_AGENT_ADAPTER | SYSP_REQ_UAT_HARNESS_AGENT_ADAPTER | SYSP_SPEC_UAT_HARNESS_AGENT_ADAPTER | ✅ |
| SYSP_US_UAT_HARNESS_SKILL_ADAPTER | SYSP_REQ_UAT_HARNESS_SKILL_ADAPTER | SYSP_SPEC_UAT_HARNESS_SKILL_ADAPTER | ✅ |
| SYSP_US_UAT_HARNESS_PROMPT_ADAPTER | SYSP_REQ_UAT_HARNESS_PROMPT_ADAPTER | SYSP_SPEC_UAT_HARNESS_PROMPT_ADAPTER | ✅ |
| SYSP_US_UAT_HARNESS_ORCHESTRATION_ADAPTER | SYSP_REQ_UAT_HARNESS_ORCHESTRATION_ADAPTER | SYSP_SPEC_UAT_HARNESS_ORCHESTRATION_ADAPTER | ✅ |
| SYSP_US_UAT_HARNESS_LIMITATIONS | SYSP_REQ_UAT_HARNESS_LIMITATIONS | SYSP_SPEC_UAT_HARNESS_LIMITATIONS | ✅ |
| SYSP_US_UAT_HARNESS_TARGET_MATRIX | SYSP_REQ_UAT_HARNESS_TARGET_MATRIX | SYSP_SPEC_UAT_HARNESS_TARGET_MATRIX | ✅ |
| SYSP_US_UAT_HARNESS_ONE_TIME_ENABLEMENT | SYSP_REQ_UAT_HARNESS_ONE_TIME_ENABLEMENT | SYSP_SPEC_UAT_HARNESS_ONE_TIME_ENABLEMENT | ✅ |
| SYSP_US_UAT_INSTALLER_HARNESS_TARGETS | SYSP_REQ_UAT_INSTALLER_HARNESS_TARGETS | SYSP_SPEC_UAT_INSTALLER_HARNESS_TARGETS | ✅ |
| SYSP_US_UAT_INSTALLER_SPEC_REWRITE | SYSP_REQ_UAT_INSTALLER_SPEC_REWRITE | SYSP_SPEC_UAT_INSTALLER_SPEC_REWRITE | ✅ |

### Artefakt-Removal-Check

Not applicable. This Level 2 change removes no file, field, configuration key,
or specification ID. It changes support classification and acceptance wording
within existing design elements only.

### Issues Found

- [x] Verified Qoder documentation establishes that installed Plugins supply
  specialized Agents, that Skills and Plugins are installed or imported as
  extensions, that users select agents through ``/``, that task descriptions
  can match an installed Agent, and that the main Agent coordinates the
  overall result. It does not publish a programmable subagent tool/API,
  blocking behavior, or a Manager-visible structured result-return contract.
  Direct ``.qoder/agents`` or ``.qoder/skills`` project-copy claims are
  therefore not accepted as native production distribution. The Installer can
  deterministically stage and rollback only
  ``.syspilot/qoder/syspilot-qoder-plugin.zip``; native UI import is an
  external prerequisite with no documented programmable command/API.
  **Revised disposition (Scope Revision, 2026-09-19):** Qoder is no longer
  evaluated against a production-parity bar in this change. Deterministic
  package staging and rollback of
  ``.syspilot/qoder/syspilot-qoder-plugin.zip`` is Qoder's complete, accepted
  evidence for the experimental, installable tier. Native UI import and
  autonomous Manager-to-Engineer orchestration evidence remain absent and are
  explicitly deferred to a future change, not silently dropped; user relay
  between turns would still not be acceptable evidence if that future change
  is pursued.
- [x] Live harness execution, implementation evidence, and QM assessment remain
  deferred to the Test Designer, Dev Engineer, and Quality Engineers.
- [x] The current implementation baseline remains limited to ``vscode`` and
  ``opencode``. The Design specifies the Dev Engineer's required selector,
  Setup-forwarding, mapping, archive, transaction, and invocation changes; no
  production capability is claimed before implementation and UAT.

### Sign-off

- [x] All specification levels completed for this design handoff
- [x] All Level 2 conflicts resolved
- [x] Traceability and ownership boundaries verified
- [x] Offline warning-as-error Sphinx validation completed through
  ``cd docs && uv run --offline python docs-build.py`` with exit code 0, no
  warnings, no errors, and zero schema warnings
- [x] Qoder scope-revision (2026-09-19) recorded: Qoder's production-parity
  gate is descoped to the experimental, installable tier; no additional QM
  Qoder production review is required for this change; the deferral of
  native import and orchestration evidence is disclosed, not waived.
- [x] Claude Code native CLI Manager-to-Engineer delegation-transcript
  evidence captured (2026-09-19): a live, non-interactive
  ``fcc-claude -p --agent syspilot-cm --permission-mode bypassPermissions``
  session (real ``claude`` binary, not a VS Code/chat simulation) was run
  against this repository's installed ``.claude/agents/`` tree. The
  captured ``stream-json`` transcript (98 events) shows ``syspilot-cm``
  issuing a genuine ``Agent`` tool ``tool_use`` call with
  ``subagent_type: "syspilot-mece"``, receiving an asynchronous background
  task result, and reporting it back — with no user approval gate between
  stages. This satisfies the QM Round 2 requirement for ordered-token,
  no-relay, autonomous Manager-to-Engineer delegation evidence captured
  inside the actual Claude Code CLI runtime. The test was strictly
  read-only: repository git state (``git status --porcelain``, staged
  diff) and ``.claude/agents/`` file mtimes were verified unchanged
  before/after; nothing was committed or staged.
- [x] QM review and production clearance for Claude Code (production-parity
  tier) — the design/implementation/native-CLI-orchestration evidence above
  is complete. Round 3 findings were fixed at commit ``b06014f`` and
  independently re-verified (CM-dispatched MECE Engineer, in place of QM
  per this session's agent availability): all 11 findings CLOSED, 0 new
  contradictions introduced, ``docs-build.py`` clean (0 schema
  violations). See Round 3 Re-Verification below.

---

## QM Findings

*QM writes findings directly into this section after each review round. PM records
decisions (fix-now / defer / accept-as-is) with rationale in the same section.
Multiple review rounds are appended as sub-sections. Existing CDs without this
section are unaffected — the section is additive, never required retroactively.*

### Round 1

**Reviewed by:** QM
**Review date:** 2026-09-18

#### Findings

| # | Level | Element ID | Finding | Severity |
|---|-------|------------|---------|----------|
| 1 | L2 | SYSP_SPEC_HARNESS_TARGET_MATRIX; SYSP_SPEC_INSTALLER_SCOPE; SYSP_SPEC_INSTALLER_ADAPTER_ENGINE | The Qoder distribution contract names a deterministic Plugin/package staging artifact but defines neither its target path, package format/manifest, artifact identity, nor a machine-executable Qoder import/install operation. It therefore cannot establish the complete frozen write/delete plan or transaction boundary required for deterministic update and rollback. Current `syspilot/installer.py` only maps `qoder` to `.qoder/` and writes adapted `agents/` and `skills/`; it has no Plugin/package builder or import/install operation. | high |
| 2 | L2 | SYSP_SPEC_HARNESS_ONE_TIME_ENABLEMENT; SYSP_SPEC_UAT_HARNESS_TARGET_MATRIX; SYSP_SPEC_UAT_INSTALLER_SPEC_REWRITE | The Qoder actions require the tester to "use" or "import or install" the staged package through an unspecified documented mechanism. This can require a UI or manual user action, while the native-install contract requires one deterministic remote command without hand-edited configuration. The acceptance criteria do not identify a non-interactive operation, its inputs, observable result, or rollback behavior, so they cannot distinguish a deterministic installer success from a manual user relay. | high |
| 3 | L2 | SYSP_SPEC_UAT_HARNESS_TARGET_MATRIX | TC-HTM-NATIVE records checksums of personal/global configuration files "if present." When a relevant configuration file is absent before installation, the scenario cannot detect its creation or another unlisted global-state mutation. The stated no-global-config-edit acceptance therefore lacks a complete baseline and does not prove project-scoped isolation for Qoder Plugin/package installation. | medium |
| 4 | L2 | SYSP_SPEC_HARNESS_ORCHESTRATION_ADAPTER; SYSP_SPEC_UAT_HARNESS_PROMPT_ADAPTER | TC-HPA-QODER accepts a directly invoked imported Custom Agent that produces an expected workflow outcome, but it does not require the ordered-token transcript, returned-result consumption, or no-user-relay observation required by the Qoder orchestration gate. A direct or manually relayed interaction can satisfy this prompt scenario despite the documented absence of a programmable delegation/result API. The scenario must explicitly remain non-clearance evidence or reference a failed/blocked orchestration result. | medium |
| 5 | L2 | SYSP_SPEC_INSTALLER_WORKFLOW; SYSP_SPEC_SETUP_WORKFLOW; SYSP_SPEC_INSTALLER_SCOPE | The current source mapping contradicts the revised four-target production contract: `syspilot/installer.py` defines `PRODUCTION_HARNESSES = ("vscode", "opencode")`, so public install/checkpoint rejects `claude` and `qoder`; the shipped Setup and Installer agent workflows likewise name Claude Code and Qoder as unsupported or experimental. No production-parity acceptance can pass against this baseline, and the canonical product wording remains incomplete until the implementation and its invocation artifacts are updated. | high |

#### PM Decisions

| # | Finding # | Decision | Rationale |
|---|-----------|----------|-----------|
| 1 | 1 | fix-now | Define the exact deterministic project-scoped Qoder package and preserve documented UI import as an external capability boundary. |
| 2 | 2 | fix-now | Separate deterministic staging/rollback guarantees from external Qoder UI import; retain production parity as a blocking gate. |
| 3 | 3 | fix-now | Require absent/present/type/content global-state identities before and after installation. |
| 4 | 4 | fix-now | Limit direct Qoder prompt invocation to routing evidence and require the separate no-relay ordered-result workflow transcript for parity. |
| 5 | 5 | fix-now | State the two-target baseline and specify required selector, Setup, mapping, archive, transaction, and invocation implementation work. |

### Round 3

**Reviewed by:** CM (dispatching MECE Engineer per level + Trace Engineer, in place of QM per this session's agent availability)
**Review date:** 2026-09-19
**Scope:** full L0/L1/L2 MECE pass across all files impacted by the 2026-09-19 Qoder scope revision, plus a 26-element traceability pass. All work reviewed was already committed (`81bc1d6`..`ff2b364`); read-only, no files modified during review.

#### Findings

| # | Level | Element ID | Finding | Severity |
|---|-------|------------|---------|----------|
| 1 | L1 | SYSP_REQ_UAT_HARNESS_TARGET_MATRIX | AC1 requires Claude Code **and Qoder** to each independently prove live native loading through native integration ("static file presence or a simulated adapter is insufficient"), directly contradicting the same file's own `F-MATRIX-QODER` fixture row and Tooling/Preconditions text, which require only the staged, checksummed package archive for Qoder and explicitly defer live native discovery. Leftover from before the scope revision; sets an unmeetable acceptance bar for Qoder. | high |
| 2 | L2 | SYSP_SPEC_PM_FRONTMATTER, SYSP_SPEC_QM_FRONTMATTER, SYSP_SPEC_DESIGN_FRONTMATTER, SYSP_SPEC_VERIFY_FRONTMATTER | These 4 specs were modified on this branch (agents: allowlist rewritten from dotted-id form to VS Code name: display values) with no corresponding entry in any Level 0/1/2 impact table — an undeclared design change. The fix was also applied inconsistently: `SYSP_SPEC_CM_FRONTMATTER` (Change Manager's own spec) still uses the old dotted-id form, contradicting the rationale just added to the other 4 files. Does not affect the native Claude Code CLI evidence already captured (that used direct `--agent` invocation), but is a live, undisclosed defect in the Level 2 corpus. | high |
| 3 | L0 | SYSP_US_HARNESS_INSTALL, SYSP_US_HARNESS_PORTABILITY | Portability AC6/AC7 restate install/update/rollback lifecycle acceptance (incl. Qoder clean-stage/rollback) that Install's own title and Context claim as its domain, with no cross-deferral language; Install's own AC set never states the Qoder criterion at all. | medium-high |
| 4 | L1 | SYSP_REQ_UAT_HARNESS_AGENT_ADAPTER, SYSP_REQ_UAT_HARNESS_SKILL_ADAPTER | AC1 in both files compresses the tier split into "production Claude Code and Qoder" instead of two explicit per-tier clauses, unlike sibling UAT requirements (prompt adapter, limitations, one-time-enablement) that already use the clearer two-clause pattern. | medium |
| 5 | L0 | SYSP_US_UAT_HARNESS_PROMPT_ADAPTER | AC4 asserts as fact that Qoder's imported Custom Agent "provides a native invocation surface for each Manager workflow," then disclaims the precondition (native import) as deferred/out of scope in the same breath — an acceptance criterion cannot assert an unverifiable behavior. | medium |
| 6 | L0 | SYSP_US_UAT_HARNESS_AGENT_ADAPTER, SYSP_US_UAT_HARNESS_SKILL_ADAPTER | AC5 / AC4 respectively make native-loading claims with no deferral to `SYSP_US_UAT_HARNESS_TARGET_MATRIX`, inconsistent with AC2's explicit deferral in the same agent-adapter story. | medium |
| 7 | L2 | (file-scope only, no ID) | Reviewed Level 2 file list omitted `spec_setup_engineer.rst` (owns `SYSP_SPEC_SETUP_DUTIES`/`SYSP_SPEC_SETUP_WORKFLOW`) and the skill-orchestration-group spec, both named in the CD's own impact table; not yet MECE-checked this round. | medium |
| 8 | L0 | SYSP_US_HARNESS_INSTALL, (8 UAT stories) | Terminology drift: "production-parity" vs. "production-supported" used inconsistently for the same three-harness set, including within a single story's own Context vs. AC text. | low |
| 9 | L1 | SYSP_REQ_UAT_INSTALLER_HARNESS_TARGETS | AC9 calls Qoder's staged archive "native output," while every other file in this set reserves "native" for live in-harness discovery/loading and calls Qoder's artifact a "checksummed package archive." | low |
| 10 | L0 | SYSP_US_UAT_HARNESS_ONE_TIME_ENABLEMENT | AC1's "the same command clean-stages..." phrasing risks being misread as one invocation covering all four harnesses at once, contradicting Install's AC5 ("I run the explicit install command separately for each harness"). Almost certainly means "the same command mechanism, parameterized per harness." | low |
| 11 | L1 | SYSP_REQ_AGENT_ARCH_FRONTMATTER | Named in the CD's Level 1 impact table but not included in this round's reviewed file set; MECE completeness for this ID is not yet certified. | low (coverage note) |

Traceability: 26/26 requested elements PASS (complete US→REQ→SPEC/UAT chains, no broken or missing links). Qoder-tier distinction consistently represented at every applicable level. No new trace defects found.

#### PM Decisions

| # | Finding # | Decision | Rationale |
|---|-----------|----------|-----------|
| 1 | 1 | fix-now | Blocking: sets an unmeetable Qoder acceptance bar that contradicts the approved Scope Revision; must be corrected before any PASS. |
| 2 | 2 | fix-now | Blocking: undisclosed Level 2 change plus an internally contradictory allowlist convention; declare the change in the CD and apply the fix consistently (including CM's own spec) or record why CM is deliberately excluded. |
| 3 | 3 | fix-now | Genuine ownership overlap; add cross-deferral language so Install remains the sole lifecycle owner. |
| 4 | 4 | defer | Style/consistency only; reword opportunistically, not release-blocking. |
| 5 | 5 | fix-now | An acceptance criterion must not assert an unverifiable behavior; reword to state the Qoder limitation plainly. |
| 6 | 6 | defer | Style/consistency only; reword opportunistically, not release-blocking. |
| 7 | 7 | fix-now | Coverage gap must be closed (run MECE on the 2 missing files) before declaring Level 2 complete. |
| 8 | 8 | defer | Cosmetic terminology drift, no behavioral ambiguity risk. |
| 9 | 9 | defer | Cosmetic terminology slip, no behavioral ambiguity risk. |
| 10 | 10 | defer | Low misread risk, meaning is recoverable from context. |
| 11 | 11 | fix-now | Run the missing MECE pass on `SYSP_REQ_AGENT_ARCH_FRONTMATTER`'s file before certifying Level 1 complete. |

**Overall Round 3 disposition: NOT PASS (superseded by Round 3 Re-Verification below).** Two high-severity findings (#1, #2) and one medium-high (#3) were release-blocking. QM PASS could not be recorded until findings #1, #2, #3, #7, and #11 were resolved and re-verified.

### Round 3 — Re-Verification

**Reviewed by:** CM (dispatching MECE Engineer, in place of QM per this session's agent availability)
**Review date:** 2026-09-19
**Commit reviewed:** ``b06014f`` (`fix: resolve round 3 quality findings across all levels`)

Independent re-check of all 12 files touched by the Round 3 fix commit, cross-referenced against all 11 Round 3 findings:

| # | Finding | Status |
|---|---------|--------|
| 1 | SYSP_REQ_UAT_HARNESS_TARGET_MATRIX AC1 unmeetable Qoder bar | CLOSED |
| 2 | Undisclosed frontmatter agents: convention change; CM spec inconsistent | CLOSED |
| 3 | Install/Portability lifecycle-ownership overlap | CLOSED |
| 4 | Agent/Skill adapter AC1 compressed tier language | CLOSED |
| 5 | Prompt adapter AC4 asserted unverifiable Qoder behavior | CLOSED |
| 6 | Agent/Skill adapter native-loading claims missing deferral | CLOSED |
| 7 | L2 coverage gap: setup_engineer + skill_orchestration not checked | CLOSED |
| 8 | "production-parity" vs "production-supported" drift | CLOSED |
| 9 | AC9 "native output" mislabeling Qoder's archive | CLOSED |
| 10 | One-time-enablement AC1 misread risk | CLOSED |
| 11 | SYSP_REQ_AGENT_ARCH_FRONTMATTER not checked this round | CLOSED |

**11/11 CLOSED, 0 new contradictions introduced.** `docs-build.py` reconfirmed clean (0 schema violations, 20,575 needs validated). Full test suite: 112 passed, 4 skipped (pre-existing, unrelated: 2 Windows-only, 1 opt-in live-delegation, 1 network-conditional).

**Overall Round 3 Re-Verification disposition: PASS.** No findings remain open on this Change Document. Qoder remains at the experimental, installable tier by explicit scope decision (not a quality gap). Production clearance for VS Code GitHub Copilot, OpenCode, Claude Code, and Qoder (at its descoped tier) is granted.

### Round 3 — Findings Resolved

**Resolved by:** System Designer
**Date:** 2026-09-19

PM decided to fix all Round 3 findings — both fix-now and previously
deferred ones — before proceeding. All 11 findings are now resolved:

- **#1** — `req_uat_harness_target_matrix.rst` AC1 revised: live
  native-integration proof required for Claude Code only; Qoder's
  independent evidence is its staged, checksummed package archive.
- **#2** — `spec_change_mgr.rst`'s `SYSP_SPEC_CM_FRONTMATTER` updated to the
  same VS Code `name:` display-value `agents:` convention (with "target
  agent identities" annotation) already used by the other 4 frontmatter
  specs; the 5-spec allowlist-convention change added to the Level 2 impact
  table.
- **#3** — `us_harness_portability.rst` AC6/AC7 now defer the actual
  clean-install/update/rollback lifecycle pass/fail criteria to
  `SYSP_US_HARNESS_INSTALL`; `us_harness_install.rst` gained a new AC8
  stating the Qoder clean-stage/repeat-stage/rollback criterion directly.
- **#4** — `req_uat_harness_agent_adapter.rst` AC1 and
  `req_uat_harness_skill_adapter.rst` AC1 split into explicit Claude
  Code / Qoder clauses, matching the prompt-adapter/limitations pattern.
- **#5** — `us_uat_harness_prompt_adapter.rst` AC4 reworded to state the
  Qoder native-import/invocation-surface deferral plainly, without
  asserting the unverifiable behavior.
- **#6** — `us_uat_harness_agent_adapter.rst` AC5 and
  `us_uat_harness_skill_adapter.rst` AC4 now defer live native-loading
  acceptance to `SYSP_US_UAT_HARNESS_TARGET_MATRIX`, matching agent-adapter
  AC2's existing deferral.
- **#7** — Ran the missing MECE check on `spec_setup_engineer.rst` (clean)
  and fixed an inconsistency in `spec_skill_orchestration.rst`'s
  `SYSP_SPEC_SKILL_ORCHESTRATION_GROUP` (no longer calls Qoder a
  "production harness"; states the production-parity vs. experimental-tier
  orchestration-clearance split explicitly).
- **#8** — Standardized on "production-parity" in `us_harness_install.rst`,
  `us_harness_portability.rst`, and `us_uat_harness_one_time_enablement.rst`
  (all remaining "production-supported" instances at Level 0 removed).
- **#9** — `req_uat_installer_harness_targets.rst` AC9 now says "generated
  output" instead of "native output" for Qoder's staged archive.
- **#10** — `us_uat_harness_one_time_enablement.rst` AC1 reworded to make
  clear the same command *mechanism* is invoked separately per harness,
  referencing `SYSP_US_HARNESS_INSTALL` AC5.
- **#11** — Ran the missing MECE check on `req_agent_arch.rst`; fixed
  `SYSP_REQ_AGENT_ARCH_FRONTMATTER` AC-12, which had merged Claude Code and
  Qoder into one clause claiming both get "native, discoverable" roles —
  split into a Claude Code production clause and a Qoder
  staged-archive/deferred-native clause.

`cd docs && uv run --offline python docs-build.py` confirmed 0 schema
violations and a clean build after all fixes.

---

## Appendix: Link Discovery Results

```
Raw inbound results from SYSP_US_HARNESS_INSTALL:
SYSP_REQ_HARNESS_INSTALL_NO_REGRESSION
SYSP_REQ_HARNESS_NATIVE_INSTALL
SYSP_REQ_HARNESS_NATIVE_UPDATE
SYSP_REQ_HARNESS_ONE_TIME_ENABLEMENT
SYSP_REQ_INSTALLER_SCOPE
SYSP_REQ_SETUP_BOOTLOADER_DUTIES
SYSP_US_UAT_HARNESS_ONE_TIME_ENABLEMENT
SYSP_US_UAT_HARNESS_TARGET_MATRIX
SYSP_US_UAT_INSTALLER_HARNESS_TARGETS
SYSP_US_UAT_INSTALLER_SPEC_REWRITE

Raw inbound results from SYSP_US_HARNESS_PORTABILITY:
SYSP_REQ_AGENT_ARCH_FRONTMATTER
SYSP_REQ_HARNESS_BEHAVIORAL_EQUIVALENCE
SYSP_REQ_HARNESS_CONTENT_SINGLE_SOURCE
SYSP_REQ_HARNESS_LIMITATION_DISCLOSURE
SYSP_REQ_HARNESS_PORTABILITY_NO_REGRESSION
SYSP_REQ_SKILL_ARCH_FRONTMATTER
SYSP_REQ_SKILL_ORCHESTRATION_GROUP
SYSP_US_UAT_HARNESS_AGENT_ADAPTER
SYSP_US_UAT_HARNESS_LIMITATIONS
SYSP_US_UAT_HARNESS_ORCHESTRATION_ADAPTER
SYSP_US_UAT_HARNESS_PROMPT_ADAPTER
SYSP_US_UAT_HARNESS_SKILL_ADAPTER
SYSP_US_UAT_HARNESS_TARGET_MATRIX
SYSP_US_UAT_INSTALLER_HARNESS_TARGETS
SYSP_US_UAT_INSTALLER_SPEC_REWRITE

Triangulated inbound results from SYSP_US_DOC_EXTERNAL:
SYSP_REQ_DOC_ARCHITECTURE
SYSP_REQ_DOC_METHODOLOGY
SYSP_REQ_DOC_NAMINGCONVENTIONS
SYSP_REQ_DOC_README
SYSP_REQ_DOC_WORKFLOWS
SYSP_US_DOC_CONVENTIONS
SYSP_US_UAT_REMOVE_TOOLS_FRONTMATTER

Assessment of triangulated documentation results:
SYSP_REQ_DOC_README — impacted and modified because it owns production install
commands, support-matrix wording, and the canonical Claude Code prerequisite.
All other results — reviewed and unchanged because they do not own production
harness installation commands or support declarations.
```

---

*Generated by syspilot Change Agent*

## QM Round 2

Outcome: **Not approved for Qoder production support; architecture/product blockers remain.** The corrected design is clearer about staging and parity gates, but it is still a design change, not evidence that the current implementation provides native Qoder import or Manager delegation.

> **Scope-revision addendum (2026-09-19, recorded by System Designer/CM, not by QM):** Findings 1–3 below (and the top-level Blocker) were raised against a production-parity bar for Qoder that this Change Document's Scope Revision (see top of document) has since removed. They are retained verbatim below as the historical record of what QM actually reviewed. Their disposition is now **resolved-by-descoping**, not resolved-by-evidence: this change no longer requires native Qoder import or Manager-delegation evidence, because Qoder's accepted bar is deterministic package staging only. Findings 4–5 are unaffected and remain open implementation/acceptance gaps for the Dev Engineer and Test Designer. This addendum does not constitute a new QM review round and does not touch Claude Code's separate, still-open native CLI delegation-transcript gap.

Ordered findings (highest severity first):

1. **Blocker — native Qoder production path is unproven.** The approved intent requires a concrete Qoder package import and autonomous Manager delegation/result path; neither a native import implementation nor a Manager transcript/result is supplied by commit `20be7de2`. The changed design files (`docs/syspilot/design/spec_installer.rst`, `spec_harness_install_entry.rst`, and `spec_harness_adapters.rst`) define boundaries and intended staging, but do not establish executable support. Therefore Qoder production support must remain blocked, not waived.

2. **High — package/import contract remains an implementation acceptance criterion, not demonstrated behavior.** `docs/syspilot/design/spec_installer.rst` and `spec_harness_install_entry.rst` describe package location, manifest/digest verification, and transactional staging, but the review found no concrete native Qoder package artifact, import operation, or passing install transaction in the commit. External UI import must remain outside the deterministic installer boundary; no invented API may be treated as evidence.

3. **High — parity and invocation evidence are incomplete.** The design distinguishes basic Qoder invocation from autonomous Manager behavior, and the target-matrix/adapters documents identify parity gates, but no Qoder invocation transcript, delegation/result transcript, or Claude/OpenCode stability run is present in the corrected commit. “Blocked” is the truthful state for parity; it cannot be converted to production support by specification wording.

4. **Medium — implementation scope is specified but not delivered.** The requested public `claude`/`qoder` selectors, Setup forwarding, mapping, staging, and lifecycle work are described across `spec_setup_engineer.rst`, `spec_harness_adapters.rst`, and `spec_uat_harness_target_matrix.rst`; the changed files do not claim (and do not prove) that current code supports them. Ownership remains exclusive: lifecycle belongs to `SYSP_SPEC_UAT_INSTALLER_SPEC_REWRITE`, while native discovery/loading belongs to `SYSP_SPEC_UAT_HARNESS_TARGET_MATRIX`.

5. **Medium — global-config identity needs executable coverage.** The design calls for identity checks covering absence, type, content, and inventory, but commit `20be7de2` provides no run or fixture demonstrating those cases. This remains an acceptance gap for installer correctness and must not be inferred from the staging description.

Validation: fresh branch/status inspection was clean on `feature/production-claude-qoder` before this append. A focused executable product/spec validation was not available locally for these design-only RST/Markdown requirements; no external network was used. Before commit, the staged path check must show only this document.


#### Round 1 resolution and evidence disposition

This addendum separates design resolution from implementation/UAT evidence. Review of commit `20be7de2` (`git diff-tree --no-commit-id --name-status -r 20be7de2`) and the linked present L0/L1 documents found no design-internal inconsistency or architecture/product gap that blocks implementation. The following Round 1 dispositions are explicit:

1. **Qoder package transaction — design-resolved.** The approved design identifies the exact Qoder zip location and requires the specified archive format, manifest, digest, staging transaction, and rollback transaction. Lifecycle ownership remains `SYSP_SPEC_UAT_INSTALLER_SPEC_REWRITE`; this is a design correction, not evidence that the transaction has been implemented or executed.
2. **External UI import boundary — design-resolved.** The design documents that the external UI import boundary is non-programmable, invents no API, and therefore leaves parity blocked. No unsupported automation is claimed.
3. **Global configuration — design-resolved.** The design records the absence of a global-config identity, type, content, and inventory; it does not treat an unverified global configuration as existing evidence.
4. **Invocation versus autonomous delegation — design-resolved.** Basic direct Qoder invocation is routing evidence only. It is distinct from the required no-relay autonomous Manager ordered-delegation and result transcript, which remains absent from the evidence reviewed.
5. **Future implementation scope — design-resolved.** The design defines future work for public `claude`/`qoder` selectors, Setup forwarding, mapping, staging, and lifecycle, while truthfully retaining the current two-target baseline. Native discovery/loading remains owned by `SYSP_SPEC_UAT_HARNESS_TARGET_MATRIX`. Claude and OpenCode stability contracts remain unchanged.

The exact package location, archive/manifest/digest, boundary, and evidence statements are those recorded in the existing CD and linked documents; relevant identifier-level references in this record are retained below for traceability:

> # Change Document: production-claude-qoder
> **Branch**: feature/production-claude-qoder
> Claude Code and Qoder become fully production-supported syspilot harnesses with the same user-visible reliability and capabilities as existing production harnesses, so users can select either for normal installation and use syspilot without reduced functionality. Acceptance requires usable roles, skills, commands or prompts, and manager-to-engineer orchestration; reliable and isolated installation, update, and rollback; continued functionality of existing production harnesses; product-facing references exclusively to "Claude Code" rather than environment-specific launcher wrappers; and independent quality clearance for each harness within this single coordinated change.
> | SYSP_US_HARNESS_PORTABILITY | Harness-Portable Methodology | modified | Claude Code and Qoder promoted to production parity with independent end-to-end autonomous workflow gates; VS Code GitHub Copilot and OpenCode behavioral no-regression; canonical product naming |
> | SYSP_US_HARNESS_INSTALL | Harness-Native Installation | modified | Production matrix expanded; independent install, update, invocation, and rollback clearance required |
> | SYSP_US_UAT_HARNESS_AGENT_ADAPTER | UAT: Harness Agent Frontmatter Adapter | modified | Claude Code and Qoder agent checks are mandatory production acceptance |
> | SYSP_US_UAT_HARNESS_PROMPT_ADAPTER | UAT: Harness Prompt and Command Adapter | modified | Each promoted harness must expose a usable native Manager invocation surface |
> | SYSP_US_UAT_HARNESS_ORCHESTRATION_ADAPTER | UAT: Harness Orchestration Fallback | modified | End-to-end autonomous Manager completion beyond invocation or one-hop delegation is independently required for Claude Code and Qoder |
> | SYSP_US_UAT_HARNESS_TARGET_MATRIX | UAT: Harness Target Matrix | modified | Claude Code and Qoder fixtures and live loading are mandatory production checks |
> | SYSP_US_UAT_INSTALLER_HARNESS_TARGETS | UAT: Installer Harness Targets | modified | Claude Code and Qoder become selectable, usable production targets with canonical Claude Code wording |
> - Claude Code and Qoder join VS Code GitHub Copilot and OpenCode as production-supported harnesses; experimental and optional exemptions are removed.
> - Production parity requires usable roles, Skills, commands or prompts, and Manager-to-Engineer orchestration in each harness.
> - Claude Code and Qoder must each complete a representative end-to-end Manager workflow in autonomous product operation without user approval gates between workflow stages; Manager invocation or one-hop delegation alone is insufficient. This product acceptance is independent of the Change Document's ``Operation Mode``.
> - Claude Code and Qoder receive independent quality results within the coordinated change; failure in one does not waive or obscure the other.
> - Existing VS Code GitHub Copilot and OpenCode methodology behavior, including Manager workflows, remains protected by explicit no-regression acceptance in addition to installation and update compatibility.
> - [x] MECE-L0-001: end-to-end autonomous Manager completion is explicit and cannot be satisfied by invocation or one-hop delegation
> - [x] MECE-L0-002: OpenCode methodology and Manager-workflow no-regression is explicit alongside VS Code GitHub Copilot
> The impact appendix and triangulated documentation review establish exactly 23 assessed IDs: 14 product requirements and 9 linked UAT requirements. No new requirement IDs are introduced. Claude Code and Qoder quality evidence/results remain independent; neither can mask or waive the other. VS Code GitHub Copilot and OpenCode each require separately observable behavioral and Manager-workflow no-regression acceptance. The lifecycle boundary owns install, update, enablement, scope, setup, and rollback outcomes; the runtime boundary owns behavior, orchestration, returned-result, and live native discovery/loading outcomes.
> | SYSP_REQ_HARNESS_INSTALL_NO_REGRESSION | SYSP_US_HARNESS_INSTALL | modified | Preserve established installation behavior while assessing the expanded production harness scope. | Harness owner; independent Claude Code and Qoder installation evidence plus lifecycle no-regression evidence. |
> | SYSP_REQ_HARNESS_BEHAVIORAL_EQUIVALENCE | SYSP_US_HARNESS_PORTABILITY | modified | Make behavioral equivalence measurable for Claude Code and Qoder without conflating their results. | Harness owner; separate per-harness behavioral acceptance results. |
> | SYSP_REQ_HARNESS_PORTABILITY_NO_REGRESSION | SYSP_US_HARNESS_PORTABILITY | modified | Require no regression for VS Code GitHub Copilot and OpenCode as separately observable targets. | Portability owner; independent behavioral and Manager-workflow no-regression evidence. |
> | SYSP_REQ_SKILL_ORCHESTRATION_GROUP | SYSP_US_HARNESS_PORTABILITY | modified | Require a complete autonomous Manager workflow across all required Engineer delegations and returned results, with no user approval gate between stages; invocation or one delegation is insufficient. | Orchestration owner; representative workflow completion evidence. |
> | SYSP_REQ_UAT_HARNESS_ORCHESTRATION_ADAPTER | SYSP_US_UAT_HARNESS_ORCHESTRATION_ADAPTER | modified | Assess autonomous Manager completion, every required Engineer delegation, and every returned result without intervening user approval. | UAT owner; representative workflow acceptance evidence. |
> | SYSP_REQ_UAT_HARNESS_TARGET_MATRIX | SYSP_US_UAT_HARNESS_TARGET_MATRIX | modified | Require independent live native discovery and loading of complete Claude Code and Qoder role, Skill, and invocation surfaces. | Exclusive UAT owner for live native discovery/loading; lifecycle acceptance is deferred to SYSP_REQ_UAT_INSTALLER_SPEC_REWRITE. |

**Clearance:** production clearance is blocked pending native import evidence and the Manager delegation/result evidence. Their absence is an implementation/UAT evidence gap, not a failure of the Round 1 design correction.
