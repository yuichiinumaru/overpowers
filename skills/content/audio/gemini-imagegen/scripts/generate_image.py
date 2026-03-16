#!/usr/bin/env python3
import os
import sys
import argparse
from google import genai
from google.genai import types

def generate_image(prompt, output_file, aspect_ratio="1:1", resolution="1K", reference_images=None):
    client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY", ""))

    # Configure image settings
    image_config = types.ImageConfig(
        aspect_ratio=aspect_ratio,
        image_size=resolution
    )

    # Prepare contents list
    contents = [prompt]

    # Add any reference images
    if reference_images:
        from PIL import Image
        for ref_img_path in reference_images:
            try:
                img = Image.open(ref_img_path)
                contents.append(img)
            except Exception as e:
                print(f"Warning: Could not open reference image {ref_img_path}: {e}")

    print(f"Generating image with prompt: '{prompt}'")
    print(f"Settings: {resolution}, {aspect_ratio}")

    # Generate content
    response = client.models.generate_content(
        model="gemini-3-pro-image-preview",
        contents=contents,
        config=types.GenerateContentConfig(
            response_modalities=['TEXT', 'IMAGE'],
            image_config=image_config
        )
    )

    # Process and save response
    image_saved = False
    for part in response.parts:
        if part.text:
            print(f"API Note: {part.text}")
        elif part.inline_data:
            image = part.as_image()

            # Ensure proper extension based on Gemini's default output
            if not output_file.lower().endswith(('.jpg', '.jpeg')):
                print("Warning: Gemini returns JPEG by default. Re-saving with correct format if needed.")
                if output_file.lower().endswith('.png'):
                    image.save(output_file, format="PNG")
                else:
                    output_file += ".jpg"
                    image.save(output_file)
            else:
                image.save(output_file)

            print(f"Successfully saved image to {output_file}")
            image_saved = True

    if not image_saved:
        print("Failed to generate image. No image data in response.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate images using Gemini API")
    parser.add_argument("prompt", help="Text prompt for image generation")
    parser.add_argument("-o", "--output", default="output.jpg", help="Output file path (default: output.jpg)")
    parser.add_argument("-a", "--aspect-ratio", default="1:1", choices=["1:1", "2:3", "3:2", "3:4", "4:3", "4:5", "5:4", "9:16", "16:9", "21:9"], help="Aspect ratio (default: 1:1)")
    parser.add_argument("-r", "--resolution", default="1K", choices=["1K", "2K", "4K"], help="Image resolution (default: 1K)")
    parser.add_argument("-i", "--images", nargs="+", help="Reference images to include")

    args = parser.parse_args()

    if not os.environ.get("GEMINI_API_KEY"):
        print("Error: GEMINI_API_KEY environment variable is required")
        sys.exit(1)

    generate_image(
        prompt=args.prompt,
        output_file=args.output,
        aspect_ratio=args.aspect_ratio,
        resolution=args.resolution,
        reference_images=args.images
    )
