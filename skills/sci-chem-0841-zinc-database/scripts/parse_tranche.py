import re
import sys

def parse_tranche(tranche_str):
    """
    Parse ZINC tranche code to extract properties.
    Format: H##P###M###-phase
    """
    match = re.match(r'H(\d+)P(\d+)M(\d+)-(\d+)', tranche_str)
    if match:
        props = {
            'h_donors': int(match.group(1)),
            'logP': int(match.group(2)) / 10.0,
            'mw': int(match.group(3)),
            'phase': int(match.group(4))
        }
        return props
    return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python parse_tranche.py <tranche_string>")
        print("Example: python parse_tranche.py H05P035M400-0")
    else:
        result = parse_tranche(sys.argv[1])
        if result:
            print(f"Tranche: {sys.argv[1]}")
            print(f"H-bond donors: {result['h_donors']}")
            print(f"LogP: {result['logP']}")
            print(f"Molecular Weight: {result['mw']} Da")
            print(f"Reactivity Phase: {result['phase']}")
        else:
            print("Error: Invalid tranche format.")
