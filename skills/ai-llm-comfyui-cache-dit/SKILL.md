---
name: comfyui-cache-dit
description: Optimize Diffusion Transformer (DiT) models like Flux and SD3 in ComfyUI by caching intermediate steps into memory for significantly faster inference times.
tags:
- ai
- llm
category: performance-optimization
color: null
tools:
  read: true
  write: true
  bash: true
---
# ComfyUI Cache DiT Optimizer

## Overview
This skill provides the procedure to speed up inference times when using Diffusion Transformer (DiT) architectures (e.g., Flux, Stable Diffusion 3) inside **ComfyUI**. By implementing caching nodes, redundant computations are stored in memory, significantly accelerating image generation times.

## Procedure

### 1. Installation
- Navigate to the `ComfyUI/custom_nodes/` directory.
- Locate the repository for the **Cache DiT** custom node via GitHub or the ComfyUI Manager.
- Clone or install the node package.
- Restart the ComfyUI server to register the new nodes.

### 2. Implementation in Workflows
- Open an existing DiT workflow (e.g., a Flux generation setup).
- Introduce the **Cache DiT** node between the `Model Loader` and the `KSampler` (or equivalent sampling node).
- Connect the model output to the Cache DiT node input, and its output to the sampler.

### 3. Configuration & Optimization
- Set the `cache_threshold` to balance speed and quality. Lower thresholds generally increase speed but may slightly degrade the final image, whereas higher thresholds preserve quality but reduce the speedup effect.
- Test the workflow iteratively to find the sweet spot for your specific DiT model and hardware configuration.

## Best Practices
- This technique is memory-intensive as it stores intermediate states. Monitor system RAM and VRAM during execution to ensure stability.
- Ensure your ComfyUI environment and related PyTorch installations are up-to-date for optimal caching performance.
- Not recommended for low-VRAM machines where caching may lead to Out-Of-Memory (OOM) errors.

## Source
Extracted from YouTube mining batch (Benji's AI Playground: Speeding Up Inference with Cache DiT).
