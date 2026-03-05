import argparse

def calculate_sizing(total_market, geo_percent, segment_percentage, capture_rate):
    tam = total_market
    sam = tam * (geo_percent / 100) * (segment_percentage / 100)
    som = sam * (capture_rate / 100)
    
    return tam, sam, som

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate TAM, SAM, and SOM.")
    parser.add_argument("--total", type=float, required=True, help="Total Market Size (e.g., in billions)")
    parser.add_argument("--geo", type=float, default=100, help="Geographic percentage (0-100)")
    parser.add_argument("--segment", type=float, default=100, help="Segment percentage (0-100)")
    parser.add_argument("--capture", type=float, default=5, help="Realistic capture rate percentage (0-100)")
    
    args = parser.parse_args()
    
    tam, sam, som = calculate_sizing(args.total, args.geo, args.segment, args.capture)
    
    print(f"TAM: {tam:.2f}")
    print(f"SAM: {sam:.2f}")
    print(f"SOM: {som:.2f}")
