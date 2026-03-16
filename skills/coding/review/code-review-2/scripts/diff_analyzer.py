import sys
import re

def analyze_diff(diff_content):
    findings = []
    
    # Simple regex patterns for common secrets/issues
    patterns = {
        "Hardcoded Password": r"password\s*=\s*['\"][^'\"]+['\"]",
        "AWS Key": r"AKIA[0-9A-Z]{16}",
        "Generic Secret": r"(secret|token|api_key)\s*=\s*['\"][^'\"]+['\"]"
    }
    
    for i, line in enumerate(diff_content.split('\n')):
        # Only check added lines
        if line.startswith('+') and not line.startswith('+++'):
            for issue, pattern in patterns.items():
                if re.search(pattern, line, re.IGNORECASE):
                    findings.append(f"Line {i+1}: Potential {issue} found in added code.")
                    
    return findings

if __name__ == "__main__":
    diff_content = sys.stdin.read()
    results = analyze_diff(diff_content)
    
    if results:
        print("🚨 Potential issues found in diff:")
        for r in results:
            print(f"- {r}")
    else:
        print("✅ No basic issues found in diff.")
