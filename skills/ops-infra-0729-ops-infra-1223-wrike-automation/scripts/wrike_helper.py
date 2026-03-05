import sys

def print_usage():
    print("Usage:")
    print("  python wrike_helper.py list_folders")
    print("  python wrike_helper.py list_tasks <folder_id>")
    print("  python wrike_helper.py create_task <folder_id> <title> [desc]")

if len(sys.argv) < 2:
    print_usage()
    sys.exit(1)

command = sys.argv[1]

if command == "list_folders":
    print("Call WRIKE_GET_FOLDERS via Rube MCP")
elif command == "list_tasks":
    if len(sys.argv) < 3:
        print("Missing folder_id")
    else:
        print(f"Call WRIKE_FETCH_ALL_TASKS with folderId={sys.argv[2]}")
elif command == "create_task":
    if len(sys.argv) < 4:
        print("Missing folder_id or title")
    else:
        folder_id = sys.argv[2]
        title = sys.argv[3]
        desc = sys.argv[4] if len(sys.argv) > 4 else ""
        print(f"Call WRIKE_CREATE_TASK with folderId='{folder_id}', title='{title}', description='{desc}'")
else:
    print_usage()
