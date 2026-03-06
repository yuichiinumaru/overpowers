import os
import argparse
import glob

def check_geo_elements(file_content):
    """
    Checks content for common GEO elements based on the checklist.
    Returns a score and a list of missing elements.
    """
    elements = {
        "Summary/TL;DR": ["summary", "tl;dr", "tldr"],
        "FAQ section": ["faq", "frequently asked questions"],
        "Last updated timestamp": ["last updated", "updated on", "updated:"],
        "Expert quotes/Sources": ["according to", "quoted", "source:", "reference:"],
        "Original data/stats": ["%", "percent", "statistics", "data shows"]
    }

    score = 0
    missing = []

    content_lower = file_content.lower()

    for element, keywords in elements.items():
        found = any(keyword in content_lower for keyword in keywords)
        if found:
            score += 1
        else:
            missing.append(element)

    return score, len(elements), missing

def audit_directory(project_path):
    print(f"Starting GEO audit for project: {project_path}")
    print("-" * 50)

    markdown_files = glob.glob(os.path.join(project_path, "**/*.md"), recursive=True)
    html_files = glob.glob(os.path.join(project_path, "**/*.html"), recursive=True)

    all_files = markdown_files + html_files

    if not all_files:
        print(f"No .md or .html files found in {project_path}")
        return

    for filepath in all_files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            score, total, missing = check_geo_elements(content)

            print(f"File: {os.path.relpath(filepath, project_path)}")
            print(f"GEO Score: {score}/{total}")

            if missing:
                print("Missing Elements:")
                for m in missing:
                    print(f"  - [ ] {m}")
            else:
                print("  ✓ All key GEO elements present!")
            print("-" * 50)

        except Exception as e:
            print(f"Error reading {filepath}: {e}")

def main():
    parser = argparse.ArgumentParser(description="GEO Audit Tool for AI citation readiness.")
    parser.add_argument("project_path", help="Path to the project directory to audit")

    args = parser.parse_args()

    if not os.path.isdir(args.project_path):
        print(f"Error: Directory '{args.project_path}' does not exist.")
        return

    audit_directory(args.project_path)

if __name__ == "__main__":
    main()
