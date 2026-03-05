import json

class SwarmPROrchestrator:
    """Helper to generate multi-step orchestration payloads for PR management."""
    
    @staticmethod
    def get_init_payload(topology="mesh", max_agents=4):
        return {
            "topology": topology,
            "maxAgents": max_agents
        }

    @staticmethod
    def get_spawn_payload(agent_type, name):
        return {
            "type": agent_type,
            "name": name
        }

    @staticmethod
    def get_orchestrate_payload(task, strategy="parallel", priority="high"):
        return {
            "task": task,
            "strategy": strategy,
            "priority": priority
        }

if __name__ == "__main__":
    orchestrator = SwarmPROrchestrator()
    
    print("1. Swarm Init Payload:")
    print(json.dumps(orchestrator.get_init_payload(), indent=4))
    
    print("\n2. Agent Spawn Payloads:")
    print(json.dumps(orchestrator.get_spawn_payload("reviewer", "Code Quality Reviewer"), indent=4))
    print(json.dumps(orchestrator.get_spawn_payload("tester", "Testing Agent"), indent=4))
    
    print("\n3. Task Orchestration Payload:")
    print(json.dumps(orchestrator.get_orchestrate_payload("Complete PR review with testing and validation"), indent=4))
