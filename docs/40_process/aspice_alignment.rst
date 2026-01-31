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
syspilot achieves this through sphinx-needs ``:links:`` attributes.

**Current Implementation:**

::

   US_xxx (Stakeholder Requirement)           ← User perspective
      ↓ links
   REQ_xxx (Software Requirement)             ← SWE.1
      ↓ links
   SPEC_xxx (Design Specification)            ← SWE.2/SWE.3

**Planned: Implementation Traceability**

Future versions will add explicit IMPL_* needs:

::

   SPEC_xxx (Design Spec)
      ↓ links
      ↓
   IMPL_xxx (Implementation Reference)        ← SWE.3 (code location)
      ↑ points to actual code files/lines
      ↓ links
      ↓
   TEST_xxx (Test Case)                       ← SWE.4

Currently, implementation traceability is maintained through:

- **Code comments**: ``# Implements: SPEC_xxx, REQ_yyy``
- **Commit messages**: Reference specs in commit messages
- **grep/semantic search**: Find implementations by spec ID

**Status:** IMPL_* type defined in conf.py but not yet used in documentation.
Links from code to specs exist informally (comments), reverse direction
(specs to code) not yet tracked in sphinx-needs.

**Note:** Similarly, TEST_* types are defined but no actual test cases exist yet.
Test implementation is planned for future releases.

**Planned: Test Pyramid Alignment**

Future versions will differentiate test types matching the test pyramid:

::

   US_xxx (User Story)
      ↓ links
      ↓
   ACCEPT_xxx (Acceptance Test)               ← SWE.6 System Tests
      ↑ validates user story
      
   REQ_xxx (Requirement)
      ↓ links
      ↓
   INTEG_xxx (Integration Test)               ← SWE.5 Integration
      ↑ validates component interaction
      
   SPEC_xxx (Design Spec)
      ↓ links
      ↓
   UNIT_xxx (Unit Test)                       ← SWE.4 Unit Tests
      ↑ validates implementation detail

This hierarchical testing approach ensures:

- **Unit Tests** verify code matches design (SPEC → UNIT)
- **Integration Tests** verify components meet requirements (REQ → INTEG)
- **Acceptance Tests** verify system solves user needs (US → ACCEPT)

**Status:** Currently using generic ``TEST_*`` type. Refinement to
``UNIT_*``, ``INTEG_*``, ``ACCEPT_*`` types planned for future release.


Agent Mapping
-------------

syspilot agents map to A-SPICE activities:

.. list-table:: syspilot Agents → A-SPICE Activities
   :header-rows: 1
   :widths: 15 25 30 30

   * - Agent
     - A-SPICE Activity
     - Responsible For
     - Artifacts Created/Updated
   * - **setup**
     - SUP.1 QA / SUP.8 Config
     - Project setup, dependency installation
     - ``.syspilot/``, ``docs/conf.py``, agents
   * - **change**
     - SWE.1 BP.1-3
     - Requirements analysis, specification
     - ``US_*``, ``REQ_*``, ``SPEC_*``, Change Document
   * - **implement**
     - SWE.3/SWE.4 BP.1-3
     - Code implementation, test creation
     - ``IMPL_*``, code files, ``TEST_*``
   * - **verify**
     - SWE.4 BP.4-5
     - Verification, traceability validation
     - Status updates (draft→implemented→verified)
   * - **mece**
     - SWE.1 BP.6
     - Consistency check (one level)
     - MECE analysis report
   * - **trace**
     - All SWE processes
     - End-to-end traceability analysis
     - Traceability report (US→REQ→SPEC→IMPL→TEST)
   * - **memory**
     - SUP.10
     - Project memory, copilot instructions
     - ``.github/copilot-instructions.md``


Artifact Ownership by Agent
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Clear separation of responsibilities:

**Change Agent** (Requirements Engineering):

* Creates/updates ``US_*`` (User Stories) in ``docs/10_userstories/``
* Creates/updates ``REQ_*`` (Requirements) in ``docs/11_requirements/``
* Creates/updates ``SPEC_*`` (Design Specs) in ``docs/12_design/``
* Creates Change Documents in ``docs/changes/``
* Sets status: ``draft`` → ``approved``
* **Does NOT touch code** - only specifications

**Implement Agent** (Development):

* Creates ``IMPL_*`` references (traceability comments in code)
* Writes actual code according to ``SPEC_*``
* Creates ``TEST_*`` (Test Cases) that verify ``REQ_*``
* Updates user documentation (README, guides, agent files)
* Commits with traceability references
* **Does NOT modify specifications** - only implements them

**Verify Agent** (Quality Assurance):

* Validates implementation matches specifications
* Runs tests and checks results
* Updates status: ``approved`` → ``implemented`` → ``verified``
* Confirms bidirectional traceability (A-SPICE requirement)
* **Does NOT write code or specs** - only validates

**MECE Agent** (Consistency Review):

* Checks one specification level for MECE properties
* Reports contradictions, redundancies, gaps
* **Does NOT modify anything** - only analyzes and reports

**Trace Agent** (Traceability Analysis):

* Follows links through all levels (US→REQ→SPEC→IMPL→TEST)
* Generates impact analysis for changes
* Identifies orphaned or missing links
* **Does NOT modify anything** - only analyzes

This separation ensures **single responsibility** and supports
A-SPICE evidence for work product ownership.


A-SPICE Process Coverage
-------------------------

syspilot currently covers key A-SPICE process areas:

.. list-table:: A-SPICE Process Area Coverage
   :header-rows: 1
   :widths: 10 35 20 35

   * - Code
     - A-SPICE Process Area
     - Coverage
     - syspilot Agent(s)
   * - **SWE.1**
     - Software Requirements Analysis
     - ✅ Full
     - **change** (creates/updates REQ_*)
   * - **SWE.2**
     - Software Architectural Design
     - ✅ Full
     - **change** (creates/updates SPEC_*)
   * - **SWE.3**
     - Software Detailed Design & Unit Construction
     - ✅ Full
     - **implement** (code + IMPL_*)
   * - **SWE.4**
     - Software Unit Verification
     - ✅ Full
     - **implement** (TEST_*), **verify** (validation)
   * - **SWE.5**
     - Software Integration & Integration Test
     - ⏳ Partial
     - Manual (not yet agent-supported)
   * - **SWE.6**
     - Software Qualification Test
     - ⏳ Partial
     - Manual (not yet agent-supported)
   * - **SUP.1**
     - Quality Assurance
     - ✅ Full
     - **verify**, **mece** (consistency checks)
   * - **SUP.8**
     - Configuration Management
     - ✅ Full
     - **setup** (version control), Git workflow
   * - **SUP.9**
     - Problem Resolution Management
     - ⏳ Partial
     - Change Documents (via **change** agent)
   * - **SUP.10**
     - Change Request Management
     - ✅ Full
     - **change** (Change Docs), **memory** (project memory)
   * - **MAN.3**
     - Project Management
     - ❌ Not covered
     - Out of scope (manual process)
   * - **MAN.5**
     - Risk Management
     - ❌ Not covered
     - Out of scope (manual process)

**Legend:**

- ✅ **Full**: Agent-supported with traceability
- ⏳ **Partial**: Some support, mainly manual
- ❌ **Not covered**: Out of scope for syspilot

**Focus:** syspilot targets **SWE (Software Engineering)** and core 
**SUP (Supporting)** processes. Project management (MAN) and integration 
testing (SWE.5/6) are intentionally out of scope.


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
