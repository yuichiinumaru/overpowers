# Vector Index Tuning Guide

## IVF (Inverted File) Tuning
Best for large datasets where memory efficiency is prioritized over absolute speed.

- **nlist**: Number of clusters. Recommendation: `int(sqrt(number_of_vectors))`.
- **nprobe**: Number of clusters to search. Recommendation: Start with `min(nlist/50, 50)`. 
  - *Increase* for higher recall.
  - *Decrease* for lower latency.

## HNSW (Hierarchical Navigable Small World) Tuning
Best for high-speed retrieval where RAM cost is secondary.

- **M**: Number of neighbors per node. Recommendation: `16` to `32`.
- **ef_construction**: Accuracy during index build. Recommendation: `128` to `512`.
- **ef_search**: Accuracy during search. Recommendation: `64` to `256`.
  - *Note*: Doubling dimensions doubles RAM usage for HNSW.

## Dimensionality Reduction (PCA)
Before indexing, consider if your semantic space can be compressed.
- Use **PCA** to reduce from high dimensions (e.g., 3072) to lower (e.g., 768).
- This significantly reduces HNSW memory footprint and improves IVF cluster quality.

## Benchmark Metrics
Always monitor:
1. **p99 Latency**: The ceiling of your user experience.
2. **Recall@10**: Percentage of ground-truth matches found in top 10 results.
3. **Memory Density**: Aim for < 4GB RAM per 1M vectors.
