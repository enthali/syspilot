User Stories
============

This section contains user stories that drive the requirements.

.. toctree::
   :maxdepth: 2
   :caption: User Stories:

   us_agent_arch
   us_skill_arch

   us_project_mgr
   us_change_mgr
   us_quality_mgr

   us_system_designer
   us_dev_engineer
   us_test_engineer
   us_docu_engineer
   us_quality_mece
   us_quality_trace
   us_release_engineer
   us_setup_engineer
   us_verify_engineer

   us_skill_ask_questions
   us_skill_orchestration
   us_skill_branching
   us_skill_impact

   us_documentation


Overview
--------

User Stories describe **what users want to achieve** and **why**.

**Format:**

   **As a** [role],
   **I want to** [action],
   **so that** [benefit].

**A-SPICE Alignment:**

User Stories serve as input to SWE.1 (Software Requirements Analysis).
They capture stakeholder needs before deriving system requirements.

**Hierarchy:**

::

   User Story (US_*)     ← Stakeholder perspective (WHY)
        ↓ :links:
   Requirement (REQ_*)   ← System behavior (WHAT)


All User Stories
----------------

.. needtable::
   :columns: id, title, status, priority
   :filter: type == 'story'
