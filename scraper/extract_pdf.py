"""
extract_pdf.py
Extracts text from the NASA Quantum Computing PDF using PyMuPDF.
Place your PDF at: data/nasa_quantum.pdf
"""

import fitz  # PyMuPDF
import json
import os

from scraper.utils import chunk_text, clean_text

# ─── CONFIG ───────────────────────────────────────────────
PDF_PATH = "data/nasa_quantum.pdf"
TOPIC = "Quantum Computing"
SOURCE = "NASA (PDF)"
# ──────────────────────────────────────────────────────────


def extract_pdf() -> list:
    if not os.path.exists(PDF_PATH):
        print(f"[NASA PDF] File not found at '{PDF_PATH}'. Skipping.")
        print("  -> Place your NASA PDF at: data/nasa_quantum.pdf")
        return []

    doc = fitz.open(PDF_PATH)
    all_text = ""
    total_pages = len(doc)

    print(f"[NASA PDF] Reading {total_pages} pages...")
    for page_num, page in enumerate(doc):
        page_text = page.get_text("text")
        all_text += " " + page_text

    doc.close()

    cleaned = clean_text(all_text, pdf_mode=True)

    if len(cleaned) < 200:
        print("[NASA PDF] Extracted text is too short. PDF may be scanned/image-based.")
        return []

    entries = []
    for chunk in chunk_text(cleaned):
        entries.append({
            "source": SOURCE,
            "url": "NASA Technical Document",
            "topic": TOPIC,
            "section": "PDF Extract",
            "content": chunk
        })

    print(f"[NASA PDF] Extracted {len(entries)} chunks from {total_pages} pages.")
    return entries


if __name__ == "__main__":
    data = extract_pdf()
    print(json.dumps(data[:2], indent=2))
    print(f"Total: {len(data)} chunks")
