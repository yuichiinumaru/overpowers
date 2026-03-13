#!/usr/bin/env python3
import sys

def generate_metadata_scaffold():
    code = """import { CalculateMetadataFunction } from 'remotion';

// Define your props type
type Props = {
  videoSrc: string;
  title: string;
};

export const calculateMetadata: CalculateMetadataFunction<Props> = async ({ props, abortSignal }) => {
  // Example: Fetch dynamic data
  // const response = await fetch('https://api.example.com/data', { signal: abortSignal });
  // const data = await response.json();

  return {
    durationInFrames: 300, // Dynamic duration
    width: 1920,           // Dynamic width
    height: 1080,          // Dynamic height
    props: {
      ...props,
      // Overwrite or add props
    },
  };
};
"""
    print(code)

if __name__ == "__main__":
    generate_metadata_scaffold()
