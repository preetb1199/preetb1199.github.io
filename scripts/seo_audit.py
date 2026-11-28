#!/usr/bin/env python3
"""Automated Technical SEO & Structured Data Regression Audit for www.preet-baxi.com.

Zero external dependencies (Python 3 standard library only).
Exit code 0 if all checks pass; non-zero on any SEO regression.
"""
from __future__ import annotations

import json
import os
import re
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
BASE_URL = "https://www.preet-baxi.com"
PERSON_ID = f"{BASE_URL}/#person"

EXPECTED_PAGES = {
    "index.html": f"{BASE_URL}/",
    "publications.html": f"{BASE_URL}/publications.html",
    "research/index.html": f"{BASE_URL}/research/",
    "research/agentsentry.html": f"{BASE_URL}/research/agentsentry.html",
    "research/cora.html": f"{BASE_URL}/research/cora.html",
    "research/cost-aware-llm-judges.html": f"{BASE_URL}/research/cost-aware-llm-judges.html",
    "research/gaming-the-gatekeeper.html": f"{BASE_URL}/research/gaming-the-gatekeeper.html",
    "research/ligo-monitoring.html": f"{BASE_URL}/research/ligo-monitoring.html",
    "research/metaaudit.html": f"{BASE_URL}/research/metaaudit.html",
    "research/opsagent-rl.html": f"{BASE_URL}/research/opsagent-rl.html",
    "research/prompt-injection-screening.html": f"{BASE_URL}/research/prompt-injection-screening.html",
    "research/rai-gate.html": f"{BASE_URL}/research/rai-gate.html",
}

UNPUBLISHED_PORTFOLIO_PAGES = {
    "research/agentsentry.html",
    "research/cora.html",
    "research/metaaudit.html",
    "research/gaming-the-gatekeeper.html",
    "research/rai-gate.html",
    "research/opsagent-rl.html",
    "research/cost-aware-llm-judges.html",
}


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_title = False
        self.title = ""
        self.metas: list[dict[str, str]] = []
        self.links: list[dict[str, str]] = []
        self.imgs: list[dict[str, str]] = []
        self.sources: list[dict[str, str]] = []
        self.anchors: list[str] = []
        self.h1_count = 0
        self.in_ld = False
        self.cur_ld = ""
        self.ld_blocks: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        d = {k: (v or "") for k, v in attrs}
        if tag == "title":
            self.in_title = True
        elif tag == "meta":
            self.metas.append(d)
        elif tag == "link":
            self.links.append(d)
        elif tag == "img":
            self.imgs.append(d)
        elif tag == "source":
            self.sources.append(d)
        elif tag == "a":
            self.anchors.append(d.get("href", ""))
        elif tag == "h1":
            self.h1_count += 1
        elif tag == "script" and d.get("type") == "application/ld+json":
            self.in_ld = True
            self.cur_ld = ""

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self.in_title = False
        elif tag == "script" and self.in_ld:
            self.ld_blocks.append(self.cur_ld.strip())
            self.in_ld = False

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title += data
        if self.in_ld:
            self.cur_ld += data


def resolve_local_path(page_rel: str, ref: str) -> Path:
    clean = ref.split("#")[0].split("?")[0]
    if clean.startswith("/"):
        rel = clean.lstrip("/")
        if rel == "" or rel.endswith("/"):
            return ROOT / rel / "index.html"
        return ROOT / rel
    base = (ROOT / page_rel).parent
    target = (base / clean).resolve()
    if target.is_dir():
        return target / "index.html"
    return target


def collect_ids_and_types(obj: object, ids: set[str], types: set[str]) -> None:
    if isinstance(obj, dict):
        if "@id" in obj and isinstance(obj["@id"], str):
            ids.add(obj["@id"])
        if "@type" in obj:
            t = obj["@type"]
            if isinstance(t, str):
                types.add(t)
            elif isinstance(t, list):
                types.update(str(x) for x in t)
        for v in obj.values():
            collect_ids_and_types(v, ids, types)
    elif isinstance(obj, list):
        for item in obj:
            collect_ids_and_types(item, ids, types)


def audit() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    titles: dict[str, str] = {}
    descriptions: dict[str, str] = {}
    inbound_links: dict[str, int] = {url: 0 for url in EXPECTED_PAGES.values()}

    # 1. Discover any unlisted HTML pages (excluding google verification & hidden/report dirs)
    for path in ROOT.rglob("*.html"):
        rel = path.relative_to(ROOT).as_posix()
        if rel.startswith((".git/", "seo-reports/", "scripts/")):
            continue
        if path.name.startswith("google") and len(path.name) > 16:
            continue
        if rel not in EXPECTED_PAGES:
            warnings.append(f"Unregistered HTML page found (not in EXPECTED_PAGES): {rel}")

    # 2. Audit each intended public page
    for rel, expected_canonical in EXPECTED_PAGES.items():
        full_path = ROOT / rel
        if not full_path.exists():
            errors.append(f"Missing expected public page: {rel}")
            continue

        parser = PageParser()
        parser.feed(full_path.read_text(encoding="utf-8"))

        # Title
        title = " ".join(parser.title.split())
        if not title:
            errors.append(f"[{rel}] Missing <title>")
        else:
            if len(title) < 20 or len(title) > 80:
                warnings.append(f"[{rel}] Title length ({len(title)} chars) outside 20-80 range: {title}")
            if title in titles:
                errors.append(f"[{rel}] Duplicate title also used on {titles[title]}: {title}")
            titles[title] = rel

        # Meta description
        desc = next((m.get("content", "").strip() for m in parser.metas if m.get("name") == "description"), "")
        if not desc:
            errors.append(f"[{rel}] Missing meta description")
        else:
            if len(desc) < 70 or len(desc) > 260:
                warnings.append(f"[{rel}] Meta description length ({len(desc)} chars) outside 70-260 range")
            if desc in descriptions:
                errors.append(f"[{rel}] Duplicate meta description also used on {descriptions[desc]}")
            descriptions[desc] = rel

        # Robots / accidental noindex
        robots_vals = [m.get("content", "").lower() for m in parser.metas if m.get("name") == "robots"]
        for rv in robots_vals:
            if "noindex" in rv or "nofollow" in rv:
                errors.append(f"[{rel}] Accidental restrictive robots directive: {rv}")
        if not robots_vals:
            warnings.append(f"[{rel}] Missing explicit <meta name='robots'> tag")

        # Canonical URL
        canonicals = [l.get("href", "").strip() for l in parser.links if l.get("rel") == "canonical"]
        if len(canonicals) != 1:
            errors.append(f"[{rel}] Expected exactly 1 canonical tag, found {len(canonicals)}")
        elif canonicals[0] != expected_canonical:
            errors.append(f"[{rel}] Canonical mismatch: got '{canonicals[0]}', expected '{expected_canonical}'")

        # Open Graph & Twitter basics
        og_props = {m.get("property"): m.get("content", "") for m in parser.metas if m.get("property")}
        tw_names = {m.get("name"): m.get("content", "") for m in parser.metas if m.get("name", "").startswith("twitter:")}
        for req in ("og:title", "og:description", "og:url", "og:image"):
            if not og_props.get(req):
                errors.append(f"[{rel}] Missing Open Graph tag: {req}")
        for req in ("twitter:card", "twitter:title", "twitter:description"):
            if not tw_names.get(req):
                errors.append(f"[{rel}] Missing Twitter Card tag: {req}")

        # Single H1
        if parser.h1_count != 1:
            errors.append(f"[{rel}] Expected exactly 1 <h1>, found {parser.h1_count}")

        # Images: alt, width, height, valid src
        for img in parser.imgs:
            src = img.get("src", "")
            if not img.get("alt", "").strip():
                errors.append(f"[{rel}] Image missing alt text: {src}")
            if not img.get("width") or not img.get("height"):
                errors.append(f"[{rel}] Image missing explicit width/height: {src}")
            if src and not src.startswith(("http://", "https://", "data:")):
                target = resolve_local_path(rel, src)
                if not target.exists():
                    errors.append(f"[{rel}] Broken image src: {src}")

        # Picture sources
        for src_tag in parser.sources:
            srcset = src_tag.get("srcset", "")
            for part in srcset.split(","):
                url_part = part.strip().split(" ")[0]
                if url_part and not url_part.startswith(("http://", "https://", "data:")):
                    target = resolve_local_path(rel, url_part)
                    if not target.exists():
                        errors.append(f"[{rel}] Broken <source> srcset asset: {url_part}")

        # Internal links & canonical consistency
        for href in parser.anchors:
            if not href or href.startswith(("#", "http://", "https://", "mailto:", "tel:")):
                continue
            clean = href.split("#")[0].split("?")[0]
            if not clean:
                continue
            if clean.endswith("index.html"):
                errors.append(f"[{rel}] Non-canonical internal link to index.html: {href}")
            target = resolve_local_path(rel, clean)
            if not target.exists():
                errors.append(f"[{rel}] Broken internal link: {href}")
            else:
                try:
                    t_rel = target.relative_to(ROOT).as_posix()
                    if t_rel in EXPECTED_PAGES and EXPECTED_PAGES[t_rel] != expected_canonical:
                        inbound_links[EXPECTED_PAGES[t_rel]] += 1
                except ValueError:
                    pass

        # Structured data JSON-LD validation
        if not parser.ld_blocks:
            errors.append(f"[{rel}] Missing JSON-LD structured data")
        ids: set[str] = set()
        types: set[str] = set()
        for idx, blk in enumerate(parser.ld_blocks):
            try:
                parsed = json.loads(blk)
                collect_ids_and_types(parsed, ids, types)
            except json.JSONDecodeError as exc:
                errors.append(f"[{rel}] Invalid JSON-LD block #{idx + 1}: {exc}")
        if PERSON_ID not in ids:
            errors.append(f"[{rel}] JSON-LD missing consistent Person @id ({PERSON_ID})")
        if rel in UNPUBLISHED_PORTFOLIO_PAGES and "ScholarlyArticle" in types:
            errors.append(f"[{rel}] Unpublished portfolio project must not use ScholarlyArticle schema")

    # 3. Orphan page check
    for url, count in inbound_links.items():
        if count == 0:
            errors.append(f"Orphan page (zero internal inbound links): {url}")

    # 4. Validate robots.txt
    robots_path = ROOT / "robots.txt"
    if not robots_path.exists():
        errors.append("Missing robots.txt")
    else:
        rtxt = robots_path.read_text(encoding="utf-8")
        if f"Sitemap: {BASE_URL}/sitemap.xml" not in rtxt:
            errors.append("robots.txt does not reference https://www.preet-baxi.com/sitemap.xml")
        if "Disallow: /" in rtxt and "Disallow: / " not in rtxt:
            for line in rtxt.splitlines():
                if line.strip().lower() == "disallow: /":
                    errors.append("robots.txt blocks entire site with 'Disallow: /'")

    # 5. Validate sitemap.xml (URLs + image locs)
    sitemap_path = ROOT / "sitemap.xml"
    if not sitemap_path.exists():
        errors.append("Missing sitemap.xml")
    else:
        try:
            tree = ET.parse(sitemap_path)
            root_el = tree.getroot()
            ns = {
                "sm": "http://www.sitemaps.org/schemas/sitemap/0.9",
                "img": "http://www.google.com/schemas/sitemap-image/1.1",
            }
            locs = [el.text.strip() for el in root_el.findall("sm:url/sm:loc", ns) if el.text]
            expected_urls = set(EXPECTED_PAGES.values())
            actual_urls = set(locs)
            if len(locs) != len(actual_urls):
                errors.append("sitemap.xml contains duplicate <loc> entries")
            missing_in_sm = expected_urls - actual_urls
            extra_in_sm = actual_urls - expected_urls
            if missing_in_sm:
                errors.append(f"sitemap.xml missing canonical URLs: {sorted(missing_in_sm)}")
            if extra_in_sm:
                errors.append(f"sitemap.xml contains unexpected URLs: {sorted(extra_in_sm)}")
            for img_loc in root_el.findall("sm:url/img:image/img:loc", ns):
                if img_loc.text:
                    parsed_u = urlparse(img_loc.text.strip())
                    local_asset = ROOT / parsed_u.path.lstrip("/")
                    if not local_asset.exists():
                        errors.append(f"sitemap.xml image <image:loc> does not exist locally: {img_loc.text}")
        except ET.ParseError as exc:
            errors.append(f"Invalid XML in sitemap.xml: {exc}")

    # 6. Validate IndexNow host verification file
    indexnow_key = "a8abb5d57579b82dc92f5ffc32629e0e"
    indexnow_file = ROOT / f"{indexnow_key}.txt"
    if not indexnow_file.exists():
        errors.append(f"Missing IndexNow key verification file: {indexnow_file.name}")
    elif indexnow_file.read_text(encoding="utf-8").strip() != indexnow_key:
        errors.append(f"IndexNow key file {indexnow_file.name} content does not match filename key")

    # 7. Check for broken local stylesheet/script/source resources across all 12 HTML pages
    asset_ref_re = re.compile(r'''(?:href|src|srcset)=["']([^"']+)["']''')
    for rel in EXPECTED_PAGES:
        raw_html = (ROOT / rel).read_text(encoding="utf-8")
        for match in asset_ref_re.findall(raw_html):
            for candidate in match.split(","):
                token = candidate.strip().split(" ")[0]
                if not token or token.startswith(("#", "http://", "https://", "mailto:", "tel:", "data:")):
                    continue
                clean = token.split("#")[0].split("?")[0]
                if not clean:
                    continue
                resolved = resolve_local_path(rel, clean)
                if not resolved.exists():
                    errors.append(f"[{rel}] Broken local resource reference: {token}")

    # 8. Secret & exposed credential scanner (public repository safety check)
    secret_patterns = [
        ("Private key block", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),
        ("Google service account JSON", re.compile(r'"type"\s*:\s*"service_account"')),
        ("GitHub personal access token", re.compile(r"\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{30,}\b")),
        ("OpenAI / Anthropic API key", re.compile(r"\bsk-(?:proj-|ant-)?[A-Za-z0-9_-]{32,}\b")),
        ("AWS access key ID", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ]
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.suffix.lower() in {".png", ".webp", ".jpg", ".jpeg", ".pdf", ".ico", ".woff", ".woff2"}:
            continue
        if path.name == "seo_audit.py":
            continue
        try:
            content = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for label, pat in secret_patterns:
            if pat.search(content):
                errors.append(f"Potential exposed credential ({label}) in {path.relative_to(ROOT).as_posix()}")

    # 9. Optional external publication link verification (--check-external)
    if "--check-external" in sys.argv:
        import urllib.error
        import urllib.request

        pub_urls = [
            "https://aclanthology.org/2026.findings-acl.142/",
            "https://doi.org/10.18653/v1/2026.findings-acl.142",
            "https://arxiv.org/abs/2606.27287",
            "https://doi.org/10.1088/1361-6382/ae7adb",
            "https://arxiv.org/abs/2601.09918",
            "https://doi.org/10.1103/PhysRevD.104.084080",
            "https://arxiv.org/abs/2103.03241",
            "https://github.com/preetb1199/Prompt_Injection_ACL26",
            "https://github.com/preetb1199/CalculateSNRg_Python",
        ]
        for u in pub_urls:
            req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0 SEO-Audit/1.0"}, method="HEAD")
            try:
                with urllib.request.urlopen(req, timeout=12) as resp:
                    if resp.status >= 400:
                        errors.append(f"External publication link returned HTTP {resp.status}: {u}")
            except urllib.error.HTTPError as exc:
                if exc.code in (403, 405):
                    # Some academic publishers block HEAD/bot probes; record informational notice only
                    pass
                else:
                    errors.append(f"External publication link broken (HTTP {exc.code}): {u}")
            except Exception as exc:
                warnings.append(f"External publication link timeout/network error ({exc}): {u}")

    print(f"SEO Audit complete: checked {len(EXPECTED_PAGES)} canonical pages, sitemap, robots, IndexNow, local assets, and secret hygiene.")
    if warnings:
        print(f"\nWarnings ({len(warnings)}):")
        for w in warnings:
            print(f"  [WARN] {w}")
    if errors:
        print(f"\nErrors ({len(errors)}):")
        for e in errors:
            print(f"  [FAIL] {e}")
        return 1

    print("All automated technical SEO, structured data, image, link, sitemap, IndexNow, and credential-hygiene checks PASSED.")
    return 0


if __name__ == "__main__":
    sys.exit(audit())
