# Change Document: setup-preserve-tools

**Status**: in-progress
**Branch**: feature/setup-preserve-tools
**Created**: 2026-05-01
**Author**: syspilot.cm

---

## Summary

When the Setup Agent updates installed agents from product source, it must
preserve the instance-specific `tools:` frontmatter field in each target
file. Only body content and non-tools frontmatter fields are overwritten.
Fresh installs copy `tools:` from product as-is. New agents are always
copied completely.

---

## Change Request (from PM)

> **Mode:** user-guided
>
> **Intent (WHAT):**
> When the Setup Agent updates installed agents from product source, it must
> preserve the instance-specific `tools:` frontmatter field in the target
> files. Only the body content and other frontmatter fields (description,
> agents, version) should be updated from the product.
>
> **Motivation (WHY):**
> The `tools:` field in installed agents is project-specific — it lists the
> actual VS Code tool namespaces available in that environment (jarvis MCP
> servers, github extension, context7, etc.). These differ per installation
> and are configured post-install. Overwriting them during an update breaks
> all agent capabilities.
>
> **Acceptance Criteria:**
> 1. During an update, the Setup Agent SHALL preserve the existing `tools:` line in each target agent file
> 2. During a fresh install, the Setup Agent SHALL copy the `tools:` from product as-is (since no instance customization exists yet)
> 3. If the product adds a NEW agent that doesn't exist in the instance, it SHALL be copied completely (including `tools:`)
> 4. The user SHALL be informed which agents were updated and that `tools:` were preserved

---

## Impact Analysis (CM)

**Performed**: 2026-05-01
**Method**: `get_need_links.py <id> --direction in --depth 1` from SYSP_US_SETUP, then depth 1 from each resulting REQ.

**From SYSP_US_SETUP (direct REQs):**
```
SYSP_REQ_SETUP_SOUL, SYSP_REQ_SETUP_DUTIES, SYSP_REQ_SETUP_WORKFLOW,
SYSP_REQ_SETUP_FRONTMATTER, SYSP_REQ_SETUP_PROMPT
```

**From Setup REQs (direct SPECs):**
```
SYSP_REQ_SETUP_SOUL     → SYSP_SPEC_SETUP_SOUL
SYSP_REQ_SETUP_DUTIES   → SYSP_SPEC_SETUP_DUTIES
SYSP_REQ_SETUP_WORKFLOW → SYSP_SPEC_SETUP_WORKFLOW
```

**In-scope elements (workflow/duties concern):**
- SYSP_US_SETUP
- SYSP_REQ_SETUP_DUTIES, SYSP_REQ_SETUP_WORKFLOW
- SYSP_SPEC_SETUP_DUTIES, SYSP_SPEC_SETUP_WORKFLOW

**Soul impact:** Requires Designer assessment — the distinction between
"faithful copy" vs. "selective merge" may touch soul character text.

**Out of scope:** FRONTMATTER and PROMPT elements (not behavioral concerns).

**Agent file in scope:**
- `syspilot/agents/syspilot.setup.agent.md`

---

## Process Log

| Step | Agent | Status | Commit | Notes |
|------|-------|--------|--------|-------|
| Branch created | CM | ✅ | — | feature/setup-preserve-tools |
| Impact Analysis | CM | ✅ | — | See section above |
| Change Document | CM | ✅ | — | This file |
| Design (L0) | syspilot.design | ✅ | — | AC-7 added to SYSP_US_SETUP |
| Design (L1) | syspilot.design | ✅ | — | AC-7/8/9 DUTIES, AC-7 WORKFLOW; SOUL unchanged |
| Design (L2) | syspilot.design | ✅ | — | Duty #4 selective merge; Step #4 per-agent tools: handling |
| Implement | syspilot.implement | ✅ | ab73928 | — |
| Verify | syspilot.verify | ⏳ | — | — |
| PM Approval | PM | ⏳ | — | — |
| Merged | CM | ⏳ | — | — |

---

## Level 0: User Stories

**Status**: ✅ done

### Impacted User Stories

| ID | Title | Impact | Notes |
|----|-------|--------|-------|
| `SYSP_US_SETUP` | Setup Manager Agent | modified | Update behavior: tools: preservation |

### Designer Section

**Decision:** Added AC-7 to `SYSP_US_SETUP`. The existing AC-5 covers the general
"user made customizations" guard (interactive, user-driven). AC-7 covers the
automatic `tools:` preservation (no user interaction — happens silently during
every agent file update), plus the user notification after the fact.

**Soul assessment:** `SYSP_US_SETUP` does not define soul; `SYSP_REQ_SETUP_SOUL` /
`SYSP_SPEC_SETUP_SOUL` unchanged — the soul character (helpful, user-friendly,
first impression) is a personality trait unaffected by this behavioral detail.
The fresh-install vs. update distinction already exists in the spec hierarchy.

**Change:** `us_setup_engineer.rst` — AC-7 added.

---

## Level 1: Requirements

**Status**: ✅ done

### Impacted Requirements

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| `SYSP_REQ_SETUP_DUTIES` | `SYSP_US_SETUP` | modified | AC-7/8/9: selective merge, fresh-install copy, user notification |
| `SYSP_REQ_SETUP_WORKFLOW` | `SYSP_US_SETUP` | modified | AC-7: detect + re-inject tools: during update |
| `SYSP_REQ_SETUP_SOUL` | `SYSP_US_SETUP` | no change | Soul character unaffected by behavioral detail |

### Designer Section

**SYSP_REQ_SETUP_SOUL:** No change. The soul character (helpful, user-friendly,
first impression) is a personality trait. The install/update distinction is already
captured in Duties/Workflow. Adding merge detail there does not alter the soul.

**SYSP_REQ_SETUP_DUTIES:** AC-7 (selective merge during update), AC-8 (full copy
during fresh install or new agent), AC-9 (user notification) added. These three ACs
map 1:1 to the four acceptance criteria from the Change Request.

**SYSP_REQ_SETUP_WORKFLOW:** AC-7 (detect + re-inject `tools:` per file during update)
added. This is the step-level complement to Duties AC-7 — Duties defines WHAT,
Workflow defines the sequencing trigger (before overwriting → save, after copying → re-inject).

**Change:** `req_setup_engineer.rst` — AC-7/8/9 added to DUTIES, AC-7 added to WORKFLOW.

---

## Level 2: Design

**Status**: ✅ done

### Impacted Design Elements

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| `SYSP_SPEC_SETUP_DUTIES` | `SYSP_REQ_SETUP_DUTIES` | modified | Duty #4 rewritten with selective merge logic |
| `SYSP_SPEC_SETUP_WORKFLOW` | `SYSP_REQ_SETUP_WORKFLOW` | modified | Step #4 expanded with per-agent tools: handling |
| `SYSP_SPEC_SETUP_SOUL` | `SYSP_REQ_SETUP_SOUL` | no change | Confirmed: soul character unaffected |

### Designer Section

**SYSP_SPEC_SETUP_SOUL:** No change. Character description (helpful, user-friendly,
thorough, reassuring) and guardrails (validates, never leaves broken state) are
not altered by the selective-merge behavior.

**SYSP_SPEC_SETUP_DUTIES:** Duty #4 "File Installation" rewritten. Now distinguishes
explicitly: (a) update mode + existing file → selective merge preserving `tools:`,
(b) fresh install or new agent → full copy from product. Post-write notification
added. Duty #8 "Customization Guard" unchanged — it handles user-reported
file-body customizations and is orthogonal.

**SYSP_SPEC_SETUP_WORKFLOW:** Step #4 "Install/Update" expanded. The per-agent
`tools:` detection/re-injection block is placed first, before the
customization-guard interaction. Order: (1) selective merge all agent files,
(2) report agents updated + tools: preserved, (3) ask user about customizations.

---

## Final Consistency Check

**Status**: ✅ done

Traceability verified:
- AC-7 (US) → AC-7/8/9 (DUTIES REQ) → Duty #4 (DUTIES SPEC) → complete
- AC-7 (US) → AC-7 (WORKFLOW REQ) → Step #4 (WORKFLOW SPEC) → complete
- SOUL: unchanged at all three levels (no traceability gap)
- Install vs. update distinction: already present in specs, `tools:` logic added cleanly on top
- Selective merge (update) vs. full copy (fresh install / new agent): covered at all levels
- User notification: covered at US AC-7, REQ DUTIES AC-9, SPEC DUTIES Duty #4 and WORKFLOW Step #4

### Traceability Verification

| Chain | Status |
|-------|--------|
| SYSP_US_SETUP → SYSP_REQ_SETUP_DUTIES → SYSP_SPEC_SETUP_DUTIES | ⏳ |
| SYSP_US_SETUP → SYSP_REQ_SETUP_WORKFLOW → SYSP_SPEC_SETUP_WORKFLOW | ⏳ |

---

## Sign-off

- [ ] Design approved by user
- [ ] Implementation complete
- [ ] Verify passed
- [ ] PM approval received
- [ ] Merged to development
