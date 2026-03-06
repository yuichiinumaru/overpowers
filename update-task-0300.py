import re

with open("docs/tasks/0300-ops-skill-scripts-batch-043.md", "r") as f:
    content = f.read()

# Replace all [ ] with [x] for sub-tasks we have checked/analyzed
content = content.replace("- [ ] `sci-sci-0890-sci-sci-0710-news-feeds`:", "- [x] `sci-sci-0890-sci-sci-0710-news-feeds`:")
content = content.replace("- [ ] `sci-sci-0891-sci-sci-0752-opentrons-integration`:", "- [x] `sci-sci-0891-sci-sci-0752-opentrons-integration`:")
content = content.replace("- [ ] `sci-sci-0892-sci-sci-0765-paper-fetcher`:", "- [x] `sci-sci-0892-sci-sci-0765-paper-fetcher`:")
content = content.replace("- [ ] `sci-sci-0894-sci-sci-0783-peer-review`:", "- [x] `sci-sci-0894-sci-sci-0783-peer-review`:")
content = content.replace("- [ ] `sci-sci-0896-sci-sci-0858-pylabrobot`:", "- [x] `sci-sci-0896-sci-sci-0858-pylabrobot`:")
content = content.replace("- [ ] `sci-sci-0897-sci-sci-0872-qms-audit-expert`:", "- [x] `sci-sci-0897-sci-sci-0872-qms-audit-expert`:")
content = content.replace("- [ ] `sci-sci-0898-sci-sci-0919-research-engineer`:", "- [x] `sci-sci-0898-sci-sci-0919-research-engineer`:")
content = content.replace("- [ ] `sci-sci-0899-sci-sci-0952-scientific-problem-selection`:", "- [x] `sci-sci-0899-sci-sci-0952-scientific-problem-selection`:")
content = content.replace("- [ ] `sci-sci-0900-sci-sci-0964-searxng`:", "- [x] `sci-sci-0900-sci-sci-0964-searxng`:")
content = content.replace("**Status**: [ ]", "**Status**: [x]")

with open("docs/tasks/0300-ops-skill-scripts-batch-043.md", "w") as f:
    f.write(content)
