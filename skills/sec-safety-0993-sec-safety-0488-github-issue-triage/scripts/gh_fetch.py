#!/usr/bin/env python3
import argparse
import subprocess
import json
import sys
from datetime import datetime, timedelta

def get_repo():
    try:
        result = subprocess.run(['gh', 'repo', 'view', '--json', 'nameWithOwner', '-q', '.nameWithOwner'], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error getting repository: {e.stderr}", file=sys.stderr)
        sys.exit(1)

def fetch_data(type_str, hours, output_format):
    repo = get_repo()
    cutoff_date = (datetime.utcnow() - timedelta(hours=hours)).isoformat() + "Z"
    
    cmd = []
    if type_str == 'issues':
        cmd = ['gh', 'issue', 'list', '--repo', repo, '--state', 'all', '--limit', '500', '--json', 'number,title,state,createdAt,updatedAt,labels,author,body']
    elif type_str == 'prs':
        cmd = ['gh', 'pr', 'list', '--repo', repo, '--state', 'all', '--limit', '500', '--json', 'number,title,state,createdAt,updatedAt']
    else:
        print(f"Unknown type: {type_str}", file=sys.stderr)
        sys.exit(1)

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        data = json.loads(result.stdout)
        
        filtered_data = [
            item for item in data 
            if item.get('createdAt', '') >= cutoff_date or item.get('updatedAt', '') >= cutoff_date
        ]
        
        if output_format == 'json':
            print(json.dumps(filtered_data, indent=2))
        else:
            for item in filtered_data:
                print(f"#{item['number']}: {item['title']} ({item['state']})")
                
    except subprocess.CalledProcessError as e:
        print(f"Error fetching data: {e.stderr}", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON output: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fetch issues or PRs from GitHub.')
    parser.add_argument('type', choices=['issues', 'prs'], help='Type of data to fetch')
    parser.add_argument('--hours', type=int, default=48, help='Hours to look back')
    parser.add_argument('--output', choices=['json', 'text'], default='json', help='Output format')
    
    args = parser.parse_args()
    fetch_data(args.type, args.hours, args.output)
