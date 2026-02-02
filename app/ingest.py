from sentence_transformers import SentenceTransformer
from endee import Endee

INDEX_NAME = "documents"

model = SentenceTransformer("all-MiniLM-L6-v2")

# Endee client (reads ENDEE_URL from env)
client = Endee()

# Get index handle
index = client.index(INDEX_NAME)


def ingest_texts(texts):
    embeddings = model.encode(texts)

    points = []
    for i, (text, vector) in enumerate(zip(texts, embeddings)):
        points.append({
            "id": f"doc-{i}",
            "vector": vector.tolist(),
            "metadata": {
                "text": text
            }
        })

    # Bulk insert via index object
    index.upsert(points)


if __name__ == "__main__":
    sample_texts = [
        "Endee is a high-performance vector database designed for fast similarity search.",
        "Retrieval Augmented Generation combines vector search with language models.",
        "Semantic search retrieves information based on meaning rather than keywords."
    ]

    ingest_texts(sample_texts)
    print("Ingestion completed.")
