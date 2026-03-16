import sys

def print_usage():
    print("X Article Publisher Helper")
    print("Usage: python x_publisher_helper.py info")
    print("\nSource: https://github.com/wshuyi/x-article-publisher-skill")

if len(sys.argv) < 2:
    print_usage()
    sys.exit(0)

command = sys.argv[1]

if command == "info":
    print("Patterns for publishing articles to X/Twitter:")
    print("1. Prepare article in Markdown.")
    print("2. Ensure X/Twitter developer credentials are set.")
    print("3. Use the publisher script from the source repo.")
else:
    print_usage()
