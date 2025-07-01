from langchain_community.vectorstores import FAISS
# from langchain_community.embeddings import HuggingFaceEmbeddings
from sentence_transformers import SentenceTransformer
from langchain_huggingface import HuggingFaceEmbeddings

# No need for OpenAI API key anymore

# Load the same model used during FAISS index creation
embedding_model = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2",
    model_kwargs={"device": "cpu"}  # Use "cuda" if you have GPU
)

# Load FAISS index
db = FAISS.load_local("embeddings/faiss_index", embeddings=embedding_model, allow_dangerous_deserialization=True)

# Test query
query = "How much revenue did Apple make in Q1 2024?"
docs = db.similarity_search(query)

# Show results
for doc in docs:
    print("🔎 Result:\n", doc.page_content)