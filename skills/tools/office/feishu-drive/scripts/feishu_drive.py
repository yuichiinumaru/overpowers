#!/usr/bin/env python3
"""
Feishu Drive API Helper

Generates JSON payload for Feishu Drive operations.
Usage:
  python3 feishu_drive.py --action list --folder "fldcnXXX"
"""

import argparse
import json

def main():
    parser = argparse.ArgumentParser(description="Feishu Drive Payload Generator")
    parser.add_argument("--action", required=True, choices=["list", "info", "create_folder", "move", "delete"])
    parser.add_argument("--folder", help="Folder token")
    parser.add_argument("--file", help="File token")
    parser.add_argument("--type", help="File type (doc, docx, sheet, etc.)")
    parser.add_argument("--name", help="Name for new folder")

    args = parser.parse_args()

    payload = {"action": args.action}

    if args.folder:
        payload["folder_token"] = args.folder
    if args.file:
        payload["file_token"] = args.file
    if args.type:
        payload["type"] = args.type
    if args.name:
        payload["name"] = args.name

    # Validation per SKILL.md rules
    if args.action == "create_folder" and not args.folder:
        print("WARNING: Bots usually don't have a root folder. create_folder without --folder might fail with 400 error.")

    print(json.dumps(payload, indent=2))

if __name__ == "__main__":
    main()
