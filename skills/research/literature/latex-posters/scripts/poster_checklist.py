import os
import sys

def check_log_for_overflow(log_file):
    """Check LaTeX log file for common poster issues"""
    if not os.path.exists(log_file):
        print(f"Error: Log file {log_file} not found.")
        return
    
    issues = []
    with open(log_file, 'r', errors='ignore') as f:
        for line in f:
            if "Overfull" in line or "Underfull" in line or "Badbox" in line:
                issues.append(line.strip())
                
    if issues:
        print(f"Found {len(issues)} potential layout issues:")
        for issue in issues[:10]:
            print(f"  - {issue}")
        if len(issues) > 10:
            print(f"  ... and {len(issues) - 10} more.")
    else:
        print("No layout issues found in log file.")

def poster_checklist():
    """Print a manual checklist for poster review"""
    checklist = [
        "1. PAGE SIZE: Matches conference requirements exactly?",
        "2. OVERFLOW: sistematic edge inspection completed (Top, Bottom, Left, Right)?",
        "3. TYPOGRAPHY: Title large enough (72pt+)? Body text readable (24pt+)?",
        "4. VISUALS: Figures are high resolution? 50% white space used?",
        "5. CONTENT: Word count between 300-800? 3-5 main takeaways?",
        "6. INTERACTIVITY: QR codes tested and functional?",
        "7. TECHNICAL: Fonts embedded in PDF?"
    ]
    
    print("\n--- Research Poster Final Checklist ---")
    for item in checklist:
        print(f"[ ] {item}")

if __name__ == "__main__":
    log_name = sys.argv[1] if len(sys.argv) > 1 else "poster.log"
    check_log_for_overflow(log_name)
    poster_checklist()
