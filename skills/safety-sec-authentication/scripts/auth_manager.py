#!/usr/bin/env python3
import json
import os
import argparse
import sys
from pathlib import Path

# Note: This tool assumes playwright is installed.
# If not available, it will fail gracefully with a descriptive error.

def setup_auth(data_dir):
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("Error: playwright not installed. Run 'pip install playwright' and 'playwright install chrome'.", file=sys.stderr)
        sys.exit(1)

    profile_dir = Path(data_dir) / "browser_profile"
    state_file = Path(data_dir) / "state.json"
    profile_dir.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        print(f"Launching Chrome with profile: {profile_dir}")
        context = p.chromium.launch_persistent_context(
            user_data_dir=str(profile_dir),
            channel="chrome",
            headless=False
        )
        page = context.new_page()
        page.goto("https://notebooklm.google.com")
        
        print("\n--- ACTION REQUIRED ---")
        print("Please log in to your Google Account in the browser window.")
        print("Once logged in and NotebookLM is loaded, come back here and press Enter.")
        input("Press Enter once logged in...")
        
        print(f"Saving session state to {state_file}")
        context.storage_state(path=str(state_file))
        context.close()
    
    print("Authentication setup complete.")

def main():
    parser = argparse.ArgumentParser(description="Authentication Manager")
    parser.add_argument("command", choices=["setup"], help="Command to run")
    parser.add_argument("--data-dir", default=str(Path.home() / ".overpowers" / "auth"), help="Data directory")
    
    args = parser.parse_args()
    
    if args.command == "setup":
        setup_auth(args.data_dir)

if __name__ == "__main__":
    main()
