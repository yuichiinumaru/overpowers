#!/usr/bin/env python3
import argparse

def run_query(query):
    print(f"[Salesforce Rube MCP] Executing SOQL Query: {query}")
    print("MOCK RESULTS: [{'Id': '001ABC', 'Name': 'Acme Corp'}]")

def main():
    parser = argparse.ArgumentParser(description="Salesforce Automation Helper")
    parser.add_argument("--query", type=str, help="SOQL Query to execute")
    args = parser.parse_args()

    if args.query:
        run_query(args.query)
    else:
        print("Provide --query to run a SOQL query.")

if __name__ == "__main__":
    main()
