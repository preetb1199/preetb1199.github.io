# Google Search Console, Bing Webmaster Tools & Monitoring Report

**Report Date:** 2026-11-27  
**Site:** `https://www.preet-baxi.com`  
**Verification File Present in Repo & Live:** `https://www.preet-baxi.com/googleb0a732b0b1e2e027.html` (verified `HTTP/2 200`)

---

## 1. Execution Status & Authentication Boundary

**Status: Blocked by authentication (interactive Google/Bing account sign-in required).**

Because this environment does not have an authenticated interactive Google account session or browser access to your personal Search Console account:
- No Search Console settings, sitemaps, or URL inspection requests were modified or submitted automatically.
- No Bing Webmaster Tools actions were executed automatically.
- **No claims of indexing or submission completion are made.**

However, technical inspection of the repository and live site confirmed:
1. A Google HTML verification file (`googleb0a732b0b1e2e027.html`) is already committed in the repository root and returns `HTTP/2 200` on `https://www.preet-baxi.com/googleb0a732b0b1e2e027.html`. This strongly indicates a URL-prefix property for `https://www.preet-baxi.com/` was previously verified (verify ownership is still active under your Google account).
2. `robots.txt` (`https://www.preet-baxi.com/robots.txt`) returns `HTTP/2 200`, permits all crawlers (`Allow: /`), and declares `Sitemap: https://www.preet-baxi.com/sitemap.xml`.
3. `sitemap.xml` on branch `seo-optimization` has been upgraded with all 12 canonical URLs, accurate `lastmod` (`2026-11-27`), and 19 `<image:image>` entries (using the `http://www.google.com/schemas/sitemap-image/1.1` namespace).

---

## 2. Step-by-Step Google Search Console Setup & Baseline Capture

Perform these steps **immediately after merging `seo-optimization` to `main`** (and waiting ~3 minutes for GitHub Pages deployment):

### Step A: Verify Property Coverage
1. Open `https://search.google.com/search-console`.
2. Confirm whether both properties exist:
   - **URL-prefix property:** `https://www.preet-baxi.com/` (already backed by `googleb0a732b0b1e2e027.html`).
   - **Domain property (recommended addition):** `preet-baxi.com` — covers `http/https` and apex/www variants together and shows redirect/canonical consolidation issues.
     - *If not yet added:* Click **Add property → Domain**, enter `preet-baxi.com`, copy the `google-site-verification=...` TXT record, and add it to your domain registrar's DNS zone. (Wait 5–15 minutes, then click **Verify**.) Do NOT remove existing `A` / `CNAME` records for GitHub Pages.

### Step B: Record Baseline GSC Exports (Before Resubmission)
Before submitting new requests, capture screenshots or CSV exports from:
1. **Indexing → Pages:** Note total *Indexed* vs. *Not indexed* counts, plus every exclusion reason (`Discovered - currently not indexed`, `Crawled - currently not indexed`, `Duplicate without user-selected canonical`, `Alternate page with proper canonical tag`, `Page with redirect`).
2. **Search results → Performance:** Export the last 3 months and 16 months of **Queries** and **Pages** (Clicks, Impressions, CTR, Average Position).
3. **Security & Manual Actions:** Confirm `No issues detected` in both tabs.
4. **Core Web Vitals & HTTPS:** Confirm `HTTPS` is green and record any Mobile/Desktop LCP warnings (expected to improve on `/` after the portrait WebP optimization deploys).

### Step C: Resubmit Updated Sitemap
1. Go to **Indexing → Sitemaps**.
2. Submit `https://www.preet-baxi.com/sitemap.xml`.
3. Confirm status updates to `Success` and `Discovered pages` = `12` (Google may take hours to days to re-read the updated XML and image tags).

---

## 3. Page-by-Page URL Inspection & Indexing Checklist (All 12 Canonical URLs)

Respect Google Search Console's daily quota (~10–12 manual "Request Indexing" submissions per day). Prioritize **Tier 1** (the 4 pages not observed in baseline SERPs + updated homepage/publications), then **Tier 2** the next day if quota is hit.

| Priority | Canonical URL | Baseline Search Observation | Action in GSC URL Inspection |
|---|---|---|---|
| **Tier 1 (Day 1)** | `https://www.preet-baxi.com/` | Observed (#1 branded) | Inspect → Live Test → Verify canonical `https://www.preet-baxi.com/` → **Request Indexing** (major LCP + ProfilePage JSON-LD update) |
| **Tier 1 (Day 1)** | `https://www.preet-baxi.com/publications.html` | Observed | Inspect → Live Test → **Request Indexing** (full abstracts, BibTeX, verified DOIs, ScholarlyArticle JSON-LD) |
| **Tier 1 (Day 1)** | `https://www.preet-baxi.com/research/cora.html` | **Not observed in baseline** | Inspect → Check exclusion reason → Live Test → **Request Indexing** |
| **Tier 1 (Day 1)** | `https://www.preet-baxi.com/research/ligo-monitoring.html` | **Not observed in baseline** | Inspect → Check exclusion reason → Live Test → **Request Indexing** (highest immediate non-branded opportunity) |
| **Tier 1 (Day 1)** | `https://www.preet-baxi.com/research/opsagent-rl.html` | **Not observed in baseline** | Inspect → Check exclusion reason → Live Test → **Request Indexing** |
| **Tier 1 (Day 1)** | `https://www.preet-baxi.com/research/cost-aware-llm-judges.html` | **Not observed in baseline** | Inspect → Check exclusion reason → Live Test → **Request Indexing** |
| **Tier 2 (Day 1–2)** | `https://www.preet-baxi.com/research/` | Observed | Inspect → Live Test → **Request Indexing** (added breadcrumb, ItemList JSON-LD, thumbnail alt text) |
| **Tier 2 (Day 1–2)** | `https://www.preet-baxi.com/research/agentsentry.html` | Observed | Inspect → Live Test → **Request Indexing** (updated title/meta, unified TechArticle JSON-LD, WebP) |
| **Tier 2 (Day 1–2)** | `https://www.preet-baxi.com/research/metaaudit.html` | Observed | Inspect → Live Test → **Request Indexing** (fixed Schema type to TechArticle, added OG/Twitter) |
| **Tier 2 (Day 1–2)** | `https://www.preet-baxi.com/research/prompt-injection-screening.html` | Observed | Inspect → Live Test → **Request Indexing** (ACL 2026 DOI, abstract, BibTeX, ScholarlyArticle) |
| **Tier 2 (Day 1–2)** | `https://www.preet-baxi.com/research/gaming-the-gatekeeper.html` | Observed | Inspect → Live Test → **Request Indexing** (removed draft caption, upgraded title/meta/JSON-LD) |
| **Tier 2 (Day 1–2)** | `https://www.preet-baxi.com/research/rai-gate.html` | Observed | Inspect → Live Test → **Request Indexing** (removed draft caption, upgraded title/meta/JSON-LD) |

*Also inspect `/index.html` and `/research/index.html` in GSC (do NOT request indexing for them):* verify Google treats them as `Alternate page with proper canonical tag` pointing to `/` and `/research/` respectively.

---

## 4. Bing Webmaster Tools Setup (Also Powers DuckDuckGo, Yahoo, Copilot Search)

1. Open `https://www.bing.com/webmasters`.
2. Sign in and choose **"Import your sites from Google Search Console"** (zero additional DNS/HTML files needed once GSC is verified).
3. Submit `https://www.preet-baxi.com/sitemap.xml` under **Sitemaps**.
4. Optionally enable **IndexNow** only if desired in future CI; standard sitemap submission is sufficient for a 12-page academic site.

---

## 5. Automated Read-Only GSC Monitoring (`scripts/gsc_monitor.py`) & 30/60/90/180/365-Day Tracking Framework

A read-only monitoring script has been added at `scripts/gsc_monitor.py` (uses only the official Search Analytics query endpoint; **never** uses Google's Indexing API).

### Setup (Optional, 5 Minutes)
1. Enable **Google Search Console API** in a Google Cloud project and create a read-only Service Account JSON key (store outside the repo, never commit).
2. Add the service account email as a **Restricted user** in GSC (`Settings → Users and permissions`).
3. Run monthly:
   ```bash
   python3 scripts/gsc_monitor.py \
     --site https://www.preet-baxi.com/ \
     --credentials /path/to/gsc-service-account.json \
     --days 28 \
     --out-dir seo-reports/gsc-snapshots
   ```
   The script exports timestamped CSV/Markdown snapshots separating **Branded** queries (containing `preet`, `baxi`, `preet-baxi`, `agentsentry`, `metaaudit`) from **Non-Branded Technical** queries, plus page-level clicks, impressions, CTR, and average position.

### Milestone Review Schedule

| Checkpoint | Primary Goals to Check in GSC & Analytics | Decision Triggers |
|---|---|---|
| **Day 30** | All 12 canonical URLs indexed; zero `noindex`/canonical conflicts; sitemap showing 12 valid URLs; zero rich-result syntax errors in GSC Enhancements; homepage Core Web Vitals LCP passing in field/lab. | If any of the 4 previously unobserved pages remain `Crawled - currently not indexed`, inspect content depth, expand technical prose/methods on that page, and re-verify internal link equity. |
| **Day 60** | First non-branded impressions emerging for high-specificity technical queries (`LIGO O4 continuous wave hardware injections`, `indirect prompt injection resume screening ACL 2026`, `LLM-as-a-judge prediction-powered inference`). Verify external profile updates (U-M LSA, MICDE, ORCID, GitHub, Scholar) are recrawled. | Identify top 5–10 queries ranking in positions 8–25 with high impressions and low CTR; refine meta descriptions and section headings naturally to match researcher intent. |
| **Day 90** | Measure branded vs. non-branded impression share; check Google Images impressions for portrait and architecture diagrams; inspect whether sitelinks appear for `"Preet Baxi"`. | Publish first new deep-dive technical artifact (e.g., open-source benchmark release or preprint summary for AgentSentry / MetaAudit / CORA) to address content gaps. |
| **Day 180** | Evaluate sustained non-branded clicks across the 5 research clusters; verify all 2026 papers (`ACL 2026`, `CQG 2026`, plus any newly accepted preprints) are consolidated across Google Scholar, ORCID, Semantic Scholar, and `/publications.html`. | Assess whether any cluster has grown to 4+ substantive pages warranting a dedicated cluster overview hub page (avoid thin hubs). |
| **Day 365** | Annual entity & publication audit: compare YoY non-branded impressions, clicks, citation linkages, and referring `.edu` / publisher / GitHub domains. | Update `sitemap.xml` `lastmod`, archive stale milestones, and align research summaries with current publications and job-market/faculty positioning. |
