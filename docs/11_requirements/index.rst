Requirements Documentation
==========================

This section contains system requirements following Sphinx-Needs methodology.

.. toctree::
   :maxdepth: 2
   :caption: Requirements:

   req_core
   req_change_mgmt
   req_traceability
   req_installation
   req_release
   req_developer_experience


Overview
--------

Requirements define **what** the system shall do.

**Format:** "The system SHALL [behavior]."

**A-SPICE Alignment:** SWE.1 Software Requirements Analysis

**Hierarchy:**

::

   User Story (US_*)     ← See 10_userstories/
        ↓ :links:
   Requirement (REQ_*)   ← This section
        ↓ :links:
   Design Spec (SPEC_*)  ← See 12_design/


All Requirements
----------------

.. needtable::
   :columns: id, title, status, priority
   :filter: type == 'req'
