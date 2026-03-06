#!/usr/bin/env python3
import sys
import os
from datetime import datetime, timedelta

def create_request_scaffold(request_id, subject_name, request_type):
    deadline = (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")
    
    template = f"""# Data Subject Request: {request_id}
Date Received: {datetime.now().strftime("%Y-%m-%d")}
Deadline (30 days): {deadline}
Subject Name: {subject_name}
Request Type: {request_type}

## 1. Identity Verification
- [ ] Identification documents provided?
- [ ] Identity confirmed?

## 2. Request Assessment
- [ ] Scope of data clearly defined?
- [ ] Any exemptions applicable?
- [ ] Third-party rights affected?

## 3. Data Collection
- [ ] Systems searched?
- [ ] Data extracted/compiled?

## 4. Response Preparation
- [ ] Information redacted (if needed)?
- [ ] Response letter drafted?
- [ ] Format compliant (e.g., electronic)?

## 5. Completion
- [ ] Response sent?
- [ ] Documentation archived?
- [ ] ROPA updated (if needed)?
"""
    file_name = f"DSR-{request_id}-{subject_name.replace(' ', '_')}.md"
    with open(file_name, "w") as f:
        f.write(template)
    print(f"Created request scaffold: {file_name}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: rights_request_scaffold.py <request_id> <subject_name> <request_type>")
        print("Types: Access, Erasure, Rectification, Portability, Restriction, Objection")
        sys.exit(1)
    
    create_request_scaffold(sys.argv[1], sys.argv[2], sys.argv[3])
