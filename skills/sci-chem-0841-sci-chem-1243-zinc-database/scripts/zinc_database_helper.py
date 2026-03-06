import re
import sys

def parse_zinc_tranche(tranche_str):
    """Parse ZINC tranche code to extract chemical properties.
    Format: H##P###M###-phase
    """
    match = re.match(r'H(\d+)P(\d+)M(\d+)-(\d+)', tranche_str)
    if match:
        return {
            'h_donors': int(match.group(1)),
            'logP': int(match.group(2)) / 10.0,
            'mw': int(match.group(3)),
            'phase': int(match.group(4))
        }
    return None

if __name__ == "__main__":
    if len(sys.argv) > 1:
        res = parse_zinc_tranche(sys.argv[1])
        print(f"Tranche '{sys.argv[1]}' properties: {res}")
    else:
        print("Usage: python zinc_database_helper.py <tranche_code>")
