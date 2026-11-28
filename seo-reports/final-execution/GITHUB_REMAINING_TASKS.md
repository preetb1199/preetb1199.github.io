# Remaining GitHub Tasks (Permission-Gated)

**Status:** Blocked by GitHub App installation scope (`HTTP 403 Resource not accessible by integration`). Per autonomous execution rules, inaccessible API operations were not retried and no new authentication was requested.

---

## 1. Completed Automatically (Live on GitHub)
- **`preetb1199/preetb1199.github.io`** — Upgraded description, homepage (`https://www.preet-baxi.com/`), 7 topics, and academic `README.md` with verified Crossref/ACL Anthology titles.
- **`preetb1199/preetb1199`** — Created public GitHub Profile README repository, set homepage (`https://www.preet-baxi.com/`) and 7 research topics, and deployed academic `README.md` (commit `2c15c63`).

---

## 2. Remaining Manual GitHub Actions (Copy-Paste Kit Already Prepared)

All exact copy-paste descriptions, topics, `README.md` replacements, `CITATION.cff`, and one-shot local `gh api` commands are stored in **[`seo-reports/github-discoverability-audit.md`](../github-discoverability-audit.md)** (not duplicated here):

1. **`preetb1199/Prompt_Injection_ACL26`** *(Priority 1 — 2 stars, ACL 2026 first-author code)*:
   - Apply **Section 4A** (Description, Homepage `https://www.preet-baxi.com/research/prompt-injection-screening.html`, 8 topics).
   - Add **`CITATION.cff`** (**Section 4B**) and replace **`README.md`** (**Section 4C**) — removes draft `"add the final paper citation here"` placeholder and adds exact ACL Anthology title (*"Prompt Injection in Automated Résumé Screening with Large Language Models: Single and Multi-Injection Settings"*), DOI `10.18653/v1/2026.findings-acl.142`, `arXiv:2606.27287`, and BibTeX.
   - *(Note: Ensure the exact Crossref/ACL title above is used in `README.md` and `CITATION.cff`.)*
2. **`preetb1199/CalculateSNRg_Python`** *(Priority 2 — LIGO CW grouped semi-coherent SNR code)*:
   - Apply **Section 5A** (Description, Homepage `https://www.preet-baxi.com/research/ligo-monitoring.html`, 7 topics) and replace 2-line **`README.md`** with **Section 5B**.
3. **GitHub Personal Profile (`https://github.com/settings/profile` & `https://github.com/preetb1199`):**
   - Update **Bio** and **Website** (`https://www.preet-baxi.com/` — adds missing `https://`) per **Section 3**.
   - **Pin these 3 repositories in order:** `Prompt_Injection_ACL26`, `CalculateSNRg_Python`, `preetb1199.github.io`. *(Keep `SolverMineSweeper` and `AHD4Inventory` unpinned.)*

*Alternative:* Run the one-shot local `gh api` commands in **Section 7** of [`github-discoverability-audit.md`](../github-discoverability-audit.md) using your signed-in `gh` CLI (`user` + `public_repo` scopes), or attach `Prompt_Injection_ACL26` and `CalculateSNRg_Python` to this project's GitHub resources in a future session.
