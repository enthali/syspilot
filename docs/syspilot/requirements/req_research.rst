Research
========

.. req:: Research Role
   :id: SYSP_REQ_RESEARCH
   :status: approved
   :implements: SYSP_US_RESEARCH
   :specializes: SYSP_REQ_ACTOR_MODEL
   :realized_by: docs/Syspilot Actors/Research.md

   The Research actor shall:

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

   Research evidence identifies the question and sources, separates verified
   facts from uncertainty, and retains decision-relevant negative results.

.. vc:: Research findings leave the product decision with its owner
   :id: SYSP_VC_RESEARCH_2
   :status: approved
   :verifies: SYSP_REQ_RESEARCH

   The role card and completed findings identify the receiving decision owner
   without assigning that product decision to Research.