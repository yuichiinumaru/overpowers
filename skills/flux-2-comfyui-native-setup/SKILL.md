---
name: flux-2-comfyui-native-setup
description: Install and run the newly released Flux 2 model natively within ComfyUI for high-quality image generation.
category: image-generation
color: "#2980B9"
tools:
  read: true
  write: true
  bash: true
---

# Flux 2 Native Setup in ComfyUI

## Overview
Install and run the newly released Flux 2 model natively within ComfyUI for high-quality image generation.

## Procedure
### 1. Requirements & Download
- Ensure you have the latest version of ComfyUI (update via `git pull` and `pip install -r requirements.txt`).
- Download the **Flux 2** model weights from Hugging Face or CivitAI.
- Download the necessary VAE and Text Encoders (T5xxl and CLIP-L) specific to the Flux 2 architecture.
- Place the main model in `models/checkpoints/`, VAE in `models/vae/`, and text encoders in `models/clip/`.

### 2. Workflow Construction
- Add a **Load Diffusion Model** or **Checkpoint Loader** node and select Flux 2.
- Add the **DualCLIPLoader** node to load both T5xxl and CLIP-L simultaneously.
- Route the text encoders to your positive and negative **CLIP Text Encode** nodes.
- Connect the model and prompt conditioning to a **KSampler** or **SamplerCustom** designed for Flux (e.g., using the `euler` sampler and `simple` scheduler).

### 3. Execution & Tuning
- Set your resolution (Flux works well at 1024x1024).
- Use a lower CFG scale (around 3.0 to 4.5) and around 20-30 steps for optimal generation.
- Execute the prompt to generate the image natively without external APIs.

## Source
- **Extracted From:** https://www.youtube.com/watch?v=gik9jjAIYxE
- **Original Context:** YouTube Mining Batch (Benji's AI Playground)
