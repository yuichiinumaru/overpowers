#!/usr/bin/env python3
import argparse
import os

def create_asset(asset_type, name):
    print(f"Creating asset of type {asset_type} named {name}...")

    content = ""
    if asset_type == "document":
        content = f"# {name}\n\n## Purpose\n\n## Content\n"
        filename = f"{name.lower().replace(' ', '_')}.md"
    elif asset_type == "config":
        content = f"{{  \"name\": \"{name}\",\n  \"settings\": {{}}\n}}"
        filename = f"{name.lower().replace(' ', '_')}.json"
    else:
        content = f"// Asset: {name}\n"
        filename = f"{name.lower().replace(' ', '_')}.txt"

    with open(filename, "w") as f:
        f.write(content)

    print(f"Asset created at {filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a new asset template")
    parser.add_argument("type", choices=["document", "config", "text"], help="Type of asset")
    parser.add_argument("name", help="Name of the asset")

    args = parser.parse_args()
    create_asset(args.type, args.name)
