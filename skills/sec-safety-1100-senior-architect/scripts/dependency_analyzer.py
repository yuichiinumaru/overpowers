import os
import sys
import json

def analyze_dependencies(path):
    print(f"--- Dependency Analyzer for {path} ---")
    
    package_json_path = os.path.join(path, "package.json")
    if os.path.exists(package_json_path):
        print("Analyzing package.json...")
        with open(package_json_path, 'r') as f:
            data = json.load(f)
            deps = data.get("dependencies", {})
            dev_deps = data.get("devDependencies", {})
            print(f"  Found {len(deps)} dependencies and {len(dev_deps)} devDependencies.")
            
            # Look for specific high-risk or architectural dependencies
            keywords = ["express", "fastapi", "react", "next", "prisma", "sequelize"]
            for d in deps:
                if any(k in d.lower() for k in keywords):
                    print(f"  - Major architectural dependency: {d}")

    requirements_path = os.path.join(path, "requirements.txt")
    if os.path.exists(requirements_path):
        print("Analyzing requirements.txt...")
        with open(requirements_path, 'r') as f:
            lines = f.readlines()
            print(f"  Found {len(lines)} Python requirements.")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    analyze_dependencies(target)
