from rag.loader import DocumentLoader

loader = DocumentLoader()

docs = loader.load("../uploads/csv/Sample - Superstore.csv")

print("Total Documents:", len(docs))
print(docs[0].page_content[:500])