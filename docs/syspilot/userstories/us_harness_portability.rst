Harness Portability
====================

Behavioral equivalence of syspilot's methodology across AI coding harnesses.


.. story:: Harness-Portable Methodology
   :id: SYSP_US_HARNESS_PORTABILITY
   :status: approved
   :priority: mandatory
   :tags: agent-v2, harness, portability
   :links: SYSP_US_AGENT_ARCH, SYSP_US_SKILL_ARCH

   **As a** syspilot user working in any production-parity harness,
   **I want to** invoke syspilot's agents and skills and receive the same
   guidance and results as a VS Code Copilot Chat user does today,
   **so that** my choice of AI coding harness does not lock me out of the
   methodology.

   **Context:**

   syspilot's agents and skills today are expressed exclusively as VS Code
   custom-agent files bound to Copilot Chat's tool and model conventions.
   This story requires that the methodology content — what each agent does,
   what each skill teaches — be authored once and installed, without
   behavioral drift, onto every supported harness.

   Each target harness's actual current extension/plugin/hook mechanism is
   researched at design time (Level 2), rather than assumed from prior
   knowledge. VS Code GitHub Copilot, OpenCode, and Claude Code are
   production-parity harnesses. Each must provide usable roles, Skills,
   commands or prompts, and Manager-to-Engineer orchestration with equivalent
   user-visible methodology behavior. Qoder is an explicitly disclosed
   experimental, installable harness: it must provide usable roles and
   Skills through its deterministic package-staging artifact, but native
   in-app import and Manager-to-Engineer orchestration parity for Qoder are
   deferred to a future change and are not required here. Harness-specific
   limitations remain honestly disclosed, but do not waive production
   capabilities on the production-parity tier.

   **Acceptance Criteria:**

   1. Given a production-parity harness (VS Code GitHub Copilot,
      OpenCode, or Claude Code), When I invoke a syspilot Manager agent,
      Then I receive the same Soul/Duties/Workflow-driven behavior as on any
      other production-parity harness
   2. Given a production-parity harness, When I consult a syspilot Skill, Then its Instructions and Rules are applied identically to how they are applied on VS Code Copilot Chat
   3. Given the methodology content (agent and skill definitions) is authored once in ``syspilot/``, When it is installed onto any target harness, Then no harness-specific fork of the behavioral content is maintained — only deterministic structural/frontmatter adapters differ per harness
   4. Given a target harness's own extension/plugin mechanism cannot cleanly support full behavioral equivalence for a given capability, When that limitation is discovered at design time, Then it is documented as a known, honestly-disclosed limitation for that harness rather than blocking support on the other harnesses
   5. Given a change is made for harness portability, When existing VS Code
      GitHub Copilot or OpenCode users invoke agents, Skills, commands, or
      Manager workflows, Then they see no regression in methodology behavior
   6. Given Claude Code is evaluated for production support, When its
      quality gate runs, Then native role and Skill invocation, command or
      prompt invocation, and Manager-to-Engineer orchestration are cleared
      independently for that harness; the clean-install, update, and
      rollback lifecycle pass/fail criteria for Claude Code are owned
      exclusively by ``SYSP_US_HARNESS_INSTALL`` and are not restated here
   7. Given Qoder is evaluated at the experimental, installable tier, When
      its quality gate runs, Then native import and Manager-to-Engineer
      orchestration remain explicitly out of scope and deferred to a future
      change, not silently dropped; the deterministic package-staging
      clean-stage, repeat-stage, and rollback pass/fail criteria for Qoder
      are owned exclusively by ``SYSP_US_HARNESS_INSTALL`` and are not
      restated here
   8. Given a production-parity harness, When a syspilot workflow invokes
      another agent or resolves a shipped Skill resource, Then the installed
      artifact uses that harness's native orchestration binding and a stable
      harness-neutral shared path without forking the semantic methodology
   9. Given product-facing content refers to the Claude Code harness,
      When a user reads that content, Then the harness is named ``Claude Code``
      without an environment-specific launcher name
   10. Given Claude Code is used to start a representative syspilot Manager
       workflow in autonomous product operation, When the workflow progresses
       through its required stages, Then the Manager completes the end-to-end
       workflow, including all required Engineer delegations and returned
       results, without user approval gates between stages. This acceptance
       does not apply to Qoder for this change; Qoder Manager-to-Engineer
       orchestration parity is deferred future scope, not a criterion cleared
       or waived here.
