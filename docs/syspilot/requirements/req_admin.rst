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
     every change to them;
   - supply workflow/preflight comparison, last successful run evidence and
     stale-evidence paths and environment changes when a release relies on
     workflow runs from a different platform;
   - continue a pristine Setup record that the Setup Contract transfers to it
     because the initiating session lacks the Jarvis messaging tools, by
     re-reading its context, its role card, and the record, verifying that the
     header names it as executor, recording its acknowledgement in the record
     rather than by message, and then acting as the Setup executor under the
     Setup Contract; and
   - leave what the release gate checks and publishes, and whether a change
     to it is acceptable, with Release, and leave code and unit verification
     with the Developer.

.. vc:: Admin owns tool and infrastructure state with evidence
   :id: SYSP_VC_ADMIN_1
   :status: approved
   :verifies: SYSP_REQ_ADMIN

   Infrastructure evidence identifies affected tooling, actions and confirming
   observations from the infrastructure, not Needs-only inference.

.. vc:: Admin provides remote workflow evidence
   :id: SYSP_VC_ADMIN_2
   :status: approved
   :verifies: SYSP_REQ_ADMIN

   A release relying on remote runs has Admin's workflow/preflight comparison,
   successful-run evidence and stale-evidence conditions.

.. vc:: Admin acknowledges Setup in the transferred record
   :id: SYSP_VC_ADMIN_3
   :status: approved
   :verifies: SYSP_REQ_ADMIN

   The role card requires context, role and record refresh, executor-header
   verification and acknowledgement in the Setup record before continuing.

.. vc:: Admin preserves Release workflow-gate authority
   :id: SYSP_VC_ADMIN_4
   :status: approved
   :verifies: SYSP_REQ_ADMIN

   Every workflow change records Release's consultation; gate content remains
   Release's while Admin owns wiring.
