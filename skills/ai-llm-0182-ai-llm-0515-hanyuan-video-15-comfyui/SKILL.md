---
name: hanyuan-video-15-comfyui
description: Set up Hanyuan Video 1.5 in ComfyUI to generate high-definition 1080p local AI videos.
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
# Hanyuan Video 1.5 Local 1080p Generation

## Overview
Set up Hanyuan Video 1.5 in ComfyUI to generate high-definition 1080p local AI videos.

## Procedure
### 1. Environment Setup
- Verify your ComfyUI installation is up-to-date to support the new Hanyuan 1.5 architecture.
- Download the massive **Hanyuan Video 1.5** model weights. Note: High VRAM (16GB+) is strongly recommended for 1080p generation.
- Place the weights in the `models/checkpoints/` directory.

### 2. Workflow Construction
- Construct the generation pipeline: Load the Hanyuan model.
- Use the dedicated text encoders required by Hanyuan (often customized or split from standard CLIP).
- Set the latent resolution to a 1080p equivalent (e.g., 1920x1080 or 1080x1920 for vertical).

### 3. Execution
- Set your text prompts.
- Due to the high resolution, use memory optimization flags (`--highvram` or `--medvram`) when launching ComfyUI to prevent crashes.
- Execute the generation and decode the latents using the Hanyuan-specific VAE to output the 1080p video.

## Source
- **Extracted From:** https://www.youtube.com/watch?v=Vjup3QGE-hg
- **Original Context:** YouTube Mining Batch (Benji's AI Playground)
