# rag/rag_pipeline.py

from rag.setup_rag import retriever, rag_chain

# Ask your query
query = "How much revenue did Apple make in Q1 2024?"

# Retrieve relevant documents
docs = retriever.get_relevant_documents(query)

print("\n🔍 Retrieved Chunks:")
for d in docs:
    print("-", d.page_content[:150])

# If no relevant documents, notify user
if not docs:
    print("❌ No relevant documents found. Try uploading more data.")
else:
    # Run RAG pipeline
    result = rag_chain.run(query)
    print("\n💬 Final RAG Answer:\n", result)