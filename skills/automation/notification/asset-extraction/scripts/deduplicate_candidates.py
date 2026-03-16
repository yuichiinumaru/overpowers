import os
import json
import shutil
import difflib
from pathlib import Path

TEMP_DIR = "/home/sephiroth/Work/overpowers/.archive/temp"
STAGING_DIR = "/home/sephiroth/Work/overpowers/.archive/staging"
CATEGORIES = ["skills", "agents", "workflows", "hooks"]

def get_content(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return ""

def similar(a, b):
    return difflib.SequenceMatcher(None, a, b).quick_ratio()

def deduplicate():
    manifest = {cat: [] for cat in CATEGORIES}
    total_deduped = 0

    for cat in CATEGORIES:
        json_path = os.path.join(TEMP_DIR, f"candidates_{cat}.json")
        if not os.path.exists(json_path):
            continue
            
        with open(json_path, 'r') as f:
            candidates = json.load(f)
            
        print(f"\nProcessing {len(candidates)} {cat} candidates...")
        
        unique_items = []
        
        for i, cand in enumerate(candidates):
            content = get_content(cand["path"])
            if not content:
                continue
                
            sample = content[:500].lower()
            cand["content_sample"] = sample
            cand["full_content"] = content
            
            is_duplicate = False
            for u_item in unique_items:
                # 1. Exact name match + size similarity check
                if cand["name"] == u_item["name"]:
                    is_duplicate = True
                    # Keep the larger/richer file
                    if cand["size"] > u_item["size"]:
                        u_item["path"] = cand["path"]
                        u_item["size"] = cand["size"]
                        u_item["full_content"] = cand["full_content"]
                    break
                
                # 2. Semantic match
                if similar(sample, u_item["content_sample"]) > 0.85:
                    is_duplicate = True
                    # Keep the larger/richer file
                    if cand["size"] > u_item["size"]:
                        u_item["path"] = cand["path"]
                        u_item["size"] = cand["size"]
                        u_item["full_content"] = cand["full_content"]
                    break
                    
            if not is_duplicate:
                unique_items.append(cand)
                
            if (i+1) % 100 == 0:
                print(f"  Deduped {i+1}/{len(candidates)} -> Found {len(unique_items)} unique so far")
                
        print(f"Final unique {cat}: {len(unique_items)}")
        total_deduped += len(unique_items)
        
        # Stage the unique items
        cat_staging_dir = os.path.join(STAGING_DIR, cat)
        os.makedirs(cat_staging_dir, exist_ok=True)
        
        for idx, item in enumerate(unique_items):
            # Create a safe, unique filename
            # Some paths might have the same file name (like SKILL.md)
            # So we use the parent dir name + file name or a hash if needed
            parent_dir = os.path.basename(os.path.dirname(item["path"]))
            base_name = os.path.basename(item["path"])
            
            if base_name.lower() == "skill.md" or base_name.lower() == "readme.md":
                safe_name = f"{parent_dir}_{base_name}"
            else:
                safe_name = f"{parent_dir}_{base_name}" if parent_dir not in base_name else base_name
                
            safe_name = safe_name.replace(" ", "_").replace("/", "_")
            dest_path = os.path.join(cat_staging_dir, safe_name)
            
            # Write the content to staging
            with open(dest_path, "w", encoding="utf-8") as f:
                f.write(item["full_content"])
                
            manifest[cat].append({
                "original_path": item["path"],
                "staged_path": dest_path,
                "name": item["name"],
                "size": item["size"]
            })

    # Save manifest
    manifest_path = os.path.join(STAGING_DIR, "manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)
        
    print(f"\nStaging complete! {total_deduped} unique items staged.")
    print(f"Manifest saved to {manifest_path}")

if __name__ == "__main__":
    deduplicate()
