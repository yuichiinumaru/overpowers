import sys
import os

HTML_TEMPLATE = """<!DOCTYPE html>
<html>
<head>
  <title>{project_name} Timeline</title>
  <style>
    body {{ font-family: system-ui; max-width: 1200px; margin: 0 auto; padding: 40px; color: #2d3748; }}
    h1 {{ border-bottom: 2px solid #e2e8f0; padding-bottom: 10px; }}
    .timeline-container {{ margin-top: 40px; }}
    .phase {{ margin-bottom: 30px; }}
    .phase-title {{ font-weight: bold; font-size: 1.2rem; margin-bottom: 10px; }}
    .timeline-item {{ display: flex; align-items: center; margin-bottom: 8px; gap: 15px; }}
    .item-label {{ width: 200px; font-size: 0.9rem; }}
    .bar-container {{ flex-grow: 1; background: #edf2f7; height: 24px; border-radius: 12px; overflow: hidden; }}
    .timeline-bar {{ height: 100%; border-radius: 12px; }}
    .done {{ background: #48bb78; }}
    .in-progress {{ background: #4299e1; }}
    .planned {{ background: #cbd5e0; }}
    .milestones {{ margin-top: 50px; border-top: 2px dashed #e2e8f0; padding-top: 20px; }}
    .milestone {{ border-left: 4px solid #e53e3e; padding: 5px 15px; margin-bottom: 10px; background: #fff5f5; }}
  </style>
</head>
<body>
  <h1>{project_name} Roadmap</h1>
  
  <div class="timeline-container">
    <div class="phase">
      <div class="phase-title">Phase 1: Foundation</div>
      <div class="timeline-item">
        <span class="item-label">Requirement Analysis</span>
        <div class="bar-container"><div class="timeline-bar done" style="width: 100%;"></div></div>
      </div>
      <div class="timeline-item">
        <span class="item-label">Design System</span>
        <div class="bar-container"><div class="timeline-bar in-progress" style="width: 60%;"></div></div>
      </div>
    </div>

    <div class="phase">
      <div class="phase-title">Phase 2: Implementation</div>
      <div class="timeline-item">
        <span class="item-label">Core Features</span>
        <div class="bar-container"><div class="timeline-bar planned" style="width: 0%;"></div></div>
      </div>
    </div>
  </div>

  <div class="milestones">
    <h2>Milestones</h2>
    <div class="milestone"><strong>Beta Launch</strong> - 2026-06-01</div>
    <div class="milestone"><strong>v1.0 Production</strong> - 2026-09-15</div>
  </div>
</body>
</html>
"""

def generate_timeline(project_name):
    filename = f"{project_name.lower().replace(' ', '-')}-timeline.html"
    content = HTML_TEMPLATE.format(project_name=project_name)
    
    with open(filename, 'w') as f:
        f.write(content)
    
    print(f"Generated {filename}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_timeline.py <Project Name>")
        sys.exit(1)
    
    generate_timeline(sys.argv[1])
