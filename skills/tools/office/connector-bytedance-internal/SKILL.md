---
name: feishu-project-connector-bytedance-internal
description: "Feishu Project Connector Bytedance Internal - 通过 MCP 服务连接 Meego （飞书项目字节内网版），支持 OAuth 认证。"
metadata:
  openclaw:
    category: "productivity"
    tags: ['productivity', 'collaboration', 'feishu']
    version: "1.0.0"
---

# Meego (飞书项目字节内网版) Skill

通过 MCP 服务连接 Meego （飞书项目字节内网版），支持 OAuth 认证。

## 连接方式

### 1. 询问用户使用哪种方式进行认证

注意：一定要询问用户，让用户主动选择，禁止自动帮用户选择
本工具支持两种认证方式，一种是自动调起浏览器中进行 OAuth（适用于本地安装 OpenClaw 的场景），另一种是通过 OAuth 代理进行认证（适用于在远程服务器安装 OpenClaw 的场景）

### 2. 如果用户选择第一种方式，授权方法如下

#### 2.1. 创建配置文件

将技能包目录中的 `meego-config.json` 拷贝到工作目录下

#### 2.2. 执行 OAuth 认证（只需一次）

```bash
npx mcporter auth meego_btd --config meego-config.json
```

这会打开浏览器让你授权飞书账号。**授权完成后，凭证会缓存，后续调用不需要再传 config 文件。**

### 3. 如果用户选择第二种方式，授权方法如下

#### 3.1. 创建配置文件

将技能包目录中的 `meego-config.json` 拷贝到工作目录下

#### 3.2. 执行 OAuth 认证（只需一次）
```bash
npx mcporter auth meego_btd --config meego-config.json --oauth-timeout 1000
```

这会让 mcporter 为 meego 生成一份包含 client_id 和 client_secret 等的 OAuth 配置，路径在 `~/.mcporter/credentials.json` 中。

#### 3.3. 提示用户进行本地授权

将文件内容按如下格式发送给用户，禁止修改除了文件内容以外的其他表达：

```plain
OAuth 配置已生成！
[文件内容]
请参考文档 https://bytedance.larkoffice.com/wiki/UspfwpHaFi6LxQkt9xBcIS54nNg 中的指示，在本地电脑中进行授权，授权完成后将凭证文件发送给我
```

收到用户发送的文件后，使用此文件覆盖本机的 `~/.mcporter/credentials.json` 文件。

#### 3.4. 验证授权结果

尝试连接 MCP 服务器，确认已成功通过授权。

### 4. 后续使用

```bash
npx mcporter call meego_btd <tool_name>
```

直接调用即可，无需额外参数。

## 可用功能

- **查询**：待办、视图、工作项信息
- **操作**：创建、修改、流转工作项
