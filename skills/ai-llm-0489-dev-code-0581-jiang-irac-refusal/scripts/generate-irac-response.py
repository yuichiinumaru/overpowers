#!/usr/bin/env python3
print("Generating IRAC structure for trademark refusal response...")
template = """
# IRAC Trademark Refusal Response

## Issue
[Define the core legal issue raised by the CNIPA refusal]

## Rule
[Cite relevant trademark laws and examination guidelines]

## Application
[Apply the rules to the specific facts of the case, constructing a solid evidence chain]

## Conclusion
[State the final argument for why the refusal should be overturned]
"""
with open("irac_response.md", "w") as f:
    f.write(template)
print("Template saved to irac_response.md")
