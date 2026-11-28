# Search Performance Monitoring Dashboard (`www.preet-baxi.com`)

Local, privacy-preserving monitoring suite for analyzing genuine **Google Search Console** exports without committing private analytics or credentials to this public repository.

## Option 1: Interactive Browser Dashboard (Zero Setup)
1. In Google Search Console (`https://search.google.com/search-console`), open **Performance → Search results**, select a date range (e.g., last 28 days or 3 months), and click **Export → Download CSV** (unzip to a local folder outside git, or inside `local-data/` which is `.gitignore`d).
2. Optional: Switch Search type to **Image** and export `Queries.csv` as `Images.csv`.
3. Open `index.html` in this folder directly in your browser and select the exported CSVs.
4. All parsing, cluster classification, position bucketing, trend charting, period-over-period diffing, and recommendation generation run locally in your browser.

## Option 2: CLI Markdown Report Generator
```bash
python3 generate_report.py \
  --gsc-dir /path/to/gsc-export-current \
  --prev-queries /path/to/gsc-export-previous/Queries.csv \
  --out /path/to/local-report.md
```

## Option 3: Read-Only GSC API Export (Optional)
Reuse `scripts/gsc_monitor.py` with a read-only Google Cloud Service Account JSON key stored **outside** this repository (never commit credentials; `.gitignore` blocks `*credentials*.json`, `*service-account*.json`, and `local-data/`).
