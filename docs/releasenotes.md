# syspilot Release Notes

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
