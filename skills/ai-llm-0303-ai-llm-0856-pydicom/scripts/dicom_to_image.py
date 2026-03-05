import sys
import pydicom
import numpy as np
from PIL import Image
import argparse

def convert_to_image(input_path, output_path, format="PNG"):
    try:
        ds = pydicom.dcmread(input_path)
        
        if not hasattr(ds, 'pixel_array'):
            print("Error: DICOM file has no pixel data.")
            sys.exit(1)
            
        pixel_array = ds.pixel_array

        # Normalize to 0-255 range if not already
        if pixel_array.dtype != np.uint8:
            p_min = pixel_array.min()
            p_max = pixel_array.max()
            if p_max == p_min:
                pixel_array = np.zeros(pixel_array.shape, dtype=np.uint8)
            else:
                pixel_array = ((pixel_array - p_min) / (p_max - p_min) * 255).astype(np.uint8)

        # Save as image
        image = Image.fromarray(pixel_array)
        image.save(output_path, format=format)
        print(f"DICOM converted to {format} image: {output_path}")
        
    except Exception as e:
        print(f"Error during conversion: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description='Convert DICOM to image')
    parser.add_argument('input', help='Input DICOM file')
    parser.add_argument('output', help='Output image file')
    parser.add_argument('--format', default='PNG', help='Output format (PNG, JPEG, etc.)')
    
    args = parser.parse_args()
    convert_to_image(args.input, args.output, args.format)

if __name__ == "__main__":
    main()
