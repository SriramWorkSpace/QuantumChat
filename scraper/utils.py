"""
scraper/utils.py
Shared text-cleaning and chunking utilities for all scrapers.
"""

import re


def clean_text(text: str, pdf_mode: bool = False) -> str:
    """
    Normalise whitespace, remove citation brackets, strip non-ASCII.

    Args:
        text:     Raw scraped / extracted text.
        pdf_mode: When True, first collapses hyphenated PDF line-breaks
                  (e.g. "quan-\\ntum" → "quantum") before general cleanup.
    """
    if pdf_mode:
        text = re.sub(r'-\n', '', text)   # remove hyphenated line-breaks
        text = re.sub(r'\n+', ' ', text)  # collapse remaining newlines

    text = re.sub(r'\[[\d]+\]', '', text)  # Remove citation numbers [1]
    text = re.sub(r'\s+', ' ', text)        # Collapse whitespace
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)  # Strip non-ASCII
    return text.strip()


def chunk_text(text: str, chunk_size: int = 250) -> list:
    """
    Split *text* into word-boundary chunks of at most *chunk_size* words.
    Chunks shorter than 60 characters are discarded.
    """
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        if len(chunk.strip()) > 60:
            chunks.append(chunk)
    return chunks
