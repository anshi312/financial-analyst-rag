# 📊 Financial Analyst RAG Assistant

A Retrieval-Augmented Generation (RAG) application for answering financial questions using real company reports (10-K, earnings releases, etc.) powered by FAISS, LangChain, and HuggingFace embeddings.

## 🔍 Overview

This project enables analysts and users to query financial data directly from embedded corporate filings and reports. Documents are chunked, embedded with `all-MiniLM-L6-v2`, and stored in a FAISS vector store to support fast, relevant semantic search.

<p align="center">
  <img src="docs/demo-screenshot.png" width="600" alt="Demo Screenshot">
</p>


---

## 🚀 Features

- 📄 **PDF support**: Upload financial reports in PDF format
- 🔍 **Semantic search**: Embeds and chunks documents using Sentence Transformers
- 🧠 **RAG pipeline**: Combines retrieval and local HuggingFace QA
- 🖥️ **Streamlit UI**: Simple frontend interface
- 💾 **FAISS vector store**: Fast local document retrieval
- 🔐 **OpenAI API support (optional)**

---

## 🧪 Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/anshi312/financial-analyst-rag.git
cd financial-analyst-rag
```
2. **Create virtual environment**

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
3. **Prepare your PDFs**

Place your financial PDF documents inside the data/ folder.

4. **Embed the documents**

```bash
python embeddings/embed_store_faiss.py
```
5. Run the application

```bash
python app.py
```		

⸻

## 🧠 Technologies Used
	•	Python 3.10+
	•	LangChain
	•	FAISS
	•	HuggingFace Sentence Transformers
	•	PyMuPDF
	•	OpenAI API (optional)

⸻

## 🛡️ Security Notes
	•	API secrets are ignored via .gitignore
	•	You can store your OpenAI API key in config/.env (optional)

Example:

OPENAI_API_KEY=your-key-here

🚨 Avoid hardcoding secrets in source files. Use .env instead.

⸻

## 📁 Project Structure

financial-analyst-rag/
│
├── app.py                     # Main app entrypoint
├── data/                      # Contains financial PDF files
├── embeddings/               # Embedding scripts and FAISS index
│   ├── embed_store_faiss.py
│   └── text_processor.py
│
├── rag/                       # RAG pipeline setup
│   ├── rag_pipeline.py
│   └── setup_rag.py
│
├── scraping/                  # Web scrapers (if needed)
│   ├── earnings_scraper.py
│   ├── sec_scraper.py
│   └── utils.py
│
├── test_env.py                # Environment variable tester
├── test_hf_pipeline.py        # Pipeline test script
├── requirements.txt           # All dependencies
├── .gitignore
└── README.md

⸻

## 💡 Example Use Cases
	•	“What was Netflix’s total revenue in 2024?”
	•	“Apple’s net income breakdown by product?”
	•	“Compare Microsoft and Apple’s R&D spending.”

⸻

## 📄 License

This project is licensed under the MIT License.

⸻

## 🙋‍♀️ Author

Anshi Shah
📧 ans10020@nyu.edu
🔗 LinkedIn
🎓 MS in Computer Engineering @ NYU Tandon
💡 Passionate about AI, MLOps, and Financial Automation


