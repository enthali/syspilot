# Change Request: ci-version-source-fix

**Status**: draft
**Created**: 2026-05-13
**Author**: PM

---

## WHY

The GitHub Actions CI workflow (`release.yml`) validates the version against `syspilot/version.json`. This file was intentionally removed when the version source was moved to the Setup Agent frontmatter (`version:` field in `syspilot/agents/syspilot.setup.agent.md`). The CI workflow was never updated to reflect this change, causing every release tag push to fail CI validation.

The v0.5.4 release tag triggered this failure. The release itself was published successfully, but CI is broken for all future releases until this is fixed.

---

## WHAT

The CI workflow shall read the version from the Setup Agent frontmatter instead of `syspilot/version.json`. The validation step shall compare the tag version against the `version:` field in `syspilot/agents/syspilot.setup.agent.md`.

Any other references to `version.json` in CI scripts or workflows shall be updated accordingly.

---

## Acceptance Criteria

- Pushing a release tag causes CI to pass validation without errors.
- CI correctly detects a version mismatch between tag and Setup Agent frontmatter.
- `syspilot/version.json` is not referenced anywhere in CI workflows or scripts.
