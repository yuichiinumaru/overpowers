from matchms import calculate_scores
from matchms.similarity import CosineGreedy, ModifiedCosine
import numpy as np

def find_best_matches(query_spectra, reference_spectra, top_n=5, modified=False):
    """Find best matches using Cosine similarity"""
    sim_func = ModifiedCosine(tolerance=0.1) if modified else CosineGreedy()
    
    print(f"Calculating similarity for {len(query_spectra)} queries against {len(reference_spectra)} references...")
    scores = calculate_scores(references=reference_spectra,
                             queries=query_spectra,
                             similarity_function=sim_func)
    
    results = []
    for query in query_spectra:
        query_matches = scores.scores_by_query(query, sort=True)[:top_n]
        results.append({
            "query": query.get("compound_name") or query.get("title"),
            "matches": [(m[0].get("compound_name"), m[1]) for m in query_matches]
        })
        
    return results

if __name__ == "__main__":
    # This script requires processed spectra objects
    print("This module provides similarity calculation functions for matchms.")
