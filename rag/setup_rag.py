from langchain_community.vectorstores import FAISS
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from langchain.chains import RetrievalQA
from langchain_huggingface import HuggingFaceEmbeddings, HuggingFacePipeline

# 1. Embedding model for document chunks
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# 2. Load FAISS vectorstore (with security flag)
vectorstore = FAISS.load_local("embeddings/faiss_index", embeddings=embedding_model, allow_dangerous_deserialization=True)

# 3. HuggingFace local model (lightweight and RAM-safe)
model_id = "google/flan-t5-base"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSeq2SeqLM.from_pretrained(model_id)

pipe = pipeline("text2text-generation", model=model, tokenizer=tokenizer)
llm = HuggingFacePipeline(pipeline=pipe)

# 4. Create retriever and QA chain
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
rag_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)