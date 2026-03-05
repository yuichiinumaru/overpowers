import sys
import json
import re

def analyze_interview(text):
    """
    Mock implementation of interview analysis.
    In a real scenario, this would use an LLM or NLP library.
    """
    
    # Simple regex-based extraction for demonstration
    pain_points = re.findall(r"(?i)(?:pain|problem|issue|difficult|hard to)\s*(?:is|with)?\s*([^.!?\n]+)", text)
    feature_requests = re.findall(r"(?i)(?:want|need|wish|would be great to have)\s*([^.!?\n]+)", text)
    
    analysis = {
        "pain_points": [{"text": p.strip(), "severity": "medium"} for p in pain_points[:5]],
        "feature_requests": [{"text": f.strip(), "priority": "medium"} for f in feature_requests[:5]],
        "sentiment": "neutral",
        "themes": ["usability", "efficiency"] if "slow" in text.lower() or "hard" in text.lower() else ["general feedback"],
        "key_quotes": [line.strip() for line in text.split('\n') if len(line.strip()) > 20][:3]
    }
    
    return analysis

def main():
    if len(sys.argv) < 2:
        print("Usage: python customer_interview_analyzer.py <transcript_file> [output_format]")
        sys.exit(1)
        
    file_path = sys.argv[1]
    output_format = sys.argv[2] if len(sys.argv) > 2 else "text"
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        sys.exit(1)
        
    analysis = analyze_interview(content)
    
    if output_format == "json":
        print(json.dumps(analysis, indent=2))
    else:
        print("=== Customer Interview Analysis ===")
        print("\nPain Points:")
        for p in analysis["pain_points"]:
            print(f"- {p['text']} (Severity: {p['severity']})")
            
        print("\nFeature Requests:")
        for f in analysis["feature_requests"]:
            print(f"- {f['text']} (Priority: {f['priority']})")
            
        print("\nKey Themes:")
        print(", ".join(analysis["themes"]))
        
        print("\nKey Quotes:")
        for q in analysis["key_quotes"]:
            print(f"> \"{q}\"")

if __name__ == "__main__":
    main()
