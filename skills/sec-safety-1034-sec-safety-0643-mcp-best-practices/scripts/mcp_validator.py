import json
import sys
import re

def validate_mcp_config(config_file):
    try:
        with open(config_file, 'r') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error loading JSON: {e}")
        return

    # Check if it's a list of tools or a full server config
    tools = data.get('tools', []) if isinstance(data, dict) else data
    if not isinstance(tools, list):
        print("Error: Expected a list of tools or an object with a 'tools' list.")
        return

    print(f"Validating {len(tools)} tools...\n")
    errors = 0
    warnings = 0

    for tool in tools:
        name = tool.get('name', 'UNKNOWN')
        description = tool.get('description', '')
        
        # 1. Name validation
        if not re.match(r'^[a-z0-9_]+_[a-z0-9_]+_[a-z0-9_]+$', name):
            if not re.match(r'^[a-z0-9_]+$', name):
                print(f"[ERROR] Tool '{name}': Name should follow snake_case pattern.")
                errors += 1
            else:
                print(f"[WARNING] Tool '{name}': Name should ideally follow {{service}}_{{action}}_{{resource}} pattern.")
                warnings += 1
        
        # 2. Description validation
        if not description:
            print(f"[ERROR] Tool '{name}': Description is missing.")
            errors += 1
        elif len(description) < 10:
            print(f"[WARNING] Tool '{name}': Description is very short.")
            warnings += 1
            
        # 3. Input Schema validation (Pagination check)
        input_schema = tool.get('inputSchema', {}).get('properties', {})
        # Infer if it's a list operation from name or description
        is_list = 'list' in name.lower() or 'list' in description.lower()
        if is_list:
            if 'limit' not in input_schema:
                print(f"[WARNING] Tool '{name}': Pagination 'limit' parameter missing for list action.")
                warnings += 1
            if 'offset' not in input_schema and 'cursor' not in input_schema:
                print(f"[WARNING] Tool '{name}': Pagination 'offset' or 'cursor' parameter missing for list action.")
                warnings += 1

        # 4. Annotations check
        # Note: Some implementations put hints inside properties or as top-level fields
        hints = ['readOnlyHint', 'destructiveHint', 'idempotentHint', 'openWorldHint']
        found_hints = [h for h in hints if h in tool]
        if not found_hints:
            # Check if they are in description as mentions (optional check)
            pass

    print(f"\nValidation complete: {errors} Errors, {warnings} Warnings.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python mcp_validator.py <mcp_tools_json_file>")
    else:
        validate_mcp_config(sys.argv[1])
