#!/usr/bin/env python3
import sys

REQUIRED_SERVERS = [
    "AWS Serverless MCP Server",
    "AWS Lambda Tool MCP Server",
    "AWS Step Functions MCP Server",
    "Amazon SNS/SQS MCP Server"
]

def check_mcp_servers():
    print("--- AWS Serverless MCP Servers Readiness Check ---")
    print("Note: This script lists the required servers for this skill.")
    print("Ensure these are configured in your MCP client.\n")
    
    for server in REQUIRED_SERVERS:
        print(f"[ ] {server}")
    
    print("\nIf any are missing, guide the user to configure them using 'aws-mcp-setup' skill.")

if __name__ == "__main__":
    check_mcp_servers()
    sys.exit(0)
