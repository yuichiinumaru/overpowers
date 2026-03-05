import requests
from bs4 import BeautifulSoup
import difflib
import os
import json

def track_competitors(competitors_file, storage_dir='tracker_storage'):
    if not os.path.exists(competitors_file):
        print(f"Error: {competitors_file} not found.")
        return

    if not os.path.exists(storage_dir):
        os.makedirs(storage_dir)

    with open(competitors_file, 'r') as f:
        competitors = json.load(f)

    for name, url in competitors.items():
        print(f"Checking {name} at {url}...")
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            current_content = response.text
            
            filename = os.path.join(storage_dir, f"{name.lower().replace(' ', '_')}.html")
            
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as f:
                    old_content = f.read()
                
                if old_content != current_content:
                    print(f"CHANGE DETECTED for {name}!")
                    # Basic diff summary
                    diff = difflib.unified_diff(
                        old_content.splitlines(),
                        current_content.splitlines(),
                        fromfile='old',
                        tofile='new',
                        n=0
                    )
                    print('\n'.join(list(diff)[:10])) # Show first 10 lines of diff
                else:
                    print(f"No changes for {name}.")
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(current_content)
                
        except Exception as e:
            print(f"Error checking {name}: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python competitor_tracker.py <competitors_json_file>")
        print("Format: {\"Competitor Name\": \"https://competitor.com\"}")
    else:
        track_competitors(sys.argv[1])
