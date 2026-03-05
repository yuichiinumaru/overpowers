#!/usr/bin/env python3
import sys

def generate_gap_prompt(obstruction, gap_type, subject, action, lighting, mood):
    prompt = f"""**Core Style:** Keyhole reveal composition, gap focus.
**Foreground:** {obstruction} blocking 50% of the view, heavily out of focus, framing the scene.
**Subject:** Through a narrow {gap_type}, {subject} is visible performing {action}.
**Optics:** Razor-sharp focus on {subject}, deep depth of field, cinematic bokeh.
**Mood:** {lighting}, {mood}, 8k resolution, cinematic color grading."""
    
    print("--- Generated Gap Focus Prompt ---")
    print(prompt)
    print("\n--- Review Checklist ---")
    print("1. Gap Constraint: Is it narrow enough?")
    print("2. Subject Placement: Is it centered in the gap?")
    print("3. Blur Contrast: Foreground blurred, subject sharp?")
    print("4. Story Element: Does it feel like a captured secret?")

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: generate_gap_prompt.py <obstruction> <gap_type> <subject> <action> [lighting] [mood]")
        sys.exit(1)
    
    obs = sys.argv[1]
    gap = sys.argv[2]
    sub = sys.argv[3]
    act = sys.argv[4]
    lit = sys.argv[5] if len(sys.argv) > 5 else "Tyndall effect light rays"
    mood = sys.argv[6] if len(sys.argv) > 6 else "suspenseful atmosphere"
    
    generate_gap_prompt(obs, gap, sub, act, lit, mood)
