---
name: ai-multimodal-image-understanding
description: Uses Zhipu AI's GLM-4V-Flash API to understand and describe image content, including object recognition and scene analysis.
tags: [image-understanding, zhipu-ai, multimodal, computer-vision, glm-4v]
version: 1.0.0
---

# Image Understanding Skill

This skill is used to understand the content of an image using Zhipu AI's free GLM-4V-Flash multimodal API.

## When to Use

Use this skill when the user needs to understand or describe image content, for example:
- "What's in this picture?"
- "Describe this image."
- "What does this cell diagram show?"
- "Analyze the content of this image."

## Prerequisites

User needs:
1. Register an account at https://bigmodel.cn/
2. Get an API Key: https://bigmodel.cn/console/apikeys
3. Provide the API Key as an environment variable: `ZHIPU_API_KEY`

## How to Use

### Method 1: Using Built-in Script

The skill provides a `scripts/analyze_image.py` script that can be called directly:

```bash
python scripts/analyze_image.py <image_path> "<question>"
```

Parameters:
- `<image_path>`: Path to the image file (JPG recommended).
- `<question>`: The question to ask, e.g., "What is in this image?"

### Method 2: Manual API Call

If the script is not available, you can call the Zhipu API directly using Python:

```python
from zhipuai import ZhipuAI

client = ZhipuAI(api_key="YOUR_API_KEY")

response = client.chat.completions.create(
    model="glm-4v",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What is in this image? Please describe in detail."},
                {"type": "image_url", "image_url": {"url": "Image URL or base64"}}
            ]
        }
    ]
)

print(response.choices[0].message.content)
```

## Output Format

Returns a detailed description of the image content, including:
- Main objects/people in the image
- Scene/Background
- Visual features like color, layout, etc.
- Text (if any)
- Possible meanings or inferences

## Notes

- GLM-4V-Flash is free but has rate limits.
- Supports image URL or Base64 encoding.
- Best supported image size: within 1024x1024.
- JPG format is recommended; PNG may have compatibility issues.
