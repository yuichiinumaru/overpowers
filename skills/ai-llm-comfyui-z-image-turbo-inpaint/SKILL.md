---
name: comfyui-z-image-turbo-inpaint
description: Set up and use the Z-Image Turbo ControlNet model for rapid, high-quality
  inpainting within ComfyUI.
tags:
- ai
- llm
category: image-generation
color: null
tools:
  read: true
  write: true
  bash: true
version: 1.0.0
---
# Z-Image Turbo ControlNet Inpaint in ComfyUI

## Overview
Set up and use the Z-Image Turbo ControlNet model for rapid, high-quality inpainting within ComfyUI.

## Procedure
### 1. Model & Node Installation
- Download the **Z-Image Turbo ControlNet Inpaint** model weights from Hugging Face or CivitAI.
- Place the weights into your `ComfyUI/models/controlnet/` directory.
- Ensure your ComfyUI installation is updated. If required, install the specific custom nodes for Z-Image through the ComfyUI Manager.

### 2. Workflow Construction
- Create a standard image generation pipeline with your base model (e.g., SDXL or SD1.5, depending on the Z-Image version).
- Add the **ControlNet Loader** node and select the Z-Image Turbo Inpaint model.
- Connect your source image to a **Mask Editor** or **Load Image with Mask** node to define the inpainting area.
- Route the masked image and the ControlNet into an **Apply ControlNet** node.
- Connect the output to your `KSampler`.

### 3. Execution & Tuning
- Set your text prompts to describe what should appear in the masked area.
- Lower the step count (Turbo models typically require only 4-8 steps).
- Adjust the ControlNet strength (usually between 0.6 and 1.0) to balance blending with the surrounding image.
- Execute the prompt to generate the inpainted image.

## Source
- **Extracted From:** https://www.youtube.com/watch?v=S3PKN2xW0YA
- **Original Context:** YouTube Mining Batch (Benji's AI Playground)
