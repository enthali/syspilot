Change Agent Design
====================

Design specifications for the Change Agent — iterative level-based change analysis.

**Document Version**: 0.1
**Last Updated**: 2026-02-06


.. spec:: Iterative Level Processing
   :id: SPEC_CHG_LEVEL_PROCESSING
   :status: implemented
   :links: REQ_CHG_ANALYSIS_AGENT, REQ_CHG_WORKFLOW_STEPS, REQ_CHG_LINK_DISCOVERY, REQ_DX_AGENT_SELECTION_MENUS
   :tags: change, agent, workflow

   **Design:**
   The Change Agent processes change requests one level at a time,
   following the hierarchy US → REQ → SPEC with user discussion at each level.

   **Level Definitions:**

   * Level 0: User Stories (WHY — stakeholder perspective)
   * Level 1: Requirements (WHAT — observable system behavior)
   * Level 2: Design (HOW — technical implementation decisions)

   **Processing Flow per Level:**

   1. **Identify Affected Items** — Search docs at current level using horizontal
      search (Level 0) or upward links from previous level (Levels 1–2)
   2. **Horizontal MECE Check** — Check linked/related items for overlaps,
      contradictions, and gaps (scoped to affected subset, not entire level)
   3. **Propose Changes** — Present new/modified items with rationale
   4. **Discuss with User** — Resolve questions and conflicts interactively
   5. **Update Change Document** — Record agreements immediately
   6. **Ask Navigation** — Confirm that the current level is saved to the
      Change Document, then present navigation using ``ask_questions``:
      "Level N is saved to the Change Document. Where do you want to continue?"
      Options: Proceed to Level N+1 / Revise Level N-1 / Pause
      (see SPEC_AGENT_INTERACTION for format)

   **Don't Skip Levels Rule:**
   Even if the answer seems obvious, the agent processes each level
   systematically to ensure complete traceability (US → REQ → SPEC).

   **Link Discovery:**
   Uses ``scripts/python/get_need_links.py`` to find impacted elements:

   ::

      # Find linked items for a specific ID
      python scripts/python/get_need_links.py <ID> --simple

      # Trace with depth
      python scripts/python/get_need_links.py <ID> --flat --depth 3

   **File:** ``.github/agents/syspilot.change.agent.md``


.. spec:: Change Document Management
   :id: SPEC_CHG_CHANGE_DOCUMENT
   :status: implemented
   :links: REQ_CHG_CHANGE_DOC, REQ_CHG_ANALYSIS_AGENT
   :tags: change, document, persistence

   **Design:**
   The Change Agent maintains a persistent Markdown document that records
   all analysis, decisions, and changes throughout the process.

   **Lifecycle:**

   1. **Create** — Derive short name (<15 chars) from user request
      (e.g., "iterative level processing" → ``iterative-level``)
   2. **Populate** — Copy from ``templates/change-document.md``
   3. **Update** — Record agreements immediately as they are reached
   4. **Simplify** — After final approval, reduce to ID/title summary
   5. **Delete** — After merge (preserved in Git history)

   **Location:** ``docs/changes/<name>.md``

   **Content Modes:**

   * **During Analysis (verbose):** Full RST content for each new/modified
     element embedded in the Change Document. Enables conversation compression
     and session pause/resume without context loss.
   * **After Approval (simplified):** Only affected IDs and titles.
     Full RST content moved to actual ``.rst`` files.

   **Example (during analysis):**

   ::

      ## Level 1: Requirements

      ### New Requirements

      #### REQ_REL_SEMVER: Semantic Versioning

      ```rst
      .. req:: Semantic Versioning
         :id: REQ_REL_SEMVER
         :status: draft
         ...
      ```

   **Example (after approval):**

   ::

      ## Level 1: Requirements

      ### New Requirements
      - REQ_REL_SEMVER: Semantic Versioning
      - REQ_REL_GITHUB_PUBLISH: GitHub Release Publication


.. spec:: Bidirectional Level Navigation
   :id: SPEC_CHG_BIDIR_NAVIGATION
   :status: implemented
   :links: REQ_CHG_BIDIR_NAV, REQ_CHG_ANALYSIS_AGENT
   :tags: change, navigation

   **Design:**
   The Change Agent supports navigating back to any previous level
   when design feasibility issues or requirement adjustments are needed.

   **Trigger:** User says "go back to requirements" or "the user story needs
   adjustment" at any point during analysis.

   **Navigation Procedure:**

   1. Navigate to the requested level section in the Change Document
   2. Make necessary changes to that level
   3. Mark all lower level sections with: ``**⚠️ DEPRECATED — NEEDS REVIEW**``
   4. Continue working forward from the requested level

   **Preservation:** Previous level work is preserved in the Change Document.
   Each iteration is marked so the full decision history is retained.

   **Rationale:** Design feasibility issues may require requirement changes,
   which may require user story adjustments. Linear-only processing
   would force restarting the entire analysis.


.. spec:: Atomic RST Updates with Status Lifecycle
   :id: SPEC_CHG_ATOMIC_UPDATE
   :status: implemented
   :links: REQ_CHG_ANALYSIS_AGENT, REQ_CHG_FINAL_CHECK, REQ_CHG_MECE_PER_LEVEL
   :tags: change, commit, status

   **Design:**
   RST files are only updated after final approval of all levels together,
   never during analysis. This prevents broken cross-level links.

   **Status Lifecycle:**

   * **During analysis:** All new/modified elements set to ``:status: draft``
     (in Change Document only, not in RST files)
   * **After final approval:** Change Agent atomically writes all RST files
     (US + REQ + SPEC together) and sets ``:status: approved``
   * **After implementation:** Verify Agent sets ``:status: implemented``

   **Final Consistency Check (before writing RST):**

   1. **Traceability** — Every REQ links to a US, every SPEC links to a REQ
   2. **Cross-Level Consistency** — No semantic drift between levels
   3. **MECE Across Levels** — All US aspects covered by REQs, all REQs by SPECs
   4. **Document Completeness** — No DEPRECATED markers remaining
   5. **User Approval** — Explicit sign-off before writing

   **After Writing:**

   * RST files updated atomically (all levels in one operation)
   * Change Document simplified to ID/title summary
   * Changes committed with traceability message

   **Rationale:** Atomic updates ensure ``sphinx-build`` always succeeds.
   Writing levels individually would create periods with broken links.


Traceability
------------

.. needtable::
   :columns: id, title, status, links
   :filter: id.startswith('SPEC_CHG')
