import argparse
import re
from collections import Counter

def calculate_density(file_path, keywords):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read().lower()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # Clean text: remove non-alphanumeric chars (keeping spaces)
    clean_text = re.sub(r'[^\w\s]', '', text)
    words = clean_text.split()
    total_words = len(words)
    
    print(f"Total words: {total_words}\n")
    print(f"{'Keyword':<20} | {'Count':<10} | {'Density':<10}")
    print("-" * 45)

    for kw in keywords:
        kw = kw.lower()
        # Handle multi-word keywords
        count = len(re.findall(r'\b' + re.escape(kw) + r'\b', text))
        density = (count / total_words) * 100 if total_words > 0 else 0
        print(f"{kw:<20} | {count:<10} | {density:>6.2f}%")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate keyword density in a text file.")
    parser.add_argument("file", help="Path to text file")
    parser.add_argument("--keywords", required=True, help="Comma-separated list of keywords")
    args = parser.parse_args()
    
    keywords = [k.strip() for kw in args.keywords.split(',') for k in [kw] if k]
    calculate_density(args.file, keywords)
