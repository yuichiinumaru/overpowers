---
name: study-buddy
description: AI-powered learning companion for creating personalized study plans, tracking progress, and providing feedback. Use when user wants to start learning something new, create a study plan, track learning progress, get study reminders, or receive learning feedback. Triggers include "帮我制定学习计划", "我要学XX", "追踪我的学习进度", "学习打卡", "study plan", "learn programming", "track my progress".
---

# Study Buddy - Intelligent Learning Companion

An AI learning companion that helps you create study plans, track progress, and provides feedback.

## Core Features

1. **User Profile** - Interactively collect learning goals, time, level, and preferences
2. **Study Plan** - Generate personalized phased plans based on background
3. **Daily Check-in** - Record study duration and content
4. **Progress Tracking** - Statistics on study days, consecutive check-ins, and phase assessments
5. **Study Report** - Generate periodic study summaries and ratings
6. **Mistake Notebook** - Record, review, and master incorrect questions
7. **Feedback Suggestions** - Provide personalized advice based on data

## Command Entry

```bash
# Start the learning journey (interactively collect background)
python3 scripts/study-buddy.py start

# View today's study tasks
python3 scripts/study-buddy.py today

# Study check-in
python3 scripts/study-buddy.py checkin "Studied basic Python syntax" --duration "45 minutes"

# View study progress
python3 scripts/study-buddy.py progress

# View study plan
python3 scripts/study-buddy.py plan

# Generate study report
python3 scripts/study-buddy.py report

# Mistake notebook management
python3 scripts/study-buddy.py wrong add "Error in solving quadratic equations"
python3 scripts/study-buddy.py wrong list
python3 scripts/study-buddy.py wrong review "Mistake ID"
python3 scripts/study-buddy.py wrong master "Mistake ID"

# Get feedback suggestions
python3 scripts/study-buddy.py feedback

# View study data storage location
python3 scripts/study-buddy.py data
```

## Data Storage

User data is stored in: `~/.study-buddy/`
- `profile.json` - Learning background profile
- `plans/` - Study plan directory
- `logs/` - Study log records
- `wrong_questions/` - Mistake notebook
- `report_YYYYMMDD.json` - Study report

## Usage Flow

1. **Initialization**: Run `start` to create a learning profile
2. **Plan Creation**: Automatically generate a study plan based on background, view with `plan`
3. **Daily Execution**: Use `today` to view tasks, `checkin` to record
4. **Regular Review**: Use `progress` to view progress, `report` to generate reports
5. **Mistake Management**: Use the `wrong` command to manage the mistake notebook

## Target Users

Primary focus: **High school students and parents**

## Safety Boundaries

- ✅ Study plan creation, progress tracking, check-ins, feedback, study reports
- ❌ Does not provide specific subject teaching content (e.g., solving math problems)
- ❌ Does not replace teacher/parent decisions
- ❌ Does not connect to external education platforms
- ❌ Does not make exaggerated learning effect promises
- ❌ Does not collect sensitive private information
- ✅ Respects user privacy, data is stored locally
- ✅ Recommends users combine with real teachers or professional courses

## Expansion Plan (Future Planning, Not Current Version)

The following features are directions for future iterations and are not implemented in the current MVP version:

- [ ] Feishu integration
- [ ] Visualized reports
- [ ] Intelligent reminder function
- [ ] Multi-plan management
- [ ] Data export function
- [ ] More intelligent plan generation algorithm

## Reference Documents

- Command detailed description: [references/commands.md](references/commands.md)
- Development to-do list: [references/todo.md](references/todo.md)
