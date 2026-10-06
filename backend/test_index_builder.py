from rag.index_builder import IndexBuilder

builder = IndexBuilder()

builder.build(
    "../uploads/documents",
    "../vector_store"
)