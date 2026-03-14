import os
import json
import re

ANALYSIS_FILE = "/home/sephiroth/Work/overpowers/.archive/temp/references_analysis.json"
OUT_DIR = "/home/sephiroth/Work/overpowers/.archive/temp/"

def get_content(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except:
        return ""

def classify_candidate(path, content, name):
    content_lower = content.lower()
    path_lower = path.lower()
    
    # Heuristics for Agents
    if (
        re.search(r'^role:\s*', content, re.IGNORECASE | re.MULTILINE) or
        re.search(r'^backstory:\s*', content, re.IGNORECASE | re.MULTILINE) or
        re.search(r'^system_prompt:\s*', content, re.IGNORECASE | re.MULTILINE) or
        "you are a " in content_lower[:500] or
        "you are an expert" in content_lower[:500] or
        "you are an ai" in content_lower[:500] or
        "/agents/" in path_lower or
        name.endswith("_expert") or
        name.endswith("_developer") or
        name.endswith("_architect")
    ):
        # Additional check to ensure it's not actually a skill that just says "You are..."
        if "skill.md" not in path_lower:
            return "agents"

    # Heuristics for Skills
    if (
        "skill.md" in path_lower or
        "/skills/" in path_lower or
        "<skill>" in content_lower or
        "# skill" in content_lower[:200]
    ):
        return "skills"

    # Heuristics for Workflows/Commands
    if (
        re.search(r'^command:\s*', content, re.IGNORECASE | re.MULTILINE) or
        "<workflow>" in content_lower or
        re.search(r'#\s*/[\w-]+', content) or  # matches "# /command-name"
        "/workflows/" in path_lower or
        "/commands/" in path_lower
    ):
        return "workflows"
        
    # Heuristics for Hooks
    if (
        "/hooks/" in path_lower or
        path_lower.endswith(".sh") or
        path_lower.endswith(".py")
    ):
        return "hooks"

    # Fallback to Frontmatter analysis
    if content.startswith("---"):
        frontmatter = content.split("---")[1]
        if "name:" in frontmatter and "description:" in frontmatter:
            return "skills" # default guess for generic frontmatter without agent fields

    return "unknown"

def main():
    if not os.path.exists(ANALYSIS_FILE):
        print("Analysis file not found. Run analyze_references.py first.")
        return
        
    with open(ANALYSIS_FILE, 'r') as f:
        data = json.load(f)
        
    yes_candidates = data.get("yes", [])
    print(f"Categorizing {len(yes_candidates)} 'YES' candidates...")
    
    categories = {
        "skills": [],
        "agents": [],
        "workflows": [],
        "hooks": [],
        "unknown": []
    }
    
    for candidate in yes_candidates:
        path = candidate["path"]
        name = candidate["name"]
        content = get_content(path)
        
        cat = classify_candidate(path, content, name)
        candidate["inferred_category"] = cat
        categories[cat].append(candidate)
        
    print("\nCategorization Results:")
    for cat, items in categories.items():
        print(f"- {cat.capitalize()}: {len(items)}")
        
        # Save each category list
        out_path = os.path.join(OUT_DIR, f"candidates_{cat}.json")
        with open(out_path, "w") as f:
            json.dump(items, f, indent=2)
            
    # Quick sanity check on Unknowns
    if categories["unknown"]:
        print("\nSample of Unknown candidates:")
        for u in categories["unknown"][:5]:
            print(f"  - {u['path']}")

if __name__ == "__main__":
    main()
