import json
import os
import argparse
from datetime import datetime

def load_data(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return json.load(f)
    return {"history": []}

def save_data(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)

def add_entry(file_path, domain, keywords_data):
    data = load_data(file_path)
    entry = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "domain": domain,
        "rankings": keywords_data
    }
    data["history"].append(entry)
    save_data(file_path, data)
    print(f"Added ranking snapshot for {domain}")

def compare_ranks(file_path, domain, date1, date2):
    data = load_data(file_path)
    # Find entries for dates
    snap1 = next((s for s in data["history"] if s["date"] == date1 and s["domain"] == domain), None)
    snap2 = next((s for s in data["history"] if s["date"] == date2 and s["domain"] == domain), None)
    
    if not snap1 or not snap2:
        print("Could not find snapshots for both dates.")
        return

    comparison = []
    for kw, rank2 in snap2["rankings"].items():
        rank1 = snap1["rankings"].get(kw)
        change = rank1 - rank2 if rank1 else "New"
        comparison.append({
            "keyword": kw,
            "old_rank": rank1,
            "new_rank": rank2,
            "change": change
        })
    
    return comparison

def main():
    parser = argparse.ArgumentParser(description="Rank Tracker Helper")
    subparsers = parser.add_argument_group("actions")
    
    parser.add_argument("--file", default="rankings.json", help="Path to rankings JSON file")
    parser.add_argument("--domain", required=True, help="Domain being tracked")
    
    parser.add_argument("--add", help="Add ranking data as 'kw1:rank1,kw2:rank2'")
    parser.add_argument("--compare", help="Compare two dates 'date1,date2'")
    
    args = parser.parse_args()
    
    if args.add:
        kw_data = {}
        for pair in args.add.split(','):
            kw, rank = pair.split(':')
            kw_data[kw.strip()] = int(rank)
        add_entry(args.file, args.domain, kw_data)
        
    if args.compare:
        d1, d2 = args.compare.split(',')
        comparison = compare_ranks(args.file, args.domain, d1.strip(), d2.strip())
        if comparison:
            print(f"Comparison for {args.domain}: {d1} -> {d2}")
            print(json.dumps(comparison, indent=2))

if __name__ == "__main__":
    main()
