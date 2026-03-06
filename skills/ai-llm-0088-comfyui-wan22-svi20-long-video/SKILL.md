---
name: comfyui-wan22-svi20-long-video
description: Create infinite-length AI videos without stiff motion or degradation using Wan 2.2 and SVI 2.0 in ComfyUI.
tags:
- ai
- llm
category: video-generation
color: null
tools:
  read: true
  write: true
  bash: true
---
# Wan 2.2 + SVI 2.0 Long Video Generation

## Overview
Create infinite-length AI videos without stiff motion or degradation using Wan 2.2 and SVI 2.0 in ComfyUI.

## Procedure
### 1. Model & Node Preparation
- Download the **Wan 2.2** Image-to-Video model and the **SVI 2.0** (Stable Video Infinity) LoRA model.
- Place them in `ComfyUI/models/checkpoints/` and `ComfyUI/models/loras/` respectively.
- Ensure the ComfyUI Wan Video Wrapper custom node is installed and updated.

### 2. Workflow Construction (Looping Structure)
- Avoid the "meatball spaghetti" (manually chaining dozens of samplers). Instead, implement a **For-Loop** structure node.
- Load the Wan 2.2 model and apply the SVI 2.0 LoRA.
- Connect a starting image (e.g., an image generated via Z-Image).
- Group your text prompts into a single text box (Travel Prompts) to feed different instructions at different time intervals.

### 3. Configuration & Generation
- Set standard settings: FPS to 16, Sampler frames to 81, and Flow Constants to 8 (or 10 for high motion).
- The SVI 2.0 framework will bi-directionally stitch the motion between 5-second chunks, maintaining the character and background without ping-pong artifacts.
- Execute the loop. The system will handle temporal masks and scene switching automatically for long-length (e.g., 30+ seconds) video generation.

## Source
- **Extracted From:** https://www.youtube.com/watch?v=XGB4qBkCFSM
- **Original Context:** YouTube Mining Batch (Benji's AI Playground)
