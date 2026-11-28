# New Substantial Research Resources — Prepared for Review (Task 4)

**Git Branch:** `research-authority-expansion` (pushed to `origin/research-authority-expansion`; **NOT merged into `main`** per your review requirement)  
**Design & Scientific Integrity:** Uses the website's existing stylesheet (`assets/styles.css`), dark/light theme toggle, canonical metadata, unified `#person` JSON-LD, existing verified scientific SVG diagrams, and strictly verified data/references—zero fabricated metrics and zero thin SEO filler.

---

## Five Prepared Deep-Dive Technical Guides

| # | Branch File Path | Planned Canonical URL (Upon Approval) | Primary Non-Branded Queries Targeted | Verified Research Artifacts & Figures Used |
|---|---|---|---|---|
| **1** | `research/guides/runtime-security-tool-using-ai-agents.html` | `https://www.preet-baxi.com/research/guides/runtime-security-tool-using-ai-agents.html` | `runtime agent security`, `MCP security`, `tool-calling security`, `agent provenance tracking`, `conformal calibration for AI agent security` | AgentSentry core study (`34/34` exploits, `0/120` vs `120/120` unseen-server false alarms, `99.7%` clean utility, conformal order-statistic formula), v3 adaptive `payload_split` (`28.1%` ASR) & threshold interaction (`~0.962` vs `~0.9`), `AgentSentry_Research_Overview.svg`, `AgentSentry_Provenance_Light.svg`, `AgentSentry_Results_Light.svg` |
| **2** | `research/guides/indirect-prompt-injection-agentic-ai.html` | `https://www.preet-baxi.com/research/guides/indirect-prompt-injection-agentic-ai.html` | `indirect prompt injection`, `prompt injection defense`, `prompt injection in résumé screening`, `multi-attacker prompt injection dynamics`, `automated résumé screening vulnerabilities` | Findings of ACL 2026 (`10.18653/v1/2026.findings-acl.142`, `arXiv:2606.27287`, `93.2%` DeepSeek-V3.2 / `45.6%` GPT-4o-mini single-attacker, multi-attacker collapse, heterogeneous fairness inversions), `Prompt_Injection_ACL26` pipeline, MetaAudit spotlighting (`13.9% → 4.9%`), `Prompt.webp`/`Prompt.png` |
| **3** | `research/guides/statistical-bias-llm-as-a-judge-ppi.html` | `https://www.preet-baxi.com/research/guides/statistical-bias-llm-as-a-judge-ppi.html` | `LLM-as-a-judge reliability`, `LLM judge bias`, `prediction-powered inference`, `statistical LLM evaluation`, `LLM judge auditing`, `Edgeworth confidence intervals for LLM evaluation` | MetaAudit HelpSteer2 bias (`9.2%` vs `17.5%`), length-sliced misses (`86%` vs `41%`), PPI++ estimator equations & `λ` power tuning, subjective (`1.27×–1.29×`) vs verifiable math (`3.80×–4.7×`) multipliers, Edgeworth certification (`12.2% → 9.2%` false accepts, `0.86` vs `0.80` power), negative active-sampling result (`0.82×`), `MetaAudit_Pipeline_Light.svg`, `MetaAudit_PPI_Correction_Light.svg`, `MetaAudit_Certification_Light.svg` |
| **4** | `research/guides/ligo-continuous-wave-hardware-injections.html` | `https://www.preet-baxi.com/research/guides/ligo-continuous-wave-hardware-injections.html` | `continuous-wave hardware injection monitoring`, `LIGO hardware injections`, `LIGO signal validation`, `LIGO timing accuracy`, `continuous-wave signal processing` | CQG 2026 (`10.1088/1361-6382/ae7adb`, `arXiv:2601.09918`), 18 CW injections (`12–2,991 Hz`), 1,800-s Fourier segments, phase preservation across $10^{11}$ cycles, matched filter (~44% lower amplitude uncertainty, `3–6 μs` timing) vs frequentist $\mathcal{F}$-statistic vs Bayesian reconstruction, `CalculateSNRg_Python` (`TS_model`, `UnivariateSpline` 20% SNR-drop template spacing) |
| **5** | `research/guides/confidence-calibration-failure-detection-llm-agents.html` | `https://www.preet-baxi.com/research/guides/confidence-calibration-failure-detection-llm-agents.html` | `agent confidence calibration`, `AI decision-making reliability`, `ECE vs AUROC under input corruption`, `out-of-distribution failure detection in LLM agents` | CORA controlled-equity + freight-transfer study (`847,838` API calls, 7 corruption families, `ΔAUROC −0.095` vs pooled `ΔECE 0.000`, silent staleness `AUROC 0.500`, verbal vs token elicitation, GBM detector `0.428` OOD failure, `−3.35 pp` gating penalty), `CORA_Split_Light.svg`, `CORA_Discrimination_Light.svg`, `CORA_Detectors_Light.svg` |

---

## Review & Publication Checklist (When Ready)
1. Inspect the 5 HTML files on branch `research-authority-expansion` (either locally or via GitHub PR diff).
2. Confirm you are comfortable publishing each technical guide at `/research/guides/<slug>.html` (or selectively cherry-pick the ones you want first — **Guide #4 (LIGO)** and **Guide #2 (ACL 2026 Indirect Prompt Injection)** are backed by already peer-reviewed 2026 papers and can ship immediately!).
3. Upon merging selected guides into `main`:
   - Link them from `research/index.html` and their parent project pages,
   - Add their URLs to `sitemap.xml` and `scripts/seo_audit.py` (`EXPECTED_PAGES`),
   - Notify Bing/IndexNow via `python3 scripts/indexnow_submit.py --from-git HEAD~1` and inspect in Google Search Console.
