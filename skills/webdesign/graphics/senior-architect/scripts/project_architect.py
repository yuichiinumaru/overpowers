import os
import sys

def analyze_project(path):
    print(f"--- Project Architect Analysis for {path} ---")
    
    # Simple checks
    has_env = os.path.exists(os.path.join(path, ".env.example"))
    has_gitignore = os.path.exists(os.path.join(path, ".gitignore"))
    has_package = os.path.exists(os.path.join(path, "package.json"))
    has_requirements = os.path.exists(os.path.join(path, "requirements.txt"))
    
    print(f"  .env.example: {'OK' if has_env else 'MISSING'}")
    print(f"  .gitignore: {'OK' if has_gitignore else 'MISSING'}")
    print(f"  Node.js (package.json): {'Detected' if has_package else 'No'}")
    print(f"  Python (requirements.txt): {'Detected' if has_requirements else 'No'}")
    
    print("\nArchitecture Recommendations:")
    if not has_env:
        print("  - Create an .env.example file for sensitive configurations.")
    if has_package:
        print("  - Ensure use of modern React patterns if applicable.")
    print("  - Follow the patterns in references/architecture_patterns.md")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    analyze_project(target)
