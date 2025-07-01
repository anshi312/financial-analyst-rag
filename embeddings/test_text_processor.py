# embeddings/test_text_processor.py

from text_processor import process_document

sample_text = """Apple Inc. reported record revenue of $90 billion in Q1 2024.
This was driven by strong demand for iPhones and Services..."""

chunks = process_document(sample_text)

for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}:\n{chunk}\n{'-'*40}")