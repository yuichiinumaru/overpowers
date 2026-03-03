import sys

def add_icon(diagram, icon, x, y, label=None):
    print(f"Adding icon '{icon}' to '{diagram}' at ({x}, {y})")
    if label:
        print(f"Label: {label}")

if __name__ == "__main__":
    # Simplified arg parsing
    print("Usage: python add-icon-to-diagram.py <diagram> <icon> <x> <y> [--label LABEL]")
