import os
import argparse

TEMPLATE = """<!DOCTYPE html>
<html>
<head>
  <title>{title} Flowchart</title>
  <style>
    body {{ font-family: system-ui; }}
    svg {{ max-width: 100%; }}
    .start-end {{ fill: #48bb78; }}
    .process {{ fill: #4299e1; }}
    .decision {{ fill: #f59e0b; }}
    text {{ font-size: 14px; fill: white; }}
    .arrow-text {{ fill: #333; font-size: 12px; }}
  </style>
</head>
<body>
  <h1>{title} Flowchart</h1>
  <svg viewBox="0 0 800 600" width="800" height="600">
    <defs>
      <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
        <path d="M0,0 L0,6 L9,3 z" fill="#666" />
      </marker>
    </defs>
    
    <!-- Start -->
    <rect x="350" y="50" width="100" height="50" rx="25" class="start-end"/>
    <text x="400" y="80" text-anchor="middle">Start</text>

    <!-- Arrow -->
    <path d="M400,100 L400,150" stroke="#666" stroke-width="2" marker-end="url(#arrow)"/>

    <!-- Process -->
    <rect x="350" y="150" width="100" height="60" class="process"/>
    <text x="400" y="185" text-anchor="middle">Process</text>

    <!-- Arrow -->
    <path d="M400,210 L400,250" stroke="#666" stroke-width="2" marker-end="url(#arrow)"/>

    <!-- Decision -->
    <path d="M400,250 L450,280 L400,310 L350,280 Z" class="decision"/>
    <text x="400" y="285" text-anchor="middle">Decision?</text>
    
    <!-- Yes Arrow -->
    <path d="M450,280 L550,280" stroke="#666" stroke-width="2" marker-end="url(#arrow)"/>
    <text x="500" y="275" text-anchor="middle" class="arrow-text">Yes</text>
    
    <!-- No Arrow -->
    <path d="M400,310 L400,360" stroke="#666" stroke-width="2" marker-end="url(#arrow)"/>
    <text x="415" y="340" class="arrow-text">No</text>
    
  </svg>
</body>
</html>
"""

def generate(title):
    filename = f"{title.lower().replace(' ', '_')}_flowchart.html"
    if os.path.exists(filename):
        print(f"Error: {filename} already exists.")
        return
        
    with open(filename, 'w') as f:
        f.write(TEMPLATE.format(title=title))
        
    print(f"Generated flowchart template: {filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate an HTML flowchart template.")
    parser.add_argument("title", help="Title of the flowchart")
    args = parser.parse_args()
    generate(args.title)
