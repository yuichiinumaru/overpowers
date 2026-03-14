import json
import logging
import sys
from collections import Counter

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def first_to_ahead_by_k(responses, k, k_min):
    """
    Implements the first-to-ahead-by-k voting logic from the MAKER paper.
    If the leading vote has a lead of 'k' active votes over the runner up 
    AND at least 'k_min' total votes have been cast, it wins.
    """
    if not responses:
        return {"status": "UNDECIDED", "reason": "No valid responses provided."}
    
    # Hashable forms of JSON 
    # Use string dumps to count identical objects
    str_votes = [json.dumps(r, sort_keys=True) if isinstance(r, dict) else str(r) for r in responses]
    counts = Counter(str_votes)
    
    most_common = counts.most_common(2)
    
    leader_count = most_common[0][1]
    runner_up_count = most_common[1][1] if len(most_common) > 1 else 0
    
    if leader_count >= k_min and (leader_count - runner_up_count) >= k:
        # Re-parse winning string if it looks like a dict representation
        winning_payload = most_common[0][0]
        try:
            winning_parsed = json.loads(winning_payload)
        except Exception:
            winning_parsed = winning_payload
            
        return {
            "status": "DECIDED",
            "winner": winning_parsed,
            "tally": dict(counts)
        }
        
    return {
        "status": "UNDECIDED",
        "leader_lead": leader_count - runner_up_count,
        "k_required": k,
        "tally": dict(counts)
    }

if __name__ == "__main__":
    # Expects JSON string via stdin with {"k": int, "k_min": int, "responses": list}
    try:
        raw_data = sys.stdin.read()
        payload = json.loads(raw_data)
        k = payload.get("k", 3)
        k_min = payload.get("k_min", k)
        responses = payload.get("responses", [])
        
        result = first_to_ahead_by_k(responses, k, k_min)
        print(json.dumps(result, indent=2))
        
    except Exception as e:
        logging.error(f"Error executing voter: {str(e)}")
        sys.exit(1)
