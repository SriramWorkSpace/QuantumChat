"""
scrape_wikipedia.py
Scrapes the Wikipedia article on Quantum Computing using requests + BeautifulSoup.
No wikipedia-api library needed.
"""

import requests
from bs4 import BeautifulSoup
import re
import json

from scraper.utils import clean_text, chunk_text

URL = "https://en.wikipedia.org/wiki/Quantum_computing"
TOPIC = "Quantum Computing"
SOURCE = "Wikipedia"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}

# Skip these Wikipedia sections (navigation noise)
SKIP_SECTIONS = {
    "contents", "references", "external links", "notes",
    "further reading", "see also", "bibliography", "footnotes"
}


def scrape_wikipedia() -> list:
    try:
        response = requests.get(URL, headers=HEADERS, timeout=20)
        response.raise_for_status()
    except Exception as e:
        print(f"[Wikipedia] Failed to fetch: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    # Wikipedia article body
    content_div = soup.find("div", {"id": "mw-content-text"})
    if not content_div:
        print("[Wikipedia] Could not find article body.")
        return []

    entries = []
    current_section = "Introduction"

    for element in content_div.find_all(["h2", "h3", "p"], recursive=True):
        if element.name in ["h2", "h3"]:
            heading = clean_text(element.get_text())
            heading = re.sub(r'\[edit\]', '', heading).strip()
            if heading.lower() in SKIP_SECTIONS:
                current_section = None  # Stop collecting under skip sections
            else:
                current_section = heading

        elif element.name == "p" and current_section:
            text = clean_text(element.get_text())
            if len(text) < 60:
                continue
            for chunk in chunk_text(text):
                entries.append({
                    "source": SOURCE,
                    "url": URL,
                    "topic": TOPIC,
                    "section": current_section,
                    "content": chunk
                })

    print(f"[Wikipedia] Extracted {len(entries)} chunks.")
    return entries


if __name__ == "__main__":
    data = scrape_wikipedia()
    print(json.dumps(data[:2], indent=2))
    print(f"Total: {len(data)} chunks")
