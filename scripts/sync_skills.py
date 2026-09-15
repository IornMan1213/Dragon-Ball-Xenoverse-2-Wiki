#!/usr/bin/env python3
"""Build the XV2 skill catalog from public Fandom category/member pages."""
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
OUT = ROOT / "docs/data/skills.json"
INDEX = ROOT / "docs/data/skills-index.json"
MD = ROOT / "docs/Skills-Auto-Database.md"
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
    "User-Agent": "Mozilla/5.0 (compatible; XV2-Wiki-Skills-Sync/3.4)",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8", "replace")


class MemberParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.items: list[str] = []
        self.href: str | None = None
        self.text: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag.lower() != "a":
            return
        d = dict(attrs)
        href = d.get("href") or ""
        cls = (d.get("class") or "").lower()
        if href.startswith("/wiki/") and "category-page__member" in cls:
            self.href, self.text = href, []

    def handle_data(self, data):
        if self.href is not None:
            self.text.append(data)

    def handle_endtag(self, tag):
        if tag.lower() == "a" and self.href is not None:
            value = re.sub(r"\s+", " ", "".join(self.text)).strip()
            if value:
                self.items.append(value)
            self.href, self.text = None, []


class TextParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        t = tag.lower()
        if t in {"script", "style", "noscript", "svg"}:
            self.skip += 1
        elif not self.skip and t in {"br", "p", "div", "li", "tr", "h1", "h2", "h3", "h4", "h5", "h6"}:
            self.parts.append("\n")

    def handle_endtag(self, tag):
        t = tag.lower()
        if t in {"script", "style", "noscript", "svg"} and self.skip:
            self.skip -= 1
        elif not self.skip and t in {"p", "div", "li", "tr", "h1", "h2", "h3", "h4", "h5", "h6"}:
            self.parts.append("\n")

    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)


def clean(value: str) -> str:
    value = html.unescape(value)
    value = re.sub(r"[ \t\r]+", " ", value)
    value = re.sub(r"\n\s*\n+", "\n", value)
    return value.strip(" |\t\r\n")


def page_url(title: str) -> str:
    return f"{BASE}/wiki/{urllib.parse.quote(title.replace(' ', '_'))}"


def category_members(category: str) -> list[str]:
    raw = fetch(f"{BASE}/wiki/Category:{urllib.parse.quote(category.replace(' ', '_'))}")
    p = MemberParser()
    p.feed(raw)
    titles = sorted(set(p.items), key=str.casefold)
    if titles:
        return titles
    # Fallback for Fandom markup changes. Restrict to anchors in the category page
    # and discard obvious navigation/category/file links.
    candidates = set()
    for href, label in re.findall(r"href=[\"'](/wiki/[^\"']+)[\"'][^>]*>(.*?)</a>", raw, flags=re.I | re.S):
        title = clean(re.sub(r"<[^>]+>", " ", label))
        slug = urllib.parse.unquote(href[6:])
        if title and not slug.startswith(("Category:", "File:", "Special:")):
            candidates.add(title)
    return sorted(candidates, key=str.casefold)


def visible(raw: str) -> str:
    p = TextParser()
    p.feed(raw)
    return clean("".join(p.parts))


def meta_description(raw: str) -> str | None:
    for pattern in (
        r"<meta[^>]+name=[\"']description[\"'][^>]+content=[\"']([^\"']+)",
        r"<meta[^>]+property=[\"']og:description[\"'][^>]+content=[\"']([^\"']+)",
    ):
        m = re.search(pattern, raw, flags=re.I)
        if m:
            return clean(m.group(1))[:1000]
    return None


def label_value(text: str, labels: tuple[str, ...]) -> str | None:
    for label in labels:
        m = re.search(rf"(?:^|\n)\s*{re.escape(label)}\s*:?\s*([^\n]+)", text, flags=re.I)
        if m:
            value = clean(m.group(1))
            if value:
                return value
    return None


def parse_skill(title: str) -> dict:
    url = page_url(title)
    raw = fetch(url)
    text = visible(raw)
    record: dict = {"sources": [url]}
    desc = meta_description(raw)
    if desc:
        record["skill_description"] = desc

    fields = {
        "ki_cost": ("Ki Used", "Ki Cost", "Ki Required"),
        "stamina_cost": ("Stamina Used", "Stamina Cost", "Stamina Required"),
        "damage_type": ("Attack Type", "Damage Type"),
        "unlock_method": ("Unlock", "How to Obtain", "Obtained"),
        "source_quest_or_shop": ("Source", "Parallel Quest", "PQ"),
        "dlc_requirement": ("DLC", "DLC Requirement", "Pack"),
        "race_restriction": ("Race Restriction", "Available to", "Race"),
        "character_source": ("Notable User(s)", "Notable User", "Character Source"),
    }
    for key, labels in fields.items():
        value = label_value(text, labels)
        if value:
            record[key] = value

    if not record.get("skill_description"):
        # The public pages generally expose Properties/Usage Tips as prose.
        for heading in ("Properties", "Effect", "Effects", "Description", "Usage Tips"):
            marker = re.search(rf"(?:^|\n)\s*{re.escape(heading)}\s*(?:\n|$)", text, flags=re.I)
            if marker:
                tail = text[marker.end():]
                snippet = clean(tail.split("Categories", 1)[0])[:1000]
                if len(snippet) > 35:
                    record["skill_description"] = snippet
                    break

    populated = sum(bool(record.get(k)) for k in (
        "skill_description", "unlock_method", "source_quest_or_shop", "ki_cost", "stamina_cost", "damage_type", "dlc_requirement", "race_restriction"
    ))
    record["research_status"] = "enriched" if populated >= 3 else ("partially_enriched" if populated else "page_unavailable")
    record["verification_status"] = "partially_verified" if populated else "indexed"
    return record


def load_curated() -> dict[tuple[str, str, str], dict]:
    if not OUT.exists():
        return {}
    try:
        data = json.loads(OUT.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    result = {}
    for r in data.get("records", []):
        key = (r.get("name", "").casefold(), r.get("class", ""), r.get("subcategory", ""))
        if key[0]:
            result[key] = {k: v for k, v in r.items() if k not in {"name", "class", "subcategory", "sources"}}
    return result


def md(value) -> str:
    if value in (None, ""):
        return "—"
    return str(value).replace("|", "\\|").replace("\n", " ").strip()


def main() -> int:
    curated = load_curated()
    members: dict[str, list[str]] = {}
    counts: dict[str, int] = {}
    all_titles: set[str] = set()

    for category in CATEGORIES:
        try:
            names = category_members(category)
        except Exception as exc:
            print(f"Category failed: {category}: {type(exc).__name__}")
            names = []
        members[category] = names
        counts[category] = len(names)
        all_titles.update(names)
        print(f"{category}: {len(names)}")

    if not all_titles:
        raise SystemExit("No skill category members found; refusing to overwrite the catalog.")

    page_cache: dict[str, dict] = {}
    failures = 0
    titles = sorted(all_titles, key=str.casefold)
    for i, title in enumerate(titles, 1):
        try:
            page_cache[title] = parse_skill(title)
        except Exception as exc:
            failures += 1
            page_cache[title] = {"sources": [page_url(title)], "research_status": "page_unavailable", "verification_status": "indexed", "source_error": type(exc).__name__}
        if i % 25 == 0 or i == len(titles):
            print(f"Pages {i}/{len(titles)}; failures={failures}")
        time.sleep(0.05)

    records = {}
    for category, (skill_class, subtype) in CATEGORIES.items():
        category_url = f"{BASE}/wiki/Category:{urllib.parse.quote(category.replace(' ', '_'))}"
        for title in members[category]:
            key = (title.casefold(), skill_class, subtype)
            r = {"name": title, "class": skill_class, "subcategory": subtype, "verification_status": "indexed", "research_status": "indexed", "sources": [category_url]}
            r.update(curated.get(key, {}))
            r.update({k: v for k, v in page_cache.get(title, {}).items() if k != "sources"})
            r["sources"] = list(dict.fromkeys(r["sources"] + page_cache.get(title, {}).get("sources", [])))
            records[key] = r

    rows = sorted(records.values(), key=lambda r: (r["name"].casefold(), r["class"], r["subcategory"]))
    payload = {
        "schema_version": "1.2", "game": "Dragon Ball Xenoverse 2", "source_index": f"{BASE}/wiki/Category:Skills",
        "generated": date.today().isoformat(), "status": "enriched_catalog", "category_counts": counts,
        "record_count": len(rows), "records": rows,
        "notes": "Coverage is indexed from public category pages. Per-skill data is imported only when parseable from the public skill page; missing data is left pending rather than guessed.",
    }
    OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    INDEX.write_text(json.dumps({
        "schema_version": "1.2", "source_index": payload["source_index"], "generated": payload["generated"],
        "category_counts": counts, "record_count": len(rows),
        "records": [{k: r[k] for k in ("name", "class", "subcategory", "verification_status", "research_status", "sources")} for r in rows],
    }, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    verified = sum(r["verification_status"] == "verified" for r in rows)
    partial = sum(r["verification_status"] == "partially_verified" for r in rows)
    lines = [
        "# Skills — Auto-Generated Master Database", "",
        f"> Generated {payload['generated']}. Contains one row for every indexed skill-category member.",
        f"> **Records:** {len(rows)} · **Verified:** {verified} · **Partially verified:** {partial} · **Indexed/pending:** {len(rows)-verified-partial}",
        "",
        "| Skill | Class | Subcategory | Effect | How to get it | Source | Ki | Stamina | DLC | Status |",
        "|---|---|---|---|---|---|---:|---:|---|---|",
    ]
    for r in rows:
        lines.append("| " + " | ".join(md(r.get(k)) for k in (
            "name", "class", "subcategory", "skill_description", "unlock_method", "source_quest_or_shop", "ki_cost", "stamina_cost", "dlc_requirement", "verification_status"
        )) + " |")
    lines += ["", "## Research policy", "", "A blank field is intentionally left blank when the source page did not expose a parseable value. This table is an exhaustive coverage layer; it does not turn unverified source material into a verified claim.", ""]
    MD.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {len(rows)} records; partial={partial}; indexed={len(rows)-verified-partial}; page_failures={failures}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
