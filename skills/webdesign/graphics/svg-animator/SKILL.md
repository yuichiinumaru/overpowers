---
name: svg-animator
description: "Generate animated videos from SVG frames using text LLM. Supports any subject (animals, humans, characters, scenes, abstract art), automatic duration calculation, and multi-scene story animations. ..."
metadata:
  openclaw:
    category: "utility"
    tags: []
    version: "1.0.0"
---

# SVG Animator

Generate SVG code with a text model, render frame by frame, and then synthesize video. No video generation API required!

## Supported Scenarios

- **Animals**: Dog running, cat jumping, fish swimming, birds flying
- **People**: Walking, running, dancing, work scenes
- **Scenes**: Sunrise, sunset, clouds drifting, leaves falling, raindrops falling
- **Abstract**: Geometric transformations, color gradients, particle effects
- **Stories**: Multi-scene continuous animation (requires stitching multiple segments)

## Usage Flow

```
User: Generate an animation of "a cat stretching"
↓
1. Understand Requirements → Determine theme, action, duration
2. Design Frame Sequence → SVG code for each frame
3. Generate Frames → Node.js generates SVG → rsvg-convert converts to PNG
4. Synthesize Video → ffmpeg combines into MP4/GIF
5. Output → Return file path or nginx link
```

## Duration Calculation Rules

| Requirement | Number of Frames | Duration | fps |
|------|------|------|-----|
| Simple Action (Stretching, Blinking) | 8-12 frames | 1 second | 10 |
| Regular Action (Walking, Running) | 16-24 frames | 2 seconds | 12 |
| Complex Action (Dancing, Tumbling) | 30-48 frames | 3-4 seconds | 12 |
| Short Story (2-3 scenes) | 60-120 frames | 5-10 seconds | 12 |
| Long Story (5+ scenes) | 120+ frames | 10+ seconds | 15 |

## Animation Principles

### Periodic Motion (Sine Function)

```javascript
// Frame index i, total frames totalFrames
const t = (i / totalFrames) * Math.PI * 2;  // 0 → 2π cycle

// Leg swing
const legOffset = Math.sin(t) * 40;

// Tail wagging
const tailAngle = Math.sin(t * 2) * 25;

// Body bobbing up and down
const bodyY = Math.sin(t) * 5;
```

### Multi-Element Coordination

```javascript
// Legs, tail, and body use the same t, but with different amplitudes
const legPhase = t;           // Leg cycle
const tailPhase = t * 2;      // Tail cycle is twice as fast
const bodyPhase = t;          // Body synchronized with legs

// Combined usage
legOffset = Math.sin(legPhase) * 40;
tailAngle = Math.sin(tailPhase) * 25;
bodyY = Math.sin(bodyPhase) * 5;
```

## Frame Generation Code Template

```javascript
const fs = require('fs');
const { execSync } = require('child_process');

const frames = 24;  // Adjust based on duration requirements
const size = 400;

for (let i = 0; i < frames; i++) {
  const t = (i / frames) * Math.PI * 2;
  
  // Calculate motion parameters
  const legOffset = Math.sin(t) * 40;
  const tailAngle = Math.sin(t * 2) * 25;
  // ... more parameters

  const svg = `<svg width='${size}' height='${size}' xmlns='http://www.w3.org/2000/svg'>
    <!-- Background -->
    <rect width='${size}' height='${size}' fill='#87CEEB'/>
    
    <!-- Ground -->
    <rect x='0' y='${size*0.88}' width='${size}' height='${size*0.12}' fill='#90EE90'/>
    
    <!-- Main Body - Use motion parameters -->
    <ellipse cx='${200 + legOffset * 0.5}' cy='${250 + Math.sin(t)*5}' ... />
    <!-- More elements -->
  </svg>`;

  fs.writeFileSync(`/tmp/frames/frame_${String(i).padStart(2, '0')}.svg`, svg);
}

// Convert to PNG
execSync('rsvg-convert frame_*.svg -o frame_%02d.png');

// Synthesize video
execSync('ffmpeg -y -framerate 12 -i frame_%02d.png -c:v mpeg4 -q:v 2 output.mp4');
```

## Common Animation Parameters

### Walking/Running

```javascript
const runCycle = {
  legSwing: Math.sin(t) * 40,      // Leg swing amplitude
  bodyBob: Math.sin(t * 2) * 5,   // Body bobbing
  tailWag: Math.sin(t * 2) * 30,  // Tail wag
  armSwing: Math.sin(t) * 25      // Arm swing
};
```

### Flying

```javascript
const flyCycle = {
  wingUp: Math.sin(t) * -45,      // Wing upward motion
  wingDown: Math.sin(t) * 45,     // Wing downward motion
  bodyTilt: Math.sin(t) * 10,     // Body tilt
  glide: Math.sin(t) * 20         // Glide height variation
};
```

### Jumping

```javascript
const jumpCycle = {
  yOffset: -Math.abs(Math.sin(t)) * 100,  // Vertical displacement
  legTuck: Math.abs(Math.sin(t)) * 30,   // Leg tuck
  armUp: Math.abs(Math.sin(t)) * -30      // Arm raise
};
```

### Swaying/Shaking

```javascript
const swayCycle = {
  rotation: Math.sin(t) * 15,     // Overall sway angle
  xOffset: Math.sin(t) * 10,     // Horizontal displacement
  wave: Math.sin(t * 3) * 5      // Slight shaking
};
```

## Scene Animation Examples

### Sunrise

```javascript
// Sun rising from the horizon
const progress = i / frames;
const sunY = size * 0.8 - progress * size * 0.6;  // From bottom to top
const skyGrad = `rgb(${255 * progress}, ${200 * progress}, ${100 + 155 * progress})`;
```

### Clouds Drifting

```javascript
const cloudX = (i / frames) * size * 1.5;  // From left to right
// Cloud opacity changes with position
const opacity = 1 - (cloudX / size) * 0.5;
```

### Raindrops Falling

```javascript
// Multiple drops
for (let drop = 0; drop < 10; drop++) {
  const startFrame = (frames / 10) * drop;
  const dropPos = ((i - startFrame) / frames) * size;
  // Draw raindrop at dropPos position
}
```

## Multi-Scene Story Animation

When the user requests "tell a story," generate multiple scenes and then stitch them together:

```javascript
// Scene 1: Cat wakes up (12 frames)
// Scene 2: Stretches (12 frames)  
// Scene 3: Plays (24 frames)
// Scene 4: Eats (16 frames)
// Scene 5: Sleeps (12 frames)

// Generate each scene separately and then stitch with ffmpeg
const scenes = ['scene1.mp4', 'scene2.mp4', 'scene3.mp4'];
const concatList = scenes.map(s => `file '${s}'`).join('\n');
fs.writeFileSync('/tmp/concat.txt', concatList);
execSync(`ffmpeg -y -f concat -safe 0 -i /tmp/concat.txt -c copy story.mp4`);
```

## Complete Workflow

### Step 1: Analyze Requirements

```
"Generate a story animation of a puppy chasing a butterfly"
```

Breakdown:
- Theme: Puppy + Butterfly
- Actions: Chasing (puppy running + butterfly flying)
- Scene: Grassland, sky
- Duration: 5-8 seconds (3 scenes)

### Step 2: Design Scenes

1. **Scene 1** (0-3 seconds): Puppy sees butterfly
   - Puppy standing, tail wagging
   - Butterfly flies by
   
2. **Scene 2** (3-6 seconds): Chasing
   - Puppy running (24-frame loop)
   - Butterfly fluttering (moving up and down)
   
3. **Scene 3** (6-8 seconds): Catches / Doesn't catch
   - Puppy stops
   - Butterfly continues flying / Puppy is happy

### Step 3: Generate Code

```bash
# Create frame directory
mkdir -p /tmp/animation_frames

# Generate SVG using Node.js (based on designed scenes)
node generate_story.js

# Convert to PNG
rsvg-convert /tmp/animation_frames/*.svg -o /tmp/animation_frames/frame_%04d.png

# Synthesize video
ffmpeg -y -framerate 12 -i /tmp/animation_frames/frame_%04d.png \
  -c:v mpeg4 -q:v 2 /tmp/story.mp4
```

### Step 4: Provide Download

Copy to nginx directory or send file path directly

## Notes

1. **ffmpeg must be installed** - `dnf install ffmpeg` or `apt install ffmpeg`
2. **rsvg-convert is required** - for SVG → PNG conversion
3. **Avoid too many frames** - exceeding 200 frames may be slow
4. **Complex stories in scenes** - do not put all actions in one frame
5. **Simple backgrounds** - complex backgrounds can affect performance

## Auxiliary Scripts

Use `scripts/animate.js` to simplify the process:

```bash
# Basic animation
node scripts/animate.js --theme "dog running" --frames 24 --output /tmp/dog.mp4

# Custom duration (seconds)
node scripts/animate.js --theme "cat stretching" --duration 2 --output /tmp/cat.mp4

# Multi-scene story
node scripts/animate.js --story "A rabbit's day" --scenes 5 --output /tmp/rabbit_day.mp4
```

## Output Formats

- **MP4**: Suitable for sharing, small file size
- **GIF**: Suitable for embedding in web pages/documents
- **Link**: Deploy to nginx for HTTP access

```bash
# Convert to GIF
ffmpeg -i input.mp4 -vf "fps=12,scale=480:-1:flags=lanczos" output.gif
```
