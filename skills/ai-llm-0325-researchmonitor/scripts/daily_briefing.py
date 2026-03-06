import json
import os
import argparse
from datetime import datetime

CONFIG_FILE = "research_config.json"

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    return {"topics": [], "last_checked": "", "seen_items": []}

def save_config(config):
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=2)

def main():
    parser = argparse.ArgumentParser(description="ResearchMonitor Helper")
    parser.add_argument("--add-topic", help="Add a new research topic")
    parser.add_argument("--list-topics", action="store_true", help="List current topics")
    parser.add_argument("--update-date", action="store_true", help="Update last checked date")
    parser.add_argument("--check-seen", help="Check if item is already in memory")
    parser.add_argument("--mark-seen", help="Mark item as seen")
    
    args = parser.parse_args()
    config = load_config()
    
    if args.add_topic:
        if args.add_topic not in config["topics"]:
            config["topics"].append(args.add_topic)
            save_config(config)
            print(f"Added topic: {args.add_topic}")
            
    if args.list_topics:
        for t in config["topics"]:
            print(f"- {t}")
            
    if args.update_date:
        config["last_checked"] = datetime.now().strftime("%Y-%m-%d")
        save_config(config)
        print("Updated last checked date.")
        
    if args.check_seen:
        if args.check_seen in config["seen_items"]:
            print("true")
        else:
            print("false")
            
    if args.mark_seen:
        if args.mark_seen not in config["seen_items"]:
            config["seen_items"].append(args.mark_seen)
            # Optional: keep only last 1000 items
            if len(config["seen_items"]) > 1000:
                config["seen_items"] = config["seen_items"][-1000:]
            save_config(config)
            print(f"Marked as seen: {args.mark_seen}")

if __name__ == "__main__":
    main()
