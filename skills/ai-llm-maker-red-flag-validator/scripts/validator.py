import json
import logging
import sys

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def validate_responses(responses, max_length=500):
    """
    Validates a list of LLM string responses.
    Discards any response that is too long (Red Flag 1) or fails JSON parsing if expected (Red Flag 2).
    """
    valid = []
    for idx, resp in enumerate(responses):
        # Red flag: too long
        if len(resp) > max_length:
            logging.warning(f"Response {idx} RED FLAGGED: length {len(resp)} exceeds {max_length}")
            continue
            
        # Red flag: must be parseable JSON
        try:
            parsed = json.loads(resp)
            valid.append(parsed)
        except json.JSONDecodeError:
            logging.warning(f"Response {idx} RED FLAGGED: invalid JSON format")
            continue
            
    return valid

if __name__ == "__main__":
    # Example usage reading from standard input
    try:
        raw_data = sys.stdin.read()
        responses = json.loads(raw_data)
        if not isinstance(responses, list):
            raise ValueError("Input must be a JSON array of response strings.")
            
        validated = validate_responses(responses)
        print(json.dumps({"valid_responses": validated, "count": len(validated)}))
    except Exception as e:
        logging.error(f"Error processing inputs: {str(e)}")
        sys.exit(1)
