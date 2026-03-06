#!/usr/bin/env python3
import sys

def run_az_cli_wrapper(command):
    print(f"Executing wrapped Azure DevOps CLI command: {command}")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        run_az_cli_wrapper(" ".join(sys.argv[1:]))
    else:
        print("Usage: ./az_devops_wrapper.py <command>")
