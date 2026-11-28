# Researcher Identity Consistency Audit (Task 7)

**Audit Date:** 2026-11-28  
**Method:** Publicly accessible read-only APIs and public web pages only (Crossref REST API, ORCID Public API v3.0, ACL Anthology, GitHub Public API, Google Search public snippets). **No external accounts were accessed or modified.**

---

## 1. Cross-Platform Identity Matrix

| Platform | Public URL | Verified Name / Affiliation | Links to `www.preet-baxi.com`? | Key Inconsistencies Found |
|---|---|---|---|---|
| **Personal Website** | `https://www.preet-baxi.com/` | Preet Baxi · University of Michigan (Physics & Scientific Computing) | Canonical (`#person` JSON-LD) | **Consistent.** Links 6 verified `sameAs` profiles; intentionally omits ORCID until duplicate is merged. |
| **GitHub Profile & Profile README** | `https://github.com/preetb1199` | Preet Baxi · University of Michigan, Ann Arbor | Profile README links `https://www.preet-baxi.com/`; `blog` field still `"www.preet-baxi.com"` (no `https://`) | `bio` still `"PhD in Physics and Scientific Computing"` (omits AI Safety/LLM Eval/LIGO); blocked by scoped token `HTTP 403`. |
| **Google Scholar** | `https://scholar.google.com/citations?user=dpuZ0_IAAAAJ` | Preet Baxi · University of Michigan-Ann Arbor (`umich.edu` verified) | Yes (Homepage set) | User confirmed Scholar profile optimization completed in this session; Google's cached snippet will refresh on next crawl. |
| **ACL Anthology** | `https://aclanthology.org/people/preet-baxi/` | Preet Baxi (author of `2026.findings-acl.142`) | No | No ORCID attached in Crossref or ACL Anthology record yet. |
| **Crossref — ACL 2026** | `https://doi.org/10.18653/v1/2026.findings-acl.142` | `Preet Baxi` (`ORCID: None`) | N/A | Official title: *"Prompt Injection in Automated Résumé Screening with Large Language Models: Single and Multi-Injection Settings"*. |
| **Crossref — CQG 2026** | `https://doi.org/10.1088/1361-6382/ae7adb` | `Preet Baxi` (`ORCID: 0009-0007-3653-9808`) | N/A | Official title: *"Monitoring of continuous-wave hardware injections in LIGO interferometers during the O4 observing run"*. Linked to **newer** ORCID. |
| **Crossref — PRD 2021** | `https://doi.org/10.1103/PhysRevD.104.084080` | `Preet Baxi` (`ORCID: 0000-0002-6726-1665`) | N/A | Official title: *"Detectability of gravitational higher order modes in the third-generation era"*. Linked to **older** ORCID. |
| **ORCID #1 (2021)** | `https://orcid.org/0000-0002-6726-1665` | Preet Baxi · Dwarkadas J. Sanghvi College of Engineering (B.E.), Univ. of Mumbai, Indian Academy of Sciences | **No** (`researcher-urls: []`) | Has 3 works (PRD 2021 + rocket nozzle); missing U-M affiliation, ACL 2026, CQG 2026, and website URL. |
| **ORCID #2 (2026)** | `https://orcid.org/0009-0007-3653-9808` | Preet Baxi · University of Michigan–Ann Arbor (GSRA, Physics) | **No** (`researcher-urls: []`) | Created Feb 2026; **0 public works** displayed despite Crossref linkage on CQG 2026; missing website URL. |
| **U-M LSA Physics** | `https://lsa.umich.edu/physics/people/graduate-students/preetb.html` | Preet Baxi · Graduate Student | **No** | Minimal listing; missing bio and website link. |
| **U-M MICDE** | `https://micde.umich.edu/member/preet-baxi/` | Preet Baxi · PhD in Scientific Computing / Physics | **No** | Empty Background section; missing website link. |
| **ResearchGate** | `https://www.researchgate.net/profile/Preet-Baxi-2` | Preet Baxi | **No** | Ranks #1 for `"Preet Baxi Publications"` yet shows outdated publication list (3 older papers). *(Not accessed/modified per restrictions.)* |

---

## 2. Duplicate ORCID Investigation (Evidence-Based Provenance)

Rather than assuming identity from matching names, public ORCID v3.0 API records and Crossref DOI authorship records were cross-referenced:

- **`0000-0002-6726-1665`** (created `2021-05-03`): Verified undergraduate/pre-PhD academic record (B.E. Mechanical Engineering at Dwarkadas J. Sanghvi College of Engineering, University of Mumbai Astronomy & Astrophysics diploma, Indian Academy of Sciences Summer Research Fellow) and linked in Crossref as co-author of **PRD 2021** (`10.1103/PhysRevD.104.084080`) alongside Divyajyoti, Chandra Kant Mishra, and K. G. Arun.
- **`0009-0007-3653-9808`** (created `2026-02-17`): Verified doctoral affiliation (Graduate Student Research Assistant, Physics, University of Michigan–Ann Arbor) and linked in Crossref as first author of **CQG 2026** (`10.1088/1361-6382/ae7adb`) alongside Jessica Leviton, Eilam Morag, Matthew Pitkin, and Keith Riles.

**Conclusion & Website Structured Data Decision:** Both records have institutional and DOI provenance connecting them to your academic trajectory, causing split publisher attribution across Crossref, IOPscience, APS, and downstream indexing graphs (OpenAlex/Semantic Scholar). Per strict integrity rules, **neither ORCID was modified** and **neither ORCID was added to `index.html` `sameAs` yet**. Once you deprecate one duplicate record in ORCID Account Settings, add your single surviving primary ORCID URL to `index.html` (`#person` JSON-LD `sameAs`).

---

## 3. Exact Publisher Title Discrepancies Found & Fixed

During Crossref verification, minor wording mismatches were found in repository READMEs vs. official Crossref records and immediately corrected on `preetb1199.github.io` and `preetb1199/preetb1199`:
- **ACL 2026:** Aligned to exact ACL Anthology/Crossref title *"Prompt Injection in Automated Résumé Screening with Large Language Models: Single and Multi-Injection Settings"*.
- **CQG 2026:** Aligned to exact IOPscience/Crossref title *"Monitoring of continuous-wave hardware injections in LIGO interferometers during the O4 observing run"*.
- **PRD 2021:** Aligned to exact APS/Crossref title *"Detectability of gravitational higher order modes in the third-generation era"*.
