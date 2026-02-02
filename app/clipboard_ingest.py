import json
import pyperclip

vectors = json.load(open("data/vectors.json"))

print(f"Loaded {len(vectors)} vectors.")
print("Each vector will be copied to clipboard as a single payload.\n")

for i, v in enumerate(vectors, start=1):
    payload = {
        "id": v["id"],
        "vector": v["vector"],
        "metadata": v["metadata"]
    }

    pyperclip.copy(json.dumps(payload))
    print(f"[{i}/{len(vectors)}] Vector copied to clipboard.")
    input("→ Paste into Endee UI and press Enter to continue...")
