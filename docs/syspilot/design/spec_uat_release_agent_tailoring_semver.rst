Release Agent Tailoring Semver Expected Outcomes
=================================================

Expected outcomes specification for
``SYSP_REQ_UAT_RELEASE_TAILORING_SEMVER``. This document is the
per-scenario verification checklist a human tester runs.


.. spec:: UAT Expected Outcomes: Release Agent Tailoring & Semver Regression Prevention
   :id: SYSP_SPEC_UAT_RELEASE_TAILORING_SEMVER
   :status: draft
   :priority: mandatory
   :tags: uat, release, tailoring, skill-arch, branching, semver, expected-outcomes
   :links: SYSP_REQ_UAT_RELEASE_TAILORING_SEMVER

   **Definition:**

   For each scenario in ``SYSP_US_UAT_RELEASE_TAILORING_SEMVER``, the
   following outcomes SHALL be observable. Each scenario is self-contained:
   the human tester prepares the named fixture (if any), runs the action,
   and confirms the expected result. A check item passes when the exact
   condition is met; it fails otherwise.

   ---

   **TC-RTS-NOSCHEME — No hardcoded versioning scheme**

   *Precondition:* Branch ``feature/release-agent-tailoring-semver``
   checked out.

   *Action:* Read ``SYSP_SPEC_RELEASE_WORKFLOW`` Step 3; search the whole
   spec node body for ``CalVer``, ``semver``, ``vYYYY.MM.DD``, or any other
   literal scheme identifier.

   *Expected result:*

   * [ ] Step 3 states the scheme is read from
     ``syspilot.release.tailoring.md``
   * [ ] Step 3 (or the node) explicitly states the scheme is never
     hardcoded in the spec
   * [ ] Zero concrete scheme names found anywhere in the node body

   *Traces to:* ``SYSP_US_UAT_RELEASE_TAILORING_SEMVER`` AC-1

   ---

   **TC-RTS-ARCHIVESOURCE — Archive-based version source-of-truth**

   *Precondition:* Branch checked out.

   *Action:* Read ``SYSP_SPEC_RELEASE_WORKFLOW`` Step 3's description of
   the current-version source.

   *Expected result:*

   * [ ] Step 3 states the current version is read from the latest
     ``docs/changes/<version>/`` archive folder
   * [ ] Step 3 explicitly distinguishes this from syspilot's own
     framework version marker

   *Traces to:* ``SYSP_US_UAT_RELEASE_TAILORING_SEMVER`` AC-2

   ---

   **TC-RTS-ESCALATE — Missing tailoring file triggers escalation**

   *Precondition:* Fixture ``F-NO-TAILORING`` (target project, syspilot
   installed, no ``syspilot.release.tailoring.md``).

   *Action:* Trigger a release via ``@syspilot.release`` (directly or via
   PM).

   *Expected result:*

   * [ ] The Release Engineer RESPONDs that tailoring is needed before any
     version-determination step runs
   * [ ] No version is computed or written
   * [ ] No file is archived and no branch/tag operation occurs

   *Traces to:* ``SYSP_US_UAT_RELEASE_TAILORING_SEMVER`` AC-3

   ---

   **TC-RTS-SYSPILOT-SEMVER — syspilot's own tailoring specifies semver**

   *Precondition:* This branch, syspilot repository.

   *Action:* Open ``.github/agents/syspilot.release.tailoring.md``.

   *Expected result:*

   * [ ] The file exists
   * [ ] The file states the versioning scheme is semantic versioning
     (semver)

   *Traces to:* ``SYSP_US_UAT_RELEASE_TAILORING_SEMVER`` AC-4

   ---

   **TC-RTS-ISOLATION — Cross-project tailoring isolation (GH #44 regression test)**

   *Precondition:* Fixtures ``F-PROJECT-SEMVER`` (Project A, tailored to
   semver) and ``F-PROJECT-CALVER`` (Project B, tailored to CalVer), two
   fully independent target projects.

   *Action:* Run a release on Project A. Independently, run a release on
   Project B. Compare each project's resulting version artifacts.

   *Expected result:*

   * [ ] Project A's new version string follows semver
     (``MAJOR.MINOR.PATCH``)
   * [ ] Project B's new version string follows CalVer
     (``vYYYY.MM.DD`` or the project's configured date-based pattern)
   * [ ] Project A's version marker, tag, and archive folder name never
     contain a CalVer-shaped string
   * [ ] Project B's version marker, tag, and archive folder name never
     contain a semver-shaped string
   * [ ] Neither project's ``syspilot.release.tailoring.md`` content
     changed as a side effect of releasing the other project

   *Traces to:* ``SYSP_US_UAT_RELEASE_TAILORING_SEMVER`` AC-5. **This is
   the regression scenario for GH #44** — had this UAT scenario existed
   and been run before the original incident, the CalVer-into-Jarvis
   defect would have been caught by the second check item.

   ---

   **TC-RTS-SKILLTAILORING-GENERIC — Skill Tailoring is generic, not branching-specific**

   *Precondition:* Branch checked out.

   *Action:* Read the full ``SYSP_SPEC_SKILL_ARCH_TAILORING`` node body;
   search for any Skill name used as part of the rule text itself (File,
   Format, Behavior, Instance-only, Difference-from-Agent-tailoring
   subsections).

   *Expected result:*

   * [ ] Every rule subsection describes the contract generically ("a
     Skill", "the Skill's documented conventions") without naming
     ``syspilot.branching`` or any other specific Skill
   * [ ] The only occurrence of ``syspilot.branching`` in the node is
     inside the illustrative file-path example, clearly marked as an
     example

   *Traces to:* ``SYSP_US_UAT_RELEASE_TAILORING_SEMVER`` AC-6

   ---

   **TC-RTS-RETAIN — Feature-branch retention defaults to retain**

   *Precondition:* Fixture ``F-RETAIN-DEFAULT`` (target project, no
   branching-skill tailoring override, one ``feature/*`` branch merged
   into ``development``).

   *Action:* Run a release via ``@syspilot.release``.

   *Expected result:*

   * [ ] The release completes successfully
   * [ ] The previously-merged ``feature/*`` branch still exists locally
   * [ ] The previously-merged ``feature/*`` branch still exists on remote

   *Traces to:* ``SYSP_US_UAT_RELEASE_TAILORING_SEMVER`` AC-7
