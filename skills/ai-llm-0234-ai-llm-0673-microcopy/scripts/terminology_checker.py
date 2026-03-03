import argparse
import os

def check_terminology(file_path):
    # Terminology from microcopy skill
    terminology = {
        "Workspace": "空间",
        "Agent": "助理",
        "Group": "群组",
        "Context": "上下文",
        "Memory": "记忆",
        "Integration": "连接器",
        "Skill": "技能",
        "Agent Profile": "助理档案",
        "Topic": "话题",
        "Page": "文稿",
        "Community": "社区",
        "Resource": "资源",
        "Library": "库",
        "Provider": "模型服务商"
    }
    
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} not found.")
        return

    with open(file_path, "r") as f:
        content = f.read()
        
    print(f"Checking {file_path} for terminology consistency...\n")
    found_issues = False
    for en, zh in terminology.items():
        if en.lower() in content.lower():
            # In a real tool, we would check if the Chinese counterpart is used correctly
            # or if the English term should be translated.
            print(f"[INFO] Found term: '{en}'. Ensure its counterpart '{zh}' is used where appropriate.")
            found_issues = True
            
    if not found_issues:
        print("No specific terminology issues found.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="LobeHub terminology consistency checker.")
    parser.add_argument("file", help="File to check")
    
    args = parser.parse_args()
    check_terminology(args.file)
