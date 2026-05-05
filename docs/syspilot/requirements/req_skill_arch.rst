Skill Architecture Requirements
================================

Meta-level requirements defining the Skill structure (Frontmatter,
Instructions, Rules) and the optional Group / DEFINITIONS extension.


.. req:: Skill Frontmatter Definition
   :id: SYSP_REQ_SKILL_ARCH_FRONTMATTER
   :status: draft
   :priority: mandatory
   :tags: agent-v2, skill, architecture, frontmatter
   :links: SYSP_US_SKILL_ARCH

   **Description:**
   Every syspilot Skill SHALL have a YAML **Frontmatter** block at the
   top of its ``SKILL.md`` carrying machine-readable metadata.

   **Rationale:**
   The Frontmatter is what tooling (Setup Agent, Mutual Exclusion check,
   discovery) reads to identify, install, and load a Skill. It also signals
   to a human reader which group a Skill belongs to and which tools it
   needs.

   **Required fields:**

   * ``name`` — dotted Skill identifier (e.g. ``syspilot.impact-python``)
   * ``description`` — one-sentence summary of what the Skill does

   **Optional fields:**

   * ``group`` — group identifier when the Skill is part of an exchangeable
     family; absent for standalone Skills
   * ``tools`` — list of tools the Skill needs (terminal commands, MCP, etc.)
   * ``triggers`` — patterns or keywords that hint when the Skill applies

   **Acceptance Criteria:**

   * AC-1: Every Skill has a Frontmatter block at the top of ``SKILL.md``
   * AC-2: ``name`` and ``description`` are mandatory fields
   * AC-3: ``group`` is optional; standalone Skills omit it
   * AC-4: Tooling can parse the Frontmatter without reading the body


.. req:: Skill Instructions Definition
   :id: SYSP_REQ_SKILL_ARCH_INSTRUCTIONS
   :status: draft
   :priority: mandatory
   :tags: agent-v2, skill, architecture, instructions
   :links: SYSP_US_SKILL_ARCH

   **Description:**
   Every syspilot Skill SHALL have an **Instructions** section that
   tells the LLM how to perform the capability.

   **Rationale:**
   Instructions are the LLM-facing body — the *how*. A calling Agent
   reads the Skill verbatim and follows its instructions. Without explicit
   instructions, the LLM has to guess, which defeats the purpose of having
   a Skill.

   The Instructions describe:

   * What the Skill is for (one-paragraph framing)
   * Which tools / commands to use
   * The expected outcome
   * The expected interaction shape (input → output)

   **Acceptance Criteria:**

   * AC-1: Every Skill has an Instructions section
   * AC-2: Instructions name the tools or commands to use
   * AC-3: Instructions describe the expected outcome
   * AC-4: Instructions are written for an LLM reader (imperative,
     unambiguous, free of speculative language)


.. req:: Skill Rules Definition
   :id: SYSP_REQ_SKILL_ARCH_RULES
   :status: draft
   :priority: mandatory
   :tags: agent-v2, skill, architecture, rules
   :links: SYSP_US_SKILL_ARCH

   **Description:**
   Every syspilot Skill SHALL have a **Rules** section listing hard
   constraints, edge cases, and explicit "don'ts" — or explicitly state
   that no special rules apply.

   **Rationale:**
   Skills frequently encode workarounds, safety constraints, and edge
   cases that are easy to miss. Putting them in a dedicated Rules section
   (rather than scattering them through the Instructions) makes them
   easy to find and easy to enforce.

   **Acceptance Criteria:**

   * AC-1: Every Skill has a Rules section
   * AC-2: Rules state constraints in imperative form ("MUST", "MUST NOT",
     "SHALL")
   * AC-3: A Skill with no special rules states this explicitly
   * AC-4: Rules are not duplicated in Instructions (each Rule appears
     exactly once)


.. req:: Skill Group Substitutability
   :id: SYSP_REQ_SKILL_ARCH_SUBSTITUTABILITY
   :status: draft
   :priority: mandatory
   :tags: agent-v2, skill, architecture, group
   :links: SYSP_US_SKILL_ARCH

   **Description:**
   Any Skill that implements all DEFINITIONS of its Group Contract Spec
   SHALL be substitutable for any other Skill of the same group. An Agent
   that links only to the Group Contract Spec SHALL continue to function
   unchanged after the swap.

   **Rationale:**
   The entire point of the group mechanism is that the *consuming Agent
   does not care which Skill is installed* — it only depends on the
   Contract. If a group-member Skill required Agents to be updated on
   replacement, the architecture's exchangeability guarantee would break.

   **Acceptance Criteria:**

   * AC-1: An Agent linked to a Group Contract Spec requires no
     modification when one group-member Skill is replaced by another
   * AC-2: A Skill is considered a valid group member when it implements
     every DEFINITION listed in the Group Contract Spec
   * AC-3: Two Skills of the same group are interchangeable from the
     perspective of every Agent that uses that group

