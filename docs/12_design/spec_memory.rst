Memory Agent Design
====================

Design specifications for the Memory Agent — project memory maintenance.

**Document Version**: 0.2
**Last Updated**: 2026-02-11


.. spec:: Memory Update Process
   :id: SPEC_MEM_UPDATE_PROCESS
   :status: implemented
   :links: REQ_DX_MEMORY_AGENT
   :tags: memory, agent, workflow

   **Design:**
   The Memory Agent follows a three-step process to keep
   ``copilot-instructions.md`` synchronized with the codebase.

   **Core Principle:**
   If an agent can learn it by reading an existing file, don't put it in
   copilot-instructions.md. The file contains only what agents **cannot
   easily discover** from the codebase.

   **Step 1 — Gather Current State:**

   * ``git log --oneline main..HEAD`` or recent commits on main
   * ``copilot-instructions.md`` — what's already documented
   * Directory structure — has anything moved?
   * New agent/skill/prompt files — do naming conventions need updating?

   **Step 2 — Identify Gaps:**

   Compare documented state vs reality. Focus on:

   * Structure: Did directories change?
   * Conventions: New naming patterns or file types?
   * Workflows: Changed agent chain or handoffs?
   * Commands: Build or query commands changed?
   * Tech stack: New tools?
   * Version: Has ``version.json`` been bumped?

   Before adding anything, ask: *"Can the agent discover this by reading
   an existing file?"* — if yes, don't add (at most add a one-line pointer).

   **Step 3 — Apply Updates:**

   Add, modify, or remove sections. Commit the change.

   **Invocation:** Invoked after verify in the change workflow.
   Hands off to change (for another change) or release (to bundle into a release).

   **File:** ``.github/agents/syspilot.memory.agent.md``


.. spec:: Memory Content Rules
   :id: SPEC_MEM_CONTENT_CATEGORIES
   :status: implemented
   :links: REQ_DX_MEMORY_AGENT
   :tags: memory, content, structure

   **Design:**
   The Memory Agent decides what belongs in copilot-instructions.md using
   a single criterion: **discoverability**.

   **Include (not discoverable from code):**

   * Project structure and mental map (directory tree with folder purposes)
   * Naming conventions and ID schemes (hard to infer from files alone)
   * Workflow chains and agent handoffs (cross-cutting, not in any one file)
   * Build commands (agents need these before reading docs)
   * Specification hierarchy and theme abbreviations

   **Exclude (discoverable from existing files):**

   * ❌ Directive format examples (visible in every RST file)
   * ❌ Status value lists (visible in specs)
   * ❌ RST formatting rules (follow existing files)
   * ❌ Dependency lists (agents can read ``requirements.txt``)
   * ❌ Installation/release workflow details (each agent has its own file)
   * ❌ Key files table (discoverable from project structure tree)
   * ❌ Element counts or current state checklists (stale within one commit)
   * ❌ Per-file listings inside directory levels
   * ❌ Duplicate info — link to the source instead

   **Rule of thumb:** If it changes every commit, it shouldn't be documented.
   If another file already says it, link don't copy.


.. spec:: copilot-instructions.md Structure
   :id: SPEC_MEM_INSTRUCTIONS_STRUCTURE
   :status: implemented
   :links: REQ_DX_MEMORY_AGENT
   :tags: memory, structure, template

   **Design:**
   The Memory Agent maintains a fixed set of sections in
   ``copilot-instructions.md``. Resist adding new top-level sections.

   **Target Structure:**

   ::

      # [Project Name] - Copilot Instructions

      ## Project Overview          — 3-5 lines, version
      ## Tech Stack                — bullet list, no versions
      ## Project Structure         — directory tree (no per-file listings)
      ## Specification Hierarchy   — 3-level diagram with prefixes
      ## Agent System              — table: agent → purpose
      ## Sphinx-Needs Conventions  — ID prefixes, theme abbreviations
      ## Development Commands      — build + query commands only
      ## Development Workflow      — agent chain diagram, one-liners
      ## Patterns & Conventions    — file organization, file naming, authoring
      ## Agent Interaction         — skill file activation reference

   **Size target:** ~150–180 lines. If it grows past 200, something should
   be cut.

   **Location:** ``.github/copilot-instructions.md``

   **Update Frequency:** After each verify pass or on-demand when
   significant structural changes occur.


Traceability
------------

.. needtable::
   :columns: id, title, status, links
   :filter: id.startswith('SPEC_MEM')
