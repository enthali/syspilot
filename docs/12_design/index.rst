Design Documentation
====================

This section contains design specifications following Sphinx-Needs methodology.

.. toctree::
   :maxdepth: 2
   :caption: Design:

   spec_agent_framework
   spec_change
   spec_implement
   spec_verify
   spec_traceability
   spec_memory
   spec_setup
   spec_doc_structure
   spec_release


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
