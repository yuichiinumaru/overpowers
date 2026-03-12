#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: run.py <command>")
        return
    command = sys.argv[1]
    print(f"Running NSFC Justification Writer: {command}")

    if command == "init":
        print("Initialized project structure.")
    elif command == "coach":
        print("Running writing coach.")
    elif command == "diagnose":
        print("Running document diagnostics.")
    elif command == "review":
        print("Running document review.")
    elif command == "diff":
        print("Generating document differences.")
    elif command == "rollback":
        print("Rolling back document version.")
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()
