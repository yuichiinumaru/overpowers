import argparse
import sys
import json

def get_intelligence():
    """Get the latest 10 reports from PULSE."""
    print("Fetching PULSE Intelligence...")
    mock_data = [
        {"slug": "rise-of-autonomous-agents", "title": "The Rise of Autonomous Agents"},
        {"slug": "llm-context-windows-expanding", "title": "LLM Context Windows are Expanding Rapidly"},
    ]
    print(json.dumps(mock_data, indent=2))

def read_article(slug):
    """Read the full content of a specific article."""
    print(f"Reading PULSE Article: {slug}")
    print("# " + slug.replace("-", " ").title())
    print("\nThis is the mock content for the requested article. Autonomous economy is thriving.\n")

def post_comment(slug, author, content):
    """Post a comment to a PULSE article."""
    print(f"Posting comment to '{slug}' by '{author}'...")
    print(f"Content: {content}")
    print("Status: Success. Comment posted.")

def main():
    if len(sys.argv) < 2:
        print("Usage: pulse_tool.py [intelligence|read|comment] [args]")
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "intelligence":
        get_intelligence()

    elif cmd == "read":
        parser = argparse.ArgumentParser(description="Read a PULSE article")
        parser.add_argument("cmd")
        parser.add_argument("--slug", required=True, help="Article slug")
        args = parser.parse_args()
        read_article(args.slug)

    elif cmd == "comment":
        parser = argparse.ArgumentParser(description="Post a comment to a PULSE article")
        parser.add_argument("cmd")
        parser.add_argument("--slug", required=True, help="Article slug")
        parser.add_argument("--author", required=True, help="Comment author")
        parser.add_argument("--content", required=True, help="Comment content")
        args = parser.parse_args()
        post_comment(args.slug, args.author, args.content)

    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)

if __name__ == "__main__":
    main()