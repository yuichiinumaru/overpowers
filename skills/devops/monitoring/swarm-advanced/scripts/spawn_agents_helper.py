#!/usr/bin/env python3
import json
import argparse

def generate_agents(role_group):
    """Generates agent spawn configurations based on role group."""
    groups = {
        "research": [
            {"type": "researcher", "name": "Web Researcher", "capabilities": ["web-search", "content-extraction"]},
            {"type": "researcher", "name": "Academic Researcher", "capabilities": ["paper-analysis", "literature-review"]},
            {"type": "analyst", "name": "Data Analyst", "capabilities": ["data-processing", "visualization"]}
        ],
        "development": [
            {"type": "architect", "name": "System Architect", "role": "coordinator"},
            {"type": "coder", "name": "Backend Developer", "capabilities": ["node", "api", "database"]},
            {"type": "coder", "name": "Frontend Developer", "capabilities": ["react", "ui"]}
        ],
        "testing": [
            {"type": "tester", "name": "Unit Tester", "capabilities": ["unit-testing", "mocking"]},
            {"type": "tester", "name": "E2E Tester", "capabilities": ["e2e", "ui-testing"]},
            {"type": "monitor", "name": "Security Tester", "capabilities": ["security-testing"]}
        ]
    }
    return groups.get(role_group, [])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Agent spawn configurations.")
    parser.add_argument("group", choices=["research", "development", "testing"], help="Role group")
    
    args = parser.parse_args()
    agents = generate_agents(args.group)
    for agent in agents:
        print(json.dumps(agent))
