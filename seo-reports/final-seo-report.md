# Final Technical SEO, Academic Discoverability & Organic Growth Report

**Website:** `https://www.preet-baxi.com`  
**Repository:** `https://github.com/preetb1199/preetb1199.github.io`  
**Branch:** `seo-optimization` (awaiting user approval before merging to `main`)  
**Completion Date:** 2026-11-27

> **Transparency & Guarantees Notice:** No search engine rankings, indexing speed, sitelinks, or Google Knowledge Panels are guaranteed. All implemented improvements follow white-hat technical SEO, academic metadata, and web performance standards. No visual design elements (fonts, colors, layouts, or visual identity) were altered, no URLs were broken, and no credentials, publications, search volumes, or traffic figures were fabricated.

---

## 1. Mission Status Summary

### A. Completed and Verified (Code, Assets, Validation & Local Audits)
1. **Live HTTP, HTTPS, Redirect & Canonical Audit:** Verified all 5 domain variants (`http/https` apex, `http/https` www, `preetb1199.github.io`) resolve via single-hop `301` to `https://www.preet-baxi.com/` (`HTTP/2 200`), and all 12 canonical pages + `robots.txt` + `sitemap.xml` return `HTTP/2 200`.
2. **All 12 Canonical HTML Pages Optimized Independently (Zero Visual Redesign):**
   - Unique, descriptive `<title>` tags, meta descriptions, `robots` directives, self-referencing `<link rel="canonical">`, and complete Open Graph + Twitter Card metadata (with image dimensions and alt text) on all 12 pages.
   - Standardized all internal navigation and footer links to canonical root-relative paths (`/`, `/research/`, `/publications.html`, `/research/<slug>.html`) — eliminating internal links to `index.html`.
   - Removed leftover draft captions (`"Verify any diagram-specific chart values before public publication."`) on 5 project pages and an empty placeholder `<div>` on `cora.html`.
3. **Unified Machine-Readable Researcher Identity & Schema.org Markup:**
   - Implemented consistent `@id: "https://www.preet-baxi.com/#person"` across all 12 pages, linking University of Michigan affiliation, research areas, and 6 verified `sameAs` profiles (Google Scholar, GitHub, LinkedIn, U-M LSA Physics, U-M MICDE, ACL Anthology).
   - Used factually accurate schema types: `ProfilePage` + `WebSite` (`/`), `CollectionPage` + `ItemList` (`/research/`, `/publications.html`), `TechArticle` + `BreadcrumbList` + `ImageObject` (project pages), and `ScholarlyArticle` **strictly** for verified published papers (ACL 2026, CQG 2026, PRD 2021) — fixing `metaaudit.html` which had inaccurately used `ScholarlyArticle` for an unpublished working paper.
4. **Academic Publication Verification & Enriched Bibliographic Records:**
   - Verified every published paper against authoritative publisher/Crossref/ACL Anthology/arXiv records:
     - **Findings of ACL 2026** (`10.18653/v1/2026.findings-acl.142`, pp. 2942–2953, `arXiv:2606.27287`, GitHub `Prompt_Injection_ACL26`).
     - **Classical and Quantum Gravity 2026** (`10.1088/1361-6382/ae7adb`, Vol. 43(13) 135019, `arXiv:2601.09918`).
     - **Physical Review D 2021** (`10.1103/PhysRevD.104.084080`, Vol. 104(8) 084080, `arXiv:2103.03241`).
     - **2026 Preprint** (*"Sequential Sampling for Binary Classification: Two LLMs are (Almost) All You Need"*, accurately labeled as `CreativeWork` / under review).
   - Added verified abstracts, full co-author lists, DOIs, arXiv links, collapsible BibTeX entries, and bidirectional links between `index.html`, `publications.html`, `prompt-injection-screening.html`, `ligo-monitoring.html`, and `cost-aware-llm-judges.html`.
5. **Image Optimization & Google Images Discoverability:**
   - Generated responsive WebP portrait (`assets/portrait-560.webp`, 32.0 KB vs. 2,097.4 KB PNG = **-98.5%**) and WebP versions of all 8 architecture figures (`assets/diagrams/*.webp`, **18,995.2 KB → 1,548.4 KB = -91.8%**) while keeping all original PNGs intact.
   - Added descriptive `alt` text and explicit `width`/`height` dimensions to every image across all 12 pages (including all 8 previously empty `alt=""` thumbnails on `/research/`).
   - Upgraded `sitemap.xml` with `lastmod` (`2026-11-27`) and 19 `<image:image>` entries.
6. **Lighthouse Performance & Accessibility Verification:**
   - Homepage mobile Performance improved from **`75` → `100`**, LCP from **`11.5 s` → `1.7 s` (-85.2%)**, total transfer size from **`2,120.4 KB` → `117.8 KB` (-94.4%)**.
   - `prompt-injection-screening.html` total transfer size dropped from **`2,526.0 KB` → `311.0 KB` (-87.7%)**.
   - Fixed `label-content-name-mismatch` accessibility failure on `research/agentsentry.html`.
   - All 5 audited pages achieve `100` Performance, `100` Best Practices, `100` SEO, `CLS = 0`, and zero console errors.
7. **Automated SEO CI & Monitoring Tooling:**
   - Created `scripts/seo_audit.py` (passes with 0 errors / 0 warnings across all 12 pages), `.github/workflows/seo-check.yml`, and read-only `scripts/gsc_monitor.py`.

### B. Implemented Awaiting Deployment (Merge Approval Required)
- All edits live on branch `seo-optimization`. They are **not yet live** on `https://www.preet-baxi.com` until you review and merge `seo-optimization` into `main`.

### C. Submitted Awaiting Google Processing
- None yet (deferred until `seo-optimization` is merged to `main` and you submit `sitemap.xml` + URL Inspection requests in authenticated Google Search Console).

### D. Blocked by Authentication or Permissions
- Interactive Google Search Console inspection, sitemap resubmission, and manual Request Indexing (requires your Google account sign-in).
- Bing Webmaster Tools property import and sitemap submission.
- External profile updates (ORCID duplicate merge, U-M LSA Physics, U-M MICDE, Google Scholar interests, ResearchGate, LinkedIn, ACL Anthology, and GitHub profile/repo metadata).

### E. Remaining Manual Actions
- Consolidated step-by-step in [`seo-reports/remaining-manual-actions.md`](remaining-manual-actions.md).

---

## 2. Five Research Topic Clusters & Internal Linking Architecture

Every project page is now anchored into one of 5 semantically coherent topic clusters with bidirectional internal links across the homepage, `/research/`, `/publications.html`, and sibling project pages:

| # | Topic Cluster | Canonical Pages | Primary Technical Search Themes |
|---|---|---|---|
| **1** | **Agentic AI & Runtime Security** | `agentsentry.html`, `rai-gate.html` | Runtime security for AI agents, MCP tool-call enforcement, fail-closed policy enforcement, provenance taint tracking, prompt-injection defense at execution boundaries |
| **2** | **LLM Evaluation & Statistical Reliability** | `metaaudit.html`, `cost-aware-llm-judges.html`, `cora.html` | LLM-as-a-judge reliability, prediction-powered inference (PPI++), Edgeworth confidence intervals, adaptive LLM routing, adversarial judge robustness, sequential sampling |
| **3** | **Indirect Prompt Injection & Applied Safety** | `prompt-injection-screening.html`, `gaming-the-gatekeeper.html`, `publications.html#acl2026` | Indirect prompt injection in automated résumé screening, ACL 2026 Findings (`2026.findings-acl.142`), gatekeeper manipulation, screening system robustness |
| **4** | **Agentic Reinforcement Learning & Post-Training** | `opsagent-rl.html`, `rai-gate.html` | Reinforcement learning for tool-using AI agents, long-horizon operations agents, verifier-grounded post-training, safe exploration |
| **5** | **Gravitational-Wave Physics & Scientific Computing** | `ligo-monitoring.html`, `publications.html#cqg2026`, `publications.html#prd2021` | LIGO O4 continuous-wave hardware injections, gravitational-wave detector monitoring (`CQG 2026`), waveform modeling (`PRD 2021`), scientific computing |

**Assessment on New Cluster Overview Pages:** Creating 5 new standalone cluster hub pages right now is **not recommended**. With 9 total projects (1–3 pages per cluster), separate cluster landing pages would risk creating thin doorway/duplication overlap with `/research/` and `/publications.html`. Revisit creating dedicated cluster hubs only when a cluster reaches **4+ substantive published papers or technical deep dives**.

---

## 3. Search Competitor Analysis & Technical Content Gaps (Observed SERPs)

Based on live non-branded Google searches across all 5 clusters (no fabricated volume or difficulty metrics):

| Cluster | Observed Top Competitors | Key Content Gap & Realistic Opportunity for `preet-baxi.com` |
|---|---|---|
| **1. Runtime Agent Security** | Enterprise vendors (Sweet Security, Aperion, Aegis, EthicalHat), Substack security blogs, recent arXiv papers (`2512.23557`) | Vendor marketing pages lack reproducible empirical evaluation. **Opportunity:** `agentsentry.html` already includes concrete unseen-server false-alarm analysis (`0/120` vs `120/120`) and adaptive attack failure modes (v3 `payload_split`). Releasing a public preprint/code repo + technical failure-mode writeup will significantly strengthen non-branded authority. |
| **2. LLM-as-a-Judge & PPI** | Academic preprints on arXiv (`2606.05308` PRECISE, `2601.18777`, `2601.05420`, `2611.13186`, `2602.00521`) | arXiv abstracts are dense and static. **Opportunity:** `metaaudit.html` and `cora.html` combine interactive statistical explainers (PPI++ tuning, Edgeworth certification) with readable prose — strong differentiation for researchers searching how to debias LLM judges. |
| **3. Prompt Injection in Résumé Screening** | ACL Anthology (including your own `2026.findings-acl.142` and ACL Industry `2026.acl-industry.127` RAPIDS) and arXiv (`2608.25880`) | **High near-term opportunity:** As first author of a peer-reviewed ACL 2026 paper with a public GitHub repo (`Prompt_Injection_ACL26`), linking ACL Anthology, arXiv, GitHub, and `prompt-injection-screening.html` creates a strong canonical explainer hub for recruiters, AI safety engineers, and researchers. |
| **4. LIGO O4 CW Hardware Injections** | Almost exclusively raw arXiv (`2601.09918`) and paywalled IOPscience (`10.1088/1361-6382/ae7adb`) | **Highest immediate non-branded ranking opportunity:** Virtually no accessible web explainers exist for LIGO O4 continuous-wave hardware injection monitoring. Indexing `ligo-monitoring.html` (previously unobserved in baseline searches) can capture niche astrophysics & scientific-computing queries quickly. |
| **5. RL for Tool-Using Agents & Cost-Aware Judge Routing** | Competitive arXiv papers (`Pathwise-Budgeted LLM Routing`, `2611.05835`) and engineering blogs | Current project pages (`opsagent-rl.html`, `cost-aware-llm-judges.html`) are concise previews. **Opportunity:** Long-tail discoverability will grow once empirical benchmarks, preprints, or code artifacts are published and linked. |

---

## 4. Prioritized Long-Term Organic Search Growth Roadmap

| Horizon | Priority Actions | Expected Qualitative Outcome |
|---|---|---|
| **Days 1–30 (Foundation & Indexing)** | Merge `seo-optimization` → `main`; verify GSC Domain property; submit `sitemap.xml`; request indexing for all 12 pages (prioritizing the 4 previously unobserved pages); import site to Bing Webmaster Tools; merge duplicate ORCID records. | Clean index coverage across all 12 canonical pages, improved mobile LCP on `/`, unified entity graph, and clean Rich Results validation. |
| **Days 31–60 (Entity & `.edu` Authority)** | Update U-M LSA Physics, U-M MICDE, Google Scholar interests, ResearchGate, LinkedIn, and GitHub profile/repo metadata (`Prompt_Injection_ACL26`, `preetb1199.github.io`, `CalculateSNRg_Python`). Run first `gsc_monitor.py` snapshot. | Stronger `.edu` and academic profile signal consolidation; higher branded CTR and stronger researcher entity recognition. |
| **Days 61–90 (High-Intent Technical Content)** | Add brief, concrete methodology/benchmark FAQ or "Reproducibility & Code" sections to `prompt-injection-screening.html` and `ligo-monitoring.html` based on early GSC query impressions; link any newly released arXiv preprints (e.g., AgentSentry, MetaAudit, CORA, `arXiv:2603.04792`) with accurate `ScholarlyArticle` markup once live. | Expanded non-branded long-tail impressions across ACL prompt injection, LIGO O4 monitoring, and LLM-as-a-judge evaluation. |
| **Days 91–180 (Open Artifacts & Scholarly Citations)** | Release reproducible code/benchmarks with Zenodo DOIs linked to your consolidated ORCID and `/research/<project>.html` pages; cross-link conference talk slides/posters to project pages; audit GSC positions 8–25 for title/heading refinement. | Natural scholarly backlinks from GitHub, Zenodo, conference sites, and citing researchers. |
| **Days 181–365 (Sustained Topical Authority)** | Review 6-month and 12-month branded vs. non-branded query trajectories via `scripts/gsc_monitor.py`; evaluate adding a dedicated cluster hub only if a research area expands to 4+ published papers; keep `publications.html` and `sitemap.xml` synchronized as new papers publish. | Durable organic visibility among AI safety researchers, academic collaborators, conference organizers, and research-lab hiring teams. |

---

## 5. Complete Deliverables Index (`seo-reports/`)

1. [`baseline-search-visibility.md`](baseline-search-visibility.md) — Phase 1 baseline Google SERP, image, and publication visibility audit
2. [`technical-seo-audit.md`](technical-seo-audit.md) — Phase 4 HTTP/HTTPS, redirect, canonical, link, asset, and crawlability audit
3. [`indexing-status.csv`](indexing-status.csv) — Page-by-page status, baseline observation, and GSC priority tracker for all 12 canonical URLs
4. [`keyword-page-mapping.csv`](keyword-page-mapping.csv) — 5-cluster research terminology and intent mapping across all 12 pages
5. [`structured-data-report.md`](structured-data-report.md) — Phase 6 Schema.org architecture, `@id` graph, and validation audit
6. [`academic-publication-audit.md`](academic-publication-audit.md) — Phase 7 verified bibliographic records, Google Scholar eligibility, and ORCID duplication findings
7. [`external-profile-optimization.md`](external-profile-optimization.md) — External academic profile audit, copy-paste bios, and white-hat backlink plan
8. [`lighthouse-before-after.md`](lighthouse-before-after.md) — Phase 12 exact measured before-vs-after Lighthouse performance, LCP, byte savings, and accessibility report
9. [`google-search-console-report.md`](google-search-console-report.md) — Phase 2/3/13 GSC & Bing setup guide, URL inspection plan, and 30–365 day monitoring framework
10. [`remaining-manual-actions.md`](remaining-manual-actions.md) — Prioritized checklist of approval- and auth-gated actions
11. [`final-seo-report.md`](final-seo-report.md) — This executive summary, competitor analysis, topic cluster plan, and organic growth roadmap
