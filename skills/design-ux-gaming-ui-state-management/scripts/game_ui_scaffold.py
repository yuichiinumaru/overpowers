#!/usr/bin/env python3
import sys

def generate_game_ui():
    code = """import React from 'react';
import { Progress } from "@/components/ui/8bit/progress";
import { cn } from "@/lib/utils";

export const HealthBar = ({ value = 100 }) => (
  <div className="retro text-xs">
    <div className="flex justify-between mb-1">
      <span>HEALTH</span>
      <span>{value}/100</span>
    </div>
    <Progress value={value} variant="retro" progressBg="bg-red-500" />
  </div>
);

export const ManaBar = ({ value = 100 }) => (
  <div className="retro text-xs">
    <div className="flex justify-between mb-1">
      <span>MANA</span>
      <span>{value}/100</span>
    </div>
    <Progress value={value} variant="retro" progressBg="bg-blue-500" />
  </div>
);

export const XpBar = ({ value = 0 }) => {
  const isLevelUp = value === 100;
  return (
    <div className="relative">
      <Progress value={value} variant="retro" progressBg="bg-yellow-500" className={cn(isLevelUp && "animate-pulse")} />
      {isLevelUp && <div className="absolute top-0 left-0 w-full text-center text-black drop-shadow-md">LEVEL UP!</div>}
    </div>
  );
};
"""
    print(code)

if __name__ == "__main__":
    generate_game_ui()
