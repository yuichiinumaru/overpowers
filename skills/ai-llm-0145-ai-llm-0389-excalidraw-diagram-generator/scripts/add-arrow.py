import sys

def add_arrow(diagram, fx, fy, tx, ty, label=None):
    print(f"Adding arrow to '{diagram}' from ({fx}, {fy}) to ({tx}, {ty})")
    if label:
        print(f"Label: {label}")

if __name__ == "__main__":
    print("Usage: python add-arrow.py <diagram> <from-x> <from-y> <to-x> <to-y> [--label LABEL]")
