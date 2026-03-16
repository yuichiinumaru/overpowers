import os
import re

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
    # Remove triple quotes and surrounding whitespace
    value = value.strip().strip("'").strip('"').strip()
    
    # Check if it's a known named color
    if value.lower() in COLOR_MAP:
        return f'"{COLOR_MAP[value.lower()]}"'
    
    # Check if it's a hex code that was just improperly quoted
    if re.match(r"^#?[0-9A-Fa-f]{6}$", value):
        if not value.startswith("#"):
            value = "#" + value
        return f'"{value}"'
    
    # For values like '''"#008080"""
    hex_match = re.search(r"#[0-9A-Fa-f]{6}", value)
    if hex_match:
        return f'"{hex_match.group(0)}"'
        
    return None

def process_file(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Find the frontmatter
    match = re.match(r"^(---\s*\n)(.*?)(\n---)", content, re.DOTALL)
    if not match:
        return False

    prefix, frontmatter, suffix = match.groups()
    
    # Replace color line
    pattern = re.compile(r"^color:\s*(.*)$", re.MULTILINE)
    color_match = pattern.search(frontmatter)
    
    if not color_match:
        return False
        
    old_value = color_match.group(1).strip()
    new_value = fix_color(old_value)
    
    if new_value and new_value != old_value:
        new_frontmatter = pattern.sub(f"color: {new_value}", frontmatter)
        new_content = prefix + new_frontmatter + suffix + content[match.end():]
        
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Fixed {path}: {old_value} -> {new_value}")
        return True
    
    return False

if __name__ == "__main__":
    count = 0
    for filename in os.listdir(AGENTS_DIR):
        if filename.endswith(".md"):
            if process_file(os.path.join(AGENTS_DIR, filename)):
                count += 1
    print(f"Total files fixed: {count}")
