---
name: skin-health-tracker
description: Skin health management skill, records skin problems, monitors mole changes (ABCDE rule), manages skincare routines, tracks skin health status, analyzes skin health trends.
tags: [skin, health, healthcare, mole-monitoring, skincare]
version: 1.0.0
category: healthcare
---

# Skin Health Management Skills

Record skin problems, monitor mole changes, manage skincare routines, track skin health status, analyze skin health trends.

## Medical Disclaimer

This system is for health tracking and educational purposes only and does not provide medical diagnosis or treatment advice.

**Cannot do:**
- All skin problems should be consulted with a professional dermatologist.
- Abnormal changes in moles should be examined by a doctor immediately.
- Cannot replace professional dermatological examination and treatment.

**Can do:**
- Record and track skin health data.
- Provide skin examination records and reminders.
- Provide ABCDE rule self-examination guidance.
- Provide general skincare advice.

## Core Workflow

```
User Input → Identify Operation Type → [concern] Parse Skin Problem → Save Record
                                  ↓
                             [mole] Parse Mole Information → ABCDE Assessment → Save
                                  ↓
                             [routine] Parse Skincare Routine → Save
                                  ↓
                             [exam] Record Exam Results → Save
                                  ↓
                             [sun] Record Sun Exposure → Save
                                  ↓
                             [status/trend] Read Data → Display Report
```

## Operation Types

| Input Keywords | Operation Type |
|---------------|----------------|
| concern | concern - Skin problem record |
| mole | mole - Mole monitoring |
| routine | routine - Skincare routine |
| exam | exam - Skin exam record |
| sun | sun - Sun exposure record |
| status | status - View status |
| trend | trend - Trend analysis |
| reminder | reminder - Exam reminder |
| screening | screening - Disease screening |

## ABCDE Rule Explained

### A - Asymmetry
- Normal: The mole, when folded in half, has two symmetrical sides.
- Abnormal: The two halves of the mole are asymmetrical, with irregular shapes.

### B - Border
- Normal: The border is clear, smooth, and regular.
- Abnormal: The border is blurred, irregular, jagged, or scalloped.

### C - Color
- Normal: The color is uniform, usually brown, black, or skin-colored.
- Abnormal: The color is uneven, containing multiple colors.

### D - Diameter
- Normal: The diameter is usually less than 6mm.
- Abnormal: The diameter is greater than 6mm, or has increased significantly recently.

### E - Evolution
- Normal: Stable over time, with no significant changes.
- Abnormal: Recent changes in size, shape, color, thickness, or sensation.

## Emergency Situation Guidelines

### Requires Urgent Attention (within 24 hours)
- Sudden bleeding or ulceration of a mole.
- Rapid increase in size or change in color of a mole.
- Newly appearing suspicious mole.
- Widespread rash accompanied by fever.

### Requires Prompt Medical Attention (within 1 week)
- Mole exhibits ABCDE abnormalities.
- Wound or ulcer has not healed for over 2 weeks.
- Persistent itching affecting sleep.
