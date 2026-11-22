Release Version Consistency
===========================

.. req:: Release Version Has One Source
   :id: SYSP_REQ_RELEASE_VERSION
   :status: approved
   :implements: SYSP_US_RELEASE_CONTRACT
   :specializes: SYSP_REQ_RELEASE_CONTRACT
   :realized_by: scripts/check_release_version.py

   The release-version mechanism shall:

   - use ``docs/releasenotes.md`` headings as the sole source, listing released
     versions newest first, with no second version file;
   - derive the documentation configuration's ``release`` value from that
     newest heading when the documentation is built, and not state it as a
     literal;
   - provide one automated check, run with the tag as its argument and
     writing nothing, that fails with a message naming the failing condition
     unless the tag has the form ``vMAJOR.MINOR.PATCH``, exactly one
     release-notes heading names the tag's version, that heading is the newest
     version heading, and the documentation configuration's ``release`` equals
     the tag's version without the leading ``v``;
   - run that same check, not a copy, in preflight and the tag-triggered
     workflow, with wiring owned by Admin and Release consulted as gate owner;
   - keep the tag-triggered workflow's extraction of the release text for the
     GitHub Release from the same heading;
   - have automated positive and negative checks for all version conditions; and
   - exclude installed baseline ``.syspilot/project.toml`` and ontology
     ``schema_version`` from release-version sources.

.. vc:: Release version agrees in tag, notes, and documentation
   :id: SYSP_VC_RELEASE_VERSION_1
   :status: approved
   :verifies: SYSP_REQ_RELEASE_VERSION

   The newest release's matching tag passes without writing. Missing,
   duplicate or older headings, a mismatched documentation version and a
   malformed tag each fail with a diagnostic naming the condition.

.. vc:: Documentation derives its release from the sole source
   :id: SYSP_VC_RELEASE_VERSION_2
   :status: approved
   :verifies: SYSP_REQ_RELEASE_VERSION

   Documentation configuration contains no literal ``release`` and derives the
   newest notes heading; installed baseline and schema labels are not consulted.

.. vc:: Preflight and workflow use the same version check
   :id: SYSP_VC_RELEASE_VERSION_3
   :status: approved
   :verifies: SYSP_REQ_RELEASE_VERSION

   Preflight and the tag-triggered workflow execute the shared checker, not
   copied logic.

.. vc:: Workflow release text comes from the same heading
   :id: SYSP_VC_RELEASE_VERSION_4
   :status: approved
   :verifies: SYSP_REQ_RELEASE_VERSION

   GitHub Release text extraction uses the release-notes heading that supplies
   the checked version.

.. vc:: Version-check wiring preserves workflow ownership
   :id: SYSP_VC_RELEASE_VERSION_5
   :status: approved
   :verifies: SYSP_REQ_RELEASE_VERSION

   Wiring changes record Admin ownership and mandatory Release consultation.
