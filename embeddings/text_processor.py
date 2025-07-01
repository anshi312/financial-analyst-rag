import re
from langchain.text_splitter import RecursiveCharacterTextSplitter

def clean_text(text):
    # Remove HTML tags
    text = re.sub(r"<.*?>", "", text)
    # Remove multiple spaces, tabs, and line breaks
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def chunk_text(text, chunk_size=1000, chunk_overlap=200):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ".", " "],  # logical breaks
        length_function=len
    )
    return splitter.split_text(text)

def process_document(raw_text):
    clean = clean_text(raw_text)
    chunks = chunk_text(clean)
    return chunks