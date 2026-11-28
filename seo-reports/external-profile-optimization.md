# External Academic & Researcher Profile Optimization Plan

**Audit Date:** 2026-11-27  
**Canonical Researcher Entity:** `Preet Baxi` (`https://www.preet-baxi.com/#person`)  
**Policy Note:** No external profiles were modified autonomously. All actions below require your direct sign-in or explicit approval. Every recommendation is white-hat, factually accurate, and grounded in verified records.

---

## 1. Entity Disambiguation & Canonical Identity

Consistent naming, affiliation, and bidirectional links across authoritative academic platforms help Google Search, Google Scholar, and Knowledge Graph systems unify your publications and web presence under a single researcher entity.

**Recommended Standard Short Bio (copy-paste ready):**
> Preet Baxi is a PhD candidate in Physics and Scientific Computing at the University of Michigan, Ann Arbor. His research focuses on AI safety, runtime security for agentic AI systems, indirect prompt injection defenses, statistically valid LLM-as-a-judge evaluation, and gravitational-wave data analysis with the LIGO Scientific Collaboration. Personal website: https://www.preet-baxi.com

**Canonical URL to use on EVERY profile:** `https://www.preet-baxi.com/` (always include `https://` and `www.`).

---

## 2. Priority External Profile Audit & Exact Actions

### Priority 1 (Critical): ORCID — Resolve Duplicate Profiles
During verification against Crossref and the public ORCID API, **two separate ORCID iDs** were discovered under your name:

| ORCID iD | Created | Linked Paper | Current Public Works | Website Link |
|---|---|---|---:|---|
| `https://orcid.org/0009-0007-3653-9808` | Feb 2026 | CQG 2026 (`10.1088/1361-6382/ae7adb`) | **0** | Missing |
| `https://orcid.org/0000-0002-6726-1665` | May 2021 | PRD 2021 (`10.1103/PhysRevD.104.084080`) | **3** (PRD 2021 + rocket nozzle) | Missing |

**Why this matters:** Split ORCID identifiers fragment publisher metadata (Crossref, IOPscience, APS, ACL Anthology, OpenAlex, Semantic Scholar) and weaken entity consolidation. `index.html` intentionally omits ORCID from `sameAs` until you deprecate the duplicate.

**Exact Actions:**
1. Decide which ORCID iD will be your permanent primary identifier (usually the older `0000-0002-6726-1665` or the newer `0009-0007-3653-9808` — note `0000-0002-6726-1665` already has 2021 DOI linkage).
2. Follow ORCID's official deprecation workflow (`Account Settings → Remove duplicate record`) so the deprecated iD automatically redirects to your primary iD.
3. On your primary ORCID profile:
   - Add **Website:** `https://www.preet-baxi.com/` (label: `Personal Research Website`).
   - Add **Employment / Education:** `University of Michigan — Ann Arbor` (Physics & Scientific Computing PhD).
   - Add **Keywords:** `AI Safety`, `Agentic AI Security`, `LLM Evaluation`, `Prompt Injection`, `Gravitational-Wave Physics`, `Scientific Computing`.
   - Import/link all verified works by DOI:
     - `10.18653/v1/2026.findings-acl.142` (Findings of ACL 2026)
     - `10.1088/1361-6382/ae7adb` (Classical and Quantum Gravity 2026)
     - `10.1103/PhysRevD.104.084080` (Physical Review D 2021)
4. Once merged, add your single primary ORCID URL to `sameAs` in `index.html` (under the `#person` JSON-LD node).

---

### Priority 2 (High Authority `.edu` Backlinks): University of Michigan Profiles
Your `.edu` profiles already rank #2 and #3 for branded searches (`Preet Baxi`, `Preet Baxi University of Michigan`), yet **neither currently links to `https://www.preet-baxi.com/`**.

1. **U-M LSA Physics Graduate Student Profile**  
   - URL: `https://lsa.umich.edu/physics/people/graduate-students/preetb.html`
   - Current state: Minimal directory entry; no research description or personal website link.
   - **Action:** Request a directory update through LSA Physics staff/profile editor to add:
     - Personal Website: `https://www.preet-baxi.com/`
     - Short bio mentioning AI safety, LLM evaluation, and LIGO gravitational-wave research.
2. **U-M MICDE (Michigan Institute for Computational Discovery & Engineering)**  
   - URL: `https://micde.umich.edu/member/preet-baxi/`
   - Current state: Lists PhD in Scientific Computing / Physics; `Background` section is empty; no website link.
   - **Action:** Update your MICDE member profile to add the standard bio above and link to `https://www.preet-baxi.com/` and `https://www.preet-baxi.com/publications.html`.

---

### Priority 3: Google Scholar Profile
- URL: `https://scholar.google.com/citations?user=dpuZ0_IAAAAJ`
- Current verified state: 2,771 citations, h-index 20, i10-index 28; homepage already linked; current research interests: `AI/ML`, `LLMs`, `Data Analysis`, `Gravitational Waves`, `Rocket Propulsion`.
- **Actions:**
  1. Update Research Interests (max 5 tags on Scholar) to reflect your current primary focus areas, e.g.:
     - `AI Safety`
     - `Agentic AI Security`
     - `LLM Evaluation`
     - `Machine Learning`
     - `Gravitational Waves`
  2. Verify that both 2026 publications (`2026.findings-acl.142` and `CQG 2026` / `arXiv:2601.09918`) are cleanly merged with their arXiv versions (no split duplicate entries splitting citation counts).
  3. Confirm the Homepage field uses `https://www.preet-baxi.com/`.

---

### Priority 4: GitHub Profile & Public Repositories (`https://github.com/preetb1199`)
Audit via GitHub API (`gh api users/preetb1199` and repo metadata) found high-leverage, zero-risk improvements:

| Resource | Current Metadata | Recommended Update |
|---|---|---|
| **User Profile** (`preetb1199`) | `bio`: `"PhD in Physics and Scientific Computing"`<br>`blog`: `"www.preet-baxi.com"` (missing `https://`) | `bio`: `"PhD Candidate in Physics & Scientific Computing @ U-M | AI Safety, Agentic Security, LLM Evaluation & LIGO Gravitational Waves"`<br>`blog`: `"https://www.preet-baxi.com/"` |
| **Repo: `Prompt_Injection_ACL26`** (2 stars) | `homepage`: `null`<br>`topics`: `[]` | `homepage`: `"https://www.preet-baxi.com/research/prompt-injection-screening.html"`<br>`topics`: `["ai-safety", "prompt-injection", "indirect-prompt-injection", "acl-2026", "llm-security", "resume-screening"]`<br>Add link to ACL Anthology (`https://aclanthology.org/2026.findings-acl.142/`), arXiv (`2606.27287`), and project page in `README.md`. |
| **Repo: `preetb1199.github.io`** | `description`: `"personal website"`<br>`homepage`: `null`<br>`topics`: `[]` | `description`: `"Personal academic website of Preet Baxi — AI Safety, Agentic Security, LLM Evaluation, and LIGO Gravitational-Wave Research"`<br>`homepage`: `"https://www.preet-baxi.com/"`<br>`topics`: `["academic-website", "ai-safety", "llm-evaluation", "gravitational-waves"]` |
| **Repo: `CalculateSNRg_Python`** | `homepage`: `null`<br>`topics`: `[]` | `homepage`: `"https://www.preet-baxi.com/research/ligo-monitoring.html"` (or `/publications.html`)<br>`topics`: `["gravitational-waves", "ligo", "astrophysics", "python"]` |
| **Optional Profile `README.md`** (`preetb1199/preetb1199`) | Not present | Create a concise academic profile README linking to `https://www.preet-baxi.com/`, `/publications.html`, and featured research pages (AgentSentry, MetaAudit, CORA, ACL 2026, LIGO O4). |

*Note:* These GitHub metadata updates can be applied via `gh api` automatically if you approve them after reviewing this report.

---

### Priority 5: ResearchGate, ACL Anthology, LinkedIn, arXiv, & Speaker Profiles

1. **ResearchGate** (`https://www.researchgate.net/profile/Preet-Baxi-2`)
   - **High visibility finding:** ResearchGate currently ranks **#1 on Google** for `"Preet Baxi Publications"`, yet lists only 3 older papers and has no link to your website.
   - **Action:** Claim/update your ResearchGate profile to add your 2026 ACL and CQG papers (linking via official DOIs/arXiv, respecting publisher copyright on PDFs) and add `https://www.preet-baxi.com/` to your profile bio/website field.
2. **ACL Anthology Author Page** (`https://aclanthology.org/people/preet-baxi/`)
   - Already verified and linked from `index.html` (`sameAs`).
   - **Action (after ORCID merge):** Submit a standard ACL Anthology metadata correction PR (via `acl-org/acl-anthology`) to associate your verified ORCID iD with your author record.
3. **LinkedIn** (`https://www.linkedin.com/in/preet-baxi/`)
   - Ensure the headline includes `AI Safety`, `Agentic AI Security`, `LLM Evaluation`, and `PhD Candidate, University of Michigan`.
   - Add `https://www.preet-baxi.com/` as your primary Custom Website / Featured link, and feature direct links to your ACL 2026 paper page (`/research/prompt-injection-screening.html`), AgentSentry (`/research/agentsentry.html`), and Publications page (`/publications.html`).
4. **Semantic Scholar & OpenAlex**
   - Claim your Semantic Scholar author profile (`https://www.semanticscholar.org/`) once both 2026 papers are indexed, merge any split author records, and add `https://www.preet-baxi.com/` as your homepage.
5. **Underline Science (`underline.io/speakers/775216-preet-baxi`) & LIGO Roster (`roster.ligo.org`)**
   - Underline Science ranks #5 for `"Preet Baxi University of Michigan"`. If editable, update the speaker bio to reference `https://www.preet-baxi.com/`.
6. **arXiv Author Identifier & Endorsement**
   - Link your primary ORCID iD in your arXiv user account settings so future arXiv preprints automatically propagate ORCID metadata to Google Scholar, InspireHEP, and NASA ADS.

---

## 3. Legitimate Academic Visibility & Natural Backlink Opportunities

Strictly white-hat opportunities that build genuine domain authority and topical relevance without artificial link building:

1. **GitHub Releases + Zenodo DOIs for Open Research Code:** Whenever you release code or benchmarks (e.g., `Prompt_Injection_ACL26`, or future releases for AgentSentry, MetaAudit, CORA), archive a versioned release via Zenodo (linked to your ORCID) and link back to the corresponding `/research/<project>.html` documentation page.
2. **Hugging Face Datasets / Spaces (if releasing public artifacts):** If you publish anonymized evaluation benchmarks or red-teaming suites (for example, prompt injection screening test sets or LLM-judge calibration splits), the dataset/model card should link directly to your canonical project page and ACL/arXiv citation.
3. **ACL / Conference Workshop & Seminar Pages:** When giving talks (U-M MICDE seminars, AI safety reading groups, LIGO calls, conference poster pages, Underline/SlidesLive), provide `https://www.preet-baxi.com/` as your speaker URL and link directly to the relevant project explainer page on slides/posters.
4. **Open-Source Awesome Lists & Community Benchmarks (only where genuinely relevant and editorially accepted):**
   - Submit peer-reviewed ACL 2026 (`2026.findings-acl.142`) to established community reading lists for prompt injection / LLM security on GitHub (e.g., curated prompt-injection paper lists that accept PRs for peer-reviewed ACL/EMNLP/NeurIPS papers), linking the ACL Anthology URL alongside your project page and `Prompt_Injection_ACL26` repo.
5. **NASA ADS & INSPIRE-HEP Author Records (Gravitational-Wave Papers):** Verify that your PRD 2021 (`2021PhRvD.104h4080D`) and CQG 2026 (`arXiv:2601.09918`) papers are claimed under your single primary ORCID in NASA ADS and INSPIRE-HEP so physics searches cleanly attribute your work.
