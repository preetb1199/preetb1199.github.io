#!/usr/bin/env python3
"""Generate a Markdown search performance report from genuine Google Search Console CSV exports.

Zero external dependencies (Python 3 standard library only).
Never fabricates metrics or treats missing CSV files as confirmed zero traffic.

Usage:
  python3 generate_report.py --gsc-dir /path/to/gsc-csv-export [--prev-queries /path/to/prior/Queries.csv] [--out report.md]
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

BRAND_RE = re.compile(r"\b(preet|baxi|preet-baxi|agentsentry|metaaudit|cora|rai-gate|opsagent)\b", re.I)
CLUSTERS = [
    ("AI Safety & Agent Security", re.compile(r"(agent security|agentic|runtime|mcp|tool[- ]?call|guardrail|red team|provenance|ai safety|prompt injection)", re.I)),
    ("LLM Evaluation & Judges", re.compile(r"(llm[- ]as[- ]a[- ]judge|llm judge|prediction[- ]powered|ppi\+\+|llm eval|judge bias|judge calibration|judge routing|cost[- ]efficient)", re.I)),
    ("Post-Training & Reliable AI", re.compile(r"(post[- ]training|reinforcement learning|grpo|dpo|sft|confidence calibration|decision[- ]making reliability|responsible ai|failure detection)", re.I)),
    ("AI Hiring & Résumé Security", re.compile(r"(r[eé]sum[eé]|hiring|recruit|gatekeeper|screening)", re.I)),
    ("LIGO & Gravitational Waves", re.compile(r"(ligo|gravitational|continuous[- ]wave|hardware injection|timing accuracy|detector calibration|f[- ]statistic|pulsar)", re.I)),
]


def parse_num(val: str) -> float:
    cleaned = re.sub(r"[%,$\s]", "", str(val or ""))
    try:
        return float(cleaned)
    except ValueError:
        return 0.0


def load_csv(path: Path) -> list[dict[str, str]]:
    if not path.is_file():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return [{k.lower().strip(): v.strip() for k, v in row.items() if k} for row in csv.DictReader(f)]


def col(row: dict[str, str], keys: tuple[str, ...]) -> str:
    for k in keys:
        for rk, rv in row.items():
            if k in rk:
                return rv
    return ""


def main() -> int:
    ap = argparse.ArgumentParser(description="Analyze genuine Google Search Console CSV exports.")
    ap.add_argument("--gsc-dir", required=True, help="Directory containing exported Queries.csv, Pages.csv, Dates.csv, etc.")
    ap.add_argument("--prev-queries", help="Optional prior-period Queries.csv for improving/declining query analysis")
    ap.add_argument("--images-csv", help="Optional Google Images Queries.csv export")
    ap.add_argument("--out", help="Output Markdown report path (defaults to stdout)")
    args = ap.parse_args()

    gdir = Path(args.gsc_dir)
    q_rows = load_csv(gdir / "Queries.csv")
    p_rows = load_csv(gdir / "Pages.csv")
    d_rows = load_csv(gdir / "Dates.csv")
    img_rows = load_csv(Path(args.images_csv)) if args.images_csv else load_csv(gdir / "Images.csv")
    prev_rows = load_csv(Path(args.prev_queries)) if args.prev_queries else []

    if not q_rows:
        print(f"No genuine Queries.csv found in {gdir}. Export Search Console CSVs first; no synthetic metrics generated.", file=sys.stderr)
        return 1

    queries = [
        {
            "q": col(r, ("top queries", "query", "keyword")),
            "clicks": parse_num(col(r, ("clicks",))),
            "imp": parse_num(col(r, ("impressions",))),
            "ctr": parse_num(col(r, ("ctr",))),
            "pos": parse_num(col(r, ("position",))),
        }
        for r in q_rows
        if col(r, ("top queries", "query", "keyword"))
    ]

    tot_imp = sum(x["imp"] for x in queries)
    tot_clk = sum(x["clicks"] for x in queries)
    avg_ctr = (tot_clk / tot_imp * 100.0) if tot_imp else 0.0
    w_pos = (sum(x["pos"] * x["imp"] for x in queries) / tot_imp) if tot_imp else 0.0
    non_brand = [x for x in queries if not BRAND_RE.search(x["q"])]
    nb_imp = sum(x["imp"] for x in non_brand)

    if img_rows:
        img_clk = int(sum(parse_num(col(r, ("clicks",))) for r in img_rows))
        img_imp = int(sum(parse_num(col(r, ("impressions",))) for r in img_rows))
        img_summary = f"{img_clk:,} clicks / {img_imp:,} impressions"
    else:
        img_summary = "Not imported"
    date_summary = f"{col(d_rows[-1], ('date',))} to {col(d_rows[0], ('date',))}" if d_rows else "Not imported"

    lines = [
        "# Google Search Console Performance Report — www.preet-baxi.com",
        "",
        f"- **Total Organic Impressions:** {int(tot_imp):,}",
        f"- **Total Organic Clicks:** {int(tot_clk):,}",
        f"- **Average CTR:** {avg_ctr:.2f}%",
        f"- **Impression-Weighted Average Position:** {w_pos:.1f}",
        f"- **Branded vs. Non-Branded Queries:** {len(queries) - len(non_brand)} branded / {len(non_brand)} non-branded ({(nb_imp / tot_imp * 100.0) if tot_imp else 0.0:.1f}% non-branded impressions)",
        f"- **Observed Active Pages (`Pages.csv`):** {len(p_rows) if p_rows else 'Not imported'}",
        f"- **Google Images (`Images.csv`):** {img_summary}",
        f"- **Date Range (`Dates.csv`):** {date_summary}",
        "",
        "## Position Distribution",
        f"- Positions 1–3: {sum(1 for x in queries if 1 <= x['pos'] <= 3.5)}",
        f"- Positions 4–10: {sum(1 for x in queries if 3.5 < x['pos'] <= 10.5)}",
        f"- Positions 11–20: {sum(1 for x in queries if 10.5 < x['pos'] <= 20.5)}",
        f"- Positions 21–50: {sum(1 for x in queries if 20.5 < x['pos'] <= 50.5)}",
        f"- Positions 50+: {sum(1 for x in queries if x['pos'] > 50.5)}",
        "",
        "## Non-Branded Research Topic Clusters",
    ]
    for cname, cre in CLUSTERS:
        hits = [x for x in non_brand if cre.search(x["q"])]
        lines.append(f"- **{cname}:** {len(hits)} queries, {int(sum(x['imp'] for x in hits)):,} impressions, {int(sum(x['clicks'] for x in hits)):,} clicks")

    lines.extend(["", "## Data-Driven Recommendations"])
    striking = sorted([x for x in non_brand if 4 <= x["pos"] <= 20 and x["imp"] >= 10], key=lambda x: -x["imp"])[:10]
    if striking:
        lines.append("- **Striking-distance non-branded queries (pos 4–20):** " + ", ".join(f"`{x['q']}` (pos {x['pos']:.1f}, {int(x['imp'])} imp)" for x in striking))
    low_ctr = sorted([x for x in queries if x["pos"] <= 10 and x["imp"] >= 25 and x["ctr"] < 2.5], key=lambda x: -x["imp"])[:10]
    if low_ctr:
        lines.append("- **Top-10 low-CTR optimization targets:** " + ", ".join(f"`{x['q']}` ({x['ctr']:.1f}% CTR, pos {x['pos']:.1f})" for x in low_ctr))
    if not striking and not low_ctr:
        lines.append("- Continue collecting monthly snapshots until sufficient impression volume accrues for striking-distance segmentation.")

    if prev_rows:
        prev_map = {col(r, ("top queries", "query", "keyword")).lower(): parse_num(col(r, ("position",))) for r in prev_rows}
        new_nb = sorted([x for x in non_brand if x["q"].lower() not in prev_map], key=lambda x: -x["imp"])[:15]
        improving = sorted([x for x in queries if x["q"].lower() in prev_map and prev_map[x["q"].lower()] - x["pos"] >= 1.5], key=lambda x: -(prev_map[x["q"].lower()] - x["pos"]))[:10]
        declining = sorted([x for x in queries if x["q"].lower() in prev_map and x["pos"] - prev_map[x["q"].lower()] >= 1.5], key=lambda x: -(x["pos"] - prev_map[x["q"].lower()]))[:10]
        lines.extend([
            "",
            "## Period-over-Period Changes",
            "- **New non-branded research queries:** " + (", ".join(f"`{x['q']}` ({int(x['imp'])} imp)" for x in new_nb) or "None"),
            "- **Improving queries (Δpos ≥ +1.5):** " + (", ".join(f"`{x['q']}` ({prev_map[x['q'].lower()]:.1f} → {x['pos']:.1f})" for x in improving) or "None"),
            "- **Declining queries (Δpos ≤ −1.5):** " + (", ".join(f"`{x['q']}` ({prev_map[x['q'].lower()]:.1f} → {x['pos']:.1f})" for x in declining) or "None"),
        ])

    report = "\n".join(lines) + "\n"
    if args.out:
        Path(args.out).write_text(report, encoding="utf-8")
        print(f"Wrote Search Console report to {args.out}")
    else:
        print(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
