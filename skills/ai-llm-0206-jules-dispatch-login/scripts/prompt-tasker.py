#!/usr/bin/env python3
import sys
import json
import argparse
import subprocess
import os
import time

def get_repo():
    try:
        url = subprocess.check_output(["git", "remote", "get-url", "origin"], universal_newlines=True).strip()
        if url.endswith(".git"):
            url = url[:-4]
        if "/" in url:
            parts = url.split("/")
            return f"{parts[-2]}/{parts[-1]}"
        elif ":" in url:
            return url.split(":")[-1]
    except Exception:
        pass
    return "yuichiinumaru/" + os.path.basename(os.getcwd())

def replace_in_object(data, search_str, replace_str):
    if isinstance(data, dict):
        return {k: replace_in_object(v, search_str, replace_str) for k, v in data.items()}
    elif isinstance(data, list):
        return [replace_in_object(i, search_str, replace_str) for i in data]
    elif isinstance(data, str):
        if search_str in data:
            return data.replace(search_str, replace_str)
        return data
    else:
        return data

def main():
    parser = argparse.ArgumentParser(description="Dispatch a Jules session using a robust JSON prompt structure.")
    parser.add_argument("-p", "--prompt", required=True, help="Path to the prompt JSON file")
    parser.add_argument("-t", "--task", help="Relative path to the task MD file (optional)")
    parser.add_argument("--repo", help="Target repository (e.g., owner/repo) - defaults to auto-detect", default="")
    parser.add_argument("--redundancy", type=int, default=2, help="Number of parallel sessions (default: 2)")
    
    args = parser.parse_args()

    # Read JSON prompt
    if not os.path.exists(args.prompt):
        print(f"❌ Error: Prompt file '{args.prompt}' not found.")
        sys.exit(1)
        
    try:
        with open(args.prompt, "r", encoding="utf-8") as f:
            prompt_data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"❌ Error parsing JSON prompt '{args.prompt}': {e}")
        sys.exit(1)

    # Read and embed Task content if provided
    task_content = ""
    if args.task:
        if not os.path.exists(args.task):
            print(f"❌ Error: Task file '{args.task}' not found.")
            sys.exit(1)
            
        with open(args.task, "r", encoding="utf-8") as f:
            task_content = f.read()

        # Perform deep replacement looking for {{TASK_CONTENT}}
        prompt_data_str = json.dumps(prompt_data)
        if "{{TASK_CONTENT}}" in prompt_data_str:
            prompt_data = replace_in_object(prompt_data, "{{TASK_CONTENT}}", task_content)
        else:
            # If the placeholder isn't there, append it cleanly as a root node
            prompt_data["task_payload_injected"] = task_content

    # Determine targeted repo
    repo = args.repo if args.repo else get_repo()
    
    # Compile the final JSON payload
    final_payload = json.dumps(prompt_data, ensure_ascii=False)

    # Setup Logging
    log_dir = "/tmp/jules-dispatch"
    os.makedirs(log_dir, exist_ok=True)
    timestamp = int(time.time())
    task_name = os.path.basename(args.task).replace(".md", "") if args.task else "no-task"
    prompt_name = os.path.basename(args.prompt).replace(".json", "")
    log_file = os.path.join(log_dir, f"{prompt_name}_{task_name}-{timestamp}.log")
    
    print(f"📡 Dispatching: [Prompt: {prompt_name}] + [Task: {task_name}] ({args.redundancy}x redundancy)")
    
    # Launch Jules asynchronously via subprocess
    cmd = [
        "jules", "remote", "new",
        "--repo", repo,
        "--parallel", str(args.redundancy),
        "--session", final_payload
    ]
    
    with open(log_file, "w", encoding="utf-8") as lf:
        proc = subprocess.Popen(cmd, stdout=lf, stderr=subprocess.STDOUT)
    
    print(f"✅ Launched background PID: {proc.pid}")
    print(f"   Log: {log_file}\n")
    
if __name__ == "__main__":
    main()
