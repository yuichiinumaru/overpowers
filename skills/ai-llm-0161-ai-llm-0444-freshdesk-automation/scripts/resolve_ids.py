#!/usr/bin/env python3
import sys

def generate_resolve_sequence(email=None, company_name=None):
    print("--- Freshdesk ID Resolution Sequence ---")
    if email:
        print(f"\n1. To resolve email '{email}' to requester_id:")
        print(f"   Call tool: FRESHDESK_SEARCH_CONTACTS")
        print(f"   Arguments: {{\"query\": \"email:'{email}'\"}}")
    
    if company_name:
        print(f"\n2. To resolve company '{company_name}' to company_id:")
        print(f"   Call tool: FRESHDESK_GET_COMPANIES")
        print(f"   Action: Filter results where name == '{company_name}'")

    print("\nNote: Always call RUBE_SEARCH_TOOLS first if you haven't already.")

if __name__ == "__main__":
    email = sys.argv[1] if len(sys.argv) > 1 else None
    company = sys.argv[2] if len(sys.argv) > 2 else None
    
    if not email and not company:
        print("Usage: resolve_ids.py <email> [company_name]")
        sys.exit(1)
        
    generate_resolve_sequence(email, company)
