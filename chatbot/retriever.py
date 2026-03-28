"""
chatbot/retriever.py
Loads corpus.json, embeds chunks with sentence-transformers,
and retrieves top-k matches for a query via cosine similarity.
"""

import json
import os
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


MODEL_NAME = "all-MiniLM-L6-v2"   # ~90MB, fast, good quality


class CorpusRetriever:
    def __init__(self, corpus_path: str = "corpus/corpus.json"):
        self.corpus_path = corpus_path
        self.corpus = []
        self.embeddings = None
        self.model = SentenceTransformer(MODEL_NAME)
        self._load_and_embed()

    def _load_and_embed(self):
        if not os.path.exists(self.corpus_path):
            raise FileNotFoundError(
                f"Corpus not found at '{self.corpus_path}'.\n"
                "Run: python build_corpus.py"
            )

        with open(self.corpus_path, "r", encoding="utf-8") as f:
            self.corpus = json.load(f)

        print(f"[Retriever] {len(self.corpus)} chunks loaded.")
        print("[Retriever] Embedding corpus...")

        texts = [e["content"] for e in self.corpus]
        self.embeddings = self.model.encode(
            texts,
            batch_size=64,
            show_progress_bar=False,
            convert_to_numpy=True
        )
        print("[Retriever] Ready.")

    def retrieve(self, query: str, top_k: int = 3) -> list:
        q_emb = self.model.encode([query], convert_to_numpy=True)
        scores = cosine_similarity(q_emb, self.embeddings)[0]
        top_idx = np.argsort(scores)[::-1][:top_k]

        results = []
        for idx in top_idx:
            entry = dict(self.corpus[idx])
            entry["score"] = float(scores[idx])
            results.append(entry)
        return results

    def answer(self, query: str, top_k: int = 3) -> dict:
        results = self.retrieve(query, top_k=top_k)

        # Relevance threshold
        if not results or results[0]["score"] < 0.20:
            return {
                "answer": (
                    "I couldn't find relevant information in the corpus for that question. "
                    "Try rephrasing or asking something more specific about quantum computing."
                ),
                "sources": [],
                "chunks": []
            }

        # Build answer from top chunks
        seen_sources = set()
        sources = []
        answer_parts = []

        for r in results:
            answer_parts.append(r["content"])
            key = r["source"]
            if key not in seen_sources:
                seen_sources.add(key)
                sources.append({
                    "source":  r["source"],
                    "section": r.get("section", ""),
                    "score":   round(r["score"], 3),
                    "url":     r.get("url", ""),
                })

        # Join chunks as paragraphs (more readable than a single space)
        combined = "\n\n".join(answer_parts)
        # Trim to ~500 words
        words = combined.split()
        if len(words) > 500:
            combined = " ".join(words[:500]) + "..."

        return {
            "answer": combined,
            "sources": sources,
            "chunks": results
        }

    def stats(self) -> dict:
        from collections import Counter
        counts = Counter(e["source"] for e in self.corpus)
        return {
            "total_chunks": len(self.corpus),
            "sources": dict(counts)
        }
