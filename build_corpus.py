"""
build_corpus.py
Runs all 4 scrapers and merges into corpus/corpus.json
Run this ONCE before launching the app.

Usage:
    python build_corpus.py
"""

import json
import os
import sys
from collections import Counter

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from scraper.scrape_wikipedia import scrape_wikipedia
from scraper.scrape_ibm import scrape_ibm
from scraper.scrape_aws import scrape_aws
from scraper.extract_pdf import extract_pdf
from scraper.scrape_azure import scrape_azure
from scraper.scrape_dst import scrape_dst
from scraper.scrape_ibm_blog import scrape_ibm_blog


def build_corpus():
    all_entries = []
    errors = []

    print("=" * 55)
    print("  QUANTUM COMPUTING CORPUS BUILDER")
    print("=" * 55)

    # Ensure required directories exist
    os.makedirs("corpus", exist_ok=True)
    os.makedirs("data", exist_ok=True)

    steps = [
        ("[1/7] Scraping Wikipedia...",   scrape_wikipedia),
        ("[2/7] Scraping IBM Think...",   scrape_ibm),
        ("[3/7] Scraping AWS...",         scrape_aws),
        ("[4/7] Extracting NASA PDF...",  extract_pdf),
        ("[5/7] Scraping Microsoft Azure...", scrape_azure),
        ("[6/7] Scraping DST NQM...",     scrape_dst),
        ("[7/7] Scraping IBM Quantum Blog...", scrape_ibm_blog),
    ]

    for label, fn in steps:
        print(f"\n{label}")
        try:
            entries = fn()
            all_entries.extend(entries)
        except Exception as e:
            msg = f"[ERROR] {label} - {e}"
            print(msg)
            errors.append(msg)

    print("\n" + "=" * 55)
    print(f"  Raw corpus entries : {len(all_entries)}")

    # ── Deduplication (same source + same content) ──────────
    seen = set()
    unique_entries = []
    for entry in all_entries:
        key = (entry["source"], entry["content"])
        if key not in seen:
            seen.add(key)
            unique_entries.append(entry)

    removed = len(all_entries) - len(unique_entries)
    if removed:
        print(f"  Duplicates removed : {removed}")
    print(f"  Final unique entries: {len(unique_entries)}")
    print("=" * 55)

    if not unique_entries:
        print("\n[ERROR] No data collected. Check your internet connection.")
        return

    # Save
    output_path = "corpus/corpus.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(unique_entries, f, indent=2, ensure_ascii=False)

    print(f"\nCorpus saved -> {output_path}")

    # Source breakdown
    source_counts = Counter(e["source"] for e in unique_entries)
    print("\nSource breakdown:")
    for source, count in source_counts.items():
        print(f"  {source:25s} -> {count} chunks")

    # Summary of any errors
    if errors:
        print("\n[!] Some scrapers encountered errors:")
        for err in errors:
            print(f"  {err}")

    # Sample entry
    print("\nSample entry:")
    print(json.dumps(unique_entries[0], indent=2))


if __name__ == "__main__":
    build_corpus()
