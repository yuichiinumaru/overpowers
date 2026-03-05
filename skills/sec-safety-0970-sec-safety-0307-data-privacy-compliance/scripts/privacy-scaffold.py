#!/usr/bin/env python3
import os
import sys
from datetime import datetime

def create_dpia_template():
    content = f"""# Data Protection Impact Assessment (DPIA)

## 1. Context & Purpose
- **Project Name**: [Name]
- **Date**: {datetime.now().strftime('%Y-%m-%d')}
- **DPO**: [Name]
- **Description**: [Brief description of the data processing activity]

## 2. Necessity & Proportionality
- [ ] Is processing necessary for the stated purpose?
- [ ] Could the purpose be achieved with less data?
- [ ] Is the retention period justified?

## 3. Risk Assessment
| Risk | Likelihood | Severity | Mitigation |
|------|------------|----------|------------|
| Data breach | [L/M/H] | [L/M/H] | [Mitigation] |
| Unauthorized access | [L/M/H] | [L/M/H] | [Mitigation] |
| Purpose creep | [L/M/H] | [L/M/H] | [Mitigation] |

## 4. Conclusion
[Final assessment and decision]
"""
    with open("DPIA-Template.md", "w") as f:
        f.write(content)
    print("Created DPIA-Template.md")

def create_privacy_policy_template():
    content = """# Privacy Policy

## 1. Data Collection
[List data collected]

## 2. Lawful Basis
- **Consent**: [Purpose]
- **Contract**: [Purpose]
- **Legitimate Interest**: [Purpose]

## 3. Your Rights
- Right to Access
- Right to Deletion
- Right to Portability
- Right to Object

## 4. Contact
Contact our DPO at: dpo@example.com
"""
    with open("Privacy-Policy-Draft.md", "w") as f:
        f.write(content)
    print("Created Privacy-Policy-Draft.md")

def main():
    print("Generating Privacy Compliance Templates...")
    create_dpia_template()
    create_privacy_policy_template()

if __name__ == "__main__":
    main()
