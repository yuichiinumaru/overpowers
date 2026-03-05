#!/usr/bin/env python3
import json
import os

def main():
    print("--- Flow Nexus Platform Integration Check ---")
    
    # Check if flow-nexus MCP is installed in Claude config
    config_paths = [
        os.path.expanduser("~/.config/Claude/claude_desktop_config.json"),
        os.path.expanduser("~/Library/Application Support/Claude/claude_desktop_config.json")
    ]
    
    found = False
    for p in config_paths:
        if os.path.exists(p):
            with open(p, "r") as f:
                try:
                    config = json.load(f)
                    if "flow-nexus" in config.get("mcpServers", {}):
                        print(f"[OK] flow-nexus MCP found in {p}")
                        found = True
                except:
                    continue
                    
    if not found:
        print("[!] flow-nexus MCP server NOT found in configuration.")
        print("    Requirement: register at flow-nexus.ruv.io")
        print("    Run: claude mcp add flow-nexus npx flow-nexus@latest mcp start")

if __name__ == "__main__":
    main()
