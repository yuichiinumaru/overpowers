import sys
import argparse

def analyze_voice(text):
    # Heuristics for voice analysis
    analysis = {
        "formality": "Neutral",
        "tone": "Informative",
        "perspective": "Third-person",
        "readability": "Standard"
    }
    
    # Very basic check for pronouns
    text_lower = text.lower()
    if "i " in text_lower or "my " in text_lower:
        analysis["perspective"] = "First-person"
    elif "you " in text_lower or "your " in text_lower:
        analysis["perspective"] = "Second-person"
        
    # Check for sentence length
    sentences = text.split('.')
    avg_len = sum(len(s.split()) for s in sentences) / len(sentences) if sentences else 0
    if avg_len > 25:
        analysis["readability"] = "Academic/Complex"
    elif avg_len < 15:
        analysis["readability"] = "Accessible/Punchy"
        
    return analysis

def main():
    parser = argparse.ArgumentParser(description="Brand Voice Analyzer")
    parser.add_argument("file", help="Path to text file")
    
    args = parser.parse_args()
    
    try:
        with open(args.file, 'r') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    profile = analyze_voice(content)
    print("--- Brand Voice Profile ---")
    for k, v in profile.items():
        print(f"{k.capitalize()}: {v}")

if __name__ == "__main__":
    main()
