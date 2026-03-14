# Feature Plan: Moltbot Memory Hybrid Search

## 1. Overview
The goal is to improve Moltbot's memory retrieval capabilities by implementing a hybrid search mechanism. Hybrid search combines the precision of keyword-based search (Full-Text Search) with the semantic understanding of vector-based search (Embedding search). This ensures that Moltbot can find relevant information even when exact keywords are not present, while still performing well for specific technical terms.

## 2. Goals & Success Criteria
- **Goal:** Implement a hybrid search function in `MemoryIndexManager` that integrates `sqlite-vec` and `FTS5`.
- **Success Criteria:**
  - Hybrid search results should be a combined ranking of keyword and vector search results.
  - Search latency should remain within acceptable limits (< 500ms for typical local databases).
  - Search quality should be demonstrably better than either single method (qualitative assessment).

## 3. Vertical Slices & Milestones

### Slice 1: Implementation of Hybrid Search Logic
- **Objective:** Create the core algorithm to combine results from `searchKeyword` and `searchVector`.
- **Deliverables:** A new `hybridSearch` method in `MemoryIndexManager`.

### Slice 2: Ranking Optimization (RRF)
- **Objective:** Use Reciprocal Rank Fusion (RRF) to unify scores from different search types.
- **Deliverables:** Optimized scoring logic in `hybridSearch`.

### Slice 3: Validation and Testing
- **Objective:** Verify correctness and performance with synthetic data.
- **Deliverables:** Test suite for hybrid search.

## 4. Risks & Mitigations
- **Complexity of combined scoring:** -> **Mitigation:** Start with a well-known algorithm like RRF (Reciprocal Rank Fusion) which is simple and robust.
- **Library stability (sqlite-vec alpha):** -> **Mitigation:** Stick to core vector search functionalities and ensure error handling for loading the extension.

## 5. Exit Conditions
- [ ] Code is fully reviewed and approved.
- [ ] Tests for hybrid search are passing.
- [ ] Hybrid search is the default search method for Moltbot memory.
