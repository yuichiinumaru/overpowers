#!/usr/bin/env python3
import sys
import subprocess
import argparse
import os

def main():
    parser = argparse.ArgumentParser(description="Add shadcn/ui components.")
    parser.add_argument('components', nargs='+', help="The components to add (e.g., button, card, dialog)")
    args = parser.parse_args()

    print(f"Adding shadcn components: {', '.join(args.components)}")
    
    # Properly escape commands for security
    for component in args.components:
        print(f"Installing {component}...")
        try:
            cmd = ["npx", "shadcn@latest", "add", component, "--yes"]
            subprocess.run(cmd, check=True)
            print(f"Successfully installed {component}.")
        except subprocess.CalledProcessError as e:
            print(f"Error installing {component}: {e}")
            sys.exit(1)

if __name__ == "__main__":
    main()
