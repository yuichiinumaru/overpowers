import re

def print_around(f, line_no):
    with open(f) as file:
        lines = file.readlines()
    print(f"\n--- {f} line {line_no} ---")
    start = max(0, line_no - 5)
    end = min(len(lines), line_no + 5)
    for i in range(start, end):
        print(f"{i+1}: {lines[i].rstrip()}")

print_around('.agents/knowledge/kb_agent_orchestration_core.json', 321)
print_around('.agents/knowledge/kb_autocontinue.json', 141)
print_around('.agents/knowledge/kb_problem_solving_network.json', 171)
print_around('.agents/knowledge/kb_reasoning_knowledge_base.json', 139)
