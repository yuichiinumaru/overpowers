#!/usr/bin/env python3
import os
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description="Scaffold a new Machine Learning project structure.")
    parser.add_argument("name", help="Name of the project")
    args = parser.parse_args()

    project_name = args.name.lower().replace(" ", "-")
    
    directories = [
        "data/raw",
        "data/processed",
        "notebooks",
        "models",
        "src/data",
        "src/features",
        "src/models",
        "src/visualization",
        "reports/figures",
        "tests"
    ]

    for directory in directories:
        path = os.path.join(project_name, directory)
        os.makedirs(path, exist_ok=True)
        # Create a placeholder file to ensure directory is tracked if using git
        with open(os.path.join(path, ".gitkeep"), "w") as f:
            pass

    # Create basic files
    files = {
        "README.md": f"# {args.name}\n\nProject description goes here.",
        "requirements.txt": "pandas\nnumpy\nscikit-learn\nmatplotlib\nseaborn\njupyter",
        ".gitignore": "data/\nmodels/\n*.pyc\n.ipynb_checkpoints/",
        "setup.py": "from setuptools import find_packages, setup\n\nsetup(\n    name='src',\n    packages=find_packages(),\n    version='0.1.0',\n    description='',\n    author='Your name (or your organization)',\n    license='MIT',\n)"
    }

    for filename, content in files.items():
        with open(os.path.join(project_name, filename), "w") as f:
            f.write(content)

    print(f"Scaffolded Machine Learning project structure in '{project_name}/'")

if __name__ == "__main__":
    main()
