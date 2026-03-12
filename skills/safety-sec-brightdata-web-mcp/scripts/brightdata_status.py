#!/usr/bin/env python3
import sys

def main():
    print("--- Bright Data Web MCP Readiness Check ---")
    print("Ensure the following is configured in your MCP settings:\n")
    print("[ ] API Token: Obtain from Bright Data dashboard")
    print("[ ] SSE Endpoint: https://mcp.brightdata.com/sse?token=YOUR_API_TOKEN")
    print("[ ] (Optional) Local instance: npx @brightdata/mcp\n")
    print("Modes:")
    print("- Rapid Mode (Free): search_engine, scrape_as_markdown")
    print("- Pro Mode: 60+ advanced tools (e-commerce, social, browser automation)")

if __name__ == "__main__":
    main()
