#!/usr/bin/env python3
import sys

def main():
    print("HubSpot Integration Best Practices Checklist:")
    print("---------------------------------------------")
    print("[ ] Using OAuth 2.0 or Private App Token for authentication.")
    print("[ ] NOT using deprecated API Keys.")
    print("[ ] Using Batch operations instead of individual CRUD requests.")
    print("[ ] Using Webhooks instead of polling for changes.")
    print("---------------------------------------------")
    print("For any 'Sharp Edges' or issues, consult the official HubSpot API documentation.")

if __name__ == "__main__":
    main()
