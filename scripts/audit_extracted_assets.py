import os
import yaml
from pathlib import Path

def get_frontmatter_name(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            if content.startswith('---'):
                parts = content.split('---')
                if len(parts) >= 3:
                    data = yaml.safe_load(parts[1])
                    return data.get('name') or data.get('id')
    except Exception:
        pass
    return None

def audit():
    base_dirs = {
        'agents': 'agents',
        'skills': 'skills',
        'workflows': 'workflows'
    }
    
    temp_base = Path('temp/extracted')
    overpowers_base = Path('.')
    
    report = []
    report.append("# Asset Audit Report: Extracted vs Existing\n")
    
    for category, folder in base_dirs.items():
        report.append(f"## Category: {category.upper()}")
        
        temp_dir = temp_base / folder
        existing_dir = overpowers_base / folder
        
        if not temp_dir.exists():
            continue
            
        temp_files = {f.name: f for f in temp_dir.glob('**/*') if f.is_file()}
        existing_files = {f.name: f for f in existing_dir.glob('**/*') if f.is_file()}
        
        collisions = set(temp_files.keys()) & set(existing_files.keys())
        
        if collisions:
            report.append("### ⚠️ Filename Collisions Found:")
            for c in collisions:
                report.append(f"- `{c}` (Already exists in `{folder}/`)")
        else:
            report.append("✅ No filename collisions.")
            
        # Check internal names for Markdown files
        temp_names = {}
        for fname, path in temp_files.items():
            if path.suffix == '.md':
                internal_name = get_frontmatter_name(path)
                if internal_name:
                    temp_names[internal_name] = fname
                    
        existing_names = {}
        for fname, path in existing_files.items():
            if path.suffix == '.md':
                internal_name = get_frontmatter_name(path)
                if internal_name:
                    existing_names[internal_name] = fname
                    
        name_collisions = set(temp_names.keys()) & set(existing_names.keys())
        if name_collisions:
            report.append("### ⚠️ Identity Name Collisions (Frontmatter):")
            for nc in name_collisions:
                report.append(f"- `{nc}` (Extracted as `{temp_names[nc]}`, already exists as `{existing_names[nc]}`)")
        
        new_assets = set(temp_files.keys()) - set(existing_files.keys())
        if new_assets:
            report.append(f"### ✨ Unique Assets to Port ({len(new_assets)}):")
            # Limit display to first 10
            for na in sorted(list(new_assets))[:15]:
                report.append(f"- `{na}`")
            if len(new_assets) > 15:
                report.append(f"- ... and {len(new_assets)-15} more.")
        
        report.append("\n" + "-"*40 + "\n")

    with open('temp/audit_report.md', 'w', encoding='utf-8') as f:
        f.write("\n".join(report))
    print("Audit report generated at temp/audit_report.md")

if __name__ == "__main__":
    audit()
