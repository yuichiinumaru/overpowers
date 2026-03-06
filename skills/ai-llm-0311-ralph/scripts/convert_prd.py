import os
import json
import argparse
import datetime

def convert_prd_to_json(prd_text, project_name="Unknown Project"):
    # This is a template generator. Actual logic might need more sophisticated parsing.
    # But we can provide a basic structure based on common PRD formats.
    
    lines = prd_text.split('\n')
    feature_name = "new-feature"
    description = ""
    user_stories = []
    
    current_section = ""
    us_count = 1
    
    for line in lines:
        line = line.strip()
        if line.startswith('# '):
            feature_name = line[2:].strip().lower().replace(' ', '-')
            description = line[2:].strip()
        elif line.startswith('## '):
            current_section = line[3:].strip().lower()
        elif line.startswith('- ') and 'stories' in current_section:
            us_id = f"US-{us_count:03d}"
            user_stories.append({
                "id": us_id,
                "title": line[2:].strip(),
                "description": f"As a user, I want {line[2:].strip()} so that I can benefit from it.",
                "acceptanceCriteria": [
                    "Feature implementation matches requirements",
                    "Typecheck passes"
                ],
                "priority": us_count,
                "passes": False,
                "notes": ""
            })
            us_count += 1
            
    if not user_stories:
        # Generic fallback if no stories found
        user_stories.append({
            "id": "US-001",
            "title": "Initial implementation",
            "description": "Implement the core functionality described in the PRD",
            "acceptanceCriteria": [
                "Core features implemented",
                "Typecheck passes"
            ],
            "priority": 1,
            "passes": False,
            "notes": ""
        })

    return {
        "project": project_name,
        "branchName": f"ralph/{feature_name}",
        "description": description or "Feature described in PRD",
        "userStories": user_stories
    }

def archive_existing(target_dir):
    prd_path = os.path.join(target_dir, "prd.json")
    progress_path = os.path.join(target_dir, "progress.txt")
    
    if os.path.exists(prd_path):
        try:
            with open(prd_path, 'r') as f:
                current_prd = json.load(f)
            
            branch_name = current_prd.get("branchName", "unknown").replace("ralph/", "")
            date_str = datetime.datetime.now().strftime("%Y-%m-%d")
            archive_name = f"{date_str}-{branch_name}"
            archive_dir = os.path.join(target_dir, "archive", archive_name)
            
            os.makedirs(archive_dir, exist_ok=True)
            
            os.rename(prd_path, os.path.join(archive_dir, "prd.json"))
            if os.path.exists(progress_path):
                os.rename(progress_path, os.path.join(archive_dir, "progress.txt"))
            
            print(f"Archived existing run to {archive_dir}")
        except Exception as e:
            print(f"Error archiving: {e}")

def main():
    parser = argparse.ArgumentParser(description="Convert PRD to ralph prd.json")
    parser.add_argument("prd_file", help="Path to the PRD markdown file")
    parser.add_argument("--project", default="Project", help="Project name")
    parser.add_argument("--output-dir", default=".", help="Directory to save prd.json")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.prd_file):
        print(f"Error: PRD file {args.prd_file} not found.")
        return

    with open(args.prd_file, 'r') as f:
        prd_text = f.read()
        
    archive_existing(args.output_dir)
    
    result = convert_prd_to_json(prd_text, args.project)
    
    output_path = os.path.join(args.output_dir, "prd.json")
    with open(output_path, 'w') as f:
        json.dump(result, f, indent=2)
        
    print(f"Generated {output_path}")

if __name__ == "__main__":
    main()
