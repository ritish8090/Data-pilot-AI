import os

from rag.loader import DocumentLoader
from rag.splitter import DocumentSplitter
from rag.vector_store import VectorStore


class IndexBuilder:

    def __init__(self):

        self.loader = DocumentLoader()
        self.splitter = DocumentSplitter()
        self.vector_store = VectorStore()

    def build(self, folder_path, save_path):

        documents = []

        for filename in os.listdir(folder_path):

            path = os.path.join(folder_path, filename)

            if os.path.isfile(path):

                try:
                    docs = self.loader.load(path)
                    documents.extend(docs)

                except Exception as e:
                    print(f"Skipping {filename}: {e}")

        print(f"Loaded {len(documents)} documents")

        chunks = self.splitter.split(documents)

        print(f"Created {len(chunks)} chunks")

        self.vector_store.create(
            chunks,
            save_path
        )

        print("Vector Store Updated")