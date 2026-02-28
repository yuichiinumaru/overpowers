---
name: steady-dancer-wan-ai-video
description: Create AI dance videos without subscriptions using the SteadyDancer implementation for Wan AI Video.
category: video-generation
color: "#E74C3C"
tools:
  read: true
  write: true
  bash: true
---

# SteadyDancer Wan AI Video

## Overview
Create AI dance videos without subscriptions using the SteadyDancer implementation for Wan AI Video.

## Procedure
### 1. Environment & Model Setup
- Install the **Wan AI Video** base model in your local environment or ComfyUI instance.
- Download the **SteadyDancer** specific LoRA or control models that stabilize character motion in dance scenarios.
- Place the models in their respective `models/checkpoints/` or `models/loras/` directories.

### 2. Workflow Integration
- Load your base image of the character you want to animate.
- Load the driving video (a reference dance video).
- Connect the SteadyDancer nodes to extract temporal motion data from the driving video and apply it to the base image.
- Ensure temporal consistency parameters are enabled to prevent the character's background or features from flickering during complex dance moves.

### 3. Execution
- Set your FPS (e.g., 24 or 30 for dance) and frame count.
- Execute the generation. Note that dance motion extraction is computationally heavy; consider running at lower resolutions initially to test the motion mapping before upscaling.

## Source
- **Extracted From:** https://www.youtube.com/watch?v=53QdhJcUjvQ
- **Original Context:** YouTube Mining Batch (Benji's AI Playground)
