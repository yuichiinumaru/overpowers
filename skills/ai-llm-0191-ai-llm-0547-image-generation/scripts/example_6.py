from scripts.generate import generate_image

paths = generate_image(
    prompt="A serene mountain lake under moonlight",
    output_path="./outputs/lake.png",
    aspect_ratio="16:9",
    num_images=2,
)
