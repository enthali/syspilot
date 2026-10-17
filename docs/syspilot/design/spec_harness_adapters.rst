Harness Adapter Design
======================

Structural/frontmatter adapters that let the single-source agent and skill
content (Soul/Duties/Workflow content per SYSP_SPEC_AGENT_ARCH_SOUL,
Skill Instructions/Rules) run on the production-parity matrix (VS Code GitHub
Copilot, Claude Code, and OpenCode) plus Qoder as an explicitly disclosed
experimental, installable harness. Findings below are based on each
harness's current native conventions and are independent of environment-
specific launcher names.

.. important::

    Content (Soul/Duties/Workflow prose, Skill Instructions/Rules prose) is
    never forked per harness. The complete methodology body bytes after the
    YAML frontmatter delimiter, including terminal-newline state, are preserved
    unchanged except for deterministic identity and tool-binding references in
    Workflow or the orchestration Skill's formally designated native-binding
    section. Those structural binding adaptations preserve all other bytes and
    semantics; they are not content drift. Only those bindings, frontmatter,
    filename, and target directory may differ, per
    SYSP_REQ_HARNESS_CONTENT_SINGLE_SOURCE.


.. spec:: Harness Target Matrix
   :id: SYSP_SPEC_HARNESS_TARGET_MATRIX
   :status: approved
   :tags: agent-v2, harness, matrix
   :links: SYSP_REQ_HARNESS_CONTENT_SINGLE_SOURCE, SYSP_REQ_HARNESS_NATIVE_INSTALL

   **Researched native mechanisms (2026-09-16):**

   .. list-table::
      :header-rows: 1
      :widths: 14 20 20 20 26

      * - Harness
        - Agent (subagent) files
        - Skill files
        - Prompt / command files
        - Native distribution
      * - VS Code Copilot Chat
        - ``.github/agents/*.agent.md``
        - ``.github/skills/<name>/SKILL.md``
        - ``.github/prompts/*.prompt.md``
        - Installer copies files directly (existing mechanism, unchanged)
      * - Claude Code
        - ``.claude/agents/*.md`` (project) or ``~/.claude/agents/*.md`` (user)
        - ``.claude/skills/<name>/SKILL.md`` (project) or
          ``~/.claude/skills/<name>/SKILL.md`` (user)
        - Skills subsume commands; a Skill folder invoked as ``/<name>``
          *is* the prompt entry point — no separate prompt file format
        - File copy into the above directories (team-shared via ``git``);
          optionally packaged as a **Plugin** (``.claude-plugin/plugin.json``
          + ``agents/`` + ``skills/`` dirs) installed via
          ``/plugin marketplace add <org>/<repo>`` then
          ``/plugin install syspilot@<marketplace>``
      * - OpenCode
        - ``.opencode/agents/*.md`` (project) or
          ``~/.config/opencode/agents/*.md`` (global). OpenCode also reads
          ``.claude/agents/`` is **not** documented for agents (Claude-compat
          is documented for Skills only — see next column)
        - ``.opencode/skills/<name>/SKILL.md`` (project),
          ``~/.config/opencode/skills/<name>/SKILL.md`` (global) — OpenCode
          additionally reads ``.claude/skills/`` and ``.agents/skills/`` at
          both project and global scope for cross-tool interop
        - ``.opencode/commands/<name>.md`` (project) or
          ``~/.config/opencode/commands/<name>.md`` (global)
        - File copy only; no marketplace/package-manager mechanism was found
          for agents/skills/commands in OpenCode's own docs
      * - Qoder
        - Plugin/package agent content; installed Plugins supply specialized
          Agents
        - Plugin/package Skill content; Skills and Plugins are installed or
          imported as extensions
        - No separate prompt/command file format documented; Skills are
          invoked as ``/<skill-name>``, same pattern as Claude Code
        - The Installer builds the project-scoped import package defined by
          the Qoder Staging Contract below. Qoder documents Plugin/package
          import through its UI, but no programmable import/install command or
          API is documented. Native import acceptance is therefore an external
          prerequisite, not an Installer operation or autonomous lifecycle
          result. The package is not a directly live-loaded project directory;
          no user-global configuration is hand-edited.

   **Qoder Staging Contract:** A ``qoder`` installation owns exactly the
   final project artifact ``.syspilot/qoder/syspilot-qoder-plugin.zip``. It is
   a deterministic ZIP archive whose root contains Qoder's documented Plugin
   manifest ``plugin.json``, ``agents/``, and ``skills/``. ``plugin.json`` is
   generated from one version-controlled Installer manifest schema and records
   the package identifier ``syspilot-qoder``, the selected immutable source
   revision, and an inventory of every archive member with its SHA-256 digest.
   The archive contains every adapted Qoder agent at
   ``agents/<source-agent-filename>`` and every adapted Skill at
   ``skills/<source-skill-directory>/SKILL.md``; it contains no prompt or
   command artifact. Member paths are normalized relative paths, ordered
   lexically, timestamp-normalized, and ZIP metadata-normalized so identical
   inputs produce byte-identical archive bytes. The package digest is the
   SHA-256 of those final archive bytes and is reported in the structured
   Installer result.

   The frozen transaction plan includes the archive and its parent directory
   existence/type/content identity exactly as it includes other mutable paths.
   Update replaces only that final archive atomically; rollback restores its
   exact pre-state or removes it when it was absent. The Installer neither
   executes nor simulates a Qoder import, changes user/global Qoder state, nor
   claims that a Qoder native surface is available after staging. The user may
   select Qoder's documented UI import flow and choose this archive only after
   the Installer has reported a valid staged package. That UI acceptance is an
   external product capability prerequisite and makes a Qoder run ``staged``,
   not ``native-imported`` or production-parity cleared. This deterministic,
   checksummed staging is Qoder's complete and sufficient installability
   evidence for its experimental, installable tier in this change. Native
   in-app import and autonomous Manager-to-Engineer orchestration parity for
   Qoder are explicitly deferred to a future change; they are disclosed
   future scope, not silently dropped blockers.

.. spec:: Harness Agent Frontmatter Adapter
  :id: SYSP_SPEC_HARNESS_AGENT_ADAPTER
  :status: approved
  :tags: agent-v2, harness, adapter, agent, frontmatter
  :links: SYSP_REQ_HARNESS_CONTENT_SINGLE_SOURCE, SYSP_REQ_HARNESS_BEHAVIORAL_EQUIVALENCE, SYSP_SPEC_AGENT_ARCH_FRONTMATTER, SYSP_SPEC_HARNESS_TARGET_MATRIX

   **Field mapping** (source: syspilot's own ``.agent.md`` frontmatter,
   SYSP_SPEC_AGENT_ARCH_FRONTMATTER):

   .. list-table::
      :header-rows: 1
      :widths: 16 28 28 28

      * - syspilot field
        - Claude Code
        - OpenCode
        - Qoder
      * - ``description``
        - ``description`` (required)
        - ``description`` (required)
        - ``description`` (required)
      * - Source dotted agent ID
        - Required ``name`` identity. Replace every ``.`` in
          ``syspilot.<role>`` with ``-`` to produce
          ``syspilot-<role>``. The result contains only lowercase letters and
          hyphens. Filename mapping may remain independently target-specific;
          Claude identity comes only from frontmatter ``name``. A file without
          ``name`` is skipped as documentation, not loaded as an agent.
        - Retained as the native dotted agent identity.
        - Filename-derived identity; no separate field documented.
      * - Soul/Duties/Workflow body
        - Markdown body (system prompt) — unchanged
        - Markdown body (system prompt) — unchanged
        - Markdown body (system prompt) — unchanged
      * - ``user-invocable``
        - Emit ``user-invocable: false`` on every generated agent as a VS Code
          compatibility extension. VS Code also discovers
          ``.claude/agents/*.md`` and defaults an omitted field to ``true``;
          the explicit ``false`` prevents duplicate Claude-format identities
          from appearing in its direct agent picker. Claude Code does not
          define this field, so it is not a Claude-native visibility control:
          all generated agents remain discoverable and invocable through
          their native Claude ``name`` and retain Agent-tool orchestration.
        - No first-class hide flag; ``mode: subagent`` plus ``hidden: true``
          removes an agent from the ``@`` autocomplete menu only — the model
          can still invoke it via the Task tool regardless.
        - No equivalent field documented.
      * - ``agents`` (SEND allowlist)
        - For a Manager that runs as the main thread, emit an explicit
          ``Agent(syspilot-role-a, syspilot-role-b)`` entry in ``tools`` after
          mapping every source allowlist ID to its Claude native ``name``.
          Preserve other required tools through an approved native mapping or
          Claude inheritance. For a nested subagent that must spawn further
          subagents, Claude's documented nested Agent-tool semantics apply;
          ``tools: Agent`` permits unrestricted spawn and therefore does not
          falsely claim per-type enforcement.
        - ``permission.task`` glob patterns on the *calling* agent's own
          frontmatter or ``opencode.json`` can allow/deny/ask which subagent
          names it may invoke via the Task tool — closest native equivalent
          of ``agents:``.
        - No equivalent field documented; orchestration is "automatic or
          manual ``/agent-name``" with no declared allowlist.
      * - ``name`` / ``agent`` (Jarvis session identity)
        - Jarvis session identity remains inapplicable. This does not remove
          Claude's required native ``name`` derived from the source dotted
          agent ID (see SYSP_SPEC_HARNESS_ORCHESTRATION_ADAPTER).
        - Not applicable — omitted.
        - Not applicable — omitted.
      * - ``tools``
        - ``tools:`` list where required by the target role. Main-thread
          Manager SEND restrictions use ``Agent(<native-name>, ...)``;
          ``Agent`` without arguments permits unrestricted spawn under
          Claude's documented semantics. Setup needs only direct
          command-execution capability and no ``Agent`` tool.
        - ``permission.task`` / built-in Task tool, gated by the agent's
          ``mode``.
        - Not documented beyond a fixed built-in tool list (Bash, Edit,
          Write, Glob, Grep, Read, WebFetch, WebSearch); no confirmed
          subagent-spawning tool name.
      * - ``version``
        - No equivalent; omitted (only ``syspilot.setup`` uses it, and the
          Setup/Bootloader concept differs per harness — see
          SYSP_SPEC_HARNESS_ONE_TIME_ENABLEMENT).
        - Omitted.
        - Omitted.

  **Adapter rule:** the Installer derives each canonical source agent ID from
  ``syspilot.<role>.agent.md`` and emits the Claude native identity
  ``syspilot-<role>`` as required frontmatter ``name``. Across all 13 product
  agents, generated names SHALL be valid and unique. The Installer otherwise
  writes identical Markdown body bytes (Soul/Duties/Workflow, including the
  Tailoring preflight sentence and exact EOF-newline state) except for the
  structural binding adaptation defined below. Fields with no native
  equivalent are dropped, except that ``user-invocable: false`` is emitted as
  the explicit VS Code compatibility extension defined above; it is never
  represented as Claude-native hiding.

  **Structural binding adaptation:** for Claude output only, replace dotted
  agent IDs with their mapped native names solely where Workflow prose binds
  SEND/RECEIVE/RESPOND to a target identity or where the designated
  orchestration native-binding section binds an Agent tool target. The
  transformation is deterministic and boundary-aware; ordinary prose,
  examples unrelated to orchestration binding, headings, duties, ordering,
  and all remaining bytes stay unchanged. Every resulting allowlist and
  binding reference SHALL resolve to exactly one generated Claude ``name``.
  This target-native wiring is structural adaptation, not methodology-content
  drift.

  **Claude Code user invocation:** installed user-facing agents use their
  generated ``syspilot-<role>`` native identities. Dotted source IDs and
  source/display filenames are not Claude Code invocation identities. Claude
  Code remains able to discover and invoke every generated agent, including
  Engineer roles, because ``user-invocable`` has no claimed Claude-native
  effect. When VS Code opens the same project, ``.github/agents`` remains the
  sole direct-picker surface: only source agents declaring
  ``user-invocable: true`` are visible, and every generated identity under
  ``.claude/agents`` is hidden from direct selection.

    **Qoder package boundary:** Qoder-adapted agent files and Skill directories
    are archive members of ``.syspilot/qoder/syspilot-qoder-plugin.zip`` under
    the Qoder Staging Contract. They are not asserted to be live-loaded merely
    by staging. Only user acceptance of Qoder's documented UI import can make
    their supplied specialized Agents and Skills available; live availability
    remains owned by SYSP_SPEC_UAT_HARNESS_TARGET_MATRIX.

   **OpenCode exact mapping:** a source Manager emits ``mode: primary`` and an
   Engineer emits ``mode: subagent``. For a nonempty parsed source ``agents``
   allowlist, emit the parser-valid map shape below: the deny-all entry is
   always present and each source allowlist value becomes one explicit allow
   entry. With an empty or absent allowlist, omit ``permission.task`` entirely.
   Setup therefore emits as ``primary`` without Installer task permission;
   Installer emits as ``subagent`` and is not part of installation control
   flow.

   .. code-block:: yaml

      mode: primary
      permission:
        task:
          "*": deny
          "syspilot.<allowed-agent>": allow


.. spec:: Harness Skill Frontmatter Adapter
   :id: SYSP_SPEC_HARNESS_SKILL_ADAPTER
   :status: approved
   :tags: agent-v2, harness, adapter, skill, frontmatter
   :links: SYSP_REQ_HARNESS_CONTENT_SINGLE_SOURCE, SYSP_REQ_HARNESS_BEHAVIORAL_EQUIVALENCE, SYSP_SPEC_SKILL_ARCH_FRONTMATTER, SYSP_SPEC_HARNESS_TARGET_MATRIX

   **Field mapping** (source: syspilot's own ``SKILL.md`` frontmatter,
   SYSP_SPEC_SKILL_ARCH_FRONTMATTER):

   .. list-table::
      :header-rows: 1
      :widths: 16 28 28 28

      * - syspilot field
        - Claude Code
        - OpenCode
        - Qoder
      * - ``name``
        - Directory name is the invocation name; frontmatter ``name`` is
          display-only for personal/project skills (only matters for
          plugin-packaged skills). Kept for readability, not load-bearing.
        - ``name`` (recognized and retained).
        - Not documented as a distinct field; directory name is the
          invocation name (``/log-analyzer``-style), same pattern.
      * - ``description``
        - ``description`` (recommended; used for auto-invocation matching)
        - ``description`` (required)
        - Used for both automatic and manual (``/name``) triggering.
      * - ``group`` (Installer mutual-exclusion key)
        - Omitted from native frontmatter. The Installer reads the source value
          before adaptation to enforce SYSP_SPEC_INSTALLER_SKILL_MUTEX.
        - Omitted from native frontmatter; the source value still drives
          Installer mutual exclusion before adaptation.
        - Omitted from native frontmatter; the same source-metadata rule
          applies.
      * - ``tools`` (Skill's own suggested toolset)
        - Omitted; Claude Code's ``allowed-tools`` has different semantics.
        - Omitted because it is not a recognized OpenCode Skill field.
        - Omitted because no native equivalent is documented.
      * - ``triggers``
        - Omitted; Claude Code relies on the natural-language ``description``.
        - Omitted because OpenCode has no equivalent field.
        - Omitted; Qoder uses description-based matching.
      * - Instructions / Rules body
        - Markdown body — unchanged. ``## Instructions`` / ``## Rules``
          headings are plain Markdown headings with no special meaning to
          Claude Code, but remain useful structure for the model and for
          humans.
        - Markdown body — unchanged except for the orchestration Skill's
          designated native Task-binding section, same as above otherwise.
        - Markdown body — unchanged, same as above.

   **Adapter rule:** the Skill's Markdown body (Frontmatter-adjacent
   Instructions/Rules content) is written byte-for-byte identical across all
   four harnesses except for the orchestration Skill's designated native
   binding section. Only recognized frontmatter fields are emitted.
   syspilot-internal fields with no harness-native meaning (``group``,
   ``tools``, ``triggers``) are omitted from native frontmatter; the
   deterministic adapter retains their installation semantics where needed,
   including Skill-group mutual exclusion.

   Non-``SKILL.md`` resources are copied to
   ``.syspilot/skills/<source-directory>/`` and product templates to
   ``.syspilot/templates/``. Installed Skill instructions reference only those
   harness-neutral shared paths. In particular, change-launcher resolves
   ``.syspilot/templates/change-document.md`` and its shared script, and impact
   resolves ``.syspilot/skills/syspilot.impact-python/scripts/get_need_links.py``.


.. spec:: Harness Prompt/Command Adapter
  :status: implemented
  :id: SYSP_SPEC_HARNESS_PROMPT_ADAPTER
  :links: SYSP_REQ_HARNESS_CONTENT_SINGLE_SOURCE, SYSP_REQ_HARNESS_BEHAVIORAL_EQUIVALENCE, SYSP_SPEC_AGENT_ARCH_PROMPT, SYSP_SPEC_HARNESS_TARGET_MATRIX
  :tags: agent-v2, harness, adapter, prompt

   **Behavior:**

   * **VS Code** — unchanged: ``syspilot.<name>.prompt.md`` with
     ``agent: syspilot.<name>`` frontmatter, per SYSP_SPEC_AGENT_ARCH_PROMPT.
   * **Claude Code** — no separate prompt-file concept exists; a Manager
     agent's own Skill/subagent entry point already serves as the
     user-invocation surface (``@agent-name`` or, if the Manager is
     packaged as a Skill with ``context: fork``, ``/name``). The Installer
     SHALL NOT generate a Claude Code prompt file — there is nothing to
     adapt it to.
   * **OpenCode** — ``.opencode/commands/<name>.md`` (or global
     ``~/.config/opencode/commands/<name>.md``) mirrors each product prompt.
     Convert the source filename by removing only the exact terminal
     ``.prompt.md`` suffix and appending ``.md``; all dots in ``<name>`` are
     preserved (for example, ``syspilot.cm.prompt.md`` becomes
     ``syspilot.cm.md``). Emit ``description`` from prompt frontmatter, falling
     back to the corresponding source agent description when absent, and emit
     the prompt's ``agent`` value. The command body consists only of
     ``$ARGUMENTS`` followed by one terminal newline. OpenCode replaces that
     documented placeholder with the complete native command request, so the
     selected agent receives the caller's full argument text without copied
     prompt or agent prose.
   * **Qoder** — no separate command-file concept is documented. The imported
     Plugin/package supplies the Custom Agent entry point; users may select it
     through ``/`` and Qoder may select a matching installed Agent from the
     task description. The Installer does not create a direct project command
     or prompt path.

   **Consequence:** the Prompt File architecture element
   (SYSP_SPEC_AGENT_ARCH_PROMPT) is VS Code- and OpenCode-specific; Claude
   Code and Qoder fold this role into the agent file itself. This is a
   structural difference the adapter absorbs, not a content fork.


.. spec:: Harness Orchestration Fallback
  :id: SYSP_SPEC_HARNESS_ORCHESTRATION_ADAPTER
  :status: approved
  :tags: agent-v2, harness, orchestration, adapter
  :links: SYSP_REQ_SKILL_ORCHESTRATION_GROUP, SYSP_REQ_HARNESS_BEHAVIORAL_EQUIVALENCE, SYSP_REQ_HARNESS_CONTENT_SINGLE_SOURCE, SYSP_SPEC_INSTALLER_ORCHESTRATION_SELECT, SYSP_SPEC_HARNESS_TARGET_MATRIX

   **Finding:** none of Claude Code, OpenCode, or Qoder expose a Jarvis-
   equivalent persistent, cross-session, named-actor messaging registry.
   Claude Code has its own cross-session ``SendMessage``/agent-teams
   mechanism, but it is a different, incompatible protocol, not a Jarvis
   integration.

   **Semantic source and adapter ownership:** the product
   ``syspilot.orchestration-subagent`` Skill owns one canonical
   SEND/RECEIVE/RESPOND vocabulary: definitions, caller/callee inputs,
   synchronous ordering, result propagation, terminal RESPOND behavior, and
   rules. Its native-binding section is explicitly adapter-owned. The Installer
   selects that section solely from the explicit harness value, replaces it as
   a structured section rather than by free-form text substitution, and rejects
   a source with a missing, duplicate, or malformed binding boundary before
   checkpoint creation.

   Every installation deterministically selects this synchronous variant. No
   ``.jarvis/`` detection, asynchronous variant choice, or actor creation
   participates. The generated binding section maps the semantic operations to
   each harness's native primitive; byte identity is required outside that
   section, while semantic equivalence rather than byte identity is required
   inside it:

   .. list-table::
      :header-rows: 1
      :widths: 20 40 40

      * - Harness
        - SEND primitive
        - Notes
      * - Claude Code
        - Built-in ``Agent`` tool (subagent invocation)
        - A main-thread Manager maps its source allowlist to
          ``Agent(<native-name>, ...)``; a nested spawning subagent follows
          Claude's documented Agent-tool semantics, where bare ``Agent`` is
          unrestricted
      * - OpenCode
        - Built-in Task tool, gated by ``permission.task``
        - Manager agents set ``mode: primary`` and grant task permission to
          named Engineer subagents
      * - Qoder
        - Documented Custom Agent invocation by exact installed identity
          (``/<agent-name>``)
        - This is a user invocation surface, not a documented Manager-callable
          delegation primitive. It starts the selected agent's chat turn and
          exposes that agent's normal response to the user; it does not return
          an Engineer result to a Manager for autonomous consumption

   **Production binding contracts:**

   * **VS Code:** SEND invokes
     ``runSubagent("syspilot.<agent>", "<task>")`` and blocks for its return;
     RECEIVE is the task that started the current agent; RESPOND is normal
     terminal output captured by the caller.
   * **OpenCode:** SEND invokes native Task with the exact allowed
     ``syspilot.<agent>`` and task, gated by the caller's ``permission.task``;
     RECEIVE is the task that started the current agent; RESPOND is the normal
     Task result returned to the caller. The installed OpenCode Skill SHALL
     contain this Task mapping and SHALL NOT instruct the model to call
     ``runSubagent``.
   * **Claude Code:** SEND invokes the built-in Agent tool with the mapped
     ``syspilot-<agent>`` native identity and blocks for its result; RECEIVE is
     the task that started the current agent; RESPOND is normal output returned
     to the caller. Main-thread Manager restrictions use explicit
     ``Agent(<native-name>, ...)`` entries; nested subagents follow Claude's
     documented Agent-tool behavior.
   * **Qoder:** The documented Plugin/package supplies specialized Agents and
     Skills after installation or import as extensions. Users may select an
     installed Agent through ``/`` and Qoder may choose a matching installed
     Agent from task description; the main Agent coordinates the overall
     result. These documented selection and coordination statements do not
     establish a programmable Manager-callable SEND tool/API, blocking
     behavior, or structured Engineer-result return contract. The generated
     Qoder package therefore SHALL NOT claim an autonomous
     Manager-to-Engineer mapping. Qoder Manager-to-Engineer orchestration
     parity is out of scope for this change and is deferred to a future
     change, not a blocked production candidate: this change's accepted
     Qoder acceptance bar is deterministic package-staging installability,
     not orchestration clearance. A user relaying requests or responses
     between turns remains unacceptable as future orchestration evidence.
     Engineer-to-Engineer nesting is neither required nor claimed.

  For every harness claiming production orchestration clearance, successful
  Manager invocation or one successful SEND is insufficient. A representative
  fixture SHALL declare an ordered Engineer list and unique fixed result token
  per Engineer. Its captured native transcript must show each required SEND
  and returned token in order, and the terminal Manager RESPOND must contain
  every token in that same order without a user prompt or approval between
  stages. This orchestration clearance gate applies to VS Code GitHub
  Copilot, OpenCode, and Claude Code. Qoder is not evaluated against it for
  this change; its orchestration evidence is explicitly deferred future
  scope, disclosed rather than silently dropped.

   The adapter never derives binding choice from installed directories or
   rewrites the shared semantic definitions. VS Code and OpenCode generated
   Skills are allowed to differ only in frontmatter and this designated
   binding section.


.. spec:: Harness Disclosed Limitations
  :id: SYSP_SPEC_HARNESS_LIMITATIONS
  :status: approved
  :tags: agent-v2, harness, limitation, disclosure
  :links: SYSP_REQ_HARNESS_LIMITATION_DISCLOSURE, SYSP_SPEC_HARNESS_AGENT_ADAPTER, SYSP_SPEC_HARNESS_SKILL_ADAPTER, SYSP_SPEC_HARNESS_ORCHESTRATION_ADAPTER

   **Disclosed, accepted limitations** (each scoped to one harness; none
   blocks support on the other harnesses, per
   SYSP_REQ_HARNESS_LIMITATION_DISCLOSURE AC-2):

   * **Claude Code — nested allowlist enforcement boundary.** A Manager
     running as the main thread can restrict Agent targets with
     ``Agent(<native-name>, ...)``. For a nested subagent that itself spawns
     another subagent, documented bare ``Agent`` semantics permit unrestricted
     spawn; Workflow target bindings remain authoritative guidance but are not
     misrepresented as harness-enforced per-type restrictions.
   * **Claude Code / VS Code — cross-discovery compatibility boundary.** VS
     Code discovers both ``.github/agents/*.agent.md`` and Claude-format
     ``.claude/agents/*.md`` and treats a missing ``user-invocable`` as
     ``true``. Every generated Claude agent therefore carries
     ``user-invocable: false`` so VS Code exposes no duplicate Claude-format
     identity in its direct picker. Claude Code's supported-field list does
     not define this field; all generated agents remain native Claude agents
     and the field is not claimed to hide or disable them in Claude Code.
   * **OpenCode — Skill frontmatter is a strict six-field allowlist.**
     Source-only ``group``, ``tools``, and ``triggers`` fields are omitted
     from adapted native frontmatter. The Installer reads source ``group``
     metadata before adaptation to enforce mutual exclusion, so omission does
     not remove installation semantics.
   * **Qoder — autonomous delegation is deferred future scope.** The
     documented ``/<agent-name>`` Custom Agent surface is a user invocation,
     not evidence of a Manager-callable delegation or result-return channel.
     This change accepts Qoder at the experimental, installable tier on
     deterministic package-staging evidence alone; the autonomous
     Manager-workflow gate is explicitly out of scope here and deferred to a
     future change, not a blocker resolved by this revision. Engineer-to-
     Engineer nesting remains neither required nor claimed.
   * **Qoder — Rules require Settings-UI registration.** Qoder's Rules
     mechanism (project convention injection, distinct from Agents/Skills)
     documents rule *type* selection (Always Apply / Model Decision /
     Specific Files) via the IDE Settings UI, not purely by dropping a file
     with the right frontmatter. syspilot does not ship Rules as part of
     its installation scope, so this does not block SYSP_REQ_HARNESS_NATIVE_INSTALL;
     it is disclosed here as a related gap should a future CR extend
     syspilot to Rules-based distribution on Qoder.
