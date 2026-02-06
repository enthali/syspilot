Memory Agent Design
====================

Design specifications for the Memory Agent — project memory maintenance.

**Document Version**: 0.1
**Last Updated**: 2026-02-06


.. spec:: Memory Update Process
   :id: SPEC_MEM_UPDATE_PROCESS
   :status: implemented
   :links: REQ_DX_MEMORY_AGENT
   :tags: memory, agent, workflow

   **Design:**
   The Memory Agent follows a four-step process to keep
   ``copilot-instructions.md`` synchronized with the codebase.

   **Step 1 — Gather Current State:**

   Read these sources to understand what has changed:

   * Git history (recent commits and messages)
   * Directory structure (current file organization)
   * Package files (pyproject.toml, requirements.txt)
   * README.md (current documentation)
   * Existing copilot-instructions.md (what's already documented)

   **Step 2 — Identify Gaps:**

   Compare current state vs documented state across all categories:

   ::

      | Aspect   | Documented | Current | Action      |
      |----------|------------|---------|-------------|
      | Features | [list]     | [list]  | Add/Remove  |
      | Files    | [list]     | [list]  | Update      |
      | Patterns | [list]     | [list]  | Document    |

   **Step 3 — Propose Updates:**

   Present additions, modifications, and deletions to the user with
   rationale for each change.

   **Step 4 — Apply Updates:**

   Update ``.github/copilot-instructions.md`` with clear, concise descriptions,
   accurate file paths, current commands, and relevant examples.

   **Invocation:** Invoked after verify in the change workflow.
   Hands off to change (for another change) or release (to bundle into a release).

   **File:** ``.github/agents/syspilot.memory.agent.md``


.. spec:: Memory Content Categories
   :id: SPEC_MEM_CONTENT_CATEGORIES
   :status: implemented
   :links: REQ_DX_MEMORY_AGENT
   :tags: memory, content, structure

   **Design:**
   The Memory Agent tracks six categories of project information
   and maintains explicit exclusion rules.

   **Categories to Track:**

   1. **Project Overview** — Capabilities, scope, tech stack
   2. **Directory Structure** — New directories, reorganizations, folder purposes
   3. **Key Files** — Important files, changed purposes, deprecated files
   4. **Patterns & Conventions** — Coding patterns, naming conventions,
      architecture decisions
   5. **Development Guidelines** — Workflow steps, build commands, testing procedures
   6. **Dependencies** — New/removed/updated dependencies

   **Exclusion Rules (What NOT to Include):**

   * ❌ Detailed implementation specifics (that's in the code)
   * ❌ Every single file (only key/important ones)
   * ❌ Temporary workarounds (unless long-term)
   * ❌ Personal preferences (only team conventions)
   * ❌ Duplicate information (link to docs instead)

   **Rationale:** The exclusion rules prevent copilot-instructions.md from
   becoming a dump of all project information. It should be a concise
   "constitution" that gives any new Copilot session full project context.


.. spec:: copilot-instructions.md Structure
   :id: SPEC_MEM_INSTRUCTIONS_STRUCTURE
   :status: implemented
   :links: REQ_DX_MEMORY_AGENT
   :tags: memory, structure, template

   **Design:**
   The Memory Agent maintains a canonical structure for ``copilot-instructions.md``.

   **Required Sections:**

   ::

      # [Project Name] - Copilot Instructions

      ## Project Overview
      ## Tech Stack
      ## Project Structure
      ## Key Files
      ## Development Setup
      ## Common Commands
      ## Architecture
      ## Patterns & Conventions
      ## Current State
      ## Known Issues

   **Quality Criteria:**

   * Every section has clear, concise descriptions
   * File paths are accurate and current
   * Commands and versions are up-to-date
   * Code examples are relevant and working

   **Location:** ``.github/copilot-instructions.md``

   **Update Frequency:** After each verify pass or on-demand when
   significant structural changes occur.


Traceability
------------

.. needtable::
   :columns: id, title, status, links
   :filter: id.startswith('SPEC_MEM')
