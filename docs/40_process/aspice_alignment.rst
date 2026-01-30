A-SPICE Alignment
=================

This project's requirements engineering approach aligns with 
**Automotive SPICE (A-SPICE)** process areas.

.. note::

   A-SPICE is the de-facto standard for software process assessment 
   in the automotive industry. This alignment enables syspilot to be 
   used in A-SPICE certified development environments.


Process Mapping
---------------

.. list-table:: syspilot Types → A-SPICE Process Areas
   :header-rows: 1
   :widths: 15 15 35 35

   * - Type
     - Prefix
     - A-SPICE Process
     - Work Product
   * - User Story
     - ``US_``
     - SWE.1 (Input)
     - Stakeholder Requirements
   * - Requirement
     - ``REQ_``
     - SWE.1 Software Requirements Analysis
     - Software Requirements Specification
   * - Design Spec
     - ``SPEC_``
     - SWE.2/SWE.3 Architecture & Design
     - Software Architecture / Detailed Design
   * - Implementation
     - ``IMPL_``
     - SWE.3 (Output)
     - Code with traceability comments
   * - Test Case
     - ``TEST_``
     - SWE.4 Unit Verification
     - Test Specification / Test Report


Traceability Chain
------------------

A-SPICE requires **bidirectional traceability** between work products.
syspilot achieves this through sphinx-needs ``:links:`` attributes:

::

   US_xxx (Stakeholder Requirement)
      ↓ links
   REQ_xxx (Software Requirement)        ← SWE.1
      ↓ links
   SPEC_xxx (Design Specification)       ← SWE.2/SWE.3
      ↓ links
   IMPL_xxx (Implementation Reference)   ← SWE.3
      ↓ links
   TEST_xxx (Test Case)                  ← SWE.4


Agent Mapping
-------------

syspilot agents map to A-SPICE activities:

.. list-table:: syspilot Agents → A-SPICE Activities
   :header-rows: 1
   :widths: 20 30 50

   * - Agent
     - A-SPICE Activity
     - Description
   * - **change**
     - SWE.1 BP.1-3
     - Specify, structure, and analyze software requirements
   * - **implement**
     - SWE.2/SWE.3/SWE.4
     - Design, implement, verify
   * - **verify**
     - SWE.4 BP.4-5
     - Verify results, ensure bidirectional traceability
   * - **review**
     - SWE.1 BP.6
     - Ensure consistency (MECE analysis)
   * - **memory**
     - SUP.10
     - Change request management (project memory)


Coverage Analysis
-----------------

sphinx-needs provides automatic coverage analysis:

.. needtable::
   :columns: id, title, status, incoming
   :filter: type == 'req'

This shows which requirements have linked user stories (incoming links).


Benefits for A-SPICE Assessment
-------------------------------

Using syspilot with sphinx-needs provides:

1. **Traceable Requirements** - Every REQ links to US and SPEC
2. **Version Control** - Requirements in Git, full history
3. **Automated Reports** - needtable, needflow, coverage metrics
4. **Consistency Checks** - MECE review agent catches issues
5. **Work Product Evidence** - Generated HTML/PDF documentation

These artifacts support A-SPICE assessment evidence for:

- SWE.1: Software Requirements Analysis (Level 2+)
- SWE.2: Software Architectural Design (Level 2+)
- SWE.4: Software Unit Verification (Level 2+)
