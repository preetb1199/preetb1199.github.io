# Unavoidable Manual Actions (Only What Genuinely Requires You)

Everything feasible within authorized repo permissions has been executed, verified, and deployed. Only the 6 actions below require your personal authentication, editorial approval, or external account access:

---

## 1. Review & Selectively Publish New Technical Guides (Approval Required)
- Inspect branch **`research-authority-expansion`** (`https://github.com/preetb1199/preetb1199.github.io/tree/research-authority-expansion`), which holds 5 substantial technical guides in `research/guides/` (summarized in `NEW_RESEARCH_RESOURCES.md`).
- **Fastest wins to publish first:** `ligo-continuous-wave-hardware-injections.html` and `indirect-prompt-injection-agentic-ai.html` (both backed by already peer-reviewed 2026 publications).

## 2. Apply Remaining GitHub Updates (`HTTP 403` Scope Limit)
- Follow `GITHUB_REMAINING_TASKS.md` (referencing `seo-reports/github-discoverability-audit.md`) to:
  1. Update **`Prompt_Injection_ACL26`** (`README.md`, `CITATION.cff`, description, homepage, topics).
  2. Update **`CalculateSNRg_Python`** (`README.md`, description, homepage, topics).
  3. Update your GitHub profile **`bio`**, **`blog`** (`https://www.preet-baxi.com/`), and **pin** `Prompt_Injection_ACL26`, `CalculateSNRg_Python`, and `preetb1199.github.io`.

## 3. Import Site into Bing Webmaster Tools (Auth Required — 2 Minutes)
- Sign in to `https://www.bing.com/webmasters` → **Import from Google Search Console** → verify `https://www.preet-baxi.com/sitemap.xml` is submitted. *(IndexNow host verification key `a8abb5d57579b82dc92f5ffc32629e0e.txt` is already deployed live!)*

## 4. Merge Duplicate ORCID Profiles & Add Primary ORCID to `index.html` (Auth Required)
- In ORCID Account Settings, deprecate one duplicate record between `0000-0002-6726-1665` (PRD 2021) and `0009-0007-3653-9808` (CQG 2026) — see provenance details in `RESEARCHER_IDENTITY_AUDIT.md`.
- Add `https://www.preet-baxi.com/` and all 3 verified DOIs to your surviving primary ORCID, then add that single ORCID URL to `sameAs` in `index.html`.

## 5. Update External University & Academic Profiles (Auth / Institutional Email Required)
- **U-M LSA Physics** (`https://lsa.umich.edu/physics/people/graduate-students/preetb.html`) and **U-M MICDE** (`https://micde.umich.edu/member/preet-baxi/`): Request bio + `https://www.preet-baxi.com/` link using Draft 1 in `outreach-drafts.md`.
- Optional when ready: Submit PRs for your peer-reviewed ACL 2026 paper to curated GitHub lists (`ACADEMIC_BACKLINK_OPPORTUNITIES.csv` + Draft 2 in `outreach-drafts.md`), mint Zenodo DOIs for `Prompt_Injection_ACL26` & `CalculateSNRg_Python`, and update ResearchGate/LinkedIn on your own schedule.

## 6. Monthly Search Performance Check (Local Dashboard)
- Once a month, export CSVs from Google Search Console and open `seo-reports/final-execution/SEARCH_MONITORING_DASHBOARD/index.html` locally (or run `generate_report.py`) to review branded vs. non-branded query growth. *(Never commit private CSV exports; `.gitignore` protects `local-data/`.)*
