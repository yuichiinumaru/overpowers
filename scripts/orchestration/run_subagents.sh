#!/bin/bash
# Subagent orchestrator script for Gemini CLI
# Based on the experimental --prompt argument

echo "Iniciando orquestração de subagents no Gemini CLI..."

gemini --yolo -p "You are an expert orchestrator. Execute Task 009: Rebuild MCP infrastructure as described in docs/tasks/009-rebuild-mcp-infrastructure.md" > .agents/reports/task-009-log.txt 2>&1 &
gemini --yolo -p "You are an expert orchestrator. Execute Task 010: Recreate semgrep-code-security skill as described in docs/tasks/010-recreate-semgrep-skill.md" > .agents/reports/task-010-log.txt 2>&1 &
gemini --yolo -p "You are an expert orchestrator. Execute Task 011: Reinstall NLM skill as described in docs/tasks/011-reinstall-nlm-skill.md" > .agents/reports/task-011-log.txt 2>&1 &
gemini --yolo -p "You are an expert orchestrator. Execute Task 012: Reorganize docs directory as described in docs/tasks/012-reorganize-docs-directory.md" > .agents/reports/task-012-log.txt 2>&1 &
gemini --yolo -p "You are an expert orchestrator. Execute Task 013: Install script UX improvements as described in docs/tasks/013-install-script-ux.md" > .agents/reports/task-013-log.txt 2>&1 &
gemini --yolo -p "You are an expert orchestrator. Execute Task 014: Fix Antigravity MCP config as described in docs/tasks/014-fix-antigravity-mcp-config.md" > .agents/reports/task-014-log.txt 2>&1 &
gemini --yolo -p "You are an expert orchestrator. Execute Task 015: Update tasklist from audit as described in docs/tasks/015-update-tasklist-from-audit.md" > .agents/reports/task-015-log.txt 2>&1 &
gemini --yolo -p "You are an expert orchestrator. Execute Task 016: Second audit as described in docs/tasks/016-second-audit.md" > .agents/reports/task-016-log.txt 2>&1 &

echo "Todos os subagents foram iniciados em background e estão logando em .agents/reports/task-*-log.txt"
wait
echo "Subagentes concluídos!"
