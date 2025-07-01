import streamlit as st
from rag.setup_rag import rag_chain, retriever

st.set_page_config(page_title="📊 Financial Analyst RAG", layout="centered")

st.title("📊 Financial Analyst RAG Assistant")
st.markdown("Ask financial questions based on your embedded documents.")

# Input box for user query
query = st.text_input("Enter your financial question 👇", "")

if query:
    with st.spinner("🔍 Retrieving relevant context and generating answer..."):
        try:
            # Get relevant documents
            docs = retriever.get_relevant_documents(query)

            if not docs:
                st.error("❌ No relevant documents found. Try uploading more data or rephrasing your question.")
            else:
                # Display retrieved chunks (optional for debugging)
                with st.expander("🔎 Retrieved Chunks"):
                    for d in docs:
                        st.markdown(f"- {d.page_content[:300]}...")

                # Run RAG pipeline
                answer = rag_chain.run(query)
                st.success("✅ Answer generated:")
                st.markdown(f"**{answer}**")

        except Exception as e:
            st.error(f"🚨 Error: {str(e)}")