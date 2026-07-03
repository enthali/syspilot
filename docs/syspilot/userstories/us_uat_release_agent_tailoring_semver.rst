Release Agent Tailoring Semver UAT
==================================

User Acceptance Test Story for the ``release-agent-tailoring-semver`` change
request, covering the Release Engineer's generic, tailorable versioning
approach, the new generic Skill Tailoring architecture applied to the
branching skill, and the regression-prevention scenario for GH #44 (CalVer
silently applied to a customer project requiring semver).


.. story:: UAT: Release Agent Tailoring & Semver Regression Prevention
   :id: SYSP_US_UAT_RELEASE_TAILORING_SEMVER
   :status: draft
   :priority: mandatory
   :tags: uat, release, tailoring, skill-arch, branching, semver
   :links: SYSP_US_RELEASE, SYSP_US_SKILL_ARCH, SYSP_US_SKILL_BRANCHING

   **As a** syspilot Test Designer,
   **I want** self-contained test scenarios that let a human verify the
   Release Engineer determines versions generically via a per-project
   tailoring file (never a hardcoded scheme), correctly escalates when
   that tailoring file is missing, reads its version source-of-truth from
   the ``docs/changes/`` archive rather than syspilot's own framework
   version, that the new Skill Tailoring architecture is genuinely generic
   and not branching-specific, that feature-branch retention now defaults
   to retain, and — most importantly — that no project's versioning scheme
   can silently leak into a different project again,
   **so that** the GH #44 incident (CalVer applied to Jarvis, whose
   ``package.json`` requires semver) cannot recur.

   **Context:**

   The ``release-agent-tailoring-semver`` CR gives the Release Engineer the
   same Tailoring Workflow pattern PM already uses: versioning scheme and
   version-write-target are project-specific tailoring decisions, never
   hardcoded in the agent spec. It also corrects a category error — the
   Release Engineer's version source-of-truth was syspilot's own framework
   version marker, not the customer project's own product version — and
   introduces a generic, reusable Skill Tailoring architecture, applied
   concretely to the ``syspilot.branching`` skill's feature-branch
   retention policy (default flipped from delete to retain).

   **Artifacts Under Test:**

   * ``docs/syspilot/design/spec_release_engineer.rst`` —
     ``SYSP_SPEC_RELEASE_DUTIES``, ``SYSP_SPEC_RELEASE_WORKFLOW``
   * ``docs/syspilot/design/spec_skill_arch.rst`` —
     ``SYSP_SPEC_SKILL_ARCH_TAILORING``
   * ``docs/syspilot/design/spec_skill_branching.rst`` —
     ``SYSP_SPEC_SKILL_BRANCHING_RETENTION``,
     ``SYSP_SPEC_SKILL_BRANCHING_PERMISSIONS``
   * ``syspilot/agents/syspilot.release.agent.md`` — Release Engineer agent
   * ``syspilot/skills/syspilot.branching/SKILL.md`` — Branching skill
   * ``.github/agents/syspilot.release.tailoring.md`` — syspilot's own
     instance tailoring file (expected: specifies semver)
   * Two separate target projects for the cross-project isolation scenario
     (one tailored to semver, one tailored to CalVer or untailored)

   **Traceability:**

   Covers ``SYSP_REQ_RELEASE_WORKFLOW`` AC-2, AC-8 (generic version
   determination, tailoring-file Preflight); ``SYSP_REQ_RELEASE_DUTIES``
   AC-4 (version consistency, tailoring-defined marker location);
   ``SYSP_REQ_SKILL_ARCH_TAILORING`` AC-1 through AC-4 (generic Skill
   Tailoring contract); ``SYSP_REQ_SKILL_BRANCHING_RETENTION`` (retention
   default: retain).
   Test data is defined in ``SYSP_REQ_UAT_RELEASE_TAILORING_SEMVER``;
   expected outcomes in ``SYSP_SPEC_UAT_RELEASE_TAILORING_SEMVER``.

   **Acceptance Criteria:**

   1. **No hardcoded versioning scheme in the Release Engineer spec.**
      *Precondition:* ``SYSP_SPEC_RELEASE_WORKFLOW`` Step 3 ("Determine
      Next Version") is readable.
      *Action:* Read Step 3 and search the whole spec node for concrete
      scheme names (``CalVer``, ``semver``, ``vYYYY.MM.DD``, or any other
      literal scheme identifier).
      *Expected result:* Step 3 states the scheme is read from
      ``syspilot.release.tailoring.md`` and is "never hardcoded in this
      spec"; zero concrete scheme names appear anywhere in the spec node
      body — traces to ``SYSP_REQ_RELEASE_WORKFLOW`` AC-2

   2. **Version source-of-truth is the change-doc archive, not syspilot's own framework version.**
      *Precondition:* ``SYSP_SPEC_RELEASE_WORKFLOW`` Step 3 is readable.
      *Action:* Read Step 3's description of where the current version is
      read from.
      *Expected result:* Step 3 states the current version is read from
      "the latest existing ``docs/changes/<version>/`` archive folder" and
      explicitly distinguishes this from "syspilot's own framework
      version" — traces to ``SYSP_REQ_RELEASE_WORKFLOW`` AC-2

   3. **Missing tailoring file triggers RESPOND-to-PM escalation (behavioural).**
      *Precondition:* A target project with a syspilot installation where
      ``.github/agents/syspilot.release.tailoring.md`` does not exist.
      *Action:* Invoke ``@syspilot.release`` (or trigger it via PM) to
      begin a release.
      *Expected result:* Before determining the next version, the Release
      Engineer RESPONDs that tailoring is needed — it does not assume a
      versioning scheme or silently proceed — traces to
      ``SYSP_REQ_RELEASE_WORKFLOW`` AC-8

   4. **syspilot's own tailoring file specifies semver.**
      *Precondition:* The syspilot repository itself, on this branch.
      *Action:* Open ``.github/agents/syspilot.release.tailoring.md``.
      *Expected result:* The file exists and states that the project's
      versioning scheme is semantic versioning (semver) — traces to the
      CR's own Decisions (syspilot instance reverted from CalVer to semver)

   5. **⚠ Regression-prevention — cross-project tailoring isolation (the GH #44 scenario).**
      *Precondition:* Two separate target projects, each with its own
      syspilot installation and its own ``syspilot.release.tailoring.md``:
      Project A's tailoring file specifies semver (mirrors the Jarvis
      incident's requirement); Project B's tailoring file specifies CalVer
      (or any different scheme).
      *Action:* Run a release on Project A. Independently, run a release
      on Project B.
      *Expected result:* Project A's next version follows semver and
      Project B's next version follows CalVer — each project's release
      artifact (version file, tag, archive folder name) reflects only its
      own tailoring file; neither project's scheme choice is observable
      in the other's output at any point — this is the exact scenario
      that, if it had existed before this CR, would have caught the
      original GH #44 incident before it shipped — traces to
      ``SYSP_REQ_RELEASE_WORKFLOW`` AC-2, AC-8

   6. **Skill Tailoring architecture is generic — not branching-specific.**
      *Precondition:* ``SYSP_SPEC_SKILL_ARCH_TAILORING`` is readable.
      *Action:* Read the full spec node body. Search for any wording that
      names the branching skill or any other single Skill by name as part
      of the *rule* (not as an illustrative example).
      *Expected result:* The rule text (File, Format, Behavior,
      Instance-only, Difference-from-Agent-tailoring) describes the
      contract in terms of "a Skill" / "the Skill's documented
      conventions" generically; any mention of ``syspilot.branching`` is
      confined to the illustrative file-path example, never to the rule
      itself — traces to ``SYSP_REQ_SKILL_ARCH_TAILORING`` AC-1 through
      AC-4

   7. **Feature-branch retention defaults to retain.**
      *Precondition:* A target project with a syspilot installation, no
      ``.github/skills/syspilot.branching/tailoring.md`` override present,
      and at least one ``feature/*`` branch fully merged into
      ``development``.
      *Action:* Run a release via ``@syspilot.release``.
      *Expected result:* After the release completes, the merged
      ``feature/*`` branch still exists (locally and on remote) — it is
      not deleted — traces to ``SYSP_REQ_SKILL_BRANCHING_RETENTION``
