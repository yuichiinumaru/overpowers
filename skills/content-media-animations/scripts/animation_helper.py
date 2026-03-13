#!/usr/bin/env python3
import sys

def generate_interpolate_boilerplate():
    code = """import { interpolate, useCurrentFrame, useVideoConfig } from 'remotion';

export const MyAnimatedComponent = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const animationValue = interpolate(
    frame,
    [0, 1 * fps], // From frame 0 to 1 second
    [0, 1],       // Values
    {
      extrapolateRight: 'clamp',
    }
  );

  return (
    <div style={{ opacity: animationValue }}>
      Animated Content
    </div>
  );
};
"""
    print(code)

if __name__ == "__main__":
    generate_interpolate_boilerplate()
