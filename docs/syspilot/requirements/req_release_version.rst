Release Version Consistency
===========================

.. req:: Release Version Has One Source
   :id: SYSP_REQ_RELEASE_VERSION
   :status: approved
   :implements: SYSP_US_RELEASE_CONTRACT
   :specializes: SYSP_REQ_RELEASE_CONTRACT
   :realized_by: scripts/check_release_version.py

   The version of a syspilot release shall have one source, and the tag, the
   release notes, and the published documentation shall agree with it, so that
   a release cannot ship with a version stated differently in two places. It
   shall:

   - take the release-notes headings of ``docs/releasenotes.md`` as the one
     source of the released versions, listed newest first, so that the newest
     version heading names the latest release, and introduce no second
     version file, because the version must exist in a committed file before
     the tag is created and the release notes are the committed file that the
     release already requires;
   - derive the documentation configuration's ``release`` value from that
     newest heading when the documentation is built, and not state it as a
     literal, so that the published documentation shows the latest released
     version and the value cannot drift from the release notes, which the
     literal ``0.1.0`` of the earlier configuration did;
   - provide one automated check, run with the tag as its argument and
     writing nothing, that fails with a message naming the failing condition
     unless the tag has the form ``vMAJOR.MINOR.PATCH``, exactly one
     release-notes heading names the tag's version, that heading is the newest
     version heading, and the documentation configuration's ``release`` equals
     the tag's version without the leading ``v``;
   - run that same check, and not a copy of its logic, in the preflight and in
     the tag-triggered workflow, so that the two cannot disagree, with the
     workflow wiring owned by the Admin and Release consulted as the gate owner;
   - keep the tag-triggered workflow's extraction of the release text for the
     GitHub Release from the same heading;
   - be verified by tests that reject a tag whose heading is missing,
     duplicated, or not the newest, a documentation ``release`` that differs
     from the tag, and a malformed tag, accept the matching case, and verify
     that the documentation configuration states no literal ``release``,
     which keeps the single source single; and
   - leave ``.syspilot/project.toml`` and the ontology's ``schema_version``
     out of it, because they state an installed baseline and a schema label
     and not a Syspilot release.

.. vc:: Release version agrees in tag, notes, and documentation
   :id: SYSP_VC_RELEASE_VERSION_1
   :status: approved
   :verifies: SYSP_REQ_RELEASE_VERSION

   Run the automated check for the newest release-notes version and confirm
   that it passes and writes nothing. Run it for a tag with no heading, a tag
   with two headings, an older tag whose heading is not the newest, a tag that
   differs from the documentation ``release``, and a malformed tag, and confirm
   that each fails with a message naming its condition. Confirm that the
   documentation configuration states no literal ``release``, that the
   workflow runs the same script and not a copy, and that the preflight and
   the workflow extract the release text from the same heading.
