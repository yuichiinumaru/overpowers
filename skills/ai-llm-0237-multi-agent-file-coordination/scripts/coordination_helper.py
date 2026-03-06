import argparse
import os
import json
import time
import random
import string

COORDINATION_DIR = "coordination"

def get_agent_id():
    timestamp = int(time.time())
    random_chars = ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))
    return f"agent_{timestamp}_{random_chars}"

def acquire_lock(agent_id, files):
    os.makedirs(os.path.join(COORDINATION_DIR, "agent_locks"), exist_ok=True)
    lock_file = os.path.join(COORDINATION_DIR, "agent_locks", f"{agent_id}.lock")
    
    lock_data = {
        "agent_id": agent_id,
        "files": files,
        "timestamp": time.time()
    }
    
    # In a real system, we would check active_work_registry.json for conflicts here
    
    with open(lock_file, "w") as f:
        json.dump(lock_data, f)
    print(f"Lock acquired for agent {agent_id} on files: {', '.join(files)}")

def release_lock(agent_id):
    lock_file = os.path.join(COORDINATION_DIR, "agent_locks", f"{agent_id}.lock")
    if os.path.exists(lock_file):
        os.remove(lock_file)
        print(f"Lock released for agent {agent_id}")
    else:
        print(f"No lock found for agent {agent_id}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Multi-Agent File Coordination helper.")
    parser.add_argument("--action", choices=["acquire", "release"], required=True)
    parser.add_argument("--agent_id", help="Required for release")
    parser.add_argument("--files", nargs="+", help="Files to lock (required for acquire)")
    
    args = parser.parse_args()
    
    if args.action == "acquire":
        if not args.files:
            print("Error: --files required for acquire action.")
        else:
            agent_id = get_agent_id()
            acquire_lock(agent_id, args.files)
            print(f"AGENT_ID={agent_id}")
    elif args.action == "release":
        if not args.agent_id:
            print("Error: --agent_id required for release action.")
        else:
            release_lock(args.agent_id)
