---
name: unilumos-comfyui-relighting
description: Deploy the UniLumos AI model locally in ComfyUI to seamlessly relight
  characters to match new backgrounds.
tags:
- ai
- llm
category: image-processing
color: null
tools:
  read: true
  write: true
  bash: true
version: 1.0.0
---
# UniLumos Character Relighting in ComfyUI

## Overview
Deploy the UniLumos AI model locally in ComfyUI to seamlessly relight characters to match new backgrounds.

## Procedure
### 1. Installation
- Download the **UniLumos** model weights (a specialized relighting diffusion model).
- Install the required custom nodes for UniLumos via the ComfyUI Manager.
- Ensure your environment has the necessary masking/segmentation nodes (like SAM or Rembg) installed.

### 2. Workflow Construction
- Use a **Load Image** node for your foreground character. Use a background removal node to isolate them.
- Use a second **Load Image** node for your new background image.
- Connect both to the **UniLumos Relighting** node. UniLumos uses the background image as a light source reference.
- Connect the output to a standard image saver or preview node.

### 3. Execution
- UniLumos calculates the ambient light, directional shadows, and color temperature of the background and applies it to the foreground character.
- Execute the prompt. Adjust the blending strength parameter if the lighting effect is too harsh or too subtle.

## Source
- **Extracted From:** https://www.youtube.com/watch?v=5ik6tPs6Yq8
- **Original Context:** YouTube Mining Batch (Benji's AI Playground)
