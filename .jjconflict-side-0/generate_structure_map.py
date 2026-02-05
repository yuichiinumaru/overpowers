#!/usr/bin/env python3
import os
from pathlib import Path

def get_file_type(path):
    parts = path.parts
    if "agents" in parts:
        return "Agent"
    if "services" in parts:
        return "Service"
    if "scripts" in parts:
        return "Script"
    if "hooks" in parts:
        return "Hook"
    if "workflows" in parts:
        return "Workflow"
    if "skills" in parts:
        return "Skill"
    if "lib" in parts:
        return "Library"
    if "config" in parts:
        return "Configuration"
    return "File"

def generate_structure_map():
    root_dir = Path(".")
    output_file = Path("docs/project_structure_map.md")

    # Exclude directories
    exclude_dirs = {
        "node_modules", ".git", "__pycache__", "dist", "coverage",
        ".claude-plugin", ".codex", ".opencode"
    }

    lines = ["# Project Structure Map\n", "\n"]
    lines.append("| Type | Path | Description (Inferred) |\n")
    lines.append("|---|---|---|\n")

    key_entities = []

    for root, dirs, files in os.walk(root_dir):
        # Modify dirs in-place to exclude unwanted directories
        dirs[:] = [d for d in dirs if d not in exclude_dirs]

        path = Path(root)

        for file in sorted(files):
            file_path = path / file
            relative_path = file_path.relative_to(root_dir)

            # Skip hidden files
            if file.startswith("."):
                continue

            file_type = get_file_type(relative_path)

            # Simple inference
            description = ""
            if file_path.suffix == ".md":
                description = "Documentation"
            elif file_path.suffix == ".json":
                description = "Data / Config"
            elif file_path.suffix == ".py":
                description = "Python Source"
            elif file_path.suffix in [".ts", ".js"]:
                description = "JavaScript/TypeScript Source"
            elif file_path.suffix == ".sh":
                description = "Shell Script"

            line = f"| {file_type} | `{relative_path}` | {description} |\n"
            lines.append(line)

            if file_type not in ["File", "Configuration"] and file_path.suffix in [".md", ".py", ".ts", ".js", ".sh"]:
                 key_entities.append((file_type, str(relative_path)))

    lines.append("\n## Key Entities Analysis\n\n")
    lines.append("Based on directory structure and file types:\n\n")

    from collections import Counter
    type_counts = Counter([k[0] for k in key_entities])

    for type_name, count in type_counts.items():
        lines.append(f"- **{type_name}s**: {count}\n")

    output_file.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, "w") as f:
        f.writelines(lines)

    print(f"Structure map generated at {output_file}")

if __name__ == "__main__":
    generate_structure_map()
