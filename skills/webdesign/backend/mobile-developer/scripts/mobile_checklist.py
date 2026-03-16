import sys

CHECKLISTS = {
    "ios": [
        "All app metadata complete",
        "Screenshots for all device sizes",
        "App preview video (optional but recommended)",
        "Privacy policy URL",
        "Support URL",
        "Test account if login required",
        "No TestFlight or debug code",
        "App Tracking Transparency implemented if tracking",
        "Verify Guideline 4.2: Minimum functionality",
        "Verify Guideline 2.1: App completeness"
    ],
    "android": [
        "App bundle (.aab) generated",
        "All store listing complete",
        "Screenshots for phone and tablet",
        "Privacy policy URL",
        "Data safety form complete",
        "Content rating questionnaire finished",
        "Tested on multiple devices/API levels",
        "Target API level matches current requirements",
        "Verify no deceptive behavior",
        "Permissions justification provided if needed"
    ]
}

def show_checklist(platform):
    if platform not in CHECKLISTS:
        print(f"Unknown platform: {platform}. Available: ios, android")
        return
    
    print(f"--- {platform.upper()} Submission Checklist ---")
    for item in CHECKLISTS[platform]:
        print(f"[ ] {item}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python mobile_checklist.py <ios|android>")
    else:
        show_checklist(sys.argv[1].lower())
