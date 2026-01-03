# 📄 Chat with PDFs using RAG (Retrieval-Augmented Generation)

This project is a Retrieval-Augmented Generation (RAG) based application that allows users to upload PDF documents and ask questions based on their content.

The system focuses on semantic search and document retrieval using vector embeddings and a vector database. It demonstrates the complete RAG pipeline in a stable, Windows-compatible setup.

---

## 🚀 Features

- Upload and process PDF documents
- Extract and chunk text intelligently
- Generate vector embeddings for semantic search
- Store and retrieve embeddings using FAISS
- Answer user queries based on retrieved document context
- Interactive interface using Streamlit
- Modular and extensible architecture

---

## 🧠 Architecture Overview

1. PDF Ingestion – Extracts text from uploaded PDF files  
2. Text Chunking – Splits text into overlapping chunks  
3. Embeddings – Converts text chunks into numerical vectors  
4. Vector Database – Stores embeddings using FAISS  
5. Retrieval-Based QA – Retrieves relevant context for user queries  

---

## 🛠 Tech Stack

- Python
- LangChain
- FAISS
- Sentence Transformers
- PyPDF
- Streamlit

---

## 📂 Project Structure

Chat-with-PDFs-RAG/
│
├── app.py               # Streamlit application
├── pdf_loader.py        # PDF loading and text processing
├── vector_store.py      # FAISS vector store creation
├── chat.py              # Retrieval-based QA logic
├── requirements.txt     # Project dependencies
├── .gitignore           # Git ignore rules
└── README.md

---

## ▶️ How to Run

1. Clone the repository
   git clone https://github.com/SciddhantoSinha/Rag-Chat-With-Pdfs.git

2. Navigate to the project directory
   cd Rag-Chat-With-Pdfs

3. Create and activate a virtual environment
   python -m venv venv
   venv\Scripts\activate

4. Install dependencies
   pip install -r requirements.txt

5. Run the application
   python -m streamlit run app.py

---

## ⚠️ Notes

- This project focuses on RAG pipeline architecture and retrieval accuracy
- The LLM layer is intentionally abstracted for stability on Windows
- The design supports easy integration with OpenAI or Ollama in Linux/WSL environments

---

## 📌 Future Enhancements

- Conversational memory support
- Multi-PDF querying
- Source citations in answers
- Integration with local LLMs
- UI enhancements

---

## 👤 Author

Sciddhanto Sinha
