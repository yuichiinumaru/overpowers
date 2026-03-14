---
name: gitlab-private
description: "通过 OAuth 授权访问私有 GitLab 仓库，支持多用户授权，加密存储"
metadata:
  openclaw:
    category: "development"
    tags: ['development', 'git', 'version-control']
    version: "1.0.0"
---

# GitLab Private v0.5.0

通过 OAuth 授权访问私有 GitLab 仓库，支持多用户授权，敏感信息加密存储。

## 功能

- **多用户授权**：每个用户独立授权，独立 token
- **加密存储**：token 以加密形式存储，安全可靠
- **自动识别**：用户发授权链接自动提取 code
- 列出用户仓库
- 读取仓库文件
- 查看最后一次合并

## 群里使用流程

### 0. 首次配置（管理员）

需要先配置 OAuth 应用信息：
```bash
node index.js config <Application ID> <Secret> [GitLab URL]
```

### 1. 用户发 GitLab 仓库链接

机器人回复授权链接：
```
请按以下步骤授权：
1. 打开浏览器访问授权链接
2. 授权后浏览器跳转到 http://localhost/callback?code=xxx
3. 把跳转后的完整链接发给我
```

### 2. 用户发授权链接

用户把完整链接发给机器人（如：`http://localhost/callback?code=xxx`）

机器人自动：
1. 提取 code
2. 换取 token
3. **加密保存**（绑定用户ID）

### 3. 后续使用

同一个人后续发仓库链接，**使用已保存的 token 直接读取**

**注意**：敏感信息（client_id, client_secret, token）只保存在本地，不会上传到 clawhub。

## 命令行使用

```bash
# 配置 OAuth 应用
node index.js config <Application ID> <Secret>

# 生成授权链接
node index.js auth-url

# 处理授权（核心）
node index.js handle <用户ID> <授权链接或code>

# 使用用户 token 执行命令
node index.js use <用户ID> list
node index.js use <用户ID> project <关键词>
node index.js use <用户ID> merge <项目ID> [分支]

# 列出已授权用户
node index.js users
```

## 安全特性

- **加密存储**：token 使用 AES-256-CBC 加密
- **独立密钥**：可通过环境变量 GITLAB_ENCRYPT_KEY 设置密钥
- **按用户隔离**：不同用户 token 分开存储

## 配置文件

| 文件 | 说明 |
|------|------|
| `config/oauth.json` | OAuth 应用配置 |
| `config/users.enc` | 加密的用户 token |

## 环境变量（必须设置）

- `GITLAB_URL`: GitLab 地址
- `GITLAB_ENCRYPT_KEY`: 加密密钥（**必须设置**，至少32个字符）

**重要**：首次使用前必须设置环境变量：
```bash
export GITLAB_ENCRYPT_KEY=你的密钥（至少32个字符）
export GITLAB_URL=http://gitlab.你的公司.com
```
