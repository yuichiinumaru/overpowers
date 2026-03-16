---
name: ops-auth-codex-sweep-cliproxy
description: High-concurrency authentication scanning and cleanup for Codex credentials via CLI Proxy Management API. Identifies 401s and quota-exhausted accounts.
tags: [ops, auth, codex, scanner, cliproxy]
version: 1.0.0
---

# 技能说明 (Skill Description)

此技能用于：

1. 通过 **CLI Proxy Management API 的认证文件接口** 获取授权（`/v0/management/auth-files`）
2. 使用 **管理端 API Call 能力**（`/v0/management/api-call` + `auth_index + $TOKEN$`）探测每个 Codex 授权状态（对齐 CLI Proxy 的刷新/代理链路）
3. 识别 401/失效凭证并在用户明确要求时清理

## 交互要求（必须）

在每次准备执行扫描前，必须先主动向用户询问并确认：

- `base_url`（CLI Proxy 管理端地址）
- `management_key`（管理密钥）

如果用户未提供这两个参数，禁止开始扫描；应先提示用户补全。

## 安全提示（必须阅读）
... (rest of content)
