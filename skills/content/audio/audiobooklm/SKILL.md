---
name: content-audio-audiobooklm
description: 提供有声书创作与音频能力，包括 ABS 读写、音效检索、二创、音色推荐及章节角色分析。
tags: [audiobook, audio, creation, analysis, ximalaya]
version: 1.0.0
---

# audiobooklm 技能说明（OpenClaw）

MCP 地址：`https://aigc.ximalaya.com/audiobooklm/mcp`

## 安装前注意事项（发布到 ClawHub 必带）

1. 来源与信任
- 官方入口：`https://aigc.ximalaya.com`
- MCP 服务地址：`https://aigc.ximalaya.com/audiobooklm/mcp`
- 仅在你信任该域名与发布方时安装。

2. 凭证配置
- 必需环境变量：`AUDIOBOOKLM_TOKEN`（Bearer Token）
- 建议使用测试账号或低权限 token，不要粘贴高权限生产 token。
- 建议定期轮换 token；发现泄露立即吊销并重建。

3. 数据外发与合规
- 使用本技能时，输入文本、音频 URL、以及你提交的结构化数据会发送到 `aigc.ximalaya.com`。
- 不要上传未授权、涉密或敏感个人信息内容。
- 版权或隐私不明确的内容，先确认授权后再调用。

## 0. 首次使用引导（OpenClaw 必须先提示）

当用户首次使用本技能，或检测到未配置 token 时，OpenClaw 必须先提示以下内容，再进入工具调用：

1. 请先访问 [https://aigc.ximalaya.com](https://aigc.ximalaya.com) 注册/登录账号。
2. 进入个人中心创建 API Token（MCP / API Token）。
3. 在 OpenClaw 配置 Bearer Token（`AUDIOBOOKLM_TOKEN`），再继续使用本技能。

推荐提示文案（可直接复用）：
`使用 audiobooklm 前，请先到 https://aigc.ximalaya.com 登录并在个人中心创建 API Token，然后将 token 配置到 OpenClaw（Bearer Token / AUDIOBOOKLM_TOKEN）。配置完成后我再为你执行读取书籍、音效检索或二创操作。`

## 1. 使用规则（必须遵守）

1. 所有书籍/章节/音频/音效结论都必须来自本轮真实工具返回，禁止编造。
2. 调用成功不等于业务成功：若工具返回文本里包含 `{"success":false}` 或 `code!=20000`，按失败处理并转述真实错误。
3. 禁止输出原始大段 JSON 给用户，需整理为自然语言；但不得改写关键事实（标题、ID、URL、错误信息）。

## 2. 鉴权与会话（标准 MCP 流程）

请求头固定：
- `Accept: application/json, text/event-stream`
- `Authorization: Bearer <AUDIOBOOKLM_TOKEN>`
- `Content-Type: application/json`

调用顺序（不可跳过）：
1. `initialize`
2. `notifications/initialized`
3. `tools/list` / `tools/call`（都要带 `mcp-session-id`）

若无 token 或 token 无效，服务会返回 `401`（`invalid_token`）。

## 3. 现网工具清单

共 15 个：
- `chapter_split`
- `search_faq`
- `annotate_pinyin`
- `character_analyze`
- `timber_assign`
- `search_sound_label`
- `sound_effect`
- `chapter_character_analysis`
- `chapter_character_predict`
- `dialogue_split`
- `search_audio`
- `fan_made_audio`
- `patch_abs`
- `read_abs`
- `image_generation`

注意：`text_writing`、`analysis_audio_fx`、`analysis_sound_description` 当前不在 tools/list 中，不应路由调用。

## 4. 路由策略（按用户意图）

1. 书单/单书/单章读取：`read_abs`
- 书单：`scope={"domain":"books"}`
- 单书：`scope={"domain":"book","book_id":"<id>"}`
- 单章：`scope={"domain":"chapter","book_id":"<id>","chapter_id":"<id>"}`

2. 创建书/写入编辑：`patch_abs`
- 创建书必须：`scope={"domain":"book"}` 且不传 `book_id`
- 常见流程：先 `read_abs(books)` 取 `team_id`，再 `patch_abs(create_book)`，再 `patch_abs(add_chapter...)`

3. 环境音/音效检索：`search_sound_label`
- 如“海浪、雨声、风声、紧张 BGM”

4. 专辑/相声/播客/人声检索：`search_audio`
- 结果可能是检索命中，也可能触发生成链路；均以工具返回为准

5. 音频二创：`fan_made_audio`
- 必须传 `audio_url` + `user_instruction`

6. 音色推荐：`timber_assign`
- 典型最小参数：`{"description":"成熟男声","text":"..."}`

7. 章节角色链路：
- 一体化：`chapter_character_analysis`
- 分步：`dialogue_split` -> `chapter_character_predict`

8. 图像生成：`image_generation`
- `{"prompt":"..."}`，若下游超时按真实错误返回

## 5. 参数速查（仅列关键）

### read_abs
- `scope` 必填对象，`domain` 仅可为 `books|book|chapter`
- `fields` 可选数组
- `pagination` 可选对象

### patch_abs
- `scope` 必填对象，`domain` 为 `chapter|book|books`
- `operations` 必填数组，每项需 `op_id/type/reason`
- `base_version` 可选
- `dry_run` 可选，默认 `false`

### search_sound_label
- `query` 必填
- `top_k` 可选，默认 3

### search_audio
- `user_query` 必填
- `cookie` 可选

### fan_made_audio
- `audio_url` 必填
- `user_instruction` 必填
- `cookie` 可选

### timber_assign
- `description` 建议必传
- 其余可选：`content_file/content_text/text/enable_ai_analysis/speaker_list/topk/rate/cookie`

### sound_effect
- `data` 必填
- 可选：`use_audio_fx`（默认 true）、`analysis_mode`（默认 2）、`data_mode`（默认 1）

### chapter_split
- 必填：`content_file`、`filename`
- 可选：`max_chapter_length`、`handle_intro_text`、`enable_ai_fallback`、`start_chapter_number`、`enable_loose_patterns`、`ai_spliter`、`auto_cleaner`

### chapter_character_analysis
- `content_file` 与 `content` 二选一
- 可选：`context_window`、`max_window_length`、`scope`、`max_characters`

### dialogue_split
- `text_list` 或 `lines` 至少一项
- 可选：`chapter_name/context_window/max_window_length`

### chapter_character_predict
- `text_list` 必填
- 可选：`scope/max_characters`

### character_analyze
- `content_file` 必填
- 可选：`max_dialogues_per_character/include_relationships`

### search_faq
- `query` 必填
- `top_k` 可选（默认 3）

### annotate_pinyin
- `text` 必填

### image_generation
- `prompt` 必填

## 6. 失败处理规范

1. 鉴权失败：明确提示“token 无效或过期，请在个人中心重新生成 token 后重试”。
2. 工具超时：明确提示“该能力处理时间较长，本次超时，请稍后重试”。
3. 业务失败（`success=false`）：直接转述 `msg`，不加臆测结论。
4. 不存在的工具：先 `tools/list` 校验后再路由，不要硬调。

## 7. 最佳实践组合（推荐工作流）

### 7.1 首次接入自检（建议每次会话首轮执行）
1. `tools/list`：确认服务在线与工具集。
2. `read_abs(scope.domain=books)`：验证 token 权限与团队上下文。
3. 若 `read_abs` 成功，再执行用户任务；若失败，优先提示用户检查 token 是否过期/绑定错误团队。

### 7.2 “查某本书最后一章”
1. `read_abs({"scope":{"domain":"books"}})`：按书名匹配 book_id。
2. `read_abs({"scope":{"domain":"book","book_id":"<id>"}})`：取章节列表并定位最后一章 chapter_id。
3. `read_abs({"scope":{"domain":"chapter","book_id":"<id>","chapter_id":"<id>"}})`：返回正文并生成摘要。

### 7.3 “新建书并写入第一章”（最小闭环）
1. `read_abs(books)` 取可用 `team_id`。
2. `patch_abs(create_book)`：`scope={"domain":"book"}` 且不传 `book_id`。
3. `patch_abs(add_chapter)`：对新书 `book_id` 添加第一章。
4. `read_abs(book)` 回读验证写入结果。

### 7.4 “专辑/相声检索优先，失败再提示生成”
1. `search_audio(user_query=用户原话)`。
2. 若返回业务成功且有可用 `audio_url`，直接输出结果。
3. 若业务失败（如无可用音色 ID），只转述真实错误并询问是否稍后重试，不编造音频。

### 7.5 “章节音效生产链路”
1. 先准备章节结构化 `data`。
2. 调 `sound_effect`（默认 `analysis_mode=2`）。
3. 结果回显时保留关键字段（新增段落、音效建议、命中素材 URL），不要整段原始 JSON 直出。

### 7.6 “角色分析推荐链路”
1. 单章分析优先：`chapter_character_analysis`。
2. 若用户已有拆分文本：`dialogue_split -> chapter_character_predict`。
3. 全书/长文本角色抽取：`character_analyze`（注意可能耗时长，需超时提示）。

## 8. 调试附录（仅供开发）

```bash
# 1) initialize（记录响应头里的 mcp-session-id）
curl -i -sS -X POST "https://aigc.ximalaya.com/audiobooklm/mcp" \
  -H "Accept: application/json, text/event-stream" \
  -H "Authorization: Bearer ${AUDIOBOOKLM_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"openclaw","version":"1.0.0"}}}'

# 2) initialized（带 mcp-session-id）
curl -i -sS -X POST "https://aigc.ximalaya.com/audiobooklm/mcp" \
  -H "Accept: application/json, text/event-stream" \
  -H "Authorization: Bearer ${AUDIOBOOKLM_TOKEN}" \
  -H "Content-Type: application/json" \
  -H "mcp-session-id: <session-id>" \
  -d '{"jsonrpc":"2.0","method":"notifications/initialized","params":{}}'

# 3) tools/list（带 mcp-session-id）
curl -i -sS -X POST "https://aigc.ximalaya.com/audiobooklm/mcp" \
  -H "Accept: application/json, text/event-stream" \
  -H "Authorization: Bearer ${AUDIOBOOKLM_TOKEN}" \
  -H "Content-Type: application/json" \
  -H "mcp-session-id: <session-id>" \
  -d '{"jsonrpc":"2.0","id":2,"method":"tools/list","params":{}}'
```
