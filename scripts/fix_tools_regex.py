import os
import re

AGENTS_DIR = "agents"

def fix_tools_inline(content):
    # Match tools: ["A", "B"] or tools: [A, B]
    pattern = re.compile(r"tools:\s*\[(.*?)\]", re.MULTILINE)
    
    def replacer(match):
        tools_str = match.group(1)
        # Split by comma and clean up
        tools = [t.strip().strip("'").strip('"').strip() for t in tools_str.split(",")]
        new_tools = "tools:\n"
        for t in tools:
            if t:
                new_tools += f"  {t.lower()}: true\n"
        return new_tools.rstrip()

    return pattern.sub(replacer, content)

def fix_tools_list(content):
    # Match tools: followed by a list of - Item
    # This is trickier with regex, so we'll do it line by line
    lines = content.split("\n")
    new_lines = []
    in_tools_list = False
    
    for i, line in enumerate(lines):
        if line.startswith("tools:") and not "[" in line:
            # Check if next line starts with -
            if i + 1 < len(lines) and lines[i+1].strip().startswith("-"):
                in_tools_list = True
                new_lines.append("tools:")
                continue
        
        if in_tools_list:
            stripped = line.strip()
            if stripped.startswith("-"):
                tool = stripped[1:].strip().strip("'").strip('"').strip()
                new_lines.append(f"  {tool.lower()}: true")
                continue
            elif stripped == "" or ":" in line: # End of list or next field
                in_tools_list = False
                new_lines.append(line)
            else:
                # Still in list?
                new_lines.append(line)
        else:
            new_lines.append(line)
            
    return "\n".join(new_lines)

def process_file(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Find the frontmatter
    match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return False

    frontmatter = match.group(1)
    rest = content[match.end():]
    
    new_frontmatter = fix_tools_inline(frontmatter)
    new_frontmatter = fix_tools_list(new_frontmatter)
    
    if new_frontmatter != frontmatter:
        with open(path, "w", encoding="utf-8") as f:
            f.write("---\n" + new_frontmatter + "\n---" + rest)
        print(f"Fixed tools in {path}")
        return True
    
    return False

if __name__ == "__main__":
    count = 0
    for filename in os.listdir(AGENTS_DIR):
        if filename.endswith(".md"):
            if process_file(os.path.join(AGENTS_DIR, filename)):
                count += 1
    print(f"Total files fixed: {count}")
