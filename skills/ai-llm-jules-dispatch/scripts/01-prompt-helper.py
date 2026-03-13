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
    parser.add_argument("--redundancy", type=int, default=1, help="Number of parallel sessions (default: 1)")
    
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
    log_dir = ".agents/jules-dispatch"
    os.makedirs(log_dir, exist_ok=True)
    timestamp = int(time.time())
    task_name = os.path.basename(args.task).replace(".md", "") if args.task else "no-task"
    prompt_name = os.path.basename(args.prompt).replace(".json", "")
    log_file = os.path.join(log_dir, f"{prompt_name}_{task_name}-{timestamp}.log")
    
    print(f"📡 Dispatching: [Prompt: {prompt_name}] + [Task: {task_name}] ({args.redundancy}x redundancy)")
    
    cmd = [
        "jules", "remote", "new",
        "--repo", repo,
        "--parallel", str(args.redundancy),
        "--session", final_payload
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        out = result.stdout
        print(out)
        import re
        match = re.search(r"ID:\s*(\d+)", out)
        if match:
            session_id = match.group(1)
            print(f"✅ Extracted Session ID: {session_id}")
            
            # Save to tracking JSON
            tracking_file = ".agents/jules_sessions.json"
            tracking_data = {}
            if os.path.exists(tracking_file):
                with open(tracking_file, "r") as f:
                    try:
                        tracking_data = json.load(f)
                    except json.JSONDecodeError:
                        pass
                        
            tracking_data[session_id] = {
                "prompt": args.prompt,
                "task": args.task,
                "timestamp": timestamp,
                "status": "Awaiting User Feedback/Completed/Running" # Placeholder
            }
            
            with open(tracking_file, "w") as f:
                json.dump(tracking_data, f, indent=2)
                
            print(f"✅ Saved to {tracking_file}")
        else:
            print("⚠️ Could not parse Session ID from output.")
            
    except subprocess.CalledProcessError as e:
        error_msg = e.stderr.lower()
        print(f"❌ Jules execution failed: {e.stderr}")
        
        # Specific detection for Quota / Rate Limits
        quota_keywords = ["quota", "limit", "too many requests", "429", "rate limit"]
        if any(kw in error_msg for kw in quota_keywords):
            print("⚠️ [QUOTA EXCEEDED] Signaling for account rotation...")
            sys.exit(69) # Special exit code for Quota
            
        sys.exit(1)
    
if __name__ == "__main__":
    main()
