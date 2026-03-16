Documentation Scope Design
===========================

Design specifications for documentation scope — template scope for new projects.

**Document Version**: 0.2
**Last Updated**: 2026-03-16


.. spec:: Template Documentation Scope
   :id: SPEC_DOC_SCOPE_TEMPLATE
   :status: approved
   :links: REQ_DOC_SCOPE, REQ_DOC_README, REQ_DOC_INDEX, SPEC_INST_SETUP_AGENT
   :tags: documentation, scope, template

   **Design:**
   Default documentation scope used by the Setup Agent as starting
   point for new projects. Minimal set — projects extend based on their needs.

   **Default Documents:**

   +-----------------------+------------------------------------------+------------------+
   | Document              | Covers                                   | Requirement      |
   +=======================+==========================================+==================+
   | ``README.md``         | Project overview, installation, usage    | REQ_DOC_README   |
   +-----------------------+------------------------------------------+------------------+
   | ``docs/index.rst``    | Documentation entry point                | REQ_DOC_INDEX    |
   +-----------------------+------------------------------------------+------------------+

   **Extension Point:**

   Projects customize by adding additional documents and creating
   corresponding requirements and structure SPECs with explicit links.
   The Implement Agent uses Chapter Structure SPECs to determine
   what content goes where.


Traceability
------------

.. needtable::
   :columns: id, title, status, links
   :filter: id == 'SPEC_DOC_SCOPE_TEMPLATE'
