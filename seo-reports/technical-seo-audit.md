# Technical SEO Audit Report

**Audit Date:** 2026-11-27  
**Branch:** `seo-optimization`  
**Live Domain Tested:** `https://www.preet-baxi.com`  
**Hosting Architecture:** GitHub Pages with custom domain (`CNAME`: `www.preet-baxi.com`)

---

## 1. Domain Variant, HTTPS & Redirect Audit (Live Verified)

All 5 domain variants were tested with `curl -sS -I`:

| Variant URL | HTTP Status | Redirect Target | Hop Count | Verdict |
|---|---|---|---|---|
| `http://preet-baxi.com` | `301 Moved Permanently` | `https://www.preet-baxi.com/` | 1 | PASS |
| `https://preet-baxi.com` | `301` (HTTP/2) | `https://www.preet-baxi.com/` | 1 | PASS |
| `http://www.preet-baxi.com` | `301 Moved Permanently` | `https://www.preet-baxi.com/` | 1 | PASS |
| `https://preetb1199.github.io` | `301` (HTTP/2) | `https://www.preet-baxi.com/` | 1 | PASS |
| `https://www.preet-baxi.com/` | `200 OK` (HTTP/2) | Canonical destination | 0 | PASS |

All 12 intended public pages plus `robots.txt` and `sitemap.xml` returned `HTTP/2 200` with TTFB between `0.067s` and `0.129s`.

---

## 2. Critical Technical Issues Found & Fixed on `seo-optimization`

| Severity | Finding (Before) | Root Cause | Fix Implemented (After) |
|---|---|---|---|
| **High** | **Duplicate `index.html` vs directory URL internal links** across all 12 pages (`href="index.html"`, `href="../index.html"`, `href="research/index.html"`). Both `/index.html` and `/` return `HTTP 200` on GitHub Pages. | Relative links explicitly referenced `index.html`, conflicting with `<link rel="canonical">` (`/` and `/research/`) and `sitemap.xml`. | Rewrote all internal links across all 12 pages to clean canonical root-relative URLs (`/`, `/research/`, `/publications.html`, `/#about`, `/#contact`). |
| **High** | **Homepage Mobile LCP = 11.5s (Performance score 75)** | `index.html` served `assets/portrait-high-resolution.png` (2,097 KB PNG) directly in the hero `<img>`. | Generated `assets/portrait-560.webp` (32 KB, 2× retina for 288 px display) and wrapped hero portrait in `<picture>` with responsive `srcset` (`portrait-560.webp 560w, portrait.webp 1122w`) and original PNG fallback. |
| **High** | **8 missing `alt` attributes and `width`/`height`** on `research/index.html` thumbnails | `<img alt="" loading="lazy" src="../assets/thumbs/*.webp"/>` | Added descriptive research-specific `alt` text, `width="950" height="535"`, and `decoding="async"` to all 8 thumbnails. |
| **High** | **Heavy 2.1–2.6 MB PNG diagrams** on 7 research pages (`19.0 MB` combined) without `width`/`height` | Direct PNG embeds without modern WebP format or intrinsic dimensions. | Generated lossless-quality WebP versions (`1.55 MB` combined — **91.8% smaller**), served via `<picture>` with full PNG preserved at original URLs and explicit `width="1672" height="941"`. |
| **High** | **`publications.html` boilerplate meta description** (`"Research portfolio of Preet Baxi..."`) caused cannibalization on branded AI Safety & Research queries and prevented ranking for `"Preet Baxi Publications"`. | Reused homepage-like copy without paper titles, venues, DOIs, or BibTeX. | Rewrote title & meta description, added full author lists, verified DOIs, arXiv links, GitHub code link, abstracts, BibTeX `<details>`, and `ScholarlyArticle` JSON-LD. |
| **Medium** | **Unpublished portfolio project (`metaaudit.html`) labeled `ScholarlyArticle`** in JSON-LD | Misclassified Schema.org type. | Corrected to `TechArticle` in a unified `@graph`, reserving `ScholarlyArticle` strictly for verified peer-reviewed papers (ACL 2026, CQG 2026, PRD 2021). |
| **Medium** | **Leftover draft text in 5 `<figcaption>` elements** (`"Verify any diagram-specific chart values before public publication."`) | Pre-launch reminder left in production HTML. | Replaced with accurate, descriptive research captions on `prompt-injection-screening.html`, `gaming-the-gatekeeper.html`, `rai-gate.html`, `opsagent-rl.html`, and `cost-aware-llm-judges.html`. |
| **Medium** | **Short, under-descriptive page titles** (`RAI-Gate | Preet Baxi` 21 chars; `OpsAgent-RL | Preet Baxi` 24 chars; `LIGO Signal Validation | Preet Baxi` 35 chars) and missing `<meta name="robots">` on 8 pages. | Minimal template head tags on non-flagship pages. | Crafted unique, research-specific `<title>`, `<meta name="description">`, `<meta name="author">`, `<meta name="robots" content="index,follow,max-image-preview:large">`, and full OG/Twitter tags across all 12 pages. |
| **Medium** | **Weak topic-cluster internal linking & missing breadcrumbs on `research/index.html`** | `prompt-injection-screening.html` didn't link to `gaming-the-gatekeeper.html` or its GitHub repo; `cost-aware-llm-judges.html` didn't link to its preprint listing; `research/index.html` lacked breadcrumb markup. | Added breadcrumbs to `research/index.html` and aligned related-work grids across all 5 research clusters. |
| **Low** | **Accessibility mismatch on `agentsentry.html`** (`label-content-name-mismatch` on `Enlarge diagram` button) & empty leftover `<div class="ae-data-table ae-table-wrap"></div>` on `cora.html`. | `aria-label="Enlarge architecture diagram"` did not contain visible label `"Enlarge diagram"`. | Updated `aria-label="Enlarge diagram of AgentSentry architecture"` and removed empty div on `cora.html`. |
| **Low** | **`sitemap.xml` lacked `<lastmod>` and `<image:image>` entries** | Minimal flat XML sitemap. | Upgraded `sitemap.xml` with `2026-11-27` `<lastmod>` dates and 19 Google Image Sitemap entries across portrait and primary figures. |

---

## 3. Verification of Crawlability & Rendering Integrity

- **Zero accidental `noindex` directives** across all 12 pages.
- **Zero broken local links or broken asset references** (verified by `scripts/seo_audit.py`).
- **Zero orphan pages**: every intended public page receives multiple internal crawlable HTML links.
- **JavaScript crawlability**: all core research prose, abstracts, tables, methods, and limitations are present in initial server-rendered HTML (no client-side API fetching or JS-only text walls). Interactive tab panels keep their content in the DOM (progressive enhancement).
- **`googleb0a732b0b1e2e027.html`**: preserved intact at repo root for Google Search Console ownership verification and properly excluded from `sitemap.xml`.
- **Root `styles.css` note**: An unused legacy copy `styles.css` exists at the repository root (all 12 pages load `assets/styles.css`). Preserved untouched to avoid unintended breakage; can be removed in a future cleanup if confirmed unused externally.
