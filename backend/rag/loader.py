import os
from typing import List

from langchain_core.documents import Document

from langchain_community.document_loaders import (
    PyPDFLoader,
    CSVLoader,
    TextLoader,
    Docx2txtLoader
)


class DocumentLoader:

    def __init__(self):
        pass

    def load(self, file_path: str) -> List[Document]:
        """
        Detect file type automatically and return
        LangChain Document objects.
        """

        extension = os.path.splitext(file_path)[1].lower()

        if extension == ".pdf":
            return self.load_pdf(file_path)

        elif extension == ".csv":
            return self.load_csv(file_path)

        elif extension == ".txt":
            return self.load_txt(file_path)

        elif extension == ".docx":
            return self.load_docx(file_path)

        else:
            raise ValueError(f"Unsupported file type: {extension}")

    def load_pdf(self, file_path: str) -> List[Document]:
        loader = PyPDFLoader(file_path)
        return loader.load()

    def load_csv(self, file_path: str) -> List[Document]:
        loader = CSVLoader(file_path=file_path)
        return loader.load()

    def load_txt(self, file_path: str) -> List[Document]:
        loader = TextLoader(
            file_path=file_path,
            encoding="utf-8"
        )
        return loader.load()

    def load_docx(self, file_path: str) -> List[Document]:
        loader = Docx2txtLoader(file_path)
        return loader.load()