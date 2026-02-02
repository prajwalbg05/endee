import json
import pyperclip

vectors = json.load(open("data/vectors.json"))

for v in vectors:
    payload = {
        "id": v["id"],
        "vector": v["vector"],
        "metadata": v["metadata"]
    }
    pyperclip.copy(json.dumps(payload))
    input("Copied next vector to clipboard. Press Enter to continue...")
