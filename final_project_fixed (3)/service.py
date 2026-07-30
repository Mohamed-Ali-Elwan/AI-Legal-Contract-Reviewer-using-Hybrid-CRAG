import os
import tempfile

from pdf_loader import PDF
from rag import rag
from search import Search
from crag import CRAG

from parser import OutputParser
from chains import ReviewChains
from llm import KaggleLLM


DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")


class ReviewService:

    def __init__(
    self,
    tavily_api_key: str,
    kaggle_endpoint_url: str,
    kaggle_api_key: str
    ):

        # Components

        self.rag = rag()
        self._load_local_legal_corpus()

        self.search = Search(tavily_api_key)

        self.crag = CRAG(
            rag_system=self.rag,
            web_search=self.search
        )

        self.llm = KaggleLLM.get_llm(endpoint_url=kaggle_endpoint_url, api_key=kaggle_api_key)

        self.parser = OutputParser()

        self.chains = ReviewChains(self.llm)

    ####################################################################

    def _load_local_legal_corpus(self):
        # The local vectorstore was never being populated anywhere, so
        # CRAG's "local" branch always raised
        # "Vectorstore has not been created." Index every PDF sitting in
        # data/ (e.g. the bundled Egyptian-law reference material) on
        # startup so local retrieval actually has something to search.
        if not os.path.isdir(DATA_DIR):
            return

        chunks = []

        for filename in os.listdir(DATA_DIR):
            if filename.lower().endswith(".pdf"):
                loader = PDF(os.path.join(DATA_DIR, filename))
                documents = loader.load()
                chunks.extend(loader.split(documents))

        if chunks:
            self.rag.create_vectorstore(chunks)

    ####################################################################

    @staticmethod
    def _format_context(context: dict) -> str:
        # crag.retrieve() returns a dict shaped one of three ways
        # ("local", "web", or "hybrid" - see crag.py), mixing LangChain
        # Document objects with raw Tavily result dicts. Passing that dict
        # straight into a {context} prompt placeholder just str()'d the
        # whole structure into the LLM prompt. Flatten it into readable text
        # instead.
        pieces = []

        for doc in context.get("documents", []) or []:
            pieces.append(getattr(doc, "page_content", str(doc)))

        for doc in context.get("local_documents", []) or []:
            pieces.append(getattr(doc, "page_content", str(doc)))

        for doc in context.get("web_documents", []) or []:
            if isinstance(doc, dict):
                pieces.append(doc.get("content") or doc.get("url", ""))
            else:
                pieces.append(str(doc))

        return "\n\n".join(p for p in pieces if p) or "No legal context found."

    ####################################################################

    def review(self, contract_text: str):

        # -------------------------------------------------------------
        # Step 1 : Extract Clauses
        # -------------------------------------------------------------

        clauses = self.chains.clause_chain.run(
            contract=contract_text
        )

        # -------------------------------------------------------------
        # Step 2 : Generate Search Query
        # -------------------------------------------------------------

        search_query = self.chains.search_chain.run(
            clause=clauses
        )

        # -------------------------------------------------------------
        # Step 3 : Retrieve Legal Context
        # -------------------------------------------------------------

        raw_context = self.crag.retrieve(search_query)
        context = self._format_context(raw_context)

        # -------------------------------------------------------------
        # Step 4 : Review Contract
        # -------------------------------------------------------------

        response = self.chains.review_chain.run(

            contract=contract_text,

            context=context,

            format_instructions=self.parser.get_format_instructions()

        )

        # -------------------------------------------------------------
        # Step 5 : Parse Output
        # -------------------------------------------------------------
        print("=" * 80)
        print(response)
        print("=" * 80)
        result = self.parser.parse(response)

        return result

    def review_pdf(self, uploaded_file):
        # `uploaded_file` is a Streamlit UploadedFile (file-like object), but
        # PyPDFLoader (used inside PDF.load()) needs a real path on disk.
        # The old code instantiated PDF() with no path at all and then
        # called .load(uploaded_file), neither of which matches PDF's
        # actual signature. Persist to a temp file and load from there.
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name

        try:
            loader = PDF(tmp_path)
            documents = loader.load()
            contract_text = "\n".join(doc.page_content for doc in documents)
            return self.review(contract_text)
        finally:
            os.remove(tmp_path)
