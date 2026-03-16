---
name: agent-task-logger
description: "Agent Task Logger - A real-time task logging system similar to Tomcat's catalina.out, **automatically detects Agent workspaces** for recording and displaying the progress of Agent task execution."
metadata:
  openclaw:
    category: "agent"
    tags: ['agent', 'automation', 'monitoring']
    version: "1.0.0"
---

# Agent Task Logger - Agent Task Logging System

A real-time task logging system similar to Tomcat's `catalina.out`, **automatically detecting the Agent workspace** for recording and displaying the progress of Agent task execution.

## 🚀 Quick Start

### 1. Initialize Logging System (Auto-detect Workspace)
```
Initialize logging system
```

### 2. Initialize Logging System (Manually Specify Workspace)
```
Initialize logging system workspace=/path/to/workspace
```

### 2. Record Task Start
```
Record task start task-id=task-001 task-name="Stop Tomcat 8" estimated-time=5s
```

### 3. Record Execution Command
```
Record execution command task-id=task-001 command="cd /path && ./shutdown.sh"
```

### 4. Record Task Status
```
Record task status task-id=task-001 status="Success" actual-time=3.5s
```

### 5. View Real-time Logs
```bash
tail -f /Users/openclaw/.openclaw/workspace/logs/agent-task.log
```

## 📋 Parameter Description

### Initialize Logging System
| Parameter | Required | Default Value | Description |
|------|------|--------|------|
| `workspace` | ❌ | Auto-detect | Workspace root directory (optional, auto-detected) |
| `log-dir` | ❌ | `logs` | Log directory (relative to workspace) |
| `log-file` | ❌ | `agent-task.log` | Log file name |

### Workspace Auto-detection

The Skill automatically detects the Agent's workspace location. Detection order:

1. `WORKSPACE` environment variable
2. `OPENCLAW_WORKSPACE` environment variable
3. Parent directory of the script's location
4. `~/.openclaw/workspace`
5. Current directory

**No manual workspace specification needed, ready to use out of the box!**

### Record Task Start
| Parameter | Required | Description |
|------|------|------|
| `task-id` | ✅ | Unique task identifier |
| `task-name` | ✅ | Task description |
| `estimated-time` | ❌ | Estimated processing time |

### Record Execution Command
| Parameter | Required | Description |
|------|------|------|
| `task-id` | ✅ | Associated task ID |
| `command` | ✅ | Executed shell command |

### Record Task Status
| Parameter | Required | Description |
|------|------|------|
| `task-id` | ✅ | Associated task ID |
| `status` | ✅ | Task status (Success/Failure/Pending) |
| `actual-time` | ❌ | Actual processing time |

## 💡 Trigger Words

- Initialize logging system
- Record task start
- Record execution command
- Record task status
- Record task completion
- Record error information
- View task logs

## 📝 Log Format

Referencing Tomcat catalina.out format, displayed in Chinese:

```
04-3 月 -2026 17:38:00.000 INFO [agent-task-1] com.openclaw.agent.TaskExecutor.execute 任务：停止 Tomcat 8
04-3 月 -2026 17:38:00.100 INFO [agent-task-1] com.openclaw.agent.TaskExecutor.execute 执行命令：cd /path && ./shutdown.sh
04-3 月 -2026 17:38:03.500 INFO [agent-task-1] com.openclaw.agent.TaskExecutor.execute 状态：Tomcat 8 关闭完成
04-3 月 -2026 17:38:03.600 INFO [agent-task-1] com.openclaw.agent.TaskExecutor.execute 预估时间：5 秒 | 实际时间：3.5 秒
04-3 月 -2026 17:38:03.700 INFO [agent-task-1] com.openclaw.agent.TaskExecutor.execute 结果：成功
```

## 🔧 Usage Examples

### Example 1: Complete Task Flow (Auto-detect Workspace)

```bash
# 1. Initialize (Auto-detect Workspace)
Initialize logging system

# 2. Start Task
Record task start task-id=deploy-001 task-name="Deploy Java Project" estimated-time=60s

# 3. Execute Command
Record execution command task-id=deploy-001 command="mvn clean package"

# 4. Record Status
Record task status task-id=deploy-001 status="Success" actual-time=45s

# 5. Complete Task
Record task completion task-id=deploy-001
```

### Example 2: Parallel Tasks

```bash
# Task 1: Compile Backend
Record task start task-id=backend-compile task-name="Compile Backend Project" estimated-time=30s
Record execution command task-id=backend-compile command="mvn compile"
Record task status task-id=backend-compile status="Success" actual-time=25s

# Task 2: Build Frontend
Record task start task-id=frontend-build task-name="Build Frontend Project" estimated-time=45s
Record execution command task-id=frontend-build command="npm run build"
Record task status task-id=frontend-build status="Success" actual-time=40s
```

### Example 3: Error Handling

```bash
Record task start task-id=deploy-app task-name="Deploy Application" estimated-time=30s
Record execution command task-id=deploy-app command="./deploy.sh"
Record error information task-id=deploy-app error="Permission denied, sudo required"
Record task status task-id=deploy-app status="Failure" actual-time=5s
```

## 📊 Log Levels

| Level | Description | Use Case |
|------|------|---------|
| `INFO` | General information | Task start, command execution, status updates |
| `WARN` | Warning information | Non-critical errors, performance warnings |
| `ERROR` | Error information | Task failure, exceptions |
| `DEBUG` | Debug information | Detailed debug output |

## 🛠️ Advanced Features

### View Task Statistics
```bash
# View all task statuses
grep "结果：" /Users/openclaw/.openclaw/workspace/logs/agent-task.log

# View failed tasks
grep "结果：失败" /Users/openclaw/.openclaw/workspace/logs/agent-task.log

# View task durations
grep "实际时间：" /Users/openclaw/.openclaw/workspace/logs/agent-task.log
```

### Log Rotation
```bash
# Archive logs by date
mv /Users/openclaw/.openclaw/workspace/logs/agent-task.log \
   /Users/openclaw/.openclaw/workspace/logs/agent-task-$(date +%Y%m%d).log
```

## ⚠️ Notes

1. **Log File Permissions**: Ensure the log directory is writable.
2. **Log File Size**: It is recommended to archive logs periodically to prevent excessively large files.
3. **Concurrent Writes**: Supports concurrent logging from multiple tasks.
4. **Time Format**: Use 24-hour format, precise to milliseconds.

## 📁 File Structure

```
workspace/
├── logs/
│   ├── agent-task.log          # Main log file
│   ├── agent-task-20260304.log # Archived log
│   └── ...
└── skills/
    └── agent-task-logger/
        ├── SKILL.md            # Skill description
        └── scripts/
            └── logger.sh       # Logging utility script
```

## 🔄 Changelog

- v1.0 - Initial version, supports basic task logging
- v1.1 - Added Chinese language support
- v1.2 - Added task statistics feature
