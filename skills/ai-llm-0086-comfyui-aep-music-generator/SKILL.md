---
name: comfyui-aep-music-generator
description: Set up and run the AEP v1.5 diffusion-based AI music model locally within ComfyUI to generate audio tracks from text prompts.
tags:
- ai
- llm
category: audio-generation
color: null
tools:
  read: true
  write: true
  bash: true
---
# ComfyUI AEP v1.5 Music Generator

## Overview
This skill outlines the procedure to utilize the **AEP v1.5** AI music diffusion model locally via ComfyUI. This process enables high-quality audio generation directly from text prompts without relying on cloud APIs.

## Procedure

### 1. Model Acquisition
- Navigate to Hugging Face or ModelScope to locate the `AEP v1.5` repository.
- Download the required model weights (safetensors format).
- Place the weights in the appropriate `models/checkpoints/` (or equivalent custom nodes) directory of your ComfyUI installation.

### 2. ComfyUI Workflow Integration
- Ensure ComfyUI is updated to support audio diffusion nodes.
- If a custom node suite for AEP is required, clone the repository into `ComfyUI/custom_nodes/` and restart the server.
- Construct the workflow:
  1. Add a **Checkpoint Loader** and select the AEP v1.5 model.
  2. Connect a **CLIP Text Encode** node for your positive/negative prompts describing the desired music track.
  3. Route through a **KSampler** tailored for audio diffusion.
  4. Decode the latents into an audio format using a specific audio decoder node.
  5. Connect to an **Audio Save/Preview** node to output the final `.wav` or `.mp3` file.

### 3. Execution & Tuning
- Set your text prompt (e.g., "upbeat synthwave track with heavy bass, 120bpm").
- Adjust step count and CFG scale for desired quality and adherence to the prompt.
- Execute the workflow and monitor VRAM usage.

## Best Practices
- Diffusion models for audio can be resource-intensive; lower batch sizes if VRAM limits are reached.
- Keep prompts descriptive and genre-specific for the best results.

## Source
Extracted from YouTube mining batch (Benji's AI Playground: AEP v1.5 Launch).
