import sys
import json

# This is a conceptual helper. In a real environment, it would call MCP tools.
# Since we are in a CLI, we provide a template for how the agent should call the tools.

def print_usage():
    print("Usage:")
    print("  python todoist_helper.py list_projects")
    print("  python todoist_helper.py list_sections <project_id>")
    print("  python todoist_helper.py create_task <content> [project_id]")

if len(sys.argv) < 2:
    print_usage()
    sys.exit(1)

command = sys.argv[1]

if command == "list_projects":
    print("Call TODOIST_GET_ALL_PROJECTS via Rube MCP")
elif command == "list_sections":
    if len(sys.argv) < 3:
        print("Missing project_id")
    else:
        print(f"Call TODOIST_GET_ALL_SECTIONS with project_id={sys.argv[2]}")
elif command == "create_task":
    if len(sys.argv) < 3:
        print("Missing content")
    else:
        content = sys.argv[2]
        project_id = sys.argv[3] if len(sys.argv) > 3 else None
        print(f"Call TODOIST_CREATE_TASK with content='{content}', project_id={project_id}")
else:
    print_usage()
