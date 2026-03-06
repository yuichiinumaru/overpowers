import matplotlib.pyplot as plt
from histolab.masks import TissueMask

# Display slide thumbnail
plt.figure(figsize=(10, 10))
plt.imshow(slide.thumbnail)
plt.title(f"Slide: {slide.name}")
plt.axis('off')
plt.show()

# Visualize tissue mask
tissue_mask = TissueMask()
slide.locate_mask(tissue_mask)

# Preview tile locations
tiler = RandomTiler(tile_size=(512, 512), n_tiles=50)
tiler.locate_tiles(slide, n_tiles=20)

# Display extracted tiles in grid
from pathlib import Path
from PIL import Image

tile_paths = list(Path("output/tiles/").glob("*.png"))[:16]
fig, axes = plt.subplots(4, 4, figsize=(12, 12))
axes = axes.ravel()

for idx, tile_path in enumerate(tile_paths):
    tile_img = Image.open(tile_path)
    axes[idx].imshow(tile_img)
    axes[idx].set_title(tile_path.stem, fontsize=8)
    axes[idx].axis('off')

plt.tight_layout()
plt.show()
