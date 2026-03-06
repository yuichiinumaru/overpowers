#!/usr/bin/env python3
"""
Validate PyTorch docstring conventions.
"""
import sys
import re
import argparse

def validate_docstring(content):
    issues = []
    
    # Check if it's a raw string
    # (This is hard to check from just the content, but we can look for r""")
    
    lines = content.strip().split('\n')
    if not lines:
        return ["Docstring is empty"]

    # Check first line signature
    # Pattern: func_name(params) -> ReturnType
    first_line = lines[0].strip()
    if not re.search(r'^\w+\(.*\)\s*->\s*\w+', first_line):
        issues.append("First line should be the function signature: func_name(params) -> ReturnType")
    if first_line.endswith('.'):
        issues.append("Signature line should not end with a period.")

    # Check for Args section
    has_args = any("Args:" in line for line in lines)
    if not has_args:
        issues.append("Missing 'Args:' section.")

    # Check for Examples section
    has_examples = any("Examples::" in line for line in lines)
    if not has_examples:
        issues.append("Missing 'Examples::' section.")

    # Check for Sphinx cross-references
    has_refs = any(re.search(r':(func|class|meth|attr):', line) for line in lines)
    if not has_refs:
        issues.append("No Sphinx cross-references (:func:, :class:, etc.) found.")

    return issues

def main():
    parser = argparse.ArgumentParser(description="Validate PyTorch docstring.")
    parser.add_argument("file", help="Python file containing docstring(s)")
    
    args = parser.parse_args()
    
    try:
        with open(args.file, 'r') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    # Simple regex to find docstrings (r\"\"\" ... \"\"\")
    docstrings = re.findall(r'r"""(.*?)"""', content, re.DOTALL)
    
    if not docstrings:
        print("No raw-string docstrings found (r\"\"\"...\"\"\").")
        sys.exit(0)

    total_issues = 0
    for i, ds in enumerate(docstrings):
        print(f"Checking docstring {i+1}...")
        issues = validate_docstring(ds)
        for issue in issues:
            print(f"  [!] {issue}")
        total_issues += len(issues)

    if total_issues > 0:
        print(f"\nTotal issues found: {total_issues}")
        sys.exit(1)
    else:
        print("\nAll docstrings follow basic PyTorch conventions.")

if __name__ == "__main__":
    main()
