Product-Owns-Tool-Lists Expected Outcomes
==========================================

Expected outcomes specification for the ``product-owns-tool-lists`` UAT chains.
Per-scenario verification checklists for both the Installer tool-ownership
transfer and the Agent base-toolset uniformity acceptance criteria.

.. note::
   **Partially superseded by** ``remove-tools-frontmatter`` (2026-07-02).
   See ``docs/syspilot/userstories/us_uat_product_owns_tool_lists.rst`` for
   details. ``T-1-3`` below is superseded; ``SYSP_SPEC_UAT_AGENT_BASE_TOOLSET``
   is deprecated in its entirety.


.. spec:: UAT Expected Outcomes: Installer Tool Ownership Transfer
   :id: SYSP_SPEC_UAT_INSTALLER_TOOL_OWNERSHIP
   :status: draft
   :priority: mandatory
   :tags: uat, installer, tools, product-owns-tool-lists, expected-outcomes
   :links: SYSP_REQ_UAT_INSTALLER_TOOL_OWNERSHIP

   **Definition:**

   For each of the three test scenarios derived from the
   ``product-owns-tool-lists`` CR for ``SYSP_US_INSTALLER``, the following
   outcomes SHALL be observable when the Installer changes are correct.
   The tester executes each scenario in order and records pass/fail for every
   check item.

   ---

   **T-1-1 — No tools: preservation in Installer Duties spec**

   *CR AC:* AC1 |
   *REQ refs:* ``SYSP_REQ_INSTALLER_DUTIES``

   **Precondition:** Branch ``feature/product-owns-tool-lists`` is checked out.
   The file ``docs/syspilot/design/spec_installer.rst`` is readable.

   **Actions:**

   1. Open ``docs/syspilot/design/spec_installer.rst``.
   2. Locate the ``SYSP_SPEC_INSTALLER_DUTIES`` spec node.
   3. Read every AC and every duty paragraph inside the node.
   4. Search for the words "preserve", "preserve tools", "tools:", "re-inject",
      "retain" within the node body.
   5. Open ``docs/syspilot/requirements/req_setup_engineer.rst``.
   6. Locate ``SYSP_REQ_INSTALLER_DUTIES``.
   7. Repeat the same keyword search inside the REQ node body.

   **Expected Results:**

   * [ ] ``SYSP_SPEC_INSTALLER_DUTIES`` contains no AC or sentence stating that
     ``tools:`` is preserved, skipped, read-back, or re-injected during
     install or update.
   * [ ] ``SYSP_REQ_INSTALLER_DUTIES`` contains no AC or sentence stating
     that ``tools:`` is preserved, skipped, read-back, or re-injected.
   * [ ] The keyword search for "preserve", "re-inject", "retain" (applied to
     ``tools:``) returns zero matches in both nodes.

   **Pass criterion:** All three check items confirmed.

   **Fail criterion:** Any AC or sentence in either node describes preserving
   or selectively skipping ``tools:`` during install/update.

   ---

   **T-1-2 — Installer Workflow AC-5 mandates verbatim copy**

   *CR AC:* AC1 |
   *REQ refs:* ``SYSP_REQ_INSTALLER_WORKFLOW``

   **Precondition:** Branch ``feature/product-owns-tool-lists`` is checked out.

   **Actions:**

   1. Open ``docs/syspilot/design/spec_installer.rst``.
   2. Locate ``SYSP_SPEC_INSTALLER_WORKFLOW``.
   3. Find AC-5 (or equivalent step covering frontmatter handling during
      install/update).
   4. Open ``docs/syspilot/requirements/req_setup_engineer.rst``.
   5. Locate ``SYSP_REQ_INSTALLER_WORKFLOW``, find AC-5.

   **Expected Results:**

   * [ ] ``SYSP_SPEC_INSTALLER_WORKFLOW`` AC-5 (or the equivalent step) states
     that all frontmatter fields are taken from upstream and no field is
     preserved locally — no exception for ``tools:`` or any other field.
   * [ ] ``SYSP_REQ_INSTALLER_WORKFLOW`` AC-5 states the same: all frontmatter
     fields come from upstream; every file is written verbatim from upstream.
   * [ ] Neither AC mentions a Bootloader exception or ``tools:``-only
     exemption.

   **Pass criterion:** All three check items confirmed.

   **Fail criterion:** Any AC carves out a field (including ``tools:``) from
   the verbatim-copy rule.

   ---

   **T-1-3 — Live update overwrites manually modified tools:**

   .. note::
      **⚠ SUPERSEDED by** ``remove-tools-frontmatter``. See
      ``SYSP_US_UAT_INSTALLER_TOOL_OWNERSHIP`` AC-3 note. Replaced by
      ``TC-RT-UPDATE`` in ``SYSP_SPEC_UAT_REMOVE_TOOLS_FRONTMATTER``.

   *CR AC:* (runtime verification of AC1 behaviour) |
   *REQ refs:* ``SYSP_REQ_INSTALLER_WORKFLOW`` AC-5, ``SYSP_REQ_INSTALLER_DUTIES``

   **Precondition:** A separate target project exists with a complete syspilot
   installation under ``.github/``. The file
   ``.github/agents/syspilot.cm.agent.md`` has been manually modified: its
   ``tools:`` field was replaced with a sentinel value, e.g.
   ``tools: [my-sentinel-tool]``. The tester knows the upstream expected
   ``tools:`` content from ``SYSP_SPEC_AGENT_BASE_TOOLSET``.

   **Actions:**

   1. Open VS Code on the target project.
   2. Verify the sentinel value is present: open
      ``.github/agents/syspilot.cm.agent.md`` and confirm ``tools:``
      contains ``my-sentinel-tool``.
   3. Invoke ``@syspilot.setup`` (no branch override needed; default branch is
      sufficient).
   4. After the agent completes, open ``.github/agents/syspilot.cm.agent.md``
      again.
   5. Read the ``tools:`` field.

   **Expected Results:**

   * [ ] The agent completes without error.
   * [ ] The ``tools:`` field in ``syspilot.cm.agent.md`` no longer contains
     ``my-sentinel-tool``.
   * [ ] The ``tools:`` field matches the base toolset enumerated in
     ``SYSP_SPEC_AGENT_BASE_TOOLSET``.

   **Pass criterion:** All three check items confirmed.

   **Fail criterion:** The sentinel value survives the update (``tools:`` was
   preserved), or the agent errors out, or ``tools:`` contains an unexpected
   value that differs from the upstream base toolset.

   ---

   **T-1-4 — sphinx-build -W passes clean**

   *CR AC:* AC3 |
   *REQ ref:* (build gate, shared with T-2-5)

   **Precondition:** Branch ``feature/product-owns-tool-lists`` is checked out.
   Python venv under ``docs/.venv`` is activated.

   **Actions:**

   1. Open a terminal and navigate to ``docs/``.
   2. Run: ``uv run python docs-build.py clean``
   3. Observe the exit code and output.

   **Expected Results:**

   * [ ] The build exits with EXIT=0.
   * [ ] No ``WARNING:`` lines are emitted (``-W`` flag promotes warnings to
     errors).
   * [ ] No ``ERROR:`` lines are emitted.

   **Pass criterion:** All three check items confirmed.

   **Fail criterion:** Non-zero exit code, any WARNING, or any ERROR in output.


.. spec:: UAT Expected Outcomes: Agent Base Toolset Uniformity
   :id: SYSP_SPEC_UAT_AGENT_BASE_TOOLSET
   :status: deprecated
   :priority: mandatory
   :tags: uat, agent-arch, tools, product-owns-tool-lists, expected-outcomes
   :links: SYSP_REQ_UAT_AGENT_BASE_TOOLSET

   .. note::
      **⚠ DEPRECATED by** ``remove-tools-frontmatter``. See
      ``SYSP_US_UAT_AGENT_BASE_TOOLSET`` for rationale. Superseded by
      ``SYSP_SPEC_UAT_REMOVE_TOOLS_FRONTMATTER``.

   **Definition:**

   For each of the four test scenarios derived from the
   ``product-owns-tool-lists`` CR for ``SYSP_US_AGENT_ARCH``, the following
   outcomes SHALL be observable when the agent base-toolset changes are correct.
   The tester executes each scenario and records pass/fail for every check item.

   ---

   **T-2-1 — SYSP_SPEC_AGENT_BASE_TOOLSET exists with correct tool IDs**

   *CR AC:* AC2 |
   *REQ refs:* ``SYSP_REQ_AGENT_ARCH_FRONTMATTER`` AC-10

   **Precondition:** Branch ``feature/product-owns-tool-lists`` is checked out.

   **Actions:**

   1. Open ``docs/syspilot/design/spec_agent_arch.rst``.
   2. Locate the spec node with id ``SYSP_SPEC_AGENT_BASE_TOOLSET``.
   3. Read the tool list in the spec.
   4. Search the spec body for ``enthali.jarvis/``.
   5. Verify the Jarvis tools use the ``jarvis-core_`` prefix.

   **Expected Results:**

   * [ ] A spec node with ``:id: SYSP_SPEC_AGENT_BASE_TOOLSET`` exists in the
     file.
   * [ ] The spec lists the Jarvis session-messaging tools using the
     ``jarvis-core_`` prefix (e.g. ``jarvis-core_createSession``,
     ``jarvis-core_sendMessage``, ``jarvis-core_receiveMessage``).
   * [ ] The search for ``enthali.jarvis/`` returns zero matches in the spec
     node body.
   * [ ] The spec explicitly states that ``vscode/resolveMemoryFileUri`` is
     excluded from the base toolset.
   * [ ] The spec explicitly states that ``agent/runSubagent`` is not part of
     the base toolset.

   **Pass criterion:** All five check items confirmed.

   **Fail criterion:** Node absent, legacy ``enthali.jarvis/`` present,
   or exclusion rules for workspace memory / runSubagent absent.

   ---

   **T-2-2 — All 14 product agent files carry the base toolset**

   *CR AC:* AC2 |
   *REQ refs:* ``SYSP_REQ_AGENT_ARCH_FRONTMATTER`` AC-10

   **Test data:** The base toolset listed in ``SYSP_SPEC_AGENT_BASE_TOOLSET``
   (reference T-2-1 to confirm content first).

   **Precondition:** T-2-1 passed. Branch checked out.

   **Actions:**

   1. Run the following command from the workspace root to list all 14 agent
      files::

         Get-ChildItem syspilot/agents/*.agent.md | Select-Object Name

   2. For each of the 14 files, open the YAML frontmatter block (lines between
      the two ``---`` delimiters at the top of the file).
   3. Read the ``tools:`` list.
   4. Compare every tool ID in ``SYSP_SPEC_AGENT_BASE_TOOLSET`` against the
      ``tools:`` list in the file.
   5. Note any tool from the base toolset that is absent from the agent file,
      and any extra tool present beyond the base toolset.

   **Expected Results:**

   * [ ] Exactly 14 files are found matching the glob pattern.
   * [ ] Every tool ID in ``SYSP_SPEC_AGENT_BASE_TOOLSET`` is present in the
     ``tools:`` list of every agent file.
   * [ ] The only agent file whose ``tools:`` list contains a tool beyond the
     base toolset is ``syspilot.setup.agent.md`` (which additionally carries
     ``agent/runSubagent``).
   * [ ] No agent file contains ``enthali.jarvis/`` or any legacy Jarvis prefix.

   **Pass criterion:** All four check items confirmed.

   **Fail criterion:** Fewer or more than 14 files found; any base tool missing
   from any agent; any non-Setup agent has extra tools; any legacy prefix
   present.

   ---

   **T-2-3 — No agent has workspace-memory access**

   *CR AC:* AC2 |
   *REQ refs:* ``SYSP_REQ_AGENT_ARCH_FRONTMATTER`` AC-11

   **Precondition:** Branch checked out.

   **Actions:**

   1. From the workspace root, run a text search across all 14 agent files::

         Select-String -Path "syspilot/agents/*.agent.md" `
           -Pattern "vscode/resolveMemoryFileUri"

   2. Record all matches.

   **Expected Results:**

   * [ ] The search returns zero matches across all 14 agent files.

   **Pass criterion:** Zero matches.

   **Fail criterion:** One or more files contain ``vscode/resolveMemoryFileUri``
   in their ``tools:`` frontmatter field.

   ---

   **T-2-4 — Only Setup Bootloader has agent/runSubagent**

   *CR AC:* AC2 |
   *REQ refs:* ``SYSP_REQ_AGENT_ARCH_FRONTMATTER`` AC-12

   **Precondition:** Branch checked out.

   **Actions:**

   1. From the workspace root, run a text search across all 14 agent files::

         Select-String -Path "syspilot/agents/*.agent.md" `
           -Pattern "agent/runSubagent"

   2. Record the file names of all matches.

   **Expected Results:**

   * [ ] Exactly one match is found.
   * [ ] The matching file is ``syspilot/agents/syspilot.setup.agent.md``.
   * [ ] No other agent file contains ``agent/runSubagent``.

   **Pass criterion:** All three check items confirmed.

   **Fail criterion:** Zero matches (Setup missing it), more than one match,
   or the matching file is not ``syspilot.setup.agent.md``.

   ---

   **Untestable ACs**

   * ``SYSP_REQ_AGENT_ARCH_FRONTMATTER`` AC-3 (concrete tool IDs, not abstract
     categories) is structurally verified by T-2-2 (all IDs are the concrete
     VS Code tool identifiers from ``SYSP_SPEC_AGENT_BASE_TOOLSET``);
     no separate scenario is required.

   * The Jarvis prefix change (``enthali.jarvis/`` → ``jarvis-core_``) is
     verified by T-2-1 (spec) and T-2-2 (agent files); both grep for the
     legacy prefix explicitly.
