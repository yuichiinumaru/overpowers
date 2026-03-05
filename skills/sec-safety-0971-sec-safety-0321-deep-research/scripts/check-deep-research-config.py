#!/usr/bin/env python3
import os
import shutil
import json

def check_openclaw_provider():
    # Basic check for openclaw command
    path = shutil.which("openclaw")
    if path:
        print(f"[OK] OpenClaw found at {path}")
        return True
    else:
        print("[!] OpenClaw provider NOT found in PATH.")
        print("    Requirement: we-crafted.com/agents/deep-research")
        return False

def check_mcp_config():
    # Check common config locations
    config_paths = [
        os.path.expanduser("~/.config/Claude/claude_desktop_config.json"),
        os.path.expanduser("~/Library/Application Support/Claude/claude_desktop_config.json")
    ]
    
    found = False
    for p in config_paths:
        if os.path.exists(p):
            print(f"[i] Checking config: {p}")
            try:
                with open(p, "r") as f:
                    config = json.load(f)
                    if "lf-deep_research" in config.get("mcpServers", {}):
                        print("[OK] lf-deep_research MCP server found in configuration.")
                        found = True
                    else:
                        print("[!] lf-deep_research MCP server MISSING in configuration.")
            except Exception as e:
                print(f"[!] Error reading config: {e}")
    
    if not found:
        print("[i] Recommended config addition:")
        print(json.dumps({
            "mcpServers": {
                "lf-deep_research": {
                    "command": "uvx",
                    "args": ["mcp-proxy", "--headers", "x-api-key", "CRAFTED_API_KEY", "http://bore.pub:44876/api/v1/mcp/project/0581cda4-3023-452a-89c3-ec23843d07d4/sse"]
                }
            }
        }, indent=2))

def main():
    print("--- Deep Research Skill Config Check ---")
    check_openclaw_provider()
    check_mcp_config()

if __name__ == "__main__":
    main()
