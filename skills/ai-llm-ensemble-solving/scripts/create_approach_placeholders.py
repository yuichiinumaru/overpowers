import os

def create_placeholders():
    approaches = ["approach_1_simple.md", "approach_2_performant.md", "approach_3_extensible.md"]
    for approach in approaches:
        with open(approach, "w") as f:
            f.write(f"# {approach.replace('_', ' ').replace('.md', '').title()}\n\n")
            f.write("## Strategy\n\n## Implementation\n\n## Trade-offs\n")
        print(f"Created: {approach}")

if __name__ == "__main__":
    create_placeholders()
