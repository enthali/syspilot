Project Manager
===============

.. req:: Project Manager Role
   :id: SYSP_REQ_PROJECT_MANAGER
   :status: approved
   :implements: SYSP_US_PROJECT_MANAGER
   :specializes: SYSP_REQ_ACTOR_MODEL
   :realized_by: docs/Syspilot Actors/Project Manager.md

   The Project Manager shall:

   - own strategy, intake, and portfolio management;
   - establish and prioritize outcome-oriented work with the user;
   - own the intent, user-decision, and closure artifacts assigned by the
     applicable process;
   - initialize Change Contracts with the Architect as first receiver;
   - present the verified outcome only after receiving Quality's ``proceed``
     judgment and evidence directly;
   - record applicable validation decisions received directly from the User,
     leaving validation responsibility with the User;
   - receive Contract responsibility again for closure; and
   - operate as an agentless Jarvis actor through the default Copilot session,
     without a dedicated syspilot agent or prompt file.

.. vc:: Project Manager governs intent and closure
   :id: SYSP_VC_PROJECT_MANAGER_1
   :status: approved
   :verifies: SYSP_REQ_PROJECT_MANAGER

   The role card and Change Process assign strategy, intent, initialization
   and closure to an agentless Project Manager, with first handoff to Architect.
   Technical artifacts remain with their owners.

.. vc:: Project Manager records decisions with direct provenance
   :id: SYSP_VC_PROJECT_MANAGER_2
   :status: approved
   :verifies: SYSP_REQ_PROJECT_MANAGER

   A completed Change records Quality's direct judgment before presentation
   and the User's direct validation decision before recording it; neither
   forwarded claims nor Project Manager validation substitute for them.