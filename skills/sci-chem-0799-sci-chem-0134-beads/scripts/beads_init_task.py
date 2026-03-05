#!/usr/bin/env python3
import argparse
import subprocess
import sys

def run_command(command):
    try:
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error executing command {' '.join(command)}: {e.stderr}")
        return None

def start_task(title, description=None):
    # 1. Create the task
    create_cmd = ["bd", "create", title]
    if description:
        create_cmd.extend(["--description", description])
    
    print(f"Creating task: {title}...")
    task_id = run_command(create_cmd)
    
    if not task_id:
        print("Failed to create task.")
        return

    print(f"Created task with ID: {task_id}")

    # 2. Set to in_progress
    print(f"Setting task {task_id} to in_progress...")
    run_command(["bd", "update", task_id, "--status", "in_progress"])

    # 3. Show context
    print("\n--- Task Context ---")
    print(run_command(["bd", "show", task_id]))
    print("--------------------")
    
    print(f"\nTask {task_id} is now active. Remember to add notes as you work.")

def main():
    parser = argparse.ArgumentParser(description='Initialize a persistent task using Beads (bd).')
    parser.add_argument('title', help='Title of the task')
    parser.add_argument('--description', help='Description of the task')

    args = parser.parse_args()

    # Check if bd is installed
    if not run_command(["bd", "--version"]):
        print("Error: 'bd' CLI not found. Please ensure it is installed and in your PATH.")
        sys.exit(1)

    start_task(args.title, args.description)

if __name__ == "__main__":
    main()
