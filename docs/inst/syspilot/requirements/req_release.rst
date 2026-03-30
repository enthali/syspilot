Release Instance Requirements
==============================

Project-specific release decisions for syspilot.

**Last Updated**: 2026-03-27


.. req:: Version File Location
   :id: INST_SYSPILOT_REQ_REL_VERSION_FILE
   :status: implemented
   :priority: mandatory
   :tags: instance, release
   :links: INST_SYSPILOT_US_REL_OWN_RELEASE, SYSPILOT_REQ_REL_SEMVER

   syspilot SHALL store its version in ``syspilot/version.json`` using SemVer format.
   The release agent reads this file for version bumps.

   * AC-1: ``syspilot/version.json`` contains ``{"version": "X.Y.Z"}``
   * AC-2: Version follows MAJOR.MINOR.PATCH (no pre-release suffixes in stable)


.. req:: GitHub Release Publication
   :id: INST_SYSPILOT_REQ_REL_GITHUB_PUBLISH
   :status: implemented
   :priority: mandatory
   :tags: instance, release
   :links: INST_SYSPILOT_US_REL_OWN_RELEASE, SYSPILOT_REQ_REL_GITHUB_PUBLISH

   syspilot SHALL publish releases via GitHub Releases with git tags ``v{version}``.

   * AC-1: Each release creates a git tag ``v{MAJOR}.{MINOR}.{PATCH}``
   * AC-2: GitHub Release includes release notes
   * AC-3: ``syspilot/version.json`` is attached as release asset


.. req:: Release Notes Format
   :id: INST_SYSPILOT_REQ_REL_NOTES_FORMAT
   :status: implemented
   :priority: mandatory
   :tags: instance, release, documentation
   :links: INST_SYSPILOT_US_REL_OWN_RELEASE, SYSPILOT_REQ_REL_NOTES

   syspilot SHALL maintain release notes in ``docs/releasenotes.md``, newest first.

   * AC-1: Each version has a ``## vX.Y.Z`` heading
   * AC-2: Sections: Features, Bug Fixes, Breaking Changes (as applicable)
   * AC-3: GitHub Actions extracts current version's notes for the GitHub Release body


.. req:: Change Document Archival
   :id: INST_SYSPILOT_REQ_REL_CHANGE_ARCHIVE
   :status: implemented
   :priority: mandatory
   :tags: instance, release, traceability
   :links: INST_SYSPILOT_US_REL_OWN_RELEASE, SYSPILOT_REQ_REL_PROCESS_DOC

   syspilot SHALL archive change documents after release to
   ``docs/changes/archive/{version}/``.

   * AC-1: All change docs from the release are moved (not deleted)
   * AC-2: Archived docs preserve git history
   * AC-3: ``docs/changes/`` is empty after release (except archive/)


.. req:: CI/CD Pipeline
   :id: INST_SYSPILOT_REQ_REL_CI_PIPELINE
   :status: implemented
   :priority: mandatory
   :tags: instance, release, automation
   :links: INST_SYSPILOT_US_REL_OWN_RELEASE, SYSPILOT_REQ_REL_GITHUB_ACTIONS

   syspilot SHALL use GitHub Actions to validate and publish releases.

   * AC-1: Workflow triggers on ``v*`` tags
   * AC-2: Validates version.json matches tag
   * AC-3: Builds Sphinx documentation (0 errors)
   * AC-4: Publishes to GitHub Releases
   * AC-5: Deploys documentation to GitHub Pages
