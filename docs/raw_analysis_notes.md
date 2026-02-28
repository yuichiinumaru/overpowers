# Raw Analysis Notes - Antigravity Extraction

## Target Repositories
1. `antigravity-skills`: **High Value**. Contains 20 unique skills not present in Overpowers.
2. `andy-universal-agent-rules`: **Medium Value**. Contains Python scripts for knowledge management (`save-knowledge.py`, etc.).
3. `sanity-gravity`: **Low Priority**. Container/Sandbox tools.
4. `AntigravityManager` & `antigravity-account-switcher`: **Low Priority**. Electron Apps.
5. `ellfarnaz-antigravity-agent-os`: **Low Priority**. Placeholder/Docs.

## Unique Skills Identified
The following 20 skills are unique to `antigravity-skills` and should be extracted:
1. `advanced-evaluation`
2. `bdi-mental-states`
3. `context-compression`
4. `context-degradation`
5. `context-fundamentals`
6. `context-optimization`
7. `evaluation`
8. `filesystem-context`
9. `hosted-agents`
10. `json-canvas`
11. `memory-systems`
12. `multi-agent-patterns`
13. `notebooklm`
14. `obsidian-bases`
15. `obsidian-markdown`
16. `planning-with-files`
17. `project-development`
18. `remotion`
19. `tool-design`
20. `using-overpowers`

## Knowledge Scripts Identified
Found in `andy-universal-agent-rules/.agent/scripts/`:
- `backup-memory.py`
- `search-knowledge.py`
- `save-knowledge.py`
- `validate-index.py`
- `detect-environment.py`

## Strategy
- **Skills**: Copy unique skills to `skills/`. Rename `using-overpowers` to `using-overpowers` (if applicable) or adapt it.
- **Scripts**: Extract knowledge scripts to `scripts/knowledge/` and create wrappers or aliases if needed.
## Deep Re-Audit Findings
### AntigravityManager
references/external_source/AntigravityManager/src
references/external_source/AntigravityManager/src/constants
references/external_source/AntigravityManager/src/constants/index.ts
references/external_source/AntigravityManager/src/App.tsx
references/external_source/AntigravityManager/src/routes
references/external_source/AntigravityManager/src/routes/proxy.tsx
references/external_source/AntigravityManager/src/routes/settings.tsx
references/external_source/AntigravityManager/src/routes/__root.tsx
references/external_source/AntigravityManager/src/routes/index.tsx
references/external_source/AntigravityManager/src/preload.ts
references/external_source/AntigravityManager/src/routeTree.gen.ts
references/external_source/AntigravityManager/src/hooks
references/external_source/AntigravityManager/src/hooks/useAppConfig.ts
references/external_source/AntigravityManager/src/hooks/useCloudAccounts.ts
references/external_source/AntigravityManager/src/utils
references/external_source/AntigravityManager/src/utils/security.ts
references/external_source/AntigravityManager/src/utils/logger.ts
references/external_source/AntigravityManager/src/utils/routes.ts
references/external_source/AntigravityManager/src/utils/protobuf.ts
references/external_source/AntigravityManager/src/utils/autoStart.ts
references/external_source/AntigravityManager/src/utils/paths.ts
references/external_source/AntigravityManager/src/utils/errorMessages.ts
references/external_source/AntigravityManager/src/components
references/external_source/AntigravityManager/src/components/navigation-menu.tsx
references/external_source/AntigravityManager/src/components/CloudAccountList.tsx
references/external_source/AntigravityManager/src/components/AccountCard.tsx
references/external_source/AntigravityManager/src/components/CloudAccountCard.tsx
references/external_source/AntigravityManager/src/components/drag-window-region.tsx
references/external_source/AntigravityManager/src/components/toggle-theme.tsx
references/external_source/AntigravityManager/src/components/theme-provider.tsx
references/external_source/AntigravityManager/src/components/ui
references/external_source/AntigravityManager/src/components/StatusBar.tsx
references/external_source/AntigravityManager/src/assets
references/external_source/AntigravityManager/src/assets/icon.png
references/external_source/AntigravityManager/src/assets/tray.png
references/external_source/AntigravityManager/src/assets/fonts
references/external_source/AntigravityManager/src/types
references/external_source/AntigravityManager/src/types/theme-mode.ts
references/external_source/AntigravityManager/src/types/cloudAccount.ts
references/external_source/AntigravityManager/src/types/account.ts
references/external_source/AntigravityManager/src/types/config.ts
references/external_source/AntigravityManager/src/main.ts
references/external_source/AntigravityManager/src/instrument.ts
references/external_source/AntigravityManager/src/ipc
references/external_source/AntigravityManager/src/ipc/context.ts
references/external_source/AntigravityManager/src/ipc/manager.ts
references/external_source/AntigravityManager/src/ipc/config
references/external_source/AntigravityManager/src/ipc/router.ts
references/external_source/AntigravityManager/src/ipc/window
references/external_source/AntigravityManager/src/ipc/cloud
references/external_source/AntigravityManager/src/ipc/database
references/external_source/AntigravityManager/src/ipc/handler.ts
references/external_source/AntigravityManager/src/ipc/gateway
references/external_source/AntigravityManager/src/ipc/account
references/external_source/AntigravityManager/src/ipc/tray
references/external_source/AntigravityManager/src/ipc/theme
references/external_source/AntigravityManager/src/ipc/system
references/external_source/AntigravityManager/src/ipc/process
references/external_source/AntigravityManager/src/ipc/app
references/external_source/AntigravityManager/src/renderer.ts
references/external_source/AntigravityManager/src/types.d.ts
references/external_source/AntigravityManager/src/server
references/external_source/AntigravityManager/src/server/main.ts
references/external_source/AntigravityManager/src/server/server-config.ts
references/external_source/AntigravityManager/src/server/modules
references/external_source/AntigravityManager/src/server/app.module.ts
references/external_source/AntigravityManager/src/tests
references/external_source/AntigravityManager/src/tests/e2e
references/external_source/AntigravityManager/src/tests/AntigravityCoreFeatures.test.ts
references/external_source/AntigravityManager/src/tests/unit
references/external_source/AntigravityManager/src/mocks
references/external_source/AntigravityManager/src/mocks/empty.ts
references/external_source/AntigravityManager/src/mocks/nestjs-microservices
references/external_source/AntigravityManager/src/mocks/nestjs-websockets
references/external_source/AntigravityManager/src/styles
references/external_source/AntigravityManager/src/styles/global.css
references/external_source/AntigravityManager/src/layouts
references/external_source/AntigravityManager/src/layouts/MainLayout.tsx
references/external_source/AntigravityManager/src/lib
references/external_source/AntigravityManager/src/lib/utils.ts
references/external_source/AntigravityManager/src/lib/antigravity
references/external_source/AntigravityManager/src/actions
references/external_source/AntigravityManager/src/actions/cloud.ts
references/external_source/AntigravityManager/src/actions/account.ts
references/external_source/AntigravityManager/src/actions/theme.ts
references/external_source/AntigravityManager/src/actions/window.ts
references/external_source/AntigravityManager/src/actions/language.ts
references/external_source/AntigravityManager/src/actions/process.ts
references/external_source/AntigravityManager/src/actions/app.ts
references/external_source/AntigravityManager/src/actions/system.ts
references/external_source/AntigravityManager/src/actions/database.ts
references/external_source/AntigravityManager/src/services
references/external_source/AntigravityManager/src/services/AutoSwitchService.ts
references/external_source/AntigravityManager/src/services/CloudMonitorService.ts
references/external_source/AntigravityManager/src/services/GoogleAPIService.ts
references/external_source/AntigravityManager/src/localization
references/external_source/AntigravityManager/src/localization/i18n.ts
### antigravity-tools-linux
references/external_source/antigravity-tools-linux/scripts
references/external_source/antigravity-tools-linux/scripts/antigravity_get_user_status.sh
references/external_source/antigravity-tools-linux/scripts/antigravity_check_quota.py
### antigravity-skills (Leftovers)
advanced-evaluation
algorithmic-art
bdi-mental-states
brainstorming
brand-guidelines
canvas-design
context-compression
context-degradation
context-fundamentals
context-optimization
dispatching-parallel-agents
doc-coauthoring
docx
evaluation
executing-plans
filesystem-context
finishing-a-development-branch
frontend-design
hosted-agents
internal-comms
json-canvas
mcp-builder
memory-systems
multi-agent-patterns
notebooklm
obsidian-bases
obsidian-markdown
pdf
planning-with-files
pptx
project-development
receiving-code-review
remotion
requesting-code-review
skill-creator
slack-gif-creator
subagent-driven-development
systematic-debugging
test-driven-development
theme-factory
tool-design
ui-ux-pro-max
using-git-worktrees
using-overpowers
verification-before-completion
web-artifacts-builder
webapp-testing
writing-plans
writing-skills
xlsx
