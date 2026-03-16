import sys
import os
try:
    from histolab.slide import Slide
    from histolab.tiler import RandomTiler
except ImportError:
    print("Error: 'histolab' package not found. Install with: pip install histolab")
    sys.exit(1)

def extract_tiles(slide_path, output_path, n_tiles=100):
    print(f"Loading slide from: {slide_path}")
    if not os.path.exists(slide_path):
        print(f"Error: Slide file not found at {slide_path}")
        return

    slide = Slide(slide_path, processed_path=output_path)
    tiler = RandomTiler(
        tile_size=(512, 512),
        n_tiles=n_tiles,
        level=0,
        seed=42
    )
    print(f"Extracting {n_tiles} tiles to: {output_path}")
    tiler.extract(slide)
    print("Extraction complete.")

if __name__ == "__main__":
    if len(sys.argv) > 2:
        slide_p = sys.argv[1]
        out_p = sys.argv[2]
        n = int(sys.argv[3]) if len(sys.argv) > 3 else 100
        extract_tiles(slide_p, out_p, n)
    else:
        print("Usage: python extract-tiles.py <slide_path> <output_path> [n_tiles]")
