Skill: DEFINITIONS Dictionary
==============================

Requirements for the global Skill DEFINITIONS Dictionary.


.. req:: Global DEFINITIONS Dictionary
   :id: SYSP_REQ_SKILL_DEFINITIONS
   :status: draft
   :priority: mandatory
   :tags: agent-v2, skill, architecture, definitions
   :links: SYSP_US_SKILL_ARCH

   **Description:**

   syspilot SHALL maintain a single global DEFINITIONS Registry: every
   DEFINITION used by any Skill SHALL be published exactly once as a
   sphinx-needs ``def`` need. Group Contract Specs reference the DEFINITIONS
   of their group via a dedicated link type (``:defines:``). The Registry is
   the single source of truth — no DEFINITION text or identity is duplicated
   elsewhere.

   **Rationale:**

   Skills are loaded based on the DEFINITIONS they declare. If two Skills
   from different groups declared the same DEFINITION name, Skill resolution
   would be ambiguous and the wrong Skill could be loaded. Publishing each
   DEFINITION as a sphinx-needs ``def`` with a unique ID makes collisions
   structurally impossible — sphinx-needs rejects duplicate IDs at build
   time. No manual cross-checking and no risk of registry drift.

   **Concepts:**

   * **DEFINITION** — a named verb or value that an Agent uses by name.
     Always written in uppercase (e.g. ``MERGE``). Published as a ``def``
     need with ID ``SYSP_DEF_<NAME>``.
   * **Group** — the contract boundary. All Skills of the same group
     implement the same set of DEFINITIONS. Only one Skill per group may
     be installed at a time (Mutual Exclusion).
   * **Group Contract Spec** — a ``spec`` need (``SYSP_SPEC_SKILL_<GROUP>_CONTRACT``)
     that links to the DEFINITIONS of its group via ``:defines:``.
   * **Registry** — the single page (``SYSP_SPEC_SKILL_DEFINITIONS``) that
     contains every ``def`` need.

   **Rules:**

   1. Every DEFINITION SHALL be published as exactly one ``def`` need on
      the Registry page, with ID ``SYSP_DEF_<NAME>``.
   2. ID uniqueness is enforced by sphinx-needs (collision check is
      structural, not manual).
   3. Each Skill group that uses DEFINITIONS SHALL have a Group Contract
      Spec (``SYSP_SPEC_SKILL_<GROUP>_CONTRACT``) that links to its
      DEFINITIONS via ``:defines:``.
   4. Concrete Skill specs SHALL link to their Group Contract Spec — not
      directly to ``def`` needs.
   5. Agent specs SHALL link to the Group Contract Spec of every group whose
      DEFINITIONS the Agent uses — not directly to ``def`` needs.
   6. Adding, renaming, or removing a DEFINITION SHALL update the Registry
      page and the relevant Group Contract Spec in the same Change Request.
   7. Only one Skill per group SHALL be installed at a time (Mutual
      Exclusion enforced by the Setup Agent).
   8. The full operational instruction for a DEFINITION (commands, LLM
      guidance, edge cases) SHALL live in the Skill that implements it,
      not in the ``def`` need itself.

   **Acceptance Criteria:**

   * AC-1: A single Registry page exists with one ``def`` need per
     DEFINITION; IDs follow ``SYSP_DEF_<NAME>``
   * AC-2: ID uniqueness is enforced by sphinx-needs (build fails on
     duplicate IDs)
   * AC-3: For each group that uses DEFINITIONS, a Group Contract Spec
     exists and links to its DEFINITIONS via ``:defines:``
   * AC-4: Skills link to their Group Contract Spec, not directly to
     ``def`` needs
   * AC-5: Agents link to the Group Contract Spec of every group whose
     DEFINITIONS they use
   * AC-6: Every DEFINITION listed in a Group Contract is implemented by
     every Skill of that group
   * AC-7: Only one Skill per group is installed at a time (Mutual
     Exclusion enforced by the Setup Agent)
