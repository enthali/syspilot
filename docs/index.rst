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

**1. Download & extract** the `latest release <https://github.com/enthali/syspilot/releases>`_.

**2. Run the init script** from your project directory:

.. code-block:: powershell

   # Windows
   C:\path\to\syspilot\scripts\powershell\init.ps1

   # Linux / Mac
   /path/to/syspilot/scripts/bash/init.sh

**3. Open VS Code Copilot Chat** and type ``@syspilot.setup`` — the agent does the rest.

That's it. Dependencies, config, validation — all handled automatically.

Prerequisites: **VS Code + GitHub Copilot**, **Python 3.10+**


How It Works
------------

Three levels, connected by traceability links:

.. code-block:: text

   User Story (WHY)  ──links──▶  Requirements (WHAT)  ──links──▶  Design Specs (HOW)

When you request a change, syspilot follows these links to find only the affected
elements — then hands that focused context to the AI agent. No guessing, no scanning.


Your AI Team
------------

Seven agents, each with a clear job:

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Agent
     - What it does
   * - ``@syspilot.change``
     - Analyzes a change request, creates a Change Document listing all affected specs
   * - ``@syspilot.implement``
     - Executes approved changes with full traceability
   * - ``@syspilot.verify``
     - Checks implementation against the Change Document
   * - ``@syspilot.mece``
     - Finds gaps and redundancies in your specs (one level at a time)
   * - ``@syspilot.trace``
     - Traces one item through all levels — up and down
   * - ``@syspilot.release``
     - Manages versioning, release notes, and GitHub publishing
   * - ``@syspilot.setup``
     - Installs or updates syspilot in your project

The typical workflow: **change** → review → **implement** → **verify**. Done.


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
   The A-SPICE alignment is optional and documented under :doc:`40_process/index`.

**How is this different from just using Copilot?**
   Copilot is great at writing code. But it doesn't know *which* of your 500 requirements
   are affected by a change. syspilot solves that navigation problem — then Copilot
   does what it does best.


Specification Reference
-----------------------

.. toctree::
   :maxdepth: 2
   :caption: Specs & Traceability

   10_userstories/index
   11_requirements/index
   12_design/index
   31_traceability/index


Guides & Process
----------------

.. toctree::
   :maxdepth: 1
   :caption: Guides

   methodology
   namingconventions
   40_process/index
   releasenotes


Indices
-------

* :ref:`genindex`
* :ref:`search`
