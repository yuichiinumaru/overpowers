import json
import argparse
import os
from datetime import datetime

def record_experience(task, approach, success, metrics=None, context=None, output_file="experiences.jsonl"):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "task": task,
        "approach": approach,
        "outcome": {
            "success": success == "true" or success is True,
            "metrics": metrics or {}
        },
        "context": context or {}
    }
    
    with open(output_file, 'a') as f:
        f.write(json.dumps(entry) + '\n')
    
    print(f"Recorded experience for task: {task}")

def main():
    parser = argparse.ArgumentParser(description="Record task experience for ReasoningBank")
    parser.add_argument("--task", required=True, help="Task type/name")
    parser.add_argument("--approach", required=True, help="Approach/Strategy used")
    parser.add_argument("--success", required=True, choices=["true", "false"], help="Whether the task was successful")
    parser.add_argument("--metrics", help="JSON string of metrics")
    parser.add_argument("--context", help="JSON string of context")
    parser.add_argument("--file", default="experiences.jsonl", help="Output JSONL file")
    
    args = parser.parse_args()
    
    metrics = json.loads(args.metrics) if args.metrics else {}
    context = json.loads(args.context) if args.context else {}
    
    record_experience(args.task, args.approach, args.success, metrics, context, args.file)

if __name__ == "__main__":
    main()
