---
name: douyin-video-analyzer
description: "深度拆解抖音视频，自动生成包含数据、结构、视觉、文案的完整分析报告。支持浏览器解析（Playwright）、视频下载（yt-dlp）、自定义 fps 抽帧和 AI 视觉分析（智谱 GLM-4.6V 系列）。"
metadata:
  openclaw:
    category: "video"
    tags: ['video', 'media', 'editing']
    version: "1.0.0"
---

# 抖音视频拆解分析器 (Douyin Video Analyzer)

> 🎬 深度拆解抖音爆款视频，自动生成包含数据、结构、视觉、文案的完整分析报告

## 功能特性

- ✅ **全自动化**: 输入链接，自动完成“网页解析 -> 视频下载 -> 抽帧分析”全闭环。
- ✅ **反爬绕过**: 内置 Playwright 浏览器，完美解决抖音 JSVM 加密和 WAF 挑战。
- ✅ **极速理解**: 优先采用 2fps 抽帧方案，兼容 1.9G 低内存环境，快速生成分析报告。
- ✅ **AI 视觉分析**: 深度集成智谱 GLM-4.6V 系列，精准捕捉视觉钩子、配色与剪辑套路。

## 使用

### 基本分析 (推荐)

```bash
# 默认 2fps, 最大 60 帧
node scripts/analyze.js https://v.douyin.com/xxxxx
```

### 高级控制

```bash
# 自定义频率：每秒抽 5 帧 (极细拆解)
node scripts/analyze.js https://v.douyin.com/xxxxx --fps 5

# 增加总采样量：长视频分析
node scripts/analyze.js https://v.douyin.com/xxxxx --max-frames 120

# 使用特定模型 (默认 glm-4.6v)
node scripts/analyze.js https://v.douyin.com/xxxxx --model glm-4.6v-flash
```

## CLI 选项

```
用法: node scripts/analyze.js <链接/本地路径> [选项]

选项:
  --model <model>        AI 模型 (glm-4.6v, glm-4.6v-flash, glm-4.6v-flashx)
  --fps <number>         每秒抽帧数量 (默认: 2)
```

## 维护者

Leo & Neo (Startup Partners)
