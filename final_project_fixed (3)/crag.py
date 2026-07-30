from rag import rag
from search import Search



class CRAG:

    def __init__(
        self,
        rag_system: rag,
        web_search: Search,
        score_threshold: float = 0.75
    ):

        self.rag = rag_system
        self.web = web_search
        self.score_threshold = score_threshold

    def retrieve(
        self,
        query: str,
        k: int = 5
    ):

        local_docs = self.rag.retrieve_with_score(query, k)

        if not local_docs:
            return {
                "source": "web",
                "documents": self.web.search(query)
            }

        best_score = local_docs[0][1]

        if best_score <= self.score_threshold:

            docs = [doc for doc, _ in local_docs]

            return {
                "source": "local",
                "documents": docs
            }

        web_docs = self.web.search(query)

        docs = [doc for doc, _ in local_docs]

        return {
            "source": "hybrid",
            "local_documents": docs,
            "web_documents": web_docs
        }