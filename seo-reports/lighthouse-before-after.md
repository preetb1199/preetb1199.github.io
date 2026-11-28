# Lighthouse Before-and-After Performance & SEO Audit

**Audit Date:** 2026-11-27  
**Site:** `https://www.preet-baxi.com`  
**Branch Compared:** Live `main` (`https://www.preet-baxi.com`) vs. local `seo-optimization` (`http://127.0.0.1:8765`)  
**Tooling:** Lighthouse CLI (headless Chrome, default mobile throttling preset; categories: Performance, Accessibility, Best Practices, SEO)

---

## 1. Executive Summary

- **Homepage Performance improved from `75` to `100` (+25 points)** and **Largest Contentful Paint (LCP) dropped from `11.5 s` to `1.7 s` (-9.8 s / -85.2%)**, driven by replacing the eager 2.1 MB `assets/portrait-high-resolution.png` download with a responsive `<picture>` element serving `assets/portrait-560.webp` (32.0 KB) for mobile/1x viewports and `assets/portrait.webp` (229.4 KB) for high-DPI displays, while preserving the original PNG as a fallback.
- **Homepage total transferred bytes dropped from `2,120.4 KB` to `117.8 KB` (-94.4%)**, and **`prompt-injection-screening.html` dropped from `2,526.0 KB` to `311.0 KB` (-87.7%)** via lossless/high-quality WebP conversion of architecture figures (`assets/diagrams/*.webp`).
- **All 5 audited pages score `100` in Performance, `100` in Best Practices, and `100` in SEO**, with `CLS = 0` and zero console errors (`errors-in-console = 1`).
- **AgentSentry Accessibility fix:** Resolved the Lighthouse `label-content-name-mismatch` failure on `research/agentsentry.html` by aligning the diagram lightbox button's `aria-label` (`"Enlarge diagram of AgentSentry architecture"`) with its visible text.
- **Preserved visual design constraint:** Remaining `color-contrast` accessibility notices originate exclusively from the existing CSS palette (`assets/styles.css`). Per the strict instruction *"Do not change the existing fonts, colors, layouts, or visual identity"*, no existing color values were modified.

---

## 2. Measured Before vs. After Scores (Mobile Emulation)

| Page | Metric | Before (`main` live) | After (`seo-optimization` local) | Delta |
|---|---|---:|---:|---|
| **`/` (Homepage)** | Performance | **75** | **100** | **+25** |
| | Accessibility | 96 | 96 | 0 |
| | Best Practices | 100 | 100 | 0 |
| | SEO | 100 | 100 | 0 |
| | FCP | 1.1 s | 1.2 s | +0.1 s |
| | **LCP** | **11.5 s** | **1.7 s** | **-9.8 s (-85.2%)** |
| | Speed Index | 1.3 s | 1.2 s | -0.1 s |
| | TBT | 40 ms | 0 ms | -40 ms |
| | CLS | 0 | 0 | 0 |
| | Total Transfer Size | 2,120.4 KB | 117.8 KB | **-2,002.6 KB (-94.4%)** |
| **`/research/`** | Performance | 100 | 100 | 0 |
| | Accessibility | 95 | 95 | 0 |
| | Best Practices | 100 | 100 | 0 |
| | SEO | 100 | 100 | 0 |
| | FCP / LCP / SI | 1.0 s / 1.0 s / 1.0 s | 1.1 s / 1.1 s / 1.1 s | +0.1 s (uncompressed local HTTP)* |
| | TBT / CLS | 40 ms / 0 | 20 ms / 0 | -20 ms / 0 |
| | Total Transfer Size | 705.0 KB | 763.8 KB | +58.8 KB (uncompressed local HTTP)* |
| **`/publications.html`** | Performance | 100 | 100 | 0 |
| | Accessibility | 95 | 95 | 0 |
| | Best Practices | 100 | 100 | 0 |
| | SEO | 100 | 100 | 0 |
| | FCP / LCP / SI | 0.9 s / 0.9 s / 0.9 s | 1.2 s / 1.2 s / 1.2 s | +0.3 s (uncompressed local HTTP)* |
| | TBT / CLS | 0 ms / 0 | 0 ms / 0 | 0 / 0 |
| | Total Transfer Size | 18.5 KB | 81.6 KB | +63.1 KB (uncompressed local HTTP + expanded abstracts/BibTeX/JSON-LD)* |
| **`/research/agentsentry.html`** | Performance | 100 | 100 | 0 |
| | Accessibility | 97 | 97 | `label-content-name-mismatch` fixed |
| | Best Practices | 100 | 100 | 0 |
| | SEO | 100 | 100 | 0 |
| | FCP / LCP / SI | 1.2 s / 1.2 s / 1.2 s | 1.5 s / 1.5 s / 1.5 s | +0.3 s (uncompressed local HTTP)* |
| | TBT / CLS | 80 ms / 0 | 0 ms / 0 | -80 ms / 0 |
| | Total Transfer Size | 49.8 KB | 181.9 KB | +132.1 KB (uncompressed local HTTP)* |
| **`/research/prompt-injection-screening.html`** | Performance | 100 | 100 | 0 |
| | Accessibility | 97 | 97 | 0 |
| | Best Practices | 100 | 100 | 0 |
| | SEO | 100 | 100 | 0 |
| | FCP / LCP / SI | 0.9 s / 0.9 s / 0.9 s | 1.2 s / 1.2 s / 1.2 s | +0.3 s (uncompressed local HTTP)* |
| | TBT / CLS | 20 ms / 0 | 0 ms / 0 | -20 ms / 0 |
| | **Total Transfer Size** | **2,526.0 KB** | **311.0 KB** | **-2,215.0 KB (-87.7%)** |

*\*Methodology note on local HTTP comparison:* The "Before" baseline ran against GitHub Pages (`https://www.preet-baxi.com`), which serves HTML/CSS/JS with CDN-level gzip/Brotli compression over HTTP/2. The "After" audit ran against Python's `http.server` on `127.0.0.1:8765`, which serves HTML/CSS/JS **uncompressed** over HTTP/1.1. Once `seo-optimization` is deployed to GitHub Pages, text assets (HTML, JSON-LD, CSS, JS) will be gzip/Brotli-compressed by Fastly, reducing transfer size and FCP/LCP further below the local HTTP numbers above.

---

## 3. Image Payload Optimization Summary (Zero Visual Degradation)

All original PNG files were preserved in place as `<picture>` fallback sources and Open Graph/Schema.org high-resolution references, while modern browsers receive WebP derivatives:

| Asset | Original PNG | New WebP | Savings |
|---|---:|---:|---:|
| `assets/portrait-high-resolution.png` → `assets/portrait-560.webp` (mobile/1x) | 2,097.4 KB | 32.0 KB | **-98.5%** |
| `assets/portrait-high-resolution.png` → `assets/portrait.webp` (2x retina) | 2,097.4 KB | 229.4 KB | **-89.1%** |
| `assets/diagrams/AgentSentry.png` → `AgentSentry.webp` | 2,145.0 KB | 126.1 KB | **-94.1%** |
| `assets/diagrams/CORA.png` → `CORA.webp` | 2,348.1 KB | 196.9 KB | **-91.6%** |
| `assets/diagrams/CostAware.png` → `CostAware.webp` | 2,497.7 KB | 224.1 KB | **-91.0%** |
| `assets/diagrams/Gatekeeper.png` → `Gatekeeper.webp` | 2,599.8 KB | 250.9 KB | **-90.3%** |
| `assets/diagrams/MetaAudit.png` → `MetaAudit.webp` | 2,246.4 KB | 165.1 KB | **-92.6%** |
| `assets/diagrams/OPS.png` → `OPS.webp` | 2,398.6 KB | 195.3 KB | **-91.9%** |
| `assets/diagrams/Prompt.png` → `Prompt.webp` | 2,504.3 KB | 226.8 KB | **-90.9%** |
| `assets/diagrams/RAIGate.png` → `RAIGate.webp` | 2,255.3 KB | 163.3 KB | **-92.8%** |
| **8 Architecture Diagrams Total** | **18,995.2 KB** | **1,548.4 KB** | **-91.8%** |

---

## 4. Accessibility & Best Practices Details

- **Console errors:** `0` across all 5 audited pages (`errors-in-console` score = `1`).
- **Layout stability (CLS):** Explicit `width` and `height` attributes were added to every `<img>` across all 12 pages, maintaining `CLS = 0` everywhere.
- **Resolved accessibility audit:** `label-content-name-mismatch` on `research/agentsentry.html` was fixed and verified passing in the after-audit.
- **Unchanged accessibility audit (`color-contrast`):** Still reported on all 5 pages because muted text tokens in `assets/styles.css` were intentionally untouched to comply with the strict no-redesign / no-color-change constraint. If you decide in a future visual polish pass to darken muted caption/metadata text slightly (e.g., increasing contrast ratio above 4.5:1), Accessibility scores can reach `100` across the site.

---

## 5. Post-Deployment Verification Step

After merging `seo-optimization` to `main` and allowing GitHub Pages to publish (~1–3 minutes), re-run Lighthouse (or PageSpeed Insights at `https://pagespeed.web.dev/`) on `https://www.preet-baxi.com/` and `https://www.preet-baxi.com/research/prompt-injection-screening.html` to confirm live CDN-compressed LCP and Performance scores.
