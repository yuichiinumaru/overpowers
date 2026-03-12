#!/usr/bin/env python3
import os
import sys

def check_env():
    required = ["ALUVIA_API_KEY", "BRAVE_API_KEY"]
    missing = [var for var in required if not os.environ.get(var)]
    
    if missing:
        print(f"Error: Missing environment variables: {', '.join(missing)}")
        print("Please set them before running the scripts:")
        print("  export ALUVIA_API_KEY=your_aluvia_key")
        print("  export BRAVE_API_KEY=your_brave_key")
        return False
    
    print("✅ All required environment variables are set.")
    if os.environ.get("ALUVIA_CONNECTION_ID"):
        print(f"ℹ️ ALUVIA_CONNECTION_ID is set to: {os.environ.get('ALUVIA_CONNECTION_ID')}")
    else:
        print("ℹ️ ALUVIA_CONNECTION_ID is not set (optional).")
    return True

def main():
    print("--- Aluvia Brave Search Connection Test ---")
    if check_env():
        print("\nNote: This script only checks configuration.")
        print("To perform actual searches, please ensure search.js and content.js are present")
        print("and that 'npm ci' has been run in the skill directory.")
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
