#!/usr/bin/env python3
import argparse

def main():
    parser = argparse.ArgumentParser(description="Generate a Scientific Problem Selection framework template.")
    parser.add_argument('--idea', required=True, help="Short title of the idea")

    args = parser.parse_args()

    template = f"""# Scientific Problem Selection: {args.idea}

## 1. Idea Pitch
**What exactly do you want to do?**
[Describe the core hypothesis or objective]

**How do you currently plan to do it?**
[Brief outline of methodology]

**If it works, why will it be a big deal?**
[Impact statement / Significance]

**What are the major risks?**
[Identify potential points of failure or limitations]

---

## 2. Risk Matrix Evaluation
| Risk Type | Description | Mitigation Strategy | Severity (1-5) |
|-----------|-------------|---------------------|----------------|
| Technical | [Equipment/Methods] | [Alternative methods] | [1-5] |
| Conceptual| [Hypothesis validity]| [Preliminary data]  | [1-5] |
| Personnel | [Expertise gaps]   | [Collaborations]    | [1-5] |

## 3. Decision Tree Navigation
(Based on Fischbach & Walsh, 2024)
- **Node 1: Is the problem tractable?**
  [Yes/No/Uncertain - Explain why]
- **Node 2: Is the problem novel or derivative?**
  [Explain the degree of novelty]
- **Node 3: Are resources available to solve it?**
  [List required vs available resources]

## 4. Conclusion & Next Steps
[Summarize whether to proceed, pivot, or abandon the idea]
"""
    print(template)

if __name__ == '__main__':
    main()
