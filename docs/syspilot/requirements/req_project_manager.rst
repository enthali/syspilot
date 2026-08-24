Syspilot Project Manager
========================

.. req:: Project Manager Role
   :id: SYSP_REQ_PROJECT_MANAGER
   :status: approved
   :implements: SYSP_US_PROJECT_MANAGER
   :specializes: SYSP_REQ_ACTOR_MODEL
   :realized_by: docs/Syspilot Actors/Syspilot Project Manager.md

   The Syspilot Project Manager shall:

   - own strategy, intake, and portfolio management;
   - establish and prioritize outcome-oriented work with the user;
   - own the intent, user-decision, and closure artifacts assigned by the
     applicable process;
   - initialize Change Contracts, transfer first responsibility to the
     Architect, receive Quality's ``proceed`` judgment and evidence directly
     from Quality before presenting the verified outcome, receive and record
     an applicable validation decision directly from the User without taking
     validation responsibility, and receive responsibility again for closure;
     and
   - operate as an agentless Jarvis actor through the default Copilot session,
     without a dedicated syspilot agent or prompt file.

.. vc:: Project Manager governs intent and closure
   :id: SYSP_VC_PROJECT_MANAGER_1
   :status: approved
   :verifies: SYSP_REQ_PROJECT_MANAGER

   Inspect the Project Manager role card and Change Process and confirm that
   strategy, intent, first handoff, presentation and recording of user
   decisions, and closure are assigned to an agentless Project Manager; that
   Quality and User decisions have direct provenance rather than a forwarded
   claim; and that neither technical artifact work nor User validation
   responsibility is assigned to the Project Manager.