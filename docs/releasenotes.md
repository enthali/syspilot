# syspilot Release Notes

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
