#!/usr/bin/env python3
import sys

def main():
    print("--- Form Health & Friction Index Calculator ---\n")
    
    categories = {
        "Field Necessity": 30,
        "Value-Effort Balance": 20,
        "Cognitive Load": 20,
        "Error Handling": 15,
        "Trust/Friction": 10,
        "Mobile Usability": 5
    }
    
    total_score = 0
    for cat, weight in categories.items():
        while True:
            try:
                score = float(input(f"{cat} (0-{weight}): "))
                if 0 <= score <= weight:
                    total_score += score
                    break
                else:
                    print(f"Please enter a value between 0 and {weight}")
            except ValueError:
                print("Invalid input. Enter a number.")
                
    print(f"\nTotal Score: {total_score}/100")
    
    if total_score >= 85:
        print("Verdict: High-Performing")
    elif total_score >= 70:
        print("Verdict: Usable with Friction")
    elif total_score >= 55:
        print("Verdict: Conversion-Limited")
    else:
        print("Verdict: Broken (Redesign Required)")

if __name__ == "__main__":
    main()
