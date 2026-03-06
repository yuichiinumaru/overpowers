import sys
import os

HTML_TEMPLATE = """<!DOCTYPE html>
<html>
<head>
  <title>{system_name} Documentation</title>
  <style>
    body {{ font-family: system-ui; max-width: 1000px; margin: 0 auto; line-height: 1.6; color: #2d3748; padding: 20px; }}
    h1 {{ color: #2b6cb0; border-bottom: 2px solid #e2e8f0; padding-bottom: 10px; }}
    h2 {{ color: #4a5568; margin-top: 40px; }}
    pre {{ background: #1e1e1e; color: #d4d4d4; padding: 15px; border-radius: 4px; overflow-x: auto; }}
    .endpoint {{ background: #f7fafc; padding: 15px; margin: 20px 0; border-left: 4px solid #4299e1; border-radius: 0 4px 4px 0; }}
    code {{ background: #e2e8f0; padding: 2px 6px; border-radius: 3px; font-family: monospace; }}
    .method {{ font-weight: bold; padding: 2px 8px; border-radius: 3px; color: white; margin-right: 10px; }}
    .get {{ background: #48bb78; }}
    .post {{ background: #4299e1; }}
    .delete {{ background: #f56565; }}
    .put {{ background: #ed8936; }}
  </style>
</head>
<body>
  <h1>{system_name} Documentation</h1>
  
  <section id="overview">
    <h2>Overview</h2>
    <p>Provide a brief description of the system and its purpose here.</p>
  </section>

  <section id="getting-started">
    <h2>Getting Started</h2>
    <pre><code>npm install package-name</code></pre>
  </section>

  <section id="api-reference">
    <h2>API Reference</h2>
    
    <div class="endpoint">
      <h3><span class="method get">GET</span> /api/resource/{{id}}</h3>
      <p>Description of the endpoint.</p>
      <h4>Request</h4>
      <pre><code>curl -X GET https://api.example.com/resource/123</code></pre>
      <h4>Response</h4>
      <pre><code>{{
  "id": 123,
  "name": "Example"
}}</code></pre>
    </div>
  </section>

  <section id="architecture">
    <h2>Architecture</h2>
    <p>Describe system architecture or embed SVG diagrams here.</p>
  </section>
</body>
</html>
"""

def generate_docs(system_name):
    filename = f"{system_name.lower().replace(' ', '-')}-docs.html"
    content = HTML_TEMPLATE.format(system_name=system_name)
    
    with open(filename, 'w') as f:
        f.write(content)
    
    print(f"Generated {filename}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_tech_docs.py <System Name>")
        sys.exit(1)
    
    generate_docs(sys.argv[1])
