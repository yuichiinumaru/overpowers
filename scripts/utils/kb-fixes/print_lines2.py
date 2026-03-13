def print_lines(f, s, e):
    lines = open(f).readlines()
    print(f"\n--- {f} ---")
    for i in range(max(0, s), min(len(lines), e)):
        print(f"{i+1}: {lines[i].rstrip()}")

print_lines('.agents/knowledge/kb_agent_orchestration_core.json', 300, 321)
print_lines('.agents/knowledge/kb_problem_solving_network.json', 160, 180)
print_lines('.agents/knowledge/kb_autocontinue.json', 135, 142)
