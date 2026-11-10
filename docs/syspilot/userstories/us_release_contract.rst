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

.. ac:: A release completes on local evidence with its limits stated
   :id: SYSP_AC_RELEASE_CONTRACT_2
   :status: approved
   :validates: SYSP_US_RELEASE_CONTRACT

   Given a release whose workflow inputs are unchanged since the last
   successful tag-triggered run,
   When Release runs its preflight,
   Then the four local checks suffice without a separate remote run, the
   limits of local evidence and the accepted trade-off are stated and
   acknowledged in the User's authorization to push, and a changed input
   requires a recorded revalidation before the tag.

.. ac:: Release, notes, and documentation state one version
   :id: SYSP_AC_RELEASE_CONTRACT_3
   :status: approved
   :validates: SYSP_US_RELEASE_CONTRACT

   Given a release whose tag, newest release-notes heading, and published
   documentation version are compared,
   When the automated check runs,
   Then it passes only when the three agree, and a recorded preflight result
   does not force a new preflight while any change to other paths does.
