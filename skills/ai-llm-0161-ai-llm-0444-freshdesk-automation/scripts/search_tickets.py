#!/usr/bin/env python3
import sys

def generate_search_tool_call(query_parts):
    # Example parts: "status:2", "priority:3", "tag:'urgent'"
    query = " AND ".join(query_parts)
    print("--- Freshdesk Advanced Search Tool Call ---")
    print(f"\nTool: FRESHDESK_GET_SEARCH")
    print(f"Arguments: {{\"query\": \"{query}\"}}")
    print("\nCommon Fields: status, priority, agent_id, requester_id, created_at, updated_at, tag")
    print("Status codes: 2=Open, 3=Pending, 4=Resolved, 5=Closed")
    print("Priority codes: 1=Low, 2=Medium, 3=High, 4=Urgent")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: search_tickets.py <query_part1> [query_part2] ...")
        print("Example: search_tickets.py \"status:2\" \"priority:4\"")
        sys.exit(1)
    
    generate_search_tool_call(sys.argv[1:])
