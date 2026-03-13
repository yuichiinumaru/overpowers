---
name: ai-llm-vector-db-scaling
description: Scaling strategies for vector databases in production environments based on Grey Haven guidelines. Use when designing RAG systems, choosing vector database parameters, optimizing latency/memory, or auditing existing vector architectures.
---

# Vector DB Production Scaling

This skill provides procedural guidance for scaling vector databases from prototype to production, ensuring sub-linear performance and cost-efficient memory usage.

## Quick Audit

Run the audit script to check your current architecture parameters:
```bash
python3 skills/ai-llm-vector-db-scaling/scripts/audit-vector-db.py --dims <dims> --index <type> --meta-kb <kb> --chunk <tokens>
```

## Core Workflows

### 1. Architecture Audit
Identify "Toy" patterns that will fail at scale.
- **Action**: Compare existing setup against [toy-vs-production.md](references/toy-vs-production.md).
- **Goal**: Eliminate FLAT indices, excessive metadata, and monolithic embedding of large documents.

### 2. Matryoshka & Reranking (Two-Stage Pipeline)
Move from single high-dimensional searches to a fast/precise split.
- **Action**: Implement Matryoshka Representation Learning (MRL) embeddings (e.g., Qwen3-Embedding).
- **Goal**: Truncate vectors (e.g., to 256/512 dims) for a fast first-pass retrieval ($Top-K \approx 100$).
- **Refinement**: Apply a Cross-Encoder Reranker on the candidate pool for final precision ($Top-N \approx 5$).
- **Reference**: Review heuristics in [mrl-and-reranking.md](references/mrl-and-reranking.md).
- **Tool**: Calculate memory savings with `python3 skills/ai-llm-vector-db-scaling/scripts/calculate-mrl-savings.py --vectors <num> --orig-dim <dims> --trunc-dim <dims>`

### 3. Index Tuning
Optimize your index based on specific dataset requirements.
- **IVF (Inverted File)**: Use for massive datasets with memory constraints. 
- **HNSW (Hierarchical Navigable Small World)**: Use for high-speed, low-latency requirements.
- **Reference**: Follow parameters in [index-tuning.md](references/index-tuning.md).

### 4. Cost & RAM Optimization
Ensure financial sustainability of the vector infrastructure.
- **Target**: Target < 4GB RAM per 1M vectors.
- **Technique**: Use Dimensionality Reduction (PCA) to lower vector dimensions before indexing.
- **Scaling**: Implement read replicas and horizontal sharding instead of vertical scaling.

## Integration Principles
- **Smart Chunking**: Always chunk documents (200-500 tokens) with sentence preservation.
- **Sidecar Metadata**: Store full document text in a primary SQL/NoSQL DB; keep only pointers/IDs in the Vector DB.
- **Async Updates**: Decouple query path from ingestion path using message queues.
