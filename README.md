# QuantumChat — NLP Task 2

Domain-specific corpus QA chatbot on **Quantum Computing**.  
Sources: Wikipedia · IBM Think · AWS · Sample PDF

---

## Folder Structure

```
task2-quantum/
├── scraper/
│   ├── scrape_wikipedia.py     ← requests + BeautifulSoup
│   ├── scrape_ibm.py           ← IBM Think article
│   ├── scrape_aws.py           ← AWS explainer page
│   └── extract_pdf.py          ← NASA PDF (PyMuPDF)
├── chatbot/
│   └── retriever.py            ← sentence-transformers QA engine
├── corpus/
│   └── corpus.json             ← generated after build step
├── data/
│   └── nasa_quantum.pdf        ← place your PDF here
├── app.py                      ← Streamlit chat UI
├── build_corpus.py             ← run this once
├── requirements.txt
└── README.md
```

---

## Local Setup

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Place NASA PDF
#    Copy your PDF to:  data/nasa_quantum.pdf

# 3. Build the corpus (scrapes all 3 sites + PDF)
python build_corpus.py

# 4. Launch the chatbot
streamlit run app.py
# Opens at http://localhost:8501
```

---

## Hosting — Streamlit Community Cloud (Free, Recommended)

This is the easiest option. No server needed.

### Step 1 — Prepare corpus locally
```bash
python build_corpus.py
```
This creates `corpus/corpus.json`. You need to commit this file.

### Step 2 — Push to GitHub
```bash
git init
git add .
git commit -m "initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/task2-quantum.git
git push -u origin main
```

### Step 3 — Deploy on Streamlit Cloud
1. Go to https://share.streamlit.io
2. Sign in with GitHub
3. Click **"New app"**
4. Set:
   - Repository: `YOUR_USERNAME/task2-quantum`
   - Branch: `main`
   - Main file path: `app.py`
5. Click **Deploy**

Your app will be live at:
`https://YOUR_USERNAME-task2-quantum-app-xxxx.streamlit.app`

> **Note:** The `all-MiniLM-L6-v2` model (~90 MB) downloads automatically
> on first startup. Streamlit Cloud handles this fine with `@st.cache_resource`.

---

## Hosting — Railway (Alternative, Always-on)

If you want the app to stay on 24/7 without sleeping:

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login and deploy
railway login
railway init
railway up
```

Add a `Procfile`:
```
web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
```

Free tier gives 500 hours/month. Paid is $5/month for always-on.

---

## How It Works

### Corpus Pipeline
```
Wikipedia (requests+BS4)  ──┐
IBM Think (requests+BS4)  ──┤──► chunk(250 words) + clean ──► corpus.json
AWS (requests+BS4)        ──┤
NASA PDF (PyMuPDF)        ──┘
```

### QA Pipeline
```
User Question
     │
     ▼
Embed with all-MiniLM-L6-v2
     │
     ▼
Cosine similarity vs all corpus chunks
     │
     ▼
Top-K chunks (threshold: score > 0.20)
     │
     ▼
Concatenate → answer text + source citations
```

---

## Sources

| # | Type      | Source                                              |
|---|-----------|-----------------------------------------------------|
| 1 | Web page  | https://en.wikipedia.org/wiki/Quantum_computing     |
| 2 | Web page  | https://www.ibm.com/think/topics/quantum-computing  |
| 3 | Web page  | https://aws.amazon.com/what-is/quantum-computing/   |
| 4 | PDF       | NASA Quantum Computing technical document           |

---

## Task 2 Deliverables

- [x] List of web sources used (4 sources above)
- [x] Sample scraping method (requests + BeautifulSoup + PyMuPDF)
- [x] Final JSON corpus (`corpus/corpus.json`)
- [x] Chatbot demonstration (`app.py` — Streamlit)
- [x] Corpus creation pipeline (see above)
