# Preet Baxi — Academic Research Website

Source repository for **[www.preet-baxi.com](https://www.preet-baxi.com/)**, the personal academic website of **Preet Baxi**, PhD Candidate in Physics and Scientific Computing at the **University of Michigan, Ann Arbor**.

**Research Focus:** AI Safety · Agentic AI & Runtime Security · Indirect Prompt Injection · Statistically Valid LLM Evaluation · Gravitational-Wave Physics (LIGO Scientific Collaboration)

---

## Featured Research Pages

### AI Safety, Agent Security & LLM Evaluation
- **[AgentSentry](https://www.preet-baxi.com/research/agentsentry.html)** — Runtime security for tool-using AI agents with fail-closed policy enforcement and provenance taint tracking
- **[MetaAudit](https://www.preet-baxi.com/research/metaaudit.html)** — Auditing LLM-as-a-judge reliability with human-grounded statistical inference (PPI++)
- **[CORA](https://www.preet-baxi.com/research/cora.html)** — Confidence calibration, ranking discrimination, and silent failure detection under input corruption in LLM decision agents
- **[Prompt Injection in LLM Résumé Screening (ACL 2026)](https://www.preet-baxi.com/research/prompt-injection-screening.html)** — Empirical study of indirect prompt injection in automated hiring pipelines ([Code: `Prompt_Injection_ACL26`](https://github.com/preetb1199/Prompt_Injection_ACL26))
- **[Gaming the Gatekeeper](https://www.preet-baxi.com/research/gaming-the-gatekeeper.html)** — Adaptive attacks and stress testing for LLM-based résumé screeners
- **[RAI-Gate](https://www.preet-baxi.com/research/rai-gate.html)** — Safety post-training (SFT/DPO) and quantitative release gating for responsible AI deployment
- **[OpsAgent-RL](https://www.preet-baxi.com/research/opsagent-rl.html)** — Verifiable-reward reinforcement learning for long-horizon tool-using operations agents
- **[Cost-Aware Routing of LLM Judges](https://www.preet-baxi.com/research/cost-aware-llm-judges.html)** — Sequential sampling and two-tier LLM verification under evaluation budgets

### Gravitational-Wave Physics & Scientific Computing
- **[LIGO O4 Continuous-Wave Hardware Injection Monitoring](https://www.preet-baxi.com/research/ligo-monitoring.html)** — Monitoring continuous-wave hardware injections during LIGO Observing Run 4 ([Related code: `CalculateSNRg_Python`](https://github.com/preetb1199/CalculateSNRg_Python))

---

## Selected Peer-Reviewed Publications

Full publication list, abstracts, and BibTeX citations are available at **[preet-baxi.com/publications.html](https://www.preet-baxi.com/publications.html)**.

- **Findings of ACL 2026:** P. Baxi, J. Xu, J. Y. Jiang, S. Jasin, *"Prompt Injection in Automated Résumé Screening with Large Language Models: Single and Multi-Injection Settings,"* Findings of the Association for Computational Linguistics: ACL 2026, pp. 2942–2953. [ACL Anthology](https://aclanthology.org/2026.findings-acl.142/) · [DOI](https://doi.org/10.18653/v1/2026.findings-acl.142) · [arXiv:2606.27287](https://arxiv.org/abs/2606.27287) · [Code](https://github.com/preetb1199/Prompt_Injection_ACL26)
- **Classical and Quantum Gravity (2026):** P. Baxi, J. Leviton, E. Morag, M. Pitkin, K. Riles, *"Monitoring of continuous-wave hardware injections in LIGO interferometers during the O4 observing run,"* Classical and Quantum Gravity 43(13), 135019. [DOI](https://doi.org/10.1088/1361-6382/ae7adb) · [arXiv:2601.09918](https://arxiv.org/abs/2601.09918)
- **Physical Review D (2021):** Divyajyoti, P. Baxi, C. K. Mishra, K. G. Arun, *"Detectability of gravitational higher order modes in the third-generation era,"* Physical Review D 104(8), 084080. [DOI](https://doi.org/10.1103/PhysRevD.104.084080) · [arXiv:2103.03241](https://arxiv.org/abs/2103.03241)

---

## Repository Structure & Automated Checks

- `index.html`, `publications.html`, `research/` — Static HTML pages deployed via GitHub Pages with custom domain `www.preet-baxi.com`
- `assets/` — Stylesheets, interactive explainer scripts, responsive WebP/PNG figures, and CV
- `scripts/seo_audit.py` — Automated technical SEO, structured data, image, canonical, and link regression checker (run in CI via `.github/workflows/seo-check.yml`)
- `scripts/gsc_monitor.py` — Read-only Google Search Console Search Analytics exporter

To run the local verification check:

```bash
python3 scripts/seo_audit.py
```

---

## Academic Profiles

- **Website:** https://www.preet-baxi.com/
- **Google Scholar:** https://scholar.google.com/citations?user=dpuZ0_IAAAAJ
- **ACL Anthology:** https://aclanthology.org/people/preet-baxi/
- **LinkedIn:** https://www.linkedin.com/in/preet-baxi/
- **University of Michigan (LSA Physics):** https://lsa.umich.edu/physics/people/graduate-students/preetb.html
- **University of Michigan (MICDE):** https://micde.umich.edu/member/preet-baxi/
