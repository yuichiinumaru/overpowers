---
name: frontend-web-usetts-hook
description: "React hook for handling Text-to-Speech (TTS) audio playback. Features fallback to real-time API, word boundary tracking, and lifecycle management."
tags:
  - react
  - hooks
  - tts
  - audio
version: 1.0.0
---

# useTTS React Hook

A React Hook for handling Text-to-Speech (TTS) audio playback.

### Features

1.  **Multiple Audio Source Support**:
    *   Prioritizes pre-generated static audio files (`/audio/{projectId}/{clipIndex}.mp3`).
    *   Falls back to real-time TTS API generation if static files are not found.
    *   Supports loading audio metadata for word boundary tracking.

2.  **Word Boundary Tracking**:
    *   Parses TTS metadata JSON files.
    *   Tracks the currently playing word in real-time.
    *   Supports `onWordBoundary` callbacks.

3.  **Audio Lifecycle Management**:
    *   Automatic resource cleanup.
    *   Prevents memory leaks.
    *   Automatically stops audio on component unmount.

4.  **Playback Controls**:
    *   `speak()`: Play from the beginning.
    *   `pause()`: Pause playback.
    *   `resume()`: Resume playback.
    *   `stop()`: Stop and reset to the beginning.

### Usage

```typescript
const {
  isSpeaking,
  isLoading,
  duration,
  speak,
  pause,
  resume,
  stop
} = useTTS({
  clip: currentClip,
  projectId: 'agentSaasPromoVideo',
  clipIndex: 0,
  onWordBoundary: (word) => console.log('Current word:', word),
  onEnd: () => console.log('Audio finished')
});
```

### Props

*   `clip`: The current clip object.
*   `projectId`: The project ID.
*   `clipIndex`: The clip index (used to locate audio files).
*   `onWordBoundary`: Callback function for word boundaries.
*   `onEnd`: Callback function for when audio finishes.

### Return Values

*   `isSpeaking`: Whether audio is currently playing.
*   `isLoading`: Whether audio is currently loading.
*   `duration`: The duration of the audio.
*   `alignment`: Word boundary alignment data.
*   `speak`/`pause`/`resume`/`stop`: Playback control functions.

### Audio File Structure

```
public/audio/{projectId}/
├── 0.mp3          # First audio clip
├── 0.json         # Corresponding metadata
├── 1.mp3          # Second audio clip
├── 1.json         # Corresponding metadata
└── ...
```

### Integration Notes

The Hook is integrated into the main App component and will automatically:
*   Load corresponding audio when clips change.
*   Synchronize with video playback state.
*   Clean up resources when the project changes.
*   Handle loading state display.
