# Endee-based Retrieval Augmented Generation (RAG) System

A compact, production-oriented Retrieval-Augmented Generation (RAG) system that uses Endee as the vector database to provide grounded, explainable answers from domain documents.

---

## Table of Contents
- [Overview](#overview)
- [Problem Statement](#problem-statement)
- [Solution Summary](#solution-summary)
- [High-Level Architecture](#high-level-architecture)
- [Technical Components](#technical-components)
- [Setup & Execution](#setup--execution)
- [Usage Example](#usage-example)
- [Notes & Limitations](#notes--limitations)
- [AI Assistance Disclosure](#ai-assistance-disclosure)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

This project implements a Retrieval-Augmented Generation (RAG) pipeline where user queries are answered using text retrieved from a vector database (Endee). Instead of relying only on an LLM's internal knowledge, answers are grounded in semantically relevant document chunks stored in Endee.

## Problem Statement

Large Language Models (LLMs) are powerful but commonly suffer from:
- Hallucinations (confident but incorrect outputs)
- Lack of grounding in private or domain-specific data
- Outdated knowledge

This project mitigates these problems by retrieving relevant document content and generating answers strictly from the retrieved context.

## Solution Summary

- Chunk documents and create dense embeddings.
- Store embeddings in Endee (vector DB).
- Embed incoming queries and perform similarity search in Endee.
- Assemble retrieved chunks as context and generate responses that are grounded in those chunks.
- Optionally re-run retrieval with a refined query when confidence is low (lightweight agentic loop).

## High-Level Architecture

Documents
  ↓
Text Chunking
  ↓
Embedding (sentence-transformers: all-MiniLM-L6-v2)
  ↓
Endee vector DB (cosine similarity)
  ↓
Top-K retrieval
  ↓
RAG answer generation (QA model using retrieved context)

---

## Technical Components

### Embedding Model
- Model: sentence-transformers/all-MiniLM-L6-v2
- Output: 384-dimensional dense vectors

### Vector Database
- Endee — stores vectors and performs cosine-similarity searches
- Index recommended: name `documents`, dim `384`, metric `cosine`

### RAG Pipeline
- Query → embedding → Endee top-K retrieval → pass retrieved text to QA model → answer generation constrained to retrieved content

### Lightweight Agentic Extension
- Evaluate retrieval confidence using similarity scores
- If confidence < threshold, optionally reformulate query and re-retrieve
- This is a controlled decision loop (no open-ended autonomous actions)

---

## Setup & Execution

Prerequisites
- Ubuntu (WSL supported)
- Python 3.10+
- Git
- Endee running locally

1. Start Endee
```bash
# ensure WSL /mnt/data is available (if using WSL)
sudo mkdir -p /mnt/data
sudo chown -R $USER:$USER /mnt/data

cd ~/endee
./build/ndd-avx2

# Endee UI should be available at:
# http://localhost:8080
```

2. Create Index in Endee (via UI)
- Index name: `documents`
- Dimension: `384`
- Distance metric: `cosine`

3. Set up Python environment
```bash
cd ~/endee-rag-project
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

4. Add documents
```bash
# Add or edit documents to ingest
nano data/docs.txt
```

5. Run ingestion pipeline (creates chunks, embeddings, and prepares vectors for Endee)
```bash
python app/ingest_pipeline.py
```
Note: Vectors are inserted using a clipboard-assisted helper:
```bash
python app/clipboard_ingest.py
# (this automates copying prepared vectors into Endee's ingestion path)
```

6. Run the RAG pipeline
```bash
python app/rag.py
```

---

## Usage Example

Query:
```
What is Endee used for?
```

Sample Answer (grounded in retrieved context):
```
Fast semantic similarity search
```

This demonstrates retrieval of relevant document chunks and generating answers strictly from retrieved content.

---

## Notes & Limitations

- At implementation time, Endee exposes much of its vector search functionality primarily through its UI; programmatic APIs may be limited or evolving.
- Ensure embeddings and index dimensions match (e.g., 384 for the specified embedding model).
- The reliability of answers depends on the quality and coverage of the ingested documents.
- For production, consider:
  - Persistence and backups for Endee indices
  - Monitoring recall/precision of retrieval
  - Rate-limiting and secure access to any APIs

---

## AI Assistance Disclosure

This project was developed with assistance from ChatGPT used as a productivity and learning tool. ChatGPT helped with:
- Explaining RAG architecture concepts
- Troubleshooting integration issues
- Improving structure and documentation clarity

All code design, implementation, testing, and final decisions were performed and validated by the project author.

---

## Contributing

Contributions, issues, and feature requests are welcome. Please open an issue or submit a PR describing the change. For small documentation improvements, feel free to propose edits directly.

---

## License

Specify your license here (e.g., MIT). Add a LICENSE file to the repository if not present.
