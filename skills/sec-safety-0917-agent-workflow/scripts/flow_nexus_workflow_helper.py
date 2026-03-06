import json

class FlowNexusWorkflowHelper:
    """Helper to generate JSON payloads for Flow Nexus workflow MCP tools."""
    
    @staticmethod
    def create_workflow_payload(name, description, steps, triggers=None):
        return {
            "name": name,
            "description": description,
            "steps": steps,
            "triggers": triggers or ["manual_trigger"]
        }

    @staticmethod
    def execute_workflow_payload(workflow_id, input_data, is_async=True):
        return {
            "workflow_id": workflow_id,
            "input_data": input_data,
            "async": is_async
        }

    @staticmethod
    def agent_assign_payload(task_id, agent_type, use_vector_similarity=True):
        return {
            "task_id": task_id,
            "agent_type": agent_type,
            "use_vector_similarity": use_vector_similarity
        }

if __name__ == "__main__":
    helper = FlowNexusWorkflowHelper()
    
    steps = [
        {"id": "lint", "action": "run_lint", "agent": "coder"},
        {"id": "test", "action": "run_tests", "agent": "tester"}
    ]
    
    print("1. Create Workflow Payload:")
    create_payload = helper.create_workflow_payload("Code Check", "Lint and test", steps)
    print(json.dumps(create_payload, indent=4))
    
    print("\n2. Execute Workflow Payload:")
    exec_payload = helper.execute_workflow_payload("wf_123", {"branch": "main"})
    print(json.dumps(exec_payload, indent=4))
