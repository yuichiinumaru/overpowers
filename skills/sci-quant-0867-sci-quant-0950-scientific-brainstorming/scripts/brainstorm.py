import sys

def main():
    print("=== Scientific Brainstorming Partner ===")
    print("This script guides you through a structured brainstorming session.\n")

    # Phase 1: Context
    print("--- Phase 1: Understanding the Context ---")
    research_topic = input("Q: What is the main research topic or problem you're working on?\n> ")
    excitement = input("Q: What aspect of this are you most excited about right now?\n> ")
    assumptions = input("Q: What are the 2-3 core assumptions you are making?\n> ")

    # Phase 2: Exploration
    print("\n--- Phase 2: Divergent Exploration ---")
    print("Let's push the boundaries. Think about these 'What Ifs':")
    print(f"1. Assumption Reversal: What if {assumptions.split(',')[0] if ',' in assumptions else 'the opposite'} were true?")
    print("2. Scale Shifting: How does this look at 1000x smaller or 1000x larger scale?")
    print("3. Interdisciplinary: How would a researcher in an unrelated field (e.g. Economics or Physics) approach this?")
    
    ideas = []
    print("\nEnter your ideas (one per line, empty line to finish):")
    while True:
        idea = input("> ")
        if not idea: break
        ideas.append(idea)

    # Phase 3: Evaluation
    print("\n--- Phase 3: Critical Evaluation ---")
    if not ideas:
        print("No ideas generated.")
        return

    print(f"Let's look at your {len(ideas)} ideas.")
    best_idea = input("Q: Which one of these feels most innovative yet tractable?\n> ")
    obstacle = input("Q: What is the biggest obstacle to testing this idea?\n> ")

    # Phase 4: Synthesis
    print("\n--- Phase 4: Next Steps ---")
    print("Recommended immediate actions:")
    print(f"1. Conduct a targeted literature search on: {best_idea}")
    print(f"2. Design a 'minimal viable experiment' to address the obstacle: {obstacle}")
    print("3. Identify 2 potential collaborators from different disciplines.")

    print("\n=== Session Complete ===")
    print("Keep exploring!")

if __name__ == "__main__":
    main()
