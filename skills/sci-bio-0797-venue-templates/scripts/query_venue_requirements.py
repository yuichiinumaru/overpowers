#!/usr/bin/env python3
import argparse
import os
import sys

def search_requirements(venue_name, category):
    base_path = "references"
    files = {
        'journal': 'journals_formatting.md',
        'conference': 'conferences_formatting.md',
        'poster': 'posters_guidelines.md',
        'grant': 'grants_requirements.md'
    }
    
    if category not in files:
        print(f"Error: Unknown category '{category}'. Choose from: {', '.join(files.keys())}")
        return

    file_path = os.path.join(os.path.dirname(__file__), "..", base_path, files[category])
    
    if not os.path.exists(file_path):
        print(f"Error: Requirements file not found at {file_path}")
        return

    print(f"Searching for '{venue_name}' in {files[category]}...")
    
    found = False
    with open(file_path, 'r') as f:
        content = f.read()
        # Simple keyword search
        if venue_name.lower() in content.lower():
            # In a real implementation, we would parse the markdown and extract relevant sections
            # For now, we'll just indicate it was found and show a snippet
            print(f"Match found for '{venue_name}'.")
            # Extract some context around the match
            index = content.lower().find(venue_name.lower())
            start = max(0, index - 100)
            end = min(len(content), index + 500)
            print("\n--- Snippet ---")
            print(content[start:end] + "...")
            print("---------------")
            found = True
            
    if not found:
        print(f"No specific requirements found for '{venue_name}'.")

def main():
    parser = argparse.ArgumentParser(description='Query venue formatting requirements.')
    parser.add_argument('venue', help='Name of the venue (e.g., "Nature", "NeurIPS")')
    parser.add_argument('--category', choices=['journal', 'conference', 'poster', 'grant'], default='journal', help='Category of the venue')

    args = parser.parse_args()

    search_requirements(args.venue, args.category)

if __name__ == "__main__":
    main()
