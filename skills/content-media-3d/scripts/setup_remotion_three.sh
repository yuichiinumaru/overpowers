#!/usr/bin/env bash
# Setup helper for Remotion Three

echo "--- Remotion Three Setup ---"
echo "Select your package manager:"
echo "1. npm"
echo "2. bun"
echo "3. yarn"
echo "4. pnpm"

read -p "Enter choice [1-4]: " choice

case $choice in
  1) cmd="npx remotion add @remotion/three" ;;
  2) cmd="bunx remotion add @remotion/three" ;;
  3) cmd="yarn remotion add @remotion/three" ;;
  4) cmd="pnpm exec remotion add @remotion/three" ;;
  *) echo "Invalid choice"; exit 1 ;;
esac

echo "Executing: $cmd"
eval $cmd

echo ""
echo "Creating basic 3D component scaffold (ThreeScene.tsx)..."
cat <<EOF > ThreeScene.tsx
import { ThreeCanvas } from "@remotion/three";
import { useVideoConfig } from "remotion";

export const ThreeScene: React.FC = () => {
  const { width, height } = useVideoConfig();

  return (
    <ThreeCanvas width={width} height={height}>
      <ambientLight intensity={0.4} />
      <directionalLight position={[5, 5, 5]} intensity={0.8} />
      <mesh>
        <sphereGeometry args={[1, 32, 32]} />
        <meshStandardMaterial color="red" />
      </mesh>
    </ThreeCanvas>
  );
};
EOF
echo "Scaffold created: ThreeScene.tsx"
