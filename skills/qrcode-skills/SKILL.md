---
name: qrcode-skills
description: Generate and decode QR codes using CaoLiao QR Code API. Use when the user wants to create a QR code from text/URL, decode/read QR code content from an image, or asks about QR code generation and scanning.
tags: [QR code, 二维码，生成，解码，草料]
version: 1.0.0
category: tool
---

# QR Code Generation & Decoding

使用草料二维码开放 API 生成和解码二维码，无需 API Key。

## 运行时选择：Python 或 Node.js

所有脚本同时提供 Python 和 Node.js 两个版本，功能和参数完全一致。

**选择策略**：
1. 检测 Python 是否可用
2. 若 Python 不可用，检测 Node.js
3. 两者都有时默认用 Python

## 生成二维码

将文本或 URL 编码为二维码图片，直接返回图片 URL 并提供预览。

**API 端点：** `https://api.2dcode.biz/v1/create-qr-code`

### 参数说明

| 参数 | 必选 | 默认值 | 说明 |
|------|------|--------|------|
| data | 是 | - | 二维码中的文本内容（需 URL 编码） |
| size | 否 | 256x256 | 图片尺寸，格式 `WxH` 或单个整数 |
| format | 否 | png | 输出格式：`png` 或 `svg` |
| error_correction | 否 | M | 纠错级别：L/M/Q/H |
| border | 否 | 2 | 边框宽度 |

### 场景一：仅生成（默认）

直接拼接 URL 返回，无需执行脚本。

### 场景二：生成并保存到本地

当用户明确要求保存时，执行脚本保存到本地。

### 场景三：批量生成

用户提供 Excel/CSV/TXT 文件时，先询问生成 URL 链接还是图片文件。

## 解码二维码

从二维码图片中读取/解码内容。优先使用本地 zxing 解码，失败时自动回退到草料 API。

### 场景一：单张解码

支持本地文件、图片 URL、用户直接发送的图片。

### 场景二：批量解码

用户提供 Excel/CSV/TXT 文件时，自动检测列并批量解码。

## 注意事项

- 生成二维码默认无需网络请求，直接拼接 URL 即可
- 解码二维码优先本地库，仅在本地失败时才调用远程 API
- data 参数需要正确的 URL 编码
- 草料 API 无需认证、免费使用
