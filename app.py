"""
app.py  –  CorpusChat: Quantum Computing QA
Run:  streamlit run app.py
"""

import streamlit as st

# ── Page config ──────────────────────────────────────────
st.set_page_config(
    page_title="QuantumChat",
    page_icon="⚛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── CSS ──────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Space+Mono:ital,wght@0,400;0,700;1,400;1,700&display=swap');




:root {
  --card: #1e1b4b;
  --ring: #8b5cf6;
  --input: #2e1065;
  --muted: #1e1b4b;
  --accent: #4338ca;
  --border: #2e1065;
  --radius: 0.625rem;
  --chart-1: #a78bfa;
  --chart-2: #8b5cf6;
  --chart-3: #7c3aed;
  --chart-4: #6d28d9;
  --chart-5: #5b21b6;
  --popover: #1e1b4b;
  --primary: #8b5cf6;
  --sidebar: #0f172a;
  --secondary: #1e1b4b;
  --background: #0f172a;
  --foreground: #e0e7ff;
  --destructive: #ef4444;
  --sidebar-ring: #8b5cf6;
  --sidebar-accent: #4338ca;
  --sidebar-border: #2e1065;
  --card-foreground: #e0e7ff;
  --sidebar-primary: #8b5cf6;
  --muted-foreground: #c4b5fd;
  --accent-foreground: #e0e7ff;
  --popover-foreground: #e0e7ff;
  --primary-foreground: #ffffff;
  --sidebar-foreground: #e0e7ff;
  --secondary-foreground: #e0e7ff;
  --destructive-foreground: #ffffff;
  --sidebar-accent-foreground: #e0e7ff;
  --sidebar-primary-foreground: #ffffff;
  --spacing: 0.25rem;
  --font-mono: "Space Mono", monospace;
  --font-sans: "Space Grotesk", sans-serif;
  --font-serif: ui-serif, Georgia, Cambria, "Times New Roman", Times, serif;
  --shadow-blur: 5px;
  --shadow-color: hsl(0 0% 0%);
  --shadow-spread: 0px;
  --letter-spacing: 0em;
  --shadow-opacity: 0.6;
  --shadow-offset-x: 0px;
  --shadow-offset-y: 2px;
}

@theme inline {
  --color-card: var(--card);
  --color-ring: var(--ring);
  --color-input: var(--input);
  --color-muted: var(--muted);
  --color-accent: var(--accent);
  --color-border: var(--border);
  --color-radius: var(--radius);
  --color-chart-1: var(--chart-1);
  --color-chart-2: var(--chart-2);
  --color-chart-3: var(--chart-3);
  --color-chart-4: var(--chart-4);
  --color-chart-5: var(--chart-5);
  --color-popover: var(--popover);
  --color-primary: var(--primary);
  --color-sidebar: var(--sidebar);
  --color-font-mono: var(--font-mono);
  --color-font-sans: var(--font-sans);
  --color-secondary: var(--secondary);
  --color-background: var(--background);
  --color-font-serif: var(--font-serif);
  --color-foreground: var(--foreground);
  --color-destructive: var(--destructive);
  --color-shadow-blur: var(--shadow-blur);
  --color-shadow-color: var(--shadow-color);
  --color-sidebar-ring: var(--sidebar-ring);
  --color-shadow-spread: var(--shadow-spread);
  --color-shadow-opacity: var(--shadow-opacity);
  --color-sidebar-accent: var(--sidebar-accent);
  --color-sidebar-border: var(--sidebar-border);
  --color-card-foreground: var(--card-foreground);
  --color-shadow-offset-x: var(--shadow-offset-x);
  --color-shadow-offset-y: var(--shadow-offset-y);
  --color-sidebar-primary: var(--sidebar-primary);
  --color-muted-foreground: var(--muted-foreground);
  --color-accent-foreground: var(--accent-foreground);
  --color-popover-foreground: var(--popover-foreground);
  --color-primary-foreground: var(--primary-foreground);
  --color-sidebar-foreground: var(--sidebar-foreground);
  --color-secondary-foreground: var(--secondary-foreground);
  --color-destructive-foreground: var(--destructive-foreground);
  --color-sidebar-accent-foreground: var(--sidebar-accent-foreground);
  --color-sidebar-primary-foreground: var(--sidebar-primary-foreground);
}




html, body, [class*="css"] { font-family: var(--font-mono); }

/* Animated main background */
.stApp {
    background: var(--background);
    color: var(--foreground);
}

/* Glassmorphic sidebar */
section[data-testid="stSidebar"] {
    background: var(--sidebar) !important;
    border-right: 1px solid var(--sidebar-border);
}
section[data-testid="stSidebar"] * { color: var(--sidebar-foreground) !important; }
section[data-testid="stSidebar"] .stMarkdown h3 {
    color: var(--sidebar-primary) !important;
    text-shadow: none;
}

/* header & animated title */
.qc-header {
    display: flex;
    align-items: baseline;
    gap: 0.8rem;
    margin-bottom: 0.2rem;
}
.qc-title {
    font-family: var(--font-sans);
    font-size: 2.2rem;
    font-weight: 800;
    letter-spacing: -0.04em;
    line-height: 1.1;
    position: relative;
    display: inline-block;
    background: linear-gradient(120deg, var(--primary) 0%, var(--primary) 40%, rgba(255,255,255,0.8) 50%, var(--primary) 60%, var(--primary) 100%);
    background-size: 250% auto;
    color: transparent;
    -webkit-background-clip: text;
    background-clip: text;
    transition: all 0.5s cubic-bezier(0.25, 0.8, 0.25, 1);
}
.qc-title:hover {
    background-position: 200% center;
    transform: translateY(-2px) scale(1.02);
    filter: drop-shadow(0 8px 16px rgba(139, 92, 246, 0.4));
}

.qc-badge {
    font-family: var(--font-mono);
    font-size: 0.68rem;
    background: var(--accent);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 3px 12px;
    color: var(--accent-foreground);
}
.qc-sub {
    font-size: 0.88rem;
    color: var(--muted-foreground);
    font-weight: 400;
    margin-bottom: 0;
}

/* glowing divider */
hr {
    border: none !important;
    height: 1px !important;
    background: var(--border) !important;
    margin: 1.2rem 0 !important;
}

/* User Message */
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) {
    background: var(--primary) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius) !important;
    padding: 1rem 1.4rem !important;
    margin-bottom: 1rem !important;
    color: var(--primary-foreground) !important;
}

/* Assistant Message */
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]) {
    background: var(--card) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius) !important;
    padding: 1rem 1.4rem !important;
    margin-bottom: 1rem !important;
    color: var(--card-foreground) !important;
}

/* source pill floating effect */
.src-pill {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: var(--muted);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 4px 14px 4px 10px;
    font-family: var(--font-mono);
    font-size: 0.73rem;
    color: var(--muted-foreground);
    margin: 4px 5px 4px 0;
}
.src-dot {
    width: 8px; height: 8px;
    border-radius: 50%;
    display: inline-block;
    flex-shrink: 0;
}
.src-score {
    color: var(--accent);
    font-size: 0.68rem;
    font-weight: 500;
}

/* relevance bar */
.rel-wrap {
    height: 3px;
    background: var(--muted);
    border-radius: var(--radius);
    margin: 4px 0 8px 0;
    width: 100%;
}
.rel-fill {
    height: 3px;
    border-radius: var(--radius);
    background: var(--primary);
}

/* chat input */
[data-testid="stChatInput"] {
    background: var(--input) !important;
    border: 1px solid transparent !important;
    border-radius: 28px !important;
    padding: 0.5rem 1rem !important;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1) !important;
    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
}
[data-testid="stChatInput"]:hover {
    border-color: var(--primary) !important;
    box-shadow: 0 8px 20px rgba(0,0,0,0.2) !important;
    transform: translateY(-1px) !important;
}
[data-testid="stChatInput"]:focus-within {
    background: var(--card) !important;
    border-color: var(--primary) !important;
    box-shadow: 0 0 0 2px var(--ring), 0 10px 24px rgba(0,0,0,0.3) !important;
    transform: translateY(-2px) !important;
}
[data-testid="stChatInput"] textarea {
    color: var(--foreground) !important;
    font-family: var(--font-sans) !important;
    font-size: 1rem !important;
}

/* stat card */
.stat-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 0.9rem 1.2rem;
    margin-bottom: 0.6rem;
}
.stat-label { color: var(--muted-foreground); font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.08em; }
.stat-value { color: var(--card-foreground); font-family: var(--font-mono); font-size: 1.2rem; font-weight: 500; }

/* Welcome card */
.welcome {
    background: linear-gradient(135deg, var(--card) 0%, var(--background) 100%);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 3.5rem 2.5rem;
    text-align: center;
    margin: 1rem 0 3rem 0;
    box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    transition: all 0.4s cubic-bezier(0.25, 0.8, 0.25, 1);
    position: relative;
    overflow: hidden;
    z-index: 1;
}
.welcome::before {
    content: '';
    position: absolute;
    top: 0; left: -150%;
    width: 60%; height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.08), transparent);
    transform: skewX(-20deg);
    transition: all 0.7s ease;
    z-index: -1;
}
.welcome:hover {
    transform: translateY(-4px) scale(1.02);
    box-shadow: 0 16px 40px rgba(0,0,0,0.4), 0 0 0 1px var(--primary);
    background: linear-gradient(135deg, var(--card) 0%, var(--muted) 100%);
}
.welcome:hover::before {
    left: 200%;
}
.welcome-title {
    font-family: var(--font-sans);
    font-size: 1.6rem;
    font-weight: 700;
    color: var(--primary);
    margin-bottom: 0.8rem;
    letter-spacing: -0.02em;
}
.welcome-desc { 
    font-family: var(--font-mono); 
    color: var(--card-foreground); 
    font-size: 0.95rem; 
    line-height: 1.7; 
    font-weight: 300; 
    opacity: 0.85; 
}

/* Interactive buttons */
.stButton > button {
    background: linear-gradient(135deg, var(--secondary) 0%, var(--card) 100%) !important;
    border: 1px solid var(--border) !important;
    border-radius: 12px !important;
    color: var(--secondary-foreground) !important;
    font-size: 0.85rem !important;
    font-family: var(--font-mono) !important;
    font-weight: 500 !important;
    padding: 0.6rem 1rem !important;
    transition: all 0.4s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1) !important;
    position: relative !important;
    overflow: hidden !important;
    z-index: 1 !important;
}
.stButton > button::before {
    content: '' !important;
    position: absolute !important;
    top: 0 !important; left: -150% !important;
    width: 60% !important; height: 100% !important;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.08), transparent) !important;
    transform: skewX(-20deg) !important;
    transition: all 0.7s ease !important;
    z-index: -1 !important;
}
.stButton > button:hover {
    transform: translateY(-2px) scale(1.02) !important;
    box-shadow: 0 10px 20px rgba(0,0,0,0.3), 0 0 0 1px var(--primary) !important;
    background: linear-gradient(135deg, var(--card) 0%, var(--muted) 100%) !important;
    color: var(--primary) !important;
    border-color: var(--primary) !important;
}
.stButton > button:hover::before {
    left: 200% !important;
}

/* clear button */
.stButton[data-testid="clear-btn"] > button {
    background: var(--destructive) !important;
    color: var(--destructive-foreground) !important;
}

/* Layout overrides */
footer { display: none !important; }
.stApp > header { background-color: transparent !important; }
.block-container { padding-top: 2rem !important; padding-bottom: 2rem !important; max-width: 900px !important; }

/* Custom glowing scrollbar */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: var(--background); }
::-webkit-scrollbar-thumb {
    background: var(--primary);
    border-radius: var(--radius);
}
::-webkit-scrollbar-thumb:hover { background: var(--accent); }

/* error box */
.err-box {
    background: var(--destructive);
    border: 1px solid var(--border);
    border-left: 4px solid var(--primary);
    border-radius: var(--radius);
    padding: 1.2rem;
    font-family: var(--font-mono);
    font-size: 0.85rem;
    color: var(--destructive-foreground);
}
</style>
""", unsafe_allow_html=True)


# ── Source color map ──────────────────────────────────────
SOURCE_COLORS = {
    "Wikipedia":    "#60a5fa",
    "IBM Think":    "#818cf8",
    "AWS":          "#34d399",
    "NASA (PDF)":   "#fb923c",
}

def source_color(src: str) -> str:
    for key, color in SOURCE_COLORS.items():
        if key.lower() in src.lower():
            return color
    return "#5b8ef0"


# ── Load retriever (cached) ───────────────────────────────
@st.cache_resource(show_spinner="Loading corpus and embedding model...")
def load_retriever():
    try:
        from chatbot.retriever import CorpusRetriever
        return CorpusRetriever(), None
    except FileNotFoundError as e:
        return None, str(e)
    except Exception as e:
        return None, f"Unexpected error: {e}"

retriever, load_error = load_retriever()


# ── Sidebar ───────────────────────────────────────────────
with st.sidebar:
    st.markdown("### QuantumChat")
    st.markdown("<hr>", unsafe_allow_html=True)

    if retriever:
        s = retriever.stats()
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-label">Corpus Chunks</div>
            <div class="stat-value">{s['total_chunks']}</div>
        </div>""", unsafe_allow_html=True)

        st.markdown("**Data Sources**")
        for src, count in s["sources"].items():
            color = source_color(src)
            st.markdown(f"""
            <div class="stat-card">
                <div class="stat-label" style="color:{color}88;">{src}</div>
                <div class="stat-value" style="color:{color};">{count} <span style="font-size:0.7rem;color:#3a4a70;">chunks</span></div>
            </div>""", unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="err-box">
        Corpus not loaded<br><br>
        Run:<br>
        <code>python build_corpus.py</code>
        </div>""", unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    top_k = st.slider("Retrieved chunks (K)", 1, 6, 3,
                      help="More chunks = more context, slightly slower")
    show_src  = st.toggle("Show source citations", value=True)
    show_raw  = st.toggle("Show raw chunks",        value=False)

    st.markdown("<hr>", unsafe_allow_html=True)
    if st.button("Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.markdown("""
    <div style="font-size:0.7rem;color:#3E7CB1;margin-top:1rem;line-height:1.6;">
    NLP Task-2 · Quantum Computing<br>
    Wikipedia · IBM · AWS<br>
    sentence-transformers / MiniLM-L6
    </div>""", unsafe_allow_html=True)


# ── Header ────────────────────────────────────────────────
st.markdown("""
<div class="qc-header">
    <span class="qc-title">QuantumChat</span>
    <span class="qc-badge">NLP Task-2</span>
</div>
<div class="qc-sub">Corpus-based QA · Quantum Computing · Wikipedia · IBM · AWS</div>
""", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# ── Session state ─────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []

# ── Welcome screen ────────────────────────────────────────
EXAMPLES = [
    "What is quantum computing?",
    "How do qubits work?",
    "What is superposition?",
    "What are applications of quantum computing?",
    "What is quantum entanglement?",
    "How is quantum different from classical computing?",
]

if not st.session_state.messages:
    st.markdown("""
    <div class="welcome">
        <div class="welcome-title">Ask anything about Quantum Computing</div>
        <div class="welcome-desc">
            Answers are generated purely from collected corpus<br>
            Wikipedia, IBM Think, AWS, and the Sample PDF document.
        </div>
    </div>""", unsafe_allow_html=True)

    cols = st.columns(3)
    for i, q in enumerate(EXAMPLES):
        with cols[i % 3]:
            if st.button(q, key=f"ex_{i}", use_container_width=True):
                st.session_state.messages.append({"role": "user", "content": q})
                st.rerun()


# ── Render existing messages ──────────────────────────────
def render_sources(sources):
    if not sources:
        return
    st.markdown("<div style='margin-top:0.6rem;'>", unsafe_allow_html=True)
    st.markdown(
        "<span style='font-size:0.73rem;color:#2a3a60;'>Sources</span>",
        unsafe_allow_html=True
    )
    for src in sources:
        color = source_color(src["source"])
        pct   = int(src["score"] * 100)
        st.markdown(f"""
        <span class="src-pill">
            <span class="src-dot" style="background:{color};"></span>
            {src['source']} · {src['section']}
            <span class="src-score">{src['score']:.2f}</span>
        </span>""", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if msg["role"] == "assistant" and "meta" in msg:
            if show_src:
                render_sources(msg["meta"].get("sources", []))
            if show_raw and msg["meta"].get("chunks"):
                with st.expander("Raw chunks", expanded=False):
                    for i, c in enumerate(msg["meta"]["chunks"]):
                        st.markdown(f"**#{i+1}** `{c['source']}` · `{c['section']}` · score `{c['score']:.3f}`")
                        st.markdown(f"> {c['content'][:280]}...")
                        st.markdown("---")


# ── Chat input ────────────────────────────────────────────
if prompt := st.chat_input("Ask about quantum computing..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.rerun()

# ── Generate assistant response ───────────────────────────
if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
    prompt = st.session_state.messages[-1]["content"]
    
    with st.chat_message("assistant"):
        if not retriever:
            msg = f"Corpus not loaded. Run `python build_corpus.py` first.\n\n`{load_error}`"
            st.markdown(msg)
            st.session_state.messages.append(
                {"role": "assistant", "content": msg, "meta": {}}
            )
        else:
            with st.spinner("Searching corpus..."):
                result = retriever.answer(prompt, top_k=top_k)

            st.markdown(result["answer"])

            if show_src:
                render_sources(result["sources"])

            if show_raw and result["chunks"]:
                with st.expander("Raw chunks", expanded=False):
                    for i, c in enumerate(result["chunks"]):
                        st.markdown(f"**#{i+1}** `{c['source']}` · `{c['section']}` · score `{c['score']:.3f}`")
                        st.markdown(f"> {c['content'][:280]}...")
                        st.markdown("---")

            st.session_state.messages.append({
                "role": "assistant",
                "content": result["answer"],
                "meta": {
                    "sources": result["sources"],
                    "chunks":  result["chunks"]
                }
            })
