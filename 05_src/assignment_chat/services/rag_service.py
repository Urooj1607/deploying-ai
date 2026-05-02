import os
import chromadb
from chromadb.utils import embedding_functions


DATA_PATH = "data/health_notes.txt"
CHROMA_PATH = "chroma_db"


def load_text_data():
    with open(DATA_PATH, "r", encoding="utf-8") as file:
        text = file.read()

    chunks = [chunk.strip() for chunk in text.split("\n\n") if chunk.strip()]
    return chunks


def build_vector_database():
    """
    Builds a persistent ChromaDB database from the local text dataset.
    """
    client = chromadb.PersistentClient(path=CHROMA_PATH)

    embedding_function = embedding_functions.DefaultEmbeddingFunction()

    collection = client.get_or_create_collection(
        name="health_research_notes",
        embedding_function=embedding_function
    )

    chunks = load_text_data()

    ids = [f"chunk_{i}" for i in range(len(chunks))]

    existing = collection.get()

    if len(existing["ids"]) == 0:
        collection.add(
            documents=chunks,
            ids=ids
        )

    return collection


def semantic_search_answer(question: str) -> str:
    """
    Searches the ChromaDB collection and returns a natural-language answer.
    """
    collection = build_vector_database()

    results = collection.query(
        query_texts=[question],
        n_results=2
    )

    documents = results["documents"][0]

    if not documents:
        return "I could not find relevant information in the dataset."

    context = "\n".join(documents)

    return f"""
Based on the healthcare research notes, here is the most relevant information:

{context}

Simple answer:
The information above is the closest match from the dataset. You can use it to answer your question or develop a research explanation.
"""