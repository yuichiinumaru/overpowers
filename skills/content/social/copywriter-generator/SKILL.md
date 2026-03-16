---
name: content-social-copywriter-generator
description: Generate viral copy for platforms like Xiaohongshu, Douyin, WeChat, and Zhihu. Features tone control, tag recommendations, and length adjustment.
tags: [content, social-media, copywriting, generator]
version: 1.0.0
---

# Social Media Copywriter Generator

Generate viral copy for multiple platforms with one click - Xiaohongshu, Douyin, WeChat Official Account, and Zhihu.

---

## Quick Start

```bash
# Generate Xiaohongshu copy
python generate.py "AI Writing Tips" -p xiaohongshu

# Generate WeChat Official Account article
python generate.py "Workplace Communication" -p wechat -l long

# Generate title options only
python generate.py "Side Hustle Earning" --titles-only
```

---

## Features

- 🎯 4 Platforms Supported (Xiaohongshu/Douyin/WeChat/Zhihu).
- 📝 Intelligent Copywriting Generation.
- 🏷️ Tag Recommendations.
- 🎨 Tone Adjustment.
- 📏 Length Control.

---

## Usage

### Command Line

```bash
python generate.py "Subject" \
  -p [Platform] \
  -t [Tone] \
  -l [Length] \
  -o [Output File]
```

### Parameters

| Parameter | Description | Default |
|:---|:---|:---|
| topic | Copywriting theme | Required |
| -p, --platform | Platform: xiaohongshu/douyin/wechat/zhihu | xiaohongshu |
| -t, --tone | Tone: natural/professional/humorous/warm | natural |
| -l, --length | Length: short/medium/long | medium |
| -k, --keywords | Keyword list | None |
| -a, --audience | Target audience | General |
| -o, --output | Output file | Screen output |
| --titles-only | Only generate titles | False |
| --no-tags | Do not generate tags | False |

... (rest of content)
