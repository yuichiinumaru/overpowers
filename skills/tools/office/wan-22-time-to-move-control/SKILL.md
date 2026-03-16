---
name: wan-22-time-to-move-control
description: Implement the 'Time-To-Move' technique in ComfyUI with Wan 2.2 for precise
  control over AI video motion timing.
tags:
- ai
- llm
category: video-generation
color: null
tools:
  read: true
  write: true
  bash: true
version: 1.0.0
---
# Wan 2.2 Time-To-Move Motion Control

## Overview
Implement the 'Time-To-Move' technique in ComfyUI with Wan 2.2 for precise control over AI video motion timing.

## Procedure
### 1. Requirements
- Ensure **Wan 2.2** is installed and functioning in ComfyUI.
- Install the custom nodes that support motion timing and keyframing (often found in advanced video control node packs).

### 2. Setting Up Motion Keyframes
- Build a standard Wan 2.2 Image-to-Video workflow.
- Insert the **Time-To-Move** or **Motion Keyframe** scheduling nodes before the sampler.
- Configure the scheduler to dictate *when* specific motions should occur. For example, instruct the model to remain still for frames 0-20, pan right from 21-40, and zoom in from 41-60.

### 3. Execution
- Connect the scheduled motion latents to the KSampler.
- Run the prompt. This technique prevents the chaotic, random movement typical of base video models and forces the animation to follow your precise timing structure.

## Source
- **Extracted From:** https://www.youtube.com/watch?v=NcuUR7hrn-Q
- **Original Context:** YouTube Mining Batch (Benji's AI Playground)
