from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


class VectorStore:
    def __init__(self):
        # Initialize the embedding model
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        self.store = None

    def build_store(self, documents):
        """
        Build a FAISS vector store from a list of text documents.
        """
        self.store = FAISS.from_texts(
            documents,
            self.embeddings
        )

    def search(self, query, k=2):
        """
        Perform semantic search on the stored documents.
        """
        if self.store is None:
            return ["No memory store built yet."]

        results = self.store.similarity_search(
            query,
            k=k
        )

        return [r.page_content for r in results]