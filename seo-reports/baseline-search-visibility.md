# Baseline Google Search Visibility Report

**Audit Date:** 2026-11-27  
**Target Website:** `https://www.preet-baxi.com`  
**Repository:** `preetb1199/preetb1199.github.io`  
**Methodology:** Programmatic Google Search queries via search tool across all 14 baseline branded and `site:` queries, plus targeted project-name and publication-title queries.

> **Important methodological notes:**
> 1. `site:` queries are diagnostic heuristics only and **not** an authoritative count of indexed pages. Authoritative indexing counts require Google Search Console (`Pages` report).
> 2. This remote Linux VM environment does not have an interactive graphical browser session authenticated to Google, so visual SERP screenshots could not be captured; observable titles, URLs, snippets, and thumbnail image URLs returned by search are documented below.

---

## 1. Branded & Site Query Baseline (14 Required Queries)

| # | Query | Observable `preet-baxi.com` URLs Returned | Top Competing / Co-Occurring Results | Observable Snippet / Image Notes |
|---|---|---|---|---|
| 1 | `Preet Baxi` | `https://www.preet-baxi.com/` (#2) | Google Scholar (`dpuZ0_IAAAAJ`) #1, U-M MICDE (`micde.umich.edu/member/preet-baxi/`) #3 | Homepage snippet uses meta description; thumbnail image `portrait-high-resolution.png` surfaced. |
| 2 | `Preet Baxi AI Safety` | `https://www.preet-baxi.com/publications.html` (#1) | — | **Issue observed:** `publications.html` outranked `/` and `/research/` because its old meta description was generic boilerplate (`"Research portfolio of Preet Baxi: agentic AI safety..."`). |
| 3 | `Preet Baxi University of Michigan` | `https://www.preet-baxi.com/` (#4), `https://www.preet-baxi.com/publications.html` (#9) | Google Scholar #1, U-M LSA Physics #2, U-M MICDE #3, Underline Science #5 | Official U-M pages rank strongly, creating high-authority referral opportunities if linked back to `www.preet-baxi.com`. |
| 4 | `Preet Baxi LIGO` | `https://www.preet-baxi.com/research/ligo-monitoring.html` (#3), `https://www.preet-baxi.com/publications.html` (#4) | Google Scholar #1, `arxiv.org/abs/2603.04792` #2, LIGO Roster #5 | `ligo-monitoring.html` is indexed and ranks #3; image thumbnail fell back to portrait because the page uses inline SVG rather than a figure image. |
| 5 | `Preet Baxi Research` | `https://www.preet-baxi.com/publications.html` (#2) | Google Scholar #1, `arxiv.org/abs/2103.03241` #5 | **Issue observed:** `/research/` did not surface ahead of `publications.html` for `"Preet Baxi Research"`. |
| 6 | `Preet Baxi Publications` | None in top 8 observable results | ResearchGate (`Preet-Baxi-2`) #1, ResearchGate PRD paper #2 | **Issue observed:** `publications.html` did not appear for `"Preet Baxi Publications"` because its old title/description lacked publication venue terms and bibliographic detail. |
| 7 | `Preet Baxi AgentSentry` | `https://www.preet-baxi.com/research/agentsentry.html` (#1), `https://www.preet-baxi.com/publications.html` (#2) | — | Indexed #1 with diagram thumbnail `AgentSentry.png`. |
| 8 | `Preet Baxi MetaAudit` | `https://www.preet-baxi.com/` (#1), `https://www.preet-baxi.com/research/metaaudit.html` (#2), `https://www.preet-baxi.com/publications.html` (#5) | Google Scholar #3, GitHub `preetb1199` #4 | Indexed with SVG thumbnail `MetaAudit_Pipeline_Light.svg`. |
| 9 | `Preet Baxi CORA` | `https://www.preet-baxi.com/research/cora.html` (#1), `https://www.preet-baxi.com/publications.html` (#3) | Google Scholar #2 | Indexed #1 with SVG thumbnail `CORA_Pipeline_Light.svg`. |
| 10 | `Preet Baxi Prompt Injection` | `https://www.preet-baxi.com/research/prompt-injection-screening.html` (#1), `https://www.preet-baxi.com/publications.html` (#2) | GitHub `preetb1199` (`Prompt_Injection_ACL26`) #3 | Strong branded visibility; GitHub code repo surfaces alongside website. |
| 11 | `Preet Baxi LLM Evaluation` | `https://www.preet-baxi.com/` (#1), `https://www.preet-baxi.com/publications.html` (#2), `https://www.preet-baxi.com/research/metaaudit.html` (#3) | — | Strong multi-page branded visibility. |
| 12 | `Preet Baxi Gravitational Waves` | `https://www.preet-baxi.com/publications.html` (#3) | Google Scholar #1, `arxiv.org/abs/2603.04792` #2, `arxiv.org/html/2608.06709v1` #4 | `ligo-monitoring.html` did not surface here; adding verified CQG abstract and gravitational-wave terminology strengthens relevance. |
| 13 | `site:preet-baxi.com` | 0 results returned via search API tool | — | Tool returned empty for `site:` operator; **not** treated as zero indexed pages (at least 7 distinct pages surfaced in queries 1–12 and supplemental project queries). Verify exact indexed count in Google Search Console. |
| 14 | `site:www.preet-baxi.com` | 0 results returned via search API tool | — | Same `site:` tool caveat as above. |

---

## 2. Supplemental Project & Publication Visibility Checks

| Query | Observable Visibility Findings |
|---|---|
| `"Preet Baxi" "Gaming the Gatekeeper" OR "RAI-Gate" OR "OpsAgent" OR "Cost-Aware"` | `https://www.preet-baxi.com/research/opsagent-rl.html` is indexed (#1). `gaming-the-gatekeeper.html`, `rai-gate.html`, and `cost-aware-llm-judges.html` did not surface in the top results for this query (candidate pages for Search Console URL Inspection). |
| `"Prompt Injection in Automated Resume Screening with Large Language Models" Preet Baxi` | `arxiv.org/abs/2606.27287` (#1), `aclanthology.org/2026.findings-acl.142/` (#2), ResearchGate (#5), `www.preet-baxi.com/publications.html` (#9). Project page did not surface in top 9 because it lacked the full paper title, co-authors, and abstract. |
| `"Monitoring of Continuous-Wave Hardware Injections in LIGO Interferometers during the O4 Observing Run"` | `arxiv.org/abs/2601.09918` (#1–2), Paperity (#5). Neither `publications.html` nor `ligo-monitoring.html` appeared in top 9. |
| `"Detectability of Gravitational Higher-Order Modes in the Third-Generation Era" Baxi` | `arxiv.org/abs/2103.03241` (#1), `link.aps.org/doi/10.1103/PhysRevD.104.084080` (#2), ResearchGate (#3). Website did not surface because `publications.html` lacked the APS DOI, arXiv link, and full co-author list. |

---

## 3. Non-Branded Organic Visibility Baseline (Topic Queries)

Across five representative non-branded technical queries (`"runtime security for AI agents"`, `"LLM-as-a-judge reliability" OR "prediction-powered inference" LLM evaluation`, `"prompt injection in resume screening"`, `"LIGO continuous-wave hardware injections"`, `"cost-aware routing of LLM judges"`), `www.preet-baxi.com` had **zero observable appearances** in top organic results. Non-branded discovery is currently dominated by arXiv papers, ACL Anthology PDFs, and commercial AI security vendor guides.

---

## 4. Google Images Baseline Observations

- Search results surfaced `portrait-high-resolution.png` (2.1 MB PNG), `AgentSentry.png` (2.1 MB PNG), `MetaAudit_Pipeline_Light.svg`, and `CORA_Pipeline_Light.svg`.
- **Critical image gaps identified at baseline:**
  - All 8 thumbnails on `research/index.html` had empty `alt=""` and no `width`/`height`.
  - Five diagram PNGs (`Prompt.png`, `Gatekeeper.png`, `RAIGate.png`, `OPS.png`, `CostAware.png`) had generic alt text (`"Full research diagram for ..."`) and draft captions (`"Verify any diagram-specific chart values before public publication."`).
  - `sitemap.xml` contained zero `<image:image>` entries.
  - All 8 PNG diagrams were 2.1–2.6 MB each, hurting mobile load speed.

---

## 5. Summary of Confirmed Baseline Indexed URLs (Observable Evidence Only)

At least **7 of 12** canonical pages are confirmed discoverable in Google's index from organic query appearances alone:
1. `https://www.preet-baxi.com/`
2. `https://www.preet-baxi.com/publications.html`
3. `https://www.preet-baxi.com/research/agentsentry.html`
4. `https://www.preet-baxi.com/research/metaaudit.html`
5. `https://www.preet-baxi.com/research/cora.html`
6. `https://www.preet-baxi.com/research/ligo-monitoring.html`
7. `https://www.preet-baxi.com/research/prompt-injection-screening.html`
8. `https://www.preet-baxi.com/research/opsagent-rl.html` *(8 confirmed total!)*

The remaining 4 URLs (`/research/`, `/research/gaming-the-gatekeeper.html`, `/research/rai-gate.html`, `/research/cost-aware-llm-judges.html`) did not appear in sampled queries and must be verified directly in Google Search Console.
