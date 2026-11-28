#!/usr/bin/env python3
"""Submit genuinely updated canonical URLs to IndexNow (Bing, Yandex, Seznam, Naver).

IMPORTANT:
- IndexNow notifies Bing and other IndexNow-participating search engines.
- IndexNow does NOT notify Google Search (Google uses sitemaps & Search Console).
- Only submit URLs whose content has genuinely changed.
"""
import argparse
import json
import os
import subprocess
import sys
import urllib.error
import urllib.request

HOST = "www.preet-baxi.com"
BASE_URL = f"https://{HOST}"
KEY = "a8abb5d57579b82dc92f5ffc32629e0e"
KEY_FILE = f"{KEY}.txt"
KEY_LOCATION = f"{BASE_URL}/{KEY_FILE}"
ENDPOINT = "https://api.indexnow.org/indexnow"

FILE_TO_URL = {
    "index.html": f"{BASE_URL}/",
    "publications.html": f"{BASE_URL}/publications.html",
    "research/index.html": f"{BASE_URL}/research/",
    "research/agentsentry.html": f"{BASE_URL}/research/agentsentry.html",
    "research/metaaudit.html": f"{BASE_URL}/research/metaaudit.html",
    "research/cora.html": f"{BASE_URL}/research/cora.html",
    "research/ligo-monitoring.html": f"{BASE_URL}/research/ligo-monitoring.html",
    "research/prompt-injection-screening.html": f"{BASE_URL}/research/prompt-injection-screening.html",
    "research/gaming-the-gatekeeper.html": f"{BASE_URL}/research/gaming-the-gatekeeper.html",
    "research/rai-gate.html": f"{BASE_URL}/research/rai-gate.html",
    "research/opsagent-rl.html": f"{BASE_URL}/research/opsagent-rl.html",
    "research/cost-aware-llm-judges.html": f"{BASE_URL}/research/cost-aware-llm-judges.html",
}


def changed_urls_from_git(base_ref: str) -> list[str]:
    out = subprocess.check_output(
        ["git", "diff", "--name-only", base_ref, "HEAD"], text=True
    ).splitlines()
    return sorted({FILE_TO_URL[f] for f in out if f in FILE_TO_URL})


def verify_key_live() -> bool:
    req = urllib.request.Request(KEY_LOCATION, headers={"User-Agent": "IndexNowVerifier/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=12) as resp:
            body = resp.read().decode("utf-8").strip()
            return resp.status == 200 and body == KEY
    except Exception as exc:
        print(f"Key file verification failed ({KEY_LOCATION}): {exc}", file=sys.stderr)
        return False


def main() -> int:
    parser = argparse.ArgumentParser(description="Submit changed canonical URLs to IndexNow.")
    parser.add_argument("--from-git", metavar="REF", help="Collect changed HTML pages via git diff REF..HEAD")
    parser.add_argument("--urls", nargs="*", help="Explicit canonical URLs to submit")
    parser.add_argument("--dry-run", action="store_true", help="Print payload without sending HTTP POST")
    args = parser.parse_args()

    if not os.path.isfile(KEY_FILE) or open(KEY_FILE, encoding="utf-8").read().strip() != KEY:
        print(f"ERROR: Local IndexNow key file {KEY_FILE} is missing or mismatched.", file=sys.stderr)
        return 1

    urls: list[str] = []
    if args.from_git:
        urls.extend(changed_urls_from_git(args.from_git))
    if args.urls:
        for u in args.urls:
            if u not in FILE_TO_URL.values():
                print(f"Skipping non-canonical URL: {u}", file=sys.stderr)
                continue
            urls.append(u)
    urls = sorted(set(urls))

    if not urls:
        print("No genuinely updated canonical URLs to submit.")
        return 0

    payload = {
        "host": HOST,
        "key": KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": urls,
    }
    if args.dry_run:
        print(json.dumps(payload, indent=2))
        return 0

    if not verify_key_live():
        print("Aborting: live IndexNow key file is not yet accessible. Deploy main first.", file=sys.stderr)
        return 1

    req = urllib.request.Request(
        ENDPOINT,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            print(f"IndexNow submission accepted: HTTP {resp.status} for {len(urls)} URL(s).")
            return 0
    except urllib.error.HTTPError as err:
        print(f"IndexNow HTTP error {err.code}: {err.read().decode('utf-8', errors='replace')}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
