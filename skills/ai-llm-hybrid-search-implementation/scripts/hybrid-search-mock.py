import sys

def rrf_fusion(results_list, k=60):
    """
    Reciprocal Rank Fusion (RRF) implementation.
    results_list: list of lists, where each list contains (doc_id, score)
    """
    scores = {}
    for results in results_list:
        for rank, (doc_id, _) in enumerate(results):
            if doc_id not in scores:
                scores[doc_id] = 0
            scores[doc_id] += 1 / (k + rank + 1)
    
    # Sort by fused score
    sorted_docs = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return sorted_docs

def mock_search(query):
    print(f"Hybrid Search for: {query}")
    # Mock vector results (doc_id, similarity)
    vector_results = [("doc1", 0.9), ("doc2", 0.8), ("doc3", 0.7)]
    # Mock keyword results (doc_id, bm25_score)
    keyword_results = [("doc3", 10.0), ("doc1", 8.0), ("doc4", 5.0)]
    
    fused = rrf_fusion([vector_results, keyword_results])
    print("Fused Results (doc_id, rrf_score):")
    for doc_id, score in fused:
        print(f"{doc_id}: {score:.4f}")

if __name__ == "__main__":
    query = sys.argv[1] if len(sys.argv) > 1 else "example query"
    mock_search(query)
