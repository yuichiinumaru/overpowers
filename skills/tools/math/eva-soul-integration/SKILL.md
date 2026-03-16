---
name: ai-personality-eva-soul-integration
description: Complete integration of the EVA Soul cognitive system. Automatically manages memory, emotions, and personality during every conversation. Features automated installation and persistent state management.
tags: ai, personality, soul, eva, cognitive-system
version: 1.1.0
---

# EVA Soul Integration Skill

Integrate the EVA Soul cognitive system into AI agent host platforms.

## Functions

- **Full Core System**: Built-in EVA Soul core modules (memory, emotion, personality).
- **Auto-Invocation**: Automatically calls `eva_integrated_final.py` for each message.
- **Memory Management**: Persists important information to the memory system.
- **Emotion Perception**: Real-time sensing of user sentiment.
- **Dynamic Personality**: Adjusts response style based on context.

## Usage

### Installation
```bash
clawhub install eva-soul-integration
bash scripts/install.sh
```

### Manual Test
```bash
python3 scripts/eva_soul_call.py -m "Hello"
```

## Structure
- `scripts/eva_soul_call.py`: Main entry point.
- `eva-soul-github/scripts/`: Core logic modules.
- `memory/`: Persistent JSON data for state.
