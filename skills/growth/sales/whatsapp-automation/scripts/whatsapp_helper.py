import sys

def print_usage():
    print("Usage:")
    print("  python whatsapp_helper.py list_numbers")
    print("  python whatsapp_helper.py send_message <to> <body> [phone_number_id]")

if len(sys.argv) < 2:
    print_usage()
    sys.exit(1)

command = sys.argv[1]

if command == "list_numbers":
    print("Call WHATSAPP_GET_PHONE_NUMBERS via Rube MCP")
elif command == "send_message":
    if len(sys.argv) < 4:
        print("Missing 'to' or 'body'")
    else:
        to = sys.argv[2]
        body = sys.argv[3]
        phone_id = sys.argv[4] if len(sys.argv) > 4 else "None"
        print(f"Call WHATSAPP_SEND_MESSAGE with to='{to}', body='{body}', phone_number_id={phone_id}")
else:
    print_usage()
