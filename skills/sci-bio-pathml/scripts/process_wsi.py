import pathml
from pathml.core import SlideData
import argparse

def create_and_run_pipeline(image_path: str, output_path: str, tile_size: int = 256):
    """Create a basic PathML preprocessing pipeline and run it on a WSI."""
    print(f"Loading image from {image_path}...")
    try:
        slide = SlideData(image_path)
    except Exception as e:
        print(f"Error loading image: {e}")
        return False

    print(f"Creating pipeline with tile size {tile_size}...")
    pipeline = pathml.preprocessing.Pipeline([
        pathml.preprocessing.Tile(tile_size=tile_size, stride=tile_size),
        pathml.preprocessing.Filter(fn=pathml.preprocessing.filter_background)
    ])

    print("Running pipeline...")
    try:
        slide = pipeline.run(slide)
        print(f"Pipeline completed successfully. Found {len(slide.tiles)} valid tiles.")

        # Save processed data
        print(f"Saving processed data to {output_path}...")
        slide.save(output_path)
        print("Success.")
        return True
    except Exception as e:
        print(f"Error running pipeline: {e}")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process a Whole Slide Image (WSI) using PathML")
    parser.add_argument("--image", required=True, help="Path to the input WSI file")
    parser.add_argument("--out", default="processed_slide.h5", help="Path to the output HDF5 file")
    parser.add_argument("--tile_size", type=int, default=256, help="Tile size in pixels")

    args = parser.parse_args()

    create_and_run_pipeline(args.image, args.out, args.tile_size)
