import sys

def print_usage():
    print("Usage:")
    print("  python zoom_helper.py create_meeting <topic> <start_time> [duration]")
    print("  python zoom_helper.py list_participants <meeting_id>")

if len(sys.argv) < 2:
    print_usage()
    sys.exit(1)

command = sys.argv[1]

if command == "create_meeting":
    if len(sys.argv) < 4:
        print("Missing topic or start_time")
    else:
        topic = sys.argv[2]
        start_time = sys.argv[3]
        duration = sys.argv[4] if len(sys.argv) > 4 else 40
        print(f"Call ZOOM_CREATE_A_MEETING with topic='{topic}', start_time='{start_time}', duration={duration}")
elif command == "list_participants":
    if len(sys.argv) < 3:
        print("Missing meeting_id")
    else:
        print(f"Call ZOOM_GET_PAST_MEETING_PARTICIPANTS with meeting_id={sys.argv[2]}")
else:
    print_usage()
