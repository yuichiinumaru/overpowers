#!/bin/bash
# Helper script for ImageMagick manipulation

command=$1
input=$2
output=$3
args=${@:4}

if [ -z "$command" ] || [ -z "$input" ]; then
    echo "Usage: ./image-manipulation-helper.sh <command> <input> [output] [args...]"
    echo "Commands: dimensions, resize, identify, batch_resize"
    exit 1
fi

if ! command -v magick &> /dev/null; then
    if command -v convert &> /dev/null; then
        magick_cmd="convert"
        identify_cmd="identify"
    else
        echo "ImageMagick not found."
        exit 1
    fi
else
    magick_cmd="magick"
    identify_cmd="magick identify"
fi

case "$command" in
    dimensions)
        $identify_cmd -format "%wx%h\n" "$input"
        ;;
    resize)
        if [ -z "$output" ] || [ -z "$args" ]; then
            echo "Usage for resize: ./image-manipulation-helper.sh resize <input> <output> <dimensions (e.g., 427x240)>"
            exit 1
        fi
        $magick_cmd "$input" -resize "$args" "$output"
        ;;
    identify)
        $identify_cmd -verbose "$input"
        ;;
    batch_resize)
        if [ -z "$output" ] || [ -z "$args" ]; then
            echo "Usage for batch_resize: ./image-manipulation-helper.sh batch_resize <input_dir> <output_dir> <dimensions>"
            exit 1
        fi
        mkdir -p "$output"
        for img in "$input"/*; do
            if [ -f "$img" ]; then
                filename=$(basename "$img")
                $magick_cmd "$img" -resize "$args" "$output/$filename"
                echo "Processed $filename"
            fi
        done
        ;;
    *)
        echo "Unknown command: $command"
        exit 1
        ;;
esac
