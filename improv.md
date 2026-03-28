# QuantumChat — Future Improvements

This file tracks potential improvements that are **not in scope** for the current implementation (which strictly follows the README architecture), but should be considered for future iterations.

---

## 1. Embedding Cache (Performance)

**Problem:** Every app restart re-embeds all corpus chunks (can take 10–30s).

**Fix:** Save the NumPy embedding matrix to disk alongside `corpus.json`:
```
corpus/
├── corpus.json
└── embeddings.npy   ← save/load with np.save / np.load
```
- Check if `embeddings.npy` exists and corpus hasn't changed (hash check)
- If unchanged, load from disk → startup time drops to <2s

---

## 2. Overlapping Chunking (Retrieval Quality)

**Problem:** Current chunker uses hard 250-word non-overlapping windows. Relevant context may be split across two chunks.

**Fix:** Use a sliding window with overlap (e.g., 250 words, 50-word stride):
```python
def chunk_text(text, chunk_size=250, overlap=50):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size - overlap):
        chunk = " ".join(words[i:i + chunk_size])
        if len(chunk.strip()) > 60:
            chunks.append(chunk)
    return chunks
```

---

## 3. Re-ranking with Cross-Encoder (Accuracy)

**Problem:** Bi-encoder cosine similarity can return chunks that are topically similar but not directly answering the question.

**Fix:** Add a cross-encoder re-ranker (e.g., `cross-encoder/ms-marco-MiniLM-L-6-v2`) that re-scores the top-10 bi-encoder results, returning the best 3.

---

## 4. Answer Formatting with LLM (UX)

**Problem:** Current answers are raw chunk text concatenated, which reads awkwardly.

**Fix:** Pass the retrieved chunks as context to a small LLM (e.g., `google/flan-t5-base` or a Gemini API call) to generate a fluent, synthesised answer.

---

## 5. Clickable Source URLs in the UI

**Problem:** Source pills show source name + section but the URL is not clickable.

**Fix:** The `url` field already exists in `corpus.json`. Render it as an `<a>` tag in the source pill HTML.

---

## 6. Persistent PDF Path Config

**Problem:** `PDF_PATH` in `extract_pdf.py` is hardcoded as `"data/nasa_quantum.pdf"`.

**Fix:** Read from an environment variable or a `config.yaml`:
```python
PDF_PATH = os.getenv("NASA_PDF_PATH", "data/nasa_quantum.pdf")
```

---

## 7. Incremental Corpus Updates

**Problem:** `build_corpus.py` always re-scrapes everything from scratch.

**Fix:** Add a `--source` flag to rebuild only one source:
```bash
python build_corpus.py --source wikipedia
python build_corpus.py --source pdf
```

---

## 8. Unit Tests

**Problem:** No automated tests exist.

**Fix:** Add `tests/` directory with:
- `test_scrapers.py` — mock HTTP responses and verify chunk structure
- `test_retriever.py` — load a small synthetic corpus and verify answer format
- `test_dedup.py` — verify deduplication logic in `build_corpus.py`

---

## 9. Additional Sources

**Problem:** Only 4 sources (Wikipedia, IBM, AWS, NASA PDF). More diverse coverage improves QA quality.

**Suggested additions:**
- Google Quantum AI: `https://quantumai.google/learn/`
- Microsoft Azure Quantum: `https://azure.microsoft.com/en-us/products/quantum`
- Arxiv abstracts (top quantum computing papers)

---

## 10. Semantic Section Labels for PDF

**Problem:** All NASA PDF chunks share `"section": "PDF Extract"` — sections are indistinguishable.

**Fix:** Use simple heuristics or regex to detect section headings within PDF text (lines in ALL CAPS or matching numeric patterns like `"1. Introduction"`).
