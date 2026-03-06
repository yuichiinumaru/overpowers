import sys
import argparse
import re
import json

# Common patterns for prompt injection
PATTERNS = [
    # Direct Instruction Patterns
    r"(?i)ignore\s+previous\s+instructions",
    r"(?i)disregard\s+all\s+previous",
    r"(?i)you\s+are\s+now\s+a",
    r"(?i)your\s+new\s+task\s+is",
    r"(?i)as\s+an\s+AI,\s+you\s+must",
    
    # Goal Manipulation
    r"(?i)actually,\s+the\s+user\s+wants",
    r"(?i)the\s+real\s+request\s+is",
    r"(?i)override:\s+do",
    
    # Data Exfiltration
    r"(?i)send\s+the\s+contents\s+of",
    r"(?i)include\s+the\s+API\s+key",
    r"(?i)append\s+all\s+file\s+contents",
    r"mailto:[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",
    
    # Obfuscation & Social Engineering
    r"(?i)URGENT:\s+You\s+must\s+do",
    r"(?i)user\s+will\s+be\s+harmed",
    r"(?i)this\s+is\s+a\s+test,\s+you\s+should",
]

def analyze_content(content):
    findings = []
    for pattern in PATTERNS:
        matches = re.finditer(pattern, content)
        for match in matches:
            findings.append({
                "pattern": pattern,
                "match": match.group(),
                "start": match.start(),
                "end": match.end()
            })
    return findings

def main():
    parser = argparse.ArgumentParser(description="Sanitize content for potential prompt injection.")
    parser.add_argument("--analyze", type=str, help="Content to analyze directly")
    parser.add_argument("--file", type=str, help="File to analyze")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")
    
    args = parser.parse_args()
    
    content = ""
    if args.analyze:
        content = args.analyze
    elif args.file:
        with open(args.file, 'r') as f:
            content = f.read()
    else:
        # Read from stdin
        content = sys.stdin.read()
        
    findings = analyze_content(content)
    
    if args.json:
        print(json.dumps({"findings": findings, "suspicious": len(findings) > 0}, indent=2))
    else:
        if findings:
            print(f"⚠️ Suspicious content detected! {len(findings)} potential injections found.")
            for f in findings:
                print(f"- Found: '{f['match']}'")
        else:
            print("✅ Content appears clean.")
            
    sys.exit(1 if len(findings) > 0 else 0)

if __name__ == "__main__":
    main()
