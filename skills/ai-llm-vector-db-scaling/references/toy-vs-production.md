# Toy vs. Production Vector DB Patterns

| Pattern | Toy (What to avoid) | Production (What to do) |
| :--- | :--- | :--- |
| **Embedding** | Embedding entire documents as one vector. | Smart chunking (max 200-500 tokens). |
| **Dimensions** | Using default high dimensions (3072+) everywhere. | Dimensionality reduction (PCA) to 384-768 where possible. |
| **Metadata** | Storing full document text in metadata. | Lean metadata (ID only). Store full docs in sidecar SQL/NoSQL. |
| **Index Type** | Using FLAT index or default HNSW params. | Tuned HNSW or IVF based on specific dataset benchmarks. |
| **Scaling** | Vertical scaling only. | Horizontal sharding and read replicas. |
| **Updates** | Synchronous updates blocking queries. | Asynchronous vector update pipeline via queues. |

## Why it matters
Toy patterns result in linear time complexity $O(n)$ for search, excessive RAM costs, and noisy retrieval results. Production patterns ensure sub-linear search time, optimized RAM density (< 4GB per 1M vectors), and higher precision.
