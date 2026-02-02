from transformers import pipeline

# Retrieved from Endee search results
retrieved_chunks = [
   "factual accuracy. Vector databases store dense embeddings instead of raw text. Endee is a vector database designed for fast semantic"
   "Retrieval Augmented Generation is a technique used in modern AI systems. It combines vector search with language models to improve"
]

question = "What is Endee used for?"

context = " ".join(retrieved_chunks)

qa_pipeline = pipeline(
    "question-answering",
    model="distilbert-base-cased-distilled-squad"
)

result = qa_pipeline(
    question=question,
    context=context
)

print("Answer:")
print(result["answer"])
