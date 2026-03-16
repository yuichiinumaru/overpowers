import numpy as np
import json
import argparse
from datetime import datetime

def cosine_similarity(v1, v2):
    """Calculate cosine similarity between two vectors."""
    dot_product = np.dot(v1, v2)
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)
    return dot_product / (norm_v1 * norm_v2)

def calculate_set_similarity(baseline_vectors, current_vectors):
    """
    Calculate the average similarity of the current set compared to the baseline.
    This is a simplified drift detection metric.
    """
    baseline_centroid = np.mean(baseline_vectors, axis=0)
    current_centroid = np.mean(current_vectors, axis=0)
    
    similarity = cosine_similarity(baseline_centroid, current_centroid)
    return similarity

def main():
    parser = argparse.ArgumentParser(description="AI Semantic Drift Monitor")
    parser.add_argument("--baseline", type=str, required=True, help="Path to baseline vectors JSON file")
    parser.add_argument("--current", type=str, required=True, help="Path to current vectors JSON file")
    parser.add_argument("--threshold", type=float, default=0.90, help="Similarity threshold for alert (default: 0.90)")
    
    args = parser.parse_args()
    
    try:
        with open(args.baseline, 'r') as f:
            baseline_data = json.load(f)
            # Assume data is a list of lists (vectors)
            baseline_vectors = np.array(baseline_data)
            
        with open(args.current, 'r') as f:
            current_data = json.load(f)
            current_vectors = np.array(current_data)
            
        similarity = calculate_set_similarity(baseline_vectors, current_vectors)
        
        status = "HEALTHY" if similarity >= args.threshold else "DRIFT DETECTED"
        
        result = {
            "timestamp": datetime.now().isoformat(),
            "similarity_score": round(float(similarity), 4),
            "threshold": args.threshold,
            "status": status
        }
        
        print(json.dumps(result, indent=2))
        
        if status == "DRIFT DETECTED":
            print(f"\n[ALERT] Semantic drift detected! Similarity ({result['similarity_score']}) is below threshold ({args.threshold}).")
            
    except Exception as e:
        print(f"Error processing vectors: {e}")

if __name__ == "__main__":
    # Example format for JSON files:
    # [ [0.1, 0.2, ...], [0.3, 0.4, ...], ... ]
    main()
