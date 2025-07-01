# embeddings/embed_store_faiss.py

import os
from pathlib import Path
import fitz  # PyMuPDF
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from text_processor import process_document


def extract_text_from_pdf(pdf_path):
    """Extract full text from a PDF using PyMuPDF."""
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text


# Set embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2",
    model_kwargs={"device": "cpu"}  # or "cuda" if using GPU
)

# Load documents from the data folder
data_dir = Path("data/")
all_chunks = []

for file_path in data_dir.glob("**/*"):
    if file_path.is_file():
        raw_text = ""
        
        # Handle .txt and .md files
        if file_path.suffix.lower() in [".txt", ".md"]:
            with open(file_path, "r", encoding="utf-8") as f:
                raw_text = f.read()

        # Handle .pdf files
        elif file_path.suffix.lower() == ".pdf":
            raw_text = extract_text_from_pdf(file_path)

        if raw_text.strip():  # Only process non-empty files
            chunks = process_document(raw_text)
            all_chunks.extend(chunks)
            print(f"✅ Processed: {file_path.name} - {len(chunks)} chunks")

if not all_chunks:
    raise ValueError("❌ No documents found or processed from `data/` folder.")

# Build and save FAISS vector store
faiss_db = FAISS.from_texts(texts=all_chunks, embedding=embedding_model)
faiss_db.save_local("embeddings/faiss_index")
print("✅ FAISS index saved with total chunks:", len(all_chunks))