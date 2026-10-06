from rag.rag_chain import RAGChain

rag = RAGChain()

question = "Which customer purchased Bookcases?"

result = rag.ask(question)

print("\nQuestion:\n")
print(result["question"])

print("\nAnswer:\n")
print(result["answer"])