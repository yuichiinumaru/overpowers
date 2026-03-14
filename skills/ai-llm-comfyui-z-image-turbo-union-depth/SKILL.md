---
name: comfyui-z-image-turbo-union-depth
description: Combine Z-Image Turbo with ControlNet Union and Depth Anything V3 in
  ComfyUI for advanced structural image control.
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
# Z-Image Turbo ControlNet Union & Depth Anything V3

## Overview
Combine Z-Image Turbo with ControlNet Union and Depth Anything V3 in ComfyUI for advanced structural image control.

## Procedure
### 1. Requirements Installation
- Ensure you have **ComfyUI** updated to the latest version.
- Download the **Z-Image Turbo** model weights.
- Download the **ControlNet Union** model compatible with Z-Image.
- Install the custom node for **Depth Anything V3** (usually via ComfyUI Manager) and download its respective model.

### 2. Workflow Construction
- Create a standard Z-Image Turbo pipeline.
- Insert a **Load Image** node for your source/reference image.
- Connect the source image to the **Depth Anything V3** preprocessor node to extract a high-quality depth map.
- Add an **Apply ControlNet** node.
- Route the Z-Image model, the extracted depth map, and the ControlNet Union model into the Apply ControlNet node.
- Connect the output to your sampler.

### 3. Execution & Tuning
- Set your text prompts to describe the desired final image.
- Adjust the `ControlNet Strength` (start around 0.8) to dictate how strictly the AI adheres to the depth map.
- Execute the workflow. The combination of Z-Image Turbo's speed and Depth Anything V3's accuracy allows for rapid, structurally precise generations.

## Source
- **Extracted From:** https://www.youtube.com/watch?v=KmYNxtLZQTU
- **Original Context:** YouTube Mining Batch (Benji's AI Playground)
