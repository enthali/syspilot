Syspilot Setup
==============

.. story:: Syspilot Setup
   :id: SYSP_US_SETUP
   :status: approved
   :priority: mandatory
   :tags: actor, setup, installation
   :tracked_by: ROOT_SYSPILOT

   **As** a user adopting or updating syspilot,
   **I want** a Setup actor to make the product work in my environment,
   **so that** installation details and environmental differences do not
   prevent me from using the intended syspilot capabilities.

.. ac:: Syspilot works in the target environment
   :id: SYSP_AC_SETUP_1
   :status: approved
   :validates: SYSP_US_SETUP

   Given a supported customer environment and a syspilot version to install or
   update,
   When Setup completes its work,
   Then the intended product capabilities are present and verified in that
   environment or an actionable blocker is explicit.