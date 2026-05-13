Skill: Global DEFINITIONS Registry
====================================

Single source of truth for all Skill DEFINITIONS.


.. spec:: Global DEFINITIONS Registry
   :id: SYSP_SPEC_SKILL_DEFINITIONS
   :status: draft
   :tags: agent-v2, skill, architecture, definitions
   :links: SYSP_REQ_SKILL_DEFINITIONS

   **Purpose:**

   This page is the **single source of truth** for every DEFINITION used by
   any Skill in syspilot. Each DEFINITION is published exactly once as a
   ``.. def::`` need on this page. Group Contract Specs reference the
   DEFINITIONS of their group via the ``:defines:`` link — they do not
   duplicate the content.

   **Rules:**

   1. Every DEFINITION SHALL be a ``.. def::`` need on this page.
   2. Every DEFINITION ID SHALL follow the pattern ``SYSP_DEF_<NAME>``
      where ``<NAME>`` is the uppercase DEFINITION name used by Agents and
      Skills (e.g. ``SYSP_DEF_MERGE``).
   3. ID uniqueness is enforced by sphinx-needs — duplicate IDs are
      structurally rejected at build time. This is the collision check.
   4. Each Group Contract Spec SHALL link to its DEFINITIONS via
      ``:defines:`` (extra link type). Skills and Agents link only to the
      Group Contract — never directly to a ``def`` need.
   5. Adding, renaming, or removing a DEFINITION requires updating this
      page and the relevant Group Contract Spec in the same Change Request.
   6. Every Skill of a group SHALL implement every DEFINITION listed in the
      Group Contract Spec.
   7. Only one Skill per group SHALL be installed at a time. Setup Agent
      enforces by rejecting duplicate group installations.

   **Why a single page:**

   * No duplication: the description, name, and identity of a DEFINITION
     live in exactly one place.
   * Free collision check: sphinx-needs rejects duplicate IDs at build.
   * Free overview: the auto-generated table below lists every DEFINITION
     and the Group Contract Spec(s) that define it (incoming ``defines`` links).

   **Registry (auto-generated):**

   .. needtable::
      :types: def
      :columns: id;title;back_links
      :style: table

   *(Empty until the first Skill group registers DEFINITIONS in a follow-up
   Change Request, e.g. the Release Skill CR.)*

   **Skill Group Status:**

   .. list-table:: Skill group DEFINITIONS status
      :header-rows: 1
      :widths: 25 20 55

      * - Skill Group
        - Uses DEFINITIONS?
        - Notes
      * - ``orchestration``
        - no
        - Generic verbs map directly to tools (``runSubagent`` /
          ``jarvis_sendToSession``); no project-specific config required
      * - ``impact``
        - no
        - Fixed interface (Need ID + options → dependency tree)
      * - ``branching``
        - no (currently)
        - Branch names currently implicit; may register DEFINITIONS later
      * - ``ask-questions``
        - no
        - Generic UI capability; no project-specific config
      * - ``release``
        - planned
        - Will be the first group to register DEFINITIONS (separate CR)


DEFINITIONS
-----------

*(No DEFINITIONS registered yet. Future Skill Change Requests add them
here as ``.. def::`` directives. Example for the Release Skill CR:)*

..
   .. def:: How the agent merges a feature branch into the development branch
      :id: SYSP_DEF_MERGE
      :status: draft
      :tags: skill-definition

      The verb the agent uses to integrate a completed feature branch.
      One Skill may resolve this to a squash-merge, another to a regular
      merge — the operational detail lives in the Skill that implements
      the group.
