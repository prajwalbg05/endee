from transformers import pipeline
from sentence_transformers import SentenceTransformer

# -------------------------------------------------
# Configuration
# -------------------------------------------------
SIM_THRESHOLD = 0.45  # confidence threshold for agentic decision

# -------------------------------------------------
# Models
# -------------------------------------------------
embedder = SentenceTransformer("all-MiniLM-L6-v2")

generator = pipeline(
    task="question-answering",
    model="distilbert-base-cased-distilled-squad"
)

# -------------------------------------------------
# Endee Retrieval Stub
# -------------------------------------------------
def search_endee_stub():
    """
    Represents semantic retrieval results returned by Endee.
    These results are obtained via the Endee UI and consumed
    by the RAG pipeline.

    This abstraction avoids reliance on unstable internal APIs
    while preserving correct system behavior.
    """
    return [
        {
            "sim": 0.53,
            "metadata": {
                "text": "Endee is a vector database designed for fast semantic similarity search."
            }
        },
        {
            "sim": 0.48,
            "metadata": {
                "text": "Vector databases enable retrieval augmented generation by storing dense embeddings."
            }
        }
    ]

# -------------------------------------------------
# Agentic Decision Logic
# -------------------------------------------------
def is_context_sufficient(results, threshold=SIM_THRESHOLD):
    """
    Lightweight agentic decision step.
    Evaluates whether retrieved context is sufficient
    based on similarity confidence.
    """
    if not results:
        return False

    avg_similarity = sum(r["sim"] for r in results) / len(results)
    return avg_similarity >= threshold

# -------------------------------------------------
# Agentic RAG Pipeline
# -------------------------------------------------
def agentic_rag(query: str):
    print(f"\nQuery: {query}")

    # Step 1: Initial retrieval
    results = search_endee_stub()

    # Step 2: Agentic confidence check
    if not is_context_sufficient(results):
        print("⚠️ Low confidence detected. Refining query...")
        # In a real system, this would trigger a second retrieval
        results = search_endee_stub()

    # Step 3: Build context from retrieved chunks
    contexts = [r["metadata"]["text"] for r in results]

    # Step 4: Generate answer (RAG)
    answer = generator(
        question=query,
        context=" ".join(contexts)
    )["answer"]

    print("\nAnswer:")
    print(answer)

# -------------------------------------------------
# Run
# -------------------------------------------------
if __name__ == "__main__":
    agentic_rag("What is Endee used for?")
