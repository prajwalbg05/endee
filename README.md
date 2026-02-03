**Endee-based Retrieval Augmented Generation (RAG) System**
Project Overview & Problem Statement
Overview

This project implements a Retrieval Augmented Generation (RAG) system using Endee as the vector database.
The system enables semantic search over documents and generates answers that are grounded in retrieved context, rather than relying solely on a language model.

Problem Statement

Large Language Models (LLMs) can generate fluent responses but often suffer from:

Hallucinations

Lack of grounding in domain-specific data

Outdated or missing knowledge

This project addresses these issues by:

Retrieving relevant document chunks using vector similarity search

Augmenting the user query with retrieved context

Generating answers strictly from retrieved information

Endee is used as the core vector search engine that enables this workflow.

**System Design / Technical Approach**
High-Level Architecture

Documents
   ↓
Text Chunking
   ↓
Embedding Generation (SentenceTransformer)
   ↓
Endee Vector Database
   ↓
Semantic Similarity Search
   ↓
Retrieved Context
   ↓
Answer Generation (RAG)

**Technical Components**

Embedding Model

Sentence-Transformers (all-MiniLM-L6-v2)

Produces 384-dimensional dense vectors

Vector Database

Endee stores embeddings

Performs cosine similarity search

RAG Pipeline

User query is converted into an embedding

Top-K similar vectors are retrieved from Endee

Retrieved text is passed as context to a Question-Answering model

Answer is generated strictly from retrieved content

Lightweight Agentic Extension

Similarity scores are evaluated

If confidence is low, retrieval can be repeated with a refined query

This introduces controlled, explainable decision-making without unstable autonomous loops

Explanation of How Endee Is Used

Endee acts as the primary vector database in this project.

Ingestion Flow

Raw documents are added

Documents are split into smaller chunks

Each chunk is converted into a dense embedding

Embeddings are inserted into Endee

Retrieval Flow

User query is embedded

Endee performs semantic similarity search

Most relevant document chunks are retrieved

Retrieved content is used by the RAG pipeline

Note:
At the time of implementation, Endee exposes vector search primarily through its UI.
Retrieval is therefore demonstrated via the Endee interface and consumed by the application layer.
This reflects real-world systems where public APIs may be limited or evolving.

Setup & Execution Instructions
Prerequisites

Ubuntu (WSL supported)

Python 3.10+

Git

Endee running locally

Step 1: Start Endee

Ensure the required data directory exists (important for WSL):

sudo mkdir -p /mnt/data
sudo chown -R $USER:$USER /mnt/data


Start Endee:

cd ~/endee
./build/ndd-avx2


Verify Endee UI:

http://localhost:8080

Step 2: Create Index in Endee

Using the Endee UI:

Index name: documents

Dimension: 384

Distance metric: cosine

Step 3: Set Up Python Environment
cd ~/endee-rag-project
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Step 4: Add Documents

Edit the document file:

nano data/docs.txt


Add sample text for ingestion.

Step 5: Run Ingestion Pipeline
python app/ingest_pipeline.py


This step:

Chunks documents

Generates embeddings

Prepares vectors for insertion into Endee

Vectors are inserted using a clipboard-assisted helper:

python app/clipboard_ingest.py

Step 6: Run the RAG Pipeline
python app/rag.py

Sample Output
Query: What is Endee used for?

Answer:
fast semantic similarity search


This confirms correct semantic retrieval and grounded answer generation.

AI Assistance Disclosure

This project was developed with the assistance of ChatGPT as a learning and productivity tool.
ChatGPT was used for:

Understanding RAG architecture concepts

Debugging environment and integration issues

Improving code structure and documentation clarity

All implementation decisions, testing, debugging, and final integration were performed and validated by the author.
