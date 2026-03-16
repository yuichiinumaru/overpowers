import argparse
import sys
from PIL import Image, ImageChops, ImageEnhance

def compare_images(img1_path, img2_path, diff_out_path):
    try:
        img1 = Image.open(img1_path).convert('RGB')
        img2 = Image.open(img2_path).convert('RGB')
    except Exception as e:
        print(f"Error loading images: {e}")
        sys.exit(1)

    if img1.size != img2.size:
        print(f"Images are different sizes: {img1.size} vs {img2.size}")
        # Resize img2 to match img1 for comparison purposes, or handle appropriately
        img2 = img2.resize(img1.size)

    # Calculate difference
    diff = ImageChops.difference(img1, img2)
    
    # Check if images are completely identical
    if not diff.getbbox():
        print("Images are identical.")
        return True

    # Enhance difference to make it more visible
    enhancer = ImageEnhance.Brightness(diff)
    diff_enhanced = enhancer.enhance(5.0)

    # Save the difference image
    try:
        diff_enhanced.save(diff_out_path)
        print(f"Images are different. Difference saved to {diff_out_path}")
    except Exception as e:
        print(f"Error saving difference image: {e}")
        sys.exit(1)

    return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Visually compare two images and generate a diff image.")
    parser.add_argument("image1", help="Path to the first image (baseline)")
    parser.add_argument("image2", help="Path to the second image (current)")
    parser.add_argument("--out", default="diff.png", help="Path to save the diff image (default: diff.png)")
    
    args = parser.parse_args()
    
    identical = compare_images(args.image1, args.image2, args.out)
    if not identical:
        sys.exit(1)
    sys.exit(0)
