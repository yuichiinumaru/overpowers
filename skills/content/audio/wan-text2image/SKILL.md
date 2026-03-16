---
name: ai-image-wan-text2image
description: Text-to-image tool using Alibaba DashScope's Wan2.6-t2i model. Supports prompt extension and custom image dimensions.
tags: [ai, image, wan, text2image]
version: 1.0.0
---

# Wan2.6 文生图 (Wan2.6 Text-to-Image)

使用阿里云DashScope的Wan2.6-t2i模型进行文生图。

## 环境要求

- DASHSCOPE_API_KEY：已配置在系统中
- curl：系统自带

## 使用方式

### 脚本调用

```bash
# 基本用法
bash scripts/t2i.sh "你的提示词"

# 指定反向提示词
bash scripts/t2i.sh "提示词" "不想出现的内容"

# 指定图片尺寸（支持：1280*1280, 720*1280, 1280*720）
bash scripts/t2i.sh "提示词" "" "1280*720"
```

## 参数说明
... (rest of content)
