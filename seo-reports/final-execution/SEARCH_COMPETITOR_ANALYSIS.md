# Non-Branded Search Competitor Analysis

**Audit Date:** 2026-11-28  
**Methodology:** Live Google SERP analysis across 5 research clusters (48+ core non-branded queries + 12 long-tail research queries). All observations reflect live search results; no search volumes, difficulty scores, or traffic estimates are fabricated.

---

## 1. Competitive Landscape by Research Cluster

### Cluster 1: AI Safety & Agentic Runtime Security
- **Observed Competitors:** Enterprise security vendors (`Sweet Security`, `CodeIntegrity`, `CrowdStrike`, `Palo Alto Unit 42`, `Trussed.ai`), official docs (`Microsoft Learn`, `OWASP GenAI`), specialist practitioner newsletters (`Software Analyst Substack`, `Christian Schneider`, `AgentKeeper`, `Gus Aragón`), and arXiv papers (`arXiv:2508.12538` MCPLib, `arXiv:2406.13352` AgentDojo).
- **Structural Content Gap:** Vendor articles focus on conceptual architecture checklists and rarely report controlled clean-task utility, out-of-distribution unseen-server false alarms, or adaptive failure modes where their own defense breaks.
- **`preet-baxi.com` Competitive Edge:** `agentsentry.html` presents concrete empirical evidence—`0/120` unseen-server false alarms vs. `120/120` for TF-IDF, `99.7%` preserved clean-task utility, AND honest disclosure of the v3 adaptive `payload_split` failure (`28.1%` undefended ASR) and conformal threshold interaction (`~0.962` vs `~0.9`). Few competing pages combine runtime provenance theory with transparent failure analysis.

### Cluster 2: LLM-as-a-Judge & Statistical Evaluation
- **Observed Competitors:** Major ML tooling docs (`MLflow` Oct 2026 LLM Judge Calibration guide, `Deepchecks`, `DataFramer`), foundational arXiv/ACL/OpenReview papers (`arXiv:2506.22316`, `arXiv:2506.13639`, `arXiv:2606.19544`, `aclanthology.org/2025.ijcnlp-long.18`, `openreview.net/forum?id=6xRIf7H6Nb`), and developer blogs (`Medium`, `GitConnected`).
- **Structural Content Gap:** Academic papers are dense static PDFs while vendor guides treat calibration informally without finite-sample statistical bounds, Edgeworth skewness corrections, or empirical comparisons of subjective vs. verifiable-task label savings.
- **`preet-baxi.com` Competitive Edge:** `metaaudit.html` offers an interactive PPI++ explainer backed by empirical numbers (`9.2%` judge-only vs. `17.5%` human consensus defect rate on HelpSteer2; `1.27×–1.29×` subjective vs. `3.80×–4.7×` verifiable math multipliers; `12.2% → 9.2%` certification false accepts with Edgeworth correction; adversarial spotlighting `13.9% → 4.9%`).

### Cluster 3: Post-Training, Agentic RL & Decision Reliability
- **Observed Competitors:** Broad arXiv surveys (`arXiv:2407.16216`, `arXiv:2507.21931`), recent calibration preprints (`arXiv:2601.15778` Agentic Confidence Calibration), academic lab pages (`Ling Huang`, `Haipeng Chen`), and Medium explainers.
- **Structural Content Gap:** Few resources empirically test whether probability calibration (ECE) and ranking discrimination (AUROC) diverge under silent data corruption—or whether out-of-distribution failure detector gating actually improves downstream policy returns.
- **`preet-baxi.com` Competitive Edge:** `cora.html` directly answers this gap with 847,838 recorded API calls across 7 corruption families (`ΔAUROC −0.095` while pooled `ΔECE = 0.000`, GBM detector OOD failure at `0.428` AUROC, and `−3.35 pp` downstream gating penalty). For `rai-gate.html` and `opsagent-rl.html`, realistic non-branded competitiveness will unlock once empirical checkpoint results and code are published.

### Cluster 4: AI Hiring & Résumé Screening Security
- **Observed Competitors:** `USENIX Security 2026` (`arXiv:2605.28999`, Zhang et al.), `arXiv:2512.20164`, `ACL Anthology` (including Preet's own `2026.findings-acl.142` and ACL Industry RAPIDS), and ResearchGate mirrors.
- **Structural Content Gap:** Almost all competing results are raw PDFs or abstract stubs without accessible explanations of multi-attacker equilibrium collapse or reproducible statistical code walkthroughs.
- **`preet-baxi.com` Competitive Edge:** As **first author of a peer-reviewed Findings of ACL 2026 paper** with an open reproducibility repository (`Prompt_Injection_ACL26`), `prompt-injection-screening.html` has one of the strongest near-term non-branded ranking opportunities on the entire site.

### Cluster 5: LIGO & Continuous Gravitational Waves
- **Observed Competitors:** `ligo.caltech.edu`, `arXiv` (`1211.0021`, `2508.20073`, `2601.09918`), `IOPscience` (paywalled CQG 2026), `LIGO DCC` (e.g., 2009 `G0900519` timing poster), `Cardiff ORCA`, and `Universe Today`.
- **Structural Content Gap:** For broad head terms (`LIGO`), institutional observatory domains are unassailable. However, for **continuous-wave hardware injections**, **O4 signal validation**, **LIGO timing accuracy**, and **grouped semi-coherent CW SNR calculations**, almost no modern, open-access, readable web guides exist outside paywalled journals and 15-year-old PDFs.
- **`preet-baxi.com` Competitive Edge:** **Highest immediate non-branded ranking opportunity across the entire website.** `ligo-monitoring.html` (backed by first-author CQG 2026 DOI `10.1088/1361-6382/ae7adb` + `CalculateSNRg_Python`) can realistically earn top visibility for specialized gravitational-wave instrumentation and CW data-analysis queries.

---

## 2. Strategic Positioning Takeaway

Compete on **specificity, empirical rigor, interactive transparency, and honest negative results**—not on broad head terms (`LIGO`, `AI safety`, `LLM evaluation`) dominated by Wikipedia, Caltech, Microsoft, and commercial SaaS platforms. The 5 draft deep-dive guides prepared on branch `research-authority-expansion` specifically target the highest-opportunity, lowest-noise technical queries identified above.
