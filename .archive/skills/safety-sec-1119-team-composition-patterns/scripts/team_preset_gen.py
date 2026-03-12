#!/usr/bin/env python3
import json
import argparse

def generate_team(preset):
    """Generates a team configuration JSON based on preset."""
    presets = {
        "review": {
            "name": "Review Team",
            "size": 3,
            "agents": [
                {"role": "Security Reviewer", "type": "agent-teams:team-reviewer"},
                {"role": "Performance Reviewer", "type": "agent-teams:team-reviewer"},
                {"role": "Architecture Reviewer", "type": "agent-teams:team-reviewer"}
            ]
        },
        "debug": {
            "name": "Debug Team",
            "size": 3,
            "agents": [
                {"role": "Hypothesis 1 Investigator", "type": "agent-teams:team-debugger"},
                {"role": "Hypothesis 2 Investigator", "type": "agent-teams:team-debugger"},
                {"role": "Hypothesis 3 Investigator", "type": "agent-teams:team-debugger"}
            ]
        },
        "feature": {
            "name": "Feature Team",
            "size": 3,
            "agents": [
                {"role": "Team Lead", "type": "agent-teams:team-lead"},
                {"role": "Implementer 1", "type": "agent-teams:team-implementer"},
                {"role": "Implementer 2", "type": "agent-teams:team-implementer"}
            ]
        },
        "fullstack": {
            "name": "Fullstack Team",
            "size": 4,
            "agents": [
                {"role": "Team Lead", "type": "agent-teams:team-lead"},
                {"role": "Frontend Developer", "type": "agent-teams:team-implementer"},
                {"role": "Backend Developer", "type": "agent-teams:team-implementer"},
                {"role": "Test Engineer", "type": "agent-teams:team-implementer"}
            ]
        }
    }
    
    return presets.get(preset, {"error": "Invalid preset"})

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Team Composition configuration.")
    parser.add_argument("preset", choices=["review", "debug", "feature", "fullstack"], help="Team preset")
    
    args = parser.parse_args()
    config = generate_team(args.preset)
    print(json.dumps(config, indent=2))
