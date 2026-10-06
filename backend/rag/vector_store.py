import os
from typing import List

from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS

from rag.embeddings import EmbeddingModel


class VectorStore:

    def __init__(self):

        self.embedding_model = EmbeddingModel().get_embeddings()

    def create(self, documents: List[Document], save_path: str):

        db = FAISS.from_documents(
            documents,
            self.embedding_model
        )

        db.save_local(save_path)

        return db

    def load(self, save_path: str):

        if not os.path.exists(save_path):
            raise FileNotFoundError(
                f"Vector store not found: {save_path}"
            )

        db = FAISS.load_local(
            save_path,
            self.embedding_model,
            allow_dangerous_deserialization=True
        )

        return db