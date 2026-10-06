from rag.retriever import Retriever

retriever = Retriever("../vector_store")

query = "Which furniture products generated the highest sales?"

docs = retriever.retrieve(query)

print(f"Retrieved {len(docs)} documents\n")

for i, doc in enumerate(docs, start=1):
    print("=" * 60)
    print(f"Document {i}")
    print("=" * 60)
    print(doc.page_content)
    print()