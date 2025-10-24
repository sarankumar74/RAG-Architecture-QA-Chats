import os
import streamlit as st
from langchain_community.document_loaders import PyPDFLoader, TextLoader, UnstructuredURLLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.vectorstores import FAISS
import google.generativeai as genai
from pypdf import PdfReader
from langchain_core.documents import Document
import google.generativeai as genai
import requests
from bs4 import BeautifulSoup

# -------------------------------
# Streamlit Setup
# -------------------------------
st.set_page_config(page_title="💬 RAG Chat", page_icon="🤖")
st.title("💬 Multi-source RAG Chat with Gemini")

# -------------------------------
# Configure Google Gemini
# -------------------------------
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    st.error("⚠️ Set GOOGLE_API_KEY in environment variables")
else:
    genai.configure(api_key=GOOGLE_API_KEY)
    model_name = "models/gemini-2.5-flash"

# -------------------------------
# Session State
# -------------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None

# -------------------------------
# Sidebar: Upload / URL
# -------------------------------
st.sidebar.header("Upload / Load Content")
pdf_file = st.sidebar.file_uploader("PDF", type="pdf")
txt_file = st.sidebar.file_uploader("TXT", type="txt")
url_input = st.sidebar.text_input("URL to scrape")

# -------------------------------
# Helper Functions
# -------------------------------
def pdf_to_text(uploaded_file):
    reader = PdfReader(uploaded_file)
    return "\n".join(page.extract_text() or "" for page in reader.pages)

def txt_to_text(uploaded_file):
    return uploaded_file.read().decode("utf-8")

def scrape_url(url):
    try:
        res = requests.get(url, timeout=5)
        soup = BeautifulSoup(res.text, "html.parser")
        for s in soup(["script","style"]): s.decompose()
        return soup.get_text(separator="\n")
    except:
        return ""

# -------------------------------
# Load Documents
# -------------------------------
documents = []

if pdf_file:
    text = pdf_to_text(pdf_file)
    documents.append(Document(page_content=text))

if txt_file:
    text = txt_to_text(txt_file)
    documents.append(Document(page_content=text))

if url_input:
    text = scrape_url(url_input)
    if text:
        documents.append(Document(page_content=text))

# -------------------------------
# Split & Build VectorStore
# -------------------------------
if documents and st.session_state.vectorstore is None:
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    split_docs = splitter.split_documents(documents)
    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    st.session_state.vectorstore = FAISS.from_documents(split_docs, embeddings)
    st.sidebar.success("✅ VectorStore ready!")

# -------------------------------
# Chat Interface
# -------------------------------
question = st.text_input("Ask a question:")
if st.button("Send") and question and st.session_state.vectorstore:
    st.session_state.chat_history.append({"role":"user","message":question})

    # Retrieve top 3 chunks
    docs = st.session_state.vectorstore.similarity_search(question, k=3)
    context = "\n".join([doc.page_content for doc in docs])

    # Prompt for Gemini
    prompt = f"Answer using ONLY the content below:\n{context}\n\nQuestion: {question}\nAnswer:"
    llm = genai.GenerativeModel(model_name=model_name)
    response = llm.generate_content(prompt)
    answer = "".join(part.text for cand in response.candidates for part in cand.content.parts if hasattr(part, "text"))

    st.session_state.chat_history.append({"role":"assistant","message":answer})

# -------------------------------
# Display Chat History
# -------------------------------
for chat in st.session_state.chat_history:
    color = "#DCF8C6" if chat["role"]=="user" else "#F1F0F0"
    align = "right" if chat["role"]=="user" else "left"
    st.markdown(
        f"<div style='text-align:{align};background-color:{color};padding:8px;border-radius:10px;margin:5px 0'>{chat['message']}</div>",
        unsafe_allow_html=True
    )
