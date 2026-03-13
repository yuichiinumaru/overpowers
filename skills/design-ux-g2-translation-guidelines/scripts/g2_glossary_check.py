#!/usr/bin/env python3
import sys
import os

GLOSSARY = {
    "图表": "Chart",
    "标记": "Mark",
    "数据": "Data",
    "比例尺": "Scale",
    "转换": "Transform",
    "坐标系": "Coordinate",
    "动画": "Animate",
    "交互": "Interaction"
}

def check_file(file_path):
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return

    with open(file_path, "r") as f:
        content = f.read()

    print(f"--- Checking Glossary in: {file_path} ---")
    found_any = False
    for zh, en in GLOSSARY.items():
        if zh in content:
            print(f"[!] Found untranslated term: '{zh}' should be '{en}'")
            found_any = True
    
    if not found_any:
        print("[OK] No untranslated glossary terms found.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: g2_glossary_check.py <file.md>")
        sys.exit(1)
    
    check_file(sys.argv[1])
