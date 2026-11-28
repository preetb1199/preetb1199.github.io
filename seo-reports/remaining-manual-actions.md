# Remaining Manual & Authentication-Gated Actions

**Date:** 2026-11-27  
**Branch Ready for Review:** `seo-optimization` (not yet merged to `main`)

Every technically feasible code, metadata, structured data, image, internal linking, sitemap, and CI improvement has been implemented on branch `seo-optimization` and verified with `python3 scripts/seo_audit.py` and Lighthouse. The actions below require your approval, account authentication, or domain/profile ownership.

---

## 1. Review & Deploy Branch `seo-optimization` (Approval Required)
- [ ] Review the diff between `main` and `seo-optimization` (`git diff main..seo-optimization --stat` or open a Pull Request on GitHub).
- [ ] Confirm visually that fonts, colors, layouts, and interactive widgets (AgentSentry, MetaAudit, CORA) are unchanged.
- [ ] Merge `seo-optimization` into `main` to trigger GitHub Pages deployment to `https://www.preet-baxi.com`.
- [ ] Verify the `.github/workflows/seo-check.yml` GitHub Action passes on `main`.

## 2. Google Search Console & Bing Webmaster Tools (Auth Required — Immediately Post-Merge)
- [ ] Sign in to `https://search.google.com/search-console` and confirm ownership of `https://www.preet-baxi.com/` (backed by existing `googleb0a732b0b1e2e027.html`).
- [ ] Add and DNS-verify the Domain property `preet-baxi.com` (via TXT record at your domain registrar) so `http`/`https` and apex/`www` are monitored together.
- [ ] Export baseline GSC **Pages** and **Search Results** reports before submitting updates.
- [ ] Submit `https://www.preet-baxi.com/sitemap.xml` under **Sitemaps** and verify 12 discovered URLs.
- [ ] Run **URL Inspection → Test Live URL → Request Indexing** for Priority Tier 1 pages first (especially the 4 pages not observed in baseline searches: `cora.html`, `ligo-monitoring.html`, `opsagent-rl.html`, `cost-aware-llm-judges.html`, plus `/` and `/publications.html`), followed by Tier 2 pages (respecting daily quota).
- [ ] Sign in to `https://www.bing.com/webmasters`, import `https://www.preet-baxi.com/` from Google Search Console, and submit `https://www.preet-baxi.com/sitemap.xml`.

## 3. Post-Deploy Live Validation (5 Minutes)
- [ ] Test `https://www.preet-baxi.com/`, `https://www.preet-baxi.com/publications.html`, and `https://www.preet-baxi.com/research/prompt-injection-screening.html` in Google's **Rich Results Test** (`https://search.google.com/test/rich-results`) and **Schema.org Validator** (`https://validator.schema.org/`).
- [ ] Run **PageSpeed Insights** (`https://pagespeed.web.dev/`) on `https://www.preet-baxi.com/` to confirm live CDN-compressed LCP drops from ~11.5 s to < 2.0 s.

## 4. Resolve Duplicate ORCID Profiles (High Entity Impact)
- [ ] Sign in to ORCID and deprecate/merge the duplicate record between `https://orcid.org/0009-0007-3653-9808` (CQG 2026) and `https://orcid.org/0000-0002-6726-1665` (PRD 2021).
- [ ] Populate your primary ORCID profile with `https://www.preet-baxi.com/`, U-M affiliation, research keywords, and DOIs for ACL 2026 (`10.18653/v1/2026.findings-acl.142`), CQG 2026 (`10.1088/1361-6382/ae7adb`), and PRD 2021 (`10.1103/PhysRevD.104.084080`).
- [ ] Add your single primary ORCID URL to `sameAs` inside `index.html` (`#person` JSON-LD).

## 5. External Profile Updates (High Authority & Discoverability Impact)
- [ ] **U-M LSA Physics** (`https://lsa.umich.edu/physics/people/graduate-students/preetb.html`): Add `https://www.preet-baxi.com/` and research bio.
- [ ] **U-M MICDE** (`https://micde.umich.edu/member/preet-baxi/`): Fill in `Background` bio and link to `https://www.preet-baxi.com/`.
- [ ] **Google Scholar** (`https://scholar.google.com/citations?user=dpuZ0_IAAAAJ`): Update research interest tags to include `AI Safety`, `Agentic AI Security`, `LLM Evaluation`, and verify 2026 papers are merged without arXiv duplicates.
- [ ] **ResearchGate** (`https://www.researchgate.net/profile/Preet-Baxi-2`): Add 2026 ACL & CQG DOIs and link to `https://www.preet-baxi.com/` (currently ranks #1 for `"Preet Baxi Publications"`).
- [ ] **GitHub (`preetb1199`)**: Update user `blog` to `https://www.preet-baxi.com/`, refine user bio, and add `homepage` URLs + repository topics to `Prompt_Injection_ACL26`, `preetb1199.github.io`, and `CalculateSNRg_Python` *(can be automated via `gh api` upon your approval)*.
- [ ] **LinkedIn** (`https://www.linkedin.com/in/preet-baxi/`): Align headline with AI Safety / Agentic Security / LLM Evaluation and feature links to `https://www.preet-baxi.com/` and `/publications.html`.
- [ ] **ACL Anthology & arXiv / NASA ADS / INSPIRE-HEP**: Associate your consolidated primary ORCID iD across author records.

## 6. Ongoing Verification (30/60/90/180/365 Days)
- [ ] Optionally connect a read-only GSC Service Account to `scripts/gsc_monitor.py` to archive monthly branded vs. non-branded query snapshots.
- [ ] Review any future papers (e.g., `arXiv:2603.04792` LIGO globular clusters, *"Sequential Sampling for Binary Classification"* upon acceptance, or upcoming AgentSentry/MetaAudit/CORA preprints) and add them to `publications.html` and their corresponding project pages with accurate `ScholarlyArticle` markup once published/posted.
