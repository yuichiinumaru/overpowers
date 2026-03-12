import re

with open("CHANGELOG.md", "r") as f:
    content = f.read()

new_entry = """## [2026-03-07] - Consolidated Parallel PRs for Jules Skill Scripts Batches
### Added
- Evaluated and verified parallel run outputs from Jules agents for the remaining `0300` skill batches.
- Merged and patched the most comprehensive version of scripts generated across 22 parallel batches directly into the main `development` bookmark via Jujutsu, avoiding snapshot corruption of immutable remote branches by using patch diffing.
- Auto-closed the corresponding Github Pull Requests associated with parallel Jules runs.
**Author**: Overpowers Architect (Antigravity)

"""

# Find the first ## [YYYY-MM-DD]
match = re.search(r"## \[\d{4}-\d{2}-\d{2}\]", content)
if match:
    idx = match.start()
    new_content = content[:idx] + new_entry + content[idx:]
    with open("CHANGELOG.md", "w") as f:
        f.write(new_content)
    print("CHANGELOG.md patched successfully.")
else:
    print("Could not find insertion point!")
