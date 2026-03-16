import json
import argparse
import sys

def create_batch(input_file):
    try:
        with open(input_file, 'r') as f:
            events = json.load(f)
    except Exception as e:
        print(f"Error reading input file: {e}")
        sys.exit(1)

    if not isinstance(events, list):
        print("Input file must contain a JSON array of events.")
        sys.exit(1)

    batch = []
    for event in events:
        # Basic validation and transformation if needed
        batch.append(event)

    output = {"batch": batch}
    print(json.dumps(output, indent=2))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a Segment batch request from a JSON file.")
    parser.add_argument("input", help="Path to input JSON file containing array of events")
    args = parser.parse_args()
    
    create_batch(args.input)
