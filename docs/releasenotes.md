# syspilot Release Notes

## v0.5.2 - 2026-05-01

### Summary
Patch release with internal process fixes: PM/CM role boundaries clarified, merge gate process formalized, QM reduced to pure auditor role, Setup Agent preserves instance-specific tools on update, and CM sends post-merge confirmation to PM.

### 🔧 Fixes & Improvements

- **PM/CM Role Boundary** (`pm-cm-role-boundary`)
  - PM writes CRs from user perspective only (intent + user-visible ACs, no implementation details)
  - CM always follows the complete change process independently
  - Design Agent gets `vscode/askQuestions` in frontmatter for user-guided mode

- **Merge Gate Process** (`qm-merge-gate`)
  - CM does not merge to development without PM approval
  - QM results are always routed to PM who decides: fix now / defer / accept as-is
  - Formal merge gate between QM review and development merge

- **QM Auditor Only** (`qm-auditor-only`)
  - QM always produces Findings Reports addressed to PM — never creates CRs directly
  - Simplified QM model: one output format (Findings Report → PM)
  - Aligns with the Merge Gate pattern

- **Setup Preserve Tools** (`setup-preserve-tools`)
  - Setup Agent preserves instance-specific `tools:` frontmatter field during updates
  - Fresh installs copy `tools:` from product as-is
  - New agents are always copied completely

- **CM Merge Confirmation** (`cm-merge-confirmation`)
  - After merging to development, CM sends confirmation to PM with commit hash and branch name
  - Existing pre-merge notification remains unchanged

### 📋 Change Requests

| Change Document | Scope |
|----------------|-------|
| `pm-cm-role-boundary` | PM/CM guardrails, CR intent stays high-level |
| `qm-merge-gate` | Merge Gate process (CM waits for PM approval) |
| `qm-auditor-only` | QM is pure auditor (Findings Reports only) |
| `setup-preserve-tools` | Setup Agent preserves instance tools: frontmatter |
| `cm-merge-confirmation` | CM post-merge confirmation to PM |

---

## v0.5.1 - 2026-04-27

### Summary
Three workflow improvements and housekeeping: Setup Manager added as a 4th manager role with prompt specification, Release workflow fixed for correct development-first prep and back-merge, Impact Analysis mandated as a required step in the CM and Design workflows.

### ✨ New Features

- **Setup Manager as 4th Manager** (CR15, `agent-prompts-perspective`)
  - Setup Manager (`@syspilot.setup`) formally added as a 4th user-invocable manager role alongside PM, CM, QM
  - Prompt specification added: only user-invocable agents (managers) SHALL have prompt files
  - Agent Frontmatter and Prompt Frontmatter established as qualified terms in the spec hierarchy
  - Engineer User Story perspective corrected from "As a syspilot user, I want to have a [Agent]..." to "...I want my agentic managers to have a [Agent] that..."

### 🔧 Fixes & Improvements

- **Release Workflow Fix** (CR16)
  - Prep steps (archive, version bump, release notes, sphinx validation) now run on `development` first — not on `main`
  - Back-merge (`development ← main`) added as explicit step after tagging to sync the squash commit
  - Conflict guidance: `-X theirs` strategy documented for squash-merge conflicts (development wins)

- **Mandatory Impact Analysis** (CR17)
  - Impact Analysis is now a required step (SHALL) in the CM workflow before dispatching to System Designer
  - Impact Analysis is now a required step (SHALL) in the System Designer workflow before analysis
  - Acceptance Criterion AC-5 language corrected from MUST to SHALL for consistency

### 🏠 Housekeeping

- `.gitignore` updated: installed product copies (agents, prompts, skills, scripts) are now gitignored in consumer workspaces
- `docs/changes/` structure flattened: archives live directly at `docs/changes/vX.Y.Z/` (no `archive/` subfolder)
- v0.5.0 release notes backfilled on `development` branch

### 📋 Change Requests

| CR | Change Document | Scope |
|----|----------------|-------|
| CR15 | `agent-prompts-perspective` | Setup Manager, Prompt Specification, Engineer US perspective |
| CR16 | (workflow fix) | Release workflow prep + back-merge + conflict guidance |
| CR17 | (workflow fix) | Mandatory Impact Analysis in CM and Design workflows |

---

## v0.5.0 - 2026-04-16

### Summary
Major architecture overhaul: complete green-field Agent Architecture v2 with new `SYSP_` prefix, Git-Flow branching model, impact analysis skill, and full spec coverage for all 11 agents plus the Verify Engineer. Includes 14 Change Requests (CR1–CR14).

### ⚠️ Breaking Changes

- **Agent Architecture v2** (CR1–CR7) — All specifications migrated from `SYSPILOT_` to `SYSP_` prefix. Old RST files removed. New traceability chain covers all 11 agents with Soul/Duties/Workflow/Frontmatter structure.
- **Instance Layer Removed** (CR5) — `docs/inst/syspilot/` eliminated; single product layer architecture.

### ✨ New Features

- **Agent Architecture v2** (CR1–CR7, `agent-architecture-v2`)
  - Full specification set (US → REQ → SPEC) for all 11 agents: PM, CM, QM, Design, Implement, UAT, Docu, MECE, Trace, Release, Setup
  - Meta-level architecture spec (`SYSP_US_AGENT_ARCH`, `SYSP_REQ_AGENT_ARCH_*`, `SYSP_SPEC_AGENT_ARCH_*`)
  - Agent structure: Soul (immutable identity), Duties (customizable), Workflow (customizable)
  - YAML frontmatter configuration specified per agent (CR5)
  - Agents distributed as product artifacts in `syspilot/agents/` and `syspilot/prompts/`

- **Skill Specifications** (CR2, `skill-specs-and-branching`)
  - Full spec chain for `syspilot.ask-questions`, `syspilot.orchestration`, `syspilot.branching` skills
  - Skills follow VS Code folder format: `.github/skills/<name>/SKILL.md`

- **Git-Flow Branching Model** (CR8, `git-flow-and-modes`)
  - Permanent `development` integration branch replaces chained branching
  - Feature branches created from and squash-merged back to `development`
  - Change Manager modes: `autonomous` and `user-guided`
  - CM-completion notification triggers QM targeted checks

- **Impact Analysis Skill** (CR9, `impact-analysis-skill`)
  - New `syspilot.impact-python` skill wrapping `get_need_links.py`
  - System Designer queries full dependency tree before analysis
  - Spec chain: `SYSP_US_SKILL_IMPACT` → `SYSP_REQ_SKILL_IMPACT_*` → `SYSP_SPEC_SKILL_IMPACT_*`

- **Verify Engineer Specs** (CR14, `verify-agent-specs`)
  - Full spec set (US → REQ → SPEC) for the Verify Engineer agent
  - `SYSP_US_VERIFY` → `SYSP_REQ_VERIFY_*` → `SYSP_SPEC_VERIFY_*`

- **Main Branch Protection** (CR4, `main-branch-protection`)
  - Only `@syspilot.release` may commit to, merge to, or push to `main`
  - All agents receive guardrail preventing direct `main` commits

### 🔧 Fixes & Improvements

- **ID Rename** (CR10) — `CHANGE` role slug renamed to `DESIGN` across all specs
- **Documentation Update** (CR12+CR13) — `docs/architecture.md`, `docs/workflows.md`, `docs/methodology.md`, `docs/namingconventions.md` updated for v2 architecture and skills-authoring principle
- **Branching & Completion Reporting** (CR3) — CM workflow Step 0 branch creation; orchestration skill completion reporting rule
- **Phase 2 Cleanup** (CR6) — Removed 27 superseded `SYSPILOT_` RST files, updated toctree indexes, cleaned dangling references

### 📋 Change Requests

| CR | Change Document | Scope |
|----|----------------|-------|
| CR1–CR7 | `agent-architecture-v2` | Agent Architecture v2 green-field |
| CR2 | `skill-specs-and-branching` | Skill specs + branching skill |
| CR3 | `branching-and-reporting` | CM branch step + completion reporting |
| CR4 | `main-branch-protection` | Main branch guardrail |
| CR5 | `frontmatter-and-instance-cleanup` | Frontmatter specs + instance removal |
| CR6 | `phase2-cleanup` | Old SYSPILOT_ file removal |
| CR8 | `git-flow-and-modes` | Git-Flow model + change modes |
| CR9 | `impact-analysis-skill` | Impact analysis skill |
| CR10 | (within CR9) | ID rename CHANGE→DESIGN |
| CR12+CR13 | (within docs) | Documentation updates |
| CR14 | `verify-agent-specs` | Verify Engineer specs |

---

## v0.4.0 - 2026-04-07

### Summary
Two workflow improvements that make the development loop tighter and safer: the Change Agent now runs `@syspilot.mece` as an automatic subagent after each level write for advisory validation, and the Setup Agent now creates a git baseline commit after a successful fresh install or adoption.

### ✨ New Features

- **MECE Agent as Subagent in Change Agent** (SYSPILOT_SPEC_CHG_LIVE_RST_PER_LEVEL)
  - After each level write `@syspilot.change` automatically invokes `@syspilot.mece` as a subagent
  - MECE results are shown as advisory findings — non-blocking, but surfaced before moving on
  - Requires the `agents:` frontmatter field in the agent file (SYSPILOT_SPEC_AGENT_FRAMEWORK)
  - Replaces manual per-level write process; RST files are written immediately after approval

- **Git Baseline Commit after Fresh Install / Adoption** (#11, SYSPILOT_SPEC_INST_INSTALL_COMMIT)
  - `@syspilot.setup` now stages and commits all placed files after successful sphinx-build validation
  - Commit message: `chore: install syspilot v{version}` (new project) or `chore: adopt syspilot v{version}` (existing project)
  - Confirmation-gated: user approves commit before it is created
  - Handles pre-existing uncommitted changes: offers to commit only syspilot files separately, or skip
  - Graceful skip if git is not initialized or identity is not configured (informational message)
  - Does not run in update mode (that is handled by the update branch workflow)

### 🔧 Fixes & Improvements

- `@syspilot.change` writes RST per level immediately after approval (`:status: draft`), enabling live link traversal via `get_need_links.py` during analysis
- Change Document is always a lean decision log from the start, not a verbose RST dump

### 📋 Specs

- New: `SYSPILOT_REQ_INST_INSTALL_COMMIT`, `SYSPILOT_SPEC_INST_INSTALL_COMMIT`
- Modified: `SYSPILOT_SPEC_INST_SETUP_AGENT` (Section 8: Git Baseline Commit)
- Modified: `SYSPILOT_US_INST_NEW_PROJECT`, `SYSPILOT_US_INST_ADOPT_EXISTING` (AC-6 added)
- Modified: `SYSPILOT_SPEC_CHG_LIVE_RST_PER_LEVEL` (MECE subagent step)
- Modified: `SYSPILOT_SPEC_AGENT_FRAMEWORK` (`agents:` frontmatter field documented)

---

## v0.3.1 - 2026-04-03

### Summary
Safety improvement to the update workflow: the Setup Agent now creates a dedicated `update/v{version}` branch before performing any updates, detects project-specific extensions that would be silently lost when replacing methodology-owned files, and creates a change document summarizing what was updated.

### ✨ New Features

- **Update Branch Workflow** (#16, SYSPILOT_SPEC_INST_UPDATE_BRANCH)
  - `@syspilot.setup` (update mode) now creates `update/v{version}` branch before any file changes
  - All update work is committed on the dedicated branch
  - A change document `docs/changes/update-v{version}.md` is created summarizing replaced/skipped files
  - User reviews the branch diff and merges when ready

- **Post-Update Extension Review** (#16, SYSPILOT_SPEC_INST_POST_UPDATE_REVIEW)
  - After replacing methodology-owned files, compares old vs new content using `git show HEAD:<path>`
  - If a file had project-specific additions that are missing in the new version, the user is alerted
  - Per-file options: accept new version / merge back manually / restore old version
  - Silent skip if no custom extensions are detected

### 🔧 Fixes & Improvements

- Resolves silent data loss when updating syspilot if methodology-owned files had been customized (e.g., extra verification steps in `syspilot.verify.agent.md`)

### 📋 Specs

- New: `SYSPILOT_REQ_INST_POST_UPDATE_REVIEW`, `SYSPILOT_REQ_INST_UPDATE_BRANCH`
- New: `SYSPILOT_SPEC_INST_POST_UPDATE_REVIEW`, `SYSPILOT_SPEC_INST_UPDATE_BRANCH`
- Modified: `SYSPILOT_SPEC_INST_UPDATE_PROCESS` (Steps 0a, 3/4a, 6/7 added)
- Modified: `SYSPILOT_US_INST_UPDATE` (AC-7 and AC-8 added)

---

## v0.3.0 - 2026-04-02

### Summary
Structural improvements: local install support, skill format migration to VS Code standard, new architecture and workflows documentation pages with Mermaid diagrams, and branching strategy documentation.

### ⚠️ Breaking Changes

- **Skill Format Migration** (#12, SYSPILOT_SPEC_AGENT_SKILL_FORMAT)
  - Skills now use folder format: `.github/skills/<name>/SKILL.md`
  - Old format `.github/skills/<name>.skill.md` is no longer recognized
  - Run `@syspilot.setup` to migrate existing installations
  - YAML frontmatter with `name`/`description` enables automatic skill discovery

### ✨ New Features

- **Local Install Support** (#9, SYSPILOT_REQ_INST_LOCAL_SOURCE)
  - Setup agent detects `syspilot/` directory and offers local vs GitHub install
  - Enables testing agent changes before pushing (dogfooding workflow)
  - File ownership rules apply equally to local install

- **Architecture Documentation** (#15, SYSPILOT_REQ_DOC_ARCHITECTURE)
  - New `docs/architecture.md` — explains Product/Instance separation concept
  - 7 chapters: Why, What (Product + Instance), How They Relate, Concrete Example, Update Safety

- **Workflows Documentation** (#15, SYSPILOT_REQ_DOC_WORKFLOWS)
  - New `docs/workflows.md` — central syspilot process description
  - Covers all 3 workflows: Change, Quality, Release
  - Agent decision guide, workflow diagrams, branching strategy

- **Mermaid Diagram Support**
  - Added `sphinxcontrib-mermaid` to Sphinx extensions
  - All ASCII diagrams replaced with Mermaid flowcharts across docs and specs
  - Client-side rendering via mermaid.js (no build-time dependency)

- **Branching Strategy** (SYSPILOT_SPEC_DOC_WORKFLOWS_STRUCTURE)
  - Documented chained feature branches model
  - Main = releases only, squash merge during `@syspilot.release`

### 🔧 Improvements

- **Housekeeping**
  - Removed version tracking from memory agent scope (SYSPILOT_SPEC_MEM_SCOPE)
  - Archived v0.2.2 change documents to `docs/changes/archive/v0.2.2/`

- **Traceability**
  - Added outgoing links from SPEC_DOC_WORKFLOWS_STRUCTURE to agent design specs
  - Impact analysis now catches documentation when agent specs change

### 📋 Issues Closed

- #9 — Setup Agent: Support local install from syspilot/ directory
- #12 — Migrate skills to VS Code standard format
- #15 — Documentation: Architecture page for Product/Instance concept


## v0.2.3 - 2026-03-30

### Summary
Agent Family Framework with product/instance architecture, plus setup agent update process with file ownership model. Specs are now organized around agent families with independent spec trees. Instance-level specs capture project-specific decisions for release and implement agents. The setup agent bootstraps itself first, then uses a 3-category ownership model (methodology/project/user) to decide which files to update.

### ✨ New Features

- **Agent Family Framework** (SYSPILOT_US_CORE_SPEC_AS_CODE, SYSPILOT_REQ_CORE_FAMILY_ARCH)
  - Product/Instance two-layer spec architecture
  - Product specs define WHAT (generic), instance specs define HOW (project-specific)
  - Family-based naming: `SYSPILOT_*` (product), `INST_SYSPILOT_*` (instance)
  - Framework-level docs separated from family-specific docs
  - `docs/syspilot/` = product specs, `docs/inst/syspilot/` = instance specs

- **Instance Spec Tree** (SYSPILOT_US_INST_AGNOSTIC, SYSPILOT_REQ_INST_CUSTOM_PRESERVE)
  - 14 new INST spec elements across all 3 levels (US → REQ → SPEC)
  - Release agent instance config: version file, tag format, archive policy, validation
  - Implement agent instance config: language, framework, testing conventions

- **Setup Agent Self-Update** (SYSPILOT_US_INST_UPDATE, SYSPILOT_REQ_INST_BOOTSTRAP_SELF)
  - Bootstrap Step 0: setup agent updates itself first before updating anything else
  - 3-category file ownership model: methodology (always replace), project (copy once), user (never touch)
  - Template banner on generic release/implement agents prompting customization

### 🐛 Bug Fixes

- **Release Agent** (INST_SYSPILOT_SPEC_REL_AGENT_CONFIG)
  - Replaced 441-line v0.2.1 fossil with customized KISS template (~60 lines)
  - Fixed: agent still contained `git rm` (delete) instead of `git mv` (archive)
  - Added squash merge step per SYSPILOT_SPEC_REL_WORKFLOW

- **Stale Path References**
  - Fixed 12× `templates/` → `syspilot/` in spec_release.rst, spec_change.rst
  - Moved `change-document.md` to `syspilot/templates/`

### 📦 Migration

- 130 spec IDs renamed with `SYSPILOT_` prefix
- 6 directory moves: `docs/{userstories,requirements,design}` → `docs/syspilot/`
- ~510 cross-reference updates across all RST files
- `copilot-instructions.md` updated with instance-level architecture

---

## v0.2.2 - 2026-03-17

### Summary
Two agent fixes: The release agent is refactored from a ~425-line syspilot-specific playbook into a ~45-line KISS template with an embedded decisions table. The setup agent now detects existing sphinx-needs installations before offering to install.

### 🐛 Bug Fixes

- **Release Agent Template** (US_REL_AGENT_TEMPLATE, REQ_REL_PROCESS_DOC, SPEC_REL_AGENT)
  - Fixed: agent was syspilot-specific, hard-coded paths like `templates/version.json`
  - Fixed: agent deleted change documents instead of archiving (violated REQ_CHG_CHANGE_DOC AC-5)
  - Refactored from ~425 to ~45 lines — KISS template with embedded decisions table
  - First `@syspilot.release` invocation bootstraps decisions by asking user
  - Closes [#5](https://github.com/enthali/syspilot/issues/5)

- **Setup Agent Dependency Detection** (US_INST_BOOTSTRAP, REQ_INST_AUTO_SETUP, SPEC_INST_SETUP_AGENT)
  - Fixed: setup agent installed sphinx-needs without checking if already available
  - Now detects existing sphinx-needs and offers A/B/C options
  - Skips installation step when sphinx-needs already available

---

## v0.2.1 - 2026-03-16

### Summary
Internal improvement to the Implement Agent workflow. Adds a systematic Acceptance Criteria completeness check between Code Implementation and Quality Gates, preventing implementation gaps from reaching the Verify Agent. Based on real-world findings from Issue #4.

### 🔧 Internal Changes

- **Implementation Completeness Check** (US_CHG_IMPLEMENT, REQ_CHG_IMPL_AGENT AC-7)
  - New Step 4 in Implement Agent: AC-by-AC verification before quality gates (SPEC_IMPL_COMPLETENESS_CHECK)
  - Updated Quality Gate Workflow with completeness check prerequisite (SPEC_IMPL_QUALITY_GATES)
  - Common gap detection: modified REQs with new ACs, multi-condition specs, cross-component integration
  - Applied to both active agent (`.github/agents/`) and distributable template (`templates/agents/`)

---

## v0.2.0 - 2026-03-16

### Summary
Major architecture update introducing template-first distribution, curl-based installation, and documentation-as-implementation-artifact. The `templates/` directory is now the single source for all distributed files, replacing the previous auto-detect + init-script approach with a simple curl/Invoke-WebRequest bootstrap. Documentation maintenance is integrated into the implement and setup agents via per-document chapter structure SPECs. Comprehensive MECE quality review across all three specification levels.

### ✨ New Features

- **Template-First Architecture** (US_INST_AGNOSTIC, US_INST_CROSS_PROJECT, REQ_INST_TEMPLATE_SOURCE)
  - `templates/` directory as single source for distribution (SPEC_INST_TEMPLATE_LAYOUT)
  - `.github/` is consumer installation, may diverge from templates
  - Language-agnostic skeleton implement agent with TODO placeholders (REQ_INST_IMPL_SKELETON)
  - Self-install validation during release (SPEC_INST_SELF_INSTALL)
  - 8 agents, 8 prompts, 1 skill, 1 script distributed via templates

- **Curl-Based Setup** (US_INST_BOOTSTRAP, REQ_INST_AUTO_SETUP, REQ_INST_NEW_PROJECT)
  - Single curl command downloads setup agent from GitHub main (SPEC_INST_CURL_BOOTSTRAP)
  - Setup agent fetches all files from `templates/` via GitHub API (SPEC_INST_SETUP_AGENT)
  - Intelligent AI-driven merge for updates (SPEC_INST_FILE_OWNERSHIP)
  - Version tracking via `.syspilot/version.json` (SPEC_INST_VERSION_MARKER)
  - Init scripts removed — no local syspilot repo needed

- **Documentation Scope** (US_DOC_MAINTAIN, REQ_DOC_SCOPE)
  - Documentation as implementation artifact, not a separate workflow step
  - Per-document requirements: REQ_DOC_README, REQ_DOC_METHODOLOGY, REQ_DOC_NAMING, REQ_DOC_RELEASE_NOTES, REQ_DOC_PROCESS, REQ_DOC_INDEX
  - Per-document chapter structure SPECs (SPEC_DOC_*_STRUCTURE)
  - Template documentation scope for new projects (SPEC_DOC_SCOPE_TEMPLATE)

- **Verification Report Persistence** (US_CHG_VERIFY, REQ_CHG_VERIFY_AGENT)
  - Verification reports saved as `docs/changes/val-<name>.md` (SPEC_VERIFY_REPORT)
  - Change Documents archived after merge to `docs/changes/archive/`

### 🔧 Internal Changes

- **MECE Quality Review — all 3 levels**
  - US level: Remove stale doc agent references, add 4 missing links
  - REQ level: Scope clarity (release notes generation vs structure, dependency declaration vs automation), documentation as implementation artifact, 12 horizontal links added
  - SPEC level: Stale doc agent reference fixed, 10 cross-links added, `spec_doc_agent.rst` renamed to `spec_doc_scope_template.rst`

- **4-step workflow** (change → implement → verify → memory)
  - Doc agent removed from workflow chain
  - Documentation maintained by implement agent guided by chapter structure SPECs

### 📊 Specification Counts

| Level | Count | Status |
|-------|-------|--------|
| User Stories | 24 | 23 implemented, 1 draft |
| Requirements | 47 | 46 implemented, 1 approved |
| Design Specs | 47 | 45 implemented, 2 approved |

---

## v0.1.0 - 2026-02-11

### Summary
First stable release of syspilot. Adds consistent agent interaction UX via VS Code selection menus, restricts auto-detection to the project directory for security, and completes a full MECE quality review across all three specification levels (US → REQ → SPEC).

### ✨ New Features

- **Agent Interaction via Selection Menus** (US_DX_AGENT_INTERACTION, REQ_DX_AGENT_SELECTION_MENUS, REQ_DX_AGENT_SKILL_FILES)
  - All agents use VS Code's `ask_questions` tool for presenting choices (SPEC_AGENT_INTERACTION)
  - New shared skill file mechanism: `.github/skills/syspilot.ask-questions.skill.md`
  - Change Agent level transitions confirm save before navigation (SPEC_CHG_LEVEL_PROCESSING)

- **Auto-Detect Restricted to Project Directory** (REQ_INST_AUTO_DETECT, SPEC_INST_AUTO_DETECT)
  - `Find-SyspilotInstallation` no longer searches above the project root
  - GitHub Release download offered as fallback when syspilot not found locally (SPEC_INST_GITHUB_FALLBACK)
  - Updated acceptance criteria for US_INST_NEW_PROJECT, US_INST_ADOPT_EXISTING

### 🔧 Internal Changes

- **Memory Agent rewritten for compactness** (SPEC_MEM_UPDATE_PROCESS, SPEC_MEM_CONTENT_CATEGORIES, SPEC_MEM_INSTRUCTIONS_STRUCTURE)
  - Core principle: "If agents can discover it, don't put it in copilot-instructions.md"
  - copilot-instructions.md trimmed from ~325 to ~177 lines
  - Size target: 150–180 lines, cut if >200

- **MECE Quality Review — all 3 levels**
  - US level: 5 missing horizontal links added
  - REQ level: 8 missing horizontal links added, REQ_CORE_ASPICE removed (orphan)
  - SPEC level: 4 missing horizontal links added
  - US_CHG_RECOVERY set to `draft` (no REQ/SPEC exists)
  - A-SPICE reduced to optional documentation (aspice_alignment.rst kept, references cleaned)

### 📊 Specification Counts

| Level | Count | Status |
|-------|-------|--------|
| User Stories | 22 | 21 implemented, 1 draft |
| Requirements | 38 | 37 implemented, 1 approved |
| Design Specs | 37 | all implemented |

---

## v0.1.0-rc.3 - 2026-02-06

### Summary
Workflow handoff corrections: The agent chain now correctly routes verify→memory→change/release instead of verify→release→memory. Both the change workflow and release workflow exit points are now fully specified at all three levels (US → REQ → SPEC).

### 🐛 Bug Fixes

- **Workflow Handoff Order** (memory-handoff)
  - Agent chain corrected: verify→memory instead of verify→release (SPEC_AGENT_WORKFLOW)
  - Memory agent now hands off to change or release (SPEC_MEM_UPDATE_PROCESS)
  - New acceptance scenario: after memory, user chooses next change or release (US_WF_CHANGE, REQ_WF_CHANGE_SEQUENCE)

- **Release Workflow Exit Point** (release-exit)
  - Release workflow now defines what happens after publish: new change or end (US_WF_RELEASE, REQ_WF_RELEASE_SEQUENCE)
  - Release workflow diagram updated with exit point (SPEC_REL_WORKFLOW)

### 🔧 Internal Changes

- Verify agent handoff changed from "Create Release" to "Update Memory"
- Memory agent gained handoffs to change and release agents
- Implement agent removed unused release handoff
- copilot-instructions.md updated with agent handoff chain diagram

---

## v0.1.0-rc.2 - 2026-02-06

### Summary
Major specification architecture improvement: monolithic design spec file decomposed into 9 per-component files with 16 reverse-engineered specs from agent implementations. File organization methodology and core workflows formally integrated into the specification chain (US → REQ → SPEC). Total specification count: 4 new User Stories, 5 new Requirements, 18 new Design Specs.

### ✨ New Features

- **L2 Split by Component** (split-l2-specs)
  - Monolithic `spec_syspilot.rst` decomposed into 9 per-component spec files
  - 16 new Design Specs reverse-engineered from agent `.md` files covering Change, Implement, Verify, MECE, Trace, and Memory agents
  - Each agent now has complete design documentation with traceability to requirements

- **File Organization Methodology** (US_CORE_FILE_ORG, REQ_CORE_DOMAIN_ORG, REQ_CORE_L1_MIRROR)
  - Formalized problem-domain vs solution-domain file organization into spec chain
  - L0/L1 organized by stakeholder theme, L2 by technical component
  - 1:1 mapping rule between `us_<theme>.rst` and `req_<theme>.rst` formally specified
  - SPEC_DOC_STRUCTURE expanded with domain-type organization section

- **Core Workflow Stories** (US_WF_CHANGE, US_WF_QUALITY, US_WF_RELEASE)
  - End-to-end Change workflow: Change → Implement → Verify → Memory (SPEC_AGENT_WORKFLOW)
  - Independent Quality checks: standalone @mece and @trace usage (SPEC_TRACE_QUALITY_WORKFLOW)
  - Release workflow: Version → Validate → Publish (SPEC_REL_WORKFLOW)

### 📚 Documentation

- `methodology.md` updated with actual per-component spec file names
- `namingconventions.md` extended with WF (Workflows) theme abbreviation

### 🔧 Internal Changes

- `spec_syspilot.rst` renamed to `spec_setup.rst` (retained Setup Agent specs only)
- Quality Gates and Pre-Check specs moved from shared framework to `spec_implement.rst`
- MECE + Trace agents consolidated in `spec_traceability.rst`

### 📊 Specification Counts

| Level | Before | After | Delta |
|-------|--------|-------|-------|
| User Stories | 14 | 18 | +4 |
| Requirements | 23 | 28 | +5 |
| Design Specs | 18 | 36 | +18 |

---

## v0.1.0-rc.1 - 2026-02-06

### Summary
Major structural refactoring preparing syspilot for public review. All specification files reorganized from monolithic per-level files into themed domain files. All IDs renamed from sequential (`US_SYSPILOT_001`) to descriptive format (`US_CORE_SPEC_AS_CODE`). New methodology guide, naming conventions, project logo, and rewritten documentation landing page.

### ⚠️ Breaking Changes

- **All sphinx-needs IDs renamed** from sequential to descriptive format
  - User Stories: `US_SYSPILOT_*` → `US_CORE_*`, `US_CHG_*`, `US_TRACE_*`, `US_INST_*`, `US_DX_*`, `US_REL_*`
  - Requirements: `REQ_SYSPILOT_*` → `REQ_CORE_*`, `REQ_CHG_*`, `REQ_TRACE_*`, `REQ_INST_*`, `REQ_DX_*`, `REQ_REL_*`
  - Design Specs: `SPEC_SYSPILOT_*` / `SPEC_RELEASE_*` → `SPEC_AGENT_*`, `SPEC_DOC_*`, `SPEC_INST_*`, `SPEC_REL_*`
- **Monolithic spec files removed**: `us_syspilot.rst`, `req_syspilot.rst` replaced by themed files
- Projects referencing old IDs must update their links

### 🔧 Refactoring

- **User Stories** split into 6 themed files by problem domain:
  `us_core.rst`, `us_change_mgmt.rst`, `us_traceability.rst`, `us_installation.rst`, `us_developer_experience.rst`, `us_release.rst`
- **Requirements** split into 6 matching files (1:1 mapping with US themes):
  `req_core.rst`, `req_change_mgmt.rst`, `req_traceability.rst`, `req_installation.rst`, `req_developer_experience.rst`, `req_release.rst`
- **Design Specs** kept as solution-domain files (intentional asymmetry), IDs renamed
- All `:links:` directives updated across 35 files
- Agent files, workflow, and traceability indices updated for new IDs

### 📚 Documentation

- **New**: methodology.md — File organization guide (problem vs solution domain, scaling rules)
- **New**: namingconventions.md — Descriptive ID naming convention (`<TYPE>_<THEME>_<SLUG>`)
- **New**: Project logo (light & dark mode SVG)
- **Rewritten**: README.md — concise, centered logo, link to full docs
- **Rewritten**: docs/index.rst — engaging landing page with Getting Started, FAQ
- **Updated**: copilot-instructions.md — new ID examples, file organization section

### 📝 Migration Notes

Previous releases used sequential IDs (`US_SYSPILOT_001`, `REQ_SYSPILOT_007`). All historical release notes preserve the original IDs for accuracy. New development should use the descriptive ID format documented in namingconventions.md.

---

*For detailed traceability, see the [documentation](https://enthali.github.io/syspilot/)*

## v0.1.0-beta.3 - 2026-01-31

### Summary
Bugfix release improving installation UX. Setup Agent now auto-detects syspilot location instead of requiring manual path input, fixing the primary installation scenario where users extract release ZIPs with nested directory structures.

### 🐛 Bug Fixes

- **Auto-Detection for Setup** (US_SYSPILOT_012-013)
  - Setup Agent no longer asks for syspilot path (REQ_SYSPILOT_019, AC-4/AC-5)
  - Find-SyspilotInstallation function searches parent directories (REQ_SYSPILOT_024, SPEC_SYSPILOT_014)
  - Parses version.json to find syspilot installations (REQ_SYSPILOT_024, AC-1/AC-2)
  - Semantic version comparison selects newest (REQ_SYSPILOT_024, AC-3)
  - Supports pre-release versions (beta.2 vs beta.3) (REQ_SYSPILOT_024, AC-3)
  - Logs all found versions for transparency (REQ_SYSPILOT_024, AC-6)
  - Graceful error with helpful instructions on failure (REQ_SYSPILOT_024, AC-5)

- **Update Workflow Implementation** (US_SYSPILOT_014)
  - Setup Agent detects existing installation via .syspilot/version.json (SPEC_SYSPILOT_010)
  - Automatic GitHub latest release fetch via API (REQ_SYSPILOT_021, SPEC_SYSPILOT_010)
  - Semantic version comparison (current vs latest) (REQ_SYSPILOT_021, AC-5)
  - Backup/rollback mechanism (.syspilot → .syspilot_backup) (SPEC_SYSPILOT_010)
  - Download and extract release ZIP automatically (SPEC_SYSPILOT_010)
  - Intelligent merge for user-modified agent files (SPEC_SYSPILOT_009)
  - Validation via sphinx-build with automatic rollback on failure (SPEC_SYSPILOT_010)

### 📚 Documentation

- A-SPICE alignment extended with agent responsibilities
- Coverage table showing which A-SPICE process areas are supported
- Test pyramid documented (current: generic TEST_*, planned: UNIT/INTEG/ACCEPT types)
- Clear separation of agent responsibilities (Change=specs, Implement=code, Verify=validation)

### 🔧 Technical Details

- New requirement: REQ_SYSPILOT_024 (Auto-Detection via version.json)
- New design spec: SPEC_SYSPILOT_014 (PowerShell Find-SyspilotInstallation)
- Updated: REQ_SYSPILOT_019, REQ_SYSPILOT_020, REQ_SYSPILOT_021 (use auto-detection)
- Updated: SPEC_SYSPILOT_008 (Setup Agent), SPEC_SYSPILOT_010 (Update Process)
- Algorithm: Search 3 parent levels, recursive file search depth 3, semantic version sort

### 📝 Known Limitations

- Auto-detection and update workflow tested on Windows PowerShell (Bash versions need testing)
- GitHub repo URL hardcoded as TODO in Setup Agent (needs configuration mechanism)

---

*For detailed traceability, see the [documentation](https://enthali.github.io/syspilot/)*

## v0.1.0-beta.2 - 2026-01-30

### Summary
Second beta release adding installation/update system and complete release automation. This release introduces a robust two-step installation workflow, automated GitHub release pipeline, and the Release Agent for guided release management. These improvements transform syspilot from a prototype into a maintainable, distributable toolkit.

### ✨ New Features

- **Installation & Update System** (US_SYSPILOT_012-014)
  - Two-step install: Minimal bootstrap script → Interactive Setup Agent (REQ_SYSPILOT_018, SPEC_SYSPILOT_007)
  - Dependency checking with user confirmation (REQ_SYSPILOT_019, SPEC_SYSPILOT_008)
  - Version tracking via version.json (REQ_SYSPILOT_021, SPEC_SYSPILOT_009)
  - Backup/rollback mechanism for safe updates (REQ_SYSPILOT_021, SPEC_SYSPILOT_010)
  - Intelligent merge for user-modified agent files (REQ_SYSPILOT_021, SPEC_SYSPILOT_010)
  - Single source of truth: .github/ directory (REQ_SYSPILOT_022, SPEC_SYSPILOT_009)
  - Bootstrap scripts for Windows (init.ps1) and Linux/Mac (init.sh) (REQ_SYSPILOT_023, SPEC_SYSPILOT_004)

- **Release Automation** (US_SYSPILOT_015-017)
  - Semantic versioning with pre-release support (REQ_RELEASE_001, SPEC_RELEASE_001)
  - GitHub Releases with automatic source archives (REQ_RELEASE_002, SPEC_RELEASE_002)
  - Structured release notes with traceability (REQ_RELEASE_003, SPEC_RELEASE_003)
  - Pre-release validation checklist (REQ_RELEASE_004, SPEC_RELEASE_004)
  - GitHub Actions workflow for automated publishing (REQ_RELEASE_005-006, SPEC_RELEASE_005-006)
    - Validates version.json matches tag
    - Builds Sphinx documentation
    - Publishes to GitHub Pages
    - Creates GitHub Release with release notes
  - Release Agent for guided release workflow (REQ_RELEASE_007-008, SPEC_RELEASE_007)
    - Pre-flight check with merge guidance
    - Change Document analysis for release note generation
    - Interactive validation and tagging
    - Required cleanup of processed Change Documents

### 📚 Documentation

- Installation process documented in US_SYSPILOT_012-014
- Release process fully documented in US_SYSPILOT_015-017
- 8 new requirements (REQ_RELEASE_001-008), 7 new design specs (SPEC_RELEASE_001-007)
- docs/releasenotes.md created as canonical release history
- .github/workflows/release.yml documented with inline comments

### 🔧 Internal Changes

- Implement Agent: Clarified NOT to change spec statuses (only Verify Agent does)
- Verify Agent: Added post-verification status update (approved → implemented)
- Verify Agent: Added handoff to Release Agent after verification
- Setup Agent: Enhanced with Section 2 "Check Dependencies (Interactive)"
- All core syspilot specs (US_001-017, REQ_001-027, SPEC_001-013) updated to status: implemented

### 🔨 Technical Details

- GitHub Actions: peaceiris/actions-gh-pages@v4, softprops/action-gh-release@v1
- Release workflow: 4 jobs (validate, build-docs, publish-docs, create-release)
- Release Agent: 8-step workflow with YAML frontmatter for agent handoffs
- Bootstrap scripts: Minimal (28 lines PS, 27 lines Bash) - logic moved to Setup Agent
- Atomic feature branch workflow: Everything in branch → squash merge → immediate release

### 📝 Known Limitations

- First test of complete release automation (experimental)
- Graphviz integration still not working on Windows (optional feature)
- No test suite yet (coming in future releases)

---

*For detailed traceability, see the [documentation](https://enthali.github.io/syspilot/)*

## v0.1.0-beta - 2026-01-30

### Summary
Initial beta release of syspilot, a requirements engineering toolkit using sphinx-needs traceability for AI-assisted development. Includes core agent system, documentation framework, and installation workflows.

### ✨ Features

- **Agent System** (US_SYSPILOT_001-009)
  - Setup Agent: Install/update syspilot in projects (REQ_SYSPILOT_001-006)
  - Change Agent: Analyze requests level-by-level (REQ_SYSPILOT_007-012)
  - Implement Agent: Execute changes with traceability (REQ_SYSPILOT_013-016)
  - Verify Agent: Check implementation matches specs (REQ_SYSPILOT_017)
  - MECE Agent: Validate completeness (REQ_SYSPILOT_019)
  - Trace Agent: Follow links through levels (REQ_SYSPILOT_020)
  - Memory Agent: Keep instructions current (REQ_SYSPILOT_021)

- **Installation & Updates** (US_SYSPILOT_012-014)
  - Bootstrap scripts for Windows/Linux (REQ_SYSPILOT_022-024)
  - Backup/rollback mechanism (REQ_SYSPILOT_025)
  - Intelligent merge for user-modified agents (REQ_SYSPILOT_026)
  - Single source of truth in .github/ (REQ_SYSPILOT_027)

- **Documentation Framework** (US_SYSPILOT_010-011)
  - Sphinx with sphinx-needs traceability (SPEC_SYSPILOT_001)
  - Three-level hierarchy: User Stories → Requirements → Design (SPEC_SYSPILOT_002)
  - Link discovery utility (SPEC_SYSPILOT_009)
  - A-SPICE process alignment (SPEC_SYSPILOT_010)

- **Change Management** (US_SYSPILOT_005-009)
  - Change Document template (SPEC_SYSPILOT_003)
  - Level-by-level analysis workflow (SPEC_SYSPILOT_004)
  - Horizontal MECE checks (SPEC_SYSPILOT_005)

### 📚 Documentation

- Self-documentation using dogfooding approach
- 14 User Stories, 27 Requirements, 13 Design Specs
- Automotive SPICE alignment documentation
- Installation guide and agent reference

### 🔧 Dependencies

- sphinx >= 7.0.0
- sphinx-needs >= 2.0.0
- furo >= 2024.0.0 (theme)
- myst-parser >= 2.0.0
- graphviz >= 0.20.0 (optional, for diagrams)

### 📝 Known Limitations

- No automated release process yet (manual tagging)
- Graphviz integration not working on Windows (optional feature)
- No test suite (coming in future releases)

---

*For detailed traceability, see the [documentation](https://enthali.github.io/syspilot/)*
