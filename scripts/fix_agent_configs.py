import os
import re
import yaml

AGENTS_DIR = "agents"

COLOR_MAP = {
    "green": "#008000",
    "teal": "#008080",
    "orange": "#FFA500",
    "purple": "#800080",
    "cyan": "#00FFFF",
    "blue": "#0000FF",
    "red": "#FF0000",
    "yellow": "#FFFF00",
    "white": "#FFFFFF",
    "black": "#000000",
    "pink": "#FFC0CB",
    "gold": "#FFD700",
    "indigo": "#4B0082"
}

def fix_color(value):
    if not value: return None
    # Remove triple quotes and surrounding whitespace
    v = str(value).strip().strip("'").strip('"').strip()
    
    # Check if it's a known named color
    if v.lower() in COLOR_MAP:
        return COLOR_MAP[v.lower()]
    
    # Check if it's a hex code
    hex_match = re.search(r"#[0-9A-Fa-f]{6}", v)
    if hex_match:
        return hex_match.group(0)
    
    if re.match(r"^[0-9A-Fa-f]{6}$", v):
        return "#" + v
        
    return None

def process_file(path):
    with open(path, "r", encoding="utf-8") as f:
        full_content = f.read()

    # Find the frontmatter
    match = re.match(r"^---\s*\n(.*?)\n---", full_content, re.DOTALL)
    if not match:
        return False

    frontmatter_str = match.group(1)
    body = full_content[match.end():]
    
    try:
        # We use a custom parser approach because standard yaml might lose comments or formatting
        # but here we want to be safe and precise.
        data = yaml.safe_load(frontmatter_str)
    except Exception as e:
        print(f"Error parsing YAML in {path}: {e}")
        return False

    changed = False

    # Fix color
    if "color" in data:
        new_color = fix_color(data["color"])
        if new_color and new_color != data["color"]:
            data["color"] = new_color
            changed = True

    # Fix tools
    if "tools" in data and isinstance(data["tools"], list):
        tools_list = data["tools"]
        new_tools = {}
        for t in tools_list:
            if isinstance(t, str):
                new_tools[t.lower()] = True
        data["tools"] = new_tools
        changed = True

    if changed:
        # To preserve as much as possible, we could use a better YAML dumper
        # but for simplicity and correctness in opencode:
        new_frontmatter = yaml.dump(data, allow_unicode=True, default_flow_style=False, sort_keys=False)
        new_content = "---\n" + new_frontmatter + "---" + body
        
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Fixed {path}")
        return True
    
    return False

if __name__ == "__main__":
    count = 0
    for filename in os.listdir(AGENTS_DIR):
        if filename.endswith(".md"):
            if process_file(os.path.join(AGENTS_DIR, filename)):
                count += 1
    print(f"Total files fixed: {count}")
