import argparse
import re
import yaml

def audit_markdown(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # Extract frontmatter
    frontmatter = {}
    fm_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if fm_match:
        try:
            frontmatter = yaml.safe_load(fm_match.group(1))
        except:
            pass
    
    body = content[fm_match.end():] if fm_match else content
    
    print(f"SEO Audit for: {file_path}\n")
    
    # Title check
    title = frontmatter.get('title', '')
    print(f"Title: '{title}'")
    print(f"- Length: {len(title)} chars (Target: 50-60)")
    if 50 <= len(title) <= 60: print("  [OK]")
    else: print("  [WARN]")
    
    # Description check
    desc = frontmatter.get('description', '')
    print(f"\nDescription: '{desc}'")
    print(f"- Length: {len(desc)} chars (Target: 150-160)")
    if 150 <= len(desc) <= 160: print("  [OK]")
    else: print("  [WARN]")
    
    # Word count
    words = body.split()
    print(f"\nWord count: {len(words)} (Target: 1500+)")
    if len(words) >= 1500: print("  [OK]")
    else: print("  [WARN]")
    
    # H1 count
    h1_count = len(re.findall(r'^#\s', content, re.MULTILINE))
    print(f"\nH1 count: {h1_count} (Target: 1)")
    if h1_count == 1: print("  [OK]")
    else: print("  [WARN]")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Audit a markdown file for SEO.")
    parser.add_argument("file", help="Path to markdown file")
    args = parser.parse_args()
    
    audit_markdown(args.file)
