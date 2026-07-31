User Stories
============

This section contains user stories that drive the requirements.

.. toctree::
   :maxdepth: 2
   :caption: User Stories:

   us_agent_arch
   us_skill_arch
   us_custom_agent_workflows
   us_ontology_arch

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
   us_skill_chg_launcher

   us_uat_skill_orchestration_vocab
   us_uat_installer_spec_rewrite
   us_uat_installer_session_first
   us_uat_installer_scoped_cleanup
   us_uat_generic_agent_workflow_pattern
   us_uat_pm_generic_workflow
   us_uat_product_owns_tool_lists
   us_uat_remove_tools_frontmatter
   us_uat_release_agent_tailoring_semver
   us_uat_branching_naming_fix
   us_uat_installer_frontmatter_sync
   us_uat_installer_orchestration_select
   us_uat_spec_root_cause_principle
   us_uat_ontology_arch
   us_uat_chg_launcher

   us_documentation


Overview
--------

User Stories describe **what users want to achieve** and **why**.

**Format:**

.. code-block:: none

   As a [role],
   I want to [action],
   so that [benefit].

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
