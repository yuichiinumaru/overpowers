import os
import re

agents_dir = "agents"

for filename in os.listdir(agents_dir):
    if not filename.endswith(".md"):
        continue

    filepath = os.path.join(agents_dir, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Find frontmatter
    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        continue

    frontmatter = match.group(1)
    new_lines = []
    
    for line in frontmatter.split("\n"):
        if line.startswith("model:") or line.startswith("model_fallback:") or line.startswith("fallback_model:"):
            continue
        
        if line.startswith("name:"):
            name_val = line.split(":", 1)[1].strip().strip('"').strip("'")
            if not name_val.startswith("ovp-"):
                name_val = f"ovp-{name_val}"
            line = f'name: "{name_val}"'
            
        new_lines.append(line)

    new_frontmatter = "\n".join(new_lines)
    new_content = content[:match.start(1)] + new_frontmatter + content[match.end(1):]
    
    # Check if file needs renaming
    new_filename = filename
    if not filename.startswith("ovp-"):
        new_filename = f"ovp-{filename}"

    new_filepath = os.path.join(agents_dir, new_filename)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
        
    if new_filename != filename:
        os.rename(filepath, new_filepath)

print("Agents cleanup and renaming complete.")
