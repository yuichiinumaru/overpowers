#!/usr/bin/env bash
# Setup helper for Remotion Audio

echo "--- Remotion Audio Setup ---"
echo "Select your package manager:"
echo "1. npm"
echo "2. bun"
echo "3. yarn"
echo "4. pnpm"

read -p "Enter choice [1-4]: " choice

case $choice in
  1) cmd="npx remotion add @remotion/media" ;;
  2) cmd="bunx remotion add @remotion/media" ;;
  3) cmd="yarn remotion add @remotion/media" ;;
  4) cmd="pnpm exec remotion add @remotion/media" ;;
  *) echo "Invalid choice"; exit 1 ;;
esac

echo "Executing: $cmd"
eval $cmd

echo ""
echo "Creating basic Audio component scaffold (AudioLayer.tsx)..."
cat <<EOF > AudioLayer.tsx
import { Audio } from "@remotion/media";
import { staticFile, useVideoConfig } from "remotion";

export const AudioLayer: React.FC = () => {
  const { fps } = useVideoConfig();

  return (
    <Audio
      src={staticFile("audio.mp3")}
      volume={0.5}
      trimBefore={1 * fps}
    />
  );
};
EOF
echo "Scaffold created: AudioLayer.tsx"
