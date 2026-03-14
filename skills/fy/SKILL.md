---
name: fy
description: Translation skill - supports Chinese-English mutual translation, translates other languages to Chinese. Trigger condition: Input "fy" followed by content to translate, e.g., "fy test" returns "测试".
tags: [translation, chinese, english, multi-language, utility]
version: "1.0.0"
---

# Translation Skill

This skill handles translation requests.

## Trigger Condition

Activates when user inputs:
- `fy <content>` - Translate the following content

## Features

1. **Chinese-English Mutual Translation**: Automatically detects if input is Chinese or English and translates to the other language
2. **Other Languages**: If input is other languages (e.g., Japanese, Korean, French), translates to Chinese

## Usage Examples

- `fy test` → Output: 测试
- `fy 你好` → Output: hello
- `fy こんにちは` → Output: 你好
- `fy Bonjour` → Output: 你好

## Translation Rules

1. Detect input text language
2. If Chinese, translate to English
3. If English, translate to Chinese
4. If other languages, translate to Chinese
5. Return translation result
