#!/usr/bin/env python3
import json
import sys

def scaffold_measure():
    print("--- Power BI Measure Scaffolder ---")
    name = input("Measure Name: ")
    table = input("Target Table Name: ")
    expression = input("DAX Expression: ")
    format_string = input("Format String (default: #,##0): ") or "#,##0"
    description = input("Description (for documentation): ")
    
    measure_def = {
        "operation": "Create",
        "definitions": [{
            "name": name,
            "tableName": table,
            "expression": expression,
            "formatString": format_string,
            "description": description
        }]
    }
    
    print("\nUse the following JSON with the measure_operations tool:")
    print(json.dumps(measure_def, indent=2))

if __name__ == "__main__":
    try:
        scaffold_measure()
    except KeyboardInterrupt:
        print("\nScaffolding cancelled.")
        sys.exit(0)
