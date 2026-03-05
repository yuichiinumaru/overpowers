import argparse
import os
from pathlib import Path

def validate_pattern(file_path):
    issues = []
    with open(file_path, 'r') as f:
        content = f.read()
        
    # Check for mandatory sections
    required_sections = [
        "## Intent",
        "## Problem",
        "## Solution",
        "## Examples"
    ]
    
    for section in required_sections:
        if section not in content:
            issues.append(f"Missing mandatory section: {section}")
            
    # Check for frontmatter
    if not content.startswith("---"):
        issues.append("Missing frontmatter delimiter (---)")
        
    return issues

def main():
    parser = argparse.ArgumentParser(description='Pattern File Validator')
    parser.add_argument('path', help='Path to pattern file or directory')
    parser.add_argument('--all', action='store_true', help='Validate all files in directory')
    
    args = parser.parse_args()
    
    path = Path(args.path)
    files = []
    if args.all and path.is_dir():
        files = list(path.glob('*.md'))
    else:
        files = [path]
        
    for f in files:
        issues = validate_pattern(f)
        if issues:
            print(f"❌ {f.name}: {len(issues)} issues found")
            for issue in issues:
                print(f"  - {issue}")
        else:
            print(f"✅ {f.name}: Valid")

if __name__ == "__main__":
    main()
