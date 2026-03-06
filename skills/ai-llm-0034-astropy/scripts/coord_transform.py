import argparse
import sys

try:
    from astropy.coordinates import SkyCoord
    import astropy.units as u
except ImportError:
    print("Error: astropy is not installed. Please install it using 'pip install astropy'.")
    sys.exit(1)

def transform(ra, dec, from_frame='icrs', to_frame='galactic'):
    try:
        # Support string input like '05h23m34.5s' or degree values
        if 'h' in str(ra):
            c = SkyCoord(ra=ra, dec=dec, frame=from_frame)
        else:
            c = SkyCoord(ra=float(ra)*u.degree, dec=float(dec)*u.degree, frame=from_frame)
            
        target = getattr(c, to_frame)
        return target
    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description='Astronomical Coordinate Transformer')
    parser.add_argument('--ra', required=True, help='Right Ascension')
    parser.add_argument('--dec', required=True, help='Declination')
    parser.add_argument('--from-frame', default='icrs', help='Source frame (default: icrs)')
    parser.add_argument('--to-frame', default='galactic', help='Target frame (default: galactic)')
    
    args = parser.parse_args()
    
    result = transform(args.ra, args.dec, args.from_frame, args.to_frame)
    if result:
        print(f"Result in {args.to_frame} frame:")
        print(result)

if __name__ == "__main__":
    main()
