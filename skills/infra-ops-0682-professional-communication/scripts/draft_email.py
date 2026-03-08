#!/usr/bin/env python3
import sys

def main():
    print("Welcome to the Professional Communication Email Drafter")

    topic = input("Topic/Subject: ")
    recipient = input("Recipient name: ")
    purpose = input("What is the main point or request (1-2 sentences)? ")

    print("\nEnter context/background bullet points (one per line, empty line to finish):")
    context = []
    while True:
        line = input("- ")
        if not line.strip():
            break
        context.append(line)

    print("\nEnter action items needed (one per line, empty line to finish):")
    actions = []
    while True:
        line = input("- ")
        if not line.strip():
            break
        actions.append(line)

    print("\n\n" + "="*50)
    print("DRAFT EMAIL:")
    print("="*50 + "\n")

    print(f"**Subject:** {topic}: Status Update and Next Steps\n")
    print(f"Hi {recipient},\n")
    print(f"{purpose}\n")

    if context:
        print("**Context/Background:**")
        for c in context:
            print(f"- {c}")
        print()

    if actions:
        print("**What I need from you:**")
        for a in actions:
            print(f"- {a}")
        print()

    print("Best,\n[Your name]")
    print("\n" + "="*50)

if __name__ == "__main__":
    main()
