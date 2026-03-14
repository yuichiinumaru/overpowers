---
name: wechat-article-typeset
description: "公众号文章排版——Markdown 生成 HTML 或已有 HTML 转公众号格式，并调用 edit.shiker.tech 生成可复制到公众号的复制页链接"
metadata:
  openclaw:
    category: "communication"
    tags: ['communication', 'chat', 'messaging']
    version: "1.0.0"
---

# 公众号文章排版

当用户需要进行**公众号文章排版**、**生成可复制到公众号的页面**或**调用 edit.shiker.tech 复制页**时，使用**本技能目录内的 JS**（不依赖仓库 `src/`）生成 HTML，再请求复制页链接。

## When to Use

- 用户提到「公众号排版」「复制到公众号」「生成公众号页面」「edit.shiker.tech」「文章转公众号」。
- 需要把 **Markdown** 排成公众号可用的富文本并得到复制页链接时。
- 需要把**已有 HTML 文章**（如带 class 的 div 排版）转为公众号可粘贴格式并得到复制页链接时。

## 1. 生成逻辑所在位置（技能目录自包含）

- **Markdown → HTML**：使用本技能目录下的 **`lib/utils/markdown.js`**（与 Web 端逻辑一致，为副本）。
- **入口脚本**：
  - `wechat-html.js`：从 Markdown 仅生成 HTML（用于预览/直接复制；**不保证**输出结构满足 `html-to-wechat-copy.js` 的两种输入格式）。
  - `wechat-copy.js`：从 Markdown 生成 HTML 并请求复制页 URL。
  - **`html-to-wechat-copy.js`**：从**已有 HTML 文章**转为公众号兼容格式并请求复制页 URL（见下方「1.2 已有 HTML 转公众号」）。

**执行方式**：在**本技能目录**下执行（复制到 `~/.openclaw/skills/wechat-article-typeset/` 后同样在该目录下执行）：

- 生成 HTML：`node wechat-html.js [选项] [input.md]` 或从 stdin 传入内容。选项见下「主题混搭」。
- 生成并获取复制页链接：`node wechat-copy.js [选项] <input.md>`，输出即为 `https://edit.shiker.tech/copy.html?id=xxx`。
- **已有 HTML 转公众号并获取复制页**：`node html-to-wechat-copy.js <path-to-article.html>`，输出为复制页 URL。
- 列出预设：`node wechat-html.js --list-presets`；列出主题：`--list-themes`；列出版式：`--list-layouts`。

### 1.2 已有 HTML 转公众号（html-to-wechat-copy.js）

- **输出**：直接请求 `edit.shiker.tech/api/copy` 并打印复制页 URL。
- **样式策略**：公众号仅对**引用（blockquote）**和**表格**保留背景色与边框，或整篇统一背景。脚本据此将整篇包统一背景，并把需强调的块转为 blockquote 或保留表格。

**文章类型与格式对应（两种格式即可覆盖全部）：**

| 文章类型 |  推荐格式 | 说明 |
|----------|----------|------|
| 大厂早报 |  **格式一** | 多条资讯 + 每条有「影响」+ 今日思考，与格式一完全一致。 |
| AI 职场文 | **格式二** | 教程/案例/清单，多段落、引用块、可选表格，用 section + table。 |
| 单厂深度 |  **格式二** | 单主题深度，多小节(h2/h3)、引用、数据表格，用格式二。 |
| 技术摸鱼周报 |  **格式一** 或 **格式二** | 若写成「多条简讯 + 每条影响」用格式一；若为自由小节+表格用格式二。 |
| 轻松吃瓜/轻思考 | **格式二** | 短文、思考、少量引用块，用 section 做高亮块即可。 |
| 一周速读 |  **格式一** 或 **格式二** | 若每条是「标题+摘要+影响」用格式一；若为列表+小节用格式二。 |
| 下周职场预警 |  **格式二** | 预警/清单，多条提醒或分段，用 section + 列表/表格。 |

**AI 生成符合输入的 HTML 时，请按以下两种格式之一输出（详见脚本文件头部注释）：**

| 格式 | 适用场景 | 结构要求 |
|------|----------|----------|
| **格式一：早报** | 大厂早报、多条资讯且每条有「影响」、部分周报/速读 | 整篇在 `<body>` 内，且有一层 `<div class="article">`；内含固定顺序：`h1` → `.intro` → 多个 `.item`（每项含 `.item-title`、`.item-content`、`.item-impact`）→ `.thinking` → `.divider` → `.footer`。无需写 `<style>`。 |
| **格式二：通用长文** | AI 职场文、单厂深度、摸鱼周报（自由结构）、轻松吃瓜、一周速读（列表式）、下周职场预警、教程/清单/带表格 | `<body>` 内直接放内容（或一层 `<section>` 包全文）。需背景/边框的块用 `<section style="...">`；表格用 `<table>`；标题用 `h1/h2/h3`，段落用 `p`，列表用 `ul/li`。脚本会把 `section` 转成 `blockquote`，表格保留。 |

**getFullHtml 签名**（与 Web 端一致）：

```js
getFullHtml(content, themeId, imageStyleId, layoutId = 'default', imageResolver, codeThemeId = 'vscode-dark')
```

## 2. 主题混搭（推荐）

**任意主题 + 任意版式** 均可自由组合（底层为 `getResolvedTheme(themeId, layoutId)`）。推荐两种用法：

### 2.1 预设（主题+版式一键）

- 使用 **`presets.js`** 中的预设名，如：`暖色色块`、`墨色下划线`、`青绿左边线`、`紫调渐变`、`极简黑白`、`雁栖湖`、`深色护眼` 等。
- 命令行：`node wechat-html.js --preset 墨色下划线 [input.md]`，或 `node wechat-copy.js --preset 青绿左边线 article.md`。
- 环境变量：`WEWORK_PRESET=墨色下划线`。
- 查看全部预设：`node wechat-html.js --list-presets`（或 `wechat-copy.js --list-presets`）。

### 2.2 自定义混搭（主题 + 版式分别指定）

- **themeId**：如 coral-warm、ink-seri、teal-fresh、purple-elegant、minimal-bw、amber-paper、starry-blue 等（`--list-themes` 列出全部）。
- **layoutId**：如 default、block、underline、leftline、minimal、gradient、card、yanqi 等（`--list-layouts` 列出全部）。
- 命令行：`node wechat-html.js --theme teal-fresh --layout leftline [input.md]`，或 `node wechat-copy.js -t ink-seri -l underline article.md`。
- 环境变量：`WEWORK_THEME_ID`、`WEWORK_LAYOUT_ID`。可与 `--preset` 同时使用，命令行会覆盖预设。

### 2.3 图片样式与代码主题

- **imageStyleId**：`default`、`rounded`、`shadow`、`border`。命令行 `--image-style` 或 `-i`，环境变量 `WEWORK_IMAGE_STYLE_ID`。
- **codeThemeId**：代码块高亮，如 `vscode-dark`、`monokai`。命令行 `--code-theme` 或 `-c`，环境变量 `WEWORK_CODE_THEME_ID`。

## 3. Steps（执行步骤）

**推荐：先走「Markdown → HTML → 公众号」链路（更可控）**

1. 让 AI 输出一份「中间态 HTML 文件」（`article.html`），**必须满足** `html-to-wechat-copy.js` 的输入要求（见上方「1.2」的两种格式，或直接看 `html-to-wechat-copy.js` 文件头部注释）。
2. 在本技能目录下执行：`node html-to-wechat-copy.js <path-to-article.html>`，直接得到复制页 URL。
3. 把复制页链接交给用户：浏览器打开 → 点击「复制到剪贴板」→ 粘贴到公众号后台。

> 说明：这条链路的目标是让「带背景/边框的块」落在公众号可保留样式的标签上（blockquote / table），并统一整篇背景。

**回退：直接「Markdown → 公众号」链路（省事，但样式可控性较弱）**

1. 确定样式：用 **预设**（`--preset` 或 `WEWORK_PRESET`）或 **自定义混搭**（`--theme` + `--layout` 等），无指定则用默认（coral-warm + default）。
2. 在本技能目录下运行 **`node wechat-copy.js [选项] <input.md>`**，输出即为复制页 URL。
3. 将复制页链接交给用户：浏览器打开 → 点击「复制到剪贴板」→ 粘贴到公众号后台。

**从已有 HTML 文章转公众号：**

1. 在本技能目录下运行 **`node html-to-wechat-copy.js <path-to-article.html>`**（如 `node html-to-wechat-copy.js "C:\path\to\article.html"`）。
2. 脚本会解析 `.article` 内结构，用统一背景 + 引用（blockquote）生成公众号兼容 HTML 并请求复制页，终端输出复制页 URL。
3. 将 URL 交给用户，在浏览器打开后复制再粘贴到公众号。

## 4. API 说明（edit.shiker.tech）

- **接口**：`POST https://edit.shiker.tech/api/copy`
- **请求体**：`Content-Type: application/json`，`{ "html": "完整 HTML 字符串" }`
- **响应**：`{ success: true, data: { id, url } }`；`url` 即为复制页地址。

## 5. 注意点

- 图片：内容中的图片需为可公网访问的 URL，否则公众号内无法显示。
- 本技能目录内 `lib/` 为 Web 端 `src/themes`、`src/utils` 的副本；若 Web 端主题/版式有更新，可酌情同步到本技能 `lib/`。
- 公众号粘贴时，仅**引用（blockquote）**和**表格**会保留背景色与边框；`html-to-wechat-copy.js` 已按此规则将需强调的块转为 blockquote。

## 简要流程小结

- **Markdown → 复制页**：在本技能目录下执行 **`node wechat-copy.js <input.md>`** 得到复制页 URL（或先 `node wechat-html.js` 再自行 POST）。
- **已有 HTML → 复制页**：执行 **`node html-to-wechat-copy.js <path-to-article.html>`** 得到复制页 URL。
- 把复制页链接交给用户，在浏览器打开后复制再粘贴到公众号。
