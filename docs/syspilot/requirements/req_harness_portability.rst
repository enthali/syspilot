Harness Portability Requirements
=================================

Requirements ensuring syspilot's agent/skill/command behavior is equivalent
across the production-parity matrix: VS Code GitHub Copilot, Claude Code, and
OpenCode. Qoder is an explicitly disclosed experimental, installable harness;
its acceptance bar is deterministic package staging, not full behavioral
equivalence.


.. req:: Harness Behavioral Equivalence
   :id: SYSP_REQ_HARNESS_BEHAVIORAL_EQUIVALENCE
   :status: approved
   :priority: mandatory
   :tags: agent-v2, harness, portability
   :links: SYSP_US_HARNESS_PORTABILITY

   **Description:**
   On every production-supported harness, a syspilot Manager agent SHALL exhibit the
   same Soul/Duties/Workflow-driven behavior, and a syspilot Skill SHALL
   have its Instructions and Rules applied identically, as on VS Code
   Copilot Chat. Equivalent user-facing commands SHALL invoke the same
   Manager behavior where the harness provides a separate command surface.

   **Rationale:**
   The methodology's value is the Soul/Duties/Workflow and
   Frontmatter/Instructions/Rules content itself, not the harness it runs
   in. Behavioral equivalence is what makes a user's harness choice
   irrelevant to the outcome they get.

   **Acceptance Criteria:**

   * AC-1: Given a production-supported harness, When a Manager agent is invoked,
     Then its Soul/Duties/Workflow-driven behavior is the same as on any
     other supported harness
   * AC-2: Given a production-supported harness, When a Skill is consulted, Then its
     Instructions and Rules are applied identically to how they are
     applied on VS Code Copilot Chat
   * AC-3: A harness is production-supported only after clean install, repeat
     update, native invocation, and rollback acceptance are complete
   * AC-4: Given equivalent VS Code and OpenCode commands, When each command
     is invoked with the same request, Then each routes to the corresponding
     Manager and exposes equivalent command behavior
   * AC-5: Given a Manager executes SEND, RECEIVE, or RESPOND on a
     production-supported harness, When the semantic operation reaches its
     harness binding, Then VS Code uses ``runSubagent`` and OpenCode uses its
     native Task mechanism while preserving the same observable contract

   * AC-6: Given Claude Code, When the native harness is exercised, Then it
     independently demonstrates native roles/agents, Skills, commands/prompts,
     and equivalent Manager behavior. Given Qoder, When the native harness is
     exercised, Then only its deterministic package-staging artifact is
     evaluated; native role/Skill behavioral equivalence for Qoder is
     deferred future scope and is not required for this criterion.

.. req:: Harness Content Single-Source
   :id: SYSP_REQ_HARNESS_CONTENT_SINGLE_SOURCE
   :status: approved
   :priority: mandatory
   :tags: agent-v2, harness, portability, single-source
   :links: SYSP_US_HARNESS_PORTABILITY; SYSP_REQ_AGENT_ARCH_FRONTMATTER, SYSP_REQ_SKILL_ARCH_FRONTMATTER

   **Description:**
    Agent, Skill, and Command methodology content SHALL be authored once in
    the product ``syspilot/`` tree on the selected upstream branch. Source
    enumeration and transformation SHALL use that product tree as the sole
    source, never an installed ``.github/`` or other harness instance.
    Installing that content onto any supported harness SHALL NOT require
    maintaining a harness-specific fork of the content — only a deterministic
    structural/frontmatter adapter differs per harness. A designated
    orchestration tool-binding section MAY differ deterministically where
    harness APIs differ, but the SEND/RECEIVE/RESPOND definitions, inputs,
    outputs, ordering, and rules remain one shared semantic source.

   **Acceptance Criteria:**

   * AC-1: Given methodology content in the product ``syspilot/`` tree on
     the selected upstream branch, When source files are enumerated or read,
     Then that tree is the sole source and no installed harness instance is
     used as source or as the enumeration basis
   * AC-2: Given an Agent, Skill, or Command source file, When it is adapted
     for a supported harness, Then its methodology body after the adapted
     structural/frontmatter boundary is preserved byte-for-byte, including
     its exact end-of-file bytes and presence or absence of a final newline,
     except for a formally designated harness tool-binding section
   * AC-3: Given two supported harnesses, When their installed methodology
     content is compared with the product source, Then only deterministic
     harness-required structural/frontmatter adaptation and the designated
     orchestration tool binding differ
   * AC-4: Skill resource paths are harness-neutral stable project paths; a
     selected non-VS-Code harness does not retain a runtime dependency on
     ``.github`` paths


.. req:: Harness Limitation Disclosure
   :id: SYSP_REQ_HARNESS_LIMITATION_DISCLOSURE
   :status: approved
   :priority: mandatory
   :tags: agent-v2, harness, portability, disclosure
   :links: SYSP_US_HARNESS_PORTABILITY

   **Description:**
   When a target harness's own extension/plugin mechanism cannot cleanly
   support full behavioral equivalence for a given capability, that
   limitation SHALL be documented as a known, honestly-disclosed
   limitation for that harness — it SHALL NOT block support on the other
   harnesses.

   **Acceptance Criteria:**

   * AC-1: Given a harness whose native mechanism cannot cleanly support a
     capability, When the limitation is discovered at design time, Then it
     is documented as a known limitation for that harness
   * AC-2: Given a documented limitation on one harness, When other
     harnesses are evaluated, Then the limitation does not block support
     on those other harnesses
   * AC-3: Given a harness limitation is disclosed, Then the disclosure never waives a mandatory production capability or independent harness acceptance.

.. req:: Harness Portability No Regression
   :id: SYSP_REQ_HARNESS_PORTABILITY_NO_REGRESSION
   :status: approved
   :priority: mandatory
   :tags: agent-v2, harness, portability, regression
   :links: SYSP_US_HARNESS_PORTABILITY

   **Description:**
    Changes made to support harness portability SHALL NOT regress existing
    VS Code Copilot Chat agent, Skill, or command behavior. Installation and
    update compatibility are owned exclusively by
    SYSP_REQ_HARNESS_INSTALL_NO_REGRESSION.

   **Acceptance Criteria:**

   * AC-1: Given a change for harness portability, When existing VS Code
     Copilot Chat users invoke agents, Skills, or commands, Then they see no
     regression in methodology behavior
   * AC-2: Given the supported methodology harnesses, When workflows run, Then VS Code GitHub Copilot and OpenCode methodology behavior is separately observable and Manager-workflow no-regression evidence is provided.
