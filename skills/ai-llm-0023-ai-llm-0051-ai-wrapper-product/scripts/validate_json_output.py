#!/usr/bin/env python3
import sys
import json
import re

def parse_ai_output(text):
    """
    Tries to parse JSON from AI output, with fallback to regex extraction.
    """
    text = text.strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        # Fallback: extract JSON from response using regex
        match = re.search(r'(\{[\s\S]*\})', text)
        if match:
            try:
                return json.loads(match.group(1))
            except json.JSONDecodeError:
                pass
        return None

def main():
    if len(sys.argv) < 2:
        print("Usage: validate_json_output.py <file_path_or_string>")
        sys.exit(1)

    input_data = sys.argv[1]
    
    # Check if input is a file
    try:
        with open(input_data, 'r') as f:
            content = f.read()
    except (FileNotFoundError, OSError):
        content = input_data

    result = parse_ai_output(content)
    if result:
        print("Successfully validated JSON output:")
        print(json.dumps(result, indent=2))
    else:
        print("Error: Could not parse valid JSON from output.")
        sys.exit(1)

if __name__ == "__main__":
    main()
