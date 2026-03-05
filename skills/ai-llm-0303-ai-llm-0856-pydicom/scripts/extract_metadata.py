import sys
import pydicom
import argparse

def extract_metadata(input_path, output_path=None):
    try:
        ds = pydicom.dcmread(input_path)
        metadata = str(ds)
        
        if output_path:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(metadata)
            print(f"Metadata extracted to: {output_path}")
        else:
            print(metadata)
            
    except Exception as e:
        print(f"Error extracting metadata: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description='Extract DICOM metadata')
    parser.add_argument('input', help='Input DICOM file')
    parser.add_argument('--output', help='Output text file (optional)')
    
    args = parser.parse_args()
    extract_metadata(args.input, args.output)

if __name__ == "__main__":
    main()
