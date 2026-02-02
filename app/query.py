from sentence_transformers import SentenceTransformer
import json
import os

model = SentenceTransformer("all-MiniLM-L6-v2")

query = "What is Endee used for?"

vector = model.encode(query)

os.makedirs("data", exist_ok=True)

with open("data/query_vector.json", "w") as f:
    json.dump(vector.tolist(), f)

print("Query:", query)
print("Vector length:", len(vector))
print("Saved query vector to data/query_vector.json")
