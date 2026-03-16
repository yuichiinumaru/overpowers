#!/usr/bin/env python3
import sys

SHORTCUTS = {
    "Forward request": "Ctrl+F / Cmd+F",
    "Drop request": "Ctrl+D / Cmd+D",
    "Send to Repeater": "Ctrl+R / Cmd+R",
    "Send to Intruder": "Ctrl+I / Cmd+I",
    "Toggle intercept": "Ctrl+T / Cmd+T"
}

PAYLOADS = {
    "SQLi": "' OR '1'='1",
    "XSS": "<script>alert(1)</script>",
    "Path Traversal": "../../../etc/passwd",
    "Command Injection": "; ls -la"
}

def main():
    print("--- Burp Suite Testing Helper ---")
    print("\nKeyboard Shortcuts:")
    for action, key in SHORTCUTS.items():
        print(f"  {action:<20} : {key}")
        
    print("\nCommon Payloads:")
    for cat, payload in PAYLOADS.items():
        print(f"  {cat:<20} : {payload}")

if __name__ == "__main__":
    main()
