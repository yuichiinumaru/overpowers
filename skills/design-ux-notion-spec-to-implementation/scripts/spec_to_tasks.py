#!/usr/bin/env python3
import sys

def map_spec_to_tasks(spec_content):
    print("--- Spec to Task Mapping Helper ---")
    print("\n1. Extraction Phase:")
    print("   - Scan spec for 'Requirements' or 'Acceptance Criteria'")
    print("   - Identify technical constraints (API, DB, UI)")
    
    print("\n2. Task Decomposition:")
    print("   - Break into 1-2 day chunks")
    print("   - [Task 1] Research & Discovery")
    print("   - [Task 2] Technical Design (if complex)")
    print("   - [Task 3] Scaffolding & Setup")
    print("   - [Task 4] Implementation Phase 1")
    print("   - [Task 5] Testing & Verification")
    
    print("\n3. Notion Registration:")
    print("   - Use notion-create-pages for each task")
    print("   - Map to correct task database ID")

if __name__ == "__main__":
    map_spec_to_tasks("")
