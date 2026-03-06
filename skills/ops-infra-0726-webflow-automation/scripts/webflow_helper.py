import sys

def print_usage():
    print("Usage:")
    print("  python webflow_helper.py list_sites")
    print("  python webflow_helper.py list_collections <site_id>")
    print("  python webflow_helper.py list_items <collection_id>")

if len(sys.argv) < 2:
    print_usage()
    sys.exit(1)

command = sys.argv[1]

if command == "list_sites":
    print("Call WEBFLOW_LIST_WEBFLOW_SITES via Rube MCP")
elif command == "list_collections":
    if len(sys.argv) < 3:
        print("Missing site_id")
    else:
        print(f"Call WEBFLOW_LIST_COLLECTIONS with site_id={sys.argv[2]}")
elif command == "list_items":
    if len(sys.argv) < 3:
        print("Missing collection_id")
    else:
        print(f"Call WEBFLOW_LIST_COLLECTION_ITEMS with collection_id={sys.argv[2]}")
else:
    print_usage()
