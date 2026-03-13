#!/usr/bin/env python3
import sys
import os

def add_composition(id, component, root_file="src/Root.tsx"):
    if not os.path.exists(root_file):
        print(f"Error: {root_file} not found.")
        return

    new_line = f'      <Composition id="{id}" component={{{component}}} durationInFrames={{100}} fps={{30}} width={{1080}} height={{1080}} />\n'
    
    with open(root_file, "r") as f:
        lines = f.readlines()

    # Find the end of the first <Folder> or the return statement
    for i, line in enumerate(lines):
        if "</Folder>" in line or "</>" in line or ");" in line:
            lines.insert(i, new_line)
            break
    else:
        lines.append(new_line)

    with open(root_file, "w") as f:
        f.writelines(lines)
    
    print(f"Added composition '{id}' to {root_file}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: add_composition.py <ID> <ComponentName> [root_file]")
        sys.exit(1)
    
    id = sys.argv[1]
    component = sys.argv[2]
    root = sys.argv[3] if len(sys.argv) > 3 else "src/Root.tsx"
    add_composition(id, component, root)
