---
name: wevoicereply
description: "|"
metadata:
  openclaw:
    category: "voice"
    tags: ['voice', 'audio', 'transcription']
    version: "1.0.0"
---

# WeVoiceReply (稳定版)

## 执行架构说明


1. **解耦设计**：本技能定义文件负责流程编排，`voice_reply_skill.py` 负责底层复杂的 TTS 转换。
2. **环境要求**：确保系统中已安装 `ffmpeg-amr` 且 Python 环境中配置了 `piper-tts`。
3. **参数传递**：`{{text}}` 使用单引号包裹，确保 Shell 执行脚本时不会因为文本中的空格或特殊符号导致断裂。