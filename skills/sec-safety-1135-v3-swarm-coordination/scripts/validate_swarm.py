#!/usr/bin/env python3
import json

def validate_swarm():
    # Dependency graph from SKILL.md
    dependencies = {
        2: [], 3: [2], 4: [2, 3],
        5: [2], 6: [5], 7: [5], 8: [5, 7], 9: [5],
        10: [5, 7, 8], 11: [5, 10], 12: [7, 10],
        13: [2, 5], 14: [5, 7, 8, 10], 15: [13, 14]
    }
    
    agents = {
        1: "Queen Coordinator", 2: "Security Architect", 3: "Security Implementer",
        4: "Security Tester", 5: "Core Architect", 6: "Core Implementer",
        7: "Memory Specialist", 8: "Swarm Specialist", 9: "MCP Specialist",
        10: "Integration Architect", 11: "CLI/Hooks Developer", 12: "Neural/Learning Dev",
        13: "TDD Test Engineer", 14: "Performance Engineer", 15: "Release Engineer"
    }

    print("--- v3 Swarm Dependency Validation ---")
    completed = set()
    phases = []
    
    while len(completed) < 15:
        ready = [agent_id for agent_id, deps in dependencies.items() if agent_id not in completed and all(d in completed for d in deps)]
        if not ready and len(completed) < 15:
            # Check for Queen Coordinator (Agent 1) which is not in the dependency map but orchestrates all
            if 1 not in completed:
                ready = [1]
            else:
                print("Error: Deadlock detected!")
                break
        
        phases.append(ready)
        for r in ready:
            completed.add(r)
            
    for i, phase in enumerate(phases):
        print(f"Phase {i+1}:")
        for agent_id in phase:
            print(f"  - Agent #{agent_id}: {agents[agent_id]}")

if __name__ == "__main__":
    validate_swarm()
