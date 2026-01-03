from langchain.chains import RetrievalQA
from langchain.llms.fake import FakeListLLM

def get_qa_chain(vector_store):
    llm = FakeListLLM(
        responses=[
            "This answer is generated from the document context using a RAG pipeline."
        ]
    )

    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vector_store.as_retriever()
    )
