#!/usr/bin/env python3
import sys
import os
from datetime import datetime

def log_shipped(content_type, title, url="", platform="", goal=""):
    today = datetime.now().strftime("%Y-%m-%d")
    log_dir = "content"
    log_file = os.path.join(log_dir, "log.md")
    
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
        
    entry = f"""
### {today}
- **[{content_type.upper()}]** "{title}"
  - URL: {url}
  - Platform: {platform}
  - Goal: {goal}
"""
    with open(log_file, "a") as f:
        f.write(entry)
        
    print(f"Logged shipped content to {log_file}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: log_shipped.py <type> <title> [url] [platform] [goal]")
        sys.exit(1)
        
    log_shipped(
        sys.argv[1], 
        sys.argv[2], 
        sys.argv[3] if len(sys.argv) > 3 else "",
        sys.argv[4] if len(sys.argv) > 4 else "",
        sys.argv[5] if len(sys.argv) > 5 else ""
    )
