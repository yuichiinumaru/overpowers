# Overpowers 🚀

**Overpowers** is a consolidated, optimized, and enhanced toolkit for OpenCode. It centralizes agents, skills, and commands into a single, highly capable repository.

## ✨ Credits

This project is built upon the foundation of the original **OpenCode Superpowers** toolkit. We extend our deepest gratitude to the creators and community of Superpowers for establishing the patterns and capabilities that make this enhanced version possible.

## 🌟 Key Features

- **Jules Swarm Integration**: Seamlessly dispatch, harvest, and triage tasks from Google's Jules AI agent. Includes the `jules-swarm` SDK as a built-in submodule.
- **Optimized Model Fallbacks**: Robust fallback chains for 120+ specialized agents, ensuring reliability across model tiers.
- **Enhanced Skills**: Brainstorming with probability sampling, advanced code review, and more.
- **Task Tracking**: Integrated with `Beads` (bd) for git-native task and memory management.
- **Codebase Visualization**: Integrated with `Codemap` for intelligent project analysis.

## 🛠 Structure

- `agents/`: 120+ specialized AI agents with benchmark-driven model configurations.
- `skills/`: Custom logic for complex workflows, including the Jules Swarm lifecycle.
- `commands/`: Convenient shorthand for frequently used agentic operations.
- `packages/`: External dependencies and submodules, including `jules-swarm`.

## 🚀 Getting Started

1. Ensure `Overpowers` is active in your `opencode.json`:
   ```json
   {
     "plugins": [
       "./overpowers/.opencode/plugin/Overpowers.js"
     ]
   }
   ```
2. Explore the available skills using `/skills:list`.
3. Dispatch your first Jules task with `/jules-dispatch`.

---
*Empowering your OpenCode environment with agentic excellence.*
