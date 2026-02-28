---
name: wan-22-ffgo-video-customization
description: Use Wan 2.2 with the FFGO LoRA model to customize video content by combining multiple subjects and backgrounds into a single scene.
category: video-generation
color: "#E74C3C"
tools:
  read: true
  write: true
  bash: true
---

# Wan 2.2 FFGO Video Customization

## Overview
Use Wan 2.2 with the FFGO LoRA model to customize video content by combining multiple subjects and backgrounds into a single scene.

## Procedure
### 1. Model & Node Preparation
- Download the **Wan 2.2 Image-to-Video** model.
- Download the **FFGO (First Frame Generative Optimization)** LoRA model.
- Place the models in their respective `models/checkpoints/` and `models/loras/` folders in ComfyUI.
- Install necessary custom nodes for image manipulation (e.g., `Image Remove Background`, `Image Resize`, `Image Stitch`).

### 2. Canvas Preparation (Subject & Background Merging)
- Create a canvas group in ComfyUI to handle up to 3 objects and 1 background.
- Load the subject images and use the **Remove Background** node for each.
- Use **Image Resize** nodes to standardize the dimensions of the subjects and the background.
- Combine them using an **Image Stitch** node (or an image composite node) to create a single unified starting frame.

### 3. Video Generation & Post-Processing
- Pass the stitched image into the Wan 2.2 video generation pipeline.
- Apply the FFGO LoRA using a **Load LoRA** node before the video sampler.
- The FFGO LoRA forces the video model to heavily reference the first frame, keeping the stitched subjects and background consistent throughout the generated motion.
- *Post-Processing:* Because FFGO often flashes the raw input on the first few frames, use an **Image Frame Batch** node to trim the first 4 frames off the generated video before saving.

## Source
- **Extracted From:** https://www.youtube.com/watch?v=Dks3q5w7sdw
- **Original Context:** YouTube Mining Batch (Benji's AI Playground)
