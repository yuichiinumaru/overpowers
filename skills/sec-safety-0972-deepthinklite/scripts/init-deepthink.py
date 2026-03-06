#!/usr/bin/env python3
import os
import sys
import json
import time

def main():
    if len(sys.argv) < 2:
        print("Usage: init-deepthink.py <research-topic>")
        sys.exit(1)

    topic = sys.argv[1]
    slug = topic.lower().replace(" ", "-")[:30]
    out_dir = f"deepthinklite/{slug}"

    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
        print(f"Created run directory: {out_dir}")

    questions_content = f"""# DeepthinkLite Investigation Map: {topic}

## High-Leverage Questions
1. [Question 1] - Source: [Web/Docs/Code]
2. [Question 2] - Source: [Web/Docs/Code]

## Investigation Plan
- [ ] Phase 1: [Task]
- [ ] Phase 2: [Task]
"""

    response_content = """# DeepthinkLite Response

## Direct Answer
[To be populated]

## Reasoning Summary
[To be populated]

## Recommendations
- [Next Step 1]

## Unknowns & Risks
- [Risk 1]

## References
- [Link/Path 1]
"""

    meta_content = {
        "topic": topic,
        "timestamp": int(time.time()),
        "status": "initialized"
    }

    with open(os.path.join(out_dir, "questions.md"), "w") as f:
        f.write(questions_content)
    with open(os.path.join(out_dir, "response.md"), "w") as f:
        f.write(response_content)
    with open(os.path.join(out_dir, "meta.json"), "w") as f:
        json.dump(meta_content, f, indent=2)

    print(f"Initialized DeepthinkLite run in: {out_dir}")

if __name__ == "__main__":
    main()
