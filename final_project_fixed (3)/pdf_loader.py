from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter

class PDF:                
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load(self):
        loader = PyPDFLoader(self.file_path)
        return loader.load()
    
    def split(self, documents):
        splitter = CharacterTextSplitter(chunk_size=600, chunk_overlap=100)
        return splitter.split_documents(documents)
