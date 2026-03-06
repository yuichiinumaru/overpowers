#!/usr/bin/env python3
import sys

REQUIRED_SERVERS = [
    "AWS Billing and Cost Management MCP Server",
    "AWS Pricing MCP Server",
    "AWS Cost Explorer MCP Server",
    "Amazon CloudWatch MCP Server",
    "Amazon CloudWatch Application Signals MCP Server",
    "AWS Managed Prometheus MCP Server",
    "AWS CloudTrail MCP Server",
    "AWS Well-Architected Security Assessment Tool MCP Server"
]

def check_mcp_servers():
    print("--- AWS MCP Servers Readiness Check ---")
    print("Note: This script lists the required servers for this skill.")
    print("Ensure these are configured in your MCP client.\n")
    
    for server in REQUIRED_SERVERS:
        print(f"[ ] {server}")
    
    print("\nIf any are missing, guide the user to configure them using 'aws-mcp-setup' skill.")

if __name__ == "__main__":
    check_mcp_servers()
    sys.exit(0)
