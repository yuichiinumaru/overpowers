---
name: nano-image-generator
description: "Generate images using Nano Banana Pro (Gemini 3 Pro Preview). Use when creating app icons, logos, UI graphics, marketing banners, social media images, illustrations, diagrams, or any visual assets. Triggers include phrases like 'generate an image', 'create a graphic', 'make an icon', 'design a logo', 'create a banner', or any request needing visual content."
---

# Nano Image Generator

Generate images using Nano Banana Pro (Gemini 3 Pro Preview) for any visual asset needs.

## Requirements

在项目根目录 `.env` 中配置：

- `apikey`（或 `APIKEY`）
- `baseurl`（或 `BASEURL`，例如 `https://generativelanguage.googleapis.com/v1beta/models`）

兼容回退：若未找到 `apikey/APIKEY`，脚本会尝试 `GEMINI_API_KEY`。

## Quick Start

```bash
python scripts/generate_image.py "A friendly robot mascot waving" --output ./assets/mascot.png
```

## Script Usage

```bash
python scripts/generate_image.py <prompt> --output <path> [options]
```

**Required:**
- `prompt` - Image description
- `--output, -o` - Output file path

**Options:**
- `--aspect, -a` - Aspect ratio (default: `1:1`)
  - Square: `1:1`
  - Portrait: `2:3`, `3:4`, `4:5`, `9:16`
  - Landscape: `3:2`, `4:3`, `5:4`, `16:9`, `21:9`
- `--size, -s` - Resolution: `1K`, `2K` (default), `4K`

## Workflow

1. **Determine output location** - Place images where contextually appropriate:
   - App icons → `./assets/icons/` or `./public/icons/`
   - Marketing → `./marketing/` or `./assets/images/`
   - UI elements → `./src/assets/` or `./public/images/`
   - General → `./generated/`

2. **Craft effective prompts** - Be specific and descriptive:
   - Include style: "flat design", "3D rendered", "watercolor", "minimalist"
   - Include context: "for a mobile app", "website hero image", "social media post"
   - Include details: colors, mood, composition

3. **Choose appropriate settings:**
   - Icons/logos → `--aspect 1:1`
   - Banners/headers → `--aspect 16:9`
   - Mobile screens → `--aspect 9:16`
   - Photos → `--aspect 3:2` or `4:3`

## Examples

**App icon:**
```bash
python scripts/generate_image.py "Minimalist flat design app icon of a lightning bolt, purple gradient background, modern iOS style" \
  --output ./assets/app-icon.png --aspect 1:1
```

**Marketing banner:**
```bash
python scripts/generate_image.py "Professional website hero banner for a productivity app, abstract geometric shapes, blue and white color scheme, modern and clean" \
  --output ./public/images/hero-banner.png --aspect 16:9
```

**High-quality illustration:**
```bash
python scripts/generate_image.py "Detailed isometric illustration of a cozy home office setup with plants, warm lighting, digital art style" \
  --output ./assets/illustrations/office.png --size 4K
```

## Prompt Tips

- **Be specific** - "A red apple on a wooden table" vs "an apple"
- **Include style** - "in the style of pixel art" or "photorealistic"
- **Mention purpose** - "for a children's book" affects the output style
- **Describe composition** - "centered", "rule of thirds", "close-up"
- **Specify colors** - Explicit color palettes yield better results
- **Avoid** - Don't ask for text in images (use overlays instead)