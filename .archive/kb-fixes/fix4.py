import json
try:
    with open('.agents/knowledge/kb_agent_orchestration_core.json') as f:
        json.load(f)
    print("kb_agent_orchestration_core.json OK")
except Exception as e:
    print("kb_agent_orchestration_core.json Error:", e)

