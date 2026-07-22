# Queued CR Draft: dark-mode-css-fix

**GH Issue**: #36
**Status**: queued (not yet branched)
**Proposed Operation Mode**: N/A — this is an Infrastructure Change per PM tailoring
(PM implements directly on a feature branch, QM still reviews, no CM involvement)

---

## Summary (draft)

In the rendered HTML documentation, sphinx-needs elements (`.. story::`, `.. req::`, `.. spec::` directives) render with a light background and light-gray text when the `furo` theme is in dark mode. Need metadata (title, status, tags, links) is effectively unreadable. Root cause: `sphinx_needs` default need styling uses fixed light-mode colors; no custom CSS in `docs/_static/` overrides this for dark mode.

Motivation: pure documentation-readability bug, no spec/architecture implications — a CSS-only fix.

Acceptance criteria: need panels (story/req/spec) are readable in both light and dark mode; colors follow furo's CSS variables (`--color-background-primary`, `--color-foreground-primary`, etc.), not hardcoded values. Add a custom CSS file under `docs/_static/`, register via `html_css_files` in `conf.py`.

---

## Next steps once branch is safe to create (per Infrastructure Change tailoring)

1. `git checkout experimental && git pull && git checkout -b feature/dark-mode-css`
2. PM implements directly (CSS file + conf.py registration) — no CM involvement
3. Lightweight change document (L0-L2 sections marked "N/A — infrastructure change")
4. QM review still performed
5. PM merges to `experimental` after QM sign-off
