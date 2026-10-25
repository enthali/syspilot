Release Contract
================

.. story:: Release Contract
   :id: SYSP_US_RELEASE_CONTRACT
   :status: approved
   :priority: mandatory
   :tags: release, contract, publication
   :tracked_by: ROOT_SYSPILOT

   **As** a user receiving a syspilot release and a project that adopts
   syspilot,
   **I want** every publication to run through a Release Contract that connects
   the included Changes, the version, the preflight evidence, the quality
   judgment, and the publication outcome,
   **so that** I can trust that what became public was verified before the
   irreversible step and can see how to run the same process in my project.

.. ac:: Stakeholder can assess a publication from its Contract
   :id: SYSP_AC_RELEASE_CONTRACT_1
   :status: approved
   :validates: SYSP_US_RELEASE_CONTRACT

   Given a release has been published,
   When a stakeholder inspects its Release Contract,
   Then the stakeholder can relate the included Changes, the version, the
   recorded preflight commands and results, Quality's judgment, and the
   publication evidence to the objective of the release.
