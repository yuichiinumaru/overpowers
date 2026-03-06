#!/usr/bin/env python3
"""
Dispatch multiple independent tasks in parallel using Gemini CLI.
"""
import sys
import subprocess
import argparse
import os

def main():
    parser = argparse.ArgumentParser(description="Dispatch parallel agents for independent tasks.")
    parser.add_argument("tasks", nargs="+", help="Task descriptions or paths to task files")
    parser.add_argument("--log-dir", default=".agents/reports", help="Directory for logs")
    
    args = parser.parse_args()
    
    os.makedirs(args.log_dir, exist_ok=True)
    
    processes = []
    
    for i, task in enumerate(args.tasks):
        log_file = os.path.join(args.log_dir, f"parallel-task-{i}-log.txt")
        
        # Determine prompt
        if os.path.isfile(task):
            prompt = f"Execute the task described in {task}"
        else:
            prompt = task
            
        print(f"Dispatching task {i}: {prompt[:50]}...")
        
        cmd = ["gemini", "--yolo", "-p", prompt]
        
        with open(log_file, "w") as f:
            p = subprocess.Popen(cmd, stdout=f, stderr=subprocess.STDOUT)
            processes.append(p)
            
    print(f"Dispatched {len(processes)} tasks. Waiting for completion...")
    
    for p in processes:
        p.wait()
        
    print("All tasks completed.")

if __name__ == "__main__":
    main()
