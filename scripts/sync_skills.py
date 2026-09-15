#!/usr/bin/env python3
"""Build a normalized XV2 skill catalog from public Fandom wiki pages."""
from __future__ import annotations

import html
import json
import re
import time
import urllib.parse
import urllib.request
from datetime import date
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX_OUT = ROOT / "docs" / "data" / "skills-index.json"
CANONICAL_OUT = ROOT / "docs" / "data" / "skills.json"
MARKDOWN_OUT = ROOT / "docs" / "Skills-Auto-Database.md"
BASE = "https://dbxv2.fandom.com"

CATEGORIES = {
    "Ki Blast Supers": ("Super", "Ki Blast"), "Strike Supers": ("Super", "Strike"),
    "Ki Blast Ultimates": ("Ultimate", "Ki Blast"), "Strike Ultimates": ("Ultimate", "Strike"),
    "Other Supers": ("Super", "Other"), "Power Up Supers": ("Super", "Power Up"),
    "Ki Blast Evasives": ("Evasive", "Ki Blast"), "Strike Evasives": ("Evasive", "Strike"),
    "Other Evasives": ("Evasive", "Other"), "Power Up Evasives": ("Evasive", "Power Up"),
    "Power Up Ultimates": ("Ultimate", "Power Up"), "Other Ultimates": ("Ultimate", "Other"),
    "Saiyan Skills": ("Awoken", "Race"), "Majin Skills": ("Awoken", "Race"),
    "Namekian Skills": ("Awoken", "Race"), "Frieza Race Skills": ("Awoken", "Race"),
    "Human Skills": ("Awoken", "Race"), "Transformations": ("Awoken", "Race"),
    "Unavailable for CaC": ("Mixed", "Special"), "Counter Skills": ("Counter", "Counter"),
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; XV2-Wiki-Skills-Sync/3.3; +https://github.com/IornMan1213/Dragon-Ball-Xenoverse-2-Wiki)",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}


def fetch_text(url: str) -> str:
    request = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(request, timeout=60) as response:
        return response.read().decode("utf-8", "replace")


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.links: list[tuple[str, str]] = []
        self._href: str | None = None
        self._text: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() != "a":
            return
        attrs_map = dict(attrs)
        href = attrs_map.get("href")
        classes = (attrs_map.get("class") or "").lower()
        if href and ("category-page__member-link" in classes or "category-page__member" in classes):
            self._href = href
            self._text = []

    def handle_data(self, data: str) -> None:
        if self._href is not None:
            self._text.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "a" and self._href is not None:
            text = re.sub(r"\s+", " ", "".join(self._text)).strip()
            if text:
                self.links.append((self._href, text))
            self._href = None
            self._text = []


class TextParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.text: list[str] = []
        self._skip = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        t = tag.lower()
        if t in {"script", "style", "noscript", "svg"}:
            self._skip += 1
        elif self._skip == 0 and t in {"br", "p", "div", "li", "tr", "h1", "h2", "h3", "h4", "h5", "h6"}:
            self.text.append("\n")

    def handle_endtag(self, tag: str) -> None:
        t = tag.lower()
        if t in {"script", "style", "noscript", "svg"} and self._skip:
            self._skip -= 1
        elif self._skip == 0 and t in {"p", "div", "li", "tr", "h1", "h2", "h3", "h4", "h5", "h6"}:
            self.text.append("\n")

    def handle_data(self, data: str) -> None:
        if self._skip == 0:
            self.text.append(data)


def visible_text(page_html: str) -> str:
    parser = TextParser()
    parser.feed(page_html)
    return html.unescape("".join(parser.text))


def normalize_text(value: str) -> str:
    value = html.unescape(value)
    value = re.sub(r"[ \t\r]+", " ", value)
    value = re.sub(r"\n\s*\n+", "\n", value)
    return value.strip(" |\t\r\n")


def canonical_key(label: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", normalize_text(label).casefold()).strip()


def page_url(title: str) -> str:
    return f"{BASE}/wiki/{urllib.parse.quote(title.replace(' ', '_'))}"


def category_members(category: str) -> list[str]:
    url = f"{BASE}/wiki/Category:{urllib.parse.quote(category.replace(' ', '_'))}"
    raw = fetch_text(url)
    parser = LinkParser()
    parser.feed(raw)
    titles = {text for href, text in parser.links if href.startswith("/wiki/") and not href.startswith(("/wiki/Category:", "/wiki/File:", "/wiki/Special:"))}
    if not titles:
        for slug, title in re.findall(r'href="/wiki/([^"]+)"[^>]*>([^<]+)</a>', raw, flags=re.I):
            if title.strip() and not slug.startswith(("Category:", "File:", "Special:")):
                titles.add(html.unescape(re.sub(r"\s+", " ", title)).strip())
    return sorted(titles, key=str.casefold)


def extract_meta_description(raw: str) -> str | None:
    patterns = [
        r'<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']+)',
        r'<meta[^>]+property=["\']og:description["\'][^>]+content=["\']([^"\']+)',
    ]
    for pattern in patterns:
        match = re.search(pattern, raw, flags=re.I)
        if match:
            return normalize_text(match.group(1))
    return None


def extract_label_value(text: str, labels: tuple[str, ...]) -> str | None:
    for label in labels:
        match = re.search(rf"(?:^|\n)\s*{re.escape(label)}\s*:?\s*([^\n]+)", text, flags=re.I)
        if match:
            value = normalize_text(match.group(1))
            if value:
                return value
    return None


def extract_section(text: str, headings: tuple[str, ...]) -> str | None:
    wanted = {canonical_key(x) for x in headings}
    lines = [normalize_text(line) for line in text.splitlines()]
    for index, line in enumerate(lines):
        if canonical_key(line) not in wanted:
            continue
        collected: list[str] = []
        for nxt in lines[index + 1:index + 24]:
            if not nxt:
                continue
            if canonical_key(nxt) in {"stats", "properties", "usage tips", "categories", "see also", "notes", "references", "unlock", "description", "effect", "effects"}:
                break
            collected.append(nxt)
            if len(" ".join(collected)) > 1200:
                break
        value = normalize_text(" ".join(collected))
        if value:
            return value[:1400]
    return None


def parse_skill_page(title: str, raw: str) -> dict:
    text = visible_text(raw)
    record: dict = {"sources": [page_url(title)]}
    meta = extract_meta_description(raw)
    if meta and len(meta) > 30:
        record["skill_description"] = meta[:1000]

    label_map = {
        "ki_cost": ("Ki Used", "Ki Cost", "Ki Required"),
        "stamina_cost": ("Stamina Used", "Stamina Cost", "Stamina Required"),
        "damage_type": ("Attack Type", "Damage Type"),
        "unlock_method": ("Unlock", "How to Obtain", "Obtained"),
        "source_quest_or_shop": ("Source", "Parallel Quest", "PQ"),
        "dlc_requirement": ("DLC", "DLC Requirement", "Pack"),
        "race_restriction": ("Race Restriction", "Available to", "Race"),
        "character_source": ("Notable User(s)", "Notable User", "Character Source"),
    }
    for key, labels in label_map.items():
        value = extract_label_value(text, labels)
        if value:
            record[key] = value

    if "skill_description" not in record:
        for headings in (("effect", "effects"), ("properties",), ("description",), ("usage tips",)):
            value = extract_section(text, headings)
            if value and len(value) > 35:
                record["skill_description"] = value[:1000]
                break

    record["usable_by_cac"] = None
    match = re.search(r"(?:Usable|Available|Can be used) (?:by|for) (?:a )?CaC[^\n]*(yes|no|true|false)", text, flags=re.I)
    if match:
        record["usable_by_cac"] = match.group(1).casefold() in {"yes", "true"}

    populated = sum(1 for key in ("ki_cost", "stamina_cost", "damage_type", "unlock_method", "source_quest_or_shop", "dlc_requirement", "skill_description", "race_restriction", "character_source") if record.get(key))
    record["research_status"] = "enriched" if populated >= 3 else ("partially_enriched" if populated else "page_unavailable")
    record["verification_status"] = "partially_verified" if populated else "indexed"
    return record


def load_curated() -> dict[tuple[str, str, str], dict]:
    if not CANONICAL_OUT.exists():
        return {}
    try:
        data = json.loads(CANONICAL_OUT.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    result: dict[tuple[str, str, str], dict] = {}
    for record in data.get("records", []):
        key = (record.get("name", "").casefold(), record.get("class", ""), record.get("subcategory", ""))
        if key[0]:
            result[key] = {k: v for k, v in record.items() if k not in {"name", "class", "subcategory", "sources"}}
    return result


def scrape_pages(titles: list[str]) -> dict[str, dict]:
    result: dict[str, dict] = {}
    failures = 0
    for index, title in enumerate(titles, 1):
        try:
            result[title] = parse_skill_page(title, fetch_text(page_url(title)))
        except Exception as exc:
            failures += 1
            result[title] = {"sources": [page_url(title)], "research_status": "page_unavailable", "verification_status": "indexed", "source_error": type(exc).__name__}
            print(f"Page failed {index}/{len(titles)}: {title} ({type(exc).__name__})")
        if index % 25 == 0 or index == len(titles):
            print(f"Fetched skill pages {index}/{len(titles)}; failures={failures}")
        time.sleep(0.05)
    return result


def md_escape(value: object) -> str:
    if value is None or value == "":
        return "—"
    return str(value).replace("|", "\\|").replace("\n", " ").strip()


def write_outputs(records: list[dict], generated: str, counts: dict[str, int]) -> None:
    payload = {
        "schema_version": "1.2", "game": "Dragon Ball Xenoverse 2", "source_index": f"{BASE}/wiki/Category:Skills",
        "generated": generated, "status": "enriched_catalog",
        "notes": "Category membership is indexed from public pages. Mechanics and acquisition fields are retained only when individual source pages expose parseable values; missing values remain explicit rather than guessed.",
        "category_counts": counts, "record_count": len(records), "records": records,
    }
    CANONICAL_OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    INDEX_OUT.write_text(json.dumps({
        "schema_version": "1.2", "source_index": payload["source_index"], "generated": generated,
        "category_counts": counts, "record_count": len(records),
        "records": [{k: r[k] for k in ("name", "class", "subcategory", "verification_status", "research_status", "sources")} for r in records],
    }, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    verified = sum(r["verification_status"] == "verified" for r in records)
    partial = sum(r["verification_status"] == "partially_verified" for r in records)
    lines = [
        "# Skills — Auto-Generated Master Database", "",
        f"> Generated {generated}. Refreshed from public Fandom category/member pages and individual skill pages.",
        "> **Coverage:** every indexed category member receives a row. A blank value means the source page did not expose that field in a form the importer could safely parse; it is **not** a license to guess.",
        "", f"**Records:** {len(records)} · **Verified:** {verified} · **Partially verified:** {partial} · **Indexed/pending:** {len(records)-verified-partial}", "",
        "| Skill | Class | Subcategory | Effect | How to get it | Source | Ki | Stamina | DLC | Status |",
        "|---|---|---|---|---|---|---:|---:|---|---|",
    ]
    for r in records:
        lines.append("| " + " | ".join([
            md_escape(r.get("name")), md_escape(r.get("class")), md_escape(r.get("subcategory")), md_escape(r.get("skill_description")),
            md_escape(r.get("unlock_method")), md_escape(r.get("source_quest_or_shop")), md_escape(r.get("ki_cost")), md_escape(r.get("stamina_cost")),
            md_escape(r.get("dlc_requirement")), md_escape(r.get("verification_status")),
        ]) + " |")
    lines.extend(["", "## Category counts", "", "| Category | Members |", "|---|---:|"])
    lines.extend(f"| {md_escape(cat)} | {count} |" for cat, count in counts.items())
    lines.extend(["", "## Research policy", "", "This generated catalog is a coverage layer, not a claim that every field is verified. Source-page data is imported when parseable, while missing acquisition, cost, DLC, restriction, or mechanics information remains pending for manual verification.", "", "See [Skills Master Database](Skills-Master-Database.md) and [Skills Complete Database](Skills-Complete-Database.md) for field definitions and verification rules.", ""])
    MARKDOWN_OUT.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    curated = load_curated()
    members_by_category: dict[str, list[str]] = {}
    all_titles: set[str] = set()
    counts: dict[str, int] = {}
    for category in CATEGORIES:
        try:
            members = category_members(category)
        except Exception as exc:
            print(f"Category failed: {category} ({type(exc).__name__})")
            members = []
        members_by_category[category] = members
        counts[category] = len(members)
        all_titles.update(members)
        time.sleep(0.15)
    if not all_titles:
        raise SystemExit("No skill category members were discovered; refusing to overwrite the catalog.")

    page_data = scrape_pages(sorted(all_titles, key=str.casefold))
    records_by_key: dict[tuple[str, str, str], dict] = {}
    for category, (skill_class, subtype) in CATEGORIES.items():
        category_url = f"{BASE}/wiki/Category:{urllib.parse.quote(category.replace(' ', '_'))}"
        for title in members_by_category[category]:
            record = {"name": title, "class": skill_class, "subcategory": subtype, "verification_status": "indexed", "research_status": "indexed", "sources": [category_url]}
            record.update(curated.get((title.casefold(), skill_class, subtype), {}))
            source_data = page_data.get(title, {})
            for key, value in source_data.items():
                if key not in {"sources", "source_error"} and value not in (None, ""):
                    record[key] = value
            record["sources"] = list(dict.fromkeys(record["sources"] + source_data.get("sources", [])))
            if source_data.get("source_error"):
                record["source_error"] = source_data["source_error"]
            records_by_key[(title.casefold(), skill_class, subtype)] = record
    records = sorted(records_by_key.values(), key=lambda r: (r["name"].casefold(), r["class"], r["subcategory"]))
    write_outputs(records, date.today().isoformat(), counts)
    verified = sum(r["verification_status"] == "verified" for r in records)
    partial = sum(r["verification_status"] == "partially_verified" for r in records)
    print(f"Wrote {len(records)} records; verified={verified}; partially_verified={partial}; indexed={len(records)-verified-partial}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
