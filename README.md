# 🤖 Q&A Chatbot using RAG Architecture
🔍 NLP • LLM • Vector Database • Semantic Search • Streamlit • Enterprise Knowledge Assistant

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![NLP](https://img.shields.io/badge/Domain-NLP-green?logo=ai)
![LLM](https://img.shields.io/badge/Model-LLM%20(GPT%2C%20Llama)-yellow?logo=openai)
![RAG](https://img.shields.io/badge/Architecture-RAG-red)
![VectorDB](https://img.shields.io/badge/Database-Chroma%20%7C%20FAISS-lightblue)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-orange?logo=streamlit)
![Deployment](https://img.shields.io/badge/Deployment-AWS%20EC2%20%7C%20Streamlit%20Cloud-success)
![Explainability](https://img.shields.io/badge/Explainability-SHAP%20%7C%20Attention%20Maps-purple)

---

## 📘 Overview
**Q&A Chatbot using RAG Architecture** is an **intelligent document-aware conversational assistant** designed to answer user questions based on **retrieved context from PDFs, text files, or web sources**.

This chatbot uses:
- 🧠 **LLMs (GPT, Llama, Gemini) for natural answer generation**
- 🔍 **Semantic retrieval via embeddings + VectorDB**
- 🧩 **RAG (Retrieval–Augmented Generation)** to ensure responses remain grounded and factual

It supports **PDF upload, text upload, and web URL extraction**, making it an AI-powered search engine for **enterprise documents and academic knowledge retrieval**.

---

## 🎯 Problem Statement
Traditional keyword-based search fails to extract accurate, contextual answers from long or complex documents.

This chatbot solves that by:
- Searching semantically instead of with keywords  
- Pulling only relevant text chunks  
- Generating grounded answers using augmented LLM prompts  
- Providing **source citations** to ensure answer transparency  

---

## 💼 Business Use Cases

| Sector | Value |
|--------|-------|
| 🛠 Customer Support | Automated responses based on product manuals & FAQs |
| ⚖ Legal Firms | Query case laws, summaries, clauses, & contracts |
| 🎓 EdTech | AI study assistant for textbooks & lecture notes |
| 🏢 Enterprises | Internal knowledge base assistant for policies & SOPs |
| 🔬 Research | Academic paper summarization & literature search automation |

---

## 🧠 Skills Takeaway
- Text preprocessing, tokenization & chunking  
- **SentenceTransformers / BERT embeddings**
- **RAG — Retrieval + Augmentation + LLM generation**
- **VectorDB search using Chroma / FAISS**
- **Prompt engineering & context optimization**
- **Explainability using relevance scores & attention visualization**
- **Streamlit deployment (Cloud / AWS EC2)**

---

## 🗺️ Project Workflow & Architecture

```
User Query ➜ Vector Retrieval (Top-K) ➜ Context Augmentation ➜ LLM Generation ➜ Final Answer + Sources
```

### 🔹 Data Pipeline
- Accepts PDFs, text files, web links  
- Cleans & splits documents into semantic chunks

### 🔹 Embeddings & VectorDB
- Sentence-Transformer / MiniLM models for embeddings  
- Stores vectors in **Chroma** or **FAISS** for similarity search

### 🔹 RAG-based Answer Generation
- Dynamic prompt = **Retrieved Context + User Query**
- LLM produces factual and grounded answer

### 🔹 Explainability
- Document-source citations
- Relevance scores
- Attention heatmaps (optional)

### 🔹 Deployment
- Multi-page **Streamlit Web App**
- Hosted on **Streamlit Cloud / AWS EC2 / Render**
- `.env` for API keys and local security

---

## 📸 Application UI Screenshots

### 📌 PDF Input – Home & Output Page 1
![Home Page](https://github.com/user-attachments/assets/0bb92053-ac5a-4164-a49e-10a58d038b34)

### 📌 PDF Input – Output Page 2
![Home Page](https://github.com/user-attachments/assets/cf32013d-5445-4b90-a659-ce2562e3d27f)

### 📌 Text Input – Results Page
![Result Page](https://github.com/user-attachments/assets/0e2be9a1-98ca-4306-b958-a107ce0e20ff)

### 📌 Web Scraping – Results Page
![Result Page](https://github.com/user-attachments/assets/1a0f9664-3279-47b8-974d-802b7900df54)

---

## 🧩 Project Structure
```bash
QnA-RAG-Chatbot/
│
├── .env                      # API keys & environment config
│
├── app.py                    # Streamlit web app
│
└── requirements.txt          # Dependencies
```

---

## 🛠 Run the Project Locally

Install dependencies:
```
pip install -r requirements.txt
```

Start the Streamlit app:
```
streamlit run app.py
```

Add your API keys inside:
```
.env
```



