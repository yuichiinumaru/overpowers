import sys

def print_usage():
    print("Usage:")
    print("  python zoho_helper.py list_modules")
    print("  python zoho_helper.py search_records <module> <criteria>")
    print("  python zoho_helper.py create_lead <last_name> <company>")

if len(sys.argv) < 2:
    print_usage()
    sys.exit(1)

command = sys.argv[1]

if command == "list_modules":
    print("Call ZOHO_LIST_MODULES via Rube MCP")
elif command == "search_records":
    if len(sys.argv) < 4:
        print("Missing module or criteria")
    else:
        print(f"Call ZOHO_SEARCH_ZOHO_RECORDS with module={sys.argv[2]}, criteria='{sys.argv[3]}'")
elif command == "create_lead":
    if len(sys.argv) < 4:
        print("Missing last_name or company")
    else:
        print(f"Call ZOHO_CREATE_ZOHO_RECORD with module='Leads', data={{'Last_Name': '{sys.argv[2]}', 'Company': '{sys.argv[3]}'}}")
else:
    print_usage()
