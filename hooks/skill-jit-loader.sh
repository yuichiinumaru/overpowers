#!/usr/bin/env bash
# Skill JIT Loader Hook
# Event: BeforeToolSelection

set -euo pipefail

# This hook can eventually be used to inject SKILL.md content
# when the agent is about to select a tool related to a skill.
# For now, it provides the bridge for Level 2 Disclosure.

INPUT=$(cat)
echo "$INPUT"
