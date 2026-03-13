def print_lines(f, l_num):
    lines = open(f).readlines()
    print(f"\n--- {f} ---")
    start = max(0, l_num - 5)
    end = min(len(lines), l_num + 5)
    for i in range(start, end):
        print(f"{i+1}: {lines[i].rstrip()}")

print_lines('.agents/knowledge/kb_agent_orchestration_core.json', 320)
print_lines('.agents/knowledge/kb_autocontinue.json', 140)
print_lines('.agents/knowledge/kb_problem_solving_network.json', 195)
print_lines('.agents/knowledge/kb_reasoning_knowledge_base.json', 138)
