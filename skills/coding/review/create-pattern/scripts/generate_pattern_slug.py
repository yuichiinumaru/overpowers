import sys
import re

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    return text.strip('-')

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_pattern_slug.py <pattern_title>")
        sys.exit(1)
        
    title = " ".join(sys.argv[1:])
    print(slugify(title))
