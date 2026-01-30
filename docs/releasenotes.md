# syspilot Release Notes

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
