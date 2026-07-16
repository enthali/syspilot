Design Documentation
====================

This section contains design specifications following Sphinx-Needs methodology.

.. toctree::
   :maxdepth: 2
   :caption: Design:

   spec_agent_arch
   spec_skill_arch
   spec_skill_definitions
   spec_ontology_arch

   spec_project_mgr
   spec_change_mgr
   spec_quality_mgr

   spec_system_designer
   spec_dev_engineer
   spec_test_engineer
   spec_docu_engineer
   spec_quality_mece
   spec_quality_trace
   spec_release_engineer
   spec_setup_engineer
   spec_installer
   spec_verify_engineer

   spec_skill_ask_questions
   spec_skill_orchestration
   spec_skill_branching
   spec_skill_impact

   spec_uat_skill_orchestration_vocab
   spec_uat_installer_spec_rewrite
   spec_uat_installer_session_first
   spec_uat_installer_scoped_cleanup
   spec_uat_product_owns_tool_lists
   spec_uat_remove_tools_frontmatter
   spec_uat_release_agent_tailoring_semver
   spec_uat_branching_naming_fix
   spec_uat_installer_frontmatter_sync
   spec_uat_installer_orchestration_select
   spec_uat_spec_root_cause_principle
   spec_uat_ontology_arch

   spec_doc_scope


Overview
--------

Design specifications define **how** the system should be implemented. They are:

* **Linked** - Connected to requirements via ``:links:``
* **Technical** - Implementation decisions and architecture
* **Traceable** - From requirements through to code

**Organization:** Level 2 is organized by **solution domain** — one file per
technical component or agent. This is intentionally different from Levels 0–1
which organize by problem domain.


All Specifications
------------------

.. needtable::
   :columns: id, title, status, links
   :filter: type == 'spec'
