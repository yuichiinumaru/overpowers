import re
from collections import defaultdict
import os

report_path = ".agents/thoughts/merged_skills_report_20260313_174344.md"
with open(report_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

groups = []
current_group = []

for line in lines:
    if line.startswith("## Grupo Consolidado:"):
        if current_group:
            groups.append(current_group)
        current_group = []
    
    m = re.search(r'`([^`]+)`', line)
    if m and ("Skill Principal:" in line or "Skill Mesclada & Removida:" in line):
        current_group.append(m.group(1))

if current_group:
    groups.append(current_group)

def get_words(name):
    # split by hyphen and remove common prefixes
    words = name.replace("ai-llm-", "").replace("frontend-web-", "").replace("infra-ops-", "").replace("safety-sec-", "").replace("design-ux-", "").replace("sci-bio-", "").replace("sci-quant-", "").replace("sci-chem-", "")
    return set(re.split(r'[-_]', words))

true_duplicates = []

for g in groups:
    # check if any two names in the group share words
    for i in range(len(g)):
        for j in range(i+1, len(g)):
            w1 = get_words(g[i])
            w2 = get_words(g[j])
            # remove common short words
            w1 = {w for w in w1 if len(w) > 3}
            w2 = {w for w in w2 if len(w) > 3}
            if w1.intersection(w2):
                true_duplicates.append((g[i], g[j]))

print(f"Encontrei {len(true_duplicates)} pares que parecem ser reais duplicatas baseadas no nome:")
for p in true_duplicates:
    print(f"- {p[0]} <---> {p[1]}")
    # ler os arquivos
    path1 = None
    path2 = None
    for root, dirs, files in os.walk("skills"):
        if os.path.basename(root) == p[0]:
            path1 = os.path.join(root, "SKILL.md")
        if os.path.basename(root) == p[1]:
            path2 = os.path.join(root, "SKILL.md")
    
    if path1 and os.path.exists(path1):
        print(f"  [{p[0]}] length: {os.path.getsize(path1)}")
    if path2 and os.path.exists(path2):
        print(f"  [{p[1]}] length: {os.path.getsize(path2)}")
    print()
