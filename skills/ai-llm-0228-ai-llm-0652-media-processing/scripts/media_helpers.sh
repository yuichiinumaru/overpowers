#!/bin/bash

# Media processing helper script
# Shortcuts for common FFmpeg and ImageMagick tasks

case "$1" in
    to-mp4)
        # Convert to H.264 MP4
        ffmpeg -i "$2" -c:v libx264 -crf 23 -c:a aac -b:a 128k "$3"
        ;;
    extract-audio)
        # Extract audio to M4A
        ffmpeg -i "$2" -vn -c:a copy "$3"
        ;;
    thumbnail)
        # Extract frame at 5s as thumbnail
        ffmpeg -ss 00:00:05 -i "$2" -vframes 1 -vf scale=320:-1 "$3"
        ;;
    resize-image)
        # Resize image maintaining aspect ratio
        magick "$2" -resize "$3" "$4"
        ;;
    optimize-image)
        # Optimize image for web
        magick "$2" -strip -quality 85 "$3"
        ;;
    *)
        echo "Usage: $0 {to-mp4|extract-audio|thumbnail|resize-image|optimize-image} args..."
        echo "Examples:"
        echo "  $0 to-mp4 input.mkv output.mp4"
        echo "  $0 extract-audio video.mp4 audio.m4a"
        echo "  $0 resize-image photo.jpg 800x600 photo_small.jpg"
        exit 1
        ;;
esac
