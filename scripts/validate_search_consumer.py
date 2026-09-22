#!/usr/bin/env python3
"""Validate the published full-text Search consumer contract.

This is a presentation/consumer validator only. It does not assert content
completeness and does not replace canonical relationship or record data.
"""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def require(text: str, pattern: str, label: str) -> None:
    if not re.search(pattern, text, re.MULTILINE):
        raise AssertionError(f"missing Search contract: {label}")


def main() -> None:
    page = read("docs/Search.md")
    js = read("docs/assets/search.js")
    data = read("docs/search-data.html")

    require(page, r"^permalink:\s*/Search/$", "Search permalink")
    require(page, r'data-wiki-search', "search input hook")
    require(page, r'data-search-results', "results hook")
    require(page, r'data-search-status', "status hook")

    require(js, r"new URLSearchParams\(window\.location\.search\)", "query-parameter parser")
    require(js, r"params\.get\(['\"]q['\"]\)", "q parameter consumption")
    require(js, r"input\.value\s*=\s*initialQuery", "initial query injection")
    require(js, r"fetch\(['\"]/Dragon-Ball-Xenoverse-2-Wiki/search-data\.json['\"]", "local generated search index")
    require(js, r"input\.addEventListener\(['\"]input['\"]", "live search listener")
    if re.search(r"fetch\(\s*['\"]https?://", js):
        raise AssertionError("Search consumer contains an external fetch endpoint")

    require(data, r"permalink:\s*/search-data\.json", "generated search-data permalink")
    require(data, r"site\.pages\s*\|\s*sort:\s*['\"]url['\"]", "site-page search corpus")
    require(data, r"page\.path\s*==\s*['\"]search-data\.html['\"]", "self-exclusion from corpus")

    print("Search consumer validation: PASS")
    print("Search page: local hook contract present")
    print("Search JS: q parameter + local search-data fetch + live input contract present")
    print("Search data producer: site.pages corpus + self-exclusion contract present")
    print("External fetch endpoints in Search JS: 0")


if __name__ == "__main__":
    main()
