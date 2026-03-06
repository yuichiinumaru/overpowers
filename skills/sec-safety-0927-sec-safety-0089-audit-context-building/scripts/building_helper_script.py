#!/usr/bin/env python3
import sys

def build_audit_context(project_path):
    print(f"Extracting context for audit from: {project_path}")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        build_audit_context(sys.argv[1])
    else:
        print("Usage: ./audit_context.py <project_path>")
