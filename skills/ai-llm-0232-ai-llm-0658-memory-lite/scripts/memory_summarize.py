import argparse
import os
from pathlib import Path
from datetime import datetime, timedelta

def summarize_memory(days):
    print(f"--- Quick Summary (Last {days} days) ---\n")
    
    # Check MEMORY.md
    if os.path.exists("MEMORY.md"):
        print("From long-term memory (MEMORY.md):")
        with open("MEMORY.md", "r") as f:
            lines = f.readlines()
            for line in lines[-10:]:  # Last 10 entries
                print(f"  {line.strip()}")
        print()

    # Check daily logs
    print("From daily logs:")
    for i in range(days):
        date_str = (datetime.now() - timedelta(days=i)).strftime("%Y-%m-%d")
        file_path = Path(f"memory/{date_str}.md")
        if file_path.exists():
            print(f"  [{date_str}]:")
            with open(file_path, "r") as f:
                lines = f.readlines()
                for line in lines[-5:]:  # Last 5 entries per day
                    print(f"    {line.strip()}")
        else:
            print(f"  [{date_str}]: No entries found.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Quick memory summary.")
    parser.add_argument("--days", type=int, default=2, help="Number of days to summarize")
    
    args = parser.parse_args()
    summarize_memory(args.days)
