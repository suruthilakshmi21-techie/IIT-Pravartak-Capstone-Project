from src.rag_pipeline.rag_search import RAGSearch

class DiseaseAgent:
    def __init__(self):
        self.rag = RAGSearch()

    def get_latest_info(self, disease: str):
        """
        Fetch latest treatment info using RAG pipeline.
        """
        return self.rag.search(disease)