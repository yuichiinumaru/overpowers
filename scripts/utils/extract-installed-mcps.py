#!/usr/bin/env python3
"""
extract-installed-mcps.py

Scans common locations for user-installed MCP configurations
(OpenCode, Gemini CLI, Antigravity) and extracts:
1. unique environment variables into a format suitable for .env.example
2. a consolidated JSON of all user-installed MCP plugins

Usage:
  python scripts/extract-installed-mcps.py
"""

import os
import json
import re
import argparse

CONFIG_LOCATIONS = [
    os.path.expanduser("~/.opencode/opencode.json"),
    os.path.expanduser("~/.gemini/antigravity/mcp_config.json"),
    os.path.expanduser("~/.config/gemini/mcp_config.json"),
    os.path.expanduser("~/.config/gemini/mcp.json"),
]

def load_json(path):
    if os.path.exists(path):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
                content = re.sub(r',\s*([\]}])', r'\1', content)
                return json.loads(content)
        except Exception as e:
            print(f"Warning: Failed to parse {path} - {e}")
    return {}

def extract(env_path=None):
    all_mcps = {}
    env_vars = set()

    for file_path in CONFIG_LOCATIONS:
        data = load_json(file_path)
        if not data:
            continue

        # Determine the MCP root key
        mcp_data = data.get("mcp") or data.get("mcpServers")
        if not mcp_data or not isinstance(mcp_data, dict):
            continue

        for server_name, server_config in mcp_data.items():
            # Add to consolidated list
            all_mcps[server_name] = server_config

            # Extract env vars
            env_dict = server_config.get("environment") or server_config.get("env")
            if env_dict and isinstance(env_dict, dict):
                for k, v in env_dict.items():
                    # don't add stuff like PATH or PYTHONPATH to .env.example usually, 
                    # but let's include everything explicitly requested for now.
                    if k not in ["PATH", "PYTHONPATH"]:
                        env_vars.add(k)

    # Determine where we are outputting these variables. 
    # Default is repo root .env.example, unless --env was provided.
    if env_path:
        target_env = env_path
        if not os.path.exists(target_env):
            # If the user-provided env doesn't exist yet, we'll create it
            open(target_env, 'w').close()
    else:
        target_env = os.path.join(os.path.dirname(__file__), "..", ".env.example")
    
    existing_envs = set()
    if os.path.exists(target_env):
        with open(target_env, "r") as f:
            for line in f:
                if "=" in line and not line.startswith("#"):
                    existing_envs.add(line.split("=")[0].strip())
                    
    new_vars = sorted([v for v in env_vars if v not in existing_envs])
    
    if new_vars:
        with open(target_env, "a") as f:
            f.write("\n# --- Extracted User Variables ---\n")
            for var in new_vars:
                f.write(f"{var}=''\n")
        print(f"--- Appended {len(new_vars)} new variables to {target_env} ---")
    else:
        print("--- No new environment variables found to append. ---")

    # Save consolidated MCPs to standard file in OpenCode format
    output_file = os.path.join(os.path.dirname(__file__), "..", "extracted_user_mcps.json")
    with open(output_file, 'w') as f:
        json.dump({"mcp": all_mcps}, f, indent=4)
        
    print(f"\n--- Extracted {len(all_mcps)} user MCPs to {output_file} ---")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract user MCPs and ENV vars.")
    parser.add_argument("--env", type=str, help="Path to an existing .env file to check/append keys to", default="")
    args = parser.parse_args()

    extract(env_path=args.env if args.env else None)
