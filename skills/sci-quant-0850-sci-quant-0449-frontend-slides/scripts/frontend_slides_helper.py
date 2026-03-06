import sys
import os

def create_slide_assets_dir(output_dir):
    """
    Ensure the assets directory exists.
    """
    assets_dir = os.path.join(output_dir, 'assets')
    os.makedirs(assets_dir, exist_ok=True)
    return assets_dir

if __name__ == "__main__":
    if len(sys.argv) > 1:
        assets = create_slide_assets_dir(sys.argv[1])
        print(f"Slide assets dir: {assets}")
    else:
        print("Usage: python frontend_slides_helper.py <output_dir>")
