Change Agent Design
====================

Design specifications for the Change Agent — iterative level-based change analysis.

**Document Version**: 0.1
**Last Updated**: 2026-02-06


.. spec:: Iterative Level Processing
   :id: SYSPILOT_SPEC_CHG_LEVEL_PROCESSING
   :status: implemented
   :links: SYSPILOT_REQ_CHG_ANALYSIS_AGENT, SYSPILOT_REQ_CHG_WORKFLOW_STEPS, SYSPILOT_REQ_CHG_LINK_DISCOVERY, SYSPILOT_REQ_DX_AGENT_SELECTION_MENUS
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
   5. **Update Change Document** — Record agreements (IDs + rationale) immediately
   6. **Write RST** — Write all new/modified elements for this level with
      ``:status: draft``; trigger sphinx-build to update ``needs_id/`` data
      (see ``SYSPILOT_SPEC_CHG_LIVE_RST_PER_LEVEL``)
   7. **MECE Advisory** — Invoke MECE Agent as subagent scoped to this level;
      present findings to user (advisory, non-blocking)
   8. **Ask Navigation** — Confirm that the current level is written and saved,
      then present navigation using ``ask_questions``:
      "Level N is written and saved. Where do you want to continue?"
      Options: Proceed to Level N+1 / Revise Level N-1 / Pause
      (see SYSPILOT_SPEC_AGENT_INTERACTION for format)

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
   :id: SYSPILOT_SPEC_CHG_CHANGE_DOCUMENT
   :status: implemented
   :links: SYSPILOT_REQ_CHG_CHANGE_DOC, SYSPILOT_REQ_CHG_ANALYSIS_AGENT
   :tags: change, document, persistence

   **Design:**
   The Change Agent maintains a persistent Markdown document that records
   all analysis, decisions, and changes throughout the process.

   **Lifecycle:**

   1. **Create** — Derive short name (<15 chars) from user request
      (e.g., "iterative level processing" → ``iterative-level``)
   2. **Populate** — Copy from ``.syspilot/templates/change-document.md``
   3. **Update** — Record agreements immediately as they are reached
   4. **Simplify** — After final approval, reduce to ID/title summary
   5. **Archive** — After merge, move Change Document and validation report
      to ``docs/changes/archive/``

   **Location:** ``docs/changes/<name>.md``

   **Content Format:**
   The Change Document is always in decision log format from the start: affected IDs,
   rationale, and decisions. No verbose RST blocks are embedded. Since RSTs are written
   per-level immediately after user approval, the Change Document does not need to carry
   full RST content for session resume — the RST files themselves serve that purpose.

   **Example:**

   ::

      ## Level 1: Requirements

      ### New Requirements
      - SYSPILOT_REQ_REL_SEMVER: Semantic Versioning — new because versioning not yet specified

      ### Modified Requirements
      - SYSPILOT_REQ_INST_GITHUB_RELEASES: Clarified to specify GitHub Releases

      ### Decisions
      - D-1: Use semantic versioning (MAJOR.MINOR.PATCH) per industry standard


.. spec:: Bidirectional Level Navigation
   :id: SYSPILOT_SPEC_CHG_BIDIR_NAVIGATION
   :status: implemented
   :links: SYSPILOT_REQ_CHG_BIDIR_NAV, SYSPILOT_REQ_CHG_ANALYSIS_AGENT
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
   4. Inform the user which already-written lower-level RSTs may be inconsistent
      due to the backward revision; user decides whether and how to update those
      RST files before continuing forward

   **Preservation:** Previous level work is preserved in the Change Document.
   Each iteration is marked so the full decision history is retained.

   **Rationale:** Design feasibility issues may require requirement changes,
   which may require user story adjustments. Linear-only processing
   would force restarting the entire analysis.


.. spec:: Atomic RST Updates with Status Lifecycle
   :id: SYSPILOT_SPEC_CHG_ATOMIC_UPDATE
   :status: deprecated
   :links: SYSPILOT_REQ_CHG_ANALYSIS_AGENT, SYSPILOT_REQ_CHG_FINAL_CHECK, SYSPILOT_REQ_CHG_MECE_PER_LEVEL, SYSPILOT_SPEC_CHG_LEVEL_PROCESSING
   :tags: change, commit, status

   .. note::
      This spec is deprecated. It is superseded by
      ``SYSPILOT_SPEC_CHG_LIVE_RST_PER_LEVEL`` (per-level RST write after user
      approval of each level).

   **Design (historical):**
   RST files were only updated after final approval of all levels together.

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


.. spec:: Per-Level RST Write and MECE Delegation
   :id: SYSPILOT_SPEC_CHG_LIVE_RST_PER_LEVEL
   :status: implemented
   :links: SYSPILOT_REQ_CHG_LIVE_RST_PER_LEVEL, SYSPILOT_REQ_CHG_MECE_PER_LEVEL
   :tags: change, rst, mece, subagent

   **Design:**
   After the user approves a level during Change Agent analysis, the agent SHALL
   execute the following write-and-validate sequence:

   1. Write all new/modified RST elements for that level with ``:status: draft``
   2. Trigger ``sphinx-build`` to update ``docs/_build/html/needs_id/`` data
   3. Invoke the MECE Agent as a subagent via ``runSubagent("syspilot.mece", ...)``
      scoped to the level just written
   4. Present MECE findings to the user as advisory (non-blocking)
   5. Proceed to next level (user may review findings first)

   **Status Lifecycle:**

   * Per-level write: ``:status: draft``
   * After final approval of all levels: Change Agent updates all touched
     elements introduced in this change to ``:status: approved``
   * After implementation: Verify Agent sets ``:status: implemented``

   **Subagent Invocation:**

   * Tool: ``runSubagent("syspilot.mece", ...)``
   * Scope: the level just written (e.g. "Level 1 Requirements, affected IDs: ...")
   * Result: MECE Agent returns findings or "no issues found"
   * Advisory: findings shown to user, no automatic blocking or rollback
   * Prerequisite: ``agents: ["syspilot.mece", "syspilot.trace"]`` must be present
     in the Change Agent YAML frontmatter to enable ``runSubagent()`` invocation

   **sphinx-build Requirement:**
   sphinx-build must run between the RST write and the MECE subagent invocation
   so that ``needs_id/`` data reflects the newly written elements.

   **File:** ``.github/agents/syspilot.change.agent.md``


Traceability
------------

.. needtable::
   :columns: id, title, status, links
   :filter: id.startswith('SYSPILOT_SPEC_CHG')
