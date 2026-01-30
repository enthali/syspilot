syspilot Requirements
=====================

This document contains requirements for the syspilot requirements engineering toolkit.

**Document Version**: 0.1  
**Last Updated**: 2026-01-28


Core Requirements
-----------------

.. req:: Requirements Management with sphinx-needs
   :id: REQ_SYSPILOT_001
   :status: implemented
   :priority: mandatory
   :tags: core, sphinx-needs
   :links: US_SYSPILOT_001

   **Description:**
   syspilot SHALL manage requirements in sphinx-needs RST format.

   **Rationale:**
   sphinx-needs provides structured requirements with automatic traceability,
   validation, and documentation generation.

   **Acceptance Criteria:**

   * AC-1: Requirements stored in ``.rst`` files with sphinx-needs directives
   * AC-2: Each requirement has unique ID, status, priority, and tags
   * AC-3: sphinx-build validates requirement syntax and links
   * AC-4: HTML documentation generated from requirements


.. req:: Design Specification with Traceability
   :id: REQ_SYSPILOT_002
   :status: implemented
   :priority: mandatory
   :tags: core, traceability
   :links: US_SYSPILOT_001, REQ_SYSPILOT_001

   **Description:**
   syspilot SHALL maintain design specifications linked to requirements.

   **Rationale:**
   Traceability from requirements to design ensures all requirements
   are addressed and design decisions are justified.

   **Acceptance Criteria:**

   * AC-1: Design specs use ``:links:`` to reference requirements
   * AC-2: sphinx-needs validates all links exist
   * AC-3: Traceability matrix auto-generated
   * AC-4: Orphan detection (specs without requirements, requirements without specs)


.. req:: Change Analysis Agent
   :id: REQ_SYSPILOT_003
   :status: implemented
   :priority: mandatory
   :tags: agent, change
   :links: US_SYSPILOT_002

   **Description:**
   syspilot SHALL provide a change agent that:

   1. Analyzes user requests against current specifications AND current implementation
   2. Produces a structured Change Document with analysis and decisions
   3. Updates US/REQ/SPEC RST files directly after user approval

   **Rationale:**
   The change agent has full context during analysis and should capture this
   in the specification immediately. Separating analysis from spec-writing
   would require duplicate work and risk information loss.

   **Acceptance Criteria:**

   * AC-1: Agent reads current User Stories, Requirements, and Design docs
   * AC-2: Agent reads current implementation (code, scripts, agents) to understand what exists
   * AC-3: Agent identifies affected US, REQ, and SPEC items
   * AC-4: Agent produces Change Document with analysis, decisions, and affected IDs
   * AC-5: Agent supports ADD, MODIFY, DELETE actions
   * AC-6: Agent detects conflicting requirements and discusses resolution with user
   * AC-7: Agent ensures every REQ change traces back to a User Story
   * AC-8: Agent updates US/REQ/SPEC RST files after user approval


.. req:: Implementation Agent with Full Traceability
   :id: REQ_SYSPILOT_004
   :status: implemented
   :priority: mandatory
   :tags: agent, implementation
   :links: US_SYSPILOT_003, REQ_SYSPILOT_001, REQ_SYSPILOT_002

   **Description:**
   syspilot SHALL provide an implement agent that:

   1. Reads the Change Document to identify affected SPECs
   2. Reads only the relevant SPEC sections as identified in the Change Document
   3. Implements code, scripts, and agents according to these SPECs
   4. Writes tests that verify the implementation
   5. Maintains traceability via comments and references

   **Rationale:**
   The Change Document provides focused context. The implement agent
   works only with the pre-identified scope, avoiding context overflow.

   **Acceptance Criteria:**

   * AC-1: Agent reads Change Document to get list of affected SPECs
   * AC-2: Agent reads only the SPECs identified in Change Document
   * AC-3: Agent runs sphinx-build to validate docs before coding
   * AC-4: Agent writes code with traceability comments (SPEC IDs)
   * AC-5: Agent writes tests referencing requirement IDs
   * AC-6: Agent runs tests and ensures they pass


.. req:: Verification Agent
   :id: REQ_SYSPILOT_005
   :status: implemented
   :priority: mandatory
   :tags: agent, verification
   :links: US_SYSPILOT_004, REQ_SYSPILOT_004

   **Description:**
   syspilot SHALL provide a verify agent that validates implementation
   completeness against the change proposal.

   **Rationale:**
   Verification ensures no requirements are missed and traceability
   is complete.

   **Acceptance Criteria:**

   * AC-1: Agent compares implementation to change proposal
   * AC-2: Agent checks all acceptance criteria have tests
   * AC-3: Agent validates traceability (REQ → SPEC → Code → Test)
   * AC-4: Agent produces verification report with PASS/PARTIAL/FAIL


.. req:: Project Memory Agent
   :id: REQ_SYSPILOT_006
   :status: implemented
   :priority: high
   :tags: agent, memory
   :links: US_SYSPILOT_006

   **Description:**
   syspilot SHALL provide a memory agent that maintains the project's
   copilot-instructions.md as the codebase evolves.

   **Rationale:**
   Long-term project memory ensures new Copilot sessions have full context.

   **Acceptance Criteria:**

   * AC-1: Agent detects changes in project structure
   * AC-2: Agent updates copilot-instructions.md
   * AC-3: Agent removes outdated information
   * AC-4: Agent documents new patterns and conventions


Integration Requirements
------------------------

.. req:: A-SPICE Process Alignment
   :id: REQ_SYSPILOT_007
   :status: implemented
   :priority: medium
   :tags: aspice, automotive

   **Description:**
   syspilot SHOULD align with A-SPICE process areas for automotive 
   software development.

   **Rationale:**
   A-SPICE alignment enables use in automotive projects with
   certification requirements.

   **Acceptance Criteria:**

   * AC-1: change agent maps to SWE.1 (Requirements Analysis)
   * AC-2: implement agent maps to SWE.2/SWE.3 (Design/Construction)
   * AC-3: verify agent maps to SWE.4 (Unit Verification)
   * AC-4: Documentation structure supports A-SPICE work products


.. req:: Portable Toolkit
   :id: REQ_SYSPILOT_008
   :status: implemented
   :priority: high
   :tags: portability, sync
   :links: US_SYSPILOT_008

   **Description:**
   syspilot SHALL be a standalone toolkit that can be used across
   multiple projects.

   **Rationale:**
   Enables syspilot to be maintained separately and reused across
   multiple projects.

   **Acceptance Criteria:**

   * AC-1: syspilot is self-contained and portable
   * AC-2: syspilot can be installed into any project

   **Note:** Installation, update, and version tracking covered by
   REQ_SYSPILOT_018 through REQ_SYSPILOT_023.


.. req:: Automatic Environment Setup
   :id: REQ_SYSPILOT_009
   :status: implemented
   :priority: high
   :tags: init, automation
   :links: US_SYSPILOT_007, REQ_SYSPILOT_001

   **Description:**
   syspilot SHALL automatically initialize the sphinx-needs environment
   when it is not available.

   **Rationale:**
   Agents running in cloud environments or fresh checkouts need to
   bootstrap their own dependencies without manual intervention.

   **Acceptance Criteria:**

   * AC-1: Detect if sphinx-needs is installed
   * AC-2: Install required dependencies automatically
   * AC-3: Create required directory structure
   * AC-4: Validate installation before proceeding


.. req:: MECE Requirements Review
   :id: REQ_SYSPILOT_010
   :status: implemented
   :priority: high
   :tags: agent, review, mece
   :links: US_SYSPILOT_005

   **Description:**
   syspilot SHALL provide a mece agent that analyzes ONE level (US, REQ, or SPEC)
   for MECE properties (Mutually Exclusive, Collectively Exhaustive).

   **Rationale:**
   Horizontal consistency within a level ensures no redundancies or contradictions.
   Focused scope prevents context overflow.

   **Acceptance Criteria:**

   * AC-1: Accept level parameter (US, REQ, SPEC)
   * AC-2: Detect redundant items (same thing said differently)
   * AC-3: Detect contradictions (conflicting items)
   * AC-4: Detect gaps (missing items for completeness)
   * AC-5: Detect overlaps (unclear boundaries)
   * AC-6: Detect missing horizontal links (item uses terms from another without :links:)
   * AC-7: Produce report with severity and recommendations


.. req:: Vertical Traceability Verification
   :id: REQ_SYSPILOT_011
   :status: implemented
   :priority: high
   :tags: agent, trace, vertical
   :links: US_SYSPILOT_009

   **Description:**
   syspilot SHALL provide a trace agent that verifies ONE user story or requirement
   is fully traced through all levels (US → REQ → SPEC → Code → Test).

   **Rationale:**
   Vertical traceability ensures complete implementation. Semantic validation
   catches links that exist but don't make sense.

   **Acceptance Criteria:**

   * AC-1: Accept starting item (US_xxx or REQ_xxx)
   * AC-2: Follow all :links: to find connected items
   * AC-3: Check link completeness (are there REQs? SPECs? Tests?)
   * AC-4: Check semantic validity (does REQ actually implement US intent?)
   * AC-5: Report coverage: FULL / PARTIAL / MISSING
   * AC-6: Identify gaps at each level


.. req:: Workflow Step Suggestions
   :id: REQ_SYSPILOT_012
   :status: implemented
   :priority: high
   :tags: agent, handoffs, workflow
   :links: US_SYSPILOT_002, US_SYSPILOT_003, US_SYSPILOT_004, US_SYSPILOT_005, US_SYSPILOT_009

   **Description:**
   syspilot SHALL suggest appropriate next workflow steps after agent completion.

   **Rationale:**
   Users need guidance on which agent to invoke next based on the current workflow state.
   This reduces cognitive load and ensures the correct workflow is followed.

   **Horizontal Links:**

   * REQ_SYSPILOT_003 (Change Analysis Agent - gets handoff capability)
   * REQ_SYSPILOT_004 (Implementation Agent - gets handoff capability)
   * REQ_SYSPILOT_005 (Verification Agent - gets handoff capability)
   * REQ_SYSPILOT_010 (MECE Review Agent - gets handoff capability)
   * REQ_SYSPILOT_011 (Trace Agent - gets handoff capability)

   **Acceptance Criteria:**

   * AC-1: After agent execution, VS Code displays handoff suggestions in UI
   * AC-2: Main workflow chain (change→implement→verify) has directional handoffs
   * AC-3: Analysis agents (mece/trace) have bidirectional handoffs
   * AC-4: Memory agent is suggested after verify or on-demand
   * AC-5: Each handoff includes a default prompt for the target agent


Iterative Change Processing Requirements
----------------------------------------

.. req:: Sphinx-Needs Link Discovery
   :id: REQ_SYSPILOT_013
   :status: implemented
   :priority: mandatory
   :tags: agent, change, links
   :links: US_SYSPILOT_011

   **Description:**
   The Change Agent SHALL use Sphinx-Needs links (via ``needs_id/*.json``) 
   to find impacted elements at each level.

   **Rationale:**
   Automatic link discovery prevents manual searching and ensures
   all impacted elements are found.

   **Acceptance Criteria:**

   * AC-1: Script reads from ``docs/_build/html/needs_id/*.json``
   * AC-2: Script returns outgoing and incoming links for any ID
   * AC-3: Script traces impact to configurable depth
   * AC-4: Script triggers sphinx-build if needs_id is missing


.. req:: Persistent Change Document
   :id: REQ_SYSPILOT_014
   :status: implemented
   :priority: mandatory
   :tags: agent, change, document
   :links: US_SYSPILOT_011

   **Description:**
   The Change Agent SHALL maintain a persistent Change Document in Markdown
   that records all analysis, decisions, and changes.

   **Rationale:**
   A persistent document provides context across sessions, enables
   review, and creates audit trail.

   **Acceptance Criteria:**

   * AC-1: Change Document created at start of change process
   * AC-2: Each level's work recorded in dedicated section
   * AC-3: Decisions and conflicts documented
   * AC-4: Navigation between levels logged
   * AC-5: Document deleted after merge (preserved in Git history)


.. req:: Horizontal MECE Check per Level
   :id: REQ_SYSPILOT_015
   :status: implemented
   :priority: high
   :tags: agent, change, mece
   :links: US_SYSPILOT_011, US_SYSPILOT_005

   **Description:**
   The Change Agent SHALL perform horizontal consistency check 
   within each level before proceeding to the next.

   **Rationale:**
   Catching conflicts early prevents cascading issues at lower levels.

   **Acceptance Criteria:**

   * AC-1: Check for contradictions with existing items at same level
   * AC-2: Check for redundancies
   * AC-3: Report conflicts before proceeding
   * AC-4: Document resolutions


.. req:: Bidirectional Level Navigation
   :id: REQ_SYSPILOT_016
   :status: implemented
   :priority: high
   :tags: agent, change, navigation
   :links: US_SYSPILOT_011

   **Description:**
   The Change Agent SHALL support navigation back to previous levels
   when issues are discovered.

   **Rationale:**
   Design feasibility issues may require requirement changes,
   which may require user story adjustments.

   **Acceptance Criteria:**

   * AC-1: User can request to go back to any previous level
   * AC-2: Previous level work preserved in Change Document
   * AC-3: New iteration marked in document
   * AC-4: Navigation logged with reason


.. req:: Final Consistency Check
   :id: REQ_SYSPILOT_017
   :status: implemented
   :priority: mandatory
   :tags: agent, change, verification
   :links: US_SYSPILOT_011

   **Description:**
   The Change Agent SHALL perform final consistency check across all levels
   after completing the Design level.

   **Rationale:**
   Bidirectional navigation can introduce inconsistencies that need
   final verification before implementation.

   **Acceptance Criteria:**

   * AC-1: Verify all links are valid (US→REQ→SPEC)
   * AC-2: Verify no orphaned elements
   * AC-3: Verify Change Document is internally consistent
   * AC-4: Produce sign-off checklist


Installation & Update Requirements
----------------------------------

.. req:: syspilot Distribution via GitHub Releases
   :id: REQ_SYSPILOT_018
   :status: implemented
   :priority: mandatory
   :tags: install, distribution
   :links: US_SYSPILOT_012, US_SYSPILOT_013, US_SYSPILOT_015

   **Description:**
   syspilot SHALL be distributed via GitHub Releases with semantic versioning.

   **Rationale:**
   GitHub Releases provides versioned distribution with automatic archive
   creation, enabling users to obtain specific versions and track what they
   have installed.

   **Acceptance Criteria:**

   * AC-1: User can identify release versions via GitHub Releases page
   * AC-2: User can download specific version archives (.zip, .tar.gz)
   * AC-3: Installation instructions are included with each release


.. req:: New Project Installation
   :id: REQ_SYSPILOT_019
   :status: implemented
   :priority: mandatory
   :tags: install, new-project
   :links: US_SYSPILOT_012

   **Description:**
   syspilot SHALL be installable into a new project.

   **Rationale:**
   New projects need a straightforward path to adopt syspilot
   from the beginning.

   **Acceptance Criteria:**

   * AC-1: User can invoke syspilot agents after installation
   * AC-2: User can build sphinx-needs documentation after installation
   * AC-3: User receives clear confirmation of successful installation


.. req:: Existing Project Adoption
   :id: REQ_SYSPILOT_020
   :status: implemented
   :priority: mandatory
   :tags: install, adoption
   :links: US_SYSPILOT_013

   **Description:**
   syspilot SHALL be adoptable into an existing project without data loss.

   **Rationale:**
   Projects already in progress need to adopt syspilot without
   disrupting their existing work.

   **Acceptance Criteria:**

   * AC-1: User's existing documentation is preserved
   * AC-2: User's existing code is preserved
   * AC-3: User is guided through any required decisions
   * AC-4: User can invoke syspilot agents after adoption


.. req:: Version Update and Migration
   :id: REQ_SYSPILOT_021
   :status: implemented
   :priority: mandatory
   :tags: update, migration
   :links: US_SYSPILOT_014

   **Description:**
   syspilot SHALL be updatable to newer versions.

   **Rationale:**
   Users need to benefit from new features, fixes, and improvements
   over time.

   **Acceptance Criteria:**

   * AC-1: User can determine currently installed version
   * AC-2: User can update to a newer version
   * AC-3: User's customizations are preserved after update
   * AC-4: User receives migration guidance for breaking changes


.. req:: Customization Preservation
   :id: REQ_SYSPILOT_022
   :status: implemented
   :priority: high
   :tags: install, update, preservation
   :links: US_SYSPILOT_013, US_SYSPILOT_014

   **Description:**
   syspilot SHALL preserve user customizations during adoption and updates.

   **Rationale:**
   Users invest effort in customizing their requirements and configuration.
   This must not be lost during updates.

   **Acceptance Criteria:**

   * AC-1: User-created requirements documents are preserved
   * AC-2: User-modified configuration is preserved
   * AC-3: User can identify what is syspilot core vs user content


.. req:: Sphinx-Needs Mandatory Dependency
   :id: REQ_SYSPILOT_023
   :status: implemented
   :priority: mandatory
   :tags: install, sphinx-needs, dependency
   :links: US_SYSPILOT_012, US_SYSPILOT_013

   **Description:**
   syspilot SHALL require sphinx-needs and its dependencies as mandatory components,
   and guide the user through installation if not available.

   **Rationale:**
   sphinx-needs provides the traceability infrastructure that syspilot
   relies on. The setup agent assists with dependency installation.

   **Acceptance Criteria:**

   * AC-1: User is informed about required dependencies (Python, sphinx, sphinx-needs, furo)
   * AC-2: User is informed about optional dependencies (graphviz for diagrams)
   * AC-3: Setup agent guides user through installation of missing dependencies
   * AC-4: User can build documentation using sphinx-needs after setup


Traceability
------------

All traceability is automatically generated by Sphinx-Needs.

.. needtable::
   :columns: id, title, status, tags
   :filter: id.startswith('REQ_SYSPILOT')

.. needflow:: REQ_SYSPILOT_001
