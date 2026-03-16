#!/usr/bin/env python3
import sys
import os
from datetime import datetime, timedelta

def generate_onboarding_plan(name, role, start_date_str, location="Remote"):
    try:
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    except ValueError:
        print("Error: Invalid date format. Use YYYY-MM-DD.")
        return

    plan = f"""# Onboarding Plan for {name}
**Role**: {role}
**Start Date**: {start_date.strftime("%A, %B %d, %Y")}
**Location**: {location}

## Pre-Onboarding Checklist
- [ ] Laptop shipped
- [ ] Email account created
- [ ] Slack/Teams invited
- [ ] GitHub/GitLab access granted
- [ ] Welcome email sent

## Day 1: Foundation
- [ ] {start_date.strftime("%H:%M")} - Manager 1:1 Welcome
- [ ] { (start_date + timedelta(hours=1)).strftime("%H:%M") } - Company Orientation
- [ ] { (start_date + timedelta(hours=2)).strftime("%H:%M") } - Team Introductions
- [ ] Technical Setup: IDE, Linters, local env
- [ ] SSH keys and Git config

## Week 1: Immersion
- [ ] Architecture overview session
- [ ] Development workflow walkthrough
- [ ] Identify 'good first issue'
- [ ] Submit first PR with buddy guidance

## 30-Day Milestones
- [ ] Complete all mandatory training
- [ ] Merge at least 3 pull requests
- [ ] Document one process or system
- [ ] Presentation of learnings to the team

## 60-Day Milestones
- [ ] Own a small feature end-to-end
- [ ] Shadow on-call rotation
- [ ] Contribute to technical design discussions

## 90-Day Milestones
- [ ] Independent feature delivery
- [ ] Active code review participation
- [ ] Mentor a newer team member (if applicable)
"""
    
    filename = f"onboarding-{name.lower().replace(' ', '-')}.md"
    with open(filename, 'w') as f:
        f.write(plan)
    
    print(f"Successfully generated onboarding plan: {filename}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: onboarding_generator.py <name> <role> <start_date_YYYY-MM-DD> [location]")
        sys.exit(1)
    
    name = sys.argv[1]
    role = sys.argv[2]
    date = sys.argv[3]
    loc = sys.argv[4] if len(sys.argv) > 4 else "Remote"
    
    generate_onboarding_plan(name, role, date, loc)
