Syspilot Release
================

.. story:: Syspilot Release
   :id: SYSP_US_RELEASE
   :status: approved
   :priority: mandatory
   :tags: actor, release, delivery
   :tracked_by: ROOT_SYSPILOT

   **As** a user receiving a syspilot release,
   **I want** a Release actor to package and ship a complete, verified product,
   **so that** the delivered version and its documentation are trustworthy and
   usable.

.. ac:: Complete release is delivered
   :id: SYSP_AC_RELEASE_1
   :status: approved
   :validates: SYSP_US_RELEASE

   Given a set of changes intended for release,
   When Release completes delivery,
   Then the packaged version, preflight evidence, release-facing documentation,
   and delivery outcome are complete and consistent.