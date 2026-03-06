#!/usr/bin/env python3
"""
Helper script to list available skills and their types.
"""
import os
import glob

def list_skills():
    skills_dir = "skills"
    if not os.path.exists(skills_dir):
        print("Skills directory not found.")
        return

    skills = glob.glob(f"{skills_dir}/*")
    print(f"Found {len(skills)} skills:")
    for skill in sorted(skills)[:10]:
        print(f" - {os.path.basename(skill)}")
    print("...")

if __name__ == "__main__":
    list_skills()
