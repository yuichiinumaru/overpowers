import os
import argparse
import re

def search_tasks(query, outcome=None, limit=10):
    task_dirs = ["docs/tasks", "docs/tasks/completed", "docs/tasks/planning"]
    results = []
    
    for task_dir in task_dirs:
        if not os.path.exists(task_dir):
            continue
            
        for filename in os.listdir(task_dir):
            if filename.endswith(".md"):
                path = os.path.join(task_dir, filename)
                with open(path, 'r', errors='ignore') as f:
                    content = f.read()
                    
                if re.search(query, content, re.IGNORECASE):
                    # Check outcome if specified
                    if outcome:
                        if outcome.upper() == "SUCCEEDED" and "[x]" not in content.lower():
                            continue
                        if outcome.upper() == "FAILED" and "failed" not in content.lower():
                            continue
                            
                    results.append({
                        "file": path,
                        "title": filename,
                        "snippet": content[:200].replace('\n', ' ') + "..."
                    })
                    
            if len(results) >= limit:
                break
        if len(results) >= limit:
            break
            
    return results

def main():
    parser = argparse.ArgumentParser(description="Search past tasks and reasoning")
    parser.add_argument("query", help="Search query")
    parser.add_argument("--outcome", choices=["SUCCEEDED", "FAILED"], help="Filter by outcome")
    parser.add_argument("--limit", type=int, default=10, help="Limit results")
    
    args = parser.parse_args()
    
    results = search_tasks(args.query, args.outcome, args.limit)
    
    if not results:
        print("No matching tasks found.")
    else:
        print(f"Found {len(results)} matching tasks:\n")
        for res in results:
            print(f"- {res['file']}")
            print(f"  {res['snippet']}\n")

if __name__ == "__main__":
    main()
