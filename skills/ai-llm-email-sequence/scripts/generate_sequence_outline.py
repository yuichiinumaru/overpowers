import argparse

def generate_outline(type):
    outlines = {
        "welcome": [
            "Email 1: Welcome & First Step (Immediate)",
            "Email 2: Quick Win (Day 1)",
            "Email 3: Story/Why (Day 3)",
            "Email 4: Social Proof (Day 5)",
            "Email 5: Objection Handler (Day 7)",
            "Email 6: Core Feature (Day 10)",
            "Email 7: Conversion (Day 14)"
        ],
        "nurture": [
            "Email 1: Deliver & Introduce (Immediate)",
            "Email 2: Expand on Topic (Day 2)",
            "Email 3: Problem Deep-Dive (Day 4)",
            "Email 4: Solution Framework (Day 7)",
            "Email 5: Case Study (Day 10)",
            "Email 6: Differentiation (Day 13)",
            "Email 7: Direct Offer (Day 16)"
        ]
    }
    
    if type in outlines:
        print(f"Sequence Outline for: {type}")
        for email in outlines[type]:
            print(f"- {email}")
    else:
        print(f"Unknown type: {type}. Available: welcome, nurture")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("type", help="Type of sequence (welcome, nurture)")
    args = parser.parse_args()
    generate_outline(args.type)
