import json
import os
import argparse
import uuid

def validate_reactive_resume(data):
    errors = []
    
    # Basic check for root fields
    required_roots = ["basics", "sections", "metadata"]
    for field in required_roots:
        if field not in data:
            errors.append(f"Missing root field: {field}")
            
    if "basics" in data:
        if not data["basics"].get("name"):
            errors.append("basics.name is required")
        if not data["basics"].get("email"):
            errors.append("basics.email is required")
            
    if "sections" in data:
        # Check if all items in sections have valid IDs
        for section_name, section in data["sections"].items():
            items = section.get("items", [])
            for i, item in enumerate(items):
                if not item.get("id"):
                    errors.append(f"Item {i} in section '{section_name}' is missing an 'id'")
                else:
                    try:
                        uuid.UUID(item["id"])
                    except ValueError:
                        errors.append(f"Item {i} in section '{section_name}' has an invalid UUID: {item['id']}")
                        
    return errors

def main():
    parser = argparse.ArgumentParser(description="Reactive Resume JSON Validator")
    parser.add_argument("file", help="Path to resume JSON file")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.file):
        print(f"Error: {args.file} not found.")
        return

    try:
        with open(args.file, 'r') as f:
            data = json.load(f)
            
        errors = validate_reactive_resume(data)
        
        if errors:
            print("Validation FAILED:")
            for e in errors:
                print(f"- {e}")
        else:
            print("Validation PASSED. JSON appears to conform to Reactive Resume schema.")
            
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format - {e}")

if __name__ == "__main__":
    main()
