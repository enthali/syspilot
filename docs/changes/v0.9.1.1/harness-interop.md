# Change Document: harness-interop

**Status**: completed
**Branch**: feature/harness-interop
**Created**: 2026-09-16
**Author**: PM
**Operation Mode**: user-guided

---

## Summary

Today, syspilot's agents and skills only run inside VS Code with GitHub Copilot Chat — a user working in Claude Code, OpenCode, or Qoder cannot use syspilot's methodology (PM → CM → Designer → Developer → Tester → QM) at all, because the agents are expressed exclusively as VS Code custom-agent files bound to Copilot Chat's tool/model conventions. This CR asks that syspilot become usable, with equivalent behavior and outcomes, from at least Claude Code, OpenCode, and Qoder, in addition to VS Code Copilot Chat, so users are not locked into a single editor/tool choice to benefit from the methodology. Acceptance criteria (user-visible): (1) a user on any of the newly supported harnesses can invoke syspilot's agents and skills and get the same guidance and results as a VS Code Copilot Chat user does today; (2) installing or updating syspilot on a new harness happens through that harness's own install mechanism — a user is never asked to hand-edit personal or global configuration files; (3) the methodology content itself (what each agent does, what each skill teaches) stays a single, consistent source of truth — behavior must not drift between harnesses; (4) existing VS Code Copilot Chat users see no regression in current behavior or installation flow.

---

## Level 0: User Stories

**Status**: ✅ completed

### Impacted User Stories

| ID | Title | Impact | Notes |
|----|-------|--------|-------|
| SYSP_US_AGENT_ARCH | Clean Agent Architecture | modified | Added AC-8: Soul/Duties/Workflow content identical across harnesses, only structural/frontmatter adapter differs |
| SYSP_US_SKILL_ARCH | Skill Architecture | modified | Added AC-10: Skill Frontmatter/Instructions/Rules identical across harnesses, only discovery adapter differs |
| SYSP_US_SKILL_ORCHESTRATION | Consistent Agent Orchestration | modified | Added AC-4: harnesses without native session-messaging fall back to the synchronous orchestration variant automatically |
| SYSP_US_SETUP | Setup Manager Agent | modified | Added AC-5: Setup exposes itself via each harness's own native entry-point mechanism, no hand-edited config |
| SYSP_US_INSTALLER | Installer Agent | modified | Added AC-12/13: Installer targets each harness's native directories/format; per-harness gaps are documented, not silently dropped, and don't block other harnesses |

### New User Stories

| ID | Title | Priority |
|----|-------|----------|
| SYSP_US_HARNESS_PORTABILITY | As a syspilot user on a non-VS Code harness, I want the same agent/skill behavior as VS Code Copilot Chat, so that my harness choice doesn't lock me out of the methodology | mandatory |
| SYSP_US_HARNESS_INSTALL | As a syspilot user on any supported harness, I want to install/update syspilot through that harness's own native mechanism, so that I never hand-edit personal/global config | mandatory |

### Decisions

- Decision 1 (PM, 2-US split): Kept behavioral-equivalence and native-install as two separate User Stories (`SYSP_US_HARNESS_PORTABILITY`, `SYSP_US_HARNESS_INSTALL`) rather than one combined story, since they have distinct acceptance criteria and different downstream design owners (agent/skill content vs. Setup/Installer).
- Decision 2 (PM, modified-US list): `SYSP_US_AGENT_ARCH`, `SYSP_US_SKILL_ARCH`, `SYSP_US_SKILL_ORCHESTRATION`, `SYSP_US_SETUP`, `SYSP_US_INSTALLER` are modified in place with additive ACs; no other existing US required a change at Level 0.
- Decision 3 (PM, Qoder open question): Each target harness's actual current extension/plugin mechanism (Claude Code, OpenCode, Qoder) is researched at Level 2 design time, not assumed from prior knowledge — including re-verifying Claude Code and OpenCode against their own current docs. If a harness (e.g. Qoder) cannot cleanly meet AC-2 of `SYSP_US_HARNESS_INSTALL` (no hand-edited personal/global config), that is captured as a documented, honestly-disclosed limitation (`SYSP_US_HARNESS_PORTABILITY` AC-4) rather than blocking the CR. Partial success across harnesses is an acceptable outcome.

### Horizontal Check (MECE)

- [x] No contradictions with existing User Stories — the two new stories are additive; the five modified stories gained additive ACs only, none of their existing ACs were altered or removed
- [x] No redundancies — behavioral equivalence (content) and native install (mechanism) are cleanly separated; no overlap with existing `SYSP_US_DOC_EXTERNAL`/`SYSP_US_DOC_INTERNAL` (those cover documentation content, not harness portability)
- [x] Gaps identified and addressed — Level 0 does not yet decide *which* per-harness mechanisms are used; that is explicitly deferred to Level 2 research, as instructed by PM

---

## Level 1: Requirements

**Status**: ✅ corrected and user-approved at `ef99a83`

### Impacted Requirements

Found via links from User Stories above. Rather than duplicating a mirrored
AC across every REQ that links to a modified US, one semantically-fitting
existing REQ per family received the new AC(s) — mirroring the Level 0
pattern of one additive AC per story.

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| SYSP_REQ_AGENT_ARCH_FRONTMATTER | SYSP_US_AGENT_ARCH | modified | Added AC-11: only frontmatter/structural adapter differs per harness; Soul/Duties/Workflow content unchanged. Added link to SYSP_US_HARNESS_PORTABILITY |
| SYSP_REQ_SKILL_ARCH_FRONTMATTER | SYSP_US_SKILL_ARCH | modified | Added AC-5: only discovery adapter differs per harness; Instructions/Rules content unchanged. Added link to SYSP_US_HARNESS_PORTABILITY |
| SYSP_REQ_SETUP_BOOTLOADER_DUTIES | SYSP_US_SETUP | modified | Added AC-5: harness-native entry point, never hand-edited config. Added link to SYSP_US_HARNESS_INSTALL |
| SYSP_REQ_INSTALLER_SCOPE | SYSP_US_INSTALLER | modified | Added AC-8 (native target dirs/format per harness), AC-9 (harness gaps documented, don't block others). Added link to SYSP_US_HARNESS_INSTALL |
| SYSP_REQ_SKILL_ORCHESTRATION_GROUP | SYSP_US_SKILL_ORCHESTRATION | modified | Added AC-6: harnesses without native session-messaging get the synchronous variant automatically. Added link to SYSP_US_HARNESS_PORTABILITY |

### New Requirements

| ID | Title | Links | Priority |
|----|-------|-------|----------|
| SYSP_REQ_HARNESS_BEHAVIORAL_EQUIVALENCE | Harness Behavioral Equivalence | SYSP_US_HARNESS_PORTABILITY | mandatory |
| SYSP_REQ_HARNESS_CONTENT_SINGLE_SOURCE | Harness Content Single-Source | SYSP_US_HARNESS_PORTABILITY, SYSP_REQ_AGENT_ARCH_FRONTMATTER, SYSP_REQ_SKILL_ARCH_FRONTMATTER | mandatory |
| SYSP_REQ_HARNESS_LIMITATION_DISCLOSURE | Harness Limitation Disclosure | SYSP_US_HARNESS_PORTABILITY | mandatory |
| SYSP_REQ_HARNESS_PORTABILITY_NO_REGRESSION | Harness Portability No Regression | SYSP_US_HARNESS_PORTABILITY | mandatory |
| SYSP_REQ_HARNESS_NATIVE_INSTALL | Harness-Native Install Mechanism | SYSP_US_HARNESS_INSTALL, SYSP_REQ_INSTALLER_SCOPE | mandatory |
| SYSP_REQ_HARNESS_NATIVE_UPDATE | Harness-Native Update Flow | SYSP_US_HARNESS_INSTALL, SYSP_REQ_SETUP_BOOTLOADER_DUTIES | mandatory |
| SYSP_REQ_HARNESS_ONE_TIME_ENABLEMENT | Harness One-Time Enablement Exception | SYSP_US_HARNESS_INSTALL | mandatory |
| SYSP_REQ_HARNESS_INSTALL_NO_REGRESSION | Harness Install No Regression | SYSP_US_HARNESS_INSTALL | mandatory |

### Conflicts Detected

None.

### Decisions

- Decision 1 (CM, REQ mirroring strategy): New US ACs were mirrored into exactly
  one existing, semantically-fitting REQ per affected family
  (`SYSP_REQ_AGENT_ARCH_FRONTMATTER`, `SYSP_REQ_SKILL_ARCH_FRONTMATTER`,
  `SYSP_REQ_SETUP_BOOTLOADER_DUTIES`, `SYSP_REQ_INSTALLER_SCOPE` (two ACs),
  `SYSP_REQ_SKILL_ORCHESTRATION_GROUP`) rather than duplicating the same AC
  across every REQ linked from the modified US — avoids MECE redundancy while
  preserving traceability.
- Decision 2 (CM, new REQ split): Two new US-level ACs (behavioral equivalence
  for agents and for skills) were combined into a single REQ
  (`SYSP_REQ_HARNESS_BEHAVIORAL_EQUIVALENCE`) since they express the same
  underlying constraint for two artefact kinds; the remaining ACs each became
  their own REQ, one per distinct concern.

### Horizontal Check (MECE)

- [x] No contradictions with existing Requirements — all changes are additive ACs or net-new REQs
- [x] No redundancies — each mirrored AC was placed on exactly one REQ per family; no AC duplicated across REQs
- [x] All new REQs link to User Stories — all 8 new REQs link to `SYSP_US_HARNESS_PORTABILITY` or `SYSP_US_HARNESS_INSTALL`

### OpenCode Acceptance Correction Round

**Status:** corrections complete in draft; Level 2 is not reopened pending
explicit user approval.

Real OpenCode acceptance testing of a clean install with an explicit upstream
branch exposed contradictions in the completed requirements. The existing
requirement families cover the corrected intent; no new requirement ID was
needed.

#### Modified Requirements

| ID | Intent-level correction |
|----|-------------------------|
| SYSP_REQ_HARNESS_NATIVE_INSTALL | A clean install must place Setup, Installer, all Managers and Engineers, Skills, and Commands in valid native locations so the initiating harness can discover and invoke them |
| SYSP_REQ_HARNESS_NATIVE_UPDATE | One selected branch governs the bootstrap manifest, manifest files, and Installer fetches; default remains `main` |
| SYSP_REQ_HARNESS_ONE_TIME_ENABLEMENT | One-time enablement must leave Setup discoverable and able to place and invoke Installer through native configuration |
| SYSP_REQ_HARNESS_CONTENT_SINGLE_SOURCE | The selected branch's product `syspilot/` tree is the sole source and inventory; adapted methodology bodies preserve exact EOF bytes, including final-newline state |
| SYSP_REQ_INSTALLER_DUTIES | A final commit or success report requires successful Sphinx validation; direct operations delegate to their owning requirement |
| SYSP_REQ_INSTALLER_WORKFLOW | Branch handoff is honored throughout Installer fetches; failed dependency or validation gates prohibit final commit and success reporting |
| SYSP_REQ_INSTALLER_GITHUB_SOURCE | Installer propagates Setup's branch selection and never enumerates an installed harness instance as source |
| SYSP_REQ_INSTALLER_DIRECT_OPS | Deterministic version-controlled product implementation is allowed; generated wrappers, temporary helpers, and intermediary target artifacts remain prohibited |
| SYSP_REQ_INSTALLER_ROLLBACK | Transaction coverage includes every mutable target path; failed dependency or validation gates preserve or restore exact pre-install state and prohibit final success |
| SYSP_REQ_INSTALLER_DOC_BOOTSTRAP | Fresh projects receive both `docs/index.rst` and a minimal `docs/conf.py` enabling `sphinx_needs`, without overwriting existing files |
| SYSP_REQ_SETUP_BOOTLOADER_DUTIES | Setup guarantees native Setup/Installer discovery and end-to-end branch propagation |
| SYSP_REQ_SETUP_BOOTLOADER_FETCH | The selected branch applies to manifest and file fetches; Installer is placed in the initiating harness's native discoverable location |
| SYSP_REQ_SETUP_BOOTLOADER_INVOKE | Setup passes the selected branch and invokes the discovered Installer through the initiating harness's native subagent mechanism |

All modified requirements remain `draft` until this user-guided Level 1 gate
is approved.

#### Decisions

- Deterministic implementation committed under upstream product `syspilot/`
  is product logic, not a generated helper. The prohibition applies to
  run-generated wrappers, temporary helpers, and intermediary target files.
- Branch selection is one end-to-end value. An explicit override propagates
  through Setup manifest/file acquisition and Installer acquisition;
  absence of an override means `main` everywhere.
- Documentation bootstrap owns the minimum validation-ready source and
  configuration pair, not only `index.rst`.
- Dependency and validation gates are success preconditions. A failed gate
  cannot produce a final commit or success report and cannot leave target
  mutations behind.
- Product-source enumeration and exact methodology-body preservation are
  separate acceptance concerns within the existing single-source requirement.
- Existing Level 2 consumers are impact only in this round. They are not
  modified before user approval.

#### MECE and Trace Check

- [x] Collectively exhaustive — all five acceptance contradictions map to
  existing requirement owners; no new requirement or uncovered intent remains.
- [x] Mutually exclusive — native-install ACs separate configuration policy
  from installed capability completeness, and Installer Duties references the
  Direct Operations owner instead of restating its artifact rules.
- [x] No contradictions remain within the modified Level 1 families.
- [x] Direct trace queries against refreshed `needs.json` resolve all 13
  modified requirements to a parent User Story and at least one existing
  Design consumer; no modified requirement is orphaned and no link is broken.
- [x] Downstream semantic impact is recorded for Level 2 follow-up after
  approval; no Level 2 file was modified in this round.
- [x] `uv run python docs/test_docs_build.py` passes all 4 tests.

---

## Level 2: Design

**Status**: ⏳ corrections complete — awaiting user-guided approval

### Research Basis

Each target harness's actual current extension/plugin/skill mechanism was
researched directly from that harness's own current documentation (fetched
2026-09-16), per PM Decision 3 — no claim from prior knowledge or from
`superpowers` was assumed to still hold:

| Harness | Docs consulted |
|---------|-----------------|
| Claude Code | `code.claude.com/docs/en/sub-agents`, `/skills`, `/plugins` |
| OpenCode | `opencode.ai/docs/agents`, `/skills`, `/commands`, `/plugins`, `/config` |
| Qoder | `docs.qoder.com/extensions/subagent`, `/extensions/skills`, `/user-guide/rules` |

**Headline finding:** all three harnesses accept a plain agent/skill file
dropped into a documented directory (`.claude/agents/`, `.opencode/agents/`,
`.qoder/agents/`, and the matching `skills/` directories) as a fully native
mechanism — none requires hand-editing an existing personal or global
configuration file. The CR's open question about Qoder ("can it meet
'no hand-edited config'?") resolves favorably: Qoder's Custom Agents and
Skills are file-drop, same as the other two. No blocking limitation was
found for any harness on the install-mechanism question itself.

### Impacted Design Elements

Found via links from Requirements above.

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| SYSP_SPEC_INSTALLER_SCOPE | SYSP_REQ_INSTALLER_SCOPE | modified | Scope note extended: additional harnesses copied alongside VS Code target, per SYSP_SPEC_INSTALLER_HARNESS_TARGETS |
| SYSP_SPEC_INSTALLER_WORKFLOW | SYSP_REQ_INSTALLER_WORKFLOW | modified | Step 4 (Install/Update) extended to also write detected harnesses' native directories |

### New Design Elements

| ID | Title | Links |
|----|-------|-------|
| SYSP_SPEC_HARNESS_TARGET_MATRIX | Harness Target Matrix | SYSP_REQ_HARNESS_CONTENT_SINGLE_SOURCE, SYSP_REQ_HARNESS_NATIVE_INSTALL |
| SYSP_SPEC_HARNESS_AGENT_ADAPTER | Harness Agent Frontmatter Adapter | SYSP_REQ_HARNESS_CONTENT_SINGLE_SOURCE, SYSP_REQ_HARNESS_BEHAVIORAL_EQUIVALENCE, SYSP_SPEC_AGENT_ARCH_FRONTMATTER, SYSP_SPEC_HARNESS_TARGET_MATRIX |
| SYSP_SPEC_HARNESS_SKILL_ADAPTER | Harness Skill Frontmatter Adapter | SYSP_REQ_HARNESS_CONTENT_SINGLE_SOURCE, SYSP_REQ_HARNESS_BEHAVIORAL_EQUIVALENCE, SYSP_SPEC_SKILL_ARCH_FRONTMATTER, SYSP_SPEC_HARNESS_TARGET_MATRIX |
| SYSP_SPEC_HARNESS_PROMPT_ADAPTER | Harness Prompt/Command Adapter | SYSP_REQ_HARNESS_CONTENT_SINGLE_SOURCE, SYSP_SPEC_AGENT_ARCH_PROMPT, SYSP_SPEC_HARNESS_TARGET_MATRIX |
| SYSP_SPEC_HARNESS_ORCHESTRATION_ADAPTER | Harness Orchestration Fallback | SYSP_REQ_SKILL_ORCHESTRATION_GROUP, SYSP_SPEC_INSTALLER_ORCHESTRATION_SELECT, SYSP_SPEC_HARNESS_TARGET_MATRIX |
| SYSP_SPEC_HARNESS_ONE_TIME_ENABLEMENT | Harness One-Time Enablement | SYSP_REQ_HARNESS_ONE_TIME_ENABLEMENT, SYSP_REQ_HARNESS_NATIVE_UPDATE, SYSP_SPEC_SETUP_DUTIES, SYSP_SPEC_SETUP_WORKFLOW |
| SYSP_SPEC_HARNESS_LIMITATIONS | Harness Disclosed Limitations | SYSP_REQ_HARNESS_LIMITATION_DISCLOSURE, SYSP_SPEC_HARNESS_AGENT_ADAPTER, SYSP_SPEC_HARNESS_SKILL_ADAPTER, SYSP_SPEC_HARNESS_ORCHESTRATION_ADAPTER |
| SYSP_SPEC_INSTALLER_HARNESS_TARGETS | Installer Harness Targets | SYSP_REQ_HARNESS_NATIVE_INSTALL, SYSP_REQ_HARNESS_INSTALL_NO_REGRESSION, SYSP_REQ_HARNESS_PORTABILITY_NO_REGRESSION, SYSP_SPEC_HARNESS_TARGET_MATRIX, SYSP_SPEC_HARNESS_AGENT_ADAPTER, SYSP_SPEC_HARNESS_SKILL_ADAPTER, SYSP_SPEC_INSTALLER_SCOPE, SYSP_SPEC_INSTALLER_WORKFLOW |

New file: `docs/syspilot/design/spec_harness_adapters.rst` (added to
`docs/syspilot/design/index.rst` toctree). Two existing specs in
`spec_installer.rst` gained additive notes only (see table above).

### Conflicts Detected

None.

### Decisions

- Decision 1 (Designer, disclosed limitations found): four non-blocking
  limitations were identified and disclosed per SYSP_REQ_HARNESS_LIMITATION_DISCLOSURE
  rather than forcing a design that doesn't hold up: (a) Claude Code has no
  `user-invocable: false` equivalent for subagents — the Installer/Bootloader
  can always be `@`-mentioned directly, mitigated only by naming convention;
  (b) Claude Code has no per-subagent SEND allowlist frontmatter field — a
  Manager's `agents:` list becomes Workflow prose instead of an enforced
  allowlist; (c) OpenCode's Skill frontmatter accepts only six fields
  (`name`, `description`, `license`, `compatibility`, `metadata`, plus
  documented but unused others) — `group`/`tools`/`triggers` are silently
  ignored, non-blocking since mutual exclusion is already Installer-side;
  (d) Qoder's subagent-to-subagent nesting depth is undocumented — treated
  as a flat, single-hop Manager→Engineer pattern until independently
  verified. None of the four block support on any other harness.
- Decision 2 (Designer, orchestration fallback): none of the three new
  harnesses expose a Jarvis-equivalent persistent cross-session actor
  registry (Claude Code's own cross-session messaging is a different,
  incompatible protocol). All three default to the synchronous orchestration
  variant (`syspilot.orchestration-subagent`) per SYSP_REQ_SKILL_ORCHESTRATION_GROUP
  AC-6, mapped onto each harness's own native subagent-spawning primitive
  (Claude Code's `Agent` tool, OpenCode's Task tool + `permission.task`,
  Qoder's undocumented "subagent approach").
- Decision 3 (Designer, prompt file adapter): Claude Code and Qoder have no
  separate prompt/command file concept — the agent/skill file itself is the
  invocation surface, so SYSP_SPEC_HARNESS_PROMPT_ADAPTER designates no file
  generation for those two harnesses rather than forcing an artificial
  prompt file to exist.
- Decision 4 (Designer, one-time enablement): every harness (including VS
  Code, unchanged) has the same first-bootstrap-file problem; the solution
  is the same shape everywhere — one documented, harness-standard copy/paste
  of the Setup Bootloader file (or, for Claude Code, an optional Plugin
  marketplace install) — never a hand-edited config file, satisfying
  SYSP_REQ_HARNESS_ONE_TIME_ENABLEMENT uniformly.

### Horizontal Check (MECE)

- [x] No contradictions with existing Designs — the two modified specs
  (`SYSP_SPEC_INSTALLER_SCOPE`, `SYSP_SPEC_INSTALLER_WORKFLOW`) gained
  additive notes pointing at the new harness-targeting spec; no existing
  VS Code behavior, table row, or step was altered or removed
- [x] No redundancies — each harness concern (target directories, agent
  frontmatter, skill frontmatter, prompt/command, orchestration fallback,
  bootstrap, disclosed limitations) has exactly one owning spec; the
  Installer-side targeting spec only orchestrates calls into those, it does
  not restate their content
- [x] All new SPECs link to Requirements — verified via
  `syspilot.impact-python` (`--direction in`) against every new/mirrored
  Level 1 REQ; see Level 2 Link Verification appendix below
- [x] Build clean — `sphinx-build` passes with 0 errors/warnings after the
  Level 2 edits

### OpenCode Acceptance Correction Round

**Status:** Design corrections complete in draft; STOP before implementation
pending explicit user approval.

The real OpenCode acceptance repository `../test-syspilot`, especially commit
`8d2e3e7`, is behavioral evidence for native parsing, discovery, command
naming, and fresh-doc configuration. Generated acceptance artifacts are not
treated as product source or copied into this design.

#### Impacted Design Elements

| ID | Impact |
|----|--------|
| SYSP_SPEC_SETUP_DUTIES | Added native Installer handoff and single-branch fidelity duties |
| SYSP_SPEC_SETUP_WORKFLOW | Added selected-branch manifest flow, pre-mutation dependency/checkpoint gate, stable runtime placement, per-harness native Installer destinations, and rollback handoff |
| SYSP_SPEC_INSTALLER_SOUL | Replaced raw-command and partial rollback guardrails with shipped-engine and complete transaction boundaries |
| SYSP_SPEC_INSTALLER_DUTIES | Reconciled direct operations with shipped deterministic product logic and strict success gates |
| SYSP_SPEC_INSTALLER_SCOPE | Restricted enumeration to selected-revision product roots and excluded upstream installed `.github` |
| SYSP_SPEC_INSTALLER_DOC_BOOTSTRAP | Added non-overwriting minimal `docs/conf.py` with `sphinx_needs` beside `docs/index.rst` |
| SYSP_SPEC_INSTALLER_WORKFLOW | Defined immutable branch input, transaction order, engine invocation, exact body bytes, validation-before-commit/report, and rollback behavior |
| SYSP_SPEC_INSTALLER_GITHUB_SOURCE | Pinned manifest, inventory, and content acquisition to one selected branch/revision and product roots only |
| SYSP_SPEC_INSTALLER_DIRECT_OPS | Allowed the version-controlled engine while prohibiting generated wrappers, helpers, temporary files, and intermediary targets |
| SYSP_SPEC_INSTALLER_ROLLBACK | Expanded the checkpoint across Setup and Installer paths and added dependency/mutation/validation failure gates |
| SYSP_SPEC_INSTALLER_HARNESS_TARGETS | Retains native target orchestration under the deterministic adapter engine |
| SYSP_SPEC_HARNESS_AGENT_ADAPTER | Defined exact body/EOF preservation and parser-valid OpenCode mode/permission mapping |
| SYSP_SPEC_HARNESS_PROMPT_ADAPTER | Defined all-prompt OpenCode command generation, dot-preserving names, description fallback, agent routing, and empty body |
| SYSP_SPEC_HARNESS_ONE_TIME_ENABLEMENT | Defined native Setup configuration and selected-branch bootstrap handoff, including OpenCode Setup-to-Installer permission |
| SYSP_SPEC_UAT_INSTALLER_HARNESS_TARGETS | Replaced prose-fragment evidence with executable fixture expectations for adapter and transaction behavior |
| SYSP_SPEC_UAT_HARNESS_AGENT_ADAPTER | Added exact OpenCode map assertions and native `debug config` validation |
| SYSP_SPEC_UAT_HARNESS_PROMPT_ADAPTER | Added exhaustive prompt conversion, fallback, filename, and empty-body assertions |
| SYSP_SPEC_UAT_HARNESS_ONE_TIME_ENABLEMENT | Added isolated OpenCode discovery, explicit-branch propagation, and Setup-to-Installer delegation UAT |

#### New Design Element

| ID | Title | Ownership |
|----|-------|-----------|
| SYSP_SPEC_INSTALLER_ADAPTER_ENGINE | Installer Deterministic Adapter Engine | Version-controlled `syspilot/installer.py`, fetched by bootstrap to stable runtime `.syspilot/installer.py` |

#### Decisions

1. **Deterministic implementation ownership:** `syspilot/installer.py` owns
  source enumeration, structured YAML parsing, harness transformation,
  UTF-8-no-BOM writes, exact methodology-body bytes, orphan cleanup, and
  structured summaries. The installed runtime is a final shipped product
  artifact; run-generated wrappers/helpers/intermediates remain prohibited.
2. **Source acquisition:** one branch resolves to one upstream revision.
  Inventory is only `syspilot/{agents,prompts,skills,templates}`; upstream
  `.github` and target installed directories are never source. The branch
  override governs manifest, bootstrap files, inventory, and content fetches.
3. **Bootstrap:** Setup checks dependencies and creates the complete checkpoint
  before mutation, fetches the engine and logical Installer source, writes the
  engine to `.syspilot/installer.py`, adapts Installer directly into the
  initiating harness's native agent directory, then invokes that discovered
  native agent. VS Code retains `.github/agents/*.agent.md` behavior.
4. **OpenCode agents:** a nonempty source `agents` allowlist emits
  `mode: primary` and a `permission.task` map containing `"*": deny` plus one
  `<allowed-agent>: allow` entry per target. Empty emits `mode: subagent` with
  no task map. Setup is primary and allows `syspilot.installer`.
5. **OpenCode commands:** every product prompt is adapted. Removing only the
  terminal `.prompt.md` suffix preserves dots; frontmatter contains source
  description or agent-description fallback and source `agent`; body is empty.
6. **Fresh documentation:** missing `docs/index.rst` and `docs/conf.py` are
  created independently and never overwrite existing files. Minimal `conf.py`
  enables `sphinx_needs`.
7. **Transaction order:** dependency gate precedes mutation; the checkpoint
  covers every Setup/Installer target; any later failure restores exact
  pre-state; only successful Sphinx validation permits final commit and
  success reporting.
8. **Exact bytes:** methodology body is all bytes after the closing YAML
  delimiter line and its line ending. Those bytes, including terminal-newline
  presence or absence, are appended unchanged to adapted frontmatter.
9. **Testing:** fixture tests execute the shipped engine against fake upstream
  revisions and isolated Git repositories, including failure injection at
  every gate. OpenCode UAT uses `opencode debug config` and native Setup
  delegation in an isolated project when available. Installer-prose fragment
  matching is not acceptance evidence.

#### Implementation Ownership and Data Flow

`Setup request -> selected branch -> bootstrap manifest -> dependency gate ->
complete checkpoint -> shipped adapter runtime + native Installer placement ->
native delegation -> selected-revision product inventory/bytes -> structured
frontmatter adaptation + unchanged body bytes -> final target writes/orphan
cleanup/docs bootstrap -> Sphinx validation -> final commit -> summary/report`.

The engine's public CLI/API receives repository, branch, target root,
initiating harness, orchestration choice, and checkpoint identifier. Its
deterministic functions are directly callable from fixtures without an LLM or
harness.

#### MECE and Trace Check

- [x] Post-edit MECE advisory complete. It identified corrected-spec status
  discipline and stale Installer Soul/Harness Targets wording; both were
  repaired. No remaining correction-round overlap, gap, or acceptance-evidence
  contradiction was found.
- [x] Post-edit trace queries resolve every corrected Design link in source.
  Ten corrected requirements resolve normally in refreshed `needs.json`; the
  three Installer source/direct-ops/rollback requirements cannot materialize
  because approved Level 1 commit `ef99a83` indents their `:status:` options
  incorrectly. Their Design `:links:` are present and syntactically correct.
- [x] `uv run python docs/test_docs_build.py` passes all 4 tests.
- [ ] Full `uv run python docs/docs-build.py clean` is blocked by approved
  Level 1 indentation defects: two docutils errors and three malformed
  requirement option blocks, plus the two pre-existing `ontology-architecture`
  cross-reference warnings. All correction-round Level 2 RST parse warnings
  were eliminated.
- [x] No production implementation file is modified in this correction round.

---

## UAT Design

**Status**: ✅ completed

UAT chains were added for the seven harness-adapter design elements that were
not covered by the earlier `SYSP_SPEC_INSTALLER_HARNESS_TARGETS` chain. Each
chain contains one test story, one test-data requirement, and one expected-
outcomes specification.

| Design Element | UAT Story | Test Data | Expected Outcomes | Scenarios |
|----------------|-----------|-----------|-------------------|-----------|
| SYSP_SPEC_HARNESS_TARGET_MATRIX | SYSP_US_UAT_HARNESS_TARGET_MATRIX | SYSP_REQ_UAT_HARNESS_TARGET_MATRIX | SYSP_SPEC_UAT_HARNESS_TARGET_MATRIX | 4 |
| SYSP_SPEC_HARNESS_AGENT_ADAPTER | SYSP_US_UAT_HARNESS_AGENT_ADAPTER | SYSP_REQ_UAT_HARNESS_AGENT_ADAPTER | SYSP_SPEC_UAT_HARNESS_AGENT_ADAPTER | 5 |
| SYSP_SPEC_HARNESS_SKILL_ADAPTER | SYSP_US_UAT_HARNESS_SKILL_ADAPTER | SYSP_REQ_UAT_HARNESS_SKILL_ADAPTER | SYSP_SPEC_UAT_HARNESS_SKILL_ADAPTER | 4 |
| SYSP_SPEC_HARNESS_PROMPT_ADAPTER | SYSP_US_UAT_HARNESS_PROMPT_ADAPTER | SYSP_REQ_UAT_HARNESS_PROMPT_ADAPTER | SYSP_SPEC_UAT_HARNESS_PROMPT_ADAPTER | 4 |
| SYSP_SPEC_HARNESS_ORCHESTRATION_ADAPTER | SYSP_US_UAT_HARNESS_ORCHESTRATION_ADAPTER | SYSP_REQ_UAT_HARNESS_ORCHESTRATION_ADAPTER | SYSP_SPEC_UAT_HARNESS_ORCHESTRATION_ADAPTER | 4 |
| SYSP_SPEC_HARNESS_ONE_TIME_ENABLEMENT | SYSP_US_UAT_HARNESS_ONE_TIME_ENABLEMENT | SYSP_REQ_UAT_HARNESS_ONE_TIME_ENABLEMENT | SYSP_SPEC_UAT_HARNESS_ONE_TIME_ENABLEMENT | 4 |
| SYSP_SPEC_HARNESS_LIMITATIONS | SYSP_US_UAT_HARNESS_LIMITATIONS | SYSP_REQ_UAT_HARNESS_LIMITATIONS | SYSP_SPEC_UAT_HARNESS_LIMITATIONS | 5 |

**Total:** 7 UAT chains, 21 traceable UAT elements, 30 scenarios.

### Testability Concerns

- Runtime discovery and invocation require installed copies of Claude Code,
  OpenCode, and Qoder; static path/frontmatter inspection cannot substitute
  for those runtime checks.
- Model-selected automatic Skill invocation is stochastic. UAT verifies
  preserved descriptions and deterministic manual invocation; automatic
  selection is exploratory only.
- Qoder subagent nesting depth remains undocumented. UAT can meaningfully
  assert only the designed flat Manager-to-Engineer hop, not deeper nesting.
- Claude Code's optional Plugin path is conditional on a published syspilot
  marketplace package. Until one exists, only the mandatory copied-bootstrap
  path is executable. Negative vendor-capability checks must record harness
  version and date because later releases may add support.

### Validation

- [x] All 21 UAT files are included in their level-specific toctrees.
- [x] Every test-data requirement links to its UAT story and every expected-
  outcomes specification links to its test-data requirement.
- [x] `uv run python docs/test_docs_build.py` passes after all seven chains
  were added.

---

## Implementation

**Status**: ✅ implemented after corrected Level 2 approval at `c9923da`

The shipped deterministic engine now owns source acquisition, structured
adaptation, native writes, documentation bootstrap, orphan cleanup, summaries,
transaction rollback, Sphinx validation, and validation-gated commit/reporting.
Setup ships the engine to `.syspilot/installer.py`, adapts Installer into the
initiating harness's native discovery path, and propagates one selected branch
through manifest, bootstrap, and Installer source operations.

| Design Element | Implementation Evidence |
|----------------|-------------------------|
| SYSP_SPEC_INSTALLER_ADAPTER_ENGINE | `syspilot/installer.py` public API and CLI; immutable branch/revision source snapshot, exact-byte adapters, atomic writes, summaries, persisted pre-bootstrap checkpoint handoff, rollback, validation and commit gates |
| SYSP_SPEC_HARNESS_TARGET_MATRIX | Exact VS Code, Claude Code, OpenCode, and Qoder project-scope path matrix; absent harnesses produce no output |
| SYSP_SPEC_HARNESS_AGENT_ADAPTER | Structured YAML/body split; Claude `Agent`, OpenCode `mode` and `permission.task`, and Qoder description-only mappings; unsupported identity/invocation/model fields omitted |
| SYSP_SPEC_HARNESS_SKILL_ADAPTER | Skill directory names and supported metadata retained; Instructions/Rules bodies copied byte-for-byte |
| SYSP_SPEC_HARNESS_PROMPT_ADAPTER | VS Code prompts remain verbatim, OpenCode commands are thin routing files, Claude Code and Qoder generate no prompt/command artifacts |
| SYSP_SPEC_HARNESS_ORCHESTRATION_ADAPTER | `.jarvis/` remains authoritative; exactly one selected orchestration Skill is propagated under mutual exclusion to every detected harness; synchronous native one-hop mappings are stated |
| SYSP_SPEC_HARNESS_ONE_TIME_ENABLEMENT | Bootstrap manifest ships runtime plus logical Installer source; Setup places native Installer before delegation and preserves explicit branch/checkpoint inputs |
| SYSP_SPEC_HARNESS_LIMITATIONS | Detected-harness-only, non-blocking disclosure table covers both Claude Code gaps, OpenCode ignored Skill metadata, and both Qoder boundaries |

### Changed Files

- `syspilot/installer.py` — shipped deterministic engine and CLI.
- `syspilot/bootstrap.json` — engine and logical Installer bootstrap entries.
- `syspilot/agents/syspilot.setup.agent.md` — branch-faithful native handoff.
- `syspilot/agents/syspilot.installer.agent.md` — shipped-engine invocation,
  complete transaction, validation, and reporting gates.
- `tests/test_installer.py` — fixture-driven
  executable transformation, source, transaction, and runtime tests.
- `docs/requirements.txt` — explicit PyYAML runtime dependency.
- `docs/changes/v0.9.1/harness-interop.md` — implementation and acceptance evidence.

### TDD Evidence

- RED 1: executable OpenCode adapter test failed with
  `ModuleNotFoundError: No module named 'syspilot.installer'`.
- RED 2: expanded fixture suite failed importing missing public engine API
  (`DependencyError`).
- RED 3: bootstrap contract failed because the manifest contained only the
  VS Code Installer entry and no shipped runtime/native destination.
- RED 4: commit rollback test failed because no commit-injection surface or
  Git-index checkpoint existed.
- RED 5: fresh validation test found persistent `docs/_build` output in the
  target; validation was moved to external temporary output/doctree paths.
- RED 6: bootstrap-to-delegated-failure continuity test found
  `.syspilot/installer.py` and the native OpenCode Installer remained after
  rollback because `install_snapshot` discarded Setup's checkpoint identifier.
- GREEN: the replacement suite passes 18 tests covering structured YAML,
  exact body/EOF bytes, no BOM, all harness mappings, 13/6/7 product output,
  source branch/revision selection, misleading `.github` exclusion, fresh and
  idempotent install, protected-orphan behavior, docs non-overwrite, native
  bootstrap, dependency-before-mutation, rollback at sync/docs/cleanup/
  validation/commit phases, pre-bootstrap delegated rollback continuity,
  Git-index restoration, checkpoint success cleanup, invalid/cross-target
  identifier rejection, VS Code no-regression, and OpenCode parser smoke, with
  no persistent validation or transaction artifacts.

### Checkpoint Handoff Correction

The complete Setup checkpoint is serialized as atomic JSON below the operating
system temporary directory in `syspilot-checkpoints/<uuid>.json`. The opaque
UUID is the only handoff value. File bytes and the Git index are Base64 encoded;
directory presence and the resolved owning target root are stored explicitly.
The delegated Installer validates UUID syntax, artifact structure, relative
snapshot paths, and exact target-root ownership before mutation. It loads the
handed-off checkpoint when present and creates a new checkpoint only for direct
invocation. Successful completion and successful rollback both delete the
artifact; it is outside the target Git tree and cannot be committed or collide
with customer files.

### Implementation Validation

- [x] `uv run python docs/test_docs_build.py` — 4 tests passed.
- [x] `uv run python -m unittest discover -s tests -v`
  — 18 tests passed.
- [x] Mandatory impact query from `SYSP_SPEC_INSTALLER_ADAPTER_ENGINE` resolves
  the content-single-source, native-install, Installer duties/workflow/source/
  direct-operations/encoding requirements and harness target consumer.
- [x] `uv run python docs/docs-build.py clean` completes source reading,
  schema validation (0 schema warnings), HTML generation, and needs export;
  it exits nonzero under `-W` only for the two known baseline
  `ontology-architecture` cross-reference warnings in `docs/methodology.md`
  and `docs/syspilot/methodology.md`. No changed file emits a warning.

### Isolated OpenCode Acceptance

- [x] Disposable sibling source and target repositories were created; no
  artifact from `../test-syspilot` was copied into product source.
- [x] Real CLI acquired explicit branch `feature/harness-interop`, excluded a
  misleading upstream `.github/agents/syspilot.fake.agent.md`, validated fresh
  docs, and created final target commit `bb1a32f` only after success.
- [x] OpenCode 1.17.4 `debug config` exited 0; Setup resolved as
  `mode: primary` with a map-shaped task permission allowing only Installer
  after the deny-all entry.
- [x] Native output contains 13 agents, 6 selected Skills, and all 7
  dot-preserving commands; recursive scan found zero UTF-8 BOM files.
- [x] Fresh `docs/index.rst` and `docs/conf.py` pass `sphinx -W` with the same
  dependency-gated interpreter used by Installer.
- [x] Native `syspilot.cm` invoked `syspilot.implement` through OpenCode's Task
  permission and received `DELEGATION_OK`; no files were modified.

### Historical / superseded: uv-Only Execution Policy Correction

> **Historical / superseded.** This section preserves the audit record for an
> intermediate design. Its bootstrap, checkpoint, and public orchestration
> command shapes are obsolete and intentionally not reproduced as executable
> commands. The current installation contract is the [README Installation
> section](../../../README.md#installation): production CLI targets are only
> ``vscode`` and ``opencode``; installation has no public ``--orchestration``
> option and no Setup-to-Installer agent delegation.

**Status:** L1/L2, UAT, implementation, and runtime re-verification complete.

#### Acceptance Evidence

A real native Setup invocation in the clean OpenCode acceptance repository
executed ``python --version`` and ``pip show ...``, reported Python dependencies
as unavailable even though ``uv`` was installed, and stopped. Direct execution
through ``uv run python syspilot/installer.py`` succeeded. The prior design
therefore constrained dependency names but not the process entry point.

#### Mandatory Impact Analysis

``syspilot.impact-python`` was executed through ``uv`` against refreshed needs
data for all requested anchors:

* ``SYSP_REQ_INSTALLER_WORKFLOW`` identified the Installer workflow, adapter
  engine, harness-target design, and existing Installer UAT consumers.
* ``SYSP_SPEC_SETUP_WORKFLOW`` identified Setup duties, native one-time
  enablement, and documentation/workflow consumers.
* ``SYSP_SPEC_INSTALLER_ADAPTER_ENGINE`` identified the harness adapter family,
  Installer workflow/source/direct-operation requirements, and harness targets.
* ``SYSP_SPEC_UAT_HARNESS_ONE_TIME_ENABLEMENT`` and
  ``SYSP_SPEC_UAT_INSTALLER_HARNESS_TARGETS`` resolved to their complete UAT
  story/requirement/spec chains.

No new product requirement or design ID is needed. Existing owners cover the
policy without overlap.

#### Corrected Requirement and Design IDs

| Level | IDs |
|-------|-----|
| L1 | ``SYSP_REQ_HARNESS_NATIVE_INSTALL``, ``SYSP_REQ_SETUP_BOOTLOADER_DUTIES``, ``SYSP_REQ_INSTALLER_DUTIES``, ``SYSP_REQ_INSTALLER_WORKFLOW``, ``SYSP_REQ_INSTALLER_DOC_BOOTSTRAP`` |
| L2 | ``SYSP_SPEC_SETUP_WORKFLOW``, ``SYSP_SPEC_INSTALLER_SOUL``, ``SYSP_SPEC_INSTALLER_DUTIES``, ``SYSP_SPEC_INSTALLER_ADAPTER_ENGINE``, ``SYSP_SPEC_INSTALLER_WORKFLOW`` |
| UAT | ``SYSP_US_UAT_INSTALLER_SPEC_REWRITE``, ``SYSP_REQ_UAT_INSTALLER_SPEC_REWRITE``, ``SYSP_SPEC_UAT_INSTALLER_SPEC_REWRITE``, ``SYSP_REQ_UAT_HARNESS_ONE_TIME_ENABLEMENT``, ``SYSP_SPEC_UAT_HARNESS_ONE_TIME_ENABLEMENT``, ``SYSP_REQ_UAT_INSTALLER_HARNESS_TARGETS``, ``SYSP_SPEC_UAT_INSTALLER_HARNESS_TARGETS`` |

The shipped Setup, Installer, Test Designer, and Verify Engineer instructions
are corrected because they execute or validate this feature workflow.

#### Exact Command Contract

Setup checks executable availability only with ``uv --version`` and
``git --version``. It does not probe Python, pip, or Sphinx executables.

At this intermediate revision, the version-controlled engine carried exact
release-series dependencies in PEP 723 inline metadata and exposed separate
bootstrap, install, and Sphinx-validation operations. Those obsolete command
signatures are omitted to prevent accidental use; the current executable
commands are maintained only in the README Installation section.

Installer-agent bytes are supplied to the bootstrap command on standard input.
The validation subprocess re-enters the same PEP 723 script through ``uv``;
``sys.executable -m sphinx`` and bare ``sphinx-build`` are prohibited. uv-managed
environments and dependency caches, plus Sphinx output and doctrees, remain
outside the target repository. No activated virtual environment or globally
installed Python package is an installation prerequisite.

#### Rollback and MECE Decisions

* Missing ``uv`` or Git stops before mutation. The complete checkpoint is
  created before the runtime or native Installer is written.
* PEP 723 resolution occurs only through ``uv`` after the checkpoint exists;
  resolution or validation failure restores exact pre-install state.
* ``SYSP_REQ_HARNESS_NATIVE_INSTALL`` owns the cross-cutting uv-only policy;
  Setup duties own the bootstrap gate; Installer workflow owns execution and
  validation order; the adapter-engine spec owns concrete commands and
  dependency metadata. UAT observes those contracts without redefining them.
* The old missing-sphinx-needs UAT is replaced by a missing-uv gate test because
  PEP 723 resolution deliberately removes ambient-package availability as an
  installation precondition.
* No dependency cache or virtual environment is created inside the target
  repository, and rollback-before-mutation semantics are unchanged.

#### Correction Validation

* [x] ``uv run python docs/test_docs_build.py`` — 4 tests passed after L1,
  after L2, and after UAT/agent-instruction edits.
* [x] Policy scan found no active bare install/uninstall command example in the
  corrected Setup/Installer/UAT surfaces; prohibited executable names remain
  only in negative assertions.
* [x] ``git diff --check`` reports no whitespace errors.
* [x] Post-edit impact queries resolve every corrected L1 owner to its parent
  User Story and intended L2 consumers, and resolve all three corrected UAT
  requirements to both their UAT story and expected-outcomes specification.
* [x] ``uv run python docs/docs-build.py clean`` completes source reading,
  schema validation with zero schema warnings, HTML generation, and needs
  export. Warning-as-error exit remains nonzero only for the two known baseline
  ``ontology-architecture`` cross-reference warnings in
  ``docs/methodology.md`` and ``docs/syspilot/methodology.md``; no corrected
  file emits a warning.

#### Implementation Evidence

* [x] RED: ``uv run python -m unittest
  tests.test_installer.TestUvOnlyRuntimeContract -v`` failed all four new
  contracts against ``9e77b31``: missing PEP 723 metadata, bare command
  guidance in three shipped Skill files, missing CLI subcommands, and the
  direct interpreter Sphinx path.
* [x] GREEN: the same focused command passes 4 tests. The executable fixture
  runs the installed runtime with ``uv run --no-project --python 3.11`` against
  a local Git source snapshot without ``VIRTUAL_ENV`` and leaves neither
  ``.venv`` nor ``docs/_build`` in the target.
* [x] ``syspilot/installer.py`` declares exact PEP 723 pins for PyYAML 6.0.3,
  Sphinx 8.2.3, and sphinx-needs 8.5.0 with Python ``>=3.11,<3.15``. The pins
  resolve successfully at the Python 3.11 compatibility floor.
* [x] The shipped CLI implements the exact bootstrap, install, and
  validate-sphinx subcommands. Parent validation launches
  ``uv run --no-project .syspilot/installer.py validate-sphinx`` and captures
  child output so stdout remains the structured JSON result channel.
* [x] Active shipped agent and Skill command guidance contains no bare Python,
  pip, or Sphinx command. The impact tool has no direct Sphinx fallback.
* [x] ``uv run python -m unittest discover -s tests -v`` passes all 22 tests,
  preserving the prior 18 and adding 4 uv-only regression tests.
* [x] ``uv run python docs/test_docs_build.py`` passes all 4 documentation
  tests. ``uv run python docs/docs-build.py clean`` completes with only the two
  accepted baseline ``ontology-architecture`` warnings.

### Direct CLI Stable Runtime Correction

**Status:** implemented after direct clean-install acceptance exposed a missing
bootstrap assumption.

The public ``install`` CLI now acquires ``syspilot/installer.py`` from the same
selected source revision as the product inventory and writes those exact bytes
to the final ``.syspilot/installer.py`` runtime through the existing target map.
The write therefore remains inside the pre-install checkpoint, atomic write,
rollback, summary, validation, and final commit boundaries. Bootstrap and
direct installation now converge on the same stable runtime without creating a
temporary or intermediary target artifact.

#### TDD and Validation Evidence

* [x] RED: the executable clean-target test invoked ``uv run --no-project
  syspilot/installer.py install`` without a checkpoint or preinstalled runtime.
  Validation failed when uv could not open ``.syspilot/installer.py`` from the
  target and the transaction rolled back.
* [x] GREEN: the same test succeeds, verifies the installed runtime byte-for-byte
  against ``git show`` from the selected revision, confirms the first summary
  and commit include ``.syspilot/installer.py``, and confirms a second install
  reports no runtime changes and creates no commit.
* [x] The clean target contains neither ``.venv`` nor ``docs/_build`` after both
  runs.
* [x] ``uv run --no-project -m unittest tests.test_installer -v`` passes all 22
  Installer tests.
* [x] Disposable direct clean/install-update acceptance passes for VS Code,
  OpenCode, and Claude: every clean run installs and commits the stable runtime;
  every update creates no commit and leaves a clean target with no local cache.
* [x] ``uv run --no-project docs/test_docs_build.py`` passes all 4 tests. The
  clean documentation build completes with zero schema warnings and remains
  warning-as-error nonzero only for the two accepted baseline
  ``ontology-architecture`` cross-reference warnings.

### Historical / superseded: Production-Stable Installation Design Correction

> **Historical / superseded.** This section records an intermediate conclusion
> and is not installation guidance. Its Claude production classification,
> public orchestration option, and Setup/Installer handoff were superseded by
> implementation and final acceptance. The current contract is the [README
> Installation section](../../../README.md#installation): production CLI
> targets are only ``vscode`` and ``opencode``; Claude Code and Qoder are
> experimental; there is no public ``--orchestration`` option, bootstrap
> subcommand, or nested Setup-to-Installer delegation.

**Status:** L0/L1/L2 and UAT corrected autonomously from acceptance evidence;
no user-approval pause requested by Change Manager.

#### Evidence and Decision

Direct remote PEP 723 execution resolves dependencies and runs the selected
branch's Installer. Clean and repeated deterministic installs are successful
and idempotent for VS Code GitHub Copilot, OpenCode, and Claude Code. OpenCode
native Manager-to-Engineer Task delegation works, but nested
Setup-to-Installer Task delegation stalled for more than 180 seconds and left
bootstrap/checkpoint mutations until external cancellation and restore.

The deterministic runtime is therefore the installation control plane. Setup
remains the primary installed user entry point but invokes the runtime directly;
the Installer agent may remain as an internal documentation/diagnostic surface.

#### Mandatory Impact Analysis

The refreshed needs database contains 9,151 needs. Inbound depth-1 traversal
from ``SYSP_US_HARNESS_INSTALL``, ``SYSP_US_SETUP``, and
``SYSP_US_INSTALLER`` identified the native-install/update, Setup bootloader,
Installer workflow/source/rollback, and UAT families. Inbound depth-1 traversal
from each corrected requirement identified the direct Design consumers.
Post-edit bidirectional depth-2 traversal confirmed the corrected Setup,
Installer engine/workflow/rollback/target, README, and UAT elements retain
parents and consumers. No new product ID was required.

#### Corrected IDs

| Level | IDs |
|-------|-----|
| L0 | ``SYSP_US_HARNESS_INSTALL``, ``SYSP_US_HARNESS_PORTABILITY``, ``SYSP_US_SETUP``, ``SYSP_US_INSTALLER`` |
| L1 | ``SYSP_REQ_HARNESS_NATIVE_INSTALL``, ``SYSP_REQ_HARNESS_NATIVE_UPDATE``, ``SYSP_REQ_HARNESS_ONE_TIME_ENABLEMENT``, ``SYSP_REQ_HARNESS_INSTALL_NO_REGRESSION``, ``SYSP_REQ_HARNESS_BEHAVIORAL_EQUIVALENCE``, ``SYSP_REQ_SETUP_SOUL``, ``SYSP_REQ_INSTALLER_WORKFLOW``, ``SYSP_REQ_INSTALLER_GITHUB_SOURCE``, ``SYSP_REQ_INSTALLER_ROLLBACK``, ``SYSP_REQ_INSTALLER_SCOPE``, ``SYSP_REQ_SETUP_BOOTLOADER_DUTIES``, ``SYSP_REQ_SETUP_BOOTLOADER_FETCH`` (deprecated), ``SYSP_REQ_SETUP_BOOTLOADER_INVOKE`` (deprecated), ``SYSP_REQ_SETUP_INSTALLER_NOT_USER_INVOCABLE``, ``SYSP_REQ_DOC_README`` |
| L2 | ``SYSP_SPEC_SETUP_SOUL``, ``SYSP_SPEC_SETUP_DUTIES``, ``SYSP_SPEC_SETUP_WORKFLOW``, ``SYSP_SPEC_SETUP_FRONTMATTER``, ``SYSP_SPEC_INSTALLER_SOUL``, ``SYSP_SPEC_INSTALLER_FRONTMATTER``, ``SYSP_SPEC_INSTALLER_SCOPE``, ``SYSP_SPEC_INSTALLER_ADAPTER_ENGINE``, ``SYSP_SPEC_INSTALLER_WORKFLOW``, ``SYSP_SPEC_INSTALLER_GITHUB_SOURCE``, ``SYSP_SPEC_INSTALLER_ROLLBACK``, ``SYSP_SPEC_INSTALLER_HARNESS_TARGETS``, ``SYSP_SPEC_HARNESS_TARGET_MATRIX``, ``SYSP_SPEC_HARNESS_ONE_TIME_ENABLEMENT``, ``SYSP_SPEC_HARNESS_LIMITATIONS``, ``SYSP_SPEC_DOC_README`` |
| UAT | ``SYSP_US_UAT_HARNESS_ONE_TIME_ENABLEMENT``, ``SYSP_REQ_UAT_HARNESS_ONE_TIME_ENABLEMENT``, ``SYSP_SPEC_UAT_HARNESS_ONE_TIME_ENABLEMENT``, ``SYSP_US_UAT_INSTALLER_HARNESS_TARGETS``, ``SYSP_REQ_UAT_INSTALLER_HARNESS_TARGETS``, ``SYSP_SPEC_UAT_INSTALLER_HARNESS_TARGETS`` |

#### Historical Command and Data-Flow Record

The intermediate design used remote and installed-runtime command forms that
included Claude as a production target and exposed orchestration selection.
Those obsolete signatures are intentionally omitted to prevent accidental use.
Use only the current commands in the README Installation section.

The data flow is:

``explicit repository/branch/harness -> PEP 723 runtime resolution ->
runtime-owned pre-mutation checkpoint -> one resolved upstream revision ->
product inventory and bytes -> selected-harness adaptation/native writes +
stable runtime refresh -> docs/orchestration configuration -> orphan cleanup ->
Sphinx validation -> final commit -> checkpoint deletion -> structured report``.

On handled failure after checkpoint creation, the runtime restores exact file
and Git-index pre-state, deletes the checkpoint, and emits neither final commit
nor success. No bootstrap manifest, native Installer-agent discovery, Agent,
Task, ``runSubagent``, or SEND operation participates in installation control
flow.

#### Production Matrix and README Acceptance

Production-supported harnesses for this CR are VS Code GitHub Copilot,
OpenCode, and Claude Code. Qoder remains an experimental next target until its
clean install, repeat update, native invocation, and rollback UAT is complete.

README Getting Started SHALL:

* list only Git and ``uv`` as common installation prerequisites;
* state that commands run in the target Git repository;
* provide separate commands for ``vscode``, ``opencode``, and ``claude``;
* state that the same command is rerun for update and once per harness used;
* show optional repository and branch inputs;
* require neither pip/bare-Python setup nor Setup pre-placement;
* state that Claude CLI installation/authentication is external; and
* label Qoder experimental rather than production-supported.

#### UAT Correction

The existing UAT chains now require: remote raw-URL clean installation for all
three production harnesses; repeat update with an unchanged command and an
idempotent no-change run; installed Setup directly invoking the local runtime
while Agent/Task/``runSubagent`` use is forbidden; and absence of checkpoint
residue after both success and injected post-checkpoint failure. Harness-target
adapter UAT runs each harness separately and treats Qoder only as an
experimental deterministic fixture.

#### MECE and Consistency

* Initial install ownership is exclusively
  ``SYSP_REQ_HARNESS_NATIVE_INSTALL``; update entry behavior is exclusively
  ``SYSP_REQ_HARNESS_NATIVE_UPDATE``.
* Runtime transaction behavior remains owned by
  ``SYSP_REQ_INSTALLER_WORKFLOW`` and ``SYSP_REQ_INSTALLER_ROLLBACK``.
* Bootstrap manifest fetch and native Installer delegation requirements retain
  their IDs as deprecated trace nodes and point to their replacements.
* Branch propagation, one-revision source fidelity, native artifact generation,
  validation gating, final commit, rollback, and exact-byte adaptation remain
  required.
* Active-spec scans contain no remaining copied-Setup, detected-harness, or
  nested Installer-delegation acceptance path.

### Residual Limitations

- Claude Code native files and frontmatter pass static discovery UAT. Live
  invocation is blocked on this machine because ``claude auth status`` reports
  ``loggedIn: false``; CLI installation and authentication remain external
  prerequisites.
- Qoder remains experimental until clean install, repeat update, native
  invocation, and rollback are independently validated.

### Production-Stable Implementation Run

Implementation followed approved design commit ``ff05900`` on
``feature/harness-interop`` without modifying specification content or version
numbers.

#### RED / GREEN

- RED: Setup source contract failed because frontmatter still allowed
  ``syspilot.installer`` and workflow prose delegated through the native agent
  mechanism.
- GREEN: Setup now declares only execution capability and directly runs
  ``uv run --no-project .syspilot/installer.py install`` with repository,
  branch, target, harness, and synchronous-orchestration defaults.
- RED: the public CLI accepted ``--harness qoder`` despite the approved
  production matrix.
- GREEN: public CLI choices are ``vscode``, ``opencode``, and ``claude``;
  deterministic Qoder adapter functions remain covered as experimental output.
- RED: an explicit OpenCode run populated pre-existing Claude and Qoder
  directories, and Installer-agent prose still claimed exclusive Setup
  invocation.
- GREEN: each run writes all byte-exact VS Code files plus only the explicitly
  selected native harness target; the Installer agent is optional diagnostic
  documentation and not a control-plane dependency.

#### Executable Acceptance

- Local HTTP PEP 723 clean installs pass for all three production harnesses
  using only Git and ``uv`` assumptions. Repeating the identical command
  reports ``commit: null`` and zero runtime changes.
- Every target remains free of ``.venv``, ``__pycache__``, ``docs/_build``, and
  transaction checkpoint residue.
- Complete VS Code output is byte-equal to product source. OpenCode output
  parses natively with CM ``mode: primary``, implementer ``mode: subagent``,
  and explicit Task permission.
- OpenCode 1.17.4 live UAT recorded a native ``task`` call from
  ``syspilot.cm`` to ``syspilot.implement``; the engineer returned
  ``ENGINEER_OK`` and the manager returned ``MANAGER_OK: ENGINEER_OK``.
- Claude Code 2.1.175 static UAT finds and parses all 13 native agents,
  including Setup, CM, and implementer. Live UAT is not claimed while auth is
  unavailable.

### Production-Readiness Cleanup

- Release validation uses ``astral-sh/setup-uv@v6`` and runs both executable
  suites through the dependency declaration in ``docs/requirements.txt``:
  ``uv run --python 3.11 --with-requirements docs/requirements.txt python -m unittest discover -s tests -v``
  and ``uv run --python 3.11 --with-requirements docs/requirements.txt python -m unittest docs.test_docs_build``.
- Release documentation uses one dependency-scoped, warnings-as-errors command:
  ``uv run --python 3.11 --with-requirements docs/requirements.txt python docs/docs-build.py clean``.
- The active release workflow contains no ``actions/setup-python`` use and no
  bare ``python``, ``pip``/``pip3``, or ``sphinx-build`` executable command.
  The executable contract check distinguishes command-boundary invocations
  from the allowed ``python`` interpreter token following ``uv run``.
- Final isolated Python 3.11 replay passed 28 installer tests and 4
  documentation-helper tests, the full clean Sphinx build completed with zero
  warnings, and PyYAML parsed ``.github/workflows/release.yml`` successfully.

---

## Final Consistency Check

**Status**: ✅ passed for the production-stable installation design correction

### Traceability Verification

| User Story | Requirements | Design | Complete? |
|------------|--------------|--------|-----------|
| ``SYSP_US_HARNESS_INSTALL`` | Native install/update/prerequisites/no-regression | Target matrix, deterministic entry/runtime/workflow/targets | ✅ |
| ``SYSP_US_SETUP`` | Setup soul/duties and deprecated bootstrap delegation | Setup soul/duties/direct-runtime workflow | ✅ |
| ``SYSP_US_INSTALLER`` | Workflow/source/rollback/scope/internal agent surface | Runtime/workflow/source/rollback/targets | ✅ |
| ``SYSP_US_DOC_EXTERNAL`` | README documentation | README structure and Getting Started criteria | ✅ |
| Harness installation UAT stories | UAT data requirements | Remote install/update/direct Setup/checkpoint outcomes | ✅ |

### Artefakt-Removal-Check

*Fill in only when this CR removes an artefact (file, field, configuration key, REQ-ID).*

For each removed artefact, run a project-wide grep on all plausible name variants and classify results:

| Removed Artefact | Class (a): Code/Workflow refs | Class (b): Doc refs | Class (c): Historic Change Docs |
|------------------|-------------------------------|---------------------|---------------------------------|
| Bootstrap-manifest control plane | Active requirements/design deprecated or replaced | Active specification docs corrected | Historical CR records retained |
| Setup-to-Installer agent delegation | Active workflow/UAT replaced with direct runtime execution | Active specification docs corrected | Historical acceptance evidence retained |
| Harness presence auto-detection | Active target design/UAT replaced with explicit ``--harness`` | Active specification docs corrected | Historical implementation records retained |

- [x] All class (a) active specification/workflow references fixed in this design-only CR
- [x] All class (b) active specification documentation references fixed in this CR
- [x] Class (c) historical Change Document records retained as audit history

### Issues Found

- [x] No open consistency issue in the corrected specification set.
- [x] The two pre-existing ``ontology-architecture`` cross-reference warnings
  are resolved; the full warnings-as-errors build reports zero warnings.

### Sign-off

- [x] All active corrected elements approved; superseded bootstrap requirements intentionally deprecated with replacements
- [x] All conflicts resolved
- [x] Traceability verified against refreshed ``needs.json``
- [x] Ready for implementation

---

## QM Findings

*QM writes findings directly into this section after each review round. PM records
decisions (fix-now / defer / accept-as-is) with rationale in the same section.
Multiple review rounds are appended as sub-sections. Existing CDs without this
section are unaffected — the section is additive, never required retroactively.*

### Round 1

**Reviewed by:** QM
**Review date:** 2026-09-16

#### Findings

| # | Level | Element ID | Finding | Severity |
|---|-------|------------|---------|----------|
| 1 | L? | {ID} | {description} | high / medium / low |

#### PM Decisions

| # | Finding # | Decision | Rationale |
|---|-----------|----------|-----------|
| 1 | 1 | fix-now / defer / accept-as-is | {rationale} |

### Round 2

**Reviewed by:** QM
**PM decision date:** 2026-09-17
**Overall disposition:** Quality is not cleared. Schema validation and tests pass,
but all consolidated findings require correction. Finding 14 is the highest
priority, followed by consistent production classification and evidence for
Claude and Qoder.

#### Findings and PM Decisions

| # | Level | Finding | Decision | PM rationale |
|---|-------|---------|----------|--------------|
| 1 | L0 | Content invariance overlaps across `SYSP_US_AGENT_ARCH`, `SYSP_US_SKILL_ARCH`, and `SYSP_US_HARNESS_PORTABILITY`; Skill AC wording contradicts allowed frontmatter adaptation. | fix-now | Assign one owner for invariance and align the Skill AC with deterministic native adaptation. |
| 2 | L0 | `SYSP_US_SETUP` ownership is stale versus remote deterministic initial install and the installed Setup update role. | fix-now | Correct ownership so initial installation and subsequent updates have unambiguous actors. |
| 3 | L0 | Claude is classified production although live native invocation UAT is unexecuted; its AC requires experimental status until completion. | fix-now | Production status must follow the stated evidence gate. |
| 4 | L0 | Selected-harness wording says only the selected target, while implementation always installs `.github` plus the selected harness. | fix-now | Choose and apply one installation-target semantic throughout the hierarchy. |
| 5 | L0 | The Installer story requires prompt files for every non-VS-Code harness although Claude has none. | fix-now | Make the story reflect harness-native invocation surfaces instead of requiring nonexistent artifacts. |
| 6 | L0 | Completed stories and statuses remain `draft`. | fix-now | Align lifecycle status with completed and approved work. |
| 7 | L1 | Stale `runSubagent` and nested Installer delegation requirements conflict with direct runtime updates. | fix-now | Requirements must describe the implemented direct runtime update model consistently. |
| 8 | L1 | Bootloader upstream-current authority conflicts with installed stable runtime update semantics. | fix-now | Establish one authoritative update source and lifecycle. |
| 9 | L1 | Verbatim frontmatter wording conflicts with deterministic native adaptation. | fix-now | Preserve methodology content while explicitly permitting required frontmatter transformation. |
| 10 | L1 | Installer scope lists only `.github` and excludes stable runtime and native targets. | fix-now | Expand scope to every transactionally managed installation target. |
| 11 | L1 | Limitation disclosure, no-regression, and transaction rules have overlapping owners. | fix-now | Separate ownership so each constraint has one testable requirement. |
| 12 | L1 | Command behavioral equivalence is uncovered. | fix-now | Add explicit requirement coverage for command behavior across supported harnesses. |
| 13 | L1 | Deprecated replacement requirements are prose-only, not machine-readable. | fix-now | Encode replacement relationships in the ontology-supported schema. |
| 14 | L2 / implementation / tests | Critical rollback gap after Git commit but before checkpoint deletion: `restore_checkpoint` does not restore `HEAD`. | fix-now | Highest priority: make rollback restore repository state for every post-commit failure window and prove it with failure injection. |
| 15 | L2 / implementation / tests | Selected-harness design and implementation disagree. | fix-now | Resolve the target-selection contract and align design, implementation, and tests. |
| 16 | L2 / implementation / tests | Stale verbatim-copy, Setup delegation, bootstrap public command, Jarvis inference/user choice, and actor creation designs remain exposed. | fix-now | Remove or replace stale designs so published behavior has one current definition. |
| 17 | L2 / implementation / tests | Setup's upstream-current claim contradicts local runtime execution. | fix-now | State the actual authority and execution location without contradiction. |
| 18 | L2 / implementation / tests | Qoder's experimental boundary conflicts with production-shaped UAT. | fix-now | Keep classification, acceptance claims, and UAT shape consistent with available evidence. |
| 19 | L2 / implementation / tests | Adapter and implemented spec statuses remain `draft`. | fix-now | Update statuses to accurately represent implemented and verified elements. |
| 20 | L2 / implementation / tests | Failure-injection tests do not cover all claimed phases, especially post-commit failure. | fix-now | Add phase-complete failure coverage, prioritizing the post-commit rollback path. |
| 21 | L2 / implementation / tests | `SYSP_SPEC_UAT_INSTALLER_SPEC_REWRITE` still assumes customized-tools preservation and Git-reset rollback. | fix-now | Rewrite the UAT contract to match deterministic installation and checkpoint rollback semantics. |
| 22 | L2 / implementation / tests | Claude production status lacks live authenticated invocation evidence. | fix-now | Keep Claude experimental until live authenticated native invocation passes and is recorded. |

#### Round 2 Specification Resolution

**Status:** All 22 fix-now findings are resolved in the specification and UAT
contracts. Production implementation and executable tests remain follow-up
work where listed below.

**Binding decisions applied:**

* Each invocation manages exactly one explicit harness target plus shared
  ``.syspilot/installer.py`` and missing-only documentation bootstrap files.
  It does not write another harness's methodology directory.
* VS Code GitHub Copilot and OpenCode are production-supported. Claude Code
  and Qoder remain experimental until each completes clean-install,
  repeat-update, live native invocation, and rollback UAT.
* ``uv run --no-project`` is the sole Python runtime and dependency entry.
* Initial installation executes the remote deterministic runtime. Installed
  Setup performs updates by directly executing the stable local runtime. No
  bootstrap manifest, Installer-agent delegation, Jarvis inference, user
  orchestration choice, actor creation, or session scaffold participates in
  installation control flow.
* Methodology bodies remain byte-exact while harness-required frontmatter and
  structural fields are transformed deterministically.
* The rollback transaction runs from checkpoint creation through checkpoint
  deletion and restores pre-install HEAD, index, and worktree even when failure
  occurs after installation commit creation.

**Finding closure:**

| Findings | Specification resolution |
|----------|--------------------------|
| 1-6 | L0 ownership, Setup lifecycle, selected-target semantics, native invocation surfaces, production classification, and statuses corrected. |
| 7-13 | L1 direct-runtime flow, local-runtime authority, deterministic frontmatter adaptation, complete scope, single-owner constraints, command equivalence, and machine-readable replacement links corrected. |
| 14-22 | L2 rollback boundary, target selection, stale flow removal/deprecation, Setup authority, experimental UAT boundaries, statuses, phase-complete failure injection, and legacy Installer UAT assumptions corrected. |

**Line endings:** The three pre-existing line-ending-only changes in the
harness one-time-enablement UAT chain were intentionally normalized to LF while
their Round 2 content was updated.

**MECE and trace verification:**

* Content invariance is owned by ``SYSP_US_HARNESS_PORTABILITY``;
  installation scope by ``SYSP_REQ_INSTALLER_SCOPE``; limitation disclosure
  by ``SYSP_REQ_HARNESS_LIMITATION_DISCLOSURE``; no-regression guarantees by
  their two dedicated requirements; and transaction restoration by
  ``SYSP_REQ_INSTALLER_ROLLBACK``.
* Refreshed inbound impact queries resolve the affected L0 stories to their
  L1 requirements and the corrected L1 requirements to their L2 designs and
  UAT chains. Deprecated bootstrap, orchestration-selection, and actor nodes
  remain linked as audit history and point to active replacements.
* ``uv run --python 3.11 --with-requirements docs/requirements.txt python
  docs/docs-build.py clean`` completes with zero warnings and schema
  validation passes.

#### Round 2 Implementation Resolution

**Status:** Implemented and verified after approved System Designer commit
``9e11b22``.

**Implemented behavior:**

* Each run writes only the explicit harness directory plus shared
  ``.syspilot/installer.py`` and missing-only documentation bootstrap files.
  Installation commits use the same path boundary and preserve unrelated
  staged changes.
* The public CLI accepts only ``vscode`` and ``opencode``. Claude Code and
  Qoder adapters remain directly testable fixture surfaces, but both values
  are rejected by the public install command with an argparse error.
* The public ``bootstrap`` subcommand, shipped ``bootstrap.json`` manifest,
  Installer-agent handoff helper, and orchestration-selection argument were
  removed. Setup directly executes the stable local runtime, which always
  installs ``syspilot.orchestration-subagent``.
* OpenCode maps a source ``user-invocable: true`` agent to ``mode: primary``
  even without an ``agents`` allowlist. Setup therefore remains the native
  user-facing entry point while carrying no Installer Task permission.
* Checkpoints now persist pre-install HEAD and symbolic-ref state in addition
  to files, directories, and index bytes. Rollback restores attached,
  detached, and unborn repository state; an injected failure after commit and
  before checkpoint deletion leaves no reachable installation commit.
* Focused failure seams cover dependency gate, source acquisition, runtime
  write, YAML parse, target write, documentation bootstrap, orphan cleanup,
  validation, summary, commit, and post-commit checkpoint deletion.
* OpenCode command tests cover every source prompt, preserving its agent route
  and description behavior while emitting an empty command body.

**RED evidence:**

* Selected OpenCode installation created ``.github``; user-invocable Setup
  adapted as ``subagent``; Claude, ``bootstrap``, and ``--orchestration`` were
  accepted by the public parser.
* Post-commit failure injection returned success and retained the installation
  commit for both an existing branch and an unborn branch.
* The installer commit absorbed an unselected ``.github`` edit and an unrelated
  pre-staged file.
* README and architecture documentation still advertised Claude as production
  and described VS Code-plus-selected-target writes.

**GREEN evidence and test matrix:**

* ``uv run --python 3.11 --with-requirements docs/requirements.txt python -m
  unittest discover -s tests -v`` passes 37 tests.
* The suite includes local and HTTP-served clean/install-update runs for VS
  Code and OpenCode, exact VS Code source bytes, static Claude/Qoder adapter
  fixtures, public experimental-target rejection, all transaction failure
  phases, success cleanup, command equivalence, and no target ``.venv``,
  ``__pycache__``, build, or checkpoint residue.
* ``uv run --python 3.11 --with-requirements docs/requirements.txt python -m
  unittest docs.test_docs_build -v`` passes 4 tests.
* ``uv run --python 3.11 --with-requirements docs/requirements.txt python
  docs/docs-build.py clean`` succeeds with zero warnings and zero schema
  warnings.
* OpenCode 1.17.4 ``debug config`` resolves Setup as primary without Task
  permission, CM as primary with ``syspilot.implement`` allowed, and the
  implementer as subagent. Authenticated live invocation produced a native
  Task call from CM to the implementer, returned ``ENGINEER_OK`` then
  ``MANAGER_OK: ENGINEER_OK``, and left the target worktree unchanged.

**Changed implementation surfaces:** ``syspilot/installer.py``, Setup and
Installer agent sources, ``tests/test_installer.py``, ``README.md``, and
``docs/architecture.md``. Obsolete ``syspilot/bootstrap.json`` was deleted.

**Blockers:** None for the approved production scope. Claude Code and Qoder
remain explicitly experimental; no live production acceptance is claimed for
either harness.

### Round 3

**Reviewed by:** QM
**PM decision date:** 2026-09-17
**Overall disposition:** Quality remains uncleared. All eight residual findings
are accepted for immediate correction despite the passing 37 implementation
tests, 4 documentation tests, and zero-warning schema build.

#### Findings and PM Decisions

| # | Level | Finding | Decision | PM rationale |
|---|-------|---------|----------|--------------|
| 1 | L0 | `SYSP_US_SKILL_ARCH` AC-10 still repeats content invariance instead of purely delegating ownership to `SYSP_US_HARNESS_PORTABILITY`. | fix-now | Remove the duplicate invariance rule and make AC-10 delegate ownership to the portability story so Level 0 has one authoritative owner. |
| 2 | L1 | `SYSP_REQ_HARNESS_PORTABILITY_NO_REGRESSION` overlaps installation behavior owned by `SYSP_REQ_HARNESS_INSTALL_NO_REGRESSION`. | fix-now | Restrict portability no-regression to behavior and keep installation-flow compatibility solely in install no-regression, yielding distinct testable ownership. |
| 3 | L1 / L2 trace | `SYSP_SPEC_HARNESS_PROMPT_ADAPTER` lacks a link to `SYSP_REQ_HARNESS_BEHAVIORAL_EQUIVALENCE`, and its executable test invokes only routing metadata rather than equivalent command requests. | fix-now | Add the missing requirement trace and exercise equivalent user command requests so both traceability and behavioral evidence cover the command adapter. |
| 4 | L2 transaction ordering | The approved workflow checkpoints before source acquisition, while implementation acquires sources before checkpoint creation. | fix-now | Define source acquisition as read-only and permitted before checkpoint creation; require checkpoint creation before every target mutation, then align specification and tests to that transaction boundary. |
| 5 | L2 / UAT | `SYSP_SPEC_UAT_INSTALLER_SPEC_REWRITE` remains stale on `@Setup` initial install, `.github`-only/table output, tools-preservation failure criteria, and Git-reset/manual best-effort rollback. | fix-now | Rewrite the UAT around remote-runtime initial installation, explicit harness targets and current output, deterministic adaptation, and checkpoint-based exact rollback. |
| 6 | L2 / UAT | `SYSP_SPEC_UAT_HARNESS_AGENT_ADAPTER` still requires Setup-to-Installer permission and delegation. | fix-now | Remove the obsolete delegation expectation and verify Setup's intended direct stable-runtime execution contract. |
| 7 | L2 Skill adapter | Approved design says unsupported `group`, `tools`, and `triggers` fields are omitted, but production OpenCode adaptation preserves them. | fix-now | Align design and implementation by omitting unsupported production OpenCode fields while preserving the methodology body byte-exactly and selecting Installer mutual exclusion from source metadata before adaptation. |
| 8 | L2 Setup frontmatter | The specification says Setup has no tools and version `0.5.3`, while the product declares `tools: [execute]` and version `v0.9.1`. | fix-now | Align the specification to the intended product values because direct runtime execution requires `execute` and the shipped release version is `v0.9.1`. |

#### Round 3 Specification Resolution

**Status:** All eight fix-now findings are resolved in the specification and
UAT contracts. Corrected active elements were held at ``draft`` during the
design pass and promoted to ``approved`` only after strict validation.

| Findings | Specification resolution |
|----------|--------------------------|
| 1 | ``SYSP_US_SKILL_ARCH`` delegates harness-portability ownership without repeating content invariance. |
| 2 | Portability no-regression owns behavior only; install no-regression owns installation/update compatibility. |
| 3 | Prompt adapter links behavioral equivalence and UAT invokes equivalent requests through both command surfaces. |
| 4 | Source acquisition, parsing, and transformation are read-only before checkpoint creation; mutation remains post-checkpoint only. |
| 5 | Installer deterministic-runtime UAT now covers remote initial install, explicit harness scope, deterministic adaptation, and exact checkpoint rollback. |
| 6 | Setup-to-Installer delegation acceptance was removed; Setup directly executes the stable local runtime. |
| 7 | Unsupported OpenCode Skill fields are omitted while source ``group`` metadata drives Installer mutual exclusion. |
| 8 | Setup frontmatter specifies ``tools: [execute]``, ``agents: []``, and ``version: v0.9.1``. |

### Round 4

**Reviewed by:** QM
**PM decision date:** 2026-09-17
**Overall disposition:** Quality remains uncleared. All seven findings require
immediate correction before the change can proceed.

#### Findings and PM Decisions

| # | Level | Finding | Decision | PM rationale |
|---|-------|---------|----------|--------------|
| 1 | Critical security | Target writes can traverse Windows junctions or reparse points outside the target; rollback may fail and leave external writes or checkpoint residue. | fix-now | Enforce containment and no-follow handling for every mutable path, with rollback that safely removes all transaction residue. |
| 2 | High safety / scalability | The checkpoint snapshots the entire non-Git project and rollback deletes and reconstructs all top-level content, exposing unrelated or sensitive files and destroying concurrent changes. | fix-now | Limit checkpoint and restore scope to declared mutable paths so unrelated and concurrent files remain untouched. |
| 3 | High OpenCode behavior | The installed orchestration Skill body remains VS Code-only `runSubagent`; OpenCode requires native Task mapping without methodology drift. | fix-now | Define a harness-specific tool binding that preserves the shared orchestration semantics while using OpenCode's native Task mechanism. |
| 4 | High installed workflow paths | OpenCode Skills retain `.github` paths, and the selected non-VS-Code target omits templates required by change-launcher. | fix-now | Provide deterministic harness-neutral path adaptation and install every runtime and template asset required by the selected harness. |
| 5 | High documentation | The current uncommitted specification has malformed RST indentation that fails the warning-as-error documentation build. | fix-now | Repair the malformed RST in the Designer pass so the strict documentation build succeeds. |
| 6 | Medium Git | Linked worktrees use a `.git` file and external index, but directory-based assumptions reject them. | fix-now | Discover Git directory, index, and ref state through `git rev-parse` and support exact rollback in linked worktrees. |
| 7 | Medium transaction order | Transformation and YAML parsing occur after checkpoint creation, although all read-only acquisition, parsing, and transformation should precede the checkpoint and every mutation should follow it. | fix-now | Align specifications and tests to one transaction boundary with all read-only work before checkpoint creation and all mutations after it. |

#### Round 4 Specification Resolution

**Status:** All seven fix-now findings are resolved in approved L0/L1/L2 and
UAT contracts. Production implementation and executable evidence are assigned
to Dev/Verify as listed below.

| Findings | Specification resolution |
|----------|--------------------------|
| 1 | Every planned write/delete/restore passes lexical containment and no-follow physical ancestry validation. Symlinks, junctions, mount points, and reparse points are rejected before mutation; rollback never traverses an out-of-target link. |
| 2 | The checkpoint manifest contains only exact planned entries in the selected harness tree, shared ``.syspilot`` runtime/resources, planned missing-only docs, and exact Git metadata. Unrelated files are never recursively snapshotted or restored; planned-path conflicts preserve external bytes and fail without success. |
| 3 | The orchestration Skill retains one semantic SEND/RECEIVE/RESPOND contract and one adapter-owned binding section. VS Code generates ``runSubagent`` mapping; OpenCode generates native Task mapping and no ``runSubagent`` instruction. |
| 4 | Native ``SKILL.md`` files remain selected-harness-only. Templates use ``.syspilot/templates/`` and non-native Skill resources use ``.syspilot/skills/<name>/``; change-launcher and impact reference these stable paths. |
| 5 | The four-line malformed RST continuation was repaired and repeatedly validated with a fresh warning-as-error build. |
| 6 | Git state discovery uses ``git rev-parse --git-dir``, ``git rev-parse --git-path index``, symbolic full HEAD, and OID/unborn detection. Attached, detached, and unborn linked-worktree rollback is explicit. |
| 7 | Dependency resolution, GitHub acquisition, YAML parsing, transformation, path derivation, containment, and complete target-plan validation all finish before checkpoint creation; only the frozen plan executes afterward. |

**Security and transaction model:** The resolved target root is the sole
filesystem trust boundary. Planned relative paths reject absolute, drive/UNC,
and ``..`` escapes, then every existing ancestry component is inspected with
no-follow semantics immediately before mutation. Git paths outside the
worktree are accepted only as exact outputs of Git discovery commands. A
checkpoint never copies an entire project or mutable parent. Existing
directories retain unplanned children; newly created directories are removed
only when empty. Optimistic identity checks detect transaction-external
changes before overwrite and before rollback restoration.

**Separate MECE checks:**

* **L0:** Installation safety is owned by
  ``SYSP_US_HARNESS_INSTALL``; native behavior/binding and stable resource
  portability by ``SYSP_US_HARNESS_PORTABILITY``; observable evidence by the
  UAT stories. ``SYSP_US_SKILL_ARCH`` delegates portability without overlap.
  No gap or contradiction remains.
* **L1:** ``SYSP_REQ_INSTALLER_SCOPE`` owns the positive mutable set;
  ``DIRECT_OPS`` owns containment; ``ROLLBACK`` owns checkpoint/restoration and
  conflicts; ``WORKFLOW`` owns ordering; ``GITHUB_SOURCE`` owns immutable
  acquisition; behavioral equivalence/content-single-source own semantics and
  adaptation. Cross-owner wording delegates rather than duplicates. No gap or
  contradiction remains.
* **L2:** Installer Scope/Engine/Workflow coordinate the frozen plan while
  Direct Operations and Rollback exclusively define security/restoration.
  Skill Adapter owns stable resources; Orchestration Adapter owns only the
  harness binding section. Dedicated UAT scenarios cover each design rule.
  No gap or contradiction remains.

The MECE Engineer is advisory and read-only. The current runtime exposed no
``runSubagent`` tool, so the System Designer applied the Engineer's published
one-level-at-a-time rubric separately at L0, L1, and L2 and recorded the
results above rather than claiming a delegated run.

**Trace and validation:** Mandatory inbound impact queries were run from the
affected consumer stories, then from changed requirements at depth 1, followed
by depth-2 L2 cross-checks. All changed active nodes resolve to parents and
children. A fresh ``sphinx-build -E -W --keep-going`` completed with zero
warnings and zero schema warnings after approval.

**Remaining implementation and verification tasks:**

All listed tasks were completed in the Round 3/4 implementation run below.

#### Round 3/4 Implementation Resolution

**Status:** Implemented and verified after approved specification commit
``1e20af2`` on ``feature/harness-interop``.

**Security and transaction implementation:**

* The runtime builds an immutable ``InstallPlan`` containing every write,
  orphan deletion, missing-only documentation file, shared resource, expected
  path identity, and mutable parent before checkpoint creation. Absolute,
  drive/UNC, backslash, empty/dot, and ``..`` source or destination escapes are
  rejected during this read-only phase.
* Every existing ancestry component is inspected with ``lstat`` semantics.
  Symbolic links, Windows junctions/reparse points, mount points, and
  non-directory ancestors are rejected before checkpointing and revalidated
  immediately before and after parent creation and before each mutation.
* Checkpoint JSON contains only declared mutable paths and exact Git state.
  It does not recursively read unrelated project files. Rollback restores only
  manifest entries, removes new directories only when empty, preserves
  unrelated concurrent changes, and reports incomplete rollback without
  overwriting a concurrent change inside a mutable path.
* Git state and index locations are discovered through ``git rev-parse
  --git-dir``, ``git rev-parse --git-path index``, symbolic full HEAD plus
  ``git symbolic-ref`` fallback, and OID queries. Attached, detached, and
  unborn ordinary and linked-worktree transactions are covered.

**Adapter and resource implementation:**

* OpenCode Skill output omits unsupported source ``group``, ``tools``, and
  ``triggers`` fields. Source ``group`` metadata is parsed before adaptation
  and still enforces orchestration mutual exclusion.
* The synchronous orchestration Skill keeps one shared semantic vocabulary.
  VS Code retains the source ``runSubagent`` binding; OpenCode receives a
  deterministic native Task binding and no ``runSubagent`` instruction.
* Native ``SKILL.md`` files remain selected-harness-only. Non-native Skill
  resources install under ``.syspilot/skills/<name>/`` and templates under
  ``.syspilot/templates/``. Change Launcher and Impact commands use those
  stable paths, and an installed Change Launcher fixture locates the shared
  template successfully.
* Setup frontmatter remains ``tools: [execute]``, ``agents: []``, and
  ``version: v0.9.1``. Public CLI targets remain VS Code and OpenCode only;
  Claude Code and Qoder remain experimental, and obsolete bootstrap,
  orchestration-choice, and checkpoint-handoff controls remain rejected.

**RED/GREEN evidence:**

* RED: scoped checkpoint API was absent; persisted state included unrelated
  files. GREEN: a 1 MiB sensitive sentinel is absent from bounded checkpoint
  JSON and rollback leaves unrelated bytes untouched.
* RED: malicious source escapes and a real Windows junction ancestry installed
  successfully. GREEN: both fail before checkpoint creation or mutation, and
  a concurrent rollback junction is preserved as a reported conflict with no
  checkpoint residue.
* RED: parse/transform occurred after checkpoint creation. GREEN: event
  instrumentation proves ``plan_validated`` precedes ``checkpoint_created``,
  which precedes ``first_mutation``; source/parse/plan failures produce no
  checkpoint or target change.
* RED: OpenCode retained unsupported Skill fields and the VS Code-only binding;
  shared scripts/templates were missing. GREEN: native metadata, Task binding,
  source-group mutex, shared resources, and installed launcher execution pass.
* RED: GitHub API accepted truncated or incomplete trees. GREEN: revision,
  truncation, duplicate, required-root, and runtime checks complete before any
  raw-content fetch.

**Executable verification:**

* ``uv run --python 3.11 --with-requirements docs/requirements.txt python -m
  unittest discover -s tests -v`` passes 55 tests with two explicit opt-in
  integration skips in the default run.
* ``uv run --python 3.11 --with-requirements docs/requirements.txt python -m
  unittest docs.test_docs_build -v`` passes 4 tests.
* ``uv run --python 3.11 --with-requirements docs/requirements.txt python
  docs/docs-build.py clean`` succeeds with zero warnings and zero schema
  warnings.
* PyYAML parses ``.github/workflows/release.yml``; Python syntax, ``git diff
  --check``, and tracked ``.venv``/``__pycache__``/checkpoint residue checks
  pass.
* OpenCode 1.17.4 ``debug config`` parses the generated installation. Live
  native CM-to-implementer Task delegation emits a ``task`` event targeting
  ``syspilot.implement`` and returns ``ENGINEER_OK`` then ``MANAGER_OK``.
* The real GitHub API acquisition test reached ``api.github.com`` but was
  conditionally skipped because the runner's unauthenticated API quota returned
  HTTP 403. The test supports ``GITHUB_TOKEN`` and does not substitute a local
  repository behind HTTP.

### Round 5

**Reviewed by:** QM
**PM decision date:** 2026-09-17
**Overall disposition:** Quality remains uncleared. All eight findings require
immediate correction on the existing feature branch before another Quality
review.

#### Findings and PM Decisions

| # | Level | Finding | Decision | PM rationale |
|---|-------|---------|----------|--------------|
| 1 | L0 | The Setup story title and description still say Setup installs and updates, while AC-6 assigns initial installation exclusively to the remote runtime. | fix-now | Scope Setup to the installed update entry point so initial-install and update ownership remain distinct. |
| 2 | L0 | Installer AC-6 unconditionally removes ``.github/templates`` artifacts, conflicting with selected-harness-only installation. | fix-now | Rewrite the criterion around legacy and shared-resource migration while preserving every unselected native harness tree. |
| 3 | L0 | Skill Architecture says Setup enforces orchestration mutual exclusion, although Installer owns that responsibility. | fix-now | Delegate mutual-exclusion ownership to Installer and keep Skill Architecture focused on the skill contract. |
| 4 | L1 | The rollback mutable-path list omits ``.syspilot/skills`` and ``.syspilot/templates``. | fix-now | Include every shared planned resource in the rollback-owned mutable set so transaction coverage matches the installation plan. |
| 5 | L1 | uv, branch, and direct-execution rules overlap among native install/update, Installer workflow/source, and Setup duties. | fix-now | Assign one normative owner to each rule and replace duplicate normative wording elsewhere with references. |
| 6 | L1 | Experimental UAT is inconsistent: the target matrix makes Claude and Qoder fixtures optional while prompt UAT requires all four harnesses installed. | fix-now | Make Claude and Qoder fixture evidence consistently optional and non-production until their independent acceptance gates are complete. |
| 7 | High implementation | Supplied checkpoint validation checks target ownership but not exact mutable-path coverage of the frozen plan, so an accepted narrow checkpoint followed by forced validation failure can leave the OpenCode agent and runtime installed. | fix-now | Require the supplied checkpoint mutable-path set to exactly cover the frozen plan before mutation, safely reject under- or over-broad checkpoints, and add a regression test for this failure path. |
| 8 | L2 | Independently verified production design specifications remain ``approved`` rather than transitioning to ``implemented``. | fix-now | Transition implementation-covered, independently verified production specifications to ``implemented`` while leaving experimental or unverified elements ``approved``. |

#### Round 5 Specification Resolution

**Status:** All eight fix-now findings are resolved in the specification and
UAT contracts. This autonomous Designer pass modifies specifications, UAT, and
this Change Document only; production Python remains unchanged.

| Finding | Resolution |
|---------|------------|
| 1 | ``SYSP_US_SETUP`` is titled and described exclusively as the installed update entry point; initial installation remains exclusively remote-runtime owned. |
| 2 | ``SYSP_US_INSTALLER`` AC-6 migrates eligible legacy selected-harness templates to shared ``.syspilot/templates/`` while preserving every unselected harness tree. |
| 3 | ``SYSP_US_SKILL_ARCH`` delegates orchestration-group mutual exclusion to the Installer owner in ``SYSP_US_INSTALLER``. |
| 4 | ``SYSP_REQ_INSTALLER_ROLLBACK`` explicitly covers the selected harness, ``.syspilot/installer.py``, ``.syspilot/skills/``, ``.syspilot/templates/``, planned missing-only docs, and exact planned Git state. |
| 5 | Normative ownership is MECE: ``SYSP_REQ_HARNESS_NATIVE_INSTALL`` owns uv-only execution, ``SYSP_REQ_INSTALLER_GITHUB_SOURCE`` owns branch propagation and immutable source fidelity, and ``SYSP_REQ_HARNESS_NATIVE_UPDATE`` owns installed direct-runtime invocation. Other requirements reference these owners. |
| 6 | Target, prompt, Skill, agent, and limitation UAT chains require VS Code/OpenCode production evidence while treating Claude Code/Qoder fixtures as optional experimental evidence that cannot block or satisfy production acceptance. |
| 7 | ``SYSP_SPEC_INSTALLER_SUPPLIED_CHECKPOINT`` requires physical target-root identity and exact canonical normalized mutable-path-set equality with the frozen plan. Narrow, broad, mismatched-root, malformed, and duplicate-ambiguous checkpoints fail before mutation. ``TC-IDR-SUPPLIED-CHECKPOINT`` requires narrow, broad, and target-mismatch rejection with byte-exact zero mutation. |
| 8 | Independently verified production-only Setup and Installer L2 elements are ``implemented``. Mixed harness elements and the new supplied-checkpoint behavior remain ``approved``; no Claude/Qoder runtime acceptance is implied. |

**Status boundary:** ``SYSP_SPEC_SETUP_SOUL``, ``SYSP_SPEC_SETUP_DUTIES``,
``SYSP_SPEC_SETUP_WORKFLOW``, ``SYSP_SPEC_SETUP_FRONTMATTER``,
``SYSP_SPEC_INSTALLER_SOUL``, ``SYSP_SPEC_INSTALLER_FRONTMATTER``,
``SYSP_SPEC_INSTALLER_DUTIES``, ``SYSP_SPEC_INSTALLER_DOC_BOOTSTRAP``,
``SYSP_SPEC_INSTALLER_SKILL_MUTEX``, ``SYSP_SPEC_INSTALLER_WORKFLOW``,
``SYSP_SPEC_INSTALLER_GITHUB_SOURCE``, ``SYSP_SPEC_INSTALLER_ENCODING``,
``SYSP_SPEC_INSTALLER_DIRECT_OPS``, and ``SYSP_SPEC_INSTALLER_ROLLBACK`` are
``implemented`` based on the independent production evidence recorded in the
Round 2 and Round 3/4 implementation resolutions. Installer Scope, Adapter
Engine, Harness Targets, all harness adapter/limitation elements, and Harness
Deterministic Installation Entry remain ``approved`` because they mix
production behavior with Claude/Qoder experimental behavior.

**Per-level MECE:**

* **L0:** Setup owns installed update entry identity, Installer owns
  installation work and mutex enforcement, Skill Architecture owns only the

  exchangeable Skill contract, and remote initial installation remains in the
  harness-install story. No criterion repeats an actor owner.
* **L1:** uv-only execution, branch/source fidelity, and direct update
  invocation each have one normative owner. Workflow and Setup duties contain
  references rather than copied criteria. Scope defines planned paths;
  Rollback owns their checkpoint/restoration coverage.
* **L2/UAT:** Existing rollback remains implemented; the unimplemented supplied
  checkpoint acceptance rule is split into its own approved design. Production
  UAT is mandatory and experimental harness evidence is optional consistently.


**Remaining implementation and verification tasks:**

1. Developer: validate any supplied checkpoint after the complete installation
  plan is frozen and before the first target or Git mutation. Compare physical
  target-root identity and exact canonical normalized mutable-path sets;
  reject subsets, supersets, target mismatch, malformed paths, and normalized
  duplicates.
2. Developer: add executable fixtures for an exact accepted checkpoint plus a
  checkpoint missing an OpenCode agent/shared resource, a checkpoint adding an
  undeclared path, and a checkpoint owned by another target root.
3. Verify Engineer: prove all three rejection cases leave selected-harness
  files, ``.syspilot/installer.py``, ``.syspilot/skills/``,
  ``.syspilot/templates/``, documentation, HEAD, index, and worktree unchanged,
  with no commit, success report, or checkpoint residue.
4. UAT: keep Claude Code and Qoder acceptance optional and experimental until
  each independently completes clean install, repeat update, live native

  invocation, and rollback gates; only then review mixed-element status.

**Validation evidence:**

* Mandatory pre-edit and refreshed post-edit impact queries were run through
  ``uv`` from ``SYSP_US_SETUP``, ``SYSP_US_INSTALLER``,
  ``SYSP_US_SKILL_ARCH``, the three normative L1 owners,
  ``SYSP_REQ_INSTALLER_ROLLBACK``, all five optional-experimental UAT stories,
  and ``SYSP_US_UAT_INSTALLER_SPEC_REWRITE``.
* Bidirectional depth-2 trace from
  ``SYSP_SPEC_INSTALLER_SUPPLIED_CHECKPOINT`` resolves its rollback requirement
  and workflow/rollback consumers. The Installer UAT requirement resolves to
  ``SYSP_SPEC_UAT_INSTALLER_SPEC_REWRITE``; that expected-outcomes element

  resolves to both its UAT requirement and the new checkpoint design.
* Separate L0, L1, and L2 ownership scans found no remaining duplicated
  normative uv, branch, or direct-runtime criterion and no mandatory wording
  for unavailable Claude Code/Qoder fixtures in the five corrected UAT chains.
* ``uv run --python 3.11 --with-requirements docs/requirements.txt python -m
  unittest docs.test_docs_build -v`` passes all 4 tests after each level.
* ``uv run --python 3.11 --with-requirements docs/requirements.txt python
  docs/docs-build.py clean`` succeeds with zero warnings and zero schema
  warnings after the complete edit set.

#### Round 5 Implementation Resolution

**Implemented:** ``SYSP_SPEC_INSTALLER_SUPPLIED_CHECKPOINT`` now validates a

caller-supplied checkpoint immediately after the complete target plan is frozen
and loaded, before ``checkpoint_created`` is observed or any target or Git
mutation begins.

* Target ownership uses strict physical resolution plus filesystem identity.
  Mutable paths are normalized deterministically to contained target-relative
  ``/`` form, with host filesystem case normalization. Absolute, drive/UNC,
  empty, and root-escaping paths are rejected, while dot and parent aliases are
  collapsed before comparison.
* Duplicate normalized entries fail before set construction. The resulting
  checkpoint set must equal the frozen plan's canonical mutable-path set
  exactly; subsets and supersets are rejected.
* Runtime-created checkpoints continue to derive every mutable path directly
  from the same frozen plan. Accepted supplied checkpoints follow the existing
  success cleanup path; rejected caller-owned checkpoints remain available to
  their caller and the rejected run creates no additional checkpoint residue.
* RED: narrow, broad, normalized-dot-alias, and Windows case-alias checkpoints
  proceeded through installation. GREEN: all are rejected before mutation;
  exact checkpoints succeed and mismatched physical roots remain rejected.
* Rejection fixtures assert unchanged selected-harness/shared/documentation
  bytes, HEAD, Git index bytes, status, and worktree, no committer invocation,
  no success result, and preservation of the supplied checkpoint artifact.
* ``uv run --python 3.11 --with-requirements docs/requirements.txt python -m
  unittest discover -s tests -v`` passes 60 tests with the two documented
  opt-in integration skips. Setup, direct API, uv-only CLI, generated OpenCode
  configuration, rollback, and accepted-checkpoint behavior remain covered.
* ``uv run --python 3.11 --with-requirements docs/requirements.txt python -m
  unittest docs.test_docs_build -v`` passes all 4 tests, and ``uv run --python
  3.11 --with-requirements docs/requirements.txt python docs/docs-build.py
  clean`` succeeds with zero schema warnings.
* OpenCode 1.17.4 parses the generated configuration. The opt-in live native
  CM-to-implementer delegation emits one ``task`` event targeting
  ``syspilot.implement`` and returns both ``ENGINEER_OK`` and ``MANAGER_OK``.
* The opt-in real GitHub API acquisition test reached ``api.github.com`` and
  was conditionally skipped because the unauthenticated quota returned HTTP
  403; no local source substitute was used.

### Round 6

**Reviewed by:** QM
**PM decision date:** 2026-09-17
**Overall disposition:** Quality remains uncleared. All six findings require
immediate correction on the existing feature branch before another Quality
review.

#### Findings and PM Decisions

| # | Severity | Finding | Decision | PM rationale |
|---|----------|---------|----------|--------------|
| 1 | High | OpenCode commands discard user requests because the generated command body is empty; the native command requires ``$ARGUMENTS`` or ``$1`` forwarding. Existing test evidence fabricates metadata tuples rather than invoking the command. | fix-now | User requests must reach the selected agent through the native command surface, and acceptance evidence must exercise that behavior directly. |
| 2 | High | Rollback can erase concurrent commits because refs reset unconditionally without compare-and-swap against the installer-created commit. | fix-now | Rollback must preserve repository changes created outside the installation transaction. |
| 3 | High | Windows supplied-checkpoint rollback case-folds loaded paths but indexes a case-preserving expected map, causing ``KeyError``, incomplete restoration, and residue. | fix-now | Supplied-checkpoint rollback must restore the complete pre-install state on Windows without leaving transaction residue. |
| 4 | Medium | Supplied checkpoint path equality does not prove freshness; a stale same-plan checkpoint can overwrite newer pre-install bytes. | fix-now | A supplied checkpoint must be proven current before it can govern restoration. |
| 5 | Medium | Parent ancestry can become a junction or reparse point after containment validation but before a path-based write or delete. | fix-now | Containment must remain effective at the mutation boundary so target operations cannot escape through a time-of-check/time-of-use change. |
| 6 | Medium | A relative repository argument can be shadowed by a target-local path, violating the GitHub-only source contract. | fix-now | Repository selection must preserve the remote-source contract regardless of the target working directory. |

**Verification note:** One independent test run terminated unexpectedly
mid-suite. The complete relevant suite must be rerun after all six corrections;
the interrupted run is not clearance evidence.

#### Designer Resolution

**Status:** All six Quality findings and the full-suite reliability gate are
resolved in requirements, design, and executable UAT. This autonomous pass
does not modify production implementation.

**Level 0:** No product User Story change is required. Command request delivery
remains owned by ``SYSP_US_HARNESS_PORTABILITY``; transaction safety, remote
source, and installation reliability remain owned by ``SYSP_US_INSTALLER``.
The existing UAT story gained acceptance coverage only.

**Level 1 changes:**

* ``SYSP_REQ_INSTALLER_WORKFLOW`` owns complete normal suite execution and
  bounded resource behavior.
* ``SYSP_REQ_INSTALLER_GITHUB_SOURCE`` owns the public GitHub repository-input
  grammar and excludes every local path from production acquisition.
* ``SYSP_REQ_INSTALLER_DIRECT_OPS`` owns mutation-boundary no-follow primitives
  and fail-closed ancestry revalidation.
* ``SYSP_REQ_INSTALLER_ROLLBACK`` owns Git compare-and-swap, canonical
  checkpoint keys, and supplied-checkpoint nonce/fingerprint freshness.
* Existing command behavioral-equivalence requirements remain sufficient; no
  duplicate requirement was added.

**Level 2 changes:**

* ``SYSP_SPEC_HARNESS_PROMPT_ADAPTER`` emits ``$ARGUMENTS`` as the complete
  OpenCode command body while preserving source agent routing and description.
* ``SYSP_SPEC_INSTALLER_GITHUB_SOURCE`` and
  ``SYSP_SPEC_INSTALLER_ADAPTER_ENGINE`` accept only ``owner/repository`` or a
  supported GitHub HTTPS URL publicly; local bytes are available only through
  internal immutable ``SourceSnapshot.from_directory`` fixtures.
* ``SYSP_SPEC_INSTALLER_DIRECT_OPS`` defines descriptor/handle-relative
  no-follow operations, verified-parent atomic files, immediate identity
  revalidation, a realistic Win32 ``ctypes`` boundary, and deterministic race
  injection.
* ``SYSP_SPEC_INSTALLER_ROLLBACK`` and
  ``SYSP_SPEC_INSTALLER_SUPPLIED_CHECKPOINT`` define one canonical map key plus
  separate display spelling, immutable nonce and exact owned-path/Git handoff
  fingerprints, and compare-and-swap restoration of Installer-created Git
  state.
* ``SYSP_SPEC_INSTALLER_WORKFLOW`` requires investigation and complete rerun
  after abrupt termination and bounds work to source plus declared mutable
  paths.

**UAT changes:** Native OpenCode UAT invokes the generated command with a
multi-token request and verifies the routed Manager receives that exact text.
Installer UAT adds concurrent post-commit ref advancement, Windows mixed-case
restore, stale checkpoint, parent-swap race, local-path shadowing, and complete
normal-suite resource scenarios. Metadata inspection, interrupted runs, and
local-source substitution are explicitly insufficient evidence.

#### Round 6 MECE and Trace Check

* [x] Level 0 remains exhaustive without overlap: portability owns equivalent
  harness behavior; Installer owns installation transaction and source policy.
* [x] Level 1 has one normative owner per concern: workflow reliability,
  source grammar, mutation primitives, and rollback state/freshness.
* [x] Level 2 separates source parsing, filesystem mutation, rollback state,
  and command adaptation; orchestration specs reference these owners without
  restating their rules.
* [x] UAT retains the existing story -> test-data requirement -> expected-
  outcomes chains and adds executable evidence to those owners.
* [x] Mandatory impact queries identify the existing consumers of
  ``SYSP_REQ_HARNESS_BEHAVIORAL_EQUIVALENCE``,
  ``SYSP_REQ_INSTALLER_ROLLBACK``, ``SYSP_REQ_INSTALLER_GITHUB_SOURCE``, and
  ``SYSP_REQ_INSTALLER_WORKFLOW``; no new orphan element is introduced.

#### Implementation Tasks

1. Generate OpenCode command bodies as exact ``$ARGUMENTS`` plus terminal
   newline and replace metadata-tuple evidence with native command invocation.
2. Record pre-state and Installer-created Git state; use expected-old-OID
   ``git update-ref``/detached-HEAD compare-and-swap and preserve concurrent
   commits on conflict.
3. Introduce one canonical checkpoint-key function used by serialization,
   expected-current maps, and restore; retain ``display_path`` separately and
   add Windows mixed-case regression coverage.
4. Bind supplied checkpoints to a cryptographic nonce and exact mutable-path
   plus Git handoff fingerprints; revalidate only that owned set immediately
   before first mutation and reject stale checkpoints without mutation.
5. Implement no-follow mutation primitives, including verified-parent temp
   creation and Win32 handle/reparse identity checks, with deterministic race
   hooks for write, replace, delete, and restore.
6. Restrict public repository parsing to GitHub identifiers/HTTPS URLs and move
   local-directory fixtures behind internal ``SourceSnapshot`` construction.
7. Rerun the complete Installer suite in a fresh process, capture termination
   diagnostics and bounded resource evidence, and investigate any abrupt exit
   before presenting the rerun as Quality evidence.

#### Designer Validation Evidence

* Authoritative OpenCode command documentation, retrieved 2026-09-17, confirms
  that ``$ARGUMENTS`` is replaced with the command's complete argument text and
  that ``description`` and ``agent`` are native command options.
* Mandatory impact and final trace queries resolve every modified production
  requirement to ``SYSP_US_INSTALLER`` and its existing Design consumers; both
  modified UAT requirements resolve to their UAT story and expected-outcomes
  specification.
* Per-level MECE review found no Level 0 change and one initial Level 2
  duplication of repository parsing in the adapter engine; the duplication was
  removed so ``SYSP_SPEC_INSTALLER_GITHUB_SOURCE`` is the sole design owner.
* ``uv run python docs/test_docs_build.py`` passes all 4 tests.
* ``uv run python docs/docs-build.py clean`` succeeds with zero Sphinx and
  schema warnings.
* ``uv run --python 3.11 --with-requirements docs/requirements.txt python -m
  unittest discover -s tests -v`` completes normally: 60 tests pass in
  140.613 seconds with two documented opt-in skips. This run does not implement
  or clear the new Round 6 UAT; the complete suite and new scenarios must run
  again after implementation, and any later abrupt run remains failed evidence.

#### Round 6 Implementation Resolution

**Implemented:** The deterministic runtime and executable UAT now implement all
six Round 6 correction areas while preserving the selected-harness, shared-path,
linked-worktree, native-routing, bounded-checkpoint, and uv-only behavior from
Rounds 3-5.

* OpenCode commands contain exactly ``$ARGUMENTS`` plus one terminal newline.
  Fixture and real-product assertions inspect generated bytes, while the live
  OpenCode probe invokes the native command with a multi-token punctuation-
  bearing request, observes the exact payload, and separately observes one
  native ``task`` event to ``syspilot.implement`` with ``ENGINEER_OK`` and
  ``MANAGER_OK`` results.
* Checkpoints use one host-normalized canonical key for serialized entries,
  expected-current identities, and restoration. Case-preserving
  ``display_paths`` remain separate. Windows mixed-case restore completes
  without lookup failure or checkpoint residue.
* Supplied checkpoints bind a UUID nonce, complete canonical mutable-path set,
  per-path filesystem identity/content fingerprints, and exact HEAD/ref/index
  handoff state. Freshness is recomputed immediately before execution; modified,
  created, deleted, Git-moved, nonce-tampered, and fingerprint-tampered fixtures
  reject without mutation.
* Rollback records the Installer-created commit and post-commit index, then uses
  expected-old-OID ``git update-ref`` operations for attached, unborn, detached,
  and linked-worktree state. Concurrent commits remain reachable, concurrent
  index state is preserved, safe owned paths are restored, and the result
  reports an incomplete rollback conflict.
* Mutation operations capture filesystem object identity and revalidate
  ancestry immediately before temporary-file creation, replacement, deletion,
  and restoration. Windows identity uses no-follow ``CreateFileW`` handles,
  reparse rejection, and volume/file IDs. Deterministic ordinary-directory and
  real-junction swaps fail closed without modifying external sentinels.
* Public repository parsing occurs before filesystem lookup and accepts only
  ``owner/repository`` or supported GitHub HTTPS URLs. Relative shadows, local
  absolute paths, ``file:`` URLs, credentials, queries/fragments, non-HTTPS,
  and non-GitHub hosts reject; ``SourceSnapshot.from_directory`` remains the
  internal fixture boundary.
* RED evidence reproduced empty OpenCode command bodies, local-source shadowing,
  accepted stale checkpoints, mixed-case restore loss, unconditional Git ref
  rewind, and mutation-boundary ancestry swaps. Each correction passed its
  focused GREEN check before the next implementation slice.
* The release-equivalent suite completed normally with 77 tests in 180.129
  seconds and one conditional GitHub rate-limit skip; that run included the
  opt-in live OpenCode UAT. The 500-file unrelated-tree fixture kept checkpoint
  size below 32 KiB and created no worker thread. All checkpoint artifacts from
  normal, conflict, race, and intentionally corrupted fixtures are cleaned.
* Documentation tests pass 4/4. The clean Sphinx build succeeds with zero
  schema warnings, and editor diagnostics report no implementation or test
  errors.
* Runtime note: OpenCode 1.17.4 parses the generated command ``agent`` route,
  but its noninteractive ``--command`` path did not consistently select that
  agent. Live evidence therefore invokes the native command with an explicit
  matching ``--agent syspilot.cm``; native command substitution and Manager
  delegation both pass, while command-only CLI route selection remains an
  upstream harness caveat rather than an Installer configuration error.

### Round 7

**Reviewed by:** QM
**Review date:** 2026-09-17
**Commit reviewed:** ``15e3392``
**Overall disposition:** Quality is not cleared. L0 is clean, but one high and
one medium security/implementation alignment finding remain in the declared
Round 6 scope.

#### L0 MECE

**Status:** PASS

``SYSP_US_HARNESS_PORTABILITY`` owns equivalent native command behavior and
``SYSP_US_INSTALLER`` owns installation transaction safety and source policy.
No overlap, contradiction, or uncovered Round 6 intent was found.

#### L1 MECE

**Status:** FAIL

| # | Element ID | Finding | Severity |
|---|------------|---------|----------|
| 1 | ``SYSP_REQ_INSTALLER_ROLLBACK`` AC-12 | The requirement rejects a reused supplied checkpoint, but the runtime records no nonce-consumption state. A copied checkpoint artifact can be restored under the same identifier and accepted again whenever owned-path and Git fingerprints still match. The test suite covers nonce alteration only, not nonce reuse/replay. | medium |

Other Round 6 L1 ownership remains mutually exclusive and collectively
exhaustive: workflow reliability, GitHub source grammar, direct mutation
operations, and rollback state each have one normative owner.

#### L2 MECE and Implementation Alignment

**Status:** FAIL

| # | Element ID | Finding | Severity |
|---|------------|---------|----------|
| 2 | ``SYSP_SPEC_INSTALLER_DIRECT_OPS`` | The design requires descriptor-relative POSIX mutation with ``dir_fd``/``*at`` and ``O_NOFOLLOW`` where available. ``_atomic_write``, ``_safe_delete``, and rollback still perform final ``os.replace``, ``Path.unlink``/``rmdir``, and file reads by pathname after identity checks. No descriptor-relative primitive exists. A parent can therefore be exchanged after the last check and before the final pathname operation on supported POSIX hosts; deterministic hooks test swaps before revalidation, not this remaining check-to-operation window. | high |
| 3 | ``SYSP_SPEC_INSTALLER_SUPPLIED_CHECKPOINT`` / ``SYSP_SPEC_INSTALLER_ROLLBACK`` | The nonce/binding implementation is replayable and not tamper-authenticating: ``binding`` is an unkeyed SHA-256 over attacker-editable checkpoint fields, and no consumed-nonce registry or one-time handoff state exists. This does not implement the specified rejection of reused checkpoints and lets a writer recompute a valid binding after changing the artifact. | medium |

No additional L2 overlap, gap, or contradiction was found in the scoped Round
6 elements. Finding 3 is the L2 manifestation of L1 Finding 1, not an
independent requirement gap.

#### Vertical Trace

**Status:** PASS

Fresh impact queries resolve ``SYSP_US_HARNESS_PORTABILITY`` and
``SYSP_US_INSTALLER`` to their scoped requirements, and resolve
``SYSP_REQ_INSTALLER_DIRECT_OPS`` and ``SYSP_REQ_INSTALLER_ROLLBACK`` to the
Installer engine, workflow, rollback, and supplied-checkpoint designs. No
broken link or orphan was found in the reviewed chain.

#### Schema and Executable Evidence

**Status:** PASS with one documented opt-in integration skip

* ``uv run --python 3.11 --with-requirements docs/requirements.txt python -m
  unittest discover -s tests -v`` completed normally: 77 tests passed in
  205.244 seconds, with one conditional GitHub API integration skip.
* ``uv run --python 3.11 --with-requirements docs/requirements.txt python -m
  unittest docs.test_docs_build -v`` passed all 4 tests.
* ``uv run --python 3.11 --with-requirements docs/requirements.txt python
  docs/docs-build.py clean`` succeeded with zero Sphinx warnings and zero
  schema warnings across 8,310 needs.
* ``git diff --check`` reported no whitespace errors before this report was
  appended.

#### Findings Report to PM

Quality is not cleared at ``15e3392``. PM disposition is required for Findings
1-3. The recommended fix-now scope is: implement POSIX descriptor-relative
no-follow mutation primitives and a one-time, authenticity-protected supplied-
checkpoint handoff, then add race-window and replay fixtures and rerun the full
gate.

#### PM Decisions

**Decision date:** 2026-09-17

| # | QM finding(s) | Decision | Rationale |
|---|---------------|----------|-----------|
| 1 | L2 Finding 2 | fix-now | Pathname-based mutation leaves a security-relevant race window that conflicts with the accepted descriptor-relative no-follow contract. POSIX mutations must satisfy that contract before quality can be cleared. |
| 2 | L1 Finding 1 / L2 Finding 3 | fix-now | A supplied checkpoint that can be replayed or modified with a recomputed binding does not provide the required one-time, tamper-authenticating handoff. Nonce consumption and binding authenticity must be enforced before quality can be cleared. |

L1 Finding 1 and L2 Finding 3 are two levels of the same checkpoint issue and
therefore receive one PM decision.

### Round 7 Specification Resolution

**Status:** Design and UAT corrections approved after impact, MECE, trace, and
documentation validation; implementation is not modified in this round.

#### Resolved Design Elements

| ID | Correction |
|----|------------|
| `SYSP_SPEC_INSTALLER_DIRECT_OPS` | POSIX write, replace, delete, cleanup, and restore operations are descriptor-relative from opened target/parent directory descriptors, use `O_DIRECTORY`/`O_NOFOLLOW` where available, reject symlink ancestry, and have no pathname-revalidation fallback. Windows retains its existing handle identity and reparse-point checks. |
| `SYSP_SPEC_INSTALLER_ROLLBACK` | Supplied and direct internal checkpoints use opaque, expiring, authenticity-protected transaction identifiers backed by trusted state outside the target and an atomic one-time consume lease. |
| `SYSP_SPEC_INSTALLER_SUPPLIED_CHECKPOINT` | Authentication binds target identity, canonical plan, owned-path and Git fingerprints, and creation/expiry time to a runtime secret or signed/HMAC token; tamper, expiry, concurrent use, and replay reject before mutation. |
| `SYSP_US_UAT_INSTALLER_SPEC_REWRITE` / `SYSP_REQ_UAT_INSTALLER_SPEC_REWRITE` / `SYSP_SPEC_UAT_INSTALLER_SPEC_REWRITE` | Added deterministic late POSIX ancestry swaps with syscall evidence and external sentinels, plus supplied/internal token tamper, expiry, atomic lease, and replay fixtures. |

#### Decisions

1. POSIX path revalidation is not a substitute for descriptor-relative
  mutation. Unsupported descriptor/no-follow primitives fail closed before
  mutation. Windows remains governed by the already-specified handle/reparse
  checks and its documented last-moment identity fallback.
2. Checkpoint identifiers are capabilities, not caller-verifiable manifests.
  Authentication and consume state live outside the caller-controlled target;
  no long-lived secret is written there. The same lifecycle applies to direct
  internal and caller-supplied checkpoints.
3. Atomic lease/consume occurs before the first target or Git mutation. Every
  attempt retires the identifier, so concurrent use and replay after either
  success or failure cannot authorize another transaction.

#### Implementation Tasks

1. Replace POSIX pathname-based atomic write, replace, unlink/rmdir, cleanup,
  and rollback calls with target/parent-dirfd-relative primitives; open each
  ancestry component with no-follow/directory flags and fail closed when the
  host lacks a required primitive.
2. Add deterministic hooks after final POSIX ancestry validation and before
  each mutation/restore primitive; assert syscall anchoring and byte-exact
  preservation of external sentinels.
3. Replace caller-recomputable checkpoint bindings with opaque authenticated
  transaction IDs backed by runtime-secret or signed/HMAC trusted state
  outside the target, bound to target, plan, state, Git, and time/expiry.
4. Implement atomic pre-mutation lease/consume and terminal retirement for
  supplied and direct internal checkpoints; reject missing, expired, tampered,
  concurrently leased, consumed, or replayed IDs before mutation.
5. Add supplied/internal checkpoint tests for field tampering with recomputed
  unkeyed hashes, expiry, concurrent acquisition, replay after success, replay
  after failure, and absence of long-lived target-resident secrets.

#### MECE, Trace, and Validation

- [x] Mandatory impact queries from `SYSP_REQ_INSTALLER_DIRECT_OPS` and
  `SYSP_REQ_INSTALLER_ROLLBACK` identified the Installer engine, workflow,
  rollback, supplied-checkpoint, and UAT consumers; no additional spec owner is
  required.
- [x] L2 MECE advisory passes: platform mutation primitives, transaction token
  lifecycle, and supplied-token acceptance checks have distinct owners and
  collectively cover both Round 7 findings without contradiction.
- [x] Refreshed two-level trace queries resolve each modified design through
  `SYSP_REQ_INSTALLER_DIRECT_OPS` or `SYSP_REQ_INSTALLER_ROLLBACK` to
  `SYSP_US_INSTALLER`; the UAT design links directly to both modified behavior
  owners and through its UAT requirement/story chain.
- [x] `uv run python docs/test_docs_build.py` passes all 4 tests.
- [x] `uv run python docs/docs-build.py clean` succeeds with zero Sphinx or
  schema warnings before approval.
- [x] No implementation file is modified in this specification round.

### Round 7 Implementation

**Implemented by:** Dev Engineer
**Implementation date:** 2026-09-17
**Base commit:** `9236698`

#### Implemented Elements

| ID | Implementation |
|----|----------------|
| `SYSP_SPEC_INSTALLER_DIRECT_OPS` | Added POSIX target/parent descriptor chains opened with `O_DIRECTORY` and `O_NOFOLLOW`; write, temporary creation, replace, unlink, directory creation/removal, cleanup, and restore use `dir_fd` operations and fail closed when required primitives are unavailable. Existing Windows handle identity and reparse-point behavior remains active. |
| `SYSP_SPEC_INSTALLER_ROLLBACK` | Added opaque UUID checkpoints with per-transaction HMAC secrets in protected OS temporary storage, authenticated target/plan/path/Git/time state, expiry, bounded stale cleanup, atomic `O_EXCL` leases, and terminal retirement after success or failure. |
| `SYSP_SPEC_INSTALLER_SUPPLIED_CHECKPOINT` | Added exact canonical plan-digest validation, pre-mutation single-use consumption, tamper/expiry/concurrency/replay rejection, and direct internal use of the same state machine. |
| `SYSP_SPEC_UAT_INSTALLER_SPEC_REWRITE` | Added deterministic tamper, expiry, concurrent claimant, replay, cross-process handoff, secret-location, bounded-cleanup, and POSIX late ancestry-swap/syscall tests. |

#### Implementation Evidence

* TDD RED evidence showed caller-recomputed SHA-256 tamper was accepted, no
  lease primitive existed, and the public CLI lacked cross-process checkpoint
  creation/consumption. Each focused test passed after its implementation.
* The fresh release-equivalent suite ran 93 tests in 131.772 seconds: 87 passed
  with six explicit environment skips, five POSIX-only descriptor probes on the
  Windows implementation host and one GitHub API rate-limit integration skip.
  OpenCode generated configuration and live command/delegation tests passed.
* Documentation tests pass 4/4. The clean Sphinx build succeeds with zero
  Sphinx or schema warnings. Editor diagnostics report no implementation,
  test, Setup, or documentation errors.
* Checkpoint lifecycle probes leave no JSON, HMAC key, or lease residue. The
  POSIX probes are committed and conditionally executable; native execution was
  unavailable because this Windows host has no WSL, Docker, Podman, or POSIX
  shell runtime.

### Round 8

**Reviewed by:** QM
**Review date:** 2026-09-17
**Commit reviewed:** ``29607ba``
**Overall disposition:** Quality is not cleared. L0, trace, and schema checks
pass. The POSIX descriptor-relative implementation has adequate static evidence
but remains conditionally unexecuted on this Windows host. One single-use token
defect and one prior-round status regression remain.

#### L0 MECE

**Status:** PASS

``SYSP_US_HARNESS_PORTABILITY`` continues to own equivalent native command
behavior and ``SYSP_US_INSTALLER`` owns installation transaction safety and
source policy. Round 7 introduces no L0 overlap, contradiction, or uncovered
intent.

#### L1 MECE

**Status:** FAIL

| # | Element ID | Finding | Severity |
|---|------------|---------|----------|
| 1 | ``SYSP_REQ_INSTALLER_ROLLBACK`` AC-12 | A supplied identifier is not retired when an install attempt fails at the dependency gate or while building the frozen plan. ``install_snapshot`` returns before ``_lease_checkpoint`` and before the only retirement block, so the same authenticated checkpoint remains valid for a later attempt. The failed-attempt replay test injects failure only after lease acquisition and does not cover either pre-lease path. This contradicts rejection of a reused checkpoint. | high |

Other scoped L1 ownership remains mutually exclusive and collectively
exhaustive. Finding 1 is an implementation-alignment defect, not a missing
requirement.

#### L2 MECE and Implementation Alignment

**Status:** FAIL

| # | Element ID | Finding | Severity |
|---|------------|---------|----------|
| 2 | ``SYSP_SPEC_INSTALLER_SUPPLIED_CHECKPOINT`` | The design says the same identifier cannot be accepted after any prior attempt, but pre-lease dependency and plan failures leave the JSON/key pair intact and reusable. Token retirement begins only after plan construction reaches ``_lease_checkpoint``. Add pre-lease replay fixtures and retire a supplied identifier on every terminal attempt path without allowing an unvalidated identifier to delete another transaction's trusted state. | high |
| 3 | ``SYSP_SPEC_INSTALLER_ROLLBACK`` / ``SYSP_SPEC_INSTALLER_SUPPLIED_CHECKPOINT`` | Both production checkpoint specifications remain ``approved`` after Round 7 records them as implemented and the executable checkpoint suite passes. This regresses Round 5 Finding 8's lifecycle-status correction. Transition independently verified production behavior to ``implemented``; keep the POSIX-dependent direct-operations/UAT status at ``approved`` until native execution or equivalent independent evidence exists. | medium |

Finding 2 is the L2 manifestation of L1 Finding 1, not a separate root cause.
No additional L2 MECE gap or contradiction was found.

#### POSIX No-Follow Assessment

**Status:** STATIC PASS; NATIVE RUNTIME NOT EXECUTED

The reviewed implementation opens the target root and each ancestry component
with ``O_DIRECTORY`` and ``O_NOFOLLOW``, verifies frozen directory identities,
and performs temporary creation, replace, mkdir, unlink, rmdir, cleanup, and
restore through ``dir_fd`` operations. Late-swap fixtures inject after final
pathname identity validation and assert that replace/delete/cleanup/restore
remain anchored to the already-open parent descriptor while external sentinels
remain unchanged. Capability checks fail closed when required flags or
``supports_dir_fd`` entries are absent. This is adequate static implementation
evidence, but the five POSIX-only tests were skipped on Windows; no native POSIX
runtime claim is cleared by execution in this round.

#### Vertical Trace

**Status:** PASS

Fresh inbound depth-1 trace from ``SYSP_US_INSTALLER`` resolves the scoped
requirements. Depth-2 traces from ``SYSP_REQ_INSTALLER_DIRECT_OPS`` and
``SYSP_REQ_INSTALLER_ROLLBACK`` resolve the Installer engine, workflow,
direct-operations, rollback, supplied-checkpoint, harness-target, and UAT
consumers. No broken link or orphan was found.

#### Schema and Executable Evidence

**Status:** PASS with six conditional skips

* The full suite completed normally: 93 tests ran in 242.604 seconds, 87 passed,
  and six were conditionally skipped (five POSIX-only descriptor tests and one
  GitHub API rate-limit integration test).
* Documentation tests passed 4/4.
* The clean documentation build succeeded with zero Sphinx warnings and zero
  schema warnings across 6,309 needs.
* ``git diff --check`` reported no whitespace errors for the reviewed commit.

#### Findings Report to PM

Quality is not cleared at ``29607ba``. PM disposition is required for Findings
1-3. The recommended fix-now scope is to consume or safely retire a supplied
checkpoint identifier on dependency and plan-construction failure, add replay
tests for both pre-lease paths (including a separate-process retry), and align
the independently verified checkpoint specification statuses. Native POSIX
execution remains a conditional evidence gap, not an additional code finding.

#### PM Decisions

**Decision date:** 2026-09-17

| # | QM finding(s) | Decision | Rationale |
|---|---------------|----------|-----------|
| 1 | L1 Finding 1 / L2 Finding 2 | fix-now | Pre-lease dependency and frozen-plan failures must not leave a supplied checkpoint identifier reusable. Every terminal attempt path must preserve the required single-use behavior before quality can be cleared. |
| 2 | L2 Finding 3 | fix-now | Independently verified production checkpoint specifications must reflect their implemented lifecycle state. The descriptor-relative direct-operations design may also become ``implemented`` because its implementation exists; native POSIX UAT remains ``approved`` and conditional pending execution on a capable host. |

L1 Finding 1 and L2 Finding 2 are two levels of the same checkpoint reuse
defect and therefore receive one PM decision. The POSIX static evidence is
accepted provisionally for this correction round because no native POSIX
runtime is available; it is not accepted as production proof.

#### System Designer Round 8 Resolution

**Resolution date:** 2026-09-17

No L0 change is required. ``SYSP_US_INSTALLER`` already owns transactional
installation safety, and ``SYSP_US_HARNESS_PORTABILITY`` already owns
cross-harness portability. Their boundary remains MECE.

At L1, ``SYSP_REQ_INSTALLER_ROLLBACK`` AC-12 now requires every public attempt
with a supplied checkpoint identifier to atomically consume its capability, or
acquire a lease that is terminally revoked on every failure path, before
dependency resolution, source acquisition or parsing, plan construction,
root/plan matching, and freshness validation. Cleanup and forensic records may
survive only when they cannot authorize replay or affect another transaction's
trusted state.

At L2, ``SYSP_SPEC_INSTALLER_ROLLBACK`` and
``SYSP_SPEC_INSTALLER_SUPPLIED_CHECKPOINT`` define the same attempt-entry
consume/revoke boundary and forbid reuse after dependency, source, parse, plan,
root-mismatch, plan-mismatch, freshness, or later failure. Both transition to
``implemented`` based on the independently verified checkpoint implementation.
``SYSP_SPEC_INSTALLER_DIRECT_OPS`` also transitions to ``implemented`` because
the descriptor-relative POSIX implementation exists and passed Round 8 static
implementation review. This lifecycle status is not a claim of native POSIX
runtime proof.

``SYSP_REQ_UAT_INSTALLER_SPEC_REWRITE`` and
``SYSP_SPEC_UAT_INSTALLER_SPEC_REWRITE`` add separate dependency, source
acquisition, source parse, formerly pre-lease plan, and malformed-input failure
fixtures. Each case retries the same identifier from a separate process and
requires replay rejection, zero target/Git mutation, no authorizing checkpoint
residue, and isolation of unrelated trusted state. Native POSIX
descriptor-relative scenarios remain ``approved``, conditional, and unexecuted
on this Windows host.

Impact discovery from ``SYSP_US_INSTALLER`` at inbound depth 1 and from
``SYSP_REQ_INSTALLER_ROLLBACK`` and ``SYSP_REQ_INSTALLER_DIRECT_OPS`` at inbound
depth 2 confirms that the modified requirement, production designs, and UAT
contracts are the controlling traceability chain. No new element or link is
required.

**Validation evidence:**

* L0/L1 MECE re-check passes: transactional supplied-checkpoint lifecycle
  remains owned by ``SYSP_US_INSTALLER`` and
  ``SYSP_REQ_INSTALLER_ROLLBACK``; the UAT requirement supplies test data and
  does not duplicate production behavior.
* Fresh inbound impact/trace queries resolve rollback to its workflow,
  rollback, supplied-checkpoint, harness-target, and soul consumers; direct
  operations additionally resolves the deterministic-runtime UAT consumer.
* The UAT chain resolves
  ``SYSP_US_UAT_INSTALLER_SPEC_REWRITE`` ->
  ``SYSP_REQ_UAT_INSTALLER_SPEC_REWRITE`` ->
  ``SYSP_SPEC_UAT_INSTALLER_SPEC_REWRITE`` with all three elements
  ``approved``.
* A clean warnings-as-errors Sphinx build succeeds with zero schema warnings.
* Native POSIX UAT was not executed on this Windows host and remains an open
  conditional evidence item; no runtime-pass claim is made.

#### Round 8 Implementation Resolution

**Implemented by:** Dev Engineer
**Implementation date:** 2026-09-17
**Base commit:** ``23eaae6``

``SYSP_SPEC_INSTALLER_ROLLBACK`` and
``SYSP_SPEC_INSTALLER_SUPPLIED_CHECKPOINT`` are implemented through one
attempt-entry checkpoint state machine. A public invocation atomically creates
an ``O_EXCL`` lease before dependency resolution, source acquisition, parse,
transform, containment, plan construction, or public input validation. The
successful claimant alone gains cleanup authority and carries the authenticated
checkpoint into pre-mutation target, plan, path, Git, and freshness validation.
Every return, rejection, exception, or cancellation owned by that claimant
retires the checkpoint JSON, HMAC key, and lease. A losing concurrent process
cannot delete the winner's trusted state, and malformed identifier text cannot
nominate or retire another transaction.

Direct internal installation remains plan-first: it creates a bounded
checkpoint only after the frozen plan validates, then enters the same
authenticated lease, validation, rollback, and terminal-cleanup state machine.
Public CLI behavior remains production-only for VS Code and OpenCode. When a
supplied checkpoint accompanies a malformed harness, the invocation reaches
the attempt gate before returning a structured rejection; tokenless malformed
harness input retains the existing parser rejection.

TDD RED evidence reproduced successful replay after dependency and source
acquisition failure, an empty branch reaching GitHub instead of deterministic
validation, parser-level malformed-harness rejection before token consumption,
and cancellation leaving the HMAC key behind. A full-suite process race also
exposed a losing claimant attempting to remove a Windows-open artifact owned by
the winner; cleanup authority was narrowed to the successful claimant.

GREEN coverage now includes dependency, source acquisition, YAML parse,
transformation, containment, malformed repository/branch/harness, target-root,
mutable-path, plan-content, and freshness failures followed by fresh-process
replay rejection. Existing and extended fixtures cover malformed/tampered/
expired tokens, direct and supplied replay, cross-process handoff, and an
exactly-one-winner process race. All pre-mutation cases preserve target bytes,
HEAD, index, and unrelated trusted state while leaving no authorizing JSON,
HMAC key, or lease residue.

The focused Installer module runs 105 tests: 99 pass and six are conditional
environment skips (five POSIX descriptor probes and one GitHub API rate-limit
integration probe). Editor diagnostics report no errors in the implementation
or test files.

Release-equivalent verification reran all 105 repository tests: 99 passed and
six conditional tests were skipped (five POSIX descriptor probes and one
GitHub API rate-limit integration probe). The installed OpenCode executable
passed the isolated native ``debug config`` fixture. The opt-in live OpenCode
delegation test was not rerun because checkpoint lifecycle changes do not alter
generated routing. All four documentation tests pass, and a clean Sphinx build
validates 8,426 needs with zero schema warnings.
Implementation and test files have no editor diagnostics; the only workspace
diagnostics are unrelated marketplace-resolution warnings for two existing
release-workflow actions.

### Round 9 — Final Independent Quality Gate

**Reviewed by:** QM
**Review date:** 2026-09-17
**Commit reviewed:** ``4666a0cf45e231109dddd8f6f7444953190b78ae``
**Overall disposition:** **CLEARED.** No confirmed high- or medium-severity
defect remains in the declared harness-interop scope or in the Round 2-8
correction chain.

#### L0 MECE

**Status:** PASS

``SYSP_US_HARNESS_PORTABILITY`` owns equivalent behavior, native routing, and
shared methodology semantics. ``SYSP_US_HARNESS_INSTALL`` and
``SYSP_US_INSTALLER`` own native installation and transactional safety, while
``SYSP_US_SETUP`` owns the installed update entry point. The Round 2-8
corrections leave no overlap, contradiction, or uncovered acceptance intent at
Level 0. Production support remains limited to VS Code GitHub Copilot and
OpenCode; Claude Code and Qoder remain explicitly experimental.

#### L1 MECE

**Status:** PASS

The Level 1 ownership split remains mutually exclusive and collectively
exhaustive: behavioral equivalence, content single-source, native install and
update, GitHub-only acquisition, uv-only execution, installation scope,
mutation containment, workflow ordering, and rollback each retain a distinct
normative owner. ``SYSP_REQ_INSTALLER_ROLLBACK`` AC-12 now matches the runtime:
every public supplied-checkpoint attempt claims the capability before harness,
branch, dependency, source, parse, transform, containment, plan, root, or
freshness validation, and claimant-owned terminal cleanup prevents replay.

#### L2 MECE and Implementation Alignment

**Status:** PASS

``SYSP_SPEC_INSTALLER_DIRECT_OPS`` separately owns platform mutation
primitives; ``SYSP_SPEC_INSTALLER_ROLLBACK`` owns transaction and Git
compare-and-swap restoration; and
``SYSP_SPEC_INSTALLER_SUPPLIED_CHECKPOINT`` owns authenticated one-time
handoff validation. All three production designs are ``implemented``. Static
review confirms HMAC-SHA-256 binding with a 32-byte runtime secret outside the
target, UUID-v4-constrained trusted-state paths, atomic ``O_EXCL`` leasing,
claimant-only retirement, bounded stale cleanup, exact canonical plan/path/Git
binding, and terminal cleanup across ordinary exceptions and cancellation.

The POSIX implementation opens root and ancestry with ``O_DIRECTORY`` and
``O_NOFOLLOW`` and performs create, replace, mkdir, unlink, rmdir, cleanup, and
restore through ``dir_fd`` operations. Windows containment retains reparse
rejection, handle identity checks, immediate parent revalidation, and race
fixtures. Rollback uses expected-old-OID Git ``update-ref`` compare-and-swap,
supports attached, detached, unborn, and linked-worktree state, and preserves
concurrent ref/index/path changes as reported conflicts. Checkpoint work and
cleanup are bounded by declared paths and configured limits.

OpenCode output preserves ``$ARGUMENTS`` and source-agent routing, installs
harness-neutral shared Skill/template paths, and uses the native Task binding.
Public acquisition accepts GitHub repository identifiers or supported GitHub
HTTPS URLs only. The selected-harness boundary, uv-only runtime, production
status matrix, and UAT status boundaries remain aligned.

#### Vertical Trace

**Status:** PASS

Fresh inbound depth-1 queries resolve ``SYSP_US_HARNESS_PORTABILITY`` and
``SYSP_US_INSTALLER`` to their scoped requirements. Depth-2 queries resolve
``SYSP_REQ_INSTALLER_ROLLBACK`` and ``SYSP_REQ_INSTALLER_DIRECT_OPS`` to the
Installer workflow, engine, rollback, supplied-checkpoint, harness-target, and
deterministic-runtime UAT consumers. No broken link or orphan was found.

#### Schema, Tests, and Adversarial Evidence

**Status:** PASS with explicit residual risks

* Ten focused supplied-checkpoint tests pass for dependency/source/parse/
  transform/containment/malformed-input failures, cancellation, fresh-process
  replay rejection, and exactly-one-winner cross-process leasing.
* The first release-equivalent run exposed one live OpenCode delegation failure
  with exit code 1 and empty stderr. The same native UAT passed in isolation,
  and the complete suite was rerun as required by the reliability gate.
* The fresh complete rerun passed: 105 tests in 202.797 seconds, with six
  conditional skips. Live OpenCode 1.17.4 command forwarding and native
  Manager-to-implementer Task delegation passed in that complete rerun.
* Documentation tests pass 4/4. A clean warning-as-error Sphinx build succeeds
  with zero schema warnings across 5,366 needs. Editor diagnostics are empty
  for all touched implementation, test, requirement, and design files.
* ``git diff --check`` passes and verification leaves the reviewed worktree
  clean before this quality-only report is appended.

#### Residual Risks

1. Five POSIX descriptor-relative tests remain unexecuted because this Windows
   host has no WSL, Docker, Podman, or native POSIX runtime. Static review found
   no defect, so this is an explicitly unvalidated portability risk rather than
   an implementation finding.
2. The real GitHub API acquisition test reached ``api.github.com`` but was
   conditionally skipped after HTTP 403 rate limiting. Unit coverage verifies
   immutable revision use, inventory validation, GitHub-only grammar, and raw
   fetch construction; live network availability remains externally limited.
3. Claude Code and Qoder remain experimental and do not contribute production
   acceptance evidence.

#### Findings Report to PM

No high-, medium-, or low-severity finding remains open in the scoped final
gate. Harness-interop is **CLEARED** at reviewed commit
``4666a0cf45e231109dddd8f6f7444953190b78ae``, subject to the residual risks
above.

### Round 10 — Claude Code Direct Acceptance Finding

**Reviewed by:** QM
**Review date:** 2026-09-17
**Commit reviewed:** ``589d324``
**Overall disposition:** Quality is no longer cleared. The direct Claude Code
acceptance finding requires immediate correction on the existing feature
branch before another Quality review.

#### Finding and PM Decision

| # | Severity | Finding | Decision | PM rationale |
|---|----------|---------|----------|--------------|
| 1 | High | Claude Code CLI 2.1.274 skips all 13 generated project subagents because Claude requires both ``name`` and ``description`` frontmatter, while the current adapter emits only ``description``. Claude names permit lowercase letters and hyphens, whereas syspilot source IDs are dotted. In the test project, ``claude --agent syspilot.qm`` reports the agent as not found; manually adding ``name: syspilot-qm`` advances invocation to the authentication gate, demonstrating native discovery. Manager Agent allowlist references and methodology binding references must use the same dotted-source-ID to hyphenated-Claude-name mapping. | fix-now | Native discovery is a prerequisite for Claude acceptance, and inconsistent identity mapping would leave delegation and methodology bindings unresolved even after discovery is repaired. Correct the complete Claude identity mapping and its acceptance evidence before quality can be cleared. Claude remains experimental until authenticated live UAT succeeds. |

#### Required Acceptance Outcome

All 13 generated Claude project subagents are natively discoverable under
valid hyphenated names derived deterministically from their dotted syspilot
source IDs. Manager Agent allowlists and methodology binding references resolve
those same generated names. Claude Code remains classified as experimental
until authenticated live invocation and delegation UAT pass and are recorded.

### Round 10 — Claude Discovery Design Correction

**Status:** Design and UAT specifications corrected, validated, and approved.

#### Impact Scope

Mandatory inbound impact queries against refreshed ``needs.json`` found no
need for a new User Story, Requirement, Design, or UAT ID. The correction is
owned by the existing harness-agent, orchestration, limitations, and
installer-target chains.

| Level | Modified IDs |
|-------|--------------|
| Design | ``SYSP_SPEC_HARNESS_AGENT_ADAPTER``, ``SYSP_SPEC_HARNESS_ORCHESTRATION_ADAPTER``, ``SYSP_SPEC_HARNESS_LIMITATIONS`` |
| UAT stories | ``SYSP_US_UAT_HARNESS_AGENT_ADAPTER``, ``SYSP_US_UAT_HARNESS_ORCHESTRATION_ADAPTER``, ``SYSP_US_UAT_HARNESS_LIMITATIONS``, ``SYSP_US_UAT_INSTALLER_HARNESS_TARGETS`` |
| UAT requirements | ``SYSP_REQ_UAT_HARNESS_AGENT_ADAPTER``, ``SYSP_REQ_UAT_HARNESS_ORCHESTRATION_ADAPTER``, ``SYSP_REQ_UAT_HARNESS_LIMITATIONS``, ``SYSP_REQ_UAT_INSTALLER_HARNESS_TARGETS`` |
| UAT designs | ``SYSP_SPEC_UAT_HARNESS_AGENT_ADAPTER``, ``SYSP_SPEC_UAT_HARNESS_ORCHESTRATION_ADAPTER``, ``SYSP_SPEC_UAT_HARNESS_LIMITATIONS``, ``SYSP_SPEC_UAT_INSTALLER_HARNESS_TARGETS`` |

#### Decisions

1. **Native identity:** the canonical source ID comes from
   ``syspilot.<role>.agent.md``. Claude frontmatter SHALL contain required
   ``name: syspilot-<role>`` and the source ``description``. Filename mapping
   may remain target-specific, but it never supplies Claude identity. A file
   without ``name`` is skipped as documentation.
2. **Manager tool binding:** a Manager running as the Claude main thread maps
   a nonempty source ``agents`` allowlist to an explicit
   ``Agent(<native-name>, ...)`` tools entry. Other required tools use an
   approved native mapping or inheritance. Bare ``Agent`` permits unrestricted
   spawn; nested subagents follow Claude's documented Agent-tool semantics and
   are not falsely described as having enforced per-target restrictions.
3. **Structural binding adaptation:** only dotted identity/tool-binding
   references in Workflow and the orchestration native-binding section may be
   changed to Claude native names. Every other methodology byte and semantic
   remains unchanged. This deterministic native wiring is structural binding
   adaptation, not content drift.
4. **User invocation:** Claude users invoke Setup, PM, QM, and CM as
   ``syspilot-setup``, ``syspilot-pm``, ``syspilot-qm``, and
   ``syspilot-cm`` respectively, including CLI form
   ``claude --agent <native-name>``.
5. **Acceptance boundary:** static checks require exactly 13 valid unique
   names and complete resolution of all allowlist and Workflow/orchestration
   binding references. Run ``claude plugin validate .claude/agents`` only if
   the installed CLI accepts that directory as a validation target.
   ``claude --agent syspilot-qm`` must pass discovery and reach authentication
   or model execution; agent-not-found fails discovery, while authentication
   failure is recorded as an external blocked result. Claude remains
   experimental until authenticated invocation and Manager-to-Engineer
   delegation pass.

#### Superseded Statements

This correction supersedes the earlier Round 2/implementation statements that
Claude omits native ``name``, has only a prose SEND allowlist, or preserves
agent bodies byte-for-byte without a structural-binding exception. Those
statements remain above as historical audit evidence and are not current
design authority.

#### MECE and Trace Check

- [x] Existing owners cover identity, Agent-tool binding, limitation
  disclosure, and runtime acceptance without adding overlapping elements.
- [x] The former blanket Claude allowlist limitation is narrowed to the nested
  enforcement boundary; main-thread restriction and nested semantics no longer
  contradict one another.
- [x] Agent content preservation has one explicit exception owner:
  deterministic identity/tool-binding references only.
- [x] Requirement-to-Design impact and Design second-order consumer queries
  identify the existing adapter, limitations, installer, and UAT scope; no
  orphan or missing owner is introduced.
- [x] Fresh depth-1 bidirectional queries resolve all 15 modified Design/UAT
  elements to their immediate traceability context.
- [x] ``uv run python docs/test_docs_build.py`` passes all 4 tests and
  ``git diff --check`` reports no whitespace errors.

#### Remaining Tasks

- Implement the corrected Claude adapter and update executable fixtures.
- Execute static 13-name and reference-resolution checks.
- Execute Claude CLI discovery and record authentication separately from
  not-found.
- Execute authenticated invocation and Manager-to-Engineer delegation before
  proposing Claude production support.
- Re-run Quality review after implementation and UAT evidence are committed.

### Round 10 Implementation

**Implemented by:** Dev Engineer
**Implementation date:** 2026-09-17
**Base commit:** ``aa7838d``

``SYSP_SPEC_HARNESS_AGENT_ADAPTER`` now derives each Claude identity from its
validated ``syspilot.<role>.agent.md`` source path and emits the required
``name: syspilot-<role>`` plus source description. User-invocable Managers map
their complete source allowlists into one explicit
``Agent(<native-name>, ...)`` tools entry. Nested spawning subagents retain
Claude's documented bare ``Agent`` behavior, while leaf agents receive no
spawn tool.

``SYSP_SPEC_HARNESS_ORCHESTRATION_ADAPTER`` now emits a Claude-native Verb
Mappings section and adapts dotted allowlist identities only on
SEND/RECEIVE/RESPOND lines within an agent's Workflow section. Other body
content and exact terminal-newline state remain unchanged. VS Code and
OpenCode adapter behavior remains covered by the release suite.

#### Implementation Evidence

* TDD RED reproduced the absent source-path contract and missing Claude
  ``name`` values. Focused GREEN coverage verifies filename-derived identity,
  primary Manager ``Agent(...)`` bindings, nested bare ``Agent`` behavior,
  leaf omission, Workflow-scoped replacement, and Claude orchestration
  binding.
* Generated-product checks find exactly 13 valid, unique native names. Every
  mapped Manager allowlist target exists in that set, and Setup, PM, QM, and
  CM resolve to ``syspilot-setup``, ``syspilot-pm``, ``syspilot-qm``, and
  ``syspilot-cm``.
* A disposable Claude project completed initial installation and repeat
  update. The update removed one injected retired agent, retained 13 generated
  agents, created no ``.github`` or ``.opencode`` tree, and the fixture was
  deleted afterward with ``fixture_exists=False``.
* Claude Code 2.1.274 accepted
  ``claude plugin validate .claude/agents`` with ``Validation passed``.
  ``claude -p --agent syspilot-qm`` reached ``Not logged in · Please run
  /login`` and did not report agent-not-found. No credentials were available,
  requested, or stored, so authenticated invocation and Manager-to-Engineer
  delegation remain unexecuted and Claude remains experimental.
* The release-equivalent Python 3.11 suite passes with seven conditional
  skips. All four documentation tests pass, the clean Sphinx build succeeds
  with zero schema warnings, editor diagnostics are empty for implementation
  and tests, and ``git diff --check`` reports no whitespace errors.

### Round 11 — Final Independent Claude Adapter Quality Gate

**Reviewed by:** QM
**Review date:** 2026-09-17
**Commit reviewed:** ``86383837ca2baf1530ad39154534f70593ac870f``
**Overall disposition:** **CLEARED**. No high-, medium-, or low-severity
finding remains open in the Round 10 scope.

#### Per-Level MECE Results

* **L0 — PASS.** The four scoped UAT stories remain approved and preserve
  distinct ownership of agent adaptation, orchestration, limitation
  disclosure, and installer target acceptance. No duplicate or missing
  acceptance owner was introduced.
* **L1 — PASS.** The four scoped UAT requirements remain approved and each
  defines the test data for exactly one corresponding UAT story. Claude Code
  2.1.274, the complete 13-agent inventory, and the authentication boundary
  are represented without weakening the production OpenCode criteria.
* **L2 — PASS.** The three corrected harness designs and four scoped UAT
  designs remain approved. Identity mapping, main-thread Manager Agent
  allowlists, nested Agent semantics, structural body/binding adaptation, and
  the experimental-support boundary have one consistent owner each.

#### Trace and Schema Results

All 15 scoped Design/UAT IDs are present and approved in the freshly generated
needs database. Their immediate Story-to-Requirement-to-UAT-Design links and
the production Design links resolve. A clean warning-as-error documentation
build succeeds with zero schema warnings. No orphan, unresolved link, status
conflict, or cross-level ownership gap was found.

#### Implementation and UAT Evidence

* The focused Claude adapter checks pass for required filename-derived
  ``name`` mapping, explicit Manager ``Agent(<native-name>, ...)`` targets,
  nested bare ``Agent`` behavior, Workflow-scoped identity replacement, and
  Claude-native orchestration binding generation.
* Independent acceptance-project inspection finds exactly 13 valid, unique
  hyphenated names and no unresolved native identity reference. Claude Code
  2.1.274 reports ``Validation passed`` for ``.claude/agents`` and
  ``claude -p --agent syspilot-qm`` reaches ``Not logged in`` rather than
  agent-not-found.
* The full release-equivalent Python 3.11 suite passes all 108 tests with seven
  documented conditional skips. The clean documentation build succeeds with
  zero warnings and zero schema warnings.
* VS Code has no regression: all 13 acceptance-project agent files are
  byte-for-byte identical to their product sources. OpenCode 1.18.31 parses
  the generated acceptance-project configuration successfully; the complete
  suite preserves its adapter coverage. The previously accepted live
  Manager-to-Engineer delegation evidence remains valid and was not
  reclassified by this Claude-only correction.
* The reviewed commit and quality checks pass ``git diff --check``. The
  quality artifact is the only follow-up change.

#### Residual Acceptance Boundary

Claude Code remains experimental. The unauthenticated discovery result proves
native loading but neither authenticated model execution nor
Manager-to-Engineer delegation. Production promotion remains blocked until
both authenticated live checks pass and are recorded; this is the specified
acceptance boundary, not an open Round 10 quality finding.

#### Findings Report to PM

L0: no findings. L1: no findings. L2: no findings. Trace: no findings. Schema:
no findings. UAT: no findings within the declared experimental boundary.
Round 10 is **CLEARED** at reviewed commit
``86383837ca2baf1530ad39154534f70593ac870f``.

### Final Multi-Harness Acceptance

**Acceptance date:** 2026-09-17

**Implementation revision installed:**
``86383837ca2baf1530ad39154534f70593ac870f``

**Source quality-clearance revision:**
``5357547902bb95bab5374f1ba5d02ff24fbab353``

Final acceptance used the installed ``../test-syspilot`` project to separate
native discovery and adapter correctness from credential-dependent model
execution. The production support boundary remains VS Code GitHub Copilot and
OpenCode. Claude Code and Qoder remain experimental; GitHub Copilot CLI was
evaluated but is not production-certified.

| Harness | CLI/version | Final outcome | Support boundary |
|---------|-------------|---------------|------------------|
| OpenCode | ``1.18.31`` (updated from ``1.17.4``) | Production target installed 13 agents, 7 commands, and 6 Skills. ``opencode debug config`` exited 0; live QM-to-MECE native Task delegation returned ``OPENCODE_TEST_OK``; same-revision update was idempotent. | Production-supported. |
| Claude Code | ``2.1.274`` (updated from ``2.1.175``) | Round 10 corrected skipped agents by mapping ``syspilot.<role>`` to required unique ``syspilot-<role>`` names. All 13 names and allowlist references resolve; ``claude plugin validate .claude/agents`` passes; ``claude --agent syspilot-qm`` reaches ``Not logged in`` rather than agent-not-found. | Experimental: no Anthropic/OAuth credential was available, so authenticated invocation and delegation remain unexecuted. |
| GitHub Copilot CLI | ``1.0.85`` (updated from ``1.0.51``) | The ``.github`` target contains 13 agents and 7 prompts byte-exact to source revision ``8638383``. | Evaluated only: no GitHub.com Copilot credential was available. The existing ``gh`` login targets only ``github.boschdevcloud.com`` and cannot validate GitHub.com Copilot CLI. Production support remains GitHub Copilot in VS Code. |
| Qoder | Not installed for live acceptance | Deterministic adapter fixtures remain available; no live native invocation evidence was added. | Experimental. |

Installed-runtime validation passed through uv-managed Sphinx. The acceptance
project contained no project ``.venv``, ``__pycache__``, or checkpoint residue.
The same-revision update did not change installed output. The test project's
pre-existing ``.gitignore`` deletion was left untouched and is not product
behavior.

Live GitHub API acquisition for the Claude fixture reached the unauthenticated
API rate limit and returned HTTP 403. Experimental verification therefore used
the local, quality-cleared ``SourceSnapshot`` for revision ``8638383``. This is
an acceptance-environment boundary, not an alternate product acquisition path;
the product supports ``GITHUB_TOKEN`` for live GitHub API acceptance where
applicable. All Python operations in acceptance used ``uv``.

### Round 12 — Final Documentation Quality Review

**Reviewed by:** QM
**Review date:** 2026-09-17
**Commit reviewed:** ``72b97b5d7a5fc91dadbfd157f5677b8ea18b445e``
**Overall disposition:** **NOT CLEARED.** Current-state README and architecture
text are accurate, but one historical-support ambiguity and one L2 lifecycle
metadata defect remain in the declared harness-interop scope.

#### Per-Level Results

* **L0 — PASS.** The approved harness portability, installation, Setup, and
  Installer stories retain distinct ownership. Current production support is
  VS Code GitHub Copilot and OpenCode; Claude Code and Qoder remain
  experimental.
* **L1 — PASS.** The approved requirements retain the same production matrix,
  uv-only execution boundary, native-install ownership, and external
  authentication boundary. No broken or orphaned scoped requirement was found.
* **L2 — FAIL.** Active harness design remains consistent with the current
  support matrix, but ``SYSP_SPEC_HARNESS_PROMPT_ADAPTER`` has malformed option
  indentation: Sphinx discovers the ID while emitting an empty lifecycle
  status in ``needs.json``.

#### Trace, Schema, and Acceptance Evidence

* All 30 sampled scoped L0/L1/L2 IDs exist in the generated needs database;
  none reports a dead or forbidden link.
* Schema validation reports 351 validated needs and zero warnings. The empty
  prompt-adapter status is a lifecycle metadata defect not rejected by the
  current schema check.
* The three cited revisions exist, and both implementation revision
  ``86383837ca2baf1530ad39154534f70593ac870f`` and source quality-clearance
  revision ``5357547902bb95bab5374f1ba5d02ff24fbab353`` are ancestors of the
  reviewed documentation commit.
* Installed versions match the record: OpenCode ``1.18.31``, Claude Code
  ``2.1.274``, and GitHub Copilot CLI ``1.0.85``. In the acceptance project,
  ``opencode debug config`` exits 0, Claude agent validation passes, Claude
  reports ``loggedIn: false``, and ``gh auth status`` lists only
  ``github.boschdevcloud.com``.
* The acceptance project contains the recorded 13 OpenCode agents, 7 commands,
  6 Skills, 13 Claude agents, and 13 VS Code agents, with no project
  ``.venv``, ``__pycache__``, or checkpoint residue. Its pre-existing
  ``.gitignore`` deletion remains present and unrelated.
* README exposes only the valid production commands for ``vscode`` and
  ``opencode``, remains concise, and documents no Python operation outside
  ``uv``. The public Installer likewise limits production harnesses to those
  two values.
* Fresh evidence supplied with this review records documentation tests 4/4,
  a strict build with zero warnings, and clean diagnostics. Independent editor
  diagnostics for the three reviewed documents are also clean.

#### Findings Report to PM

| # | Level | Severity | Finding | Required disposition |
|---|-------|----------|---------|----------------------|
| 1 | L2 / Change Document | medium | The historical ``Production-Stable Installation Design Correction`` still declares Claude Code production-supported and publishes ``--harness <vscode\|opencode\|claude> --orchestration <skill-name>`` commands. Later text restores the correct matrix, but the only explicit ``Superseded Statements`` notice is limited to Claude identity/allowlist/body-adaptation statements. A reader can still mistake the stale support classification and commands for current guidance. | fix-now: add an explicit historical/non-authoritative notice that supersedes the complete earlier production matrix, README acceptance, command, and implementation statements; point to the final support matrix and current installer commands. |
| 2 | L2 / ``SYSP_SPEC_HARNESS_PROMPT_ADAPTER`` | medium | The directive's ``:id:``, ``:links:``, and ``:tags:`` options are under-indented relative to ``:status:``. The generated need exists but has an empty status, contradicting the Change Document's approved-status claims and preventing a clean lifecycle-status conclusion. | fix-now: align the directive option indentation, rebuild documentation, and verify the generated need retains ``status=approved`` with its existing links. |

#### PM Decisions

**PM decision date:** 2026-09-17

| # | Finding # | Decision | PM rationale |
|---|-----------|----------|--------------|
| 1 | 1 | fix-now | Historical material must be unmistakably non-authoritative so users receive only the current production support boundary and valid installer guidance. |
| 2 | 2 | fix-now | The approved design must expose its intended lifecycle status consistently in generated documentation and traceability evidence. |

#### Round 12 Resolution

**Resolution date:** 2026-09-17

* [x] Earlier correction sections are headed and admonished as historical and
  superseded; obsolete bootstrap, Claude-production, and public
  ``--orchestration`` command forms are no longer executable examples.
* [x] Current guidance points to README Installation. Production CLI support is
  limited to ``vscode`` and ``opencode``; Claude Code and Qoder remain
  experimental fixture targets.
* [x] ``SYSP_SPEC_HARNESS_PROMPT_ADAPTER`` directive options are aligned and
  its lifecycle is ``implemented`` based on independently verified VS Code
  prompt identity and OpenCode native command generation/routing. Its
  Claude/Qoder mappings remain explicitly experimental and are not presented
  as production acceptance.
* [x] Active documentation outside historical Change Document sections has no
  unsupported ``--harness claude``, ``--harness qoder``, public
  ``--orchestration``, bootstrap-subcommand, or nested Setup-to-Installer
  delegation instruction.

**Current-state support summary:** GitHub Copilot in VS Code and OpenCode are
production-supported. Claude Code and Qoder are experimental. The public
Installer accepts only ``vscode`` and ``opencode`` and deterministically
installs synchronous orchestration without a public selection option.

**Verification evidence:** ``docs.test_docs_build`` passes 4/4 tests; the full
clean warnings-as-errors build succeeds with zero schema warnings;
``needs.json`` reports ``SYSP_SPEC_HARNESS_PROMPT_ADAPTER`` as
``status=implemented`` with all four links; source scans report no active stale
CLI or delegation instructions and no executable stale historical command;
``git diff --check`` reports no whitespace errors.

### Round 13 — Final Independent Quality Clearance

**Reviewed by:** QM
**Review date:** 2026-09-17
**Commit reviewed:** ``bca342e9144216c1b9676c7770fc8c06eb430fd6``
**Overall disposition:** **CLEARED.** Both Round 12 findings are resolved, and
no new finding exists within the Change Document's declared scope.

#### Per-Level Results

* **L0 — PASS.** Production support remains limited to GitHub Copilot in VS
  Code and OpenCode. Claude Code and Qoder remain experimental, and GitHub
  Copilot CLI remains evaluated but not production-certified. The scoped
  stories preserve distinct portability, installation, Setup, and Installer
  ownership without a new gap, overlap, or contradiction.
* **L1 — PASS.** The scoped requirements preserve the uv-only installation
  boundary, explicit production harness selection, direct installed-runtime
  update flow, and external authentication boundaries. No scoped requirement
  is missing, broken, or contradicted by the reviewed documentation.
* **L2 — PASS.** ``SYSP_SPEC_HARNESS_PROMPT_ADAPTER`` is generated with
  ``status=implemented`` and links to
  ``SYSP_REQ_HARNESS_BEHAVIORAL_EQUIVALENCE``,
  ``SYSP_REQ_HARNESS_CONTENT_SINGLE_SOURCE``,
  ``SYSP_SPEC_AGENT_ARCH_PROMPT``, and
  ``SYSP_SPEC_HARNESS_TARGET_MATRIX``. Current architecture and README text
  agree with that lifecycle and with the production support boundary.

#### MECE, Trace, and Schema

* **MECE — PASS by level.** L0 support and actor ownership, L1 executable and
  authentication boundaries, and L2 adapter/status ownership remain mutually
  exclusive and collectively exhaustive for the declared correction scope.
* **Trace — PASS.** The freshly generated need retains the intended lifecycle
  and all four links; no scoped dead or forbidden link was found.
* **Schema — PASS.** The strict clean documentation build validates 351 needs
  with zero schema warnings and completes with zero Sphinx warnings.

#### Final Acceptance Evidence

* Documentation tests pass 4/4, the warnings-as-errors build succeeds, editor
  diagnostics for all reviewed files are clean, and the README stale-command
  scan is empty. Active README, architecture, specification, and product
  surfaces contain no unsupported Claude/Qoder install target, public
  ``--orchestration`` option, bootstrap subcommand, or Setup-to-Installer
  delegation instruction.
* OpenCode ``1.18.31`` remains the production native target: the acceptance
  project contains 13 agents, 7 commands, and 6 Skills, and ``opencode debug
  config`` exits 0. GitHub Copilot in VS Code remains production-supported;
  its acceptance tree contains 13 agents and the recorded 7 prompts.
* Claude Code ``2.1.274`` remains experimental. The corrected native mapping
  uses unique ``syspilot-<role>`` names instead of dotted source identities;
  all 13 generated agents validate, while ``claude auth status`` remains
  ``loggedIn: false``. Authenticated invocation and delegation are therefore
  not claimed.
* GitHub Copilot CLI ``1.0.85`` remains evaluated only. The available ``gh``
  authentication targets ``github.boschdevcloud.com``, not GitHub.com Copilot.
  The recorded unauthenticated GitHub API HTTP 403 boundary and optional
  ``GITHUB_TOKEN`` path remain explicit and are not presented as successful
  live acquisition evidence. Qoder was not installed for live acceptance and
  remains an experimental deterministic-fixture target.
* The acceptance project has 13 Claude agents and 13 VS Code agents and no
  project ``.venv``, ``__pycache__``, or checkpoint residue. Historical
  command records are explicitly marked superseded, omit obsolete executable
  signatures, and direct readers to the current README installation contract.

#### Findings Report to PM

L0: no findings. L1: no findings. L2: no findings. Trace: no findings. Schema:
no findings. Acceptance/documentation: no findings. Round 13 is **CLEARED** at
reviewed commit ``bca342e9144216c1b9676c7770fc8c06eb430fd6``.

### Round 14 — Targeted Implementation Quality Clearance

**Reviewed by:** QM
**Review date:** 2026-09-17
**Commit reviewed:** ``15e722fdb5533ccc43eebec4e39a5d6d344a67c9``
**Verdict:** **CLEARED.** The targeted review confirms that checkpoint restore
operations resolve mutable paths from their current identities, preserving the
transaction boundary when path identities change after checkpoint creation.

#### Verification Evidence

* Focused regressions: **5/5 passed**.
* Full installer suite: **104 passed and 4 expected skips**.
* Documentation tests: **4/4 passed**.
* Strict documentation build: **zero warnings and zero schema violations**.

#### Findings Report to PM

No findings. The implementation commit is **CLEARED**.

---

## Appendix: Link Discovery Results

```
=== SYSP_US_AGENT_ARCH ===
SYSP_REQ_AGENT_ARCH_DUTIES, SYSP_REQ_AGENT_ARCH_FRONTMATTER, SYSP_REQ_AGENT_ARCH_PROMPT,
SYSP_REQ_AGENT_ARCH_SOUL, SYSP_REQ_AGENT_ARCH_WORKFLOW
(+ existing consumer USs, unaffected: SYSP_US_CM, SYSP_US_CUSTOM_AGENT_WORKFLOWS, SYSP_US_DESIGN,
 SYSP_US_DOCU, SYSP_US_DOC_CONVENTIONS, SYSP_US_DOC_EXTERNAL, SYSP_US_DOC_INTERNAL,
 SYSP_US_DOC_RELEASE_NOTES, SYSP_US_IMPLEMENT, SYSP_US_INSTALLER, SYSP_US_MECE, SYSP_US_PM,
 SYSP_US_QM, SYSP_US_RELEASE, SYSP_US_SETUP, SYSP_US_SKILL_ARCH, SYSP_US_TRACE, SYSP_US_UAT,
 SYSP_US_UAT_AGENT_BASE_TOOLSET, SYSP_US_UAT_GENERIC_AGENT_WORKFLOW, SYSP_US_UAT_REMOVE_TOOLS_FRONTMATTER,
 SYSP_US_VERIFY)

=== SYSP_US_SKILL_ARCH ===
SYSP_REQ_SKILL_ARCH_FRONTMATTER, SYSP_REQ_SKILL_ARCH_INSTRUCTIONS, SYSP_REQ_SKILL_ARCH_RULES,
SYSP_REQ_SKILL_ARCH_SUBSTITUTABILITY, SYSP_REQ_SKILL_ARCH_TAILORING, SYSP_REQ_SKILL_DEFINITIONS

=== SYSP_US_SETUP ===
SYSP_REQ_SETUP_BOOTLOADER_DUTIES, SYSP_REQ_SETUP_BOOTLOADER_FETCH, SYSP_REQ_SETUP_BOOTLOADER_INVOKE,
SYSP_REQ_SETUP_BOOTLOADER_VERSION, SYSP_REQ_SETUP_FRONTMATTER, SYSP_REQ_SETUP_PROMPT, SYSP_REQ_SETUP_SOUL

=== SYSP_US_INSTALLER ===
SYSP_REQ_INSTALLER_DIRECT_OPS, SYSP_REQ_INSTALLER_DOC_BOOTSTRAP, SYSP_REQ_INSTALLER_DUTIES,
SYSP_REQ_INSTALLER_ENCODING, SYSP_REQ_INSTALLER_GITHUB_SOURCE, SYSP_REQ_INSTALLER_ORCHESTRATION_SELECT,
SYSP_REQ_INSTALLER_ROLLBACK, SYSP_REQ_INSTALLER_SCOPE, SYSP_REQ_INSTALLER_SESSION_SCAFFOLD,
SYSP_REQ_INSTALLER_WORKFLOW, SYSP_REQ_SETUP_INSTALLER_NOT_USER_INVOCABLE, SYSP_REQ_SETUP_SKILL_MUTEX

=== SYSP_US_SKILL_ORCHESTRATION ===
SYSP_REQ_INSTALLER_ORCHESTRATION_SELECT, SYSP_REQ_SKILL_ORCHESTRATION_AGENT_VOCAB,
SYSP_REQ_SKILL_ORCHESTRATION_GROUP, SYSP_REQ_SKILL_ORCHESTRATION_REPORTING,
SYSP_REQ_SKILL_ORCHESTRATION_VERBS

=== SYSP_US_HARNESS_PORTABILITY === (new US, no inbound REQ links yet — expected)
[]

=== SYSP_US_HARNESS_INSTALL === (new US, no inbound REQ links yet — expected)
[]
```

Confirms `:links:` on both new Level 0 stories resolved correctly (each appears as an
inbound consumer of its parent US in the parent's own query), and sphinx-build passed
with 0 errors/warnings after the Level 0 edits.

### Level 1 Link Verification

```
=== SYSP_US_HARNESS_PORTABILITY (post-L1, in, depth 1) ===
SYSP_REQ_AGENT_ARCH_FRONTMATTER, SYSP_REQ_SKILL_ARCH_FRONTMATTER,
SYSP_REQ_SKILL_ORCHESTRATION_GROUP, SYSP_REQ_HARNESS_BEHAVIORAL_EQUIVALENCE,
SYSP_REQ_HARNESS_CONTENT_SINGLE_SOURCE, SYSP_REQ_HARNESS_LIMITATION_DISCLOSURE,
SYSP_REQ_HARNESS_PORTABILITY_NO_REGRESSION

=== SYSP_US_HARNESS_INSTALL (post-L1, in, depth 1) ===
SYSP_REQ_INSTALLER_SCOPE, SYSP_REQ_SETUP_BOOTLOADER_DUTIES,
SYSP_REQ_HARNESS_NATIVE_INSTALL, SYSP_REQ_HARNESS_NATIVE_UPDATE,
SYSP_REQ_HARNESS_ONE_TIME_ENABLEMENT, SYSP_REQ_HARNESS_INSTALL_NO_REGRESSION
```

Confirms every new/mirrored Level 1 REQ resolves as an inbound consumer of the
correct Level 0 story, no broken links, and sphinx-build passed with 0
errors/warnings after the Level 1 edits.

### Level 2 Link Verification

```
=== SYSP_REQ_HARNESS_NATIVE_INSTALL (post-L2, in, depth 1) ===
SYSP_SPEC_HARNESS_TARGET_MATRIX, SYSP_SPEC_INSTALLER_HARNESS_TARGETS

=== SYSP_REQ_HARNESS_CONTENT_SINGLE_SOURCE (post-L2, in, depth 1) ===
SYSP_SPEC_HARNESS_AGENT_ADAPTER, SYSP_SPEC_HARNESS_PROMPT_ADAPTER,
SYSP_SPEC_HARNESS_SKILL_ADAPTER, SYSP_SPEC_HARNESS_TARGET_MATRIX

=== SYSP_REQ_HARNESS_LIMITATION_DISCLOSURE (post-L2, in, depth 1) ===
SYSP_SPEC_HARNESS_LIMITATIONS

=== SYSP_REQ_HARNESS_BEHAVIORAL_EQUIVALENCE (post-L2, in, depth 1) ===
SYSP_SPEC_HARNESS_AGENT_ADAPTER, SYSP_SPEC_HARNESS_SKILL_ADAPTER

=== SYSP_REQ_HARNESS_ONE_TIME_ENABLEMENT (post-L2, in, depth 1) ===
SYSP_SPEC_HARNESS_ONE_TIME_ENABLEMENT

=== SYSP_REQ_HARNESS_NATIVE_UPDATE (post-L2, in, depth 1) ===
SYSP_SPEC_HARNESS_ONE_TIME_ENABLEMENT

=== SYSP_REQ_HARNESS_INSTALL_NO_REGRESSION (post-L2, in, depth 1) ===
SYSP_SPEC_INSTALLER_HARNESS_TARGETS

=== SYSP_REQ_HARNESS_PORTABILITY_NO_REGRESSION (post-L2, in, depth 1) ===
SYSP_SPEC_INSTALLER_HARNESS_TARGETS

=== SYSP_REQ_SKILL_ORCHESTRATION_GROUP (post-L2, in, depth 1) ===
SYSP_SPEC_HARNESS_ORCHESTRATION_ADAPTER, SYSP_SPEC_SKILL_ORCHESTRATION_CONTRACT,
SYSP_SPEC_SKILL_ORCHESTRATION_GROUP, SYSP_SPEC_SKILL_ORCHESTRATION_VERB_MODEL_SUBAGENT
```

Confirms every new Level 2 SPEC resolves as an inbound consumer of the
correct Level 1 REQ, no broken links, and sphinx-build passed with 0
errors/warnings after the Level 2 edits (list-table column-count mismatches
and one stray cross-reference were caught and fixed during this check).

---

*Generated by syspilot Change Agent*
