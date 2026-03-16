import sys
import argparse
import re

def analyze_seo(text, keyword):
    keyword = keyword.lower()
    text_lower = text.lower()
    
    # Word count
    words = text_lower.split()
    word_count = len(words)
    
    # Keyword count and density
    keyword_count = len(re.findall(re.escape(keyword), text_lower))
    density = (keyword_count / word_count * 100) if word_count > 0 else 0
    
    # Structure checks
    has_h1 = bool(re.search(r'^# ', text, re.MULTILINE))
    has_h2 = bool(re.search(r'^## ', text, re.MULTILINE))
    
    # Keyword in headings
    kw_in_h1 = bool(re.search(r'^# .*' + re.escape(keyword), text, re.IGNORECASE | re.MULTILINE))
    
    results = {
        "word_count": word_count,
        "keyword_count": keyword_count,
        "density": f"{density:.2f}%",
        "has_h1": has_h1,
        "has_h2": has_h2,
        "kw_in_h1": kw_in_h1,
        "score": 0
    }
    
    # Basic score calculation
    score = 0
    if word_count > 1000: score += 20
    if 0.5 <= density <= 3: score += 30
    if has_h1: score += 10
    if has_h2: score += 10
    if kw_in_h1: score += 30
    
    results["score"] = score
    return results

def main():
    parser = argparse.ArgumentParser(description="SEO Optimizer")
    parser.add_argument("file", help="Path to markdown file")
    parser.add_argument("keyword", help="Primary keyword")
    
    args = parser.parse_args()
    
    try:
        with open(args.file, 'r') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    analysis = analyze_seo(content, args.keyword)
    print(f"--- SEO Analysis for '{args.keyword}' ---")
    for k, v in analysis.items():
        print(f"{k.replace('_', ' ').capitalize()}: {v}")

if __name__ == "__main__":
    main()
