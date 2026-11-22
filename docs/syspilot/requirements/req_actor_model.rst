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
   - name its role card and process registry in ``context.md`` as
     project-root-relative paths in code spans that resolve to existing files;
   - obtain artifact ownership and current responsibility from the applicable
     process and Contract Document rather than from a prescribed actor
     sequence;
   - use project-neutral role cards and instructions that name no specific
     project;
   - state required behavior in positive wording in its role card and
     instructions, rather than relying on a negation to imply the bounded
     alternative; and
   - inherit memory, messaging, escalation, and culture from the Jarvis Actor
     Kernel without duplicating that behavior in syspilot.

.. vc:: Actor model exposes role and process authority
   :id: SYSP_VC_ACTOR_MODEL_1
   :status: approved
   :verifies: SYSP_REQ_ACTOR_MODEL

   Each public role card identifies domain, responsibilities, character and
   perspective. Its instructions are project-neutral and express required
   behavior positively.

.. vc:: Actor context resolves its authority sources
   :id: SYSP_VC_ACTOR_MODEL_2
   :status: approved
   :verifies: SYSP_REQ_ACTOR_MODEL

   Every actor's ``context.md`` contains code-span, project-root-relative paths
   to an existing role card and process registry.

.. vc:: Actor authority preserves the kernel boundary
   :id: SYSP_VC_ACTOR_MODEL_3
   :status: approved
   :verifies: SYSP_REQ_ACTOR_MODEL

   Role cards derive artifact authority from Contracts, not an actor sequence,
   and leave memory, messaging, escalation and culture to the Jarvis Kernel.