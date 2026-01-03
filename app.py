import streamlit as st
import os
from pdf_loader import load_and_split_pdf
from vector_store import create_vector_store
from chat import get_qa_chain

st.set_page_config(page_title="Chat with PDFs (RAG)")
st.title("📄 Chat with Your PDFs")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("PDF uploaded successfully!")

    with st.spinner("Processing document..."):
        documents = load_and_split_pdf("temp.pdf")
        vector_store = create_vector_store(documents)
        qa_chain = get_qa_chain(vector_store)

    st.success("You can now ask questions!")

    query = st.text_input("Ask a question from the PDF")

    if query:
        with st.spinner("Generating answer..."):
            response = qa_chain.run(query)
        st.write("### Answer:")
        st.write(response)
