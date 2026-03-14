---
name: vetmew-consultation
description: "专业宠物（猫、狗及异宠）多轮医疗问诊。基于 VetMew 3.0 API 提供症状分析与诊断建议。"
metadata:
  openclaw:
    category: "utility"
    tags: []
    version: "1.0.0"
---

# VetMew 宠物问诊 Skill

## 简介
这是一个接入了 VetMew 开放平台 (VetMew Open Platform) 的专业宠物问诊技能。它能够处理复杂的宠物档案（涵盖犬、猫及龙猫、豚鼠等异宠），并通过 HMAC-SHA256 安全认证调用深度学习模型，为宠物提供专业的医疗咨询建议。

## Setup (Automated / Environment Priority)

本技能优先支持通过环境变量进行自动化配置。

### 1. 自动化环境 (OpenClaw / Agent 框架)
在 OpenClaw 等环境下，技能已通过元数据声明了 `VETMEW_AUTH_TOKEN` 的需求。**您只需在平台的技能设置界面输入凭据即可**，系统会自动将其注入运行环境。

- **凭据格式**: `API_KEY:API_SECRET` (中间以冒号分隔)。

### 2. 运行需求
- **Python**: 需要 3.12 或更高版本。
- **依赖安装**: `pip install -r requirements.txt` (自动化环境下通常由平台完成)。

> 若您需要在本地开发环境手动配置，请参考文档末尾的 [附录：手动凭据配置](#appendix-manual-credential-setup)。

## Usage

> **注意**：执行以下脚本前，请确保当前工作目录 (CWD) 为脚本所在的根目录。

### 1. 宠物医疗问诊
`python3 scripts/consultation.py --name <name> --breed <breed> --pet_type <pet_type> --birth <YYYY-MM-DD> --gender <1|2> --fertility <1|2> [--msg <question>] [--image <base64>] [--image_url <url>] [--image_type <1-6>] [--conversation_id <id>] [--thinking]`

### 2. 养宠知识问答 (轻量)
`python3 scripts/free_chat.py --msg <question> [--online] [--conversation_id <id>]`

### 3. 异宠医疗问诊
`python3 scripts/exotic_consultation.py --name <name> --breed <breed> --pet_type 3 --gender <1|2> --msg <question> [--conversation_id <id>] [--thinking]`

## Input (输入参数)

### 1. 医疗问诊参数 (仅适用于 `consultation.py`)
- `--name`: **宠物昵称** (String)。宠物在家庭中的常用名。
- `--breed`: **品种名称** (String)。必须是标准中文品种名，如“金毛”、“布偶猫”。
- `--pet_type`: **宠物类型** (String)。"1" 代表猫，"2" 代表狗。必须与品种所属物种一致。
- `--birth`: **生日** (YYYY-MM-DD)。用于计算宠物的生理阶段。
- `--gender`: **性别** (Integer)。1 为公，2 为母。
- `--fertility`: **绝育情况** (Integer)。1 为未绝育，2 为已绝育。
- `--msg`: **用户提问/症状描述** (String)。当提供图片时，此参数可选。
- `--image`: **图片 Base64 数据** (String)。去除头部的 Base64 编码字符串。
- `--image_url`: **图片 URL** (String)。图片的公网访问链接。
- `--image_type`: **视觉分析类型** (Integer)。
    - **1**: 情绪分析
    - **2**: 呕吐物分析
    - **3**: 粪便分析
    - **4**: 尿液分析
    - **5**: 皮肤分析
    - **6**: 耳道分析
- `--thinking`: **深度思考开关** (Flag)。开启后 API 会返回更详尽的推理逻辑（Deep Thinking）。

### 2. 异宠问诊参数 (仅适用于 `exotic_consultation.py`)
- `--name`: **宠物昵称** (String)。
- `--breed`: **品种名称** (String)。如“龙猫”、“豚鼠”、“松鼠”。
- `--pet_type`: **宠物类型** (String)。必须固定为 "3"。
- `--gender`: **性别** (Integer)。1 为公，2 为母。
- `--thinking`: **深度思考开关** (Flag)。

### 3. 知识问答参数 (仅适用于 `free_chat.py`)
- `--msg`: **用户提问** (String)。长度上限 200 字符。
- `--online`: **联网搜索开关** (Flag)。开启后 AI 会获取最新联网资讯进行回答。

### 3. 通用交互信息
- `--msg`: **用户提问/症状描述** (String)。请尽可能详细描述宠物的精神、饮食、排泄等异常表现。
- `--conversation_id`: **会话 ID** (Optional)。在多轮对话中，Agent 应自动提取并传递此 ID 以维持上下文。**注意：必须确保传入的 ID 与当前触发的脚本路径（医疗 vs 问答）一致。**

## Steps (工作流程)

1. **意图识别**: 当用户表达出对宠物健康的担忧或寻求专业建议时，触发此技能。
2. **槽位映射 (Session Slotting)**: Agent **必须** 维护三个独立的槽位以隔离会话。**在 OpenClaw 中，请将其持久化到对应的变量中**：
    - `VETMEW_MEDICAL_SESSION`: 存储来自 `consultation.py` 的 ID。
    - `VETMEW_EXOTIC_SESSION`: 存储来自 `exotic_consultation.py` 的 ID。
    - `VETMEW_CHAT_SESSION`: 存储来自 `free_chat.py` 的 ID。
3. **参数收集**: Agent 检查必选参数。如果用户未提及品种或年龄（针对犬猫），Agent 必须主动发起追问。
4. **运行环境就绪**: 确保已按照 `metadata.openclaw.install` 规格安装依赖，并正确获取环境变量。
5. **流式消费**: 实时解析来自 VetMew 的 SSE 数据块，提取 `msg` 内容并即时向用户渲染。
6. **状态捕获与同步**: 脚本正常结束时打印 `CONVERSATION_ID: <id>`。
    - **Agent 行动**: 必须提取此 ID 并更新到上述对应的 Session 槽位中，以便在下轮对话中通过 `--conversation_id` 自动复用。
7. **异常回退**: 若脚本返回“会话无效或隔离冲突”错误，Agent 必须清除对应槽位的旧 ID 并提示用户重新发起会话。

## Output (输出示例)

### 诊断中 (流式 Markdown)
> "根据**大黄**（金毛，8个月，未绝育）的呕吐频率，初步判断可能存在急性胃炎风险。建议：
> 1. **禁食 12 小时**：观察是否继续呕吐。
> 2. **精神观察**：若伴随拉稀或发烧，请及时就医。"

### 诊断结束 (状态标识)
> "--------------------"
> "CONVERSATION_ID: v2-chat-session-88291"

## Guardrails (护栏)

- **品种映射限制**: 若输入品种无法在官方库中找到，脚本将返回错误并要求用户更正。
- **物种匹配校验**: 系统将校验品种是否属于指定的 `pet_type`。禁止跨物种问诊。
- **安全红线**: 严禁在输出中包含任何 API 秘钥或原始签名字符串。
- **医疗免责**: 输出内容仅供参考，危急情况下请务必引导用户前往线下宠物医院。

## Appendix: Manual Credential Setup

如果您需要在本地 CLI 环境中手动配置凭据，请按以下步骤操作。

### 1. 获取凭据
请前往 [VetMew 开放平台](https://open.vetmew.com/) 申请 `API_KEY` 和 `API_SECRET`。

### 2. 初始化配置
直接运行任一入口脚本（如 `consultation.py`）。系统将检测到缺失凭据并自动启动配置向导：
1. 按照终端提示输入您的 `API_KEY` 和 `API_SECRET`。
2. 系统将自动在当前目录下创建 `.env` 文件，并将凭据合并为 `VETMEW_AUTH_TOKEN`。
3. 配置完成后，即可正常使用。

> **安全提示**：请勿将生成的包含真实密钥的 `.env` 文件提交到版本控制系统。

## Technical Dependencies
- Python 3.12+
- `requests`, `python-dotenv`
- `consultation.py` (主程序)
- `breed_manager.py` (品种管理)
