.. warning:: **V2 STATUS: TO BE UPDATED** - This document still describes the v1 product architecture.

Welcome to your system pilot documentation!
===========================================

**Your project has 5000 requirements. A change affects 5 of them. Find those 5.**

syspilot is a requirements engineering toolkit that gives AI agents *focused context* —
not your entire codebase, just the parts that matter. It uses
`sphinx-needs <https://sphinx-needs.readthedocs.io/>`_ traceability links to navigate
from a User Story down to exactly the affected Requirements and Design Specs.

The result? **O(affected), not O(total).** That's what makes it scale.


.. _getting-started:

Getting Started
---------------

.. note::

   The v2 bootstrap is being defined. The v1 setup-agent download has been
   removed. V2 will start from a README prompt pasted into a new Copilot
   session; that prompt creates the Syspilot Setup actor, which performs
   installation or update through a Setup Contract.

Prerequisites: **VS Code + GitHub Copilot + Jarvis**, **Python 3.10+**


How It Works
------------

Three levels, connected by traceability links:

.. code-block:: text

   User Story (WHY)  ──links──▶  Requirements (WHAT)  ──links──▶  Design Specs (HOW)

When you request a change, syspilot follows these links to find only the affected
elements — then hands that focused context to the AI agent. No guessing, no scanning.


Your AI Team
------------

Nine agents, each with a clear job:

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Agent
     - What it does
   * - ``@syspilot.design``
     - Analyzes a change request, creates a Change Document listing all affected specs
   * - ``@syspilot.implement``
     - Executes approved changes with full traceability
   * - ``@syspilot.verify``
     - Checks implementation against the Change Document
   * - ``@syspilot.memory``
     - Keeps project memory (copilot-instructions.md) current
   * - ``@syspilot.mece``
     - Finds gaps and redundancies in your specs (one level at a time)
   * - ``@syspilot.trace``
     - Traces one item through all levels — up and down
   * - ``@syspilot.release``
     - Manages versioning, release notes, and GitHub publishing
   * - ``@syspilot.setup``
     - Installs or updates syspilot in your project

The typical workflow: **change** → **implement** → **verify** → **memory**. Done.


FAQ
---

**Do I need to know reStructuredText?**
   Not really. The agents write the RST for you. But it helps to understand the basics —
   it's just text with some directives.

**Can I use this with an existing project?**
   Yes. ``@syspilot.setup`` can adopt an existing ``docs/`` folder. You can also start
   with an empty project and grow from there.

**What about Markdown?**
   syspilot uses `myst-parser <https://myst-parser.readthedocs.io/>`_ so you can mix
   Markdown and RST. The specs themselves use RST (because sphinx-needs requires it),
   but your prose documentation can be Markdown.

**Is this only for automotive / A-SPICE?**
   No. The spec hierarchy (User Stories → Requirements → Design) is universal.
   The A-SPICE alignment is optional.

**How is this different from just using Copilot?**
   Copilot is great at writing code. But it doesn't know *which* of your 500 requirements
   are affected by a change. syspilot solves that navigation problem — then Copilot
   does what it does best.


syspilot Actors & Processes (v2)
---------------------------------

.. toctree::
   :maxdepth: 2
   :caption: syspilot v2

   syspilot/index
   Syspilot Actors/index
   Syspilot Actors/Syspilot Project Manager
   Syspilot Actors/Syspilot Architect
   Syspilot Actors/Syspilot Developer
   Syspilot Actors/Syspilot Tester
   Syspilot Actors/Syspilot Quality
   Syspilot Actors/Syspilot Setup
   Syspilot Actors/Syspilot Release
   Syspilot Actors/Syspilot Research
   Syspilot Processes/index


Traceability
------------

.. toctree::
   :maxdepth: 2
   :caption: Traceability

   traceability/index


Guides & Process
----------------

.. toctree::
   :maxdepth: 1
   :caption: Guides

   methodology
   architecture
   workflows
   namingconventions
   releasenotes
   ontology-reference


Field Notes
-----------

.. toctree::
   :maxdepth: 1
   :caption: Field Notes

   experiences/index
   experiences/north-star-workflow-less-actors
   experiences/beyond-agent-memory
   experiences/auto-agent-messaging
   experiences/case-study-self-optimizing-agents
   experiences/customizing-agents-without-forking
   experiences/self-learning-agents
   experiences/lean-personas-rich-skills
   experiences/which-model-runs-syspilot


Indices
-------

* :ref:`genindex`
* :ref:`search`
