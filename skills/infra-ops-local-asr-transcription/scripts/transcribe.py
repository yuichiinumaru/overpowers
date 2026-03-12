#!/usr/bin/env python3
"""
Local ASR Transcription Script.
Usage: python3 transcribe.py <path_to_audio_file> [--model qwen|vibe]
"""

import argparse
import sys
import os
import torch
import torchaudio

def transcribe(audio_path, model_name):
    print(f"Loading {model_name} ASR model...")
    print(f"Processing audio file: {audio_path}")

    if not os.path.exists(audio_path):
        print(f"Error: Audio file {audio_path} not found.")
        sys.exit(1)

    device = "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"
    print(f"Using device: {device}")

    try:
        from transformers import AutoProcessor, AutoModelForSpeechSeq2Seq
    except ImportError:
        print("Error: transformers package is required. Run 'pip install transformers torchaudio'")
        sys.exit(1)

    if model_name == "qwen":
        model_id = "Qwen/Qwen-Audio-Chat" # or whatever the Qwen 3 ASR model is actually called in HF
    else:
        model_id = "microsoft/speecht5_asr" # Vibe Voice equivalent if not public

    processor = AutoProcessor.from_pretrained(model_id)
    model = AutoModelForSpeechSeq2Seq.from_pretrained(model_id).to(device)

    # Load audio
    waveform, sample_rate = torchaudio.load(audio_path)

    # Resample if needed
    if sample_rate != 16000:
        resampler = torchaudio.transforms.Resample(orig_freq=sample_rate, new_freq=16000)
        waveform = resampler(waveform)
        sample_rate = 16000

    # Ensure mono
    if waveform.shape[0] > 1:
        waveform = torch.mean(waveform, dim=0, keepdim=True)

    inputs = processor(audio=waveform.squeeze().numpy(), sampling_rate=sample_rate, return_tensors="pt").to(device)

    print("Running inference...")
    with torch.no_grad():
        generated_ids = model.generate(**inputs)

    transcript = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]

    output_path = os.path.splitext(audio_path)[0] + ".txt"
    print(f"Transcription complete. Saving to {output_path}...")
    with open(output_path, "w") as f:
        f.write(transcript + "\n")

    print("Done!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run local ASR transcription.")
    parser.add_argument("audio_path", help="Path to the audio file (.wav or .mp3)")
    parser.add_argument("--model", choices=["qwen", "vibe"], default="qwen", help="Model to use: qwen or vibe")

    args = parser.parse_args()
    transcribe(args.audio_path, args.model)
