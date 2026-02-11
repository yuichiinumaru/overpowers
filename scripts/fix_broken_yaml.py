import os
import re

AGENTS_DIR = 'agents'

def fix_frontmatter(content):
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)', content, re.DOTALL)
    if not match:
        return content

    frontmatter_raw = match.group(1)
    body = match.group(2)

    new_lines = []
    lines = frontmatter_raw.split('\n')

    current_parent = None

    for line in lines:
        if line.strip() == '':
            new_lines.append(line)
            continue

        # Check indentation
        indent = len(line) - len(line.lstrip())

        if indent == 0:
            # Top level key
            if ':' in line:
                key, value = line.split(':', 1)
                value = value.strip()
                # If value is empty or indicates multiline string, set as parent
                if value == '' or value == '|' or value == '>':
                    current_parent = key
                else:
                    current_parent = None
            else:
                current_parent = None
            new_lines.append(line)
        else:
            # Indented line
            if current_parent:
                new_lines.append(line)
            else:
                # Orphaned indented line -> Remove
                # This catches the leftover lines from 'tools:' removal
                pass

    new_frontmatter = '\n'.join(new_lines)
    return f"---\n{new_frontmatter}\n---\n{body}"

def process_files():
    print("Scanning for broken YAML...")
    for root, dirs, files in os.walk(AGENTS_DIR):
        for file in files:
            if not file.endswith('.md'):
                continue
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r') as f:
                    content = f.read()

                new_content = fix_frontmatter(content)

                if new_content != content:
                    with open(filepath, 'w') as f:
                        f.write(new_content)
                    print(f"Fixed YAML in {filepath}")
            except Exception as e:
                print(f"Error processing {filepath}: {e}")

if __name__ == '__main__':
    process_files()
