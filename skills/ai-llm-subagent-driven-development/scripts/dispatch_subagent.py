#!/usr/bin/env python3
import sys

def generate_dispatch_command(task_id, task_text, context=""):
    print(f"--- Subagent Dispatch Command Generator ---")
    print(f"\nTask ID: {task_id}")
    print(f"Task Text: {task_text}")
    print(f"Context: {context}")
    print("\n--- Command to Execute ---")
    # This is a conceptual generator for the user/controller
    print(f"Launch subagent with: \n\"I need you to implement Task {task_id}. Here is the plan context: {context}. Specific task: {task_text}. Please follow TDD and self-review before committing.\"")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: dispatch_subagent.py <task_id> <task_text> [context]")
        sys.exit(1)
    
    task_id = sys.argv[1]
    task_text = sys.argv[2]
    context = sys.argv[3] if len(sys.argv) > 3 else ""
    generate_dispatch_command(task_id, task_text, context)
