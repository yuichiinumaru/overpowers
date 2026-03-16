import argparse
import json
from pymatgen.core import Structure
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
from pymatgen.analysis.local_env import CrystalNN

def analyze_structure(file_path, symmetry=False, neighbors=False):
    struct = Structure.from_file(file_path)
    results = {
        "formula": struct.composition.reduced_formula,
        "density": struct.density,
        "num_sites": len(struct),
        "lattice": struct.lattice.as_dict()
    }

    if symmetry:
        sga = SpacegroupAnalyzer(struct)
        results["symmetry"] = {
            "symbol": sga.get_space_group_symbol(),
            "number": sga.get_space_group_number(),
            "crystal_system": sga.get_crystal_system()
        }

    if neighbors:
        cnn = CrystalNN()
        all_neighbors = []
        for i in range(len(struct)):
            site_neighbors = cnn.get_nn_info(struct, i)
            all_neighbors.append({
                "site": i,
                "element": struct[i].species_string,
                "coordination_number": len(site_neighbors),
                "neighbors": [{"index": n['site_index'], "element": struct[n['site_index']].species_string, "distance": n['weight']} for n in site_neighbors]
            })
        results["coordination"] = all_neighbors

    return results

def main():
    parser = argparse.ArgumentParser(description='Comprehensive structure analysis using pymatgen.')
    parser.add_argument('input', help='Input structure file')
    parser.add_argument('--symmetry', action='store_true', help='Perform symmetry analysis')
    parser.add_argument('--neighbors', action='store_true', help='Analyze coordination environments')
    parser.add_argument('--export', choices=['json', 'text'], default='text', help='Export format')

    args = parser.parse_args()

    try:
        results = analyze_structure(args.input, args.symmetry, args.neighbors)
        if args.export == 'json':
            print(json.dumps(results, indent=2))
        else:
            print(f"--- Analysis for {args.input} ---")
            print(f"Formula: {results['formula']}")
            print(f"Density: {results['density']:.2f} g/cm³")
            print(f"Sites: {results['num_sites']}")
            if 'symmetry' in results:
                sym = results['symmetry']
                print(f"Space Group: {sym['symbol']} ({sym['number']})")
                print(f"Crystal System: {sym['crystal_system']}")
            if 'coordination' in results:
                print("\nCoordination Environments:")
                for site in results['coordination']:
                    print(f"  Site {site['site']}({site['element']}): CN={site['coordination_number']}")
    except Exception as e:
        print(f"Error analyzing structure: {e}")

if __name__ == "__main__":
    main()
