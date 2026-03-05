# getsentry-skills Comparison Report

## Overview
- Total items: 7 skills, 1 agent
- ADOPT: 2
- ADAPT: 1
- DISCARD: 5

## ADOPT (Ready to Use)
| Item | Type | Reason |
|------|------|--------|
| find-bugs | skill | Focused bug/vulnerability detection in branch changes - novel approach |
| iterate-pr | skill | CI iteration loop until all checks pass - useful workflow |

## ADAPT (Needs Modification)
| Item | Type | Changes Needed |
|------|------|----------------|
| claude_settings_audit | skill | Rename - already exists in Overpowers but may have different implementation |

## DISCARD (Skip)
| Item | Reason |
|------|--------|
| code_review | Covered by code_review skill |
| commit | Covered by git_pushing skill |
| create-pr | Covered by create-pr command |
| agents-md | Sentry-specific format |
| code-simplifier | Covered by code_refactorer agent |

## Recommendation
**MEDIUM VALUE** - find-bugs and iterate-pr skills offer useful patterns. The bug detection in branch changes is a focused approach worth adopting.
