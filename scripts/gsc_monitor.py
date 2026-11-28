#!/usr/bin/env python3
"""Read-only Google Search Console Search Analytics exporter for www.preet-baxi.com.

Usage (requires authorized Google Cloud service account or OAuth token with
Search Console read-only scope `https://www.googleapis.com/auth/webmasters.readonly`):

    pip install google-api-python-client google-auth
    export GSC_PROPERTY="sc-domain:preet-baxi.com"   # or "https://www.preet-baxi.com/"
    export GOOGLE_APPLICATION_CREDENTIALS="/path/to/gsc-readonly-key.json"
    python3 scripts/gsc_monitor.py --days 28 --out seo-reports/gsc-snapshots

This script is strictly READ-ONLY. It does NOT call Google's Indexing API.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import os
import re
from pathlib import Path

BRAND_PATTERN = re.compile(r"\b(preet|baxi|preetb1199|preet-baxi)\b", re.IGNORECASE)


def fetch_search_analytics(service, site_url: str, start_date: str, end_date: str, dimensions: list[str], row_limit: int = 5000):
    body = {
        "startDate": start_date,
        "endDate": end_date,
        "dimensions": dimensions,
        "rowLimit": row_limit,
    }
    resp = service.searchanalytics().query(siteUrl=site_url, body=body).execute()
    return resp.get("rows", [])


def main() -> None:
    parser = argparse.ArgumentParser(description="Export read-only Google Search Console performance metrics.")
    parser.add_argument("--property", default=os.environ.get("GSC_PROPERTY", "sc-domain:preet-baxi.com"))
    parser.add_argument("--days", type=int, default=28)
    parser.add_argument("--out", default="seo-reports/gsc-snapshots")
    args = parser.parse_args()

    try:
        from google.oauth2 import service_account
        from googleapiclient.discovery import build
    except ImportError as exc:
        raise SystemExit(
            "Missing dependencies. Install with: pip install google-api-python-client google-auth"
        ) from exc

    cred_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    if not cred_path or not os.path.exists(cred_path):
        raise SystemExit(
            "Set GOOGLE_APPLICATION_CREDENTIALS to a valid Search Console read-only service-account JSON key."
        )

    creds = service_account.Credentials.from_service_account_file(
        cred_path,
        scopes=["https://www.googleapis.com/auth/webmasters.readonly"],
    )
    service = build("searchconsole", "v1", credentials=creds)

    end = dt.date.today() - dt.timedelta(days=3)
    start = end - dt.timedelta(days=args.days)
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    stamp = end.isoformat()

    # 1. Query + Page breakdown with branded vs non-branded classification
    qp_rows = fetch_search_analytics(service, args.property, start.isoformat(), end.isoformat(), ["query", "page"])
    qp_file = out_dir / f"queries-pages-{stamp}.csv"
    with qp_file.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["query", "segment", "page", "clicks", "impressions", "ctr", "position"])
        for r in qp_rows:
            q, p = r["keys"]
            seg = "branded" if BRAND_PATTERN.search(q) else "non_branded"
            w.writerow([q, seg, p, r["clicks"], r["impressions"], f"{r['ctr']:.4f}", f"{r['position']:.2f}"])

    # 2. Page-level summary
    page_rows = fetch_search_analytics(service, args.property, start.isoformat(), end.isoformat(), ["page"])
    page_file = out_dir / f"pages-{stamp}.csv"
    with page_file.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["page", "clicks", "impressions", "ctr", "position"])
        for r in page_rows:
            w.writerow([r["keys"][0], r["clicks"], r["impressions"], f"{r['ctr']:.4f}", f"{r['position']:.2f}"])

    print(f"Saved {len(qp_rows)} query-page rows to {qp_file}")
    print(f"Saved {len(page_rows)} page summary rows to {page_file}")


if __name__ == "__main__":
    main()
