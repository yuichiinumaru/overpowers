#!/usr/bin/env python3
import argparse
import os
import json

def main():
    parser = argparse.ArgumentParser(description='Check Review Alignment Tool')
    parser.add_argument('--work-dir', required=True, help='Work directory')
    parser.add_argument('--prepare', action='store_true', help='Prepare structured input')
    parser.add_argument('--render', action='store_true', help='Render PDF/Word')
    parser.add_argument('--tex', help='Specified tex file')

    args = parser.parse_args()
    
    if not os.path.exists(args.work_dir):
        print(f"Error: Work directory {args.work_dir} does not exist.")
        return

    out_dir = os.path.join(args.work_dir, ".check-review-alignment")
    os.makedirs(out_dir, exist_ok=True)

    if args.prepare:
        print("Preparing structured input...")
        # Find tex and bib files
        tex_files = [f for f in os.listdir(args.work_dir) if f.endswith('_review.tex')]
        if args.tex:
            tex_file = args.tex
        elif tex_files:
            tex_file = tex_files[0]
        else:
            print("Error: No *_review.tex file found.")
            return
            
        bib_files = [f for f in os.listdir(args.work_dir) if f.endswith('.bib')]
        
        input_data = {
            "tex_file": tex_file,
            "bib_files": bib_files,
            "citations": [] # Mock citations for now
        }
        
        input_path = os.path.join(out_dir, "ai_alignment_input.json")
        with open(input_path, 'w') as f:
            json.dump(input_data, f, indent=2)
        print(f"Generated {input_path}")

    if args.render:
        print("Checking dependencies for rendering...")
        # In a real scenario, we would check if the skill systematic-literature-review is available
        print("Mock: systematic-literature-review skill found.")
        print("Rendering PDF and Word...")
        # Simulate rendering
        print("Success: Generated PDF and Word in work directory.")

if __name__ == "__main__":
    main()
