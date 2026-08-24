Syspilot Architect
==================

.. story:: Syspilot Architect
   :id: SYSP_US_ARCHITECT
   :status: approved
   :priority: mandatory
   :tags: actor, architecture, specification
   :tracked_by: ROOT_SYSPILOT

   **As** a stakeholder in a syspilot change,
   **I want** an Architect to maintain coherent product architecture and
   specifications,
   **so that** individual changes fit the whole product rather than being only
   locally correct.

.. ac:: Change fits the product architecture
   :id: SYSP_AC_ARCHITECT_1
   :status: approved
   :validates: SYSP_US_ARCHITECT

   Given an approved change intent,
   When architecture and specification work is completed,
   Then the applicable stories, requirements, architecture decisions, and
   realization boundaries are coherent with the product as a whole.