#!/usr/bin/env python3
import sys
import os

def generate_explorer(ged_file, out_file):
    print(f"Parsing {ged_file}...")
    # This is a stub for the logic mentioned in SKILL.md
    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>Family Explorer</title>
    <style>
        body {{ font-family: sans-serif; padding: 20px; }}
        .card {{ border: 1px solid #ccc; padding: 10px; margin: 10px 0; }}
    </style>
</head>
<body>
    <h1>Family Tree Dashboard</h1>
    <div class="card">
        <p>Source: {ged_file}</p>
        <p>Stats: [Parsing Result Here]</p>
    </div>
</body>
</html>
"""
    with open(out_file, "w") as f:
        f.write(html_content)
    print(f"Generated dashboard: {out_file}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: gedcom_to_html.py <input.ged> [output.html]")
        sys.exit(1)
    
    input_ged = sys.argv[1]
    output_html = sys.argv[2] if len(sys.argv) > 2 else "family-explorer.html"
    generate_explorer(input_ged, output_html)
