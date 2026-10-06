from rag.embeddings import EmbeddingModel

embedding_model = EmbeddingModel()

embeddings = embedding_model.get_embeddings()

vector = embeddings.embed_query(
    "Which category has the highest sales?"
)

print("Vector Length:", len(vector))

print("\nFirst 10 Values:")

print(vector[:10])