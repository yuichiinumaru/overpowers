#!/usr/bin/env python3

def list_mappings():
    mappings = {
        "ultralearn": {
            "agents": ["researcher", "coder"],
            "fallback": "planner",
            "phases": "discovery → patterns → vectorization → summary"
        },
        "optimize": {
            "agents": ["performance-analyzer", "coder"],
            "fallback": "researcher",
            "phases": "static-analysis → performance → patterns"
        },
        "audit": {
            "agents": ["security-analyst", "tester"],
            "fallback": "reviewer",
            "phases": "security → secrets → vulnerability-scan"
        },
        "benchmark": {
            "agents": ["performance-analyzer"],
            "fallback": "coder, tester",
            "phases": "performance → metrics → report"
        }
    }
    
    print(f"{'Trigger':<15} | {'Agents':<30} | {'Phases'}")
    print("-" * 80)
    for trigger, data in mappings.items():
        agents = ", ".join(data["agents"])
        print(f"{trigger:<15} | {agents:<30} | {data['phases']}")

if __name__ == "__main__":
    list_mappings()
