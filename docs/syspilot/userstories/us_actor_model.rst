Syspilot Actor Model
====================

.. story:: Syspilot Actor Model
   :id: SYSP_US_ACTOR_MODEL
   :status: approved
   :priority: mandatory
   :tags: architecture, actor, model
   :tracked_by: ROOT_SYSPILOT

   **As** a participant in a syspilot process,
   **I want** every Syspilot actor to expose its distinct role through one
   common actor model,
   **so that** I can understand the judgment each actor contributes and where
   its process authority comes from without relying on prescribed workflow
   prose.

   **Context:**

   Syspilot defines method-specific roles and process authority. Every actor
   inherits memory, messaging, escalation, and culture from the Jarvis Actor
   Kernel; syspilot does not duplicate that behavior.

.. ac:: Actor role and authority are inspectable
   :id: SYSP_AC_ACTOR_MODEL_1
   :status: approved
   :validates: SYSP_US_ACTOR_MODEL

   Given a participant inspects a Syspilot actor,
   When they follow the actor's context and public documentation,
   Then they can identify its role, its applicable process registry, and the
   boundary between syspilot method behavior and the Jarvis Actor Kernel.