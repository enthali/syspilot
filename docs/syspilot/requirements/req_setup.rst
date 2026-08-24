Syspilot Setup
==============

.. req:: Setup Role
   :id: SYSP_REQ_SETUP
   :status: approved
   :implements: SYSP_US_SETUP
   :specializes: SYSP_REQ_ACTOR_MODEL
   :realized_by: docs/Syspilot Actors/Syspilot Setup.md

   The Syspilot Setup actor shall:

   - own installation and update work assigned by the applicable process;
   - act as the customer's first contact for making syspilot operational;
   - account for the target environment while preserving the intended product
     capabilities; and
   - verify the resulting installation or expose an actionable environmental
     blocker.

.. vc:: Setup verifies the target installation
   :id: SYSP_VC_SETUP_1
   :status: approved
   :verifies: SYSP_REQ_SETUP

   Inspect the Setup role card and completed setup evidence and confirm that
   the target environment, installed or updated capabilities, verification
   result, and any remaining blocker are explicit.