---
name: tencentcloud-vita
description: ">"
metadata:
  openclaw:
    category: "tencent"
    tags: ['tencent', 'cloud', 'services']
    version: "1.0.0"
---

# 腾讯云 VITA 图像/视频理解 Skill

## 功能描述

本 Skill 基于腾讯云 **VITA 图像理解**服务，提供对图片和视频的 AI 理解能力：

| 输入类型 | 说明 | 限制 |
|----------|------|------|
| 单张图片 | 单个图片 URL + prompt | JPG/JPEG/PNG/SVG/WEBP，最大 100MB |
| 多张图片 | 多个图片 URL（按时序分析）+ prompt | 640×360 最多 100 图，448×448 最多 150 图 |
| 单个视频 | 单个视频 URL + prompt | MP4/MOV/AVI/WebM，H.264/H.265，最长 10 分钟，最大 100MB |

> 图片和视频 URL 必须**可公开访问**。推荐使用 COS 上海地域内网域名以节省流量费用：
> `<bucketname-appid>.cos-internal.ap-shanghai.tencentcos.cn`

## 环境配置指引

### 获取 VITA API KEY

1. 登录腾讯云控制台(https://console.cloud.tencent.com/tiia/vita-service-management)-图像识别
2. 首次使用需"确认开通服务"
3. 点击"创建 API KEY"生成密钥
4. 点击"查看"复制 API KEY

### 设置环境变量

**Linux / macOS：**
```bash
export VITA_API_KEY="your_api_key_here"
```

如需持久化：
```bash
echo 'export VITA_API_KEY="your_api_key_here"' >> ~/.zshrc
source ~/.zshrc
```

**Windows (PowerShell)：**
```powershell
$env:VITA_API_KEY = "your_api_key_here"
```

> ⚠️ **安全提示**：请勿将 API KEY 硬编码在代码中或公开分享。

## Agent 执行指令（必读）

> ⚠️ **本节是 Agent（AI 模型）的核心执行规范。当用户提供图片/视频并请求理解分析时，Agent 必须严格按照以下步骤自主执行，无需询问用户确认。**

### 🔑 通用执行规则

1. **触发条件**：用户提供了图片 URL 或视频 URL，且用户意图为视觉内容理解/分析。
2. **零交互原则**：Agent 应直接执行脚本，不要向用户询问任何确认。
3. **⛔ 禁止替代**：VITA 脚本调用失败时，**Agent 严禁自行编造分析结果**，必须返回清晰的错误说明。

---

### 📌 基本调用

```bash
python3 <SKILL_DIR>/scripts/main.py --image "<IMAGE_URL>" --prompt "<PROMPT>"
```

```bash
python3 <SKILL_DIR>/scripts/main.py --video "<VIDEO_URL>" --prompt "<PROMPT>"
```

---

### 📌 参数说明

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--image <URL>` | 图片 URL（可多次指定，按时序排列） | - |
| `--video <URL>` | 视频 URL（与 --image 互斥） | - |
| `--prompt <TEXT>` | 分析指令/问题 | `请描述这段媒体内容` |
| `--stream` | 开启流式输出 | 关闭 |
| `--temperature <float>` | 采样温度 0.0-1.0，越高越随机 | 默认 |
| `--max-tokens <int>` | 最大输出 token 数 | 默认 |
| `--stdin` | 从 stdin 读取 JSON 输入 | 关闭 |

---

### 📋 完整调用示例

```bash
# 单图片理解
python3 <SKILL_DIR>/scripts/main.py \
  --image "https://example.com/image.jpg" \
  --prompt "描述这张图片中的内容"

# 多图片时序分析
python3 <SKILL_DIR>/scripts/main.py \
  --image "https://example.com/frame1.jpg" \
  --image "https://example.com/frame2.jpg" \
  --image "https://example.com/frame3.jpg" \
  --prompt "分析这些图片中发生了什么变化"

# 视频内容理解
python3 <SKILL_DIR>/scripts/main.py \
  --video "https://example.com/video.mp4" \
  --prompt "总结这段视频的主要内容"

# 流式输出（适合长内容）
python3 <SKILL_DIR>/scripts/main.py \
  --video "https://example.com/video.mp4" \
  --prompt "详细描述视频内容" \
  --stream

# 调低 temperature 获取确定性输出
python3 <SKILL_DIR>/scripts/main.py \
  --image "https://example.com/chart.png" \
  --prompt "提取图表中的数据" \
  --temperature 0.1

# stdin JSON 模式
echo '{"media":[{"type":"video","url":"https://example.com/video.mp4"}],"prompt":"分析视频"}' \
  | python3 <SKILL_DIR>/scripts/main.py --stdin
```

---

### 📤 输出格式

**非流式输出（默认）：**
```json
{
  "result": "视频中展示了...",
  "usage": {
    "prompt_tokens": 1024,
    "completion_tokens": 256,
    "total_tokens": 1280
  }
}
```

**流式输出（--stream）：**
直接逐字输出文本内容（Server-Sent Events），无 JSON 包装。

---

### 📝 Prompt 模板推荐

根据使用场景选择合适的 prompt：

**监控视频分析：**
```
你是一个视频事件摘要专家。分析视频内容，以JSON格式输出：{"description":"一句话描述","title":"标题","object":["对象"],"event":["事件序列"]}
```

**新闻视频解读：**
```
你是专业新闻分析师，基于视频核心信息，生成：①标题（3个风格选项）②事件核心概述③关键细节④影响与延伸⑤信息来源
```

**带货商品讲解：**
```
观看带货视频，提取：商品名称、应用场景、核心卖点，并按营销阶段（时间范围、画面描述、语音内容、景别、营销意图）划分视频结构
```

**体育高光时刻：**
```
以专业体育解说视角，捕捉视频中的得分、高光、犯规、特写片段，输出：片段编号、时间范围（含关键帧）、景别、情景描述、画面文字
```

**直播质量评分：**
```
从6个维度评估直播片段：①直播间环境②主播语言③主播形象④出镜状态⑤互动引导⑥礼貌热情，每项输出是/否及判断依据
```

---

### ❌ Agent 须避免的行为

- 只打印脚本路径而不执行
- 向用户询问"是否要执行分析"——应直接执行
- 手动安装依赖——脚本内部自动处理
- 忘记读取输出结果并返回给用户
- VITA 服务调用失败时，自行编造分析内容
- 同时指定 `--image` 和 `--video`（两者互斥）

## 费用说明

| 计费项 | 单价 |
|--------|------|
| 输入 token | 1.2 元/百万 token |
| 输出 token | 3.5 元/百万 token |

> 默认并发为 **5**，超出会返回 429 错误。

## 核心脚本

- `scripts/main.py` — VITA 图像/视频理解，支持单图、多图、视频，流式/非流式输出

## 依赖

- Python 3.7+
- `openai`（OpenAI 兼容 SDK）

安装依赖（可选 - 脚本会自动安装）：
```bash
pip install openai
```
