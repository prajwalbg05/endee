from sentence_transformers import SentenceTransformer
import json

model = SentenceTransformer("all-MiniLM-L6-v2")

text = "Endee is a high-performance vector database for semantic search."

vector = model.encode(text)

print("Vector length:", len(vector))
print(json.dumps(vector.tolist()))
