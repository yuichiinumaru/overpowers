import sys
import os

TEMPLATES = {
    "deal_review": ["Deal summary", "Contract status", "Approval requirements", "Counterparty dynamics", "Comparable deals"],
    "board": ["Legal department update", "Risk highlights", "Regulatory update", "Pending approvals", "Litigation summary"],
    "regulatory": ["Regulatory body context", "Matter history", "Compliance posture", "Counsel coordination", "Privilege considerations"]
}

BASE_TEMPLATE = """## Meeting Brief

### Meeting Details
- **Meeting**: {title}
- **Date/Time**: {datetime}
- **Duration**: {duration}
- **Location**: {location}
- **Your Role**: {role}

### Participants
| Name | Organization | Role | Key Interests | Notes |
|---|---|---|---|---|
| | | | | |

### Agenda / Expected Topics
1. 

### Background and Context

### Key Documents
- 

### Open Issues
| Issue | Status | Owner | Priority | Notes |
|---|---|---|---|---|
| | | | | |

### Legal Considerations

### Talking Points
1. 

### Questions to Raise
- 

### Decisions Needed
- 

### Red Lines / Non-Negotiables

### Prior Meeting Follow-Up

### Preparation Gaps
"""

def generate_brief(meeting_type, title="[title]"):
    content = BASE_TEMPLATE.format(
        title=title,
        datetime="[date and time]",
        duration="[duration]",
        location="[location]",
        role="[advisor / presenter / negotiator / observer]"
    )
    
    if meeting_type in TEMPLATES:
        content += "\n### " + meeting_type.replace('_', ' ').title() + " Specifics\n"
        for section in TEMPLATES[meeting_type]:
            content += f"#### {section}\n\n"
            
    return content

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_meeting_brief.py <meeting_type> [title]")
        print("Types: deal_review, board, regulatory, general")
    else:
        m_type = sys.argv[1].lower()
        m_title = sys.argv[2] if len(sys.argv) > 2 else "[title]"
        print(generate_brief(m_type, m_title))
