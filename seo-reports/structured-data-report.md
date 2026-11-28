# Structured Data & Researcher Identity Report

**Audit Date:** 2026-11-27  
**Branch:** `seo-optimization`  
**Validator:** `scripts/seo_audit.py` (JSON-LD syntax, consistent `@id`, factual schema typing)

---

## 1. Unified Researcher Identity (`#person`)

Every page across `https://www.preet-baxi.com/` now references the single canonical entity identifier:

```json
"@id": "https://www.preet-baxi.com/#person"
```

On `index.html`, this `#person` node declares verified identity attributes:
- **`name`**: `"Preet Baxi"`
- **`jobTitle`**: `"Ph.D. Researcher in Physics and Scientific Computing"`
- **`affiliation`**: `CollegeOrUniversity` — University of Michigan (`https://umich.edu/`)
- **`image`**: linked to `ImageObject` (`#portrait`, `1122×1402`)
- **`knowsAbout`**: 12 verified research areas across AI safety, agentic AI security, prompt injection, LLM-as-a-judge evaluation, PPI, post-training, RL for agents, gravitational-wave physics, LIGO continuous-wave hardware injections, and scientific computing.
- **`sameAs`** (6 verified, unambiguous official profiles):
  1. `https://scholar.google.com/citations?user=dpuZ0_IAAAAJ`
  2. `https://github.com/preetb1199`
  3. `https://www.linkedin.com/in/preet-baxi/`
  4. `https://lsa.umich.edu/physics/people/graduate-students/preetb.html`
  5. `https://micde.umich.edu/member/preet-baxi/`
  6. `https://aclanthology.org/people/preet-baxi/`

> **ORCID Note:** Crossref metadata revealed two separate ORCIDs linked to Preet Baxi (`0009-0007-3653-9808` on CQG 2026 and `0000-0002-6726-1665` on PRD 2021). Neither was added to `sameAs` yet to avoid pointing search engines at an un-reconciled duplicate; once merged in ORCID settings, add the single primary ORCID URI to `index.html`'s `sameAs` array.

---

## 2. Page-by-Page Schema.org Matrix (Before vs. After)

| Page | Before (`@type`) | After (`@graph` `@type`s) | Key Improvements |
|---|---|---|---|
| `/` | `Person`, `WebSite` | `ProfilePage`, `Person`, `ImageObject`, `WebSite` | Added `ProfilePage` (`mainEntity: #person`), U-M affiliation, `knowsAbout`, 3 additional verified academic `sameAs` URLs, and portrait `ImageObject`. |
| `/publications.html` | `CollectionPage`, `BreadcrumbList` | `CollectionPage`, `ItemList`, `Person`, 3× `ScholarlyArticle`, `CreativeWork`, `BreadcrumbList` | Added verified `ScholarlyArticle` nodes for ACL 2026, CQG 2026, and PRD 2021 with full co-authors, exact DOIs, `datePublished`, volume/issue/pages, and arXiv `sameAs`, plus `CreativeWork` for the 2026 preprint under review. |
| `/research/` | `CollectionPage`, `BreadcrumbList` | `CollectionPage`, `ItemList`, `Person`, `BreadcrumbList` | Added `ItemList` enumerating all 9 canonical research pages. |
| `/research/agentsentry.html` | 2 separate blocks: `CreativeWork`, `BreadcrumbList` | Unified `@graph`: `TechArticle`, `Person`, `ImageObject`, `BreadcrumbList` | Linked `author` to `#person`, added `ImageObject` (`1672×941`) and research keywords. |
| `/research/metaaudit.html` | 2 separate blocks: **`ScholarlyArticle`** *(inaccurate)*, `BreadcrumbList` | Unified `@graph`: **`TechArticle`**, `Person`, `ImageObject`, `BreadcrumbList` | **Fixed factual inaccuracy:** unpublished independent study is no longer marked `ScholarlyArticle`. |
| `/research/cora.html` | 2 separate blocks: `CreativeWork`, `BreadcrumbList` | Unified `@graph`: `TechArticle`, `Person`, `ImageObject`, `BreadcrumbList` | Unified graph, linked `#person`, added `ImageObject` (`1200×630`). |
| `/research/prompt-injection-screening.html` | `CreativeWork`, `BreadcrumbList` | Unified `@graph`: `TechArticle`, `ScholarlyArticle` (`#acl2026`), `Person`, `ImageObject`, `BreadcrumbList` | Connects portfolio explainer page (`TechArticle`) via `about` to the verified peer-reviewed ACL 2026 `ScholarlyArticle` with DOI and arXiv. |
| `/research/ligo-monitoring.html` | `CreativeWork`, `BreadcrumbList` | Unified `@graph`: `TechArticle`, `ScholarlyArticle` (`#cqg2026`), `Person`, `BreadcrumbList` | Connects project page (`TechArticle`) via `about` to the verified CQG 2026 `ScholarlyArticle` (`43(13) 135019`, DOI `10.1088/1361-6382/ae7adb`, arXiv `2601.09918`). |
| `/research/gaming-the-gatekeeper.html` | `CreativeWork`, `BreadcrumbList` | Unified `@graph`: `TechArticle`, `Person`, `ImageObject`, `BreadcrumbList` | Added `creativeWorkStatus: "Research in progress"`, `ImageObject`, `#person` link. |
| `/research/rai-gate.html` | `CreativeWork`, `BreadcrumbList` | Unified `@graph`: `TechArticle`, `Person`, `ImageObject`, `BreadcrumbList` | Added `creativeWorkStatus: "Research in progress"`, `ImageObject`, `#person` link. |
| `/research/opsagent-rl.html` | `CreativeWork`, `BreadcrumbList` | Unified `@graph`: `TechArticle`, `Person`, `ImageObject`, `BreadcrumbList` | Added `creativeWorkStatus: "Research in progress"`, `ImageObject`, `#person` link. |
| `/research/cost-aware-llm-judges.html` | `CreativeWork`, `BreadcrumbList` | Unified `@graph`: `TechArticle`, `Person`, `ImageObject`, `BreadcrumbList` | Added `creativeWorkStatus: "Collaborative research · under review"`, `ImageObject`, `#person` link. |

---

## 3. Validation Status

- **Automated JSON-LD syntax & rule validation:** Verified via `scripts/seo_audit.py` (all 12 pages pass JSON parsing, `#person` `@id` consistency, and non-misrepresentation checks).
- **Recommended post-deployment live check:** Run key URLs (`/`, `/publications.html`, `/research/agentsentry.html`, `/research/prompt-injection-screening.html`, `/research/ligo-monitoring.html`) through Google's Rich Results Test (`https://search.google.com/test/rich-results`) and Schema Markup Validator (`https://validator.schema.org/`) after merging to `main`.
