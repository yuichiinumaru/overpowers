import argparse
import re
from collections import Counter

def get_keywords(text):
    # Basic keyword extraction (words > 3 chars)
    words = re.findall(r'\w+', text.lower())
    return [w for w in words if len(w) > 3]

def detect_cannibalization(file1, file2):
    with open(file1, 'r') as f:
        content1 = f.read()
    with open(file2, 'r') as f:
        content2 = f.read()
        
    kw1 = set(get_keywords(content1))
    kw2 = set(get_keywords(content2))
    
    overlap = kw1.intersection(kw2)
    
    print(f"Page 1 keywords: {len(kw1)}")
    print(f"Page 2 keywords: {len(kw2)}")
    print(f"Overlapping keywords: {len(overlap)}")
    
    if len(overlap) > 0:
        print("\nTop overlapping keywords:")
        for kw in list(overlap)[:10]:
            print(f"- {kw}")
            
    similarity = len(overlap) / max(len(kw1), len(kw2)) * 100
    print(f"\nKeyword Similarity: {similarity:.2f}%")
    
    if similarity > 30:
        print("WARNING: High cannibalization risk detected!")
    else:
        print("Risk is low.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Basic SEO keyword overlap detector")
    parser.add_argument("file1", help="Path to first page content")
    parser.add_argument("file2", help="Path to second page content")
    
    args = parser.parse_args()
    detect_cannibalization(args.file1, args.file2)
