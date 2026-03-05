import os
import sys
import argparse
import requests
from requests.auth import HTTPBasicAuth
import json

def get_auth():
    email = os.environ.get('JIRA_EMAIL')
    token = os.environ.get('JIRA_API_TOKEN')
    if not email or not token:
        print("Error: JIRA_EMAIL and JIRA_API_TOKEN environment variables must be set.")
        sys.exit(1)
    return HTTPBasicAuth(email, token)

def get_base_url():
    url = os.environ.get('JIRA_BASE_URL')
    if not url:
        print("Error: JIRA_BASE_URL environment variable must be set.")
        sys.exit(1)
    return url.rstrip('/')

def create_issue(args):
    url = f"{get_base_url()}/rest/api/3/issue"
    payload = {
        "fields": {
            "project": {"key": args.project},
            "summary": args.summary,
            "description": {
                "type": "doc",
                "version": 1,
                "content": [{
                    "type": "paragraph",
                    "content": [{"type": "text", "text": args.description or args.summary}]
                }]
            },
            "issuetype": {"name": args.type}
        }
    }
    
    response = requests.post(url, json=payload, auth=get_auth())
    if response.status_code == 201:
        print(f"✅ Issue created: {response.json()['key']}")
    else:
        print(f"❌ Failed to create issue: {response.status_code}")
        print(response.text)

def search_issues(args):
    url = f"{get_base_url()}/rest/api/3/search"
    params = {"jql": args.jql, "maxResults": args.limit}
    response = requests.get(url, params=params, auth=get_auth())
    if response.status_code == 200:
        issues = response.json().get('issues', [])
        print(f"Found {len(issues)} issues:")
        for issue in issues:
            print(f"[{issue['key']}] {issue['fields']['summary']} ({issue['fields']['status']['name']})")
    else:
        print(f"❌ Search failed: {response.status_code}")
        print(response.text)

def main():
    parser = argparse.ArgumentParser(description="Jira Issue Management Tool")
    subparsers = parser.add_subparsers(dest="command")

    # Create command
    create_parser = subparsers.add_parser("create", help="Create a Jira issue")
    create_parser.add_argument("--project", required=True, help="Project key")
    create_parser.add_argument("--summary", required=True, help="Issue summary")
    create_parser.add_argument("--description", help="Issue description")
    create_parser.add_argument("--type", default="Task", help="Issue type (Bug, Task, etc.)")

    # Search command
    search_parser = subparsers.add_parser("search", help="Search Jira issues using JQL")
    search_parser.add_argument("--jql", required=True, help="JQL query")
    search_parser.add_argument("--limit", type=int, default=10, help="Max results")

    args = parser.parse_args()

    if args.command == "create":
        create_issue(args)
    elif args.command == "search":
        search_issues(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
