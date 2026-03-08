import os
import json
import re

def main():
    skills_dir = 'skills'
    output_mapping = '.agents/thoughts/skill_mapping.json'
    os.makedirs(os.path.dirname(output_mapping), exist_ok=True)
    
    mapping = {}
    
    skills = []
    for d in os.listdir(skills_dir):
        if os.path.isdir(os.path.join(skills_dir, d)):
            skills.append(d)
    
    # Sort them to keep things deterministic
    skills.sort()
    
    # We want a 4-digit ID
    # Try to reuse existing IDs where possible if they match the pattern perfectly, 
    # but the task implies creating a new mapping using heuristics
    # Let's extract heuristics from SKILL.md.
    
    current_id = 1
    used_ids = set()
    
    for original_name in skills:
        skill_path = os.path.join(skills_dir, original_name)
        skill_md_path = os.path.join(skill_path, 'SKILL.md')
        
        type_val = 'misc'
        subtype_val = 'general'
        clean_name = original_name
        
        if os.path.exists(skill_md_path):
            with open(skill_md_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            name_match = re.search(r'^name:\s*(.+)$', content, re.MULTILINE)
            if name_match:
                clean_name = name_match.group(1).strip().strip("'\"")
                
            tags_match = re.search(r'^tags:\s*\n((?:-\s*.*\n?)*)', content, re.MULTILINE)
            if tags_match:
                tags_block = tags_match.group(1)
                tags = [t.strip().lstrip('-').strip() for t in tags_block.split('\n') if t.strip().startswith('-')]
                if len(tags) >= 1:
                    type_val = tags[0].lower().replace(' ', '-')
                if len(tags) >= 2:
                    subtype_val = tags[1].lower().replace(' ', '-')
            else:
                lower_content = content.lower()
                if 'ai' in lower_content or 'llm' in lower_content:
                    type_val = 'ai'
                    subtype_val = 'llm'
                elif 'security' in lower_content:
                    type_val = 'sec'
                    subtype_val = 'safety'
                elif 'frontend' in lower_content or 'react' in lower_content:
                    type_val = 'web'
                    subtype_val = 'frontend'
                elif 'backend' in lower_content or 'api' in lower_content:
                    type_val = 'dev'
                    subtype_val = 'code-backend'
                    
        clean_name = re.sub(r'[^a-z0-9]+', '-', clean_name.lower()).strip('-')
        
        # If the original folder already has a 4 digit ID in it, we preserve it to avoid massive unneeded renames
        existing_id_match = re.search(r'-(\d{4})-', original_name)
        if existing_id_match:
            nnnn = existing_id_match.group(1)
            used_ids.add(nnnn)
        else:
            # Generate a new unique ID
            while f"{current_id:04d}" in used_ids:
                current_id += 1
            nnnn = f"{current_id:04d}"
            used_ids.add(nnnn)
            current_id += 1
            
        new_name = f"{type_val}-{subtype_val}-{nnnn}-{clean_name}"
        
        mapping[original_name] = {
            'id': nnnn,
            'type': type_val,
            'subtype': subtype_val,
            'name': clean_name,
            'original': original_name,
            'new': new_name
        }
        
    with open(output_mapping, 'w') as f:
        json.dump(mapping, f, indent=2)
        
    print(f"Mapping generated at {output_mapping}")
    
    # Perform renames safely
    for orig, data in mapping.items():
        if orig != data['new']:
            orig_path = os.path.join(skills_dir, orig)
            new_path = os.path.join(skills_dir, data['new'])
            
            if os.path.exists(new_path) and orig_path != new_path:
                print(f"Warning: {new_path} already exists. Skipping rename for {orig}.")
                continue
                
            os.rename(orig_path, new_path)
            print(f"Renamed: {orig} -> {data['new']}")

if __name__ == "__main__":
    main()
