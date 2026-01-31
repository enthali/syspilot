syspilot Documentation
=======================

Welcome to the syspilot documentation.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   10_userstories/index
   11_requirements/index
   12_design/index
   31_traceability/index
   40_process/index
   releasenotes


Overview
--------

syspilot is a requirements engineering toolkit that uses **sphinx-needs traceability links**
to provide focused context to AI agents.

**Key Features:**

* Manage User Stories, Requirements, and Design Specs as code
* AI agents for change analysis, implementation, and verification
* Automatic traceability via sphinx-needs
* A-SPICE process alignment


Requirements & Design
---------------------

This project uses **sphinx-needs** for requirements engineering:

* **User Stories** (``US_*``) - Why (stakeholder perspective)
* **Requirements** (``REQ_*``) - What the system should do
* **Design Specifications** (``SPEC_*``) - How it should be implemented
* **Traceability** - Links from US to REQ to SPEC to code to tests


Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
