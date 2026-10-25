Process Maintenance Example
===========================

.. story:: Process Maintenance Example
   :id: SYSP_US_PROCESS_MAINTENANCE
   :status: approved
   :priority: mandatory
   :tags: contract, process, example, adoption
   :tracked_by: ROOT_SYSPILOT

   **As** a project that adopts syspilot and keeps its own process documents
   as Markdown Contracts and role cards,
   **I want** a worked Process Maintenance Contract in which an Admin changes
   those documents and Quality compares the affected Contracts against their
   peers,
   **so that** I can change my own process in a checkable way and know what a
   manual comparison can and cannot show.

.. ac:: Adopter can follow a process-document change from its Contract
   :id: SYSP_AC_PROCESS_MAINTENANCE_1
   :status: approved
   :validates: SYSP_US_PROCESS_MAINTENANCE

   Given a project changes its own process documents,
   When it follows the Process Maintenance example,
   Then one Contract shows the Admin's changed documents, the affected
   Contracts that Quality compared, the limits of that manual comparison, and
   the User's validation.
