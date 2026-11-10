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
   - state, when a release process relies on that workflow's runs for a
     platform on which its preflight does not run, the facts of those runs
     that the reliance rests on, namely what the workflow's jobs execute
     compared with the preflight commands, the evidence of the last
     successful run, and the repository paths and environment changes that
     make that evidence stale, so that the process can name its revalidation
     triggers;
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

   Inspect the Admin role card and a completed infrastructure artifact in a
   Contract and confirm that the affected infrastructure, the action taken,
   and the confirming evidence are explicit, that a change to a release
   workflow definition records Release as consulted, and that release gate
   content and delivery remain with Release. Confirm that the role card names
   the continuation of a transferred Setup record, with the acknowledgement
   recorded in that record, and that a release process relying on the
   workflow's runs finds the facts, last successful run, and stale-evidence
   conditions in the Admin's infrastructure artifact.
