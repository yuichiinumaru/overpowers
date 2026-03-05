#!/usr/bin/env python3
"""
Run the full Denario research pipeline.
"""
import os
import sys
from denario import Denario, Journal

def main():
    project_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    
    if not os.path.exists(project_dir):
        print(f"Error: Directory '{project_dir}' does not exist.")
        sys.exit(1)

    print(f"Starting full pipeline in: {project_dir}")
    den = Denario(project_dir=project_dir)

    print("Step 1: Generating Idea...")
    den.get_idea()

    print("Step 2: Developing Methodology...")
    den.get_method()

    print("Step 3: Generating Results...")
    den.get_results()

    print("Step 4: Generating Paper (APS format)...")
    den.get_paper(journal=Journal.APS)

    print("Pipeline completed successfully.")

if __name__ == "__main__":
    main()
