import sys

def print_usage():
    print("Usage:")
    print("  python trello_helper.py list_boards")
    print("  python trello_helper.py list_lists <board_id>")
    print("  python trello_helper.py create_card <list_id> <name> [desc]")

if len(sys.argv) < 2:
    print_usage()
    sys.exit(1)

command = sys.argv[1]

if command == "list_boards":
    print("Call TRELLO_GET_MEMBERS_BOARDS_BY_ID_MEMBER with idMember='me'")
elif command == "list_lists":
    if len(sys.argv) < 3:
        print("Missing board_id")
    else:
        print(f"Call TRELLO_GET_BOARDS_LISTS_BY_ID_BOARD with idBoard={sys.argv[2]}")
elif command == "create_card":
    if len(sys.argv) < 4:
        print("Missing list_id or name")
    else:
        list_id = sys.argv[2]
        name = sys.argv[3]
        desc = sys.argv[4] if len(sys.argv) > 4 else ""
        print(f"Call TRELLO_ADD_CARDS with idList='{list_id}', name='{name}', desc='{desc}'")
else:
    print_usage()
