import os
import re
import difflib
import json
from pathlib import Path
from tqdm import tqdm # Let's hope it's installed, otherwise we'll just print. We'll skip tqdm to be safe.

REFERENCES_FILE = "/home/sephiroth/Work/overpowers/.archive/temp/references_files_filtered.txt"
OVERPOWERS_ROOT = "/home/sephiroth/Work/overpowers"

CATEGORIES = {
    "skills": os.path.join(OVERPOWERS_ROOT, "skills"),
    "agents": os.path.join(OVERPOWERS_ROOT, "agents"),
    "workflows": os.path.join(OVERPOWERS_ROOT, "workflows"),
    "hooks": os.path.join(OVERPOWERS_ROOT, "hooks")
}

def get_content(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Remove frontmatter for pure content comparison
            content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)
            return content.strip()
    except Exception as e:
        return ""

def load_existing():
    existing = {cat: {} for cat in CATEGORIES}
    print("Loading existing Overpowers assets...")
    
    # Skills
    for root, dirs, files in os.walk(CATEGORIES["skills"]):
        if "SKILL.md" in files:
            name = os.path.basename(root)
            content = get_content(os.path.join(root, "SKILL.md"))
            if content:
                existing["skills"][name.lower()] = {
                    "content": content,
                    "sample": content[:500].lower(),
                    "size": len(content)
                }
    
    # Agents
    for root, dirs, files in os.walk(CATEGORIES["agents"]):
        for file in files:
            if file.endswith(".md") and file != "AGENTS.md":
                name = file.replace(".md", "").replace("ovp-", "")
                content = get_content(os.path.join(root, file))
                if content:
                    existing["agents"][name.lower()] = {
                        "content": content,
                        "sample": content[:500].lower(),
                        "size": len(content)
                    }

    # Workflows
    for root, dirs, files in os.walk(CATEGORIES["workflows"]):
        for file in files:
            if file.endswith(".md"):
                name = file.replace(".md", "")
                content = get_content(os.path.join(root, file))
                if content:
                    existing["workflows"][name.lower()] = {
                        "content": content,
                        "sample": content[:500].lower(),
                        "size": len(content)
                    }

    # Hooks
    for root, dirs, files in os.walk(CATEGORIES["hooks"]):
        for file in files:
            if file.endswith(".sh") or file.endswith(".py") or file.endswith(".js"):
                name = file.split(".")[0]
                content = get_content(os.path.join(root, file))
                if content:
                    existing["hooks"][name.lower()] = {
                        "content": content,
                        "sample": content[:500].lower(),
                        "size": len(content)
                    }
                    
    for cat, items in existing.items():
        print(f"Loaded {len(items)} existing {cat}.")
    return existing

def similar(a, b):
    return difflib.SequenceMatcher(None, a, b).quick_ratio()

def determine_category(path):
    path_lower = path.lower()
    if "skill.md" in path_lower or "/skills/" in path_lower:
        return "skills"
    elif "/agents/" in path_lower and path_lower.endswith(".md"):
        return "agents"
    elif "/workflows/" in path_lower and path_lower.endswith(".md"):
        return "workflows"
    elif "/hooks/" in path_lower:
        return "hooks"
    elif "/commands/" in path_lower and path_lower.endswith(".md"):
        return "workflows"  # commands are workflows
    return None

def analyze_candidates():
    existing = load_existing()
    results = {"yes": [], "maybe": [], "no": []}
    
    with open(REFERENCES_FILE, "r") as f:
        candidate_paths = [line.strip() for line in f if line.strip()]
        
    print(f"\nAnalyzing {len(candidate_paths)} candidate files...")
    
    processed = 0
    for path in candidate_paths:
        processed += 1
        if processed % 1000 == 0:
            print(f"Processed {processed}/{len(candidate_paths)}...")
            
        cat = determine_category(path)
        if not cat:
            continue
            
        content = get_content(path)
        if not content or len(content) < 50: # Skip very short/empty files
            continue
            
        # Determine logical name
        if cat == "skills":
            name = os.path.basename(os.path.dirname(path)).lower()
        else:
            name = os.path.basename(path).split(".")[0].lower()
            
        sample = content[:500].lower()
        
        max_ratio = 0.0
        best_match_name = None
        
        # Exact name match check first (often duplicate)
        if name in existing[cat]:
            max_ratio = similar(sample, existing[cat][name]["sample"])
            best_match_name = name
            
        # If not highly similar by name, check semantic across category
        if max_ratio < 0.85:
            for ex_name, ex_data in existing[cat].items():
                if sample == ex_data["sample"]:
                    max_ratio = 1.0
                    best_match_name = ex_name
                    break
                
                # Check ratio if it's potentially similar
                ratio = similar(sample, ex_data["sample"])
                if ratio > max_ratio:
                    max_ratio = ratio
                    best_match_name = ex_name
                    if max_ratio > 0.95:
                        break # Stop early if nearly identical
                        
        candidate_info = {
            "path": path,
            "category": cat,
            "name": name,
            "size": len(content),
            "match_ratio": round(max_ratio, 2),
            "matched_with": best_match_name
        }
        
        if max_ratio > 0.85:
            results["no"].append(candidate_info)
        elif max_ratio > 0.60:
            results["maybe"].append(candidate_info)
        else:
            results["yes"].append(candidate_info)

    print("\nAnalysis Complete!")
    print(f"YES (New): {len(results['yes'])}")
    print(f"MAYBE (Similar): {len(results['maybe'])}")
    print(f"NO (Duplicate): {len(results['no'])}")
    
    # Save reports
    report_path = os.path.join(OVERPOWERS_ROOT, ".agents", "thoughts", "references_analysis_report.md")
    os.makedirs(os.path.dirname(report_path), exist_ok=True)
    
    with open(report_path, "w") as f:
        f.write("# References Analysis Report\n\n")
        f.write(f"Total candidates processed: {processed}\n")
        f.write(f"- YES (New candidates): {len(results['yes'])}\n")
        f.write(f"- MAYBE (Potentially updated/similar): {len(results['maybe'])}\n")
        f.write(f"- NO (Duplicates): {len(results['no'])}\n\n")
        
        f.write("## YES (Top 200 candidates by size)\n")
        yes_sorted = sorted(results["yes"], key=lambda x: x["size"], reverse=True)
        for c in yes_sorted[:200]:
            f.write(f"- **{c['name']}** ({c['category']}, {c['size']} bytes) -> `{c['path']}`\n")
            
        f.write("\n## MAYBE (Top 200 candidates by size)\n")
        maybe_sorted = sorted(results["maybe"], key=lambda x: x["size"], reverse=True)
        for c in maybe_sorted[:200]:
            f.write(f"- **{c['name']}** ({c['category']}, {c['size']} bytes) [Match: {c['match_ratio']} w/ {c['matched_with']}] -> `{c['path']}`\n")
            
    # Also save JSON for scripting later if needed
    json_path = os.path.join(OVERPOWERS_ROOT, ".archive", "temp", "references_analysis.json")
    os.makedirs(os.path.dirname(json_path), exist_ok=True)
    with open(json_path, "w") as f:
        json.dump(results, f, indent=2)
        
    print(f"Report saved to {report_path}")

if __name__ == "__main__":
    analyze_candidates()
