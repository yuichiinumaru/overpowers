---
name: qwen-image-edit-multi-angle
description: Use Qwen Image Edit to generate consistent multi-angle views and realistic lighting of a subject using a single prompt.
category: image-generation
color: "#2980B9"
tools:
  read: true
  write: true
  bash: true
---

# Qwen Image Edit Multi-Angle Generation

## Overview
Use Qwen Image Edit to generate consistent multi-angle views and realistic lighting of a subject using a single prompt.

## Procedure
### 1. Model Preparation
- Download the **Qwen Image Edit** model weights.
- Install the specific custom nodes for Qwen Image editing in ComfyUI.

### 2. Workflow Architecture
- Set up the Qwen Image Checkpoint Loader.
- To generate multiple angles consistently, utilize the model's specialized control tokens or dedicated multi-view node configuration.
- Provide a base image (if modifying an existing subject) or a highly detailed text prompt.
- Include directional keywords in your prompt (e.g., "front view, side profile, back view").

### 3. Execution & Tuning
- Set the batch size to the number of angles you wish to generate (e.g., 3 or 4).
- Execute the generation. The Qwen model maintains high internal consistency, ensuring the subject's clothing, facial features, and lighting remain identical across the different camera angles.

## Source
- **Extracted From:** https://www.youtube.com/watch?v=VCc2_suVcZ4
- **Original Context:** YouTube Mining Batch (Benji's AI Playground)
