#!/usr/bin/env python3
import json
import argparse
import sys

def create_workflow_payload(name, desc, steps, triggers):
    """Generate payload for creating a workflow."""
    # steps should be in format "id:action:agent"
    parsed_steps = []
    for step in steps:
        parts = step.split(':')
        if len(parts) != 3:
            print(f"Error: Invalid step format '{step}'. Expected 'id:action:agent'", file=sys.stderr)
            sys.exit(1)
        parsed_steps.append({
            "id": parts[0],
            "action": parts[1],
            "agent": parts[2]
        })

    payload = {
        "name": name,
        "description": desc,
        "steps": parsed_steps,
        "triggers": triggers
    }
    return json.dumps(payload, indent=2)

def execute_workflow_payload(workflow_id, input_data_str, is_async=True):
    """Generate payload for executing a workflow."""
    try:
        input_data = json.loads(input_data_str) if input_data_str else {}
    except json.JSONDecodeError:
        print("Error: Input data must be valid JSON", file=sys.stderr)
        sys.exit(1)

    payload = {
        "workflow_id": workflow_id,
        "input_data": input_data,
        "async": is_async
    }
    return json.dumps(payload, indent=2)

def assign_agent_payload(task_id, agent_type, use_similarity=True):
    """Generate payload for assigning an agent to a task."""
    payload = {
        "task_id": task_id,
        "agent_type": agent_type,
        "use_vector_similarity": use_similarity
    }
    return json.dumps(payload, indent=2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flow Nexus Workflow Payload Generator")
    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # Create workflow
    create_parser = subparsers.add_parser("create", help="Create workflow payload")
    create_parser.add_argument("--name", required=True, help="Workflow name")
    create_parser.add_argument("--desc", required=True, help="Workflow description")
    create_parser.add_argument("--steps", required=True, nargs="+", help="Steps in format 'id:action:agent'")
    create_parser.add_argument("--triggers", required=True, nargs="+", help="Trigger events")

    # Execute workflow
    exec_parser = subparsers.add_parser("execute", help="Execute workflow payload")
    exec_parser.add_argument("--id", required=True, help="Workflow ID")
    exec_parser.add_argument("--data", default="{}", help="Input data as JSON string")
    exec_parser.add_argument("--sync", action="store_true", help="Run synchronously (default is async)")

    # Assign agent
    assign_parser = subparsers.add_parser("assign", help="Assign agent payload")
    assign_parser.add_argument("--task-id", required=True, help="Task ID")
    assign_parser.add_argument("--agent-type", required=True, help="Agent type needed")
    assign_parser.add_argument("--exact", action="store_true", help="Require exact match (disable vector similarity)")

    args = parser.parse_args()

    if args.command == "create":
        print(create_workflow_payload(args.name, args.desc, args.steps, args.triggers))
    elif args.command == "execute":
        print(execute_workflow_payload(args.id, args.data, not args.sync))
    elif args.command == "assign":
        print(assign_agent_payload(args.task_id, args.agent_type, not args.exact))
    else:
        parser.print_help()
        sys.exit(1)
