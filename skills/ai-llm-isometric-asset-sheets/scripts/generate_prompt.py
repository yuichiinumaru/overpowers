import argparse

def generate_prompt(asset_type, descriptions, special_view):
    template = f"""Using the same format as reference - red background, 6 rows, 5 columns - I need you to make a new asset sheet with {asset_type.upper()} for my isometric city game. 

Each row should be ONE {asset_type.upper()}. The first 4 items should be the {asset_type.upper()} isometrically projected 4 times for flying/facing north west, north east, south east, and then south west. The last one should be {special_view}.

ALL {asset_type.upper()}S SHOULD BE HYPER REALISTIC. {descriptions}.

NO SHADOWS. Full size, 2048x2048 square."""
    
    return template

def main():
    parser = argparse.ArgumentParser(description='Generate prompt for isometric asset sheet generation')
    parser.add_argument('--type', required=True, help='Asset type (e.g., Airplane, Vehicle)')
    parser.add_argument('--rows', required=True, help='Category descriptions by row')
    parser.add_argument('--special', required=True, help='Special view description for column 5')
    
    args = parser.parse_args()
    
    prompt = generate_prompt(args.type, args.rows, args.special)
    print("\n--- GENERATED PROMPT ---\n")
    print(prompt)
    print("\n------------------------\n")

if __name__ == "__main__":
    main()
