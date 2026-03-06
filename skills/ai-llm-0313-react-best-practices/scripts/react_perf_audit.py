import os
import re
import argparse

# Common anti-patterns to check
PATTERNS = [
    {
        "id": "async-parallel",
        "name": "Potential Waterfall (await in sequence)",
        "regex": r"await\s+.*\n\s*await",
        "description": "Sequential awaits found. Consider using Promise.all() if they are independent."
    },
    {
        "id": "rerender-derived-state",
        "name": "useEffect for Derived State",
        "regex": r"useEffect\(\(\s*\)\s*=>\s*\{[\s\S]*?set[A-Z][a-zA-Z]*\(.*\)",
        "description": "useEffect found updating state. Consider deriving state during render instead."
    },
    {
        "id": "bundle-barrel-imports",
        "name": "Barrel Import potential",
        "regex": r"import\s+\{.*\}\s+from\s+['\"](\.\.?\/)+['\"]",
        "description": "Importing multiple items from a local directory. Ensure it's not a heavy barrel file."
    },
    {
        "id": "rendering-conditional-render",
        "name": "Usage of && for conditionals",
        "regex": r"\{.*?\s+&&\s+<",
        "description": "Found && for conditional rendering. Prefer ternary to avoid rendering '0' or other falsy values."
    }
]

def audit_file(file_path):
    issues = []
    with open(file_path, 'r', errors='ignore') as f:
        content = f.read()
        
    for p in PATTERNS:
        matches = re.finditer(p["regex"], content)
        for match in matches:
            line_no = content.count('\n', 0, match.start()) + 1
            issues.append({
                "line": line_no,
                "pattern_id": p["id"],
                "name": p["name"],
                "description": p["description"]
            })
    return issues

def main():
    parser = argparse.ArgumentParser(description="React Performance Auditor")
    parser.add_argument("path", help="Directory or file to audit")
    args = parser.parse_args()
    
    if os.path.isfile(args.path):
        files = [args.path]
    else:
        files = []
        for root, _, filenames in os.walk(args.path):
            for f in filenames:
                if f.endswith(('.tsx', '.jsx', '.js', '.ts')):
                    files.append(os.path.join(root, f))
                    
    total_issues = 0
    for f in files:
        issues = audit_file(f)
        if issues:
            print(f"\n--- Issues in {f} ---")
            for issue in issues:
                print(f"Line {issue['line']}: [{issue['pattern_id']}] {issue['name']}")
                print(f"  {issue['description']}")
                total_issues += 1
                
    print(f"\nAudit complete. Found {total_issues} potential performance issues.")

if __name__ == "__main__":
    main()
