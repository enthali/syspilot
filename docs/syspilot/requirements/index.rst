Requirements Documentation
==========================

This section contains system requirements following Sphinx-Needs methodology.

.. toctree::
   :maxdepth: 2
   :caption: Requirements:

   req_agent_arch
   req_skill_arch
   req_skill_definitions

   req_project_mgr
   req_change_mgr
   req_quality_mgr

   req_system_designer
   req_dev_engineer
   req_test_engineer
   req_docu_engineer
   req_quality_mece
   req_quality_trace
   req_release_engineer
   req_setup_engineer
   req_verify_engineer

   req_skill_ask_questions
   req_skill_orchestration
   req_skill_branching
   req_skill_impact

   req_documentation


Overview
--------

Requirements define **what** the system shall do.

**Format:** "The system SHALL [behavior]."

**A-SPICE Alignment:** SWE.1 Software Requirements Analysis

**Hierarchy:**

::

   User Story (SYSP_US_*)     ← See userstories/
        ↓ :links:
   Requirement (SYSP_REQ_*)   ← This section
        ↓ :links:
   Design Spec (SYSP_SPEC_*)  ← See design/


All Requirements
----------------

.. needtable::
   :columns: id, title, status, priority
   :filter: type == 'req'
