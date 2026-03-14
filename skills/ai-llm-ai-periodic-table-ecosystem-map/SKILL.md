---
name: ai-periodic-table-ecosystem-map
description: The AI Ecosystem Map (Periodic Table)
tags:
- ai
- llm
version: 1.0.0
category: general
---
# The AI Ecosystem Map (Periodic Table)

## Description
This skill provides a structured mental model for navigating the chaotic and rapidly evolving Generative AI ecosystem. It acts as a "Periodic Table," grouping technologies by their fundamental role in building an AI application (like RAG or Autonomous Agents). When designing an AI system, engineers should select the best "element" from each group based on their specific constraints (cost, latency, open-source vs. proprietary).

## Context
Extracted from: [IBM Technology - AI Periodic Table Explained: Mapping LLMs, RAG & AI Agent Frameworks](https://www.youtube.com/watch?v=ESBMgZHzfG0)

## The Core Groups (The AI Stack)

### Group 1: The Brains (Foundation Models & LLMs)
The reasoning engines that process text, code, or images.
-   **Proprietary / Closed:** OpenAI (GPT-4o), Anthropic (Claude 3.5), Google (Gemini 1.5). Best for zero-setup, highest immediate capability, but introduces vendor lock-in and data privacy concerns.
-   **Open Weights / Open Source:** Meta (Llama 3), Mistral, Qwen. Best for deploying locally, fine-tuning on highly sensitive corporate data, and long-term cost control.

### Group 2: The Connectors (Orchestration Frameworks)
The glue that connects the Brain to the outside world, creating RAG pipelines or Agent loops.
-   **LangChain:** The Swiss Army knife. Massive community, integrates with everything, but can become overly complex for simple tasks.
-   **LlamaIndex:** Specifically optimized for data ingestion and advanced RAG strategies (chunking, semantic routing).
-   **Haystack:** Excellent for enterprise search and scalable NLP pipelines.
-   **Agentic Frameworks:** CrewAI, AutoGen, OpenClaw. Specialized for multi-agent collaboration and defining tools/personas.

### Group 3: The Memory (Vector Databases)
Optimized storage for the mathematical representations (embeddings) of your documents, enabling fast similarity search.
-   **Managed/Cloud Native:** Pinecone. Easiest to scale, zero infrastructure to manage.
-   **Open Source / Flexible:** ChromaDB, Weaviate, Milvus. Good for local deployment or specific indexing needs.
-   **Relational Add-ons:** `pgvector` (PostgreSQL extension). Best if your company already uses Postgres and wants to avoid adding a new standalone database to the stack.

### Group 4: The Senses (Embedding Models)
The algorithms that convert raw text into the vectors stored in Group 3.
-   **Proprietary:** OpenAI `text-embedding-3`.
-   **Open Source:** BGE (BAAI General Embedding), Nomic, Hugging Face Sentence Transformers.

### Group 5: The Observers (Evaluations & Observability)
You cannot improve what you cannot measure. These tools monitor the LLM's outputs for hallucinations, toxicity, and drift in production.
-   **Observability (Logging the pipeline):** LangSmith, Phoenix. Crucial for debugging "Why did the agent choose that tool?".
-   **Evaluation (Scoring the output):** Ragas (RAG Assessment), TruLens. Uses "LLM-as-a-judge" to score answers on metrics like Faithfulness and Answer Relevancy.

## Architectural Best Practice: The Mix-and-Match Strategy
Never tightly couple your application logic to a single Group 1 (Model) provider. Use Group 2 (Orchestration) to abstract the model call. If OpenAI goes down, or Anthropic releases a significantly cheaper model, your architecture should allow you to swap the "Brain" by changing a single environment variable, without rewriting the entire pipeline.
