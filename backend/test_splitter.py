from rag.loader import DocumentLoader
from rag.splitter import DocumentSplitter

loader = DocumentLoader()

docs = loader.load("../uploads/csv/Sample - Superstore.csv")

print("Original Documents:", len(docs))

splitter = DocumentSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split(docs)

print("Chunks:", len(chunks))

print("\nFirst Chunk:\n")
print(chunks[0].page_content)