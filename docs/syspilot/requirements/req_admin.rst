Admin
=====

.. req:: Admin Role
   :id: SYSP_REQ_ADMIN
   :status: approved
   :implements: SYSP_US_ADMIN
   :specializes: SYSP_REQ_ACTOR_MODEL
   :realized_by: docs/Syspilot Actors/Admin.md

   The Admin actor shall:

   - own the tools and repository infrastructure assigned by the applicable
     process, including build, test, and documentation tooling, workflow and
     CI definitions, and repository conflicts;
   - troubleshoot tool and repository problems that arise outside the
     development flow and return the project to a working state;
   - own process documents when an applicable process assigns them;
   - confirm claims about workflow, CI, and packaging infrastructure against
     that infrastructure rather than inferring them from Needs-only impact
     results;
   - own release workflow definitions as tooling, meaning job and step wiring,
     runners, and dependencies, and treat Release as a mandatory consultee on
     every change to them; and
   - leave what the release gate checks and publishes, and whether a change
     to it is acceptable, with Release, and leave code and unit verification
     with the Developer.

.. vc:: Admin owns tool and infrastructure state with evidence
   :id: SYSP_VC_ADMIN_1
   :status: approved
   :verifies: SYSP_REQ_ADMIN

   Inspect the Admin role card and a completed infrastructure artifact in a
   Contract and confirm that the affected infrastructure, the action taken,
   and the confirming evidence are explicit, that a change to a release
   workflow definition records Release as consulted, and that release gate
   content and delivery remain with Release.
