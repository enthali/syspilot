Admin
=====

.. story:: Admin
   :id: SYSP_US_ADMIN
   :status: approved
   :priority: mandatory
   :tags: actor, admin, tools
   :tracked_by: ROOT_SYSPILOT

   **As** a project team using syspilot,
   **I want** an Admin actor to own the project's tools, repository
   infrastructure, and assigned process documents,
   **so that** tool failures, repository conflicts, and infrastructure claims
   have one accountable owner instead of surfacing as unowned blockers inside
   other actors' work.

.. ac:: Tool and infrastructure trouble has an accountable owner
   :id: SYSP_AC_ADMIN_1
   :status: approved
   :validates: SYSP_US_ADMIN

   Given a tool failure, repository conflict, or claim about workflow, CI, or
   packaging infrastructure,
   When Admin completes the work assigned by the applicable process,
   Then the infrastructure state, the confirmation evidence, and any assigned
   process document are current and inspectable.
