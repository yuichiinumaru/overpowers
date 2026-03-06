import json
import sys
import argparse

def validate_json(content):
    try:
        parsed = json.loads(content)
        return True, parsed
    except json.JSONDecodeError as e:
        # Try to extract JSON if it's wrapped in other text
        import re
        match = re.search(r'\{[\s\S]*\}|\[[\s\S]*\]', content)
        if match:
            try:
                parsed = json.loads(match.group(0))
                return True, parsed
            except:
                pass
        return False, str(e)

def main():
    parser = argparse.ArgumentParser(description='Validate JSON output from AI')
    parser.add_argument('file', nargs='?', type=argparse.FileType('r'), default=sys.stdin, help='File to validate (defaults to stdin)')
    
    args = parser.parse_args()
    
    content = args.file.read()
    is_valid, result = validate_json(content)
    
    if is_valid:
        print("JSON is valid.")
        print(json.dumps(result, indent=2))
        sys.exit(0)
    else:
        print(f"Invalid JSON: {result}")
        sys.exit(1)

if __name__ == "__main__":
    main()
