#!/usr/bin/env python3
"""
Initialize a Denario research project from a data description file.
"""
import sys
import os
import argparse
from denario import Denario, Journal

def main():
    parser = argparse.ArgumentParser(description="Initialize a Denario research project.")
    parser.add_argument("data_description_file", help="Path to the markdown file containing data description")
    parser.add_argument("--project-dir", default="./research_project", help="Directory for the research project")
    parser.add_argument("--journal", default="APS", help="Journal format (default: APS)")
    parser.add_argument("--run-full", action="store_true", help="Run the full pipeline (idea -> method -> results -> paper)")

    args = parser.parse_args()

    if not os.path.exists(args.data_description_file):
        print(f"Error: Data description file not found: {args.data_description_file}")
        sys.exit(1)

    with open(args.data_description_file, 'r') as f:
        data_description = f.read()

    print(f"Initializing Denario project in: {args.project_dir}")
    den = Denario(project_dir=args.project_dir)
    
    den.set_data_description(data_description)
    print("Data description set.")

    if args.run_full:
        print("Running full research pipeline...")
        
        print("1. Generating research idea...")
        den.get_idea()
        
        print("2. Developing methodology...")
        den.get_method()
        
        print("3. Executing experiments and generating results...")
        den.get_results()
        
        journal_type = getattr(Journal, args.journal.upper(), Journal.APS)
        print(f"4. Generating paper in {args.journal} format...")
        den.get_paper(journal=journal_type)
        
        print("Full pipeline completed successfully.")
    else:
        print("Project initialized. Run stage by stage using the Denario API or CLI.")

if __name__ == "__main__":
    main()
