import json
import sys
import os

THEMES = {
    "Ocean Depths": {
        "colors": ["#001f3f", "#003366", "#0074D9", "#7FDBFF", "#39CCCC"],
        "fonts": {"header": "Playfair Display", "body": "Open Sans"}
    },
    "Sunset Boulevard": {
        "colors": ["#FF4136", "#FF851B", "#FFDC00", "#F012BE", "#B10DC9"],
        "fonts": {"header": "Montserrat", "body": "Lato"}
    },
    "Forest Canopy": {
        "colors": ["#2ECC40", "#3D9970", "#01FF70", "#39CCCC", "#001f3f"],
        "fonts": {"header": "Lora", "body": "Merriweather"}
    },
    "Modern Minimalist": {
        "colors": ["#111111", "#333333", "#555555", "#777777", "#AAAAAA"],
        "fonts": {"header": "Inter", "body": "Roboto"}
    }
}

def apply_theme(theme_name, target_file):
    if theme_name not in THEMES:
        print(f"Theme '{theme_name}' not found. Available: {list(THEMES.keys())}")
        return

    theme = THEMES[theme_name]
    print(f"Applying theme '{theme_name}' to {target_file}...")
    print(f"Colors: {theme['colors']}")
    print(f"Fonts: {theme['fonts']}")
    
    # In a real scenario, this would manipulate CSS or JSON artifacts.
    # For now, we'll output the theme config.
    config_file = f"{os.path.splitext(target_file)[0]}_theme.json"
    with open(config_file, 'w') as f:
        json.dump(theme, f, indent=2)
    
    print(f"Theme configuration saved to {config_file}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python apply_theme.py <Theme Name> <Target File>")
        sys.exit(1)
    
    apply_theme(sys.argv[1], sys.argv[2])
