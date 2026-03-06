import sys

def analyze_warning_severity(boxed_warning, contraindications):
    """Categorize warning severity."""
    severity = 'Low'
    if boxed_warning:
        severity = 'High'
    elif contraindications:
        severity = 'Medium'
    return severity

if __name__ == "__main__":
    if len(sys.argv) > 2:
        bw = sys.argv[1].lower() == 'true'
        ci = sys.argv[2].lower() == 'true'
        print(f"Warning Severity: {analyze_warning_severity(bw, ci)}")
    else:
        print("Usage: python pharmacovigilance_helper.py <has_boxed_warning> <has_contraindications>")
