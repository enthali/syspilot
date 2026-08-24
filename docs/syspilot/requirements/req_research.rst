Syspilot Research
=================

.. req:: Research Role
   :id: SYSP_REQ_RESEARCH
   :status: approved
   :implements: SYSP_US_RESEARCH
   :specializes: SYSP_REQ_ACTOR_MODEL
   :realized_by: docs/Syspilot Actors/Syspilot Research.md

   The Syspilot Research actor shall:

   - investigate material questions that do not yet fit specification-driven
     work, including model viability, tool behavior, ecosystem changes, and
     feasibility;
   - ground findings in inspectable evidence and distinguish verified facts
     from assumptions and remaining uncertainty;
   - retain relevant negative results and dead ends when they affect a later
     decision; and
   - return decision-ready findings without making the product decision owned
     by another actor.

.. vc:: Research returns evidence without taking decision ownership
   :id: SYSP_VC_RESEARCH_1
   :status: approved
   :verifies: SYSP_REQ_RESEARCH

   Inspect the Research role card and completed research evidence and confirm
   that the question, sources, verified findings, uncertainty, relevant dead
   ends, and receiving decision owner are explicit.