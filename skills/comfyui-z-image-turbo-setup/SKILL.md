---
name: comfyui-z-image-turbo-setup
description: Install and run the distilled Z-Image Turbo model in ComfyUI for rapid, hyper-realistic image generation.
category: image-generation
color: "#2980B9"
tools:
  read: true
  write: true
  bash: true
---

# Z-Image Turbo Setup and Execution

## Overview
Install and run the distilled Z-Image Turbo model in ComfyUI for rapid, hyper-realistic image generation.

## Procedure
### 1. Model Acquisition
- Download the **Z-Image Turbo** model (a fast, distilled image generation model).
- Download its specific VAE (`ae.safetensors`) and Text Encoder files if they are provided separately.
- Place all files in their respective ComfyUI directories (`models/checkpoints`, `models/vae`, `models/clip`).

### 2. Basic Workflow Construction
- Add a **Checkpoint Loader** and select Z-Image Turbo.
- Add the corresponding **Load VAE** and **Load CLIP** nodes if the model is split.
- Connect text encoders for positive and negative prompts.
- Route to a **KSampler**. Since this is a Turbo/distilled model, set the sampling steps to a low number (e.g., 4 to 8 steps) and lower the CFG scale (e.g., 1.5 to 2.5).

### 3. Execution
- Write a prompt focusing on hyper-realism or human anatomy, as Z-Image excels in these areas.
- Execute the generation. The low step count will result in incredibly fast inference times compared to base models, making it ideal for rapid iteration.

## Source
- **Extracted From:** https://www.youtube.com/watch?v=3mT7KnotPqk
- **Original Context:** YouTube Mining Batch (Benji's AI Playground)
