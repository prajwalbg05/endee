from sentence_transformers import SentenceTransformer
import json
import uuid

CHUNK_SIZE = 20  # words per chunk

model = SentenceTransformer("all-MiniLM-L6-v2")


def load_docs(path="data/docs.txt"):
    with open(path) as f:
        return f.read()


def chunk_text(text, size):
    words = text.split()
    return [
        " ".join(words[i:i + size])
        for i in range(0, len(words), size)
    ]


def generate_vectors(chunks):
    embeddings = model.encode(chunks)
    vectors = []

    for chunk, emb in zip(chunks, embeddings):
        vectors.append({
            "id": str(uuid.uuid4()),
            "vector": emb.tolist(),
            "metadata": {
                "text": chunk
            }
        })

    return vectors


if __name__ == "__main__":
    raw_text = load_docs()
    chunks = chunk_text(raw_text, CHUNK_SIZE)
    vectors = generate_vectors(chunks)

    with open("data/vectors.json", "w") as f:
        json.dump(vectors, f, indent=2)

    print(f"Generated {len(vectors)} vectors.")
    print("Saved to data/vectors.json")
