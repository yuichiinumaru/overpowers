import argparse
import sys
import os

# Add the scripts directory to path to allow direct execution
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from ingest_manager import IngestManager

def main():
    parser = argparse.ArgumentParser(description="Ingest a GitHub repository into a Markdown digest.")
    parser.add_argument("url", help="URL of the repository to ingest.")
    parser.add_argument("-o", "--output", default="digest.md", help="Output Markdown file path (default: digest.md). Use '-' for STDOUT.")
    parser.add_argument("-s", "--max-size", type=int, help="Maximum file size in bytes to include.")
    parser.add_argument("-i", "--include", action="append", help="Patterns to include (e.g., *.py).")
    parser.add_argument("-e", "--exclude", action="append", help="Patterns to exclude (e.g., node_modules/*).")
    parser.add_argument("-b", "--branch", help="Specific branch to ingest.")
    parser.add_argument("-t", "--token", help="GitHub personal access token.")

    args = parser.parse_args()

    # Priority: Flag > Environment variable
    token = args.token or os.environ.get("GITHUB_TOKEN")

    manager = IngestManager(
        url=args.url,
        output=args.output,
        max_size=args.max_size,
        include_patterns=args.include,
        exclude_patterns=args.exclude,
        branch=args.branch,
        token=token
    )

    try:
        manager.run()
        if args.output != "-":
            print(f"Successfully ingested {args.url} into {args.output}")
    except Exception as e:
        print(f"Error during ingestion: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
