#!/usr/bin/env python3
"""
Verification Before Completion Script.
Enforces the 'evidence before claims' rule by requiring output validation.
"""
import sys
import subprocess
import argparse

def run_verification_command(command):
    print(f"Running verification command: {command}")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        print("--- Output ---")
        print(result.stdout)
        if result.stderr:
            print("--- Error Output ---")
            print(result.stderr)

        if result.returncode == 0:
            print(f"\n✅ Verification passed (exit code {result.returncode})")
            return True
        else:
            print(f"\n❌ Verification failed (exit code {result.returncode})")
            return False
    except Exception as e:
        print(f"Failed to execute command: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Run a verification command before claiming completion")
    parser.add_argument("command", help="The bash command to run for verification")

    args = parser.parse_args()
    success = run_verification_command(args.command)
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()
