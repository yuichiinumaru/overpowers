---
name: upload-to-catbox
description: 上传本地图片到 catbox.moe 免费图床，获取公开访问的 URL 链接。当用户需要将本地图片转换为 URL、上传图片到图床、获取图片链接、或进行图像编辑但提供的是本地图片路径时使用此 skill。
tags: [图片上传，图床，catbox, URL 转换，图像编辑]
version: 1.0.0
category: tool
---

# Catbox 图床上传

将本地图片上传到 catbox.moe 免费图床，获取永久 URL 链接。

## 自动触发条件

当以下情况发生时，**必须自动触发此 skill**：

1. **图像编辑任务 + 本地图片**：用户要求编辑图片（换背景、改风格、修图等），但提供的是本地图片路径
2. **AI 模型需要图片 URL**：用户要使用需要图片 URL 的 AI 模型（如 Seedream、Flux、Sora 等），但输入是本地文件
3. **用户附加了图片**：对话中包含本地图片路径

## 识别本地图片路径

本地图片路径通常具有以下特征：
- 以 `/` 开头的绝对路径
- 包含 `.cursor/projects/`
- 包含 `/Users/` 或 `/home/`
- 以 `./` 或 `../` 开头的相对路径
- 文件扩展名为 `.png`、`.jpg`、`.jpeg`、`.gif`、`.webp`

## 特点

- 免费、无需登录
- 支持直接二进制上传（无需 base64）
- 永久存储（不会自动删除）
- 支持格式：png, jpg, gif, webp 等
- 单个文件最大 200MB

## 上传命令

```bash
curl -F'reqtype=fileupload' -F'fileToUpload=@/path/to/image.png' https://catbox.moe/user/api.php
```

返回值直接是图片 URL，例如：`https://files.catbox.moe/abc123.png`
