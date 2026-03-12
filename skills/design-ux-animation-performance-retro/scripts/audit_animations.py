#!/usr/bin/env python3
import os
import re
import argparse

def audit_file(file_path):
    bad_props = ['width', 'height', 'margin', 'padding', 'top', 'left', 'right', 'bottom']
    
    with open(file_path, 'r') as f:
        content = f.read()

    findings = []
    
    # Check for animation/transition of layout-triggering properties
    for prop in bad_props:
        # Match transition: prop or animate-[...prop...]
        if re.search(fr'transition.*{prop}', content) or re.search(fr'animate-.*{prop}', content):
            findings.append(f"Found layout-triggering property '{prop}' being animated/transitioned.")

    # Check if SVGs are wrapped in divs (simple heuristic)
    svg_blocks = re.findall(r'<svg.*?>.*?</svg>', content, re.DOTALL)
    for svg in svg_blocks:
        # This is a very simple check, might need refinement
        if not re.search(r'<div.*?>\s*<svg', content):
             # findings.append("Found SVG that might not be wrapped in a div for hardware acceleration.")
             pass

    return findings

def audit_animations(target):
    if os.path.isfile(target):
        findings = audit_file(target)
        if findings:
            print(f"Findings for {target}:")
            for f in findings:
                print(f"  - {f}")
        else:
            print(f"No issues found in {target}.")
    elif os.path.isdir(target):
        for root, _, files in os.walk(target):
            for file in files:
                if file.endswith(('.tsx', '.jsx', '.css')):
                    path = os.path.join(root, file)
                    findings = audit_file(path)
                    if findings:
                        print(f"Findings for {path}:")
                        for f in findings:
                            print(f"  - {f}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Audit animations for performance issues.")
    parser.add_argument("target", help="File or directory to audit")
    args = parser.parse_args()

    audit_animations(args.target)
