#!/usr/bin/env python3

import json
import argparse
import sys

def validate_resume(json_file):
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)

        required_keys = ["basics", "sections", "metadata"]
        missing = [k for k in required_keys if k not in data]

        if missing:
            print(f"Validation failed: Missing required root keys: {', '.join(missing)}")
            return False

        basics = data.get("basics", {})
        if "name" not in basics or not basics["name"]:
            print("Validation failed: 'name' is required in 'basics'")
            return False

        if "email" not in basics or not basics["email"]:
            print("Validation failed: 'email' is required in 'basics'")
            return False

        print("Resume JSON structure appears valid for Reactive Resume schema.")
        return True

    except json.JSONDecodeError:
        print(f"Error: {json_file} is not a valid JSON file.")
        return False
    except Exception as e:
        print(f"Error validating {json_file}: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Validate a resume JSON file against Reactive Resume schema")
    parser.add_argument("file", help="Path to resume JSON file")

    args = parser.parse_args()

    if validate_resume(args.file):
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
