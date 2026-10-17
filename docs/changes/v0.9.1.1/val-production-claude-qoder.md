# Validation Report: production-claude-qoder

**Change Document:** `docs/changes/v0.9.1.1/production-claude-qoder.md`

**Branch:** `feature/production-claude-qoder`

**Verification date:** 2026-09-18

**Result:** FAILED
**Qoder live production clearance:** BLOCKED independently of deterministic implementation correctness

## Findings

### High

1. **The shipped Installer diagnostics contradict the four-harness production contract.**
   `syspilot/agents/syspilot.installer.agent.md:41` says that only `vscode` and
   `opencode` are production harnesses and calls Claude Code and Qoder
   experimental. Line 53 repeats the experimental classification. This
   violates `docs/syspilot/design/spec_installer.rst:239-244`, which requires
   shipped invocation text not to classify either harness as unsupported or
   experimental. The existing assertion at `tests/test_installer.py:2765-2777`
   rejects a different obsolete sentence and does not detect the current text.

2. **The Qoder native-install chain does not preserve the approved L0/L1
   outcome.** `docs/syspilot/userstories/us_harness_install.rst:32` and
   `docs/syspilot/requirements/req_harness_install.rst:17` require a complete
   native installation outcome, while
   `docs/syspilot/design/spec_harness_install_entry.rst:39-41` and
   `docs/syspilot/design/spec_harness_adapters.rst:85-109` stop at an externally
   imported staged archive. The structural links resolve, but live Qoder
   production parity remains blocked.

3. **The Qoder installer-target chain is semantically contradictory.**
   `docs/syspilot/userstories/us_uat_installer_harness_targets.rst:86-94`
   requires generated `.qoder/agents` and `.qoder/skills` plus native
   invocation. `docs/syspilot/design/spec_uat_installer_harness_targets.rst:97-114`
   instead requires one staged archive and explicitly rejects a live `.qoder`
   tree or parity claim. The implementation correctly follows the approved L2
   staging design, but the vertical intent is not reconciled.

4. **The exclusive Qoder native-loading owner has no complete native-loading
   acceptance.** `docs/syspilot/requirements/req_uat_harness_target_matrix.rst:68`
   mandates complete Manager, Engineer, Skill, and invocation loading. The
   designated native scenario at
   `docs/syspilot/design/spec_uat_harness_target_matrix.rst:74-94` explicitly
   excludes Qoder loading, and the external-import scenario at lines 98-115
   records package identity and visible surfaces without proving completeness.

### Medium

5. **Qoder one-time enablement remains underspecified across the staged/imported
   boundary.** `docs/syspilot/design/spec_uat_harness_one_time_enablement.rst:27`
   requires successful installation for every production harness, while
   `docs/syspilot/design/spec_harness_install_entry.rst:39-41` reports Qoder as
   staged. No scenario proves that the external UI import persists without
   repeated enablement. This is a specification/UAT evidence gap, not a defect
   in archive rollback.

### Low

6. `docs/syspilot/userstories/us_uat_harness_orchestration_adapter.rst:16`
   still describes one-hop SEND behavior, while its acceptance criteria at
   lines 30-35 correctly reject one-hop evidence and require complete
   autonomous orchestration. L1 and L2 use the stronger rule.

7. Status alignment is inconsistent although links resolve:
   `SYSP_REQ_SKILL_ARCH_FRONTMATTER` is approved while its scoped L2 consumer
   remains draft, and approved README requirement/design elements link through
   draft `SYSP_US_DOC_EXTERNAL`.

## Implementation Obligations

| Obligation | Result | Evidence |
|---|---|---|
| Exactly four public selectors | PASS | `syspilot/installer.py:59`, `tests/test_installer.py:2884-2905` |
| Isolated harness mappings | PASS | `syspilot/installer.py:53-58,1526-1580`; full installer suite |
| Claude Code and OpenCode adapter behavior | PASS | `syspilot/installer.py:816-965`, `tests/test_installer.py:63-140,2503-2589`; OpenCode native config test ran, live delegation remained opt-in |
| Deterministic Qoder ZIP identity/content and no live tree | PASS | `syspilot/installer.py:61-63,1442-1535`, `tests/test_installer.py:596-632` |
| Transactional update, injected failure, and rollback | PASS | `syspilot/installer.py:1646-1745,2200-2296`, `tests/test_installer.py:562-660`; full suite |
| Setup forwards selected harness unchanged | PASS | `syspilot/agents/syspilot.setup.agent.md:34-55`, `tests/test_installer.py:2778-2787` |
| Canonical Claude Code wording | PASS | `README.md:22-35`, `syspilot/agents/syspilot.setup.agent.md:34`; no active product `Claude CLI` match |
| README and architecture accurately state boundaries | PASS | `README.md:44-56`, `docs/architecture.md:18-40` |
| Explicit external Qoder import and autonomous-orchestration blocker | PASS | `README.md:52-56`, `docs/architecture.md:31-40` |
| Shipped production classification is consistent | FAIL | `syspilot/agents/syspilot.installer.agent.md:41,53` |

Implementation alignment assessed all 27 declared L2 elements: **26 PASS, 1
FAIL** (`SYSP_SPEC_INSTALLER_WORKFLOW`). Therefore implementation verification
does not pass.

## Traceability

A nested SEND to `Trace Engineer` checked all 27 declared L2 elements and all
23 declared L1 requirements against current RST sources.

- L2 elements checked: **27**
- L1 requirements checked: **23**
- Structurally complete L2 -> L1 -> L0 chains: **27**
- Structurally incomplete chains: **0**
- L1 requirements with at least one scoped L2 consumer: **23/23**
- Broken IDs, missing directives/files, unresolved scoped links: **0**
- Semantic trace findings: **6** (**3 high, 1 medium, 2 low**)

Structural completeness does not waive the semantic findings above.

## Executable Validation

| Check | Result | Counts |
|---|---|---|
| `UV_NO_INDEX=1 PYTHONPATH=. uv run --no-project --with pytest --with pyyaml pytest -q tests/test_installer.py` | PASS | 111 passed, 100 subtests passed, 4 skipped, 0 failed, 34.64 s |
| `UV_NO_INDEX=1 uv run --no-project --with pytest pytest -q docs/test_docs_build.py` | PASS | 4 passed, 0 skipped, 0 failed |
| `cd docs && UV_NO_INDEX=1 uv run --offline python docs-build.py clean` | PASS | 0 warnings, 0 errors, 0 schema violations |
| `git diff --check` | PASS | 0 whitespace errors |
| VS Code diagnostics on runtime, tests, README, and architecture | PASS | 0 diagnostics |

The four skipped installer tests were two Windows-only normalization checks,
the network-conditional GitHub API acquisition check, and opt-in live OpenCode
delegation. No live Qoder import, native loading, or autonomous ordered-token
workflow was executed or inferred.

## Disposition

Implementation verification is **FAILED** because one shipped product artifact
contradicts the approved production classification. Specification statuses were
not changed. Deterministic Qoder staging, update, failure, and rollback are
implemented and tested; Qoder live production clearance remains separately
**BLOCKED** pending external import evidence and a repeatable native autonomous
Manager transcript that invokes every required Engineer and consumes every
ordered result without user relay.