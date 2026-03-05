import argparse
from datetime import datetime

def generate_summary(intent, files_modified, decisions, current_state, next_steps):
    files_list = "\n".join([f"- {f}" for f in files_modified]) if files_modified else "None"
    decisions_list = "\n".join([f"- {d}" for f in decisions]) if decisions_modified else "None"
    next_steps_list = "\n".join([f"{i+1}. {step}" for i, step in enumerate(next_steps)]) if next_steps else "None"
    
    summary = f"""# Session Summary - {datetime.now().strftime('%Y-%m-%d %H:%M')}

## Session Intent
{intent}

## Files Modified
{files_list}

## Decisions Made
{decisions_list}

## Current State
{current_state}

## Next Steps
{next_steps_list}
"""
    return summary

def main():
    parser = argparse.ArgumentParser(description='Generate a structured session summary for context compression.')
    parser.add_argument('--intent', required=True, help='Session intent')
    parser.add_argument('--files', nargs='*', help='List of modified files')
    parser.add_argument('--decisions', nargs='*', help='List of decisions made')
    parser.add_argument('--state', required=True, help='Current state description')
    parser.add_argument('--next', nargs='*', help='List of next steps')
    parser.add_argument('--output', help='Output file path (default: stdout)')

    args = parser.parse_args()

    files = args.files if args.files else []
    decisions = args.decisions if args.decisions else []
    next_steps = args.next if args.next else []

    # Check if we have comma-separated strings instead of list
    if len(files) == 1 and ',' in files[0]: files = [f.strip() for f in files[0].split(',')]
    if len(decisions) == 1 and ',' in decisions[0]: decisions = [d.strip() for d in decisions[0].split(',')]
    if len(next_steps) == 1 and ',' in next_steps[0]: next_steps = [s.strip() for s in next_steps[0].split(',')]

    files_list = "\n".join([f"- {f}" for f in files]) if files else "None"
    decisions_list = "\n".join([f"- {d}" for f in decisions]) if decisions else "None"
    next_steps_list = "\n".join([f"{i+1}. {step}" for i, step in enumerate(next_steps)]) if next_steps else "None"
    
    summary = f"""# Session Summary - {datetime.now().strftime('%Y-%m-%d %H:%M')}

## Session Intent
{args.intent}

## Files Modified
{files_list}

## Decisions Made
{decisions_list}

## Current State
{args.state}

## Next Steps
{next_steps_list}
"""

    if args.output:
        with open(args.output, 'w') as f:
            f.write(summary)
        print(f"Summary written to {args.output}")
    else:
        print(summary)

if __name__ == "__main__":
    main()
