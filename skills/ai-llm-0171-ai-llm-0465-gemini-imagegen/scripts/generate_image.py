import os
import argparse
import sys
from google import genai
from google.genai import types

def main():
    parser = argparse.ArgumentParser(description="Generate images using Gemini API.")
    parser.add_argument("prompt", help="Text prompt for image generation")
    parser.add_argument("--output", "-o", default="output.jpg", help="Output file path (must end in .jpg)")
    parser.add_argument("--resolution", "-r", choices=["1K", "2K", "4K"], default="1K", help="Image resolution")
    parser.add_argument("--aspect-ratio", "-a", choices=["1:1", "2:3", "3:2", "3:4", "4:3", "4:5", "5:4", "9:16", "16:9", "21:9"], default="1:1", help="Aspect ratio")

    args = parser.parse_args()

    if 'GEMINI_API_KEY' not in os.environ:
        print("Error: GEMINI_API_KEY environment variable not set.", file=sys.stderr)
        sys.exit(1)

    if not args.output.lower().endswith(".jpg"):
        print("Warning: Gemini returns images in JPEG format by default. It's recommended to use .jpg extension.")

    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

    print(f"Generating image for prompt: '{args.prompt}'...")
    print(f"Resolution: {args.resolution}, Aspect Ratio: {args.aspect_ratio}")

    try:
        response = client.models.generate_content(
            model="gemini-3-pro-image-preview",
            contents=[args.prompt],
            config=types.GenerateContentConfig(
                response_modalities=['TEXT', 'IMAGE'],
                image_config=types.ImageConfig(
                    aspect_ratio=args.aspect_ratio,
                    image_size=args.resolution
                ),
            )
        )

        for part in response.parts:
            if part.text:
                print(part.text)
            elif part.inline_data:
                image = part.as_image()
                image.save(args.output)
                print(f"Image saved to {args.output}")

    except Exception as e:
        print(f"Error calling Gemini API: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
