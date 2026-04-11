"""
scrape_dst.py
Scrapes the DST National Quantum Mission page.
"""

import requests
from bs4 import BeautifulSoup
import re
import json

from scraper.utils import clean_text, chunk_text

URL = "https://dst.gov.in/national-quantum-mission-nqm"
TOPIC = "Quantum Computing"
SOURCE = "DST NQM"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}

def scrape_dst() -> list:
    try:
        response = requests.get(URL, headers=HEADERS, timeout=20)
        response.raise_for_status()
    except Exception as e:
        print(f"[{SOURCE}] Failed to fetch: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    for tag in soup(["nav", "footer", "script", "style", "header",
                     "aside", "form", "iframe", "button", "noscript"]):
        tag.decompose()

    entries = []

    sections = soup.find_all(["h2", "h3"])
    for section in sections:
        heading = clean_text(section.get_text())
        if len(heading) < 3 or len(heading) > 150:
            continue

        content_parts = []
        for sibling in section.find_next_siblings():
            if sibling.name in ["h2", "h3"]:
                break
            if sibling.name == "p":
                txt = clean_text(sibling.get_text())
                if len(txt) > 40:
                    content_parts.append(txt)
            elif sibling.name == "div":
                for p in sibling.find_all("p"):
                    txt = clean_text(p.get_text())
                    if len(txt) > 40:
                        content_parts.append(txt)

        combined = " ".join(content_parts)
        if len(combined) < 80:
            continue

        for chunk in chunk_text(combined):
            entries.append({
                "source": SOURCE,
                "url": URL,
                "topic": TOPIC,
                "section": heading,
                "content": chunk
            })

    if not entries:
        paragraphs = soup.find_all("p")
        raw = " ".join(clean_text(p.get_text()) for p in paragraphs)
        if raw.strip():
            for chunk in chunk_text(raw):
                entries.append({
                    "source": SOURCE,
                    "url": URL,
                    "topic": TOPIC,
                    "section": "Article",
                    "content": chunk
                })

    print(f"[{SOURCE}] Extracted {len(entries)} chunks.")
    return entries

if __name__ == "__main__":
    data = scrape_dst()
    print(json.dumps(data[:2], indent=2))
    print(f"Total: {len(data)} chunks")