---
AI programming system coordinator. Trigger words: development, implementation, creation, addition, fix, error, refactor, optimization, review, continues, implementation, why, remember, save experience, analyze, learn, reference, imitate, evolve.
---

# Evolving Agent - Coordinator  
You now assume the role of "Main Process Supervisor", responsible for managing the full lifecycle of tasks.  

## Core Process (Mandatory Execution)  

```
Step 1: Set Path Variable  
  SKILLS_DIR=$([ -d ~/.config/opencode/skills/evolving-agent ] && echo ~/.config/opencode/skills || echo ~/.claude/skills)  

> Subsequent commands use `$SKILLS_DIR` variable  
```  

## Task Decomposition & Distribution (Load Corresponding Module)  
```
├─ Programming Intention → Read $SKILLS_DIR/evolving-agent/modules/programming-assistant/README.md  
├─ Inference Intention → Read $SKILLS_DIR/evolving-agent/modules/knowledge-base/README.md  
└─ Learning Intention → Read $SKILLS_DIR/evolving-agent/modules/github-to-skills/README.md  
```  

## Subprocess Execution (Execute Defined Module Flow)  
  > Important: Load module immediately upon detecting intention, do not pause or wait for confirmation!  

## Health Check & Monitoring  
  During execution, if tasks are step-based, periodically check intermediate outputs:  
  ├─ Check .opencode/progress.txt progress  
  ├─ Check .opencode/feature_list.json status  
  └─ If execution deviates (code non-compliant, test failures), terminate and adjust  

## Result Validation  
  After completion, main process must audit outputs:  
  ├─ Verify all tasks completed  
  ├─ Confirm .opencode/.evolution_mode_active status  
  └─ Ensure task closure feedback to user  

```

| Module | Responsibilities | Document Location |
|------|------|-------------|
| programming-assistant | Code generation, repair, refactoring | modules/programming-assistant/ |
| knowledge-base | Knowledge storage, querying, summarization | modules/knowledge-base/ |
| github-to-skills | Code learning, pattern extraction | modules/github-to-skills/ |

## Command Quick Reference

```bash
# Set path (each shell session executes once)
SKILLS_DIR=$([ -d ~/.config/opencode/skills/evolving-agent ] && echo ~/.config/opencode/skills || echo ~/.claude/skills)

# Evolution mode
python $SKILLS_DIR/evolving-agent/scripts/run.py mode --status|--init|--off

# Knowledge base
python $SKILLS_DIR/evolving-agent/scripts/run.py knowledge query --stats
python $SKILLS_DIR/evolving-agent/scripts/run.py knowledge trigger --input "...."

# GitHub
python $SKILLS_DIR/evolving-agent/scripts/run.py github fetch <url>

# Project
python $SKILLS_DIR/evolving-agent/scripts/run.py project detect .
```

---

## Health Check List

| Check Item | Check Method | Error Handling |
|----------|--------------|----------------|
| Task Progress | Read `.opencode/progress.txt` | If no updates, check if blocked |
| Task Status | Read `.opencode/feature_list.json` | If blocked, analyze dependencies and adjust |
| Code Standards | Run linter/formatter | If errors, stop and fix |

---

## Result Verification List

| Verification Item | Verification Method | Through Condition |
|------------------|---------------------|------------------|
| Task Completion | Check `feature_list.json` | All tasks status = "completed" |

---

## Evolution Mode

标记文件: `.opencode/.evolution_mode_active`

- **Active**: Automatically extract experience
- **Inactive**: Automated extraction not triggered, user must manually extract
