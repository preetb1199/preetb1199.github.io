# Academic Publication Visibility & Bibliographic Audit

**Audit Date:** 2026-11-27  
**Authoritative Records Checked:** ACL Anthology, arXiv, Crossref API (IOPscience / CQG & APS / Physical Review D), Google Scholar, ORCID Public API

---

## 1. Verified Publication Records

### Paper 1 — Findings of ACL 2026 (First Author · Peer-Reviewed)
- **Authoritative Title:** Prompt Injection in Automated Résumé Screening with Large Language Models: Single and Multi-Injection Settings
- **Verified Authors:** Preet Baxi, Jiannan Xu, Jane Yi Jiang, Stefanus Jasin
- **Venue:** *Findings of the Association for Computational Linguistics: ACL 2026*, pp. 2942–2953, San Diego, California, USA (July 2026)
- **DOI:** `https://doi.org/10.18653/v1/2026.findings-acl.142`
- **Publisher URL:** `https://aclanthology.org/2026.findings-acl.142/` (PDF: `https://aclanthology.org/2026.findings-acl.142.pdf`)
- **arXiv Preprint:** `https://arxiv.org/abs/2606.27287` (submitted 25 June 2026, `cs.AI`)
- **Public Code Repository:** `https://github.com/preetb1199/Prompt_Injection_ACL26`
- **Website Improvements Made:** Added full co-authors, exact pagination/DOI, arXiv link, GitHub code link, verified publisher abstract, collapsible BibTeX, and `ScholarlyArticle` JSON-LD on both `/publications.html` and `/research/prompt-injection-screening.html`, plus cross-links between them and `/research/gaming-the-gatekeeper.html`.

### Paper 2 — Classical and Quantum Gravity 2026 (First Author · Peer-Reviewed)
- **Authoritative Title:** Monitoring of Continuous-Wave Hardware Injections in LIGO Interferometers during the O4 Observing Run
- **Verified Authors:** Preet Baxi, Jessica Leviton, Eilam Morag, Matthew Pitkin, Keith Riles
- **Venue:** *Classical and Quantum Gravity*, Vol. 43, No. 13, 135019 (Published 7 July 2026 — verified via Crossref API)
- **DOI:** `https://doi.org/10.1088/1361-6382/ae7adb`
- **arXiv Preprint:** `https://arxiv.org/abs/2601.09918` (submitted 14 January 2026, `astro-ph.IM; gr-qc`)
- **Website Improvements Made:** Added full co-authors, exact volume/issue/article number/date, DOI, arXiv link, verified abstract summary, collapsible BibTeX, and `ScholarlyArticle` JSON-LD on both `/publications.html` and `/research/ligo-monitoring.html`, plus cross-links between them.

### Paper 3 — Physical Review D 2021 (Peer-Reviewed)
- **Authoritative Title:** Detectability of gravitational higher order modes in the third-generation era
- **Verified Authors:** Divyajyoti, Preet Baxi, Chandra Kant Mishra, K. G. Arun
- **Venue:** *Physical Review D*, Vol. 104, No. 8, 084080 (Published 21 October 2021 — verified via APS & Crossref API)
- **DOI:** `https://doi.org/10.1103/PhysRevD.104.084080`
- **arXiv Preprint:** `https://arxiv.org/abs/2103.03241` (submitted 4 March 2021, `gr-qc`)
- **Website Improvements Made:** Replaced the generic Google Scholar link on both `/` and `/publications.html` with the authoritative APS DOI (`10.1103/PhysRevD.104.084080`), added `arXiv:2103.03241`, full co-author names, verified abstract summary, collapsible BibTeX, and `ScholarlyArticle` JSON-LD.

### Paper 4 — 2026 Preprint Under Review
- **Title:** Sequential Sampling for Binary Classification: Two LLMs are (Almost) All You Need
- **Authors:** G. Li, J. Liang, M. Liu, Y. Lei, S. Jasin, F. Yang, P. Baxi
- **Status:** Preprint under review (not marked `ScholarlyArticle`; represented accurately as `CreativeWork` with status `"Preprint under review"`).
- **Website Improvements Made:** Connected the `/publications.html#two-llms-preprint` listing directly to `/research/cost-aware-llm-judges.html` (and vice versa).

---

## 2. Critical Academic Identity Finding: Duplicate ORCID Accounts

Querying Crossref and the public ORCID v3 API revealed **two distinct ORCID profiles** registered under Preet Baxi:

1. **`https://orcid.org/0009-0007-3653-9808`** (created Feb 2026; attached to **CQG 2026** `10.1088/1361-6382/ae7adb`)
   - Public works listed: **0**
   - Website URLs listed: **0**
2. **`https://orcid.org/0000-0002-6726-1665`** (created May 2021; attached to **PRD 2021** `10.1103/PhysRevD.104.084080`)
   - Public works listed: **3** (PRD 2021 + 2021 arXiv + rocket exhaust nozzle paper)
   - Website URLs listed: **0**
   - Missing both 2026 papers (ACL 2026 and CQG 2026).

**Impact:** Split ORCIDs fragment author disambiguation across Crossref, OpenAlex, INSPIRE-HEP, NASA ADS, Semantic Scholar, and ACL Anthology.  
**Recommended Action:** Decide which ORCID to keep as primary (typically the older `0000-0002-6726-1665` with existing works, or `0009-0007-3653-9808` if preferred for LIGO/O4), deprecate the duplicate via ORCID Account Settings (which creates a permanent redirect), add all DOIs + `https://www.preet-baxi.com/` to the primary ORCID, and then add that single ORCID URL to `index.html`'s `sameAs` list.

---

## 3. Google Scholar Inclusion & Eligibility Audit

Per Google Scholar's Inclusion Guidelines:
- **Eligible for Google Scholar indexing:** Full-text scholarly papers (PDF or full HTML paper with bibliographic `citation_*` meta tags). Your three peer-reviewed papers are **already hosted on authoritative Scholar-indexed venues**: ACL Anthology (`2026.findings-acl.142`), IOPscience (`10.1088/1361-6382/ae7adb`), APS (`10.1103/PhysRevD.104.084080`), and arXiv (`2606.27287`, `2601.09918`, `2103.03241`), and your additional LIGO CW collaboration paper (`arXiv:2603.04792`) is also on arXiv.
- **Not eligible as standalone Google Scholar paper records:** Portfolio explainer/case-study pages (`agentsentry.html`, `metaaudit.html`, `cora.html`, `rai-gate.html`, `opsagent-rl.html`, `gaming-the-gatekeeper.html`, `cost-aware-llm-judges.html`). We intentionally did **not** add `citation_pdf_url` or misclassify unpublished studies as `ScholarlyArticle` (and corrected `metaaudit.html` from `ScholarlyArticle` to `TechArticle`).
- **How to legitimately expand Scholar visibility for independent projects:** If you later release full technical reports / preprints for **AgentSentry**, **MetaAudit**, or **CORA** on arXiv (or host full-text PDFs with complete `citation_*` meta tags on your site), those manuscripts become genuinely eligible for Google Scholar and can link directly to your interactive web companions.
