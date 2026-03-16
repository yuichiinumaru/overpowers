---
name: content-media-openstoryline-video-editor
description: "Start local MCP/Web services for OpenStoryline, manage sessions, and perform video editing via natural language instructions. Supports multi-turn editing and video rendering."
tags: ["video-editing", "ai", "content-creation", "multimodal", "openstoryline"]
version: 1.0.0
---

# OpenStoryline Usage Skill

你负责在“已安装完成”的前提下，执行 OpenStoryline 的实际剪辑流程。
OpenStoryline 是一个剪辑 Agent，用户可使用自己的素材，通过自然语言对话的方式剪辑视频。内置素材搜索、内容理解、生成字幕、文字转语音等功能，用户可以多次提出具体的剪辑/修改意见。

目标是：使用已有脚本，稳定地完成一次从启动服务到产出视频的闭环；并且支持在同一个 `session_id` 上继续对话、二次编辑、重新生成新视频。

## Scope

此技能只处理“使用与剪辑”：

1. 检查并修改 `config.toml` 的必要字段。
2. 启动 MCP server。
3. 启动 `uvicorn agent_fastapi:app`。
4. 创建 session 并发送剪辑请求.
5. 等待并验证输出视频产物.
6. 在同一个 `session_id` 上继续对话，执行二次编辑.
7. 验证二次编辑后是否生成了新的 `output_*.mp4`.

## Core Rules

1. 默认只监听 `127.0.0.1`，不要主动暴露到局域网。
2. 优先复用现有脚本，不要重复造轮子。
3. 长驻服务（MCP / Web）必须按“长驻进程”方式启动，并持续观察日志。
4. 每次完成任务后，都要向用户明确返回 `session_id` 和最终视频路径。

## Standard Workflow

### 1) 配置
设置 `llm` 和 `vlm` 的 `model`, `base_url`, `api_key`。

### 2) 启动服务
- 启动 MCP Server: `python -m open_storyline.mcp.server`
- 启动 Web 服务: `uvicorn agent_fastapi:app --host 127.0.0.1 --port 8005`

### 3) 剪辑流程
- 创建会话: `curl -X POST "http://127.0.0.1:8005/api/sessions"`
- 上传素材: `curl -X POST "http://127.0.0.1:8005/api/sessions/{session_id}/media" -F "files=@/path/to/media"`
- 开始剪辑: 使用 bridge 脚本发送 prompt。
- 观察进度: 查看 Web 服务日志节点（filter_clips, render_video 等）。
- 验证产物: 检查 `output_*.mp4` 是否生成。
