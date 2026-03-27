Requirements Documentation
==========================

This section contains system requirements following Sphinx-Needs methodology.

.. toctree::
   :maxdepth: 2
   :caption: Requirements:

   req_core
   req_workflows
   req_change_mgmt
   req_traceability
   req_installation
   req_release
   req_developer_experience
   req_documentation


Overview
--------

Requirements define **what** the system shall do.

**Format:** "The system SHALL [behavior]."

**A-SPICE Alignment:** SWE.1 Software Requirements Analysis

**Hierarchy:**

::

   User Story (SYSPILOT_US_*)     ← See userstories/
        ↓ :links:
   Requirement (SYSPILOT_REQ_*)   ← This section
        ↓ :links:
   Design Spec (SYSPILOT_SPEC_*)  ← See design/


All Requirements
----------------

.. needtable::
   :columns: id, title, status, priority
   :filter: type == 'req'
