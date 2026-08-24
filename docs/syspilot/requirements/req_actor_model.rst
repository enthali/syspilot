Syspilot Actor Model
====================

.. req:: Actor Model
   :id: SYSP_REQ_ACTOR_MODEL
   :status: approved
   :implements: SYSP_US_ACTOR_MODEL
   :realized_by: docs/Syspilot Actors/index.md

   Every Syspilot actor shall:

   - have a public role card that defines its domain, responsibilities,
     character, and perspective;
   - maintain a ``context.md`` that links to its public role card and to the
     process registry it follows;
   - obtain artifact ownership and current responsibility from the applicable
     process and Contract Document rather than from a prescribed actor
     sequence; and
   - inherit memory, messaging, escalation, and culture from the Jarvis Actor
     Kernel without duplicating that behavior in syspilot.

.. vc:: Actor model exposes role and process authority
   :id: SYSP_VC_ACTOR_MODEL_1
   :status: approved
   :verifies: SYSP_REQ_ACTOR_MODEL

   Inspect each Syspilot actor's public role card and ``context.md`` and confirm
   that its role, process registry, process-derived authority, and Jarvis
   kernel boundary follow the common Actor Model.