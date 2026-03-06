#!/usr/bin/env python3
"""
Product Audit Checklist Generator
"""
def generate():
    print("=== PRODUCT AUDIT CHECKLIST ===")
    print("Product Name/Family: [ENTER NAME]")
    print("Lot/Batch Number: [ENTER LOT]")
    print("\n1. Product Specifications")
    print("  [ ] Does the product meet documented specifications?")
    print("  [ ] Are critical dimensions/attributes within tolerance?")
    print("\n2. Packaging and Labeling")
    print("  [ ] Is labeling correct and legible?")
    print("  [ ] Does packaging meet integrity requirements?")
    print("\n3. Traceability")
    print("  [ ] Is complete traceability maintained to raw materials?")
    print("\n4. Final Release")
    print("  [ ] Has final inspection/testing been completed and documented?")
    print("  [ ] Was release authorized by designated personnel?")

if __name__ == "__main__":
    generate()
