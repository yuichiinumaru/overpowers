import argparse
import os
import matplotlib.pyplot as plt
from mp_api.client import MPRester
from pymatgen.analysis.phase_diagram import PhaseDiagram, PDPlotter
from pymatgen.core import Composition

def main():
    parser = argparse.ArgumentParser(description='Generate phase diagrams from Materials Project data.')
    parser.add_argument('chemsys', help='Chemical system (e.g. Li-Fe-O)')
    parser.add_argument('--output', help='Output image path')
    parser.add_argument('--analyze', help='Analyze stability of specific composition (e.g. LiFeO2)')
    parser.add_argument('--show', action='store_true', help='Show plot')
    parser.add_argument('--api-key', help='Materials Project API Key (overrides MP_API_KEY env var)')

    args = parser.parse_args()

    api_key = args.api_key or os.environ.get("MP_API_KEY")
    if not api_key:
        print("Error: Materials Project API key not found. Set MP_API_KEY or use --api-key.")
        return

    print(f"Fetching data for system {args.chemsys} from Materials Project...")
    try:
        with MPRester(api_key) as mpr:
            entries = mpr.get_entries_in_chemsys(args.chemsys.split('-'))
            
        pd = PhaseDiagram(entries)
        plotter = PDPlotter(pd)

        if args.analyze:
            comp = Composition(args.analyze)
            e_above_hull = pd.get_e_above_hull(Composition(args.analyze))
            print(f"Analysis for {args.analyze}:")
            print(f"  Energy above hull: {e_above_hull:.4f} eV/atom")
            if e_above_hull > 0.001:
                decomp = pd.get_decomposition(comp)
                print(f"  Decomposes to: {decomp}")
            else:
                print("  Stable on the convex hull.")

        if args.output:
            plotter.get_plot().savefig(args.output)
            print(f"Phase diagram saved to {args.output}")
            
        if args.show:
            plotter.show()

    except Exception as e:
        print(f"Error generating phase diagram: {e}")

if __name__ == "__main__":
    main()
