import os

from dotenv import load_dotenv
from langchain_classic.chains import RetrievalQA
from langchain_openai import OpenAI
from src.memory.vector_store import VectorStore


class RAGSearch:
    def __init__(self):
        load_dotenv()

        openai_key = os.getenv("OPENAI_API_KEY")

        if not openai_key:
            raise ValueError("No OpenAI API key found in .env")

        self.vs = VectorStore()

        docs = [
            "Chronic kidney disease treatment includes dialysis and kidney transplant.",
            "AI-driven monitoring helps track patient vitals in real time.",
            "New immunotherapy methods are being explored for kidney disease."
        ]

        self.vs.build_store(docs)

        self.qa = RetrievalQA.from_chain_type(
            llm=OpenAI(
                temperature=0,
                api_key=openai_key
            ),
            retriever=self.vs.store.as_retriever()
        )

    def search(self, disease: str):
        return self.qa.invoke(
            f"Summarize latest treatment methods for {disease}"
        )