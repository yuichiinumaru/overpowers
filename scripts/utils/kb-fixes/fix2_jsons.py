import json

files = ['.agents/knowledge/kb_agent_orchestration_core.json',
         '.agents/knowledge/kb_autocontinue.json',
         '.agents/knowledge/kb_problem_solving_network.json',
         '.agents/knowledge/kb_reasoning_knowledge_base.json']

for f in files:
    with open(f, 'r') as file:
        data = file.read()
    try:
        json.loads(data)
        print(f"OK: {f}")
    except json.JSONDecodeError as e:
        print(f"Error {f}: {e}")

