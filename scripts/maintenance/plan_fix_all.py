import os
import re

folders = [
    "skills/sec-safety-1114-stripe-integration",
    "skills/sec-safety-1116-swarm-advanced",
    "skills/sec-safety-1117-systematic-debugging",
    "skills/sec-safety-1118-task-coordination-strategies",
    "skills/sec-safety-1119-team-composition-patterns",
    "skills/sec-safety-1120-terraform-specialist",
    "skills/sec-safety-1121-test-driven-development",
    "skills/sec-safety-1122-threat-mitigation-mapping",
    "skills/sec-safety-1123-threat-modeling-expert",
    "skills/sec-safety-1124-threejs-shaders",
    "skills/sec-safety-1125-tooluniverse-drug-research",
    "skills/sec-safety-1126-top-web-vulnerabilities",
    "skills/sec-safety-1127-triaging-issues",
    "skills/sec-safety-1128-twitter-algorithm-optimizer",
    "skills/sec-safety-1129-uspto-database",
    "skills/sec-safety-1130-v3-core-implementation",
    "skills/sec-safety-1131-v3-ddd-architecture",
    "skills/sec-safety-1132-v3-integration-deep",
    "skills/sec-safety-1133-v3-performance-optimization",
    "skills/sec-safety-1134-v3-security-overhaul"
]

for folder in folders:
    skill_file = os.path.join(folder, "SKILL.md")
    if os.path.exists(skill_file):
        with open(skill_file, 'r') as f:
            content = f.read()
            
        scripts_dir = os.path.join(folder, "scripts")
        if not os.path.exists(scripts_dir):
            continue
            
        scripts = os.listdir(scripts_dir)
        
        # Check if the generated scripts are mentioned
        for script in scripts:
            if script not in content:
                print(f"Script {script} not in {skill_file}")
                
