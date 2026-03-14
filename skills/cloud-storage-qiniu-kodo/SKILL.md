---
name: cloud-storage-qiniu-kodo
description: Manage Qiniu Kodo object storage and data processing via MCP, Node.js SDK, and qshell. Supports file operations and image/video processing.
tags: [cloud, storage, qiniu, kodo]
version: 1.0.0
---

# Qiniu KODO Skill

Manage Qiniu Cloud Object Storage (KODO) and data processing through the qiniu-mcp tool, Node.js SDK scripts, and qshell.

---

## 📖 Feature Description

### Core Features
- 📤 **Upload Files** - Single file, batch upload, breakpoint resume.
- 📥 **Download Files** - Single file, batch download.
- 📋 **List Files** - By prefix, with pagination.
- 🗑️ **Delete Files** - Single file, batch deletion.
- 🔗 **Get URL** - Public/private bucket URL generation.
- 📊 **File Info** - View file details.
- 📁 **Directory Operations** - Move, copy, rename.

### Advanced Features (via MCP Tool)
- 🖼️ **Image Processing** - Scaling, cropping, watermarking, format conversion.
- 🎵 **Audio/Video Processing** - Transcoding, screenshots, slicing.
- 🔍 **Smart Search** - File search and metadata query.
- 📝 **Document Processing** - Document preview, format conversion.

---

## 🚀 First-Time Use — Auto Setup

When the user first requests a KODO operation, follow this process:

### Step 1: Check Current Status

```bash
bash scripts/setup.sh --check-only
```

**Check items:**
- ✅ Node.js Environment
- ✅ qiniu-mcp installed
- ✅ qshell installed
- ✅ Configuration file exists
- ✅ Credentials configured

If the output shows everything is OK, skip to "Execution Strategy."

---

### Step 2: Guide User to Provide Credentials if Not Configured

Inform the user:

```
I need your Qiniu Cloud credentials to connect to the KODO storage service. Please provide:

AccessKey — Qiniu AccessKey
SecretKey — Qiniu SecretKey  
Region — Storage region (e.g., z0=East China, z1=North China, z2=South China, na0=North America, as0=Southeast Asia)
Bucket — Storage bucket name
Domain (Optional) — Access domain (used for generating file URLs, e.g., http://cdn.example.com)

You can obtain these from the Qiniu Console:
- Key Management: https://portal.qiniu.com/user/key
- Bucket List: https://portal.qiniu.com/kodo/bucket
- Region Codes:
  - z0: East China (Hangzhou)
  - z1: North China (Hebei)
  - z2: South China (Guangzhou)
  - na0: North America (Los Angeles)
  - as0: Southeast Asia (Singapore)
```

... (rest of content)
