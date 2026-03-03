import json
import argparse
import os

def generate_html(data):
    competitors_html = ""
    for name, info in data.get("competitors", {}).items():
        competitors_html += f"""
        <div class="competitor-card">
            <h2>{name}</h2>
            <p><strong>Website:</strong> <a href="{info.get('website')}">{info.get('website')}</a></p>
            <p><strong>Value Prop:</strong> {info.get('value_prop')}</p>
            <p><strong>Pricing:</strong> {info.get('pricing')}</p>
            <h3>Strengths</h3>
            <ul>{"".join([f"<li>{s}</li>" for s in info.get('strengths', [])])}</ul>
            <h3>Weaknesses</h3>
            <ul>{"".join([f"<li>{w}</li>" for w in info.get('weaknesses', [])])}</ul>
        </div>
        """

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Battlecard: {data.get('company')}</title>
        <style>
            body {{ font-family: sans-serif; background: #0a0d14; color: white; padding: 20px; }}
            .competitor-card {{ background: #161b28; padding: 20px; margin-bottom: 20px; border-radius: 8px; }}
            a {{ color: #3b82f6; }}
        </style>
    </head>
    <body>
        <h1>Competitive Battlecard for {data.get('company')}</h1>
        {competitors_html}
    </body>
    </html>
    """
    return html

def main():
    parser = argparse.ArgumentParser(description="Generate HTML Battlecard")
    parser.add_argument("--input", default="competitive_report.json", help="Input JSON report")
    parser.add_argument("--output", default="battlecard.html", help="Output HTML file")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.input):
        print(f"Error: {args.input} not found.")
        return
        
    with open(args.input, "r") as f:
        data = json.load(f)
        
    html_content = generate_html(data)
    
    with open(args.output, "w") as f:
        f.write(html_content)
        
    print(f"Battlecard generated: {args.output}")

if __name__ == "__main__":
    main()
