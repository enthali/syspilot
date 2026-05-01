Documentation Scope
===================

Design specifications defining the structure and content of each documentation file.


.. spec:: README Structure
   :id: SYSP_SPEC_DOC_README
   :status: draft
   :tags: agent-v2, documentation, external, readme
   :links: SYSP_REQ_DOC_README, SYSP_SPEC_AGENT_ARCH_SOUL, SYSP_SPEC_PM_SOUL, SYSP_SPEC_CM_SOUL, SYSP_SPEC_QM_SOUL, SYSP_SPEC_DESIGN_SOUL, SYSP_SPEC_IMPLEMENT_SOUL, SYSP_SPEC_UAT_SOUL, SYSP_SPEC_DOCU_SOUL, SYSP_SPEC_MECE_SOUL, SYSP_SPEC_TRACE_SOUL, SYSP_SPEC_RELEASE_SOUL, SYSP_SPEC_SETUP_SOUL

   **File:** ``README.md`` (repository root)

   **Current Content:**

   * Logo and tagline ("Requirements Engineering that scales with AI")
   * Value proposition (O(affected) not O(total))
   * Quick Start section with platform-specific install commands (Linux/Mac, Windows)
   * Agent table listing 8 agents with brief descriptions
   * "How It Works" diagram showing the US → REQ → SPEC link chain
   * Link to full documentation site
   * Requirements (VS Code + GitHub Copilot, Python 3.10+)
   * License (Apache 2.0)

   **Required Sections:**

   1. Logo and tagline
   2. Value proposition / elevator pitch
   3. Quick Start with install commands per platform
   4. Agent overview table
   5. How it works (specification link chain)
   6. Link to full docs
   7. Requirements
   8. License

   **Status Notes:**
   The README currently covers the v2 agent architecture with 8 agents.
   Needs review to confirm the agent table matches the current agent set.


.. spec:: Methodology Structure
   :id: SYSP_SPEC_DOC_METHODOLOGY
   :status: draft
   :tags: agent-v2, documentation, external, methodology
   :links: SYSP_REQ_DOC_METHODOLOGY, SYSP_SPEC_AGENT_ARCH_SOUL, SYSP_SPEC_AGENT_ARCH_DUTIES, SYSP_SPEC_AGENT_ARCH_WORKFLOW, SYSP_SPEC_AGENT_ARCH_FRONTMATTER, SYSP_SPEC_SETUP_WORKFLOW

   **File:** ``docs/methodology.md``

   **Current Content:**

   * Overview of spec-driven development
   * Agent Families concept (syspilot, sysmlv2, common)
   * Repository structure — family directories (product) and documentation structure (specs)
   * Installation directory layout
   * ID naming convention (FAMILY_TYPE_THEME_SLUG)
   * Specification levels (US → REQ → SPEC) with directives

   **Required Sections:**

   1. Overview — spec-driven development philosophy
   2. Agent Families — concept, table, per-family artifacts
   3. Repository Structure — product dirs, spec dirs, install dirs
   4. ID Naming Convention — format, family prefixes, type abbreviations
   5. Specification Levels — three levels with descriptions

   **Status Notes:**
   The methodology describes the family framework well. May need updates
   as the agent architecture v2 stabilizes to ensure consistency with
   copilot-instructions.md.


.. spec:: Architecture Structure
   :id: SYSP_SPEC_DOC_ARCHITECTURE
   :status: draft
   :tags: agent-v2, documentation, external, architecture
   :links: SYSP_REQ_DOC_ARCHITECTURE, SYSP_SPEC_AGENT_ARCH_SOUL, SYSP_SPEC_AGENT_ARCH_DUTIES, SYSP_SPEC_AGENT_ARCH_WORKFLOW, SYSP_SPEC_AGENT_ARCH_FRONTMATTER, SYSP_SPEC_SETUP_DUTIES, SYSP_SPEC_SETUP_WORKFLOW

   **File:** ``docs/architecture.md``

   **Current Content:**

   * Overview — separation of Product from Installation
   * Why the separation (reusability, update safety, clear ownership)
   * What is Product — contents of ``syspilot/`` directory
   * How Installation works — Setup Agent flow with Mermaid diagram
   * Concrete example: Release Agent (product → spec → installed copy)
   * File ownership model

   **Required Sections:**

   1. Overview — Product vs. Installation concept
   2. Motivation — why this separation exists
   3. Product definition — what lives in ``syspilot/``
   4. Installation flow — Setup Agent copies product to ``.github/``
   5. Concrete example demonstrating the pattern
   6. File ownership (methodology-owned vs. project-owned)

   **Status Notes:**
   Architecture document is comprehensive and well-structured.
   May need review once agent architecture v2 defines new ownership rules.


.. spec:: Workflows Structure
   :id: SYSP_SPEC_DOC_WORKFLOWS
   :status: approved
   :tags: agent-v2, documentation, external, workflows
   :links: SYSP_REQ_DOC_WORKFLOWS, SYSP_SPEC_PM_WORKFLOW, SYSP_SPEC_CM_WORKFLOW, SYSP_SPEC_QM_WORKFLOW, SYSP_SPEC_DESIGN_WORKFLOW, SYSP_SPEC_IMPLEMENT_WORKFLOW, SYSP_SPEC_UAT_WORKFLOW, SYSP_SPEC_DOCU_WORKFLOW, SYSP_SPEC_MECE_WORKFLOW, SYSP_SPEC_TRACE_WORKFLOW, SYSP_SPEC_RELEASE_WORKFLOW, SYSP_SPEC_SETUP_WORKFLOW, SYSP_SPEC_SKILL_BRANCHING_STRATEGY, SYSP_SPEC_SKILL_ORCHESTRATION_PATTERN

   **File:** ``docs/workflows.md``

   **Current Content:**

   * Overview — three workflows (Change, Quality, Release)
   * Change Workflow: design → implement → uat → verify → docu, with per-agent detail
   * Quality Workflow: independent read-only analysis (mece, trace)
   * Release Workflow section

   **Required Sections:**

   1. Overview — workflow table (Change, Quality, Release)
   2. Change Workflow — agent sequence with Mermaid diagram, per-agent input/output
   3. Quality Workflow — independent checks, agents involved
   4. Release Workflow — bundling and publishing process

   **Status Notes:**
   Workflows document describes the current agent sequence accurately.
   Needs review to ensure the memory agent step is still current and
   that the v2 agent names match. The Design Workflow and PM Workflow
   now include impact analysis steps (CR9) — ``docs/workflows.md`` must
   be updated to reflect the impact analysis skill usage in both workflows.
   The CM workflow now includes an Intent Gate step (reason about underlying
   intent and consult user when a CR contains implementation instructions)
   and a Change Document creation step (first act after CR acceptance).
   The PM workflow now includes a CR Content Check step before delegation.


.. spec:: Naming Conventions Structure
   :id: SYSP_SPEC_DOC_NAMINGCONVENTIONS
   :status: draft
   :tags: agent-v2, documentation, external, naming
   :links: SYSP_REQ_DOC_NAMINGCONVENTIONS, SYSP_SPEC_AGENT_ARCH_FRONTMATTER

   **File:** ``docs/namingconventions.md``

   **Current Content:**

   * Overview — why descriptive IDs (comparison table: sequential vs. descriptive)
   * ID format: ``FAMILY_TYPE_THEME_SLUG``
   * Family prefixes (SYSP\_, SYSMLV2\_, INST\_, COMMON\_)
   * Type abbreviations (US, REQ, SPEC) with directives
   * Theme abbreviations (family-specific, referenced to family docs)
   * Directory naming conventions
   * Cross-family linking examples
   * Uniqueness enforcement via sphinx-needs
   * Slug guidelines

   **Required Sections:**

   1. Overview — rationale for descriptive IDs
   2. ID Format — pattern and components
   3. Family Prefixes — table with scope
   4. Type Abbreviations — level, directive mapping
   5. Theme Abbreviations — delegation to family docs
   6. Directory Naming — purpose and examples
   7. Cross-Family Linking — sphinx-needs resolution
   8. Slug Guidelines — length, specificity

   **Status Notes:**
   The naming conventions document is thorough and well-structured.
   Theme tables may need updating as agent architecture v2 introduces
   new themes or renames existing ones.


.. spec:: Release Notes Structure
   :id: SYSP_SPEC_DOC_RELEASENOTES
   :status: draft
   :tags: agent-v2, documentation, release-notes
   :links: SYSP_REQ_DOC_RELEASENOTES, SYSP_SPEC_RELEASE_WORKFLOW

   **File:** ``docs/releasenotes.md``

   **Current Content:**

   * Entries for v0.4.0 and v0.3.1 (reverse chronological)
   * Each entry contains: version, date, summary, new features, fixes, spec references
   * Uses emoji-prefixed sections (✨ New Features, 🔧 Fixes, 📋 Specs)

   **Required Sections per Entry:**

   1. Version heading with date (``## vX.Y.Z - YYYY-MM-DD``)
   2. Summary paragraph
   3. New Features section (``### ✨ New Features``)
   4. Fixes & Improvements section (``### 🔧 Fixes & Improvements``)
   5. Specs section (``### 📋 Specs``) listing new/modified spec IDs

   **Status Notes:**
   Release notes follow a consistent pattern. The format is established
   and does not require structural changes. Content will be added by the
   Release Engineer agent per release.


.. spec:: Copilot Instructions Template Guidance
   :id: SYSP_SPEC_DOC_COPILOT_INSTRUCTIONS
   :status: open
   :tags: agent-v2, documentation, internal, copilot-instructions
   :links: SYSP_REQ_DOC_COPILOT_INSTRUCTIONS, SYSP_SPEC_AGENT_ARCH_SOUL, SYSP_SPEC_SKILL_BRANCHING_STRATEGY, SYSP_SPEC_SKILL_ORCHESTRATION_PATTERN

   **File:** ``.github/copilot-instructions.md``

   **Ownership:** Project-owned. syspilot does not overwrite this file on update.

   **Purpose:** Always-loaded context for VS Code Copilot. Because it is always
   active, it must be kept concise. Detailed patterns belong in Skills.

   **Recommended Sections (project-specific):**

   1. Project identity — name, purpose, key insight
   2. Tech stack — tools, extensions
   3. Dev commands — build, query, test
   4. Safety rules — e.g. branch protection HARD RULEs
   5. Jarvis / role structure — if the project uses manager agents
   6. Pointers to skills — brief hints so agents know which skills exist
