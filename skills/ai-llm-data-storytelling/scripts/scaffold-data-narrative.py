#!/usr/bin/env python3
print("Scaffolding data storytelling narrative...")
template = """
# Data Story: [Title]

## The Hook (Context)
[Why does this data matter now?]

## The Conflict (The Problem/Insight)
[What surprising or critical insight does the data reveal?]

## The Resolution (Actionable Takeaways)
[What should the audience do based on this data?]
"""
with open("data_narrative.md", "w") as f:
    f.write(template)
print("Saved to data_narrative.md")
