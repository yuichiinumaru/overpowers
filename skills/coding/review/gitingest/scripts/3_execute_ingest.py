import os
import json
import argparse
import subprocess
import time

def main():
    parser = argparse.ArgumentParser(description="Execute gitingest chunks.")
    parser.add_argument("plan_file", help="Path to chunks_plan.json")
    parser.add_argument("-o", "--out-dir", default="chunks_output", help="Output directory for MD files")
    
    args = parser.parse_args()
    
    with open(args.plan_file, "r", encoding="utf-8") as f:
        plan = json.load(f)
        
    repo_path = plan["repo_path"]
    chunks = plan["chunks"]
    
    os.makedirs(args.out_dir, exist_ok=True)
    
    print(f"Starting ingestion of {len(chunks)} chunks into {args.out_dir}...")
    
    for i, chunk in enumerate(chunks, 1):
        output_file = os.path.join(args.out_dir, chunk["name"])
        
        cmd = ["gitingest", repo_path, "-o", output_file]
        for pattern in chunk["includes"]:
            # Need to ensure pattern matches gitingest wildcard format
            cmd.extend(["--include-pattern", pattern])
            
        print(f"[{i}/{len(chunks)}] Ingesting {chunk['name']} (approx {chunk['size']/1024:.1f} KB)...")
        
        try:
            # 120s timeout to prevent hanging as requested
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            if result.returncode != 0:
                print(f"  Warning: failed to ingest {chunk['name']}: {result.stderr}")
        except subprocess.TimeoutExpired:
            print(f"  Error: Timeout expired (120s) while processing {chunk['name']}")
            
        # brief sleep to avoid OS io spikes
        time.sleep(0.5)
        
    print("Ingestion complete.")

if __name__ == "__main__":
    main()
