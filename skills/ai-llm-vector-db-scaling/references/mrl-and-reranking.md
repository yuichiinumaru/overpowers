# Matryoshka Embeddings & Reranking Pipeline

For production systems, relying solely on a single large embedding (e.g., 1536+ dimensions) for exact search is an anti-pattern (high RAM cost, slow retrieval). The modern production pattern is a **Two-Stage Pipeline** using Matryoshka Representation Learning (MRL).

## The Two-Stage Architecture

1. **First-Pass Retrieval (Fast & Cheap)**
   - Use an MRL-capable embedding model (e.g., Qwen3-Embedding, Voyage, OpenAI).
   - Truncate the vector to a lower dimension (e.g., 256 or 512 dimensions) before storing in the Vector DB.
   - Retrieve a larger candidate pool ($Top-K \approx 50$ to $100$).
   - *Result*: Massively reduced RAM footprint, faster ANN search.

2. **Second-Pass Reranking (Slow & Precise)**
   - Use a Cross-Encoder Reranker (e.g., Qwen3-Reranker, Cohere Rerank) on the retrieved candidates.
   - The Reranker evaluates the `(query, document)` pair and outputs a final relevance score.
   - Filter down to the final set ($Top-N \approx 5$).
   - *Result*: High precision retrieval without the cost of high-dimensional indexing for the whole corpus.

## Model Scale Heuristics (Qwen3 Example)

Do not automatically default to massive models. Use scale and semantic difficulty as your guide:

| Scale (Chunks) | Scenario Characteristics | Recommended Model Size |
| :--- | :--- | :--- |
| **< 500k** | Fits in memory easily, latency is manageable. | **~0.6B params** (Default choice, highly efficient) |
| **500k - 5M** | RAM costs rise, compression matters. | **~0.6B params**. Upgrade to ~4B *only* if recall suffers after tuning. |
| **5M - 50M** | Sharding required. False negatives multiply. | **~4B params**. Needed for multi-lingual or highly technical corpus. |
| **50M+** | Mission critical, complex queries, heavy compression. | **~8B params**. Only when ROI on recall is proven positive. |

*Rule of Thumb*: If your target documents are completely missing from the first-pass $Top-100$ candidate pool, the bottleneck is the Embedding model. If they are in the pool but not reaching the final $Top-5$, the bottleneck is the Reranker.
