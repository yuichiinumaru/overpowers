#!/usr/bin/env python3
"""
Inject all generated agents into opencode.json

This script reads the agents-all.json and merges it into your opencode.json,
preserving your existing configuration.

Usage:
    python3 inject-agents-to-config.py
"""

import json
from pathlib import Path
import shutil
from datetime import datetime

# Paths
OVERPOWERS_DIR = Path(__file__).parent
CONFIG_DIR = OVERPOWERS_DIR / "config" / "agents"
AGENTS_FILE = CONFIG_DIR / "agents-all.json"
OPENCODE_JSON = Path.home() / ".config" / "opencode" / "opencode.json"
BACKUP_DIR = Path.home() / ".config" / "opencode" / "backups"

def backup_config():
    """Create a timestamped backup of opencode.json"""
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = BACKUP_DIR / f"opencode.json.{timestamp}.bak"
    shutil.copy2(OPENCODE_JSON, backup_file)
    print(f"✅ Backup created: {backup_file}")
    return backup_file

def load_json(file_path):
    """Load JSON file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(file_path, data):
    """Save JSON file with proper formatting"""
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def main():
    # Check if agents file exists
    if not AGENTS_FILE.exists():
        print(f"❌ Error: {AGENTS_FILE} not found!")
        print("Run generate-agent-configs.py first.")
        return
    
    # Check if opencode.json exists
    if not OPENCODE_JSON.exists():
        print(f"❌ Error: {OPENCODE_JSON} not found!")
        return
    
    # Load files
    print("📖 Loading configuration files...")
    agents_data = load_json(AGENTS_FILE)
    opencode_config = load_json(OPENCODE_JSON)
    
    all_agents = agents_data.get("agent", {})
    print(f"📦 Found {len(all_agents)} agents to inject")
    
    # Backup
    backup_config()
    
    # Merge agents
    if "agent" not in opencode_config:
        opencode_config["agent"] = {}
    
    existing_count = len(opencode_config["agent"])
    print(f"📊 Existing agents in opencode.json: {existing_count}")
    
    # Merge (preserving existing ones, but overwriting with new data if name matches)
    opencode_config["agent"].update(all_agents)
    
    final_count = len(opencode_config["agent"])
    new_count = final_count - existing_count
    
    # Save
    print("💾 Saving updated opencode.json...")
    save_json(OPENCODE_JSON, opencode_config)
    
    print(f"\n✅ SUCCESS!")
    print(f"   Total agents: {final_count}")
    print(f"   Newly added: {new_count}")
    print(f"   Updated: {len(all_agents) - new_count}")
    print(f"\n🚀 Agora reinicie o OpenCode para carregar o Exército completo!")
    print(f"\n💡 Se ficar lento, remova categorias inteiras em opencode.json > agent")

if __name__ == "__main__":
    main()
