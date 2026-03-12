import os
import re
from datetime import datetime

class AnalysisSessionHelper:
    """Helper to manage analyze-with-file sessions."""
    
    def __init__(self, project_root):
        self.project_root = project_root

    def generate_session_id(self, topic):
        slug = re.sub(r'[^a-z0-9]+', '-', topic.lower())[:40].strip('-')
        date_str = datetime.now().strftime("%Y-%m-%d")
        return f"ANL-{slug}-{date_str}"

    def initialize_session(self, topic, depth="standard"):
        session_id = self.generate_session_id(topic)
        session_folder = os.path.join(self.project_root, ".workflow", ".analysis", session_id)
        os.makedirs(session_folder, exist_ok=True)
        
        discussion_path = os.path.join(session_folder, "discussion.md")
        if not os.path.exists(discussion_path):
            template = self._get_discussion_template(session_id, topic, depth)
            with open(discussion_path, 'w') as f:
                f.write(template)
        
        return session_id, session_folder

    def _get_discussion_template(self, session_id, topic, depth):
        now = datetime.now().isoformat()
        return f"""# Analysis Discussion

**Session ID**: {session_id}
**Topic**: {topic}
**Started**: {now}
**Dimensions**: architecture, implementation
**Depth**: {depth}

## Analysis Context
- Focus areas: TBD
- Perspectives: Technical
- Depth: {depth}

## Initial Questions
- What are the core components involved in {topic}?
- What are the current patterns being used?

---

## Discussion Timeline

> Rounds will be appended below as analysis progresses.

---

## Current Understanding

> To be populated after exploration.
"""

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python analysis_session_helper.py <topic> [depth]")
        sys.exit(1)
    
    topic = sys.argv[1]
    depth = sys.argv[2] if len(sys.argv) > 2 else "standard"
    
    helper = AnalysisSessionHelper(os.getcwd())
    sid, folder = helper.initialize_session(topic, depth)
    print(f"Session Initialized: {sid}")
    print(f"Folder: {folder}")
