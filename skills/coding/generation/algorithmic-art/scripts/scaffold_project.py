#!/usr/bin/env python3
import os
import shutil
import argparse

def scaffold_project(name):
    # Base directory for the new project
    project_dir = os.path.join(os.getcwd(), name)
    
    if os.path.exists(project_dir):
        print(f"Error: Directory '{name}' already exists.")
        return

    os.makedirs(project_dir)
    print(f"Created directory: {project_dir}")

    # Path to templates (relative to this script)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    skill_root = os.path.dirname(script_dir)
    templates_dir = os.path.join(skill_root, "templates")

    # Files to copy
    files_to_copy = ["viewer.html", "generator_template.js"]

    for filename in files_to_copy:
        src = os.path.join(templates_dir, filename)
        dst = os.path.join(project_dir, filename)
        if os.path.exists(src):
            shutil.copy(src, dst)
            print(f"Copied {filename} to {project_dir}")
        else:
            print(f"Warning: Template {filename} not found in {templates_dir}")

    # Create placeholder philosophy.md
    philosophy_file = os.path.join(project_dir, "philosophy.md")
    with open(philosophy_file, "w") as f:
        f.write(f"# {name} Algorithmic Philosophy\n\n[Write your 4-6 paragraph philosophy here based on SKILL.md guidelines]\n")
    print(f"Created placeholder: philosophy.md")

    print(f"\nScaffolding complete for project '{name}'.")
    print(f"Follow the instructions in SKILL.md to express your philosophy in code using the provided templates.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scaffold a new Algorithmic Art project.")
    parser.add_argument("name", help="Name of the new project directory")
    args = parser.parse_args()

    scaffold_project(args.name)
