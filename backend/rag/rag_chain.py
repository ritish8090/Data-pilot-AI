from rag.retriever import Retriever
from rag.prompts import RAG_PROMPT
from llm import ask_gemini


class RAGChain:

    def __init__(self, vector_path="../vector_store"):

        self.retriever = Retriever(vector_path)

    def ask(self, question: str):

        docs = self.retriever.retrieve(question)

        context = "\n\n".join(
            doc.page_content
            for doc in docs
        )

        prompt = RAG_PROMPT.format(
            context=context,
            question=question
        )

        answer = ask_gemini(prompt)

        return {
            "question": question,
            "answer": answer,
            "context": docs
        }