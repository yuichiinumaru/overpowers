from histolab.slide import Slide
from histolab.tiler import RandomTiler
import logging

# Enable logging for progress tracking
logging.basicConfig(level=logging.INFO)

# Load slide
slide = Slide("slide.svs", processed_path="output/random_tiles/")

# Inspect slide
print(f"Dimensions: {slide.dimensions}")
print(f"Levels: {slide.levels}")
slide.save_thumbnail()

# Configure random tiler
random_tiler = RandomTiler(
    tile_size=(512, 512),
    n_tiles=100,
    level=0,
    seed=42,
    check_tissue=True,
    tissue_percent=80.0
)

# Preview locations
random_tiler.locate_tiles(slide, n_tiles=20)

# Extract tiles
random_tiler.extract(slide)
