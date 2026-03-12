#!/usr/bin/env python3
import json
import argparse

def generate_topology(topology_type, max_agents=5):
    """Generates a swarm initialization JSON based on topology."""
    topologies = {
        "mesh": {
            "topology": "mesh",
            "maxAgents": max_agents,
            "strategy": "adaptive",
            "description": "Peer-to-peer communication, best for research and analysis"
        },
        "hierarchical": {
            "topology": "hierarchical",
            "maxAgents": max_agents,
            "strategy": "balanced",
            "description": "Coordinator with subordinates, best for development"
        },
        "star": {
            "topology": "star",
            "maxAgents": max_agents,
            "strategy": "parallel",
            "description": "Central coordinator, best for testing"
        },
        "ring": {
            "topology": "ring",
            "maxAgents": max_agents,
            "strategy": "sequential",
            "description": "Sequential processing chain"
        }
    }
    
    return topologies.get(topology_type, {"error": "Invalid topology type"})

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Swarm initialization configuration.")
    parser.add_argument("type", choices=["mesh", "hierarchical", "star", "ring"], help="Topology type")
    parser.add_argument("--agents", type=int, default=5, help="Max agents (default: 5)")
    
    args = parser.parse_args()
    config = generate_topology(args.type, args.agents)
    print(json.dumps(config, indent=2))
