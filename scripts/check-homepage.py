#!/usr/bin/env python3
"""Offline integrity and paper-reference checks. Run from any working directory."""

import hashlib
import json
import re
import sys
from dataclasses import dataclass, field
from decimal import Decimal, ROUND_HALF_UP
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}


@dataclass
class Element:
    tag: str
    attrs: dict
    text: str = ""
    children: list = field(default_factory=list)

    def all(self, tag):
        return [child for item in self.children for child in ([item] if item.tag == tag else []) + item.all(tag)]


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Element("document", {})
        self.stack = [self.root]
        self.elements = []

    def handle_starttag(self, tag, attrs):
        element = Element(tag, dict(attrs))
        self.stack[-1].children.append(element)
        self.elements.append(element)
        if tag not in VOID:
            self.stack.append(element)

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, 0, -1):
            if self.stack[index].tag == tag:
                del self.stack[index:]
                break

    def handle_data(self, text):
        for element in self.stack:
            element.text += text


def normalized(text):
    return " ".join(text.split())


def check():
    errors = []

    def require(condition, message):
        if not condition:
            errors.append(message)

    source = (ROOT / "index.html").read_text()
    reference = json.loads((ROOT / "scripts/homepage-reference.json").read_text())
    page = Page()
    page.feed(source)
    ids = [el.attrs["id"] for el in page.elements if "id" in el.attrs]
    require(len(ids) == len(set(ids)), "Duplicate HTML id")
    require(len(page.root.all("h1")) == 1, "Expected one page heading")
    require(not re.search(r"coming(?:\s|%20)*soon|lorem ipsum|PAPER_TITLE|YOUR_DOMAIN|FIRST_AUTHOR_NAME", source, re.I), "Placeholder content or link remains")

    local_files = set()
    for el in page.elements:
        for attr in ("href", "src", "poster"):
            if attr not in el.attrs:
                continue
            value = el.attrs[attr] or ""
            url = urlsplit(value)
            require(bool(value.strip()) and value != "#", f"Empty {attr} on <{el.tag}>")
            if url.scheme or url.netloc:
                require(url.scheme in ("https", "http", "mailto", "tel"), f"Unexpected URL scheme: {value}")
                continue
            if not url.path:
                require(unquote(url.fragment) in ids, f"Missing internal anchor: {value}")
            else:
                path = ROOT / unquote(url.path).lstrip("/")
                require(path.is_file() and path.stat().st_size > 0, f"Missing or empty linked file: {value}")
                local_files.add(path)
        if el.tag == "img":
            require(bool(el.attrs.get("alt", "").strip()), "Figure is missing alternative text")
            require(all(el.attrs.get(key, "").isdigit() and int(el.attrs[key]) > 0 for key in ("width", "height")), f"Figure needs intrinsic dimensions: {el.attrs.get('src')}")

    for path in sorted(local_files):
        if path.suffix == ".css" and path.is_file():
            for value in re.findall(r"url\(\s*['\"]?([^)'\"\s]+)", path.read_text()):
                url = urlsplit(value)
                if not url.scheme and not url.netloc and url.path:
                    asset = path.parent / unquote(url.path)
                    require(asset.is_file(), f"Missing CSS asset: {value}")

    pdf = ROOT / reference["pdf"]
    require(pdf.is_file() and hashlib.sha256(pdf.read_bytes()).hexdigest() == reference["pdf_sha256"], "Served PDF differs from the reviewed 2026-09-09 paper")
    metadata = {el.attrs.get("name"): el.attrs.get("content") for el in page.root.all("meta")}
    require(metadata.get("citation_pdf_url", "").endswith(reference["pdf"]), "Citation metadata points to a different PDF")
    citation_authors = [el.attrs.get("content") for el in page.root.all("meta") if el.attrs.get("name") == "citation_author"]
    require(citation_authors == [a["citation"] for a in reference["authors"]], "Citation author order differs from the paper")
    authors = [el for el in page.elements if "author-block" in el.attrs.get("class", "").split()]
    require(len(authors) == len(reference["authors"]), "Visible author count differs from the paper")
    for author, expected in zip(authors, reference["authors"]):
        require(normalized(author.text) == expected["name"] + expected["marks"], f"Incorrect author or affiliation marks: {expected['name']}")
    affiliation_groups = [el for el in page.elements if "publication-affiliations" in el.attrs.get("class", "").split()]
    require(len(affiliation_groups) == 1, "Expected one visible affiliation group")
    if affiliation_groups:
        visible = [normalized(el.text) for el in affiliation_groups[0].all("span")]
        expected = [f"{index} {name}" for index, name in enumerate(reference["affiliations"], 1)]
        require(visible == expected, "Visible affiliation numbers or names differ from the paper")
    articles = []
    for script in page.root.all("script"):
        if script.attrs.get("type") == "application/ld+json":
            try:
                articles.append(json.loads(script.text))
            except json.JSONDecodeError as error:
                errors.append(f"Invalid JSON-LD: {error}")
    require(len(articles) == 1, "Expected one ScholarlyArticle JSON-LD block")
    if articles:
        article = articles[0]
        require(article.get("@type") == "ScholarlyArticle", "Incorrect structured-data type")
        require(article.get("dateModified") == reference["date"], "Paper revision date is missing")
        structured = article.get("author", [])
        require(len(structured) == len(reference["authors"]), "Structured author count differs from the paper")
        for actual, expected in zip(structured, reference["authors"]):
            require(actual.get("name") == expected["name"], "Structured author order differs from the paper")
            require([a.get("name") for a in actual.get("affiliation", [])] == [reference["affiliations"][i-1] for i in expected["affiliations"]], f"Structured affiliations differ for {expected['name']}")

    row_count = 0
    for key, expected_rows in reference["tables"].items():
        matches = [el for el in page.root.all("table") if el.attrs.get("data-reference") == key]
        require(len(matches) == 1, f"Missing or duplicated paper table: {key}")
        if not matches:
            continue
        rows = [r for tbody in matches[0].all("tbody") for r in tbody.all("tr")]
        require(len(rows) == len(expected_rows), f"Row count differs for {key}")
        for row, expected in zip(rows, expected_rows):
            # Keep the original seven task scores as independent reference data.
            avg = (sum(Decimal(str(x)) for x in expected["doc_ocr"]) / 7).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)
            cells = [normalized(c.text) for c in row.children if c.tag in ("th", "td")]
            values = [expected["model"], expected["arch"], expected["data"], str(avg), str(expected["mme"]), str(expected["caption"]), str(expected["all_avg"])]
            require(cells == values, f"{key} {expected['model']} {expected['arch']}: expected {values}, got {cells}")
            row_count += 1

    if errors:
        print("Homepage checks failed:")
        print("\n".join(f"  - {error}" for error in errors))
        return 1
    print(f"Homepage checks passed: {len(local_files)} local resources, {len(authors)} authors, 4 affiliations, {row_count} paper table rows, current PDF and metadata.")
    return 0


if __name__ == "__main__":
    sys.exit(check())
