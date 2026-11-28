# GitHub Discoverability Audit & Copy-Paste Optimization Kit

**Audit Date:** 2026-11-27  
**GitHub Account:** `https://github.com/preetb1199`  
**Canonical Website:** `https://www.preet-baxi.com/`

---

## 1. Permissions & Implementation Status Summary

The connected GitHub App integration token in this environment is scoped strictly to **`preetb1199/preetb1199.github.io`**.

| Target | Access Level in This Environment | Status | Required Permissions to Automate |
|---|---|---|---|
| **`preetb1199/preetb1199.github.io`** | Full push + metadata/topics (`200 OK`) | **Implemented & deployed** (description, homepage, topics, upgraded `README.md`) | Already granted |
| **`preetb1199/Prompt_Injection_ACL26`** | Read-only (`HTTP 403 Resource not accessible by integration` on PATCH/PUT) | **Copy-paste kit ready below** (Priority 1) | Attach repo to project with `Contents: Read & Write` + `Administration/Metadata: Write`, OR apply via your signed-in GitHub web/CLI session |
| **`preetb1199/CalculateSNRg_Python`** | Read-only (`HTTP 403`) | **Copy-paste kit ready below** (Priority 2) | Same as above |
| **`preetb1199/AHD4Inventory`** (fork of `YyyyyyiZ/AHD4Inventory`) | Read-only (`HTTP 403`) | **Audit & copy-paste metadata below** (Priority 3) | Same as above |
| **`preetb1199/SolverMineSweeper`** (fork of `CLiao29/SolverMineSweeper`) | Read-only (`HTTP 403`) | **Audit recommendation below** (Non-research coursework fork; keep unpinned) | None needed |
| **GitHub User Profile (`preetb1199`)** | Read-only (`HTTP 403` on `PATCH /user`) | **Copy-paste profile + Profile README (`preetb1199/preetb1199`) ready below** | Signed-in GitHub web session (`github.com/settings/profile`) or classic PAT / `gh auth login` with `user` + `public_repo` scopes |

---

## 2. Full Public Repository Audit Table

| Repository | Type | Language | Stars | Current Gaps Found | Priority |
|---|---|---|---:|---|---|
| **`preetb1199.github.io`** | Original | HTML | 0 | Previously had leftover ChatGPT draft checklist in `README.md` & generic metadata — **now fixed & deployed** | **Done** |
| **`Prompt_Injection_ACL26`** | Original | Python | 2 | `homepage: null`, `topics: []`, README still contains placeholder `"add the final paper citation here"` + draft `"GitHub upload notes"`, missing ACL Anthology URL, DOI `10.18653/v1/2026.findings-acl.142`, `arXiv:2606.27287`, `CITATION.cff`, and link to `https://www.preet-baxi.com/research/prompt-injection-screening.html` | **P1 (Highest)** |
| **`CalculateSNRg_Python`** | Original | Python | 0 | `homepage: null`, `topics: []`, 2-line README with no LIGO/continuous-wave context, dependencies (`numpy`, `scipy`, `matplotlib`), parameter/usage docs, or link to `https://www.preet-baxi.com/research/ligo-monitoring.html` & `/publications.html` | **P2 (High)** |
| **`AHD4Inventory`** | Fork (`YyyyyyiZ/AHD4Inventory`) | Python | 0 | `description: null`, `homepage: null`, `topics: []`; upstream collaborator repo (Evolution of Heuristics with LLMs for inventory control; commits by Parshan Pakiman). Add concise description/topics only if keeping public; do not overwrite upstream code | **P3 (Optional)** |
| **`SolverMineSweeper`** | Fork (`CLiao29/SolverMineSweeper`) | C++/CUDA | 0 | `description: null`, `topics: []`; 2023 CMU 15-418 coursework fork. Keep **unpinned** so AI safety & LIGO research repos dominate your profile | **P4 (Low)** |
| **`preetb1199/preetb1199`** | *Does not exist yet* | Markdown | — | Missing GitHub Profile README — highest-visibility landing surface on `https://github.com/preetb1199` | **P1 (High)** |

---

## 3. GitHub Profile Optimization (`https://github.com/settings/profile`)

### Profile Fields (Copy-Paste)
- **Bio:**
  ```text
  PhD Candidate in Physics & Scientific Computing @ University of Michigan | AI Safety, Agentic Security, LLM Evaluation & LIGO Gravitational Waves
  ```
- **Website (Blog):** *(currently missing `https://`)*
  ```text
  https://www.preet-baxi.com/
  ```
- **Company:** `University of Michigan, Ann Arbor` *(already set)*
- **Location:** `Ann Arbor, MI, USA` *(already set)*
- **Social Accounts (optional under Profile Settings):**
  - `https://scholar.google.com/citations?user=dpuZ0_IAAAAJ`
  - `https://www.linkedin.com/in/preet-baxi/`
  - `https://aclanthology.org/people/preet-baxi/`
- **Pinned Repositories (Pin these 3 in order on `https://github.com/preetb1199`):**
  1. `Prompt_Injection_ACL26`
  2. `CalculateSNRg_Python`
  3. `preetb1199.github.io`
  *(Leave `SolverMineSweeper` unpinned.)*

### Optional High-Impact Addition: GitHub Profile README (`preetb1199/preetb1199`)
Create a public repository named **`preetb1199`** with a `README.md` containing:

```markdown
# Hi, I'm Preet Baxi

PhD Candidate in Physics and Scientific Computing at the **University of Michigan, Ann Arbor**.  
I research **AI safety**, **runtime security for agentic AI systems**, **indirect prompt injection**, **statistically valid LLM-as-a-judge evaluation**, and **gravitational-wave data analysis** with the **LIGO Scientific Collaboration**.

🌐 **Website:** [www.preet-baxi.com](https://www.preet-baxi.com/) · 📚 **Publications:** [preet-baxi.com/publications.html](https://www.preet-baxi.com/publications.html) · 🎓 [Google Scholar](https://scholar.google.com/citations?user=dpuZ0_IAAAAJ) · 📄 [ACL Anthology](https://aclanthology.org/people/preet-baxi/) · 💼 [LinkedIn](https://www.linkedin.com/in/preet-baxi/)

---

### Research Focus & Featured Projects

- **Agentic AI & Runtime Security:** [AgentSentry](https://www.preet-baxi.com/research/agentsentry.html) (fail-closed policy enforcement & provenance taint tracking for tool-using AI agents) · [RAI-Gate](https://www.preet-baxi.com/research/rai-gate.html) (SFT/DPO safety post-training & release gates) · [OpsAgent-RL](https://www.preet-baxi.com/research/opsagent-rl.html) (verifiable-reward RL for tool-using agents)
- **Indirect Prompt Injection:** [Prompt Injection in LLM Résumé Screening (Findings of ACL 2026)](https://www.preet-baxi.com/research/prompt-injection-screening.html) ([Code: `Prompt_Injection_ACL26`](https://github.com/preetb1199/Prompt_Injection_ACL26)) · [Gaming the Gatekeeper](https://www.preet-baxi.com/research/gaming-the-gatekeeper.html)
- **LLM Evaluation & Statistical Reliability:** [MetaAudit](https://www.preet-baxi.com/research/metaaudit.html) (auditing LLM judges via PPI++) · [CORA](https://www.preet-baxi.com/research/cora.html) (calibration & failure detection under input corruption) · [Cost-Aware LLM Judges](https://www.preet-baxi.com/research/cost-aware-llm-judges.html)
- **Gravitational-Wave Physics (LIGO):** [O4 Continuous-Wave Hardware Injection Monitoring (CQG 2026)](https://www.preet-baxi.com/research/ligo-monitoring.html) · [Grouped Semi-Coherent CW SNR Tool (`CalculateSNRg_Python`)](https://github.com/preetb1199/CalculateSNRg_Python)

### Selected Publications

- **Findings of ACL 2026:** P. Baxi, J. Xu, J. Y. Jiang, S. Jasin — *Prompt Injection Attacks in Automated Résumé Screening with Large Language Models* ([ACL Anthology](https://aclanthology.org/2026.findings-acl.142/) · [DOI](https://doi.org/10.18653/v1/2026.findings-acl.142) · [arXiv:2606.27287](https://arxiv.org/abs/2606.27287))
- **Classical and Quantum Gravity (2026):** P. Baxi, J. Leviton, E. Morag, M. Pitkin, K. Riles — *Monitoring of continuous-wave hardware injections during LIGO's fourth observing run* ([DOI](https://doi.org/10.1088/1361-6382/ae7adb) · [arXiv:2601.09918](https://arxiv.org/abs/2601.09918))
- **Physical Review D (2021):** Divyajyoti, P. Baxi, C. K. Mishra, K. G. Arun — *Detectability of gravitational higher modes in the third-generation detectors* ([DOI](https://doi.org/10.1103/PhysRevD.104.084080) · [arXiv:2103.03241](https://arxiv.org/abs/2103.03241))
```

---

## 4. Priority 1 Repository: `preetb1199/Prompt_Injection_ACL26`

### A. Repository Settings ("About" gear icon on GitHub)
- **Description:**
  ```text
  Official code and statistical analysis pipeline for Findings of ACL 2026: Prompt Injection Attacks in Automated Résumé Screening with Large Language Models
  ```
- **Website (Homepage):**
  ```text
  https://www.preet-baxi.com/research/prompt-injection-screening.html
  ```
- **Topics:**
  ```text
  ai-safety, prompt-injection, indirect-prompt-injection, llm-security, llm-evaluation, acl-2026, resume-screening, red-teaming
  ```

### B. Copy-Paste `CITATION.cff` (Add at repo root — enables GitHub's built-in "Cite this repository" widget!)
```yaml
cff-version: 1.2.0
message: "If you use this code or analysis pipeline in your research, please cite the Findings of ACL 2026 paper below."
title: "Prompt Injection Attacks in Automated Résumé Screening with Large Language Models"
type: software
authors:
  - family-names: "Baxi"
    given-names: "Preet"
    affiliation: "University of Michigan, Ann Arbor"
    website: "https://www.preet-baxi.com/"
  - family-names: "Xu"
    given-names: "Jiannan"
  - family-names: "Jiang"
    given-names: "Jane Yi"
  - family-names: "Jasin"
    given-names: "Stefanus"
repository-code: "https://github.com/preetb1199/Prompt_Injection_ACL26"
url: "https://www.preet-baxi.com/research/prompt-injection-screening.html"
keywords:
  - ai-safety
  - prompt-injection
  - indirect-prompt-injection
  - llm-security
  - llm-evaluation
  - resume-screening
preferred-citation:
  type: conference-paper
  title: "Prompt Injection Attacks in Automated Résumé Screening with Large Language Models"
  authors:
    - family-names: "Baxi"
      given-names: "Preet"
    - family-names: "Xu"
      given-names: "Jiannan"
    - family-names: "Jiang"
      given-names: "Jane Yi"
    - family-names: "Jasin"
      given-names: "Stefanus"
  collection-title: "Findings of the Association for Computational Linguistics: ACL 2026"
  year: 2026
  month: 7
  start: 2942
  end: 2953
  doi: "10.18653/v1/2026.findings-acl.142"
  url: "https://aclanthology.org/2026.findings-acl.142/"
```

### C. Copy-Paste Upgraded `README.md` (Preserves 100% of existing code docs, removes draft placeholders, adds verified ACL 2026 citation & website links)
```markdown
# Prompt Injection Attacks in Automated Résumé Screening with Large Language Models (Findings of ACL 2026)

[![ACL Anthology](https://img.shields.io/badge/ACL%20Anthology-2026.findings--acl.142-blue)](https://aclanthology.org/2026.findings-acl.142/)
[![arXiv](https://img.shields.io/badge/arXiv-2606.27287-b31b1b.svg)](https://arxiv.org/abs/2606.27287)
[![DOI](https://img.shields.io/badge/DOI-10.18653%2Fv1%2F2026.findings--acl.142-green)](https://doi.org/10.18653/v1/2026.findings-acl.142)
[![Project Page](https://img.shields.io/badge/Project%20Page-preet--baxi.com-informational)](https://www.preet-baxi.com/research/prompt-injection-screening.html)

Official experiment, statistical analysis, and figure-generation code for our **Findings of ACL 2026** paper:

> **Prompt Injection Attacks in Automated Résumé Screening with Large Language Models**  
> [Preet Baxi](https://www.preet-baxi.com/), Jiannan Xu, Jane Yi Jiang, Stefanus Jasin  
> *Findings of the Association for Computational Linguistics: ACL 2026*, pp. 2942–2953 (San Diego, July 2026)  
> **Links:** [Project Page](https://www.preet-baxi.com/research/prompt-injection-screening.html) · [ACL Anthology](https://aclanthology.org/2026.findings-acl.142/) · [arXiv:2606.27287](https://arxiv.org/abs/2606.27287) · [All Publications](https://www.preet-baxi.com/publications.html)

The codebase is organized so that **`USER_MAIN_ALL.py` is the single user-facing entry point** for running experiments. The remaining scripts handle experiment execution, rank remapping, aggregate analysis, Welch statistical testing, and paper figure generation.

---

## Repository structure

```text
.
├── USER_MAIN_ALL.py
├── LLM_RANKING_ALL.py
├── RANK_REMAPPING_ALL.py
├── COUNTER_STATS_ALL.py
├── WELCH_STATS_ALL.py
├── FIGURES_ALL.py
├── requirements.txt
├── README.md
├── DATA/
│   ├── REAL_JOB.txt
│   ├── HOMO_5.csv
│   ├── HOMO_10.csv
│   ├── HETERO_5_5_10_5.csv
│   └── UNIVERSAL_MAPPING_10.csv
├── PROMPT/
│   └── MAIN_JOB.txt
├── INJECTION/
│   ├── SP_DES.txt
│   └── SP_INSTR_HALF.txt
├── RESULTS/
└── FIGURES_FINAL/
```

---

## What each file does

### `USER_MAIN_ALL.py`
This is the **only file you need to edit** to launch a new experiment.

It defines the editable configuration block, including:
- job description setting
- résumé pool type
- injection type
- single vs multi-injection mode
- backend model
- number of rounds
- number of injected résumés
- optional parallelism limits

It validates the configuration and passes it into `run_llm_ranking(...)`.

### `LLM_RANKING_ALL.py`
This is the main experiment runner.

It:
- loads prompt templates, job description text, injection text, and résumé pools
- loads the universal candidate mapping from `DATA/UNIVERSAL_MAPPING_10.csv`
- builds no-injection and injection prompts for each round
- sends requests to the selected LLM backend
- runs calls in parallel using `ThreadPoolExecutor`
- limits simultaneous live API requests with a semaphore
- retries failed parsing / generation cases
- writes round-level **RAW** outputs to `RESULTS/.../*_RAW.csv`
- triggers rank remapping to generate corresponding summary outputs

### `RANK_REMAPPING_ALL.py`
This script converts RAW round-level results into résumé-level summary results.

It:
- parses round-wise candidate rankings
- normalizes candidate IDs
- completes partial rankings so each round still yields a strict full ranking
- remaps candidate ranks back to résumé IDs
- computes injected rank and rank gain columns
- writes `*_SUMMARY.csv`

### `COUNTER_STATS_ALL.py`
This script scans the `RESULTS/` directory and computes count-based summaries for each primary `*_SUMMARY.csv` file.

It writes:
- `COUNTER_POS_NEG_ZERO_<basename>.csv`
- `COUNTER_DISTRIBUTION_<basename>.csv`

These summarize how often injected ranks improved, worsened, or stayed unchanged.

### `WELCH_STATS_ALL.py`
This script scans the `RESULTS/` directory and computes descriptive statistics and Welch t-tests for each primary `*_SUMMARY.csv` file.

It writes:
- `WELCH_STATS_<basename>.csv`

The output includes:
- mean rank
- standard deviation
- Welch t-statistic
- Welch degrees of freedom
- two-sided p-value

### `FIGURES_ALL.py`
This script reads the summary/statistics outputs and generates the final paper figures.

It writes figures to `FIGURES_FINAL/` in both `.png` and `.pdf` format:
- `FIGURE_1_HOMO_5_MULTI`
- `FIGURE_2_HETERO_MULTI`
- `FIGURE_3_HOMO_5_SINGLE`
- `FIGURE_4_HETERO_SINGLE`
- `FIGURE_5_HOMO_10_SINGLE`
- `FIGURE_6_HOMO_10_MULTI`

---

## Installation

Create a fresh virtual environment and install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Required packages

```txt
numpy
pandas
matplotlib
scipy
requests
```

---

## How to run the code

### 1. Run a new experiment
Edit the configuration block at the top of `USER_MAIN_ALL.py`, set your API key locally (do not commit real API keys), then run:

```bash
python3 USER_MAIN_ALL.py
```

This validates the configuration, calls the selected LLM backend, saves RAW round-level outputs, and generates the corresponding SUMMARY file.

### 2. Generate counter statistics

```bash
python3 COUNTER_STATS_ALL.py
```

### 3. Generate Welch statistics

```bash
python3 WELCH_STATS_ALL.py
```

### 4. Generate all final figures

```bash
python3 FIGURES_ALL.py
```

---

## Configuration options in `USER_MAIN_ALL.py`

- `JOB_DES = "REAL_JOB"`
- `RES_TYPE = "HETERO_5_5_10_5", "HETERO_5_5_10_5_HQ", "HETERO_5_5_10_5_LQ", "HOMO_5", "HOMO_10"`
- `TYPE = "SP"`
- `INJ_TYPE = "DES", "INSTR_HALF"`
- `RUNS = "SINGLE", "MULTI"`
- `LLM_BACKEND = "CHATGPT", "DEEPSEEK"`

### Injection & pool rules
- `RUNS = "SINGLE"` requires `NUM_INJ_RES = 1`; `RUNS = "MULTI"` requires `NUM_INJ_RES >= 2`
- Heterogeneous pools: `SINGLE` uses `HETERO_5_5_10_5`; `MULTI` uses `HETERO_5_5_10_5_HQ` or `HETERO_5_5_10_5_LQ`
- Homogeneous pools: `HOMO_5` and `HOMO_10` can be used in both `SINGLE` and `MULTI`
- `NUM_ROUNDS` must not exceed the number of rows in `DATA/UNIVERSAL_MAPPING_10.csv`
- `TOTAL_RESUMES` must match the number of résumé columns expected by the mapping/data files
- Injection placement (`TOP` or `BOTTOM`) is randomized round by round

---

## Output naming convention

Primary experiment outputs:
- `RESULTS/<experiment_folder>/<backend>/<stem>_RAW.csv`
- `RESULTS/<experiment_folder>/<backend>/<stem>_SUMMARY.csv`

Example:
```text
RESULTS/SP_DES/CHATGPT/SP_DES_CHATGPT_HOMO_5_MULTI_5x_RAW.csv
RESULTS/SP_DES/CHATGPT/SP_DES_CHATGPT_HOMO_5_MULTI_5x_SUMMARY.csv
```

Downstream analysis outputs:
```text
COUNTER_POS_NEG_ZERO_<basename>.csv
COUNTER_DISTRIBUTION_<basename>.csv
WELCH_STATS_<basename>.csv
```

---

## Reproducibility & API key notes

- Candidate remapping is controlled through `DATA/UNIVERSAL_MAPPING_10.csv`
- Partial rankings are completed so each round yields a strict full ranking
- Retries and robust parsing reduce generation/parsing failures
- `USER_MAIN_ALL.py` uses `KEY = "Replace key here"` as a placeholder; supply your own key locally or via environment variables and never commit credentials

---

## Related Research

- **[Gaming the Gatekeeper](https://www.preet-baxi.com/research/gaming-the-gatekeeper.html)** — Adaptive attacks on LLM-based résumé screeners
- **[AgentSentry](https://www.preet-baxi.com/research/agentsentry.html)** — Runtime security and provenance taint tracking for tool-using AI agents
- **[MetaAudit](https://www.preet-baxi.com/research/metaaudit.html)** — Auditing LLM-as-a-judge reliability with prediction-powered inference (PPI++)

---

## Citation

If you use this codebase or findings in your research, please cite:

```bibtex
@inproceedings{baxi-etal-2026-prompt,
  title     = {Prompt Injection Attacks in Automated R{\'e}sum{\'e} Screening with Large Language Models},
  author    = {Baxi, Preet and Xu, Jiannan and Jiang, Jane Yi and Jasin, Stefanus},
  booktitle = {Findings of the Association for Computational Linguistics: ACL 2026},
  month     = jul,
  year      = {2026},
  address   = {San Diego, California, USA},
  publisher = {Association for Computational Linguistics},
  pages     = {2942--2953},
  doi       = {10.18653/v1/2026.findings-acl.142},
  url       = {https://aclanthology.org/2026.findings-acl.142/}
}
```
```

---

## 5. Priority 2 Repository: `preetb1199/CalculateSNRg_Python`

### A. Repository Settings ("About" gear icon on GitHub)
- **Description:**
  ```text
  Python implementation of a grouped semi-coherent continuous-wave gravitational-wave search method to compute SNRs, detection statistics, and template spacings (LIGO)
  ```
- **Website (Homepage):**
  ```text
  https://www.preet-baxi.com/research/ligo-monitoring.html
  ```
- **Topics:**
  ```text
  gravitational-waves, ligo, continuous-waves, astrophysics, signal-processing, scientific-computing, python
  ```

### B. Copy-Paste Upgraded `README.md` (Strictly grounded in `PY_Calculate_SNRG.py` & `SNRgModelParams.csv`)
```markdown
# CalculateSNRg_Python

[![Website](https://img.shields.io/badge/Research%20Page-preet--baxi.com-informational)](https://www.preet-baxi.com/research/ligo-monitoring.html)
[![Publications](https://img.shields.io/badge/Publications-LIGO%20%26%20GW-blue)](https://www.preet-baxi.com/publications.html)

Python implementation of a **grouped semi-coherent search method** for continuous-wave (CW) gravitational-wave signal analysis, computing grouped signal-to-noise ratios ($\mathrm{SNR}_g$), detection statistics, and frequency ($f_0$) / spin-down ($\dot{f}$) template spacings.

**Author:** [Preet Baxi](https://www.preet-baxi.com/) (University of Michigan, Ann Arbor · LIGO Scientific Collaboration)

---

## Overview

`PY_Calculate_SNRG.py` simulates continuous-wave signals in Gaussian noise spectrograms segmented by coherence time $T_{\mathrm{coh}}$ over an observation duration $T_{\mathrm{obs}}$, then evaluates grouped semi-coherent detection statistics for group sizes $M \le g \le N$:

- **`TS_model(a, g, Tobs, fdot)`** — Empirical template-spacing model parameterized by `SNRgModelParams.csv`
- **`h0rms(S, fIndex, Nseg, nBinSide)`** — Signal/noise RMS amplitude estimator across neighboring frequency bins
- **`gbar(g, Nseg)`** — Effective group-size helper
- **`noise_mean_DS` / `noise_std_DS` / `pred_signal_DS`** — Analytical noise mean, noise standard deviation, and predicted signal detection statistics
- **Template-spacing estimation** — Uses cubic spline interpolation (`scipy.interpolate.UnivariateSpline`) over $\Delta f_0$ or $\Delta \dot{f}$ sweeps to find the parameter step causing a 20% drop in $\mathrm{SNR}_g$, with optional matplotlib diagnostic plots and CSV exports

---

## Files

- `PY_Calculate_SNRG.py` — Main simulation, grouped semi-coherent SNR/detection-statistic calculation, spline template-spacing estimator, and plotting script
- `SNRgModelParams.csv` — Precomputed power-law parameter table used by `TS_model`

---

## Requirements & Usage

Requires Python 3 with `numpy`, `scipy`, and `matplotlib`:

```bash
pip install numpy scipy matplotlib
python3 PY_Calculate_SNRG.py
```

Key configuration flags at the top of `PY_Calculate_SNRG.py`:
- `TS`: Choose `'f'` (frequency sweep) or `'fdot'` (frequency derivative sweep)
- `M`, `N`, `Ntrial`: Group-size range and number of Monte Carlo noise trials
- `Tobs_hr`, `f_sig`, `fdot_sig`, `hamp`, `hnoise`, `fsamp`: Observation time, injected signal parameters, noise ASD, and sampling frequency
- `ParsevalSNR`, `PlotSNRvsParam`, `OutputFile1`–`OutputFile4`: Toggle Parseval-normalized SNR, diagnostic plots, and CSV output files

---

## Related Gravitational-Wave Research & Publications

- **[LIGO O4 Continuous-Wave Hardware Injection Monitoring](https://www.preet-baxi.com/research/ligo-monitoring.html)** — Research overview on `preet-baxi.com`
- **Classical and Quantum Gravity (2026):** P. Baxi, J. Leviton, E. Morag, M. Pitkin, K. Riles, *"Monitoring of continuous-wave hardware injections during LIGO's fourth observing run,"* CQG 43(13), 135019. [DOI](https://doi.org/10.1088/1361-6382/ae7adb) · [arXiv:2601.09918](https://arxiv.org/abs/2601.09918)
- **Physical Review D (2021):** Divyajyoti, P. Baxi, C. K. Mishra, K. G. Arun, *"Detectability of gravitational higher modes in the third-generation detectors,"* PRD 104(8), 084080. [DOI](https://doi.org/10.1103/PhysRevD.104.084080) · [arXiv:2103.03241](https://arxiv.org/abs/2103.03241)
- **Full Publications & Website:** [https://www.preet-baxi.com/publications.html](https://www.preet-baxi.com/publications.html)
```

---

## 6. Secondary Public Forks Audit (`AHD4Inventory` & `SolverMineSweeper`)

### `preetb1199/AHD4Inventory` (Fork of `YyyyyyiZ/AHD4Inventory`)
- **Finding:** Collaborator fork implementing Evolution of Heuristics (EoH) with LLMs for automated inventory policy design (MIT License; commits by Parshan Pakiman). Currently has empty `description`, `homepage`, and `topics`.
- **Recommendation (if kept public):** Add accurate metadata without altering upstream code:
  - **Description:** `Evolution of Heuristics (EoH) with LLMs for automated inventory-control policy design (fork of YyyyyyiZ/AHD4Inventory)`
  - **Topics:** `llm-optimization, evolutionary-computation, inventory-control, operations-research, heuristics`
  - **Homepage:** Link only if a public paper or project page exists for this work (e.g., `https://www.preet-baxi.com/publications.html` once published).

### `preetb1199/SolverMineSweeper` (Fork of `CLiao29/SolverMineSweeper`)
- **Finding:** 2023 fork of a CMU 15-418 parallel CUDA/OpenMP Minesweeper solver.
- **Recommendation:** Do **not** pin on your GitHub profile; optionally leave as-is or archive/remove if you want your public repository list focused exclusively on AI safety, LLM evaluation, and LIGO research.

---

## 7. Optional One-Shot Local `gh` CLI Commands (Run on Your Machine)

If you have `gh` signed in locally (`gh auth login` with `repo` and `user` scopes), you can apply all metadata, topics, and profile updates in seconds:

```bash
# 1. Update GitHub user profile bio & website
gh api -X PATCH user \
  -f bio="PhD Candidate in Physics & Scientific Computing @ University of Michigan | AI Safety, Agentic Security, LLM Evaluation & LIGO Gravitational Waves" \
  -f blog="https://www.preet-baxi.com/"

# 2. Update Prompt_Injection_ACL26 metadata & topics
gh api -X PATCH repos/preetb1199/Prompt_Injection_ACL26 \
  -f description="Official code and statistical analysis pipeline for Findings of ACL 2026: Prompt Injection Attacks in Automated Résumé Screening with Large Language Models" \
  -f homepage="https://www.preet-baxi.com/research/prompt-injection-screening.html"

gh api -X PUT repos/preetb1199/Prompt_Injection_ACL26/topics \
  -H "Accept: application/vnd.github+json" \
  -f 'names[]=ai-safety' -f 'names[]=prompt-injection' -f 'names[]=indirect-prompt-injection' \
  -f 'names[]=llm-security' -f 'names[]=llm-evaluation' -f 'names[]=acl-2026' \
  -f 'names[]=resume-screening' -f 'names[]=red-teaming'

# 3. Update CalculateSNRg_Python metadata & topics
gh api -X PATCH repos/preetb1199/CalculateSNRg_Python \
  -f description="Python implementation of a grouped semi-coherent continuous-wave gravitational-wave search method to compute SNRs, detection statistics, and template spacings (LIGO)" \
  -f homepage="https://www.preet-baxi.com/research/ligo-monitoring.html"

gh api -X PUT repos/preetb1199/CalculateSNRg_Python/topics \
  -H "Accept: application/vnd.github+json" \
  -f 'names[]=gravitational-waves' -f 'names[]=ligo' -f 'names[]=continuous-waves' \
  -f 'names[]=astrophysics' -f 'names[]=signal-processing' -f 'names[]=scientific-computing' \
  -f 'names[]=python'
```
