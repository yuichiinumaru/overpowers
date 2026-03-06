#!/usr/bin/env python3
import sys
import subprocess

def manage_mcps(action, name=None, cmd_or_url=None, transport="stdio", args=None):
    if action == "list":
        subprocess.run(["gemini", "mcp", "list"])
    elif action == "remove" and name:
        subprocess.run(["gemini", "mcp", "remove", name])
    elif action == "add" and name and cmd_or_url:
        cmd = ["gemini", "mcp", "add", name, cmd_or_url]
        if transport == "http":
            cmd.extend(["--transport", "http"])
        if args:
            cmd.extend(args)
        print(f"Executing: {' '.join(cmd)}")
        subprocess.run(cmd)
    else:
        print("Invalid arguments.")
        print("Usage:")
        print("  list")
        print("  remove <name>")
        print("  add <name> <cmd_or_url> [--http] [additional args...]")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: manage_mcps.py <action> [args...]")
        sys.exit(1)
        
    action = sys.argv[1]
    name = sys.argv[2] if len(sys.argv) > 2 else None
    cmd_or_url = sys.argv[3] if len(sys.argv) > 3 else None
    
    transport = "stdio"
    args = []
    if "--http" in sys.argv:
        transport = "http"
        sys.argv.remove("--http")
    
    if len(sys.argv) > 4:
        args = sys.argv[4:]

    manage_mcps(action, name, cmd_or_url, transport, args)
