import sys
import argparse

def choreograph(subject):
    """
    Generate a 5-beat high-dynamic action sequence for AI video generation.
    """
    print(f"Choreographing high-dynamic sequence for: {subject}\n")
    
    template = f"""**[Subject: {subject}]**

**Beat 1 (0-1.5s)**: [Initial reaction or preparation based on the starting state]
**Beat 2 (1.5-2.0s)**: [Significant shift in posture or beginning of acceleration]
**Beat 3 (2.0-3.0s)**: [Core dynamic peak - the most intense movement]
**Beat 4 (3.0-4.0s)**: [Action climax or dramatic interaction with the environment]
**Beat 5 (4.0-5.0s)**: [Momentum release, inertia, or landing result]

**Camera work**: [Dynamic motion description, e.g., tracking shots, low-angle hero shots].
**Acting style**: Acting should be emotional and realistic.

**Technical Specs**: 4K details, natural color, cinematic lighting and shadows, crisp textures, clean edges, fine material detail, high microcontrast, realistic shading, accurate tone mapping, smooth gradients, realistic highlights, detailed fabric and hair, sharp and natural.
"""
    print(template)
    return template

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python choreograph_sequence.py <subject_description>")
    else:
        choreograph(sys.argv[1])
