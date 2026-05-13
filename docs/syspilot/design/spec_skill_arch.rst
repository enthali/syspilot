Skill Architecture Design
==========================

Concrete file structure of a Skill's ``SKILL.md`` and how the architecture
elements (Frontmatter, Instructions, Rules) are laid out.


.. spec:: Skill Frontmatter Structure
   :id: SYSP_SPEC_SKILL_ARCH_FRONTMATTER
   :status: draft
   :tags: agent-v2, skill, architecture, frontmatter
   :links: SYSP_REQ_SKILL_ARCH_FRONTMATTER

   **File:** Top of every ``SKILL.md`` (between ``---`` fences).

   **Format:** YAML.

   **Schema:**

   .. code-block:: yaml

      ---
      name: syspilot.<dotted-identifier>     # mandatory
      description: <one-sentence summary>    # mandatory
      group: <group-name>                    # optional
      tools: [tool1, tool2, ...]             # optional
      triggers: [keyword1, pattern1, ...]    # optional
      ---

   **Examples:**

   *Standalone Skill (no group):*

   .. code-block:: yaml

      ---
      name: syspilot.impact-python
      description: Impact analysis using sphinx-needs traceability links.
      tools: [terminal]
      triggers: [impact, blast radius, dependencies]
      ---

   *Group-member Skill:*

   .. code-block:: yaml

      ---
      name: syspilot.orchestration-subagent
      description: Manager-to-engineer orchestration via subagent invocation.
      group: orchestration
      ---

   **Notes:**

   * ``name`` follows the ``syspilot.<group-or-purpose>[-<variant>]``
     pattern (e.g. ``syspilot.impact-python``,
     ``syspilot.orchestration-jarvis``).
   * ``group`` MUST be lowercase, dashed where needed
     (``release``, ``ask-questions``).
   * The Setup Agent uses ``group`` (when present) to enforce Mutual
     Exclusion at install time.


.. spec:: Skill Instructions Section
   :id: SYSP_SPEC_SKILL_ARCH_INSTRUCTIONS
   :status: draft
   :tags: agent-v2, skill, architecture, instructions
   :links: SYSP_REQ_SKILL_ARCH_INSTRUCTIONS

   **File:** Body section of every ``SKILL.md``, below the Frontmatter.

   **Heading:** ``## Instructions`` (required heading; LLM looks for it).

   **Required content:**

   1. **Purpose** — one paragraph: what the Skill does and when to invoke it
   2. **Tools** — explicit list of tools or commands the Skill uses
   3. **Procedure** — numbered or imperative steps the LLM follows
   4. **Outcome** — what the calling Agent gets back

   **Style:**

   * Imperative voice ("Run …", "Read …", "Return …")
   * No speculative language ("might", "could", "may want to")
   * No prose narration of the architecture — state what to do

   **Example skeleton:**

   .. code-block:: markdown

      ## Instructions

      **Purpose:** Resolve the inbound and outbound traceability links of
      a sphinx-needs ID.

      **Tools:** Python interpreter, ``get_need_links.py`` script.

      **Procedure:**

      1. Validate that the ``<id>`` argument matches ``SYSP_*``
      2. Run ``python .github/skills/syspilot.impact-python/scripts/get_need_links.py <id>``
      3. Parse the JSON result

      **Outcome:** A JSON object with ``id``, ``linked_to`` and
      ``linked_from`` arrays.


.. spec:: Skill Rules Section
   :id: SYSP_SPEC_SKILL_ARCH_RULES
   :status: draft
   :tags: agent-v2, skill, architecture, rules
   :links: SYSP_REQ_SKILL_ARCH_RULES

   **File:** Body section of every ``SKILL.md``, after Instructions.

   **Heading:** ``## Rules`` (required heading; LLM looks for it).

   **Content:**

   * Bulleted hard constraints, written as ``MUST`` / ``MUST NOT`` / ``SHALL``
     statements
   * Edge cases the LLM is likely to miss
   * Explicit "don'ts" that prevent common mistakes
   * Constraints that appear here MUST NOT be restated in the Instructions
     section — each constraint lives in exactly one place

   **No-rules case:** A Skill with no special rules SHALL still contain
   the section, with the single line ``No special rules.``. This makes
   "no rules" an explicit, reviewable statement rather than an oversight.

   **Example:**

   .. code-block:: markdown

      ## Rules

      * MUST run the script from the repository root.
      * MUST NOT call this Skill with non-``SYSP_*`` IDs — it has no
        meaning outside that namespace.
      * If the script exits non-zero, MUST surface stderr verbatim;
        MUST NOT swallow the error.


.. spec:: Skill Group Substitutability
   :id: SYSP_SPEC_SKILL_ARCH_SUBSTITUTABILITY
   :status: draft
   :tags: agent-v2, skill, architecture, group
   :links: SYSP_REQ_SKILL_ARCH_SUBSTITUTABILITY

   **Mechanism:**

   A Skill is substitutable within its group when it satisfies the Group
   Contract Spec. The Group Contract Spec is the interface that Agents
   and Skills share:

   * **Agent** — links to the Group Contract Spec (``:links:``). The Agent
     never references a concrete Skill. It only reads DEFINITIONS by name.
   * **Group Contract Spec** — declares all DEFINITIONS of the group via
     ``:defines:``. This is the interface boundary.
   * **Skill** — links to the Group Contract Spec (``:links:``) and
     implements every DEFINITION listed there. Different Skills may
     implement the same DEFINITION differently (e.g. ``MERGE`` as
     squash-merge vs. regular merge).

   **Substitution invariant:**

   When Skill A is uninstalled and Skill B of the same group is installed:

   1. The Group Contract Spec is unchanged — same DEFINITIONS, same IDs.
   2. The Agent spec is unchanged — its ``:links:`` still points to the
      Group Contract Spec.
   3. The LLM reads the newly installed Skill B's implementation of each
      DEFINITION instead of Skill A's — different behaviour, same interface.

   **Enforcement:**

   * The Setup Agent checks the ``group:`` field at install time.
   * If a Skill of the same group is already installed, the Setup Agent
     blocks or replaces it (Mutual Exclusion).
   * A Skill that omits a mandatory DEFINITION is not a valid member of
     the group and MUST NOT be installed as one.

