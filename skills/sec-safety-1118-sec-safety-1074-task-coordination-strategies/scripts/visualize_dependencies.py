#!/usr/bin/env python3
import sys
import json

def generate_mermaid(tasks):
    """
    Generates a Mermaid.js flowchart from a list of tasks.
    Expected input: [{"id": "1", "name": "Task A", "blockedBy": []}, ...]
    """
    print("graph TD")
    for task in tasks:
        task_id = task.get("id")
        task_name = task.get("name", f"Task {task_id}")
        
        # Define the node
        print(f"  {task_id}[{task_name}]")
        
        # Define relationships
        for blocker_id in task.get("blockedBy", []):
            print(f"  {blocker_id} --> {task_id}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            tasks = json.loads(sys.argv[1])
            generate_mermaid(tasks)
        except json.JSONDecodeError:
            print("Error: Input must be a valid JSON string.")
    else:
        # Example usage
        example = [
            {"id": "A", "name": "Build API", "blockedBy": []},
            {"id": "B", "name": "Build UI", "blockedBy": []},
            {"id": "C", "name": "Integration", "blockedBy": ["A", "B"]}
        ]
        print("Example Mermaid output:")
        generate_mermaid(example)
