from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
import torch

embedding_model_name = "sentence-transformers/all-MiniLM-L6-v2"

class rag:
    
    def __init__(self):
        self.embedding_model = HuggingFaceEmbeddings(model_name=embedding_model_name, model_kwargs={"device": "cuda" if torch.cuda.is_available() else "cpu"})
        self.vectorstore = None

    def create_vectorstore(self, documents):
        self.vectorstore = FAISS.from_documents(documents, self.embedding_model)

    def retrieve(self, query: str, k: int = 5):
        if self.vectorstore is None:
            raise ValueError("Vectorstore has not been created. Please call create_vectorstore() first.")
        return self.vectorstore.similarity_search(query, k=k)
    
    
    
    def retrieve_with_score(self, query: str, k: int = 5):
        if self.vectorstore is None:
            raise ValueError(
                "Vectorstore has not been created."
            )

        return self.vectorstore.similarity_search_with_score(query,k=k)