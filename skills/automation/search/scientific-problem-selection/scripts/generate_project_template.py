#!/usr/bin/env python3
"""
Helper script to generate a structured project planning document
based on the Scientific Problem Selection framework.
"""
import argparse
import datetime

def generate_template(project_name, author):
    date = datetime.date.today().isoformat()
    return f"""# Scientific Problem Selection: Project Plan
**Project Name:** {project_name}
**Author:** {author}
**Date:** {date}

## Phase 1: Problem Definition & Ideation (Skill 1)
### The Core Idea (1-2 sentences)
[Insert short description here]

### The "Why Now?"
[Why is this problem solvable now when it wasn't before?]

## Phase 2: Risk Assessment (Skill 2)
### Key Assumptions
1. [Assumption 1]
2. [Assumption 2]

### Fatal Flaw Analysis
[What is the most likely reason this project will fail?]

## Phase 3: Optimization & Impact (Skill 3)
### Success Metrics
[How will we know if this works? What does success look like?]

### Broader Impact
[If successful, how does this change the field?]

## Phase 4: Parameter Strategy (Skill 4)
### Fixed Parameters (Constraints)
- [Constraint 1]

### Floating Parameters (Flexibility)
- [Variable 1]
- [Variable 2]

## Phase 5: Decision Tree & Adversity Planning (Skills 5 & 6)
### Key Milestones & Go/No-Go Points
1. Milestone 1: [Description] -> Expected Date: [Date]
2. Milestone 2: [Description] -> Expected Date: [Date]

### Contingency Plans
- **If X fails:** [We will do Y]
- **If Z takes too long:** [We will pivot to W]
"""

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a Scientific Problem Selection project template")
    parser.add_argument("--name", required=True, help="Project Name")
    parser.add_argument("--author", default="Researcher", help="Author Name")

    args = parser.parse_args()
    print(generate_template(args.name, args.author))
