# 📋 Master Tasklist

Este é o índice principal de tarefas do repositório Overpowers. Agentes Jules e outros orquestradores vasculham esta lista para descobrir em qual macrotarefa trabalhar.

## 🔴 Prioridade Crítica (Core reliability)
- [x] [0018-ops-intent-classification](tasks/completed/0018-ops-intent-classification.md) — Mandatory Phase 0 for intent gating
- [x] [0023-ops-advanced-hooks](tasks/completed/0023-ops-advanced-hooks.md) — Todo Enforcer, Dir Context Injector, Edit Recovery
- [x] [0032-ai-model-fallback-system](.archive/0032-ai-model-fallback-system.md) — (Archived) Automatic fallback (Opus -> Flash -> GLM)
- [x] [0034-ops-installer-ux-modularity](tasks/completed/0034-ops-installer-ux-modularity.md) — Refactor install.sh and unify deploys
- [x] [0033-ops-skill-standardization-phase-2](tasks/completed/0033-ops-skill-standardization-phase-2.md) — Metadata sweep and template implementation (Done via 0180, 0200, 0210)
- [x] [0009-ops-rebuild-mcp-infrastructure](tasks/completed/0009-ops-rebuild-mcp-infrastructure.md) — Rebuild build-packages.sh, .env.example, opencode-example.json, install-mcps.sh
- [x] [0014-ops-fix-antigravity-mcp-config](tasks/completed/0014-ops-fix-antigravity-mcp-config.md) — Standardized with absolute paths

## 🟡 Prioridade Alta (Scale & Performance)
- [x] [0019-ops-feature-progressive-disclosure](tasks/completed/0019-ops-feature-progressive-disclosure.md) — Context-efficient skill loading (Infrastructure)
- [x] [0010-ops-recreate-semgrep-skill](tasks/completed/0010-ops-recreate-semgrep-skill.md) — Recreate skills/semgrep-code-security/SKILL.md
- [x] [0011-ops-reinstall-nlm-skill](tasks/completed/0011-ops-reinstall-nlm-skill.md) — Reinstall NotebookLM skill via nlm CLI

## 🔵 Organização & Melhoria
- [ ] [0025-dev-evaluation-driven-dev](tasks/0025-dev-evaluation-driven-dev.md) — QA framework for skills
- [ ] [0026-ops-moltbot-memory-integration](tasks/0026-ops-moltbot-memory-integration.md) — Hybrid Vector/Keyword search
- [ ] [0035-ops-containerized-sandbox](tasks/0035-ops-containerized-sandbox.md) — Docker environment for tasks
- [x] [0020-ai-ralph-loop-recursion](tasks/completed/0020-ai-ralph-loop-recursion.md) — Autonomous recursion with completion markers
- [x] [0021-ops-workflow-toml-converter](tasks/completed/0021-ops-workflow-toml-converter.md) — Markdown to TOML converter for Gemini CLI commands
- [x] [0012-ops-reorganize-docs-directory](tasks/completed/0012-ops-reorganize-docs-directory.md) — Classify, move, archive, rename docs

- [x] [0013-ops-install-script-ux](tasks/completed/0013-ops-install-script-ux.md) — Symlink handling, conflict detection, user prompts
- [x] [0015-ops-update-tasklist-from-audit](tasks/completed/0015-ops-update-tasklist-from-audit.md) — All core tasks tracked and verified
- [x] [0017-ops-update-vcs-rules](tasks/completed/0017-ops-update-vcs-rules.md) — Consolidate VCS rules, remove Mothership-specific rules
- [ ] [0024-ai-agent-reasoning-bdi](tasks/0024-ai-agent-reasoning-bdi.md) — BDI paradigm research
- [ ] [0027-ops-skill-decision-trees](tasks/0027-ops-skill-decision-trees.md) — Dynamic skill selection design
- [ ] [0028-ops-memory-lifecycle-updates](tasks/0028-ops-memory-lifecycle-updates.md) — Standardized workflow memory rules
- [ ] [0029-ai-harvest-claude-templates](tasks/0029-ai-harvest-claude-templates.md) — Missing agent templates
- [ ] [0030-ai-harvest-omnara-monitoring](tasks/0030-ai-harvest-omnara-monitoring.md) — PTY session audit (Flight Recorder)
- [ ] [0031-ai-micode-mindmodel-context](tasks/0031-ai-micode-mindmodel-context.md) — Graph-based project continuity

## ✨ Padronização & Qualidade de Skills
- [x] [0170-ops-skill-reorganization](tasks/completed/0170-ops-skill-reorganization.md) — Reorganize 1237 skill folders to `type-subtype-nnnn-name` convention
- [x] [0180-ops-skill-metadata-standardization](tasks/completed/0180-ops-skill-metadata-standardization.md) — Standardize YAML frontmatter across all skills
- [x] [0190-ops-skill-consolidation](tasks/completed/0190-ops-skill-consolidation.md) — Merge redundant skills (Diagrams, News, Search)
- [x] [0200-dev-skill-localization](tasks/completed/0200-dev-skill-localization.md) — Translate non-English skills and metadata
- [x] [0210-sec-skill-integrity-fix](tasks/completed/0210-sec-skill-integrity-fix.md) — Repair or archive 82 invalid skills identified in audit

- [x] [0220-ops-skill-knowledge-base](tasks/completed/0220-ops-skill-knowledge-base.md) — Create script and workflow to parse, map, and synchronize all skills into memory MCPs

## 💡 Planejamento / Novos Itens (USER-NOTES)
- [x] [0037-ops-mcp-documentation-ingestion](tasks/completed/0037-ops-mcp-documentation-ingestion.md) — Create workflows to ingest and map comprehensive library/framework documentation into our memory systems.
- [x] [0038-ops-session-rule-discovery](tasks/completed/0038-ops-session-rule-discovery.md) — Workflow to scan session and discover new business rules or organizational changes.
- [x] [0039-ops-sdd-workflows-revision](tasks/completed/0039-ops-sdd-workflows-revision.md) — Revise, clarify, and strictly delineate the specific SDD workflows and their designated contexts.
- [x] [0040-ai-acp-a2a-orchestration-research](tasks/completed/0040-ai-acp-a2a-orchestration-research.md) — Research and define modern, optimal methods for orchestrating agents using ACP and A2A paradigms.
- [x] [0041-ops-task-enrichment-workflow](tasks/completed/0041-ops-task-enrichment-workflow.md) — Create a proactive workflow that enriches existing tasks by conducting supplementary research.
- [x] [0042-ops-skill-extraction-workflow](tasks/completed/0042-ops-skill-extraction-workflow.md) — Create a workflow to extract, analyze, and integrate agent skills from external GitHub repositories.

## 🔍 Verificação
- [x] [0016-ops-second-audit](tasks/completed/0016-ops-second-audit.md) — Second comprehensive audit pass

## 🔄 Tarefas Existentes (Pré-Auditoria)
- [/] [0001-ops-mcp-integrations](tasks/0001-ops-mcp-integrations.md) — Local MCPs integrated; Remote MCPs pending
- [x] [0002-ops-advanced-hooks](tasks/0002-ops-advanced-hooks.md) — Todo Continuation Enforcer scaffolded
- [/] [0003-ops-moltbot-memory](tasks/0003-ops-moltbot-memory.md) — In-Memoria integrated as persistent memory
- [x] [0004-ops-dedup-docs-docs](tasks/completed/0004-ops-dedup-docs-docs.md) — Completed via reorganization
- [x] [0005-ops-dedup-docs-analysis](tasks/completed/0005-ops-dedup-docs-analysis.md) — Completed via reorganization
- [x] [0006-ops-dedup-docs-knowledge](tasks/completed/0006-ops-dedup-docs-knowledge.md) — Completed via reorganization
- [x] [0007-ops-rename-overpowers-rebranding](tasks/completed/0007-ops-rename-overpowers-rebranding.md) — Complete rebranding cleanup
- [x] [0008-ops-feature-knowledge-mcp](tasks/completed/0008-feature-knowledge-mcp.md) — Knowledge MCP server functional in packages/knowledge-mcp

## ✅ Tarefas Concluídas
- [x] [0004-ops-dedup-docs-docs](tasks/completed/0004-ops-dedup-docs-docs.md)
- [x] [0005-ops-dedup-docs-analysis](tasks/completed/0005-ops-dedup-docs-analysis.md)
- [x] [0006-ops-dedup-docs-knowledge](tasks/completed/0006-ops-dedup-docs-knowledge.md)
- [x] [0007-ops-rename-overpowers-rebranding](tasks/completed/0007-ops-rename-overpowers-rebranding.md)
- [x] [0008-ops-feature-knowledge-mcp](tasks/completed/0008-feature-knowledge-mcp.md)
- [x] [0009-ops-rebuild-mcp-infrastructure](tasks/completed/0009-ops-rebuild-mcp-infrastructure.md)
- [x] [0010-ops-recreate-semgrep-skill](tasks/completed/0010-ops-recreate-semgrep-skill.md)
- [x] [0011-ops-reinstall-nlm-skill](tasks/completed/0011-ops-reinstall-nlm-skill.md)
- [x] [0012-ops-reorganize-docs-directory](tasks/completed/0012-ops-reorganize-docs-directory.md)
- [x] [0013-ops-install-script-ux](tasks/completed/0013-ops-install-script-ux.md)
- [x] [0014-ops-fix-antigravity-mcp-config](tasks/completed/0014-ops-fix-antigravity-mcp-config.md)
- [x] [0015-ops-update-tasklist-from-audit](tasks/completed/0015-ops-update-tasklist-from-audit.md)
- [x] [0016-ops-second-audit](tasks/completed/0016-ops-second-audit.md)
- [x] [0017-ops-update-vcs-rules](tasks/completed/0017-ops-update-vcs-rules.md)
- [x] [0018-ops-intent-classification](tasks/completed/0018-ops-intent-classification.md)
- [x] [0019-ops-feature-progressive-disclosure](tasks/completed/0019-ops-feature-progressive-disclosure.md)
- [x] [0020-ai-ralph-loop-recursion](tasks/completed/0020-ai-ralph-loop-recursion.md)
- [x] [0021-ops-workflow-toml-converter](tasks/completed/0021-ops-workflow-toml-converter.md)
- [x] [0170-ops-skill-reorganization](tasks/completed/0170-ops-skill-reorganization.md)
- [x] [0180-ops-skill-metadata-standardization](tasks/completed/0180-ops-skill-metadata-standardization.md)
- [x] [0190-ops-skill-consolidation](tasks/completed/0190-ops-skill-consolidation.md)
- [x] [0200-dev-skill-localization](tasks/completed/0200-dev-skill-localization.md)
- [x] [0210-sec-skill-integrity-fix](tasks/completed/0210-sec-skill-integrity-fix.md)
- [x] [0220-ops-skill-knowledge-base](tasks/completed/0220-ops-skill-knowledge-base.md)
- [ ] [0022-data-json-knowledge-graph](tasks/0022-data-json-knowledge-graph.md) - Migrate knowledge graph to JSON
- [ ] [0300-ops-skill-scripts-batch-001](tasks/0300-ops-skill-scripts-batch-001.md) — Analyze and deploy Helper Scripts for Batch 001
- [ ] [0300-ops-skill-scripts-batch-002](tasks/0300-ops-skill-scripts-batch-002.md) — Analyze and deploy Helper Scripts for Batch 002
- [ ] [0300-ops-skill-scripts-batch-003](tasks/0300-ops-skill-scripts-batch-003.md) — Analyze and deploy Helper Scripts for Batch 003
- [ ] [0300-ops-skill-scripts-batch-004](tasks/0300-ops-skill-scripts-batch-004.md) — Analyze and deploy Helper Scripts for Batch 004
- [/] [0300-ops-skill-scripts-batch-005](tasks/0300-ops-skill-scripts-batch-005.md) — Analyze and deploy Helper Scripts for Batch 005
- [ ] [0300-ops-skill-scripts-batch-006](tasks/0300-ops-skill-scripts-batch-006.md) — Analyze and deploy Helper Scripts for Batch 006
- [/] [0300-ops-skill-scripts-batch-007](tasks/0300-ops-skill-scripts-batch-007.md) — Analyze and deploy Helper Scripts for Batch 007
- [ ] [0300-ops-skill-scripts-batch-008](tasks/0300-ops-skill-scripts-batch-008.md) — Analyze and deploy Helper Scripts for Batch 008
- [ ] [0300-ops-skill-scripts-batch-009](tasks/0300-ops-skill-scripts-batch-009.md) — Analyze and deploy Helper Scripts for Batch 009
- [ ] [0300-ops-skill-scripts-batch-010](tasks/0300-ops-skill-scripts-batch-010.md) — Analyze and deploy Helper Scripts for Batch 010
- [ ] [0300-ops-skill-scripts-batch-011](tasks/0300-ops-skill-scripts-batch-011.md) — Analyze and deploy Helper Scripts for Batch 011
- [ ] [0300-ops-skill-scripts-batch-012](tasks/0300-ops-skill-scripts-batch-012.md) — Analyze and deploy Helper Scripts for Batch 012
- [ ] [0300-ops-skill-scripts-batch-013](tasks/0300-ops-skill-scripts-batch-013.md) — Analyze and deploy Helper Scripts for Batch 013
- [ ] [0300-ops-skill-scripts-batch-014](tasks/0300-ops-skill-scripts-batch-014.md) — Analyze and deploy Helper Scripts for Batch 014
- [/] [0300-ops-skill-scripts-batch-015](tasks/0300-ops-skill-scripts-batch-015.md) — Analyze and deploy Helper Scripts for Batch 015
- [ ] [0300-ops-skill-scripts-batch-016](tasks/0300-ops-skill-scripts-batch-016.md) — Analyze and deploy Helper Scripts for Batch 016
- [ ] [0300-ops-skill-scripts-batch-017](tasks/0300-ops-skill-scripts-batch-017.md) — Analyze and deploy Helper Scripts for Batch 017
- [ ] [0300-ops-skill-scripts-batch-018](tasks/0300-ops-skill-scripts-batch-018.md) — Analyze and deploy Helper Scripts for Batch 018
- [ ] [0300-ops-skill-scripts-batch-019](tasks/0300-ops-skill-scripts-batch-019.md) — Analyze and deploy Helper Scripts for Batch 019
- [ ] [0300-ops-skill-scripts-batch-020](tasks/0300-ops-skill-scripts-batch-020.md) — Analyze and deploy Helper Scripts for Batch 020
- [ ] [0300-ops-skill-scripts-batch-021](tasks/0300-ops-skill-scripts-batch-021.md) — Analyze and deploy Helper Scripts for Batch 021
- [ ] [0300-ops-skill-scripts-batch-022](tasks/0300-ops-skill-scripts-batch-022.md) — Analyze and deploy Helper Scripts for Batch 022
- [ ] [0300-ops-skill-scripts-batch-023](tasks/0300-ops-skill-scripts-batch-023.md) — Analyze and deploy Helper Scripts for Batch 023
- [ ] [0300-ops-skill-scripts-batch-024](tasks/0300-ops-skill-scripts-batch-024.md) — Analyze and deploy Helper Scripts for Batch 024
- [ ] [0300-ops-skill-scripts-batch-025](tasks/0300-ops-skill-scripts-batch-025.md) — Analyze and deploy Helper Scripts for Batch 025
- [ ] [0300-ops-skill-scripts-batch-026](tasks/0300-ops-skill-scripts-batch-026.md) — Analyze and deploy Helper Scripts for Batch 026
- [ ] [0300-ops-skill-scripts-batch-027](tasks/0300-ops-skill-scripts-batch-027.md) — Analyze and deploy Helper Scripts for Batch 027
- [ ] [0300-ops-skill-scripts-batch-028](tasks/0300-ops-skill-scripts-batch-028.md) — Analyze and deploy Helper Scripts for Batch 028
- [ ] [0300-ops-skill-scripts-batch-029](tasks/0300-ops-skill-scripts-batch-029.md) — Analyze and deploy Helper Scripts for Batch 029
- [ ] [0300-ops-skill-scripts-batch-030](tasks/0300-ops-skill-scripts-batch-030.md) — Analyze and deploy Helper Scripts for Batch 030
- [ ] [0300-ops-skill-scripts-batch-031](tasks/0300-ops-skill-scripts-batch-031.md) — Analyze and deploy Helper Scripts for Batch 031
- [ ] [0300-ops-skill-scripts-batch-032](tasks/0300-ops-skill-scripts-batch-032.md) — Analyze and deploy Helper Scripts for Batch 032
- [ ] [0300-ops-skill-scripts-batch-033](tasks/0300-ops-skill-scripts-batch-033.md) — Analyze and deploy Helper Scripts for Batch 033
- [ ] [0300-ops-skill-scripts-batch-034](tasks/0300-ops-skill-scripts-batch-034.md) — Analyze and deploy Helper Scripts for Batch 034
- [ ] [0300-ops-skill-scripts-batch-035](tasks/0300-ops-skill-scripts-batch-035.md) — Analyze and deploy Helper Scripts for Batch 035
- [ ] [0300-ops-skill-scripts-batch-036](tasks/0300-ops-skill-scripts-batch-036.md) — Analyze and deploy Helper Scripts for Batch 036
- [ ] [0300-ops-skill-scripts-batch-037](tasks/0300-ops-skill-scripts-batch-037.md) — Analyze and deploy Helper Scripts for Batch 037
- [ ] [0300-ops-skill-scripts-batch-038](tasks/0300-ops-skill-scripts-batch-038.md) — Analyze and deploy Helper Scripts for Batch 038
- [ ] [0300-ops-skill-scripts-batch-039](tasks/0300-ops-skill-scripts-batch-039.md) — Analyze and deploy Helper Scripts for Batch 039
- [ ] [0300-ops-skill-scripts-batch-040](tasks/0300-ops-skill-scripts-batch-040.md) — Analyze and deploy Helper Scripts for Batch 040
- [ ] [0300-ops-skill-scripts-batch-041](tasks/0300-ops-skill-scripts-batch-041.md) — Analyze and deploy Helper Scripts for Batch 041
- [ ] [0300-ops-skill-scripts-batch-042](tasks/0300-ops-skill-scripts-batch-042.md) — Analyze and deploy Helper Scripts for Batch 042
- [ ] [0300-ops-skill-scripts-batch-043](tasks/0300-ops-skill-scripts-batch-043.md) — Analyze and deploy Helper Scripts for Batch 043
- [ ] [0300-ops-skill-scripts-batch-044](tasks/0300-ops-skill-scripts-batch-044.md) — Analyze and deploy Helper Scripts for Batch 044
- [ ] [0300-ops-skill-scripts-batch-045](tasks/0300-ops-skill-scripts-batch-045.md) — Analyze and deploy Helper Scripts for Batch 045
- [ ] [0300-ops-skill-scripts-batch-046](tasks/0300-ops-skill-scripts-batch-046.md) — Analyze and deploy Helper Scripts for Batch 046
- [ ] [0300-ops-skill-scripts-batch-047](tasks/0300-ops-skill-scripts-batch-047.md) — Analyze and deploy Helper Scripts for Batch 047
- [ ] [0300-ops-skill-scripts-batch-048](tasks/0300-ops-skill-scripts-batch-048.md) — Analyze and deploy Helper Scripts for Batch 048
- [ ] [0300-ops-skill-scripts-batch-049](tasks/0300-ops-skill-scripts-batch-049.md) — Analyze and deploy Helper Scripts for Batch 049
- [ ] [0300-ops-skill-scripts-batch-050](tasks/0300-ops-skill-scripts-batch-050.md) — Analyze and deploy Helper Scripts for Batch 050
- [ ] [0300-ops-skill-scripts-batch-051](tasks/0300-ops-skill-scripts-batch-051.md) — Analyze and deploy Helper Scripts for Batch 051
- [ ] [0300-ops-skill-scripts-batch-052](tasks/0300-ops-skill-scripts-batch-052.md) — Analyze and deploy Helper Scripts for Batch 052
- [ ] [0300-ops-skill-scripts-batch-053](tasks/0300-ops-skill-scripts-batch-053.md) — Analyze and deploy Helper Scripts for Batch 053
- [ ] [0300-ops-skill-scripts-batch-054](tasks/0300-ops-skill-scripts-batch-054.md) — Analyze and deploy Helper Scripts for Batch 054
- [ ] [0300-ops-skill-scripts-batch-055](tasks/0300-ops-skill-scripts-batch-055.md) — Analyze and deploy Helper Scripts for Batch 055
- [ ] [0300-ops-skill-scripts-batch-056](tasks/0300-ops-skill-scripts-batch-056.md) — Analyze and deploy Helper Scripts for Batch 056
- [ ] [0300-ops-skill-scripts-batch-057](tasks/0300-ops-skill-scripts-batch-057.md) — Analyze and deploy Helper Scripts for Batch 057
- [ ] [0300-ops-skill-scripts-batch-058](tasks/0300-ops-skill-scripts-batch-058.md) — Analyze and deploy Helper Scripts for Batch 058
- [ ] [0300-ops-skill-scripts-batch-059](tasks/0300-ops-skill-scripts-batch-059.md) — Analyze and deploy Helper Scripts for Batch 059