# ⚖️ AI Legal Contract Reviewer using Hybrid CRAG

> 🏆 This repository is my official submission for the **Tips Hindawi Challenge (June–July 2026)**.

An AI-powered legal contract analysis system that reviews contracts according to **Egyptian law** using a **Hybrid Corrective Retrieval-Augmented Generation (CRAG)** architecture. The application combines a local legal knowledge base with trusted online Egyptian legal resources to identify risky clauses, explain potential legal issues, and recommend improvements.

---

# 👤 Participant

| Field | Value |
|-------|-------|
| **Full Name** | Mohamed Ali Mohamed Elwan |
| **Project Name** | AI Legal Contract Reviewer using Hybrid CRAG |
| **GitHub Username** | MohamedElwan |
| **Challenge Batch** | June–July 2026 |
| **Training Program** | Large Language Models (LLMs) Program |
| **Organization** | **Edrak for AI** |

---

# 📖 Project Overview

Legal contracts often contain clauses that may expose individuals or businesses to legal and financial risks. Reviewing these contracts manually requires legal expertise and considerable time.

This project provides an AI-powered assistant that analyses legal contracts according to **Egyptian law**. It combines:

- A **local legal knowledge base** (RAG)
- **Trusted Egyptian legal websites** (Tavily Search)
- A **Hybrid CRAG retrieval strategy**
- A **Large Language Model (Mistral)**

The system produces a structured legal review including:

- Contract summary
- Risky clauses
- Risk level
- Legal explanation
- Suggested revisions

The application is built with **Streamlit** for an easy-to-use interface and supports both **PDF contracts** and **plain text** input.

---

# ✨ Features

- 📄 Upload contracts as PDF files
- 📝 Analyse pasted contract text
- ⚖️ Egyptian law-focused legal review
- 🔍 Hybrid CRAG retrieval (Local RAG + Web Search)
- 📚 Local FAISS vector database
- 🌐 Trusted Egyptian legal web search using Tavily
- 🤖 Mistral Large Language Model
- 📊 Structured JSON output using LangChain Output Parser
- 🎨 Streamlit web interface
- 📑 Automatic contract summarisation
- ⚠️ Risk detection and classification
- 💡 Suggested legal improvements

---

# 🏗️ Project Architecture

```
                        User Contract
                             │
          ┌──────────────────┴──────────────────┐
          │                                     │
      Upload PDF                          Paste Text
          │                                     │
          └──────────────► PDF Loader ◄─────────┘
                             │
                             ▼
                     Contract Text
                             │
                             ▼
                     Hybrid CRAG Engine
                    ┌──────────┴──────────┐
                    │                     │
             Local FAISS RAG       Tavily Search
                    │                     │
                    └──────────┬──────────┘
                               ▼
                     Retrieved Legal Context
                               │
                               ▼
                     Prompt Construction
                               │
                               ▼
                     Mistral LLM (Kaggle API)
                               │
                               ▼
                    LangChain Output Parser
                               │
                               ▼
                     Structured Legal Report
```

---

# 🛠️ Technologies Used

## Programming Language

- Python

## LLM

- Mistral Nemo Instruct 2407

## Frameworks

- LangChain
- Streamlit
- FastAPI

## Vector Database

- FAISS

## Embeddings

- sentence-transformers/all-MiniLM-L6-v2

## Retrieval

- Hybrid CRAG
- Tavily Search

## PDF Processing

- PyPDFLoader

## Output Parsing

- Pydantic
- LangChain Output Parser

## Deployment

- Kaggle Notebook
- FastAPI
- ngrok

---

# 📂 Project Structure

```
project/
│
├── app.py
├── service.py
├── llm.py
├── rag.py
├── crag.py
├── search.py
├── prompts.py
├── parser.py
├── chains.py
├── pdf_loader.py
│
├── data/
│   └── Egyptian_Laws.pdf
│
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/AI-Legal-Contract-Reviewer.git

cd AI-Legal-Contract-Reviewer
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run app.py
```

---

# 🚀 Usage

1. Launch the Streamlit application.
2. Enter your Tavily API key.
3. Enter your Kaggle/ngrok endpoint.
4. Upload a PDF contract or paste contract text.
5. Click **Analyse Contract**.
6. Review the generated legal report.

The report includes:

- Contract Summary
- Overall Risk Level
- Risky Clauses
- Legal Explanation
- Suggested Improvements

---

# 📸 Demo

### Home Screen

> Add a screenshot here

### Upload Contract

> Add a screenshot here

### Contract Analysis

> Add a screenshot here

---

# 📈 Results

The system successfully:

- Reviews contracts using Egyptian legal references.
- Combines local and online legal knowledge.
- Detects risky contractual clauses.
- Generates structured legal reports.
- Produces machine-readable JSON outputs.
- Supports both PDF and text inputs.

---

# 🔮 Future Improvements

- Support Arabic PDF OCR.
- Add clause-by-clause highlighting inside PDFs.
- Improve retrieval using reranking models.
- Fine-tune a legal-specific LLM.
- Support multilingual legal contracts.
- Deploy the application on Hugging Face Spaces or Azure.
- Add user authentication and report history.
- Export reports as PDF and Word documents.

---

# 📚 About the Challenge

This project was developed as part of the **Tips Hindawi Challenge (June–July 2026)**.

The challenge is organised by **Tips Hindawi**, the internships department of **Edrak for AI**, to encourage participants to build practical AI applications using modern Large Language Model technologies.

This project demonstrates the application of:

- Retrieval-Augmented Generation (RAG)
- Corrective RAG (CRAG)
- Large Language Models
- LangChain
- Vector Databases
- Prompt Engineering
- AI-powered document analysis

---

# 📄 License

This project is shared for educational, research, and portfolio purposes.

---
## ⭐ Acknowledgements

Special thanks to:

- **Tips Hindawi**
- **Edrak for AI**
- **LangChain**
- **Hugging Face**
- **Mistral AI**
- **FAISS**
- **Tavily**
- **Streamlit**

Their tools and educational resources made this project possible.
