import argparse
from datetime import datetime

def generate_minutes_template(title, organizer):
    now = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    today = datetime.utcnow().strftime("%Y-%m-%d")
    
    schema = f"""# Meeting Minutes: {title}

## 1. Metadata
- **Title**: {title}
- **Date (YYYY-MM-DD)**: {today}
- **Start Time (UTC)**: TBD
- **End Time (UTC) or Duration**: TBD
- **Organizer**: {organizer}
- **Location / Virtual Link**: TBD
- **Minutes Author**: Agent
- **Distribution List**: TBD

## 2. Attendance
- **Present**: TBD
- **Regrets / Absent**: TBD
- **Notetaker / Recorder**: Agent

## 3. Agenda
- Item 1: TBD

## 4. Summary
TBD (1-3 sentences)

## 5. Decisions Made
- **Decision 1**: TBD
  - Who decided / approved: TBD
  - Rationale: TBD

## 6. Action Items
- [A1] Action: TBD
  - **Owner**: TBD
  - **Due**: TBD
  - **Acceptance Criteria**: TBD

## 7. Notes by Agenda Item
- **Agenda Item 1**: TBD

## 8. Parking Lot / Unresolved Items
- **Item**: TBD

## 9. Risks / Blockers
- **Risk 1**: TBD

## 10. Next Meeting / Follow-up
- TBD

## 11. Attachments / References
- TBD

## 12. Version & Change Log
- **Version**: 1.0
- **Last updated**: {now}
- **Changes**: Initial draft
"""
    return schema

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate meeting minutes template.")
    parser.add_argument("--title", required=True, help="Meeting title")
    parser.add_argument("--organizer", required=True, help="Meeting organizer")
    parser.add_argument("--output", help="Output file path (optional)")
    
    args = parser.parse_args()
    
    minutes = generate_minutes_template(args.title, args.organizer)
    
    if args.output:
        with open(args.output, "w") as f:
            f.write(minutes)
        print(f"Template saved to {args.output}")
    else:
        print(minutes)
