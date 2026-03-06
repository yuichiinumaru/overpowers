#!/usr/bin/env python3
import sys
import subprocess
import json
import argparse
from datetime import datetime, timedelta

def fetch_github_data(type, hours, output_format):
    now = datetime.utcnow()
    cutoff_date = (now - timedelta(hours=hours)).isoformat() + "Z"
    
    cmd = [
        "gh", type, "list",
        "--state", "all",
        "--limit", "500",
        "--json", "number,title,state,createdAt,updatedAt,labels,author,body"
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        data = json.loads(result.stdout)
        
        filtered_data = [
            item for item in data 
            if item['createdAt'] >= cutoff_date or item['updatedAt'] >= cutoff_date
        ]
        
        if output_format == "json":
            print(json.dumps(filtered_data, indent=2))
        else:
            for item in filtered_data:
                print(f"#{item['number']} - {item['title']} ({item['state']})")
                
    except subprocess.CalledProcessError as e:
        print(f"Error fetching GitHub data: {e.stderr}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch issues or PRs from GitHub")
    parser.add_argument("type", choices=["issue", "pr"], help="Type of data to fetch")
    parser.add_argument("--hours", type=int, default=48, help="Hours to look back")
    parser.add_argument("--output", choices=["json", "text"], default="json", help="Output format")
    
    args = parser.parse_args()
    
    # gh issue list or gh pr list
    fetch_type = "issue" if args.type == "issue" else "pr"
    
    fetch_github_data(fetch_type, args.hours, args.output)
