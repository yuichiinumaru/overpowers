---
name: lu-music-player
description: "Lu Music Player - Mopidy Music Player Management Skill - Helps you manage and control the Mopidy music service on your NAS."
metadata:
  openclaw:
    category: "music"
    tags: ['music', 'audio', 'entertainment']
    version: "1.0.0"
---

# lu-music-player

Mopidy Music Player Management Skill - Helps you manage and control the Mopidy music service on your NAS.

## Description

This skill provides management functions for the Mopidy music player, including:
- Viewing playback status
- Controlling play/pause/skip
- Volume adjustment
- Scanning local music
- Viewing playlists

## Triggers

Activated when the user mentions the following keywords:
- "mopidy"
- "music player"
- "play music"
- "pause music"
- "next song"
- "volume"
- "scan music"

## Usage

### View Playback Status
```
mopidy status
music player status
what's playing
```

### Control Playback
```
play music
pause music
next song
previous song
```

### Volume Control
```
set volume to 50
volume up 10
volume down 10
mute
```

### Music Library Management
```
scan local music
refresh music library
view playlists
```

## Example Dialogues

**User**: What's the mopidy status?
**Assistant**: The Mopidy music player is running fine! Current status: idle. Visit http://192.168.3.26:6680/iris to view the web interface.

**User**: Play music
**Assistant**: Mopidy web interface opened: http://192.168.3.26:6680/iris You can select songs to play in the Iris interface.

**User**: Scan local music
**Assistant**: Please scan your local music library in the Iris interface: Settings → Local Music → Scan. Or execute the command: `docker exec mopidy mopidy local scan`

## Configuration

### Environment Variables (Optional)
```bash
MOPIDY_URL=http://192.168.3.26:6680
MOPIDY_IRIS_URL=http://192.168.3.26:6680/iris
```

### Docker Commands
```bash
# View status
docker ps | grep mopidy

# View logs
docker logs mopidy --tail 50

# Restart service
docker-compose restart mopidy

# Scan local music
docker exec mopidy mopidy local scan
```

## Access Addresses

| Service | Address |
|------|------|
| **Mopidy Iris** | http://192.168.3.26:6680/iris |
| **Mopidy HTTPS** | https://music.jesson.online:1443/iris |

## Troubleshooting

### Music Player Inaccessible
1. Check container status: `docker ps | grep mopidy`
2. View logs: `docker logs mopidy --tail 50`
3. Restart service: `docker-compose restart mopidy`

### Cannot Play Local Music
1. Ensure music files are in the `/vol1/1000/Docker/music-player/music/` directory
2. Scan in Iris interface: Settings → Local Music → Scan
3. Check file permissions: `chmod -R 777 /vol1/1000/Docker/music-player/music/`

## Author

- **Author**: jesson1222-ship-it
- **Version**: 1.0.0
- **Created**: 2026-03-08
- **License**: MIT

## Changelog

### v1.0.0 (2026-03-08)
- Initial release
- Supports Mopidy status viewing
- Supports playback control
- Supports volume adjustment
- Supports music library scanning
