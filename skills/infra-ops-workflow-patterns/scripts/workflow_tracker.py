import sys
import json
import os
from datetime import datetime

STATUS_FILE = ".workflow_status.json"

def load_status():
    if os.path.exists(STATUS_FILE):
        with open(STATUS_FILE, 'r') as f:
            return json.load(f)
    return {"current_task": None, "phase": "START", "checkpoints": []}

def save_status(status):
    with open(STATUS_FILE, 'w') as f:
        json.dump(status, f, indent=2)

def log_checkpoint(phase, message):
    status = load_status()
    status["phase"] = phase
    status["checkpoints"].append({
        "timestamp": datetime.now().isoformat(),
        "phase": phase,
        "message": message
    })
    save_status(status)
    print(f"Checkpoint logged: {phase} - {message}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python workflow_tracker.py <phase> <message>")
        print("Phases: RED, GREEN, REFACTOR, DONE")
        sys.exit(1)
    log_checkpoint(sys.argv[1], sys.argv[2])
