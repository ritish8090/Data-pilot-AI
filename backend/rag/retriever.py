from typing import List

from langchain_core.documents import Document

from rag.vector_store import VectorStore


class Retriever:

    def __init__(self, vector_path: str):

        self.db = VectorStore().load(vector_path)

    def retrieve(
        self,
        query: str,
        k: int = 5
    ) -> List[Document]:
        """
        Retrieve the top-k most relevant chunks.
        """

        docs = self.db.similarity_search(
            query,
            k=k
        )

        return docs