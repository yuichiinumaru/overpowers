import sys

def filter_high_res_structures(structures, max_resolution=2.5):
    """Filter structural results by resolution limit."""
    high_res = [
        entry for entry in structures
        if entry.get("resolution") and entry["resolution"] <= max_resolution
    ]
    return high_res

if __name__ == "__main__":
    test_data = [{'pdb_id': '4INS', 'resolution': 1.5}, {'pdb_id': '1ABC', 'resolution': 3.0}]
    filtered = filter_high_res_structures(test_data)
    print(f"High res structures (<=2.5A): {filtered}")
