#!/usr/bin/env python3
import sys
import argparse

def generate_infographic_html(title, syntax, output_path):
    template = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>{title} - Infographic</title>
  <style>
    body, html {{ margin: 0; padding: 0; width: 100%; height: 100%; overflow: hidden; }}
    #container {{ width: 100%; height: 100%; }}
    #export-btn {{
      position: absolute;
      top: 10px;
      right: 10px;
      padding: 8px 16px;
      background: #3b82f6;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      z-index: 100;
    }}
  </style>
</head>
<body>
  <button id="export-btn">Export SVG</button>
  <div id="container"></div>
  <script src="https://unpkg.com/@antv/infographic@latest/dist/infographic.min.js"></script>
  <script>
    const syntax = `{syntax}`;
    const infographic = new AntVInfographic.Infographic({{
      container: '#container',
      width: '100%',
      height: '100%',
    }});

    infographic.render(syntax);

    // Rerender when fonts are loaded
    if (document.fonts) {{
      document.fonts.ready.then(() => {{
        infographic.render(syntax);
      }}).catch((error) => console.error('Error waiting for fonts to load:', error));
    }}

    document.getElementById('export-btn').addEventListener('click', async () => {{
      try {{
        const svgDataUrl = await infographic.toDataURL({{ type: 'svg' }});
        const link = document.createElement('a');
        link.href = svgDataUrl;
        link.download = '{title.lower().replace(' ', '-')}-infographic.svg';
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
      }} catch (err) {{
        console.error('Failed to export SVG:', err);
        alert('Failed to export SVG');
      }}
    }});
  </script>
</body>
</html>
"""
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(template)
    print(f"Generated {output_path} successfully.")

def main():
    parser = argparse.ArgumentParser(description="Generate AntV Infographic HTML template")
    parser.add_argument("--title", required=True, help="Title of the infographic")
    parser.add_argument("--syntax", required=True, help="Path to file containing AntV Infographic syntax")
    parser.add_argument("--output", required=True, help="Output HTML file path")
    args = parser.parse_args()

    with open(args.syntax, 'r', encoding='utf-8') as f:
        syntax_content = f.read()

    generate_infographic_html(args.title, syntax_content, args.output)

if __name__ == "__main__":
    main()
