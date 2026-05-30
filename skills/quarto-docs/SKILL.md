---
name: quarto-docs
description: Navigate the Quarto documentation efficiently when working on a Quarto-based publishing site. Use this skill whenever a task involves Quarto — including `_quarto.yml`, navbars, sidebars, listings, themes, format options, citations, freeze, partial render. Quarto publishes LLM-optimized markdown bundles at quarto.org/llms.txt and per-page `.llms.md` URLs; this skill teaches which page to fetch and how to navigate so agents don't hallucinate YAML keys, nest options under the wrong parent (`format.html.sidebar` is wrong — `sidebar` is top-level under `website`), or guess at listing-type/theme-extension semantics. Trigger whenever the user mentions Quarto, qmd, _quarto.yml, listings, navbar, sidebar, cosmo, brand, theme, freeze, render, or page-navigation.
metadata:
  type: documentation
  vendoring: custom
---

# quarto-docs

Quarto's docs evolve fast, and the YAML option surface is large enough that guessing wrong wastes a render cycle (or worse, a CI run). The naive failure modes when agents work with Quarto are:

1. **Hallucinating YAML keys** — guessing `format.html.sidebar` when sidebars are a top-level `website.sidebar` block, or guessing `categories-filter: true` when the listing key is `categories: true`.
2. **Nesting at the wrong scope** — confusing project-level config (`project.*`), website-level config (`website.*`), format-level config (`format.html.*`), and per-page frontmatter. Each accepts different keys.
3. **Going stale on versioning** — using a YAML option that changed shape between Quarto 1.4 and 1.9 (e.g., listings categories filter behavior; brand support).
4. **Reaching for plugins when a built-in works** — Quarto has built-in listings, search, navigation, themes, citations, and cross-references. Custom Lua filters or shortcodes are rarely the first answer.

This skill exists to make each of those the obvious failure to avoid. The core move is: **fetch the relevant `.llms.md` page directly, read the option table, then write the YAML.**

## The `.llms.md` URL pattern

Quarto publishes a markdown-optimized version of every doc page. Use these patterns:

| URL | What's in it | When to fetch |
| --- | --- | --- |
| `https://quarto.org/llms.txt` | **Index manifest** — lists every doc page with its URL. | First stop when you don't know the topic. Tiny; always safe. |
| `https://quarto.org/docs/{section}/{page}.llms.md` | LLM-optimized markdown for a guide page. | Conceptual / narrative how-to. |
| `https://quarto.org/docs/reference/{area}/{page}.llms.md` | LLM-optimized YAML option reference. | When you need the exact option name, default value, or nesting. |

URL transformation: take any `quarto.org/docs/...html` page and swap `.html` for `.llms.md`. The same page renders as cleaner markdown with `[TABLE]` placeholders for the option tables (the actual tables follow in markdown form).

If a `.llms.md` URL 404s (it happens on a few index pages), fetch the `.html` page — Quarto's HTML extracts cleanly through WebFetch.

## The four scopes (and which keys live in which)

This is the most common source of failed renders. Quarto's YAML has four nesting scopes, each with its own key surface:

| Scope | YAML location | What lives here |
| --- | --- | --- |
| **Project** | `project: ...` at the top of `_quarto.yml` | `type`, `output-dir`, `render`, `resources`, `preview`, `pre-render`, `post-render`, `profile`. Project-shape and lifecycle. |
| **Website** | `website: ...` at the top of `_quarto.yml` (only when `project.type: website`) | `title`, `site-url`, `description`, `navbar`, `sidebar`, `page-navigation`, `back-to-top-navigation`, `bread-crumbs`, `reader-mode`, `search`, `open-graph`, `twitter-card`, `cookie-consent`, `comments`, `repo-url`, `repo-actions`. **Most "site-wide UX" options live here, not under `format.html`.** |
| **Format** | `format.{html,pdf,typst,...}: ...` at top of `_quarto.yml` or per-page | `theme`, `css`, `toc`, `toc-depth`, `code-copy`, `code-overflow`, `fontsize`, `linestretch`, `grid`, `embed-resources`, `output-file`. Per-output rendering. |
| **Page frontmatter** | At the top of a `.qmd` file between `---` markers | `title`, `subtitle`, `author`, `date`, `description`, `categories`, `format`, **`sidebar: <id>`** (to bind a page to a specific sidebar by id), `image`, `license`, `draft`. Per-document overrides. |

The single most common confused-nesting bug: putting `sidebar:` under `format.html.*`. It belongs under `website.*`. Same for `navbar`, `page-navigation`, `bread-crumbs`.

## The website pages you'll fetch most often

For VADE's publishing-site work, these are the doc pages worth memorizing:

| URL | Covers |
| --- | --- |
| `quarto.org/docs/reference/projects/websites.llms.md` | **The authoritative option list** for `project.*`, `website.*`, `navbar.*`, `sidebar.*`. The single most useful page; bookmark mentally. |
| `quarto.org/docs/websites/website-navigation.llms.md` | Narrative guide on navbar + sidebar patterns, including the hybrid "navbar + per-section sidebar" model. |
| `quarto.org/docs/websites/website-listings.llms.md` | Listings system: types (`default`, `grid`, `table`), fields, categories filter, feed generation. |
| `quarto.org/docs/websites/website-search.llms.md` | Search configuration: `location`, `type`, `show-item-context`. |
| `quarto.org/docs/websites/website-tools.llms.md` | Reader mode, code links, repo actions, social previews, dark/light theme toggle. |
| `quarto.org/docs/reference/formats/html.llms.md` | The full `format.html` surface: theme, layout, typography, code rendering, grid. |
| `quarto.org/docs/projects/quarto-projects.llms.md` | Project mechanics: pre/post-render hooks, profiles, `_metadata.yml` (per-directory config merging), resources. |
| `quarto.org/docs/output-formats/html-themes.llms.md` | Theme application: bootswatch themes, SCSS extension (`theme: [cosmo, custom.scss]`), light/dark pairing. |

## Decision tree for common questions

**"How do I add a navbar dropdown / nested menu?"**
→ `quarto.org/docs/reference/projects/websites.llms.md` (search "menu"). Each `navbar.left` / `navbar.right` entry can have `menu: [...]` instead of `href:`.

**"How do I get a sidebar to appear on some pages but not others?"**
→ `quarto.org/docs/websites/website-navigation.llms.md` §Side Navigation. Multiple `sidebar:` blocks under `website:`, each with an `id:`; bind a page to one via `sidebar: <id>` in frontmatter. **Quarto does NOT auto-assign sidebars by directory — the assignment is explicit.**

**"Which listing type should I use — default, grid, or table?"**
→ `quarto.org/docs/websites/website-listings.llms.md` §Listing Types. `default` for blog-style date-sorted prose, `grid` for image-led card layouts (small set), `table` for dense dated rows.

**"What goes in `_metadata.yml`?"**
→ `quarto.org/docs/projects/quarto-projects.llms.md` §Directory Metadata. Per-directory file that merges (not replaces) project config; useful for per-section listing config without bloating root `_quarto.yml`.

**"How do I extend the Bootstrap theme with custom SCSS / CSS?"**
→ `quarto.org/docs/output-formats/html-themes.llms.md`. `theme: [cosmo, custom.scss]` for SCSS extension; `css: custom.css` for plain CSS. Plain CSS is staged into the build dir; SCSS goes through Quarto's theme compiler.

**"Why isn't my freeze cache working / why does CI re-render everything?"**
→ `quarto.org/docs/projects/code-execution.llms.md` §Freeze. `execute.freeze: auto` (project-level) skips re-execution when source is unchanged; the `_freeze/` cache is gitignored by default but checked into the build harness via the partial-render path.

**"Where do I configure the page-bottom prev/next links?"**
→ `website.page-navigation: true`. Top-level under `website:`.

**"I don't know the right topic / option name."**
→ `https://quarto.org/llms.txt` (the index). It's small and lists every doc page by name.

## VADE-specific context

This skill is used heavily inside `vade-coo-memory` for the publishing site at **https://read.vade-app.dev**. A few things worth knowing when doing Quarto work here:

- **Current Quarto version: 1.9.37.** Pinned by the CI workflow and by `vade-runtime/scripts/lib/common.sh::ensure_quarto_cli`. Local Macs typically have a similar or newer 1.9.x via brew.
- **Authoritative config lives in `bin/publish-site/build.py` as `QUARTO_BASE_CONFIG`** (~line 61). It's a Python dict that's dumped to `_quarto.yml` per build via `yaml.safe_dump`. **Edit there, not in a static `_quarto.yml` file** — there is no checked-in `_quarto.yml`; it's generated each render.
- **Build harness agent doc: `bin/publish-site/CLAUDE.md`.** Read it before any non-trivial harness change. Covers the stage → frontmatter → preprocess → render → verify pipeline.
- **Source-substrate paths get normalized at stage time:** `.md` → `.qmd`, `README.qmd` → `index.qmd`, body-level `---` → `***` (to avoid Pandoc YAML metadata-block misparsing). Don't fight these; they're load-bearing.
- **Pre-processor handles raw-text refs the Lua filter can't:** memos, public/private `<repo>#N`, bare `<filename>.md`. Source at `bin/publish-site/preprocess.py`. The Lua filter (`reference-rewriter.lua`) handles AST-level Link substitution.
- **PDF render via typst, not LaTeX.** Faster, no tinytex install, ships with Quarto. Each content page emits both HTML and a typst PDF; listings/landing opt out via per-page `format: html: default`.
- **CSS additions** are staged into the build dir alongside the Lua filter; wire via `format.html.css: "quarto-overrides.css"` and a `shutil.copy2` in `build.py`'s render-prep block. Example landed in commit `c8d8eb0` (hiding the title-block description duplicate).
- **`from: markdown-citations`** is set project-wide. This disables Pandoc's citation extension so `@mention` strings in transcripts (e.g. `@vade-coo`) render as plain text, not citation tokens. Don't enable citations without understanding this trade-off.
- **Partial render is wired** (`bin/publish-site/diff_scope.py`). Single-file content PRs render only the touched page + listing dependencies. Cardinality changes (add / delete / rename) escalate to full render. Theme / CSS / Lua / template changes automatically escalate because `bin/publish-site/**` is in the full-render trigger set.
- **Sidebars need explicit per-page frontmatter assignment.** Quarto does NOT infer from directory. If you add sidebars, extend `build.py`'s frontmatter-merge step (`inject_frontmatter()`) to set `sidebar: <id>` based on the staged page's projected path prefix. Add a test in `test_build.py`.

## Working efficiently

**Fetch the reference first, the guide second.** Reference pages (`quarto.org/docs/reference/...`) give you the exact option name + nesting + default. Guide pages (`quarto.org/docs/websites/...`, `quarto.org/docs/projects/...`) explain the *model* — when to use a feature, what trade-offs it carries. Reference is what you write into YAML; guide is what helps you decide whether to write it at all.

**Avoid `llms-full` / mega-bundles.** Quarto's per-page `.llms.md` files are small — usually a few hundred lines. Fetching one page is almost always cheaper than pulling everything.

**Don't trust pre-trained knowledge for YAML keys.** Quarto's option names have shifted across 1.x versions. Always confirm a key exists at our pinned version by reading the reference page, not by memory.

**When in doubt, render locally first.** `python3 bin/publish-site/build.py --tier-filter T1 --substrate-capture-probe live --build-dir /tmp/vbuild --out /tmp/vsite --force-full-render` produces a full render in ~2 minutes. Cheaper than a CI cycle. The `--skip-render` flag stops after frontmatter staging if all you need is to inspect the generated `_quarto.yml`.

**Anchor YAML changes to a render-verified snippet.** When proposing a new option, paste the YAML you wrote, the doc page you read it from, and a screenshot or grep of the rendered output. The PR template's test plan section is the right place.
