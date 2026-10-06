from rag.loader import DocumentLoader
from rag.splitter import DocumentSplitter
from rag.vector_store import VectorStore

loader = DocumentLoader()

docs = loader.load("../uploads/csv/Sample - Superstore.csv")

splitter = DocumentSplitter()

chunks = splitter.split(docs)

print("Chunks:", len(chunks))

vector_db = VectorStore()

db = vector_db.create(
    chunks,
    "../vector_store"
)

print("\nVector database created successfully!")

print("\nTotal vectors:", db.index.ntotal)