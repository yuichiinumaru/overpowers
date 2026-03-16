#!/usr/bin/env python3
import argparse
import sys
import os

def generate_template(template_type, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    template_path = os.path.join(output_dir, f"{template_type}_template.md")

    templates = {
        "job_description": """# Job Description: [Role Title]
## Mission
[What is the primary purpose of this role?]

## Outcomes in the First 90 Days
1. [Outcome 1]
2. [Outcome 2]
3. [Outcome 3]

## Core Competencies
- [Competency 1]
- [Competency 2]

## Requirements
### Must-Haves
- [Must-Have 1]
- [Must-Have 2]

### Nice-to-Haves
- [Nice-to-Have 1]

## Pay Band
[Pay Band Range]

## EOE Statement
[Your company's Equal Opportunity Employer statement]
""",
        "interview_rubric": """# Interview Rubric: [Role Title]
## Competency: [Competency Name]
- **1 (Needs Work):** [Description]
- **3 (Meets Expectations):** [Description]
- **5 (Exceeds Expectations):** [Description]

## Behavioral Questions
1. [Question 1]
   - *Look for:* [What a good answer sounds like]
2. [Question 2]
   - *Look for:* [What a good answer sounds like]
""",
        "offboarding_checklist": """# Offboarding Checklist
## Immediate Tasks
- [ ] Revoke IT/System access
- [ ] Collect company equipment

## Payroll/Benefits
- [ ] Process final paycheck
- [ ] Provide benefits continuation information

## Exit Process
- [ ] Conduct Exit Interview
- [ ] Communicate departure to team
"""
    }

    if template_type in templates:
        with open(template_path, 'w') as f:
            f.write(templates[template_type])
        print(f"[*] Generated {template_type} template at {template_path}")
    else:
        print(f"[-] Invalid template type: {template_type}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="HR Template Generator")
    parser.add_argument("-t", "--type", required=True, choices=["job_description", "interview_rubric", "offboarding_checklist"], help="Type of template to generate")
    parser.add_argument("-o", "--output", default=".", help="Output directory for the template")

    args = parser.parse_args()
    generate_template(args.type, args.output)
