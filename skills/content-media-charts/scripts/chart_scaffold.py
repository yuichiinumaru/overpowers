#!/usr/bin/env python3
import sys

def generate_chart_scaffold():
    code = """import { spring, useCurrentFrame, useVideoConfig } from 'remotion';

export const BarChart: React.FC<{ data: number[] }> = ({ data }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  return (
    <div style={{ display: 'flex', alignItems: 'flex-end', gap: 10, height: 400 }}>
      {data.map((value, i) => {
        const height = spring({
          frame,
          fps,
          delay: i * 5,
          config: { damping: 200 },
        });

        return (
          <div
            key={i}
            style={{
              width: 40,
              height: height * value,
              backgroundColor: '#4a9eff',
            }}
          />
        );
      })}
    </div>
  );
};
"""
    print(code)

if __name__ == "__main__":
    generate_chart_scaffold()
