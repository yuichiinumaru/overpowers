---
name: local-asr-transcription
description: Set up state-of-the-art Automatic Speech Recognition (ASR) locally using
  models like Qwen 3 ASR or Microsoft Vibe Voice for robust audio transcription in
  complex environments.
tags:
- infra
- ops
category: language-processing
color: null
tools:
  read: true
  write: true
  bash: true
version: 1.0.0
---
# Local Automatic Speech Recognition (ASR)

## Overview
This skill provides the procedure to deploy robust, local **Automatic Speech Recognition (ASR)** models such as **Qwen 3 ASR** or **Microsoft Vibe Voice**. These models excel at extracting accurate transcriptions from highly noisy environments, complex audio (e.g., songs), and multi-speaker scenarios across various languages without relying on external cloud APIs.

## Procedure

### 1. Model Selection & Setup
- Choose between Qwen 3 ASR and Microsoft Vibe Voice depending on your specific hardware and language requirements.
- Clone the respective model repository from Hugging Face or GitHub.
- Create an isolated Python virtual environment (`venv`) to manage dependencies.
- Install the required packages (e.g., `transformers`, `torch`, `torchaudio`, `ffmpeg`).

### 2. Audio Processing Pipeline
- Obtain the target audio file (in `.wav` or `.mp3` format).
- Write a Python script to initialize the ASR pipeline:
  1. Load the model and its processor (tokenizer).
  2. Load and resample the audio file using `torchaudio` or `librosa` to match the model's expected sampling rate (usually 16kHz).
  3. Pass the audio waveform to the processor to generate input features.
  4. Perform inference with the model (`model.generate()` or equivalent).
  5. Decode the output tokens back into raw text using the processor.
- Save the resulting text to a file (e.g., `.txt` or `.srt` format).

### 3. Execution & Optimization
- For long audio files, implement chunking (processing the audio in smaller segments) to prevent Out-Of-Memory (OOM) errors.
- Ensure CUDA/MPS acceleration is enabled for PyTorch to significantly reduce transcription time.

## Best Practices
- These models perform well in extreme environments. Test them on difficult audio (e.g., noisy cafes or music tracks) to verify robustness.
- Depending on the model, specific language codes may need to be provided during inference. Consult the model documentation for the correct formatting.
- Batch processing can increase throughput if processing multiple short audio clips simultaneously.

## Source
Extracted from YouTube mining batch (Benji's AI Playground: Qwen 3 ASR vs. Microsoft Vibe Voice).
